# Task: revise the <<SECTION>> draft against the outline

Another model wrote an English <<SECTION>> draft from a finalized outline. Your job is to check that draft against two sets of requirements and to fix what does not follow them: the outline and this paper's writing rules, which keep the text on topic and correct, and the writing requirements of ml-paper-writing, which keep the expression in line with academic norms. You are not rewriting the draft from scratch.

All paths below are relative to the project root, which is your working directory. The folder for this task is `<<DIR>>/`.

## Inputs (read all of them)

1. `<<DIR>>/outline.md`: the <<SECTION>> outline, in <<OUTLINE_LANGUAGE>>, finalized with the author. It is the only source of content.
2. `<<DIR>>/references.md`: the only references the draft may cite.
3. The rules: `<<DIR>>/skill/default_constraints.md`; the presets in `<<DIR>>/skill/presets.md` that this paper enables: <<ENABLED_PRESETS>>; `<<RULES_DIR>>/project_constraints.md`.
4. `<<RULES_DIR>>/glossary.md`: the glossary.
5. `<<DIR>>/section_glossary.md`: the English to use for each term in this section, line by line.
6. `<<DIR>>/runs/draft.md`: the draft.
7. The writing requirements of ml-paper-writing: the Writing Style Guidelines section of `<<DIR>>/skill/ml-paper-writing/SKILL.md`, and the sections Sentence-Level Clarity, Micro-Level Writing Tips and Word Choice and Precision of `<<DIR>>/skill/ml-paper-writing/references/writing-guide.md`. Read only these parts; ml-paper-writing's workflow steps are not part of this task.
8. `<<DIR>>/skill/phrasebank.md`: the phrasebank; consult it when looking for an English phrasing.
9. <<EXTRA_INPUTS>> (for the method section: `<<DIR>>/skill/method_formula.md`; for other sections, delete this item.)

Do not open the writer's notes (`<<DIR>>/runs/draft_notes.md`) or any other file under `<<DIR>>/` beyond the inputs above. You should judge the draft only against the outline and the rules, not against the writer's own account of it.

## What to do

Go through the draft sentence by sentence against the outline.

- A sentence that adds a fact, cause, mechanism, evaluation, capability or scope the outline does not have: delete it, or cut it back to what the outline says (B1).
- A sentence that states something more strongly or more weakly than the outline (for example "cannot" where the outline says "hard to", or a lost "may" or "not necessarily"): bring it back to the outline's strength (B2, B3).
- Independent content the outline has but the draft dropped or garbled: restore it, in the outline's logical order. Do not restore duplicate wording already represented elsewhere or content explicitly deleted by the author (B4, B6).
- A sentence in the B1 categories that need the author's approval (definitional expansion, an explanation the outline does not state, a derived number, an extra comparison): do not delete it and do not approve it. Leave it as it is and list it in your notes under "needs author approval".
- Terms: every term must match the section glossary and the glossary; proper names must match exactly. Fix any drift.
- Citations that are missing, misplaced or not in `references.md`: fix them.
- Enabled presets: <<PRESET_RULES>> Fix any violation.
- The rules for this section in the project constraints: fix any violation.
- Expression: a sentence that breaks ml-paper-writing's writing requirements (subject far from its verb, two ideas in one sentence, a nominalization where a verb would do, context placed after new information, a pronoun without a clear noun, an awkward X's Y, filler words or intensifiers, vague words, the same word repeated within a sentence, different terms for one concept): rewrite it with the smallest change that fixes it, keeping every claim, its strength and its citations (B2, B3). Where ml-paper-writing conflicts with the project rules (for example, its advice to drop "may" and "can"), follow the project rules and note the conflict.
- Repetition: identify literal translation that repeats information already preserved. Consolidate or cut redundant wording under B6, record the source propositions, and apply L10 to ordinary verbs and sentence structures without varying fixed technical terms.

Leave every sentence that meets both sets of requirements exactly as it is. Do not reorder paragraphs that already follow the outline, and do not merge or split sentences unless a fix requires it.

## Mapping check

After your fixes, check both directions (B4):

- every sentence of the revised draft maps to an outline line or to a B1 category;
- every independent claim in the outline appears in the revised draft; consolidated duplicate wording shares that mapping, and explicit deletions requested by the author are recorded rather than restored.

Report any sentence you could not map.

## Self-check

Run:

`python3 -I <<DIR>>/skill/check_draft.py <<DIR>>/runs/revised.md --rules <<RULES_DIR>>/check_rules.json --glossary <<RULES_DIR>>/glossary.md --however <<HOWEVER_N>> --refs <<DIR>>/references.md`

Fix every item under "Must fix". For each item under "Hints", fix it or keep it with a one-line reason. Run the script again after your fixes.

## Output

Write exactly two files, and nothing else on disk:

- `<<DIR>>/runs/revised.md`: the revised <<SECTION>> in Markdown. The first line is `<<HEADING>>`. The file contains only the section text.
- `<<DIR>>/runs/revised_notes.md`, in four parts:
  1. every change you made, one entry per change, in draft order: the original text (or "inserted"), the revised text (or "deleted"), and the reason, naming the outline line, the rule ID or the ml-paper-writing principle; end with the total number of changes;
  2. needs author approval: each sentence, its B1 category, and its basis;
  3. the result of the mapping check;
  4. the final output of the check script, and how you handled each hint.

When both files are written, reply with the two file paths, the number of changes and the word count of the revised <<SECTION>>.
