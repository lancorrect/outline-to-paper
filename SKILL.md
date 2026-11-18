---
name: outline-to-paper
description: Write an English paper section by section from a settled outline. The skill consists mainly of writing logic and writing requirements. Writing logic says what each section contains and in what order: per-section logic, a 14-item outline logic checklist, and cross-section correspondences. Writing requirements say how to write, in two layers: general (default constraints, optional presets, formula writing, a phrasebank, ml-paper-writing's academic style) and per paper (project constraints, glossary, section glossary, check-script word lists). It also has sub-agent task sheets and two tools: a check script and a local annotation page. A writer and a reviser run as separate sub-agents; the main agent audits the outline, runs the final check and hands drafts to the user for annotation. Use when the user asks to write a section from the outline, write the next section, audit the outline logic, list what the writer needs to add, process annotations, produce the next version, or finalize a section.
---

# Outline to paper

## What this skill does

It turns an outline the user has settled into the English text of a paper, one section at a time. The outline may be in any language; the text is always English. The workflow is written for several agents; please run it that way, because a single agent has not been tested (see "How the work is split" below).

## What it consists of

It consists mainly of two parts, writing logic and writing requirements, plus task sheets for sub-agents and two tools. Each kind of file lives in its own folder; to find something, first decide which kind it is. `<skill>` below is the folder of this skill.

**Writing logic** (`references/logic/`) says what each section contains and in what order:

| File | What it covers | Who reads it, and when |
|---|---|---|
| `<section>.md` | One per section, eight in all: introduction, related work, preliminaries, method, abstract, experiments, conclusion, captions. Each says which parts the section has, what each part says and how to check it; it ends with "Decide before writing" | The main agent when auditing the outline and in the final check; the writer while writing. "Decide before writing" is asked at step 2 |
| `outline_logic_checklist.md` | The 14 criteria L01 to L14 for auditing the logic of an outline | Step 2: the main agent and the audit sub-agent |
| `cross_section.md` | Correspondences across sections, for example whether the general problem, the challenges and the components agree everywhere | Checked separately in the final check |

**Writing requirements** say how to write. The writer, the reviser and the final check all follow them at once. They come in two kinds (default constraints P2): the constraints and the glossary keep the text on topic and correct, with only the content of the outline and the right terms, claim strength and citations; ml-paper-writing keeps the expression academically sound, with Gopen and Swan's seven principles, Perez's micro-level advice, and the word-choice requirements of Lipton and Steinhardt. Where the two conflict, follow the constraints and point the conflict out to the user first (default constraints P1).

The writing requirements have two layers. The general requirements are in `references/requirements/`; every paper shares them, and they are read as they are, never edited:

| File | What it covers | Who reads it, and when |
|---|---|---|
| `default_constraints.md` | Default constraints, valid for any paper | All three |
| `presets.md` | Optional presets that depend on the venue or on personal habit | Asked one by one at the start; the enabled ones are read by all three |
| `method_formula.md` | How to write the formulas of the method section | All three, for the method section |
| `phrasebank.md` | Phrasebank | The writer and the reviser, when looking for an English phrasing |
| `ml-paper-writing/` | ml-paper-writing's academic style requirements | The writer reads all of it; the reviser reads only the sections on writing |

The per-paper requirements are templates in `references/requirements/per_paper/`; each paper copies them into its project and fills them in:

| File | What it covers | When it is made, who reads it |
|---|---|---|
| `project_constraints.md` (project constraints) | Enabled presets, wording specific to this paper, rules for individual sections, the error log | Copied into the project's rules folder at step 0 and updated after annotations; read by all three |
| `glossary.md` (glossary) | Wording for the whole paper, in two tables: proper names and terms | Copied into the project's rules folder at step 0 and extended before each section; read by all three |
| `section_glossary.md` (section glossary) | The glossary entries this section uses, matched line by line to its outline | Made for each section at step 3, in the section's work folder; sent to the writer and the reviser with their task sheets |
| `check_rules.json` (check-script word lists) | The glossary's forbidden forms and hint words, the abbreviation whitelist and the enabled presets, in a form the script can read. It is only the small part of the writing requirements a script can check; most rules are still checked by reading | Copied into the project's rules folder at step 0, changed together with the glossary; read by the check script |

This file only says how to operate; it does not copy any rule. New rules the user sets in annotations also go only into the project constraints and the glossary.

**Task sheets** are in `task_sheets/`: templates of the task sheets for sub-agents. Before each dispatch, copy one and fill in its placeholders:

| File | For whom | Step |
|---|---|---|
| `TASK_logic_audit.md` | The sub-agent that audits the outline logic; it checks the outline, not a draft | 2 |
| `TASK_supplement.md` | The sub-agent that lists what the writer needs to add | 4, when the outline needs filling in |
| `TASK_write.md` | The writer | 4 |
| `TASK_revise.md` | The reviser | 5 |

**Tools** are in `scripts/`:

- `check_draft.py`: the check script. It checks the rules tagged [script], reads the project's check-script word lists, and reports "Must fix" and "Hints".
- `review/`: the local annotation page, where the user annotates sentence by sentence, submits and finalizes. `review_config.example.json` is the sample of its config; write each config from it.

The sample of the machine settings, `config.local.json.example`, is in the root of this skill; copy it, rename it to `config.local.json` and fill it in.

## Files in the project

Locations come from the machine settings `config.local.json`. The defaults are:

- `writing/`: the per-paper requirements: `project_constraints.md`, `glossary.md`, `check_rules.json`.
- `writing/drafts/`: every version handed to the user, `<section>_v<N>.md`; its review config `<section>_v<N>_review_config.json`; the user's annotations `<section>_v<N>_review.json` and `.md`. The annotation drafts of the outline audit and of the writer supplement list go here too.
- `writing/final/`: finalized sections, `<section>.md`.
- `writing_work/<section>/`: process material, not for the user to review: `outline.md`, `references.md`, `section_glossary.md`, the task sheets, `skill/` with the copied rule files and script, and `runs/` with the sub-agents' output.

Section names are lowercase English with underscores, such as `introduction`, `related_work`, `method`, `experiments`.

**If the user has not said which section to write, do not start one.**

## How the work is split

The workflow is written for several agents: the main agent coordinates, audits the outline logic and runs the final check; the writer and the reviser are two sub-agents, each in its own session. A single agent has not been tested, and its results are not guaranteed.

**Tested combination**: the writer on GPT (through Codex) and the reviser on Claude, both as sub-agents. Test other combinations yourself.

How sub-agents are started is the user's choice at step 0: a terminal command, another skill, or the sub-agents built into the harness. Whatever the method:

- A sub-agent is a new session, with no memory and none of the main agent's context.
- Its working directory is the main agent's (the project root), and every path in a task sheet is relative to the project root.
- It reads only the files its task sheet names; the task sheet says what it must not open.
- The writer and the reviser are never the same session.
- After dispatching, watch the sub-agent in the background until it delivers; do not leave the user to watch it. When a sub-agent asks for a permission, see exactly what it will run before allowing it, and say in one line of your reply what you allowed.
- Close each sub-agent when it is done, and verify that it is closed.

## Step 0: Start (once per paper)

1. Copy `project_constraints.md`, `glossary.md` and `check_rules.json` from `references/requirements/per_paper/` into the project's rules folder. If there are no machine settings yet, create them from the sample.
2. Ask the user the following, and record the answers:
   - How sub-agents are started, and which models the writer and the reviser use: `subagent_launcher`, `writer_model`, `reviser_model` in the machine settings.
   - Which local folders of papers may be searched when auditing the outline logic, and whether there is implementation code to compare with (read only): `paper_dirs`, `code_dir` in the machine settings.
   - Whether there is a corpus of papers in the field (for finding model sentences and checking usage); leave it empty if not: `corpus_dir` in the machine settings.
   - Where the outline is: a Markdown file in the project, or an online document such as a Notion page. Record it in the project constraints.
   - How the outline marks citations, and whether a reference table exists. Record it in the project constraints.
   - Which results summary is the reference for experimental numbers (default constraints S2). Record it in the project constraints.
   - The target venue and where its author guidelines are. Record it in the project constraints.
   - Optional presets: ask about each one in `presets.md` and record the answers in the project constraints. Set the three the script checks (H, American spelling, no em dash) under `presets` in `check_rules.json` as well.
3. Review notes and the annotation page use the language of the session; do not ask about it. The page ships with English and Chinese language tables. For another language, write a table in that language from `scripts/review/lang/en.json`, put it in the project's rules folder, and point `lang` in the review config to it.

## Step 1: Gather the material (once per section)

1. **Outline**: take the original text of this section and save it as `writing_work/<section>/outline.md`. Do not change a word; only remove markup such as colors. Write its source and the export date at the top. From now on, "outline line N" means line N of this file.
2. **Reference table**: collect the outline's citation marks into `references.md` with four columns, Key, Work, Venue and Link, and state at the top that only these keys may be cited.
3. **Copy the rule files and the script** into `writing_work/<section>/skill/`: `ml-paper-writing/` (its `SKILL.md` and `references/`), `default_constraints.md`, `presets.md`, `phrasebank.md`, `logic/<section>.md`, `logic/outline_logic_checklist.md` and `check_draft.py`; for the method section, also `method_formula.md`. Do not copy the templates in `per_paper/`. The copies are read only.

## Step 2: Audit the outline logic (every section)

1. First ask "Decide before writing", the items at the end of this section's writing logic. For the experiments section, first ask the user which experiments were run; those with a matching item in the writing logic are written by it, and those without are written by the user.
2. Look for only two kinds of problems; fewer and solid is better:
   - hard flaws: contradictions or one quantity with conflicting meanings, a method that does not match the challenge it addresses, a concept used without a definition, a broken chain of reasoning;
   - missing design rationale: what is done without why, including a borrowed method without an explanation of why it fits here.
   Do not record the order of components, the order of presentation, forward references, claims awaiting experiments, hyperparameter values or wording.
3. The basis is this section's writing logic and the 14-item checklist. Decisions the user has already settled (in the project constraints and the glossary) are not raised again unless they amount to a real hard flaw; then mark them separately as "touches a settled decision".
4. The main agent and one sub-agent audit independently, then cross-check once:
   - write the sub-agent's task sheet from `task_sheets/TASK_logic_audit.md`;
   - keep the main agent's audit outside the work folder (for example in the session's temporary folder) and copy it into `runs/` only for the cross-check, so the sub-agent does not see it first;
   - in the cross-check, answer each disagreement item by item, and keep a record of withdrawn items too.
