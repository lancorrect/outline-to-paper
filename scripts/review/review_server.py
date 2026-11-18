"""Local annotation page for drafts: splits a draft into paragraphs and sentences for index.html,
and stores annotations on sentences, paragraphs and the whole document.

Usage: python3 -I review_server.py <review_config.json> [--port 8765] [--root DIR] [--exit-on-submit]
  Open http://127.0.0.1:<port>/ in a browser; the server listens on this machine only.
  --root            directory that the paths in the config are relative to; default: the current directory
                    (run the server from the paper project)
  --exit-on-submit  exit after writing the files when the user clicks "Submit" or "Finalize". Start the server
                    in the background with this flag: when the process exits, the agent is notified and reads
                    the annotations.
  When the user clicks "Finalize", the annotation file has finalized: true (the readable version says so at the
  top), so the agent finalizes directly instead of producing another version.

Review config (JSON; paths relative to --root):
  draft       the draft in Markdown. The first # heading is the page title; paragraphs are separated by blank lines.
              With rich_layout, other headings, lists and tables are laid out as they are, each list item and each
              table counts as one paragraph, and tables are split into sentences cell by cell
  outline     the outline in Markdown (optional); lines are shown under the paragraphs they map to
  paragraphs  [{"match": opening text of a paragraph, "outline_lines": [line numbers]}]; paragraphs are matched
              by their opening text, not by position, so adding or removing paragraphs does not shift the others
  notes       [{"match": text inside a sentence, "kind": "question|change|style", "text": note}]: the agent's
              questions and change notes, shown as marks next to the sentence
  doc_notes   [{"kind": ..., "text": ...}]: notes on the whole document
  output      where annotations are saved (.json); on submit a readable .md with the same name is written too
  rich_layout optional; true lays out Markdown headings, lists and tables (for structured drafts such as plans or
              research summaries). Leave it out to split paragraphs the legacy way, which keeps paragraph IDs of
              drafts already under review unchanged
  base        the previous version of the draft (optional). Sentences are compared: changed sentences show the
              words added and removed, new sentences are marked as a whole, deleted sentences show struck through
  lang        language of the page and of the readable annotation file: "en" (default), "zh", or a path to a JSON
              file with the same keys as lang/en.json
Every annotation stores a snapshot of the original sentence or paragraph, so it stays readable after the draft changes.
"""
import argparse
import difflib
import hashlib
import json
import re
import sys
import threading
from datetime import datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path.cwd()
# Do not split after these abbreviations, or "et al. [x]" and "e.g. the" become two sentences
NO_SPLIT = ("e.g.", "i.e.", "et al.", "etc.", "vs.", "Fig.", "Eq.", "Sec.", "cf.")


def load_lang(spec):
    """Return (strings, warning). English is the base; another table overrides it key by key."""
    base = json.loads((HERE / "lang" / "en.json").read_text(encoding="utf-8"))
    spec = spec or "en"
    path = Path(spec) if spec.endswith(".json") else HERE / "lang" / f"{spec}.json"
    if not path.is_absolute() and spec.endswith(".json"):
        path = ROOT / path
    if not path.exists():
        return base, base["warn_lang_missing"].format(lang=spec)
    return {**base, **json.loads(path.read_text(encoding="utf-8"))}, None


def split_sentences(text):
    """English splits after . ! ? plus whitespace when the next character is an uppercase letter, [ or *;
    the abbreviations in NO_SPLIT do not split. Chinese (outline drafts) splits after 。！？, and a closing
    red-text mark == that follows goes with the sentence before it, so ==…== marked sentence by sentence stays whole.
    Nothing splits inside $...$ or $$...$$: a period inside a formula (such as \\mu=\\frac{...}{2}.) must not
    cut the formula in two, or the page cannot render it."""
    math = [m.span() for m in re.finditer(r"\$\$.+?\$\$|\$[^$]+\$", text, re.S)]
    # Cut points: (end of the previous sentence, start of the next one, whether to check English abbreviations)
    cuts = [(m.start(), m.end(), True) for m in re.finditer(r"(?<=[.!?])\s+(?=[A-Z\[*])", text)]
    cuts += [(m.end(), m.end(), False) for m in re.finditer(r"[。！？](?:==)?", text)]
    out, start = [], 0
    for end, nxt, check_abbr in sorted(cuts):
        if end <= start or any(a < end < b for a, b in math):
            continue
        head = text[start:end]
        if check_abbr and head.endswith(NO_SPLIT):
            continue
        if head.strip():
            out.append(head.strip())
        start = nxt
    tail = text[start:].strip()
    if tail:
        out.append(tail)
    return out


