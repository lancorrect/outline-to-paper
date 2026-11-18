"""Check a section draft against the rules that carry a [script] or [script hint] tag.

Usage:
  python3 -I check_draft.py DRAFT.md --rules check_rules.json [--glossary glossary.md]
                            [--however N] [--refs references.md] [-o report.md]

  --rules     the project's check_rules.json: forbidden forms, hints, abbreviation whitelist,
              enabled presets, extra proper names
              (template: references/requirements/per_paper/check_rules.json)
  --glossary  the project's glossary; proper names are read from its "Proper names" table
              (the English column, several names separated by " / ", parentheses and $math$ ignored)
  --however   number of sentences in this section that state the general problem (preset H);
              default 0
  --refs      reference table with rows like "| key | ...", enables the citation check (L1)

Output has two parts:
  Must fix   breaks a confirmed rule; the exit code is 1 when there is any
  Hints      the script can only point to suspects; read the draft and decide

Rule IDs follow references/requirements/default_constraints.md and presets.md.
"""
import argparse
import json
import re
import sys
from pathlib import Path

CITE = r"\[[a-z0-9_]+(?:;\s*[a-z0-9_]+)*\]"
# Preset "american_spelling": common British spelling stems
BRIT = (r"\b(analys(e|ed|es|ing)|colours?|behaviour\w*|favour\w*|modelling|labelled|labelling|optimis\w*|recognis\w*|"
        r"emphasis(e|ed|es|ing)|characteris(e|ed|es|ing|ation)|organis\w*|utilis\w*|centre\w*|generalis\w*|summaris\w*|"
        r"prioritis\w*|minimis\w*|maximis\w*|normalis\w*|realis(e|ed|es|ing)|categoris\w*|specialis\w*|customis\w*)\b")
# L5: a bare This / These / That / It as the subject at the start of a sentence
BARE_THIS = r"^(This|These|That|It)\s+(shows?|indicates?|suggests?|demonstrates?|means?|implies|leads?|allows?|enables?|makes?|results?)\b"
# L10: ordinary verbs whose repetition within one paragraph is hinted; a project may replace this list
DEFAULT_REPEATED_VERBS = [{"label": "use", "pattern": r"\b(?:use[ds]?|using)\b"},
                          {"label": "exceed", "pattern": r"\bexceed(?:s|ed|ing)?\b"}]
DEFAULT_PRESETS = {"however": False, "american_spelling": False, "no_em_dash": False}


def sentences(text):
    """Split into sentences after dropping heading lines, Markdown bold and list markers.
    Good enough for hints: periods inside abbreviations (e.g., et al.) may split wrongly."""
    out = []
    for para in re.split(r"\n\s*\n", text):
        para = "\n".join(l for l in para.splitlines() if not l.lstrip().startswith("#"))
        para = re.sub(r"\*\*|__", "", para)
        para = re.sub(r"^\s*(\d+\.|[-*])\s+", "", para, flags=re.M)
        para = " ".join(para.split())
        if para:
            out += re.split(r"(?<=[.!?])\s+(?=[A-Z\[])", para)
    return out