5. Use only the local paper folders in the machine settings, and search all of them; the task sheet says not to go online, except for an item the user explicitly asked to look up online. Say in your reply which folders were searched and how many papers each held.
6. For questions about how something was implemented, compare with the code in the machine settings (read only) and say "from the code, not from the paper".
7. Start an annotation page (as in step 7): the draft is a copy of the original outline, each problem sits next to its sentence with its grade (hard flaw or optional), basis, smallest fix, and what happens without a reply; withdrawn items and the audit process go at the top of the page.
8. When the user has annotated it, produce the next version from the annotations until it is final. Before changing the outline, list the changes for the user to confirm, and change only after confirmation:
   - if the outline is a local file, edit it directly;
   - if it is an online document, reread the page before editing, replace text by exact match, and mark the changes the way the project constraints say. If a match fails, the user has probably edited the page: reread it, see what the user changed, apply the approved changes to the new version without overwriting the user's edits, and tell the user. Read the page back after writing to check.

## Step 3: Prepare

- **W1**: scan this section's outline and check every word against the glossary. List for the user the pending entries this section needs and the terms the glossary lacks, with candidate forms and their basis. With a corpus, look up usage in it, filtering and trimming before reading so that whole files never enter the context. After the user confirms, write the entries into the glossary with who confirmed them, the date and the basis, and only then go on. When a forbidden form changes in the glossary, change `forbidden` in `check_rules.json` too.
- **W2**: make this section's `section_glossary.md` in its work folder from the template `references/requirements/per_paper/section_glossary.md`, listing line by line the outline fragment, its glossary ID and the English to use. Fill in the same word separately for each concept; do not unify by surface form.
- **If preset H is enabled**: count the sentences in this section's outline that state the general problem, usually 0 or 1. Call it N and put it in the task sheets and in `--however N` of the check command. Without preset H, skip the count.