LIST_RE = re.compile(r"^(\s*)(\d+\.|[-*])\s+(.*)")
TABLE_SEP_RE = re.compile(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)*\|?\s*$")


def split_cells(line):
    """Split a table row into cells at |; a | inside $...$ or `...` does not split, so formulas and code stay whole."""
    s = line.strip()
    s = s[1:] if s.startswith("|") else s
    s = s[:-1] if s.endswith("|") else s
    cells, cur, in_math, in_code = [], "", False, False
    for ch in s:
        if ch == "`":
            in_code = not in_code
        elif ch == "$" and not in_code:
            in_math = not in_math
        if ch == "|" and not in_math and not in_code:
            cells.append(cur.strip())
            cur = ""
        else:
            cur += ch
    cells.append(cur.strip())
    return cells


def _structural(line):
    """List items, table rows and headings end the paragraph or list item being collected."""
    s = line.lstrip()
    return bool(LIST_RE.match(line)) or s.startswith("|") or s.startswith("#")


def parse_draft_legacy(md):
    """Legacy splitting (used when the config does not set rich_layout): returns (title, paragraphs, layout).
    Each list item (starting with 1. or -) is its own paragraph; of the headings at the start of blocks only the
    first is kept, as the document title; tables are plain paragraphs. It is kept so that paragraph IDs of drafts
    already under review stay the same and old annotations still match after the server restarts."""
    title, blocks = "", []
    for block in re.split(r"\n\s*\n", md.strip()):
        lines = [l for l in block.splitlines() if l.strip()]
        if not lines:
            continue
        if lines[0].lstrip().startswith("#"):
            title = title or lines[0].lstrip("#").strip()
            lines = lines[1:]
            if not lines:
                continue
        if re.match(r"^\s*(\d+\.|[-*])\s+", lines[0]):
            item = None
            for l in lines:
                m = re.match(r"^\s*(\d+\.|[-*])\s+(.*)", l)
                if m:
                    if item:
                        blocks.append(item)
                    item = ("item", m.group(1), m.group(2))
                elif item:
                    item = (item[0], item[1], item[2] + " " + l.strip())
            if item:
                blocks.append(item)
        else:
            blocks.append(("para", "", " ".join(l.strip() for l in lines)))
    paras = []
    for pi, (kind, marker, text) in enumerate(blocks, 1):
        sents = [{"sid": f"p{pi}s{si}", "text": s} for si, s in enumerate(split_sentences(text), 1)]
        paras.append({"pid": f"p{pi}", "kind": kind, "marker": marker, "text": text, "sentences": sents})
    return title, paras, [{"type": "para", "pid": p["pid"]} for p in paras]


def parse_draft(md, rich=False):
    """Lay out headings, lists and tables (parse_draft_rich) only when the config sets "rich_layout": true;
    otherwise use the legacy splitting."""
    return parse_draft_rich(md) if rich else parse_draft_legacy(md)


def balance_bold(sents):
    """After splitting, make the ** in each sentence pair up, so rendering sentence by sentence shows no stray
    asterisks (rich layout only). A closing ** right after a period moves back to the previous sentence; bold that
    spans several sentences gets a closing ** at each sentence end and an opening ** at the next sentence start."""
    s, opened = list(sents), False
    for k in range(len(s)):
        # Judge by cumulative parity: if bold is still open at the end of the previous sentence,
        # a ** at the start of this one is the closing mark and moves back
        if k and opened and s[k].startswith("**"):
            s[k - 1] += "**"
            s[k] = s[k][2:].lstrip()
            opened = False
        opened = opened != (s[k].count("**") % 2 == 1)
    out, carry = [], False
    for t in s:
        if carry:
            t = "**" + t
        carry = t.count("**") % 2 == 1
        if carry:
            t += "**"
        if t.strip("* "):
            out.append(t)
    return out