def proper_names_from_glossary(path, heading="proper names", column="english"):
    """Read the first table under a heading that contains `heading`, take the column named `column`,
    and split each cell into names. Cells may hold several names separated by " / " or ";";
    text in parentheses (abbreviations, notes) and $math$ are dropped."""
    names, in_section, col = [], False, None
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if line.startswith("#"):
            if in_section and col is not None:
                break
            in_section = heading in line.lower()
            col = None
            continue
        if not in_section or not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if col is None:
            low = [c.lower() for c in cells]
            if column in low:
                col = low.index(column)
            continue
        if set(line.replace("|", "").strip()) <= set("-: "):
            continue
        cell = re.sub(r"\$[^$]*\$", " ", cells[col])
        cell = re.sub(r"\([^)]*\)|（[^）]*）", " ", cell)
        for part in re.split(r"\s/\s|;|；", cell):
            part = " ".join(part.split()).strip(" ,")
            if part and part not in names:
                names.append(part)
    return names


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("draft")
    ap.add_argument("--rules", required=True)
    ap.add_argument("--glossary")
    ap.add_argument("--however", type=int, default=0)
    ap.add_argument("--refs")
    ap.add_argument("-o", "--out")
    args = ap.parse_args()

    rules = json.loads(Path(args.rules).read_text(encoding="utf-8"))
    presets = {**DEFAULT_PRESETS, **rules.get("presets", {})}
    # Keys were renamed from "fixed names" to "proper names"; the old keys are still read, so rule files
    # written before the rename (fixed_names_from_glossary, glossary_fixed_heading, extra_fixed_names) keep working
    fixed = []
    if args.glossary and rules.get("proper_names_from_glossary", rules.get("fixed_names_from_glossary", True)):
        heading = rules.get("glossary_names_heading", rules.get("glossary_fixed_heading", "proper names"))
        fixed = proper_names_from_glossary(args.glossary, heading.lower(),
                                           rules.get("glossary_english_column", "english").lower())
    extra = rules.get("extra_proper_names", rules.get("extra_fixed_names", []))
    fixed += [n for n in extra if n not in fixed]
    abbr_ok = set(rules.get("abbreviation_whitelist", []))

    text = Path(args.draft).read_text(encoding="utf-8")
    plain = re.sub(CITE, " ", text)
    sents = sentences(plain)
    hard, hint = [], []

    # Preset no_em_dash; CJK characters always (in an English draft they are usually untranslated leftovers)
    if presets["no_em_dash"]:
        n_dash = text.count("—") + len(re.findall(r"\s--\s", text))
        if n_dash:
            hard.append(f"em dash (preset): {n_dash}")
    cjk = re.findall(r"[一-鿿]", text)
    if cjk:
        hard.append(f"CJK characters: {len(cjk)}")

    # Preset american_spelling
    if presets["american_spelling"]:
        brit = sorted(set(m.group(0) for m in re.finditer(BRIT, plain, re.I)))
        if brit:
            hard.append(f"British spelling (preset): {brit}")

    # L1 citation keys outside the reference table
    if args.refs:
        allowed = set(re.findall(r"^\| ([a-z0-9_]+) \|", Path(args.refs).read_text(encoding="utf-8"), re.M))
        keys = {k.strip() for c in re.findall(r"\[([a-z0-9_]+(?:;\s*[a-z0-9_]+)*)\]", text) for k in c.split(";")}
        bad = sorted(keys - allowed)
        if bad:
            hard.append(f"L1 citation keys not in the reference table: {bad}")

    # T1 proper names drifting: search ignoring case and treating spaces and hyphens alike; report forms
    # that differ from the confirmed one. A lowercase adjectival use may not be the proper name, so hint only
    for name in fixed:
        pat = r"\b" + r"[\s-]+".join(map(re.escape, re.split(r"[\s-]+", name))) + r"\b"
        drift = sorted(set(m.group(0) for m in re.finditer(pat, plain, re.I)) - {name})
        if drift:
            hint.append(f"T1 proper name {name!r} appears in other forms: {drift}")

    # T2 forbidden forms and project hints from check_rules.json
    for r in rules.get("forbidden", []):
        flags = re.I if r.get("ignore_case", True) else 0
        hits = sorted(set(m.group(0) for m in re.finditer(r["pattern"], plain, flags)))
        if hits:
            hard.append(f"{r['why']}: {hits}")
    for r in rules.get("hints", []):
        flags = re.I if r.get("ignore_case", True) else 0
        n = len(re.findall(r["pattern"], plain, flags))
        if n:
            hint.append(f"{r['why']}: {n} occurrence(s)")

    # L10 only locates ordinary verbs repeated within a paragraph; no global count limit, no forced synonyms.
    # Tables are not running text; read the hit and decide, terms still follow T2
    verbs = rules.get("repeated_verbs", DEFAULT_REPEATED_VERBS)
    for para in re.split(r"\n\s*\n|\n(?=\s*(?:[-*]|\d+\.)\s+)", plain):
        if para.lstrip().startswith(("#", "|")):
            continue
        repeated = [v["label"] for v in verbs if len(re.findall(v["pattern"], para, re.I)) > 1]
        if repeated:
            hint.append(f"L10 ordinary verb repeated within a paragraph {repeated}; consider another action or "
                        f"sentence pattern, but do not replace fixed terms: {para.strip()[:90]!r}")

    # Preset H: a however inside a sentence, or a sentence-initial one without a comma, breaks the rule;
    # sentence-initial ones are listed to compare with the general-problem sentences of the section
    if presets["however"]:
        initial = []
        for s in sents:
            for m in re.finditer(r"\bhowever\b", s, re.I):
                if m.start() == 0 and s[m.end():m.end() + 1] == ",":
                    initial.append(s)
                else:
                    hard.append(f"H However not at the start of the sentence, or not followed by a comma: {s[:90]!r}")
        if len(initial) > args.however:
            hard.append(f"H {len(initial)} sentence-initial However, only {args.however} allowed in this section")
        for s in initial:
            hint.append(f"H sentence-initial However; check that it is in an allowed position (the general-problem "
                        f"sentence; in related work, the last paragraph of a subsection): {s[:90]!r}")

    # L2 an abbreviation at its first appearance is not inside parentheses. It may have been spelled out
    # in an earlier section, so hint only
    seen = set()
    for m in re.finditer(r"\b[A-Z][A-Z0-9]{1,}s?\b", plain):
        abbr = m.group(0).rstrip("s")
        if abbr in seen or abbr in abbr_ok or not re.search(r"[A-Z].*[A-Z]", abbr):
            continue
        seen.add(abbr)
        if plain[max(0, m.start() - 1)] != "(":
            hint.append(f"L2 abbreviation {abbr} not spelled out at its first appearance (ignore if spelled out earlier)")

    # L7 the same conjunction (and / or) twice within one segment (between commas, semicolons, colons,
    # parentheses or the end of the sentence): possibly a list of three or more without commas. Hint only:
    # it also fires on legal structures such as between A and B followed by a coordinated predicate
    for s in sents:
        if re.search(r"\b(and|or)\b[^,.;:!?()]*\b\1\b", s, re.I):
            hint.append(f"L7 and or or appears twice in one segment; check for a list of three or more without "
                        f"commas: {s[:90]!r}")

    # L8 semicolons sparingly: every sentence with a semicolon is hinted
    for s in sents:
        if ";" in re.sub(r"\[[^\]]*\]", "", s):
            hint.append(f"L8 semicolon; check whether to split the sentence or use a comma and a conjunction: {s[:90]!r}")

    # L9 the paragraph right after a display formula starts with Here: explaining symbols starts with a lowercase
    # where; the formula before where ends with a comma. Other "Here, $" are hints only; query boxes are not formulas
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    for prev, para in zip(paras, paras[1:]):
        if para.startswith("Here") and prev.startswith("$$"):
            hard.append(f"L9 explain the symbols of a formula with where, not Here: {para[:90]!r}")
        elif para.startswith("where") and prev.startswith("$$") and not re.sub(r"(\\end\{\w+\}\s*)+$", "", prev.rstrip("$").rstrip()).rstrip().endswith(","):
            # a trailing \end{aligned} or \end{cases} does not count; look at the punctuation before it
            hard.append(f"L9 a formula followed by where must end with a comma: {prev.rstrip('$').rstrip()[-60:]!r}")
        elif para.startswith("Here, $"):
            hint.append(f"L9 paragraph starts with Here, $; if it explains symbols of the formula above, use where "
                        f"(placeholders in a query box take The placeholder): {para[:90]!r}")

    # L3 / L5 sentence openings
    for s in sents:
        if re.match(r"(Regarding|As for|With regard to)\b", s):
            hint.append(f"L3 opens with Regarding / As for: {s[:90]!r}")
        if re.match(BARE_THIS, s):
            hint.append(f"L5 unclear reference at the start of the sentence: {s[:90]!r}")
    run = 0
    for s in sents:
        run = run + 1 if re.match(r"We\b", s) else 0
        if run == 3:
            hint.append(f"L3 three sentences in a row open with We, starting here: {s[:90]!r}")

    on = [k for k, v in presets.items() if v]
    out = [f"# Script check: {Path(args.draft).name}", "",
           f"{len(sents)} sentences, {args.however} However allowed, presets enabled: {on or 'none'}", "",
           "## Must fix", ""] + [f"- {x}" for x in hard or ["none"]] + ["", "## Hints (read and decide)", ""] + \
          [f"- {x}" for x in hint or ["none"]]
    report = "\n".join(out) + "\n"
    if args.out:
        Path(args.out).write_text(report, encoding="utf-8")
    print(report)
    sys.exit(1 if hard else 0)


if __name__ == "__main__":
    main()