## Step 4: The writer writes

### First decide whether a writer supplement list is needed

The outline logic was audited at step 2. Now decide which kind of outline this section has, tell the user the decision and the reason, and go on only after the user confirms:

- **Propositions and logic complete**: definitions, rationales and transitions are all there, and no substantive content needs approval; dispatch the writer directly. The writer still writes academic prose by ml-paper-writing and compresses repetition under default constraints B6; it does not translate sentence by sentence.
- **Needs filling in by the writer**: the outline is brief; in places it says what is done but not why, or lacks definitions or transitions, so prose cannot be written from it as it stands. Make a writer supplement list first:
  1. List the places where the writer cannot write prose from the outline and something must be added, in three tiers under default constraints B1: A, the writer may add it directly (transitions, section pointers and symbol reminders that only point back to existing propositions); B, needs the user's approval (definitional expansions, explanations of logic the outline does not state); C, settle the scope or revise the outline first (new facts, a mismatch between the outline and the implementation, a question of which section the content belongs in).
  2. The main agent and one sub-agent list independently (the sub-agent from `task_sheets/TASK_supplement.md`), then cross-check. Compare with the same section of local papers for what they write that our outline lacks.
  3. Hand the list to the user on an annotation page. Approved additions by the writer go into "Approved additions" of the writer's task sheet; approved outline revisions are made as in step 2, item 8. If the approved additions bring new terms, add them to the glossary and the section glossary before dispatching the writer.
  4. Save the final list as `writing/drafts/<section>_supplement_final.md`.