def parse_draft_rich(md):
    """Return (title, paragraphs, layout).
    Paragraph: {pid, kind: para|item|table, marker, text, sentences: [{sid, text}]}; list items also carry list
    (the number of their list) and indent (nesting level); tables carry table: {header, rows}, where each cell is
    the list of sids of its sentences.
    The layout lists headings and paragraphs in the original order: {type: heading, hid, level, text} or
    {type: para, pid}. The first # heading is the document title; other headings go into the layout without a pid,
    so drafts with only body paragraphs keep their old pids.
    Each list item and each table has its own pid: list items can still be annotated one by one, and tables are
    split into sentences cell by cell and annotated sentence by sentence."""
    title, blocks, list_no, prev_list = "", [], 0, False
    for block in re.split(r"\n\s*\n", md.strip()):
        lines = [l for l in block.splitlines() if l.strip()]
        i = 0
        while i < len(lines):
            line = lines[i]
            m = re.match(r"^\s*(#{1,6})\s+(.*)", line)
            if m:
                if not title:
                    title = m.group(2).strip()
                else:
                    blocks.append(("heading", len(m.group(1)), m.group(2).strip()))
                prev_list, i = False, i + 1
                continue
            if line.lstrip().startswith("|") and i + 1 < len(lines) and TABLE_SEP_RE.match(lines[i + 1]):
                header, rows, i = split_cells(line), [], i + 2
                while i < len(lines) and lines[i].lstrip().startswith("|"):
                    rows.append(split_cells(lines[i]))
                    i += 1
                blocks.append(("table", header, rows))
                prev_list = False
                continue
            m = LIST_RE.match(line)
            if m:
                # Adjacent list items separated by blank lines (a loose list) still count as one list
                if not prev_list:
                    list_no += 1
                text, i = m.group(3), i + 1
                while i < len(lines) and not _structural(lines[i]):
                    text += " " + lines[i].strip()
                    i += 1
                blocks.append(("item", m.group(2), text, list_no, len(m.group(1).expandtabs(4)) // 2))
                prev_list = True
                continue
            text, i = line.strip(), i + 1
            while i < len(lines) and not _structural(lines[i]):
                text += " " + lines[i].strip()
                i += 1
            blocks.append(("para", text))
            prev_list = False
    paras, layout, hi = [], [], 0
    for b in blocks:
        if b[0] == "heading":
            hi += 1
            layout.append({"type": "heading", "hid": f"h{hi}", "level": b[1], "text": b[2]})
            continue
        pid = f"p{len(paras) + 1}"
        sents = []

        def cut(text):
            out = []
            for s in balance_bold(split_sentences(text)):
                sents.append({"sid": f"{pid}s{len(sents) + 1}", "text": s})
                out.append(sents[-1]["sid"])
            return out

        if b[0] == "table":
            table = {"header": [cut(c) for c in b[1]], "rows": [[cut(c) for c in r] for r in b[2]]}
            text = "\n".join(" | ".join(r) for r in [b[1]] + b[2])
            paras.append({"pid": pid, "kind": "table", "marker": "", "text": text, "sentences": sents, "table": table})
        elif b[0] == "item":
            cut(b[2])
            paras.append({"pid": pid, "kind": "item", "marker": b[1], "text": b[2], "sentences": sents,
                          "list": b[3], "indent": b[4]})
        else:
            cut(b[1])
            paras.append({"pid": pid, "kind": "para", "marker": "", "text": b[1], "sentences": sents})
        layout.append({"type": "para", "pid": pid})
    return title, paras, layout


def plain(s):
    """Drop bold, the red-text mark == and citation brackets before matching, so a match works with or without them."""
    return re.sub(r"\*\*|==|\[[a-z0-9_;\s]+\]", "", s)


def diff_tokens(s):
    """Tokens for comparison: $...$ or $$...$$ counts as one token; the rest splits on whitespace, keeping it.
    Each formula then lands whole in one eq, ins or del segment, so the change view can still render it."""
    out, pos = [], 0
    for m in re.finditer(r"\$\$.+?\$\$|\$[^$]+\$", s, re.S):
        out += re.findall(r"\S+|\s+", s[pos:m.start()])
        out.append(m.group(0))
        pos = m.end()
    return out + re.findall(r"\S+|\s+", s[pos:])


def word_diff(old, new):
    """Word-level comparison returning [[eq|ins|del, text], ...]; tokens as in diff_tokens, joining gives the sentence back."""
    a, b = diff_tokens(old), diff_tokens(new)
    segs = []
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(a=a, b=b, autojunk=False).get_opcodes():
        if tag == "equal":
            segs.append(["eq", "".join(b[j1:j2])])
        else:
            if i2 > i1:
                segs.append(["del", "".join(a[i1:i2])])
            if j2 > j1:
                segs.append(["ins", "".join(b[j1:j2])])
    return segs


def mark_changes(base_md, paras, rich=False):
    """Compare every sentence of the new draft with the previous version and write the result into the sentences:
    change=changed with segments, or change=new for an added sentence. A sentence deleted from the previous version
    is attached to the sentence that follows its old position (deleted_before); sentences deleted at the very end are
    attached to the last sentence (deleted_after). Whole sentences are aligned first; inside replaced blocks,
    sentences are paired by similarity: a ratio of at least 0.4 counts as changed, otherwise one deletion plus one addition."""
    _, base_paras, _ = parse_draft(base_md, rich)
    stats = {"changed": 0, "new": 0, "deleted": 0}
    if rich:
        # A table whose header changed counts as rewritten: all its sentences are new and the old table is left out
        # of the comparison (otherwise pairing sentence by sentence would attach old cells to unrelated new cells)
        head = lambda p: p["text"].split("\n")[0]
        old_heads = {head(p) for p in base_paras if p["kind"] == "table"}
        new_heads = {head(p) for p in paras if p["kind"] == "table"}
        for p in paras:
            if p["kind"] == "table" and head(p) not in old_heads:
                p["rewritten"] = True
                for sent in p["sentences"]:
                    sent["change"] = "new"
                    stats["new"] += 1
        for p in base_paras:
            if p["kind"] == "table" and head(p) not in new_heads:
                stats["deleted"] += len(p["sentences"])
        base_paras = [p for p in base_paras if not (p["kind"] == "table" and head(p) not in new_heads)]
        paras = [p for p in paras if not p.get("rewritten")]
    old = [s["text"] for p in base_paras for s in p["sentences"]]
    new = [s for p in paras for s in p["sentences"]]
    pending_del = []

    def flush_deleted(target):
        if pending_del:
            target.setdefault("deleted_before", []).extend(pending_del)
            pending_del.clear()

    sm = difflib.SequenceMatcher(a=old, b=[s["text"] for s in new], autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            if j2 > j1:
                flush_deleted(new[j1])
            continue
        olds, used = list(range(i1, i2)), set()
        for j in range(j1, j2):
            best, score = None, 0.4
            for i in olds:
                if i in used:
                    continue
                r = difflib.SequenceMatcher(a=old[i], b=new[j]["text"], autojunk=False).ratio()
                if r >= score:
                    best, score = i, r
            # Old sentences before the paired one that are still unpaired count as deleted, keeping the original order
            if best is not None:
                for i in olds:
                    if i < best and i not in used:
                        pending_del.append(old[i])
                        used.add(i)
                        stats["deleted"] += 1
                used.add(best)
                flush_deleted(new[j])
                new[j]["change"] = "changed"
                new[j]["segments"] = word_diff(old[best], new[j]["text"])
                stats["changed"] += 1
            else:
                flush_deleted(new[j])
                new[j]["change"] = "new"
                stats["new"] += 1
        for i in olds:
            if i not in used:
                pending_del.append(old[i])
                stats["deleted"] += 1
    if pending_del and new:
        new[-1].setdefault("deleted_after", []).extend(pending_del)
    return stats


def build_doc(cfg):
    lang, lang_warn = load_lang(cfg.get("lang"))
    draft_path = ROOT / cfg["draft"]
    md = draft_path.read_text(encoding="utf-8")
    rich = bool(cfg.get("rich_layout"))
    title, paras, layout = parse_draft(md, rich)
    outline = []
    if cfg.get("outline"):
        outline = (ROOT / cfg["outline"]).read_text(encoding="utf-8").splitlines()
    warnings = [lang_warn] if lang_warn else []
    diff_stats = None
    if cfg.get("base"):
        diff_stats = mark_changes((ROOT / cfg["base"]).read_text(encoding="utf-8"), paras, rich)
    # Map paragraphs to outline lines by their opening text; mismatches go into warnings at the top of the page
    for spec in cfg.get("paragraphs", []):
        hit = [p for p in paras if plain(p["text"]).startswith(plain(spec["match"]))]
        if len(hit) != 1:
            warnings.append(lang["warn_paragraph_match"].format(n=len(hit), match=spec["match"][:40]))
            continue
        hit[0]["outline"] = [{"line": n, "text": outline[n - 1]} for n in spec["outline_lines"] if 0 < n <= len(outline)]
    # Attach the agent's questions and change notes to sentences; mismatches are reported, never dropped silently
    notes = []
    for ni, spec in enumerate(cfg.get("notes", []), 1):
        hit = [(p, s) for p in paras for s in p["sentences"] if plain(spec["match"]) in plain(s["text"])]
        if len(hit) != 1:
            warnings.append(lang["warn_note_match"].format(n=len(hit), match=spec["match"][:40]))
            continue
        p, s = hit[0]
        notes.append({"nid": f"n{ni}", "pid": p["pid"], "sid": s["sid"], "kind": spec.get("kind", "change"), "text": spec["text"]})
    return {
        "title": title or draft_path.stem,
        "draft": cfg["draft"],
        "draft_sha1": hashlib.sha1(md.encode("utf-8")).hexdigest(),
        "paragraphs": paras,
        "layout": layout,
        "rich": rich,
        "notes": notes,
        "doc_notes": cfg.get("doc_notes", []),
        "categories": lang["categories"],
        "i18n": lang,
        "warnings": warnings,
        "base": cfg.get("base"),
        "diff_stats": diff_stats,
    }


def render_md(doc, state):
    """The readable file written on submit: annotations on the whole document first, then annotations on
    paragraphs and sentences in the order of the draft."""
    L = doc["i18n"]
    out = [L["md_title"].format(title=doc["title"]), "", L["md_submitted"].format(draft=doc["draft"], time=state["submitted_at"]), ""]
    if state.get("finalized"):
        out += [L["md_finalized"], ""]
    anns = state["annotations"]

    def fmt(a):
        lines = [f"- **[{a.get('category') or L['md_uncategorized']}]**{L['md_general'] if a.get('general') else ''} {a.get('comment', '').strip()}"]
        if a.get("suggestion", "").strip():
            lines.append(L["md_suggestion"].format(text=a["suggestion"].strip()))
        if a.get("reply_to"):
            lines.append(L["md_reply"].format(nid=a["reply_to"]))
        return lines

    docs = [a for a in anns if a["target"]["type"] == "document"]
    out += [L["md_doc_heading"], ""] + (sum((fmt(a) for a in docs), []) or [L["md_none"]]) + [""]
    out += [L["md_para_heading"], ""]
    for p in doc["paragraphs"]:
        pa = [a for a in anns if a["target"].get("pid") == p["pid"]]
        if not pa:
            continue
        ref = ",".join(f"L{o['line']}" for o in p.get("outline", []))
        out.append(f"### {p['pid']}{L['md_outline_ref'].format(ref=ref) if ref else ''}")
        for a in [a for a in pa if a["target"]["type"] == "paragraph"]:
            out += [L["md_para_ann"]] + fmt(a)
        for s in p["sentences"]:
            sa = [a for a in pa if a["target"].get("sid") == s["sid"]]
            if sa:
                out += ["", f"> {s['text']}", ""]
                for a in sa:
                    out += fmt(a)
        out.append("")
    # Old annotations that no longer match the draft are listed separately and stay readable through their snapshots:
    # paragraph annotations by whether their pid exists, sentence annotations by whether their sid exists
    pids = {p["pid"] for p in doc["paragraphs"]}
    sids = {s["sid"] for p in doc["paragraphs"] for s in p["sentences"]}
    orphan = [a for a in anns
              if (a["target"]["type"] == "paragraph" and a["target"].get("pid") not in pids)
              or (a["target"]["type"] == "sentence" and a["target"].get("sid") not in sids)]
    if orphan:
        out += [L["md_orphans"], ""]
        for a in orphan:
            out += [f"> {a['target'].get('snapshot', '')}", ""] + fmt(a) + [""]
    return "\n".join(out) + "\n"


class Handler(BaseHTTPRequestHandler):
    cfg = None
    out_json = None
    exit_on_submit = False

    def log_message(self, fmt, *args):  # print only submit events, not the access log
        pass

    def _send(self, code, body, ctype="application/json; charset=utf-8"):
        data = body if isinstance(body, bytes) else json.dumps(body, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def _state(self):
        if self.out_json.exists():
            return json.loads(self.out_json.read_text(encoding="utf-8"))
        return {"annotations": [], "submitted_at": None}

    def do_GET(self):
        if self.path in ("/", "/index.html"):
            self._send(200, (HERE / "index.html").read_bytes(), "text/html; charset=utf-8")
        elif self.path == "/api/doc":
            # Re-read the draft and config on every request, so a changed draft shows after a page refresh
            self._send(200, build_doc(self.cfg))
        elif self.path == "/api/state":
            self._send(200, self._state())
        else:
            self._send(404, {"error": "not found"})

    def do_POST(self):
        if self.path not in ("/api/save", "/api/submit"):
            self._send(404, {"error": "not found"})
            return
        body = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))) or b"{}")
        doc = build_doc(self.cfg)
        state = self._state()
        state.update({
            "draft": doc["draft"],
            "draft_sha1": doc["draft_sha1"],
            "annotations": body.get("annotations", []),
            "saved_at": datetime.now().isoformat(timespec="seconds"),
        })
        if self.path == "/api/submit":
            state["submitted_at"] = state["saved_at"]
            # "Finalize" also goes through /api/submit, with finalize set; a plain submit clears an earlier finalize
            state["finalized"] = bool(body.get("finalize"))
        self.out_json.parent.mkdir(parents=True, exist_ok=True)
        self.out_json.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        if self.path == "/api/submit":
            out_md = self.out_json.with_suffix(".md")
            out_md.write_text(render_md(doc, state), encoding="utf-8")
            print(f"SUBMITTED annotations={len(state['annotations'])} finalized={int(state['finalized'])} json={self.out_json} md={out_md}", flush=True)
            # Tell the page where the files went and whether the server exits, so it can show the result
            self._send(200, {"ok": True, "submitted_at": state["submitted_at"], "count": len(state["annotations"]),
                             "finalized": state["finalized"],
                             "json": str(self.out_json.relative_to(ROOT)) if self.out_json.is_relative_to(ROOT) else str(self.out_json),
                             "exiting": self.exit_on_submit})
            if self.exit_on_submit:
                threading.Thread(target=self.server.shutdown, daemon=True).start()
            return
        self._send(200, {"ok": True, "saved_at": state["saved_at"]})


def main():
    global ROOT
    ap = argparse.ArgumentParser()
    ap.add_argument("config")
    ap.add_argument("--port", type=int, default=8765)
    ap.add_argument("--root", default=".")
    ap.add_argument("--exit-on-submit", action="store_true")
    args = ap.parse_args()
    ROOT = Path(args.root).resolve()
    cfg_path = Path(args.config).resolve()
    Handler.cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
    Handler.out_json = ROOT / Handler.cfg["output"]
    Handler.exit_on_submit = args.exit_on_submit
    doc = build_doc(Handler.cfg)  # parse once before starting, so config errors show up immediately
    for w in doc["warnings"]:
        print("WARN", w, flush=True)
    httpd = ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
    print(f"READY http://127.0.0.1:{args.port}/ paragraphs={len(doc['paragraphs'])} notes={len(doc['notes'])}", flush=True)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    sys.exit(0)


if __name__ == "__main__":
    main()