### Dispatch the writer

1. Write `writing_work/<section>/TASK_write.md` from `task_sheets/TASK_write.md` and fill in every `<<…>>` placeholder: the content order, the enabled presets, this section's rules in the project constraints, the length, N, the heading of the first line, ml-paper-writing advice to ignore as well, the approved additions ("none" if there are none), and extra rule files for this section (`method_formula.md` for the method section).
2. Start the writer sub-agent the way the user chose at step 0, and have it read the task sheet and do it.
3. It produces `runs/draft.md` and `runs/draft_notes.md`. Read parts 3 and 4 of the notes (terms the writer translated, sentences needing the user's approval) and keep them for the final check.

## Step 5: The reviser revises

1. Write `TASK_revise.md` from `task_sheets/TASK_revise.md`. The reviser does not see `draft_notes.md`; it checks the content against the outline and the constraints and revises the expression by ml-paper-writing's writing requirements.
2. Start a separate sub-agent as the reviser; it must not be the writer's session.
3. It produces `runs/revised.md` and `runs/revised_notes.md`.

## Step 6: Final check (main agent)

1. **Run the script**: `python3 -I writing_work/<section>/skill/check_draft.py writing_work/<section>/runs/revised.md --rules writing/check_rules.json --glossary writing/glossary.md --however N --refs writing_work/<section>/references.md`. Fix everything under "Must fix"; read the sentence of every hint and decide.
2. **Read the draft against the outline, sentence by sentence**:
   - content and order;
   - claim strength (B2, B3);
   - the mapping of propositions in both directions (B4), recording the repetitions merged or deleted under B6; the mapping must not turn into sentence-by-sentence translation;
   - this section's writing logic, and this section's rules in the project constraints;
   - ml-paper-writing's writing requirements: check each sentence against the Writing Style Guidelines section of ml-paper-writing's `SKILL.md`, with details in the sections Sentence-Level Clarity, Micro-Level Writing Tips and Word Choice and Precision of `references/writing-guide.md`. The points are Gopen and Swan's seven principles (subject close to verb, emphasis at the end, context first, old information before new, one idea per sentence, action in the verb, set up before new content); Perez (few pronouns, and each with its noun; verbs early; expand an awkward X's Y into the Y of X; delete fillers such as actually and very); Lipton and Steinhardt (specific words, no intensifiers, one word per concept). ml-paper-writing's advice to delete may and can is not followed; claim strength follows the outline (B3).
   Save the result as `runs/final.md` and record every change with its basis: which constraint, or which point of ml-paper-writing.
3. **Cross-section correspondences**: for sections already written that correspond to this one, check the rows of `cross_section.md` that involve this section; when all sections are written, go through the whole table once more.
4. **Formulas in the method section**: for every version, start a separate sub-agent for a read-only review: whether the formulas agree with the original papers, whether the annotations were carried out, naming and wording. Facts the user questions are also checked independently in the code by a sub-agent, with file and line.
5. **Collect what the user must decide**:
   - terms the writer translated (T3), added to the glossary as "pending";
   - sentences under B1 that need the user's approval;
   - with preset H enabled, contrasts in the outline other than the general problem;
   - conflicts between the constraints or the user's annotations and ml-paper-writing, stating what each side requires;
   - changes the main agent is unsure of.
6. **Close the writer and the reviser**, and verify that they are closed.

## Step 7: Hand over for review

1. Copy `runs/final.md` to `writing/drafts/<section>_v1.md`. **Never leave the draft in the work folder for the user to find.**
2. Write `writing/drafts/<section>_v1_review_config.json` from `scripts/review/review_config.example.json`; its `_help` says how to fill each key. The first version has no previous version, so delete `base`.
3. Start the annotation page in the background: `python3 -I <skill>/scripts/review/review_server.py writing/drafts/<section>_v1_review_config.json --root <project root> --exit-on-submit`. The default port is 8765; if it is taken, choose another with `--port`.
4. When it prints READY, fetch `http://127.0.0.1:8765/api/doc` with curl and check: `warnings` must be empty, and the number of notes must match the config.
5. Give the user the address and list what this version needs them to decide; do not write separate review notes. The "Submit", "Finalize" and "Copy all" buttons in the top bar must not be lost in any later change to the page.

## Step 8: Process the annotations (repeat until the user finalizes)

When the annotation page's process exits, the user has submitted; an exit the main agent caused itself (exit code 143) does not count. First look at `finalized` in the annotations `.json`: if it is true, the user clicked "Finalize"; make the small changes any annotations ask for and go straight to step 9 without another version. Otherwise read `<section>_v<N>_review.md` for the annotations, then two fields of the `.json`: `general` (whether "Apply from now on" was ticked) and `reply_to` (`n1` onward are notes next to sentences, `d1` onward are notes on the whole document, numbered in the order of the config).

- **"Apply from now on" ticked**: turn it into a rule. Wording goes into the glossary; anything else goes into the project constraints, with an entry in the error log; whatever the script can check also goes into `check_rules.json`. Then list for the user which rules changed.
- **Not ticked**: change only that place.
- **The user asks to discuss with another model**: put the task sheet in `writing_work/rule_<name>/`, start a sub-agent for the discussion, and write each round to a file. The outcome is only a suggestion; it enters the constraints only after the user approves.
- **The user asks a question** (for example "is whereas all right here?"): look for evidence first, with corpus usage if there is a corpus and then a dictionary online, and list the sources; answer in a `question` note on that sentence in the next version, with a recommendation and alternative wordings; do not change the text on your own.
- **An annotation overturns an existing rule or an example in a rule**: change the rule, add an entry to the error log, and record in the change log where the old rule came from and what was wrong with it.
- **Producing the next version**:
  - write `<section>_v<N+1>.md` and add `base` pointing to the previous version in the config;
  - each change note says "Per your annotation, …"; changes the main agent makes on its own are marked separately as `question` for the user to confirm;
  - every new or changed sentence goes through the ml-paper-writing checklist of step 6, not only through the constraints;
  - when a new "Apply from now on" rule is applied to sentences the user did not annotate, mark each as `question`, not as a change. When a new rule conflicts with ml-paper-writing, point it out to the user first instead of applying it across the text;
  - make changes by exact replacement in Python with assert, not with sed;
  - after the changes, run the check script, then start and check the annotation page as in step 7.
- **A round that only settled rules and needs no change to the text**: do not produce a new version; ask the user whether the section can be finalized.
- **Something asked twice without a reply**: give the default in the note and say that it will be followed without a reply.

## Step 9: Finalize

1. Copy the last version to `writing/final/<section>.md` and run the check script once more.
2. **Remind the user to bring the outline in line with the final text; do not change it on your own.** Compare the final text with the outline paragraph by paragraph and list differences in content or structure: content changed by annotations, added definitional sentences, deleted sentences, merged or split paragraphs, text turned into lists. Different English wording with the same meaning does not count. For each, give the location, the outline's original text and the suggested new text, and hand the list to the user. Change the outline only after the user approves each item, as in step 2, item 8.
3. Tell the user which files changed. If the project keeps a work log, add an entry the way the project does.

## Lessons learned

| Problem | What to do |
|---|---|
| The final draft stayed in the work folder, and the user could not review it | Always copy it to the drafts folder before starting the annotation page |
| The constraints contained a rule the user never stated | Give every rule its source; rules the main agent infers are only suggestions to the user |
| A number from the original paper was converted before being written | Copy numbers exactly from the original source; never convert them |
| A sentence the user annotated was used as a rule example, but its structure had been misread | Before using it as an example, confirm your reading with the user |
| sed changed nothing and reported no error | Use exact replacement in Python with assert |
| An escape went wrong in a heredoc, and a literal \n appeared in the file | Mind escapes when writing files with Python, and look at the end of the file afterwards |
| The final check and the next version were checked only against the constraints and missed ml-paper-writing; a new rule rewrote one sentence pattern across the text, and the user found the result too colloquial | Run the ml-paper-writing checklist in the final check and for every new version; mark a new rule applied to other sentences as `question`; raise conflicts with ml-paper-writing first |
| The outline audit searched only one paper folder and missed the others | Search every folder in the machine settings |
| An edit to the online outline failed to match because the user had edited the page | Reread the page to see what the user changed, apply the approved change to the new version, and tell the user |
| A sub-agent seemed closed but was still running | Verify after closing that it is really closed |
