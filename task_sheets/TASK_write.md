# Task: write the <<SECTION>> section of the paper

You write the <<SECTION>> section of a paper, in English, from a finalized outline. Another agent will later check your draft against the outline, so follow the outline closely and record your decisions honestly in the notes file.

All paths below are relative to the project root, which is your working directory. The folder for this task is `<<DIR>>/`.

## Inputs (read all of them before writing)

1. `<<DIR>>/outline.md`: the <<SECTION>> outline, in <<OUTLINE_LANGUAGE>>, finalized with the author. It is the only source of content.
2. `<<DIR>>/references.md`: the only references you may cite, with their keys.
3. The rules, all binding: `<<DIR>>/skill/default_constraints.md` (default constraints); the presets in `<<DIR>>/skill/presets.md` that this paper enables: <<ENABLED_PRESETS>>; `<<RULES_DIR>>/project_constraints.md` (project constraints).
4. `<<RULES_DIR>>/glossary.md`: the glossary. It is binding.
5. `<<DIR>>/section_glossary.md`: the English to use for each term in this section, line by line.
6. `<<DIR>>/skill/logic/<<SECTION_FILE>>.md`: the writing logic of this section. Organize the text by it.
7. ml-paper-writing: read the Writing Style Guidelines section of `<<DIR>>/skill/ml-paper-writing/SKILL.md` and `<<DIR>>/skill/ml-paper-writing/references/writing-guide.md` in full; read its other reference files only when its workflow for this section calls for them.
8. `<<DIR>>/skill/phrasebank.md`: the phrasebank; consult it when looking for an English phrasing.
9. <<EXTRA_INPUTS>> (for the method section: `<<DIR>>/skill/method_formula.md`, which says how to write formulas; for other sections, delete this item.)

Do not open any other file: nothing else under `<<DIR>>/`, nothing under <<WORK_DIR>>, <<DRAFTS_DIR>> or <<FINAL_DIR>>, and nothing outside the project.

## Priority when sources disagree

1. Content: only the outline. Keep its content, its claims, and its argument order: <<CONTENT_ORDER>>.
2. How to write: two sets of writing requirements, both binding for every sentence. The constraints, the glossary and the section glossary keep the text on the outline and correct (content, terms, claim strength, citations). The writing requirements of ml-paper-writing keep the expression in line with academic norms: Gopen and Swan's seven principles, Ethan Perez's micro-level tips, and the word-choice advice of Lipton and Steinhardt. Where the two conflict, the constraints win, and you list each conflict in your notes.
3. ml-paper-writing's workflow steps are not part of this task. Skip every step that would change or add content or that needs something you do not have: exploring a code repository, searching literature, confirming the contribution with the author, drafting figures, compiling LaTeX, waiting for feedback. Record the skipped steps in your notes. Ignore the skill's advice to drop hedges such as "may" or "can": the strength of every claim must match the outline (B3).<<SKILL_OVERRIDES>>

## Rules to apply while writing (details in the default constraints, the enabled presets and the project constraints)

- **Terms**: proper names exactly as in the glossary (T1); every term in the section glossary as given there (T2); terms not listed there are translated once and kept consistent, and each one is listed in your notes (T3).
- **Sentences not in the outline** follow table B1. Grammar fixes, splitting or merging sentences, neutral organizing sentences, and topic, transition or summary sentences that only point back to claims already in the outline are allowed. Definitional expansions, extra explanations, derived numbers and extra comparisons need the author's approval: you may write them, but list each one in your notes. New facts, causes, mechanisms, evaluations, capabilities or scope are not allowed. Do not drop or weaken anything the outline requires.
- **Outline fidelity is not sentence-by-sentence translation.** Apply B6: write academic prose from the outline's propositions and logic, compress repetition without losing independent information, and record each consolidation or deletion of redundant wording in your notes. Apply L10 to ordinary verbs and sentence structures while keeping technical terms fixed under T2.
- **Approved additions** (from the writer supplement list; write them only where listed, nothing beyond them): <<APPROVED_ADDITIONS>>
- **Claim strength**: compare every sentence with the outline. For example, when the outline says "hard to", do not write "cannot"; words such as "may" or "not necessarily" keep their uncertainty (B2, B3).
- **Citations**: only keys from `references.md`, written `[key]` or `[key1; key2]`, placed where the outline cites that work; you may move a citation within its sentence (L1).
- **Language**: abbreviations expanded at first use (L2); consistent tense, correct number, no overlong chains of modifiers, no sentences opening with "Regarding", and not many sentences in a row starting with "We" (L3); no bare "This shows" subjects (L5); in a list of three or more, "and" or "or" only before the last item (L7); semicolons sparingly (L8); symbols after a formula explained in a sentence starting with a lowercase "where" (L9).
- **Enabled presets**: <<PRESET_RULES>> (For example, with preset H enabled: "However" only in the sentence that states the general problem, sentence-initial, written "However, ..."; this section has <<HOWEVER_N>> such sentence(s), and every other contrast uses a connective chosen by the actual relation. Leave out presets that are not enabled.)
- **Rules for this section in the project constraints**: <<SECTION_RULES>>
- **Length**: <<LENGTH>>, not counting citation brackets.

## Self-check before you finish

Run:

`python3 -I <<DIR>>/skill/check_draft.py <<DIR>>/runs/draft.md --rules <<RULES_DIR>>/check_rules.json --glossary <<RULES_DIR>>/glossary.md --however <<HOWEVER_N>> --refs <<DIR>>/references.md`

Fix every item under "Must fix". For each item under "Hints", read the sentence and either fix it or keep it with a one-line reason in your notes. Run the script again after your fixes.

Then read the draft once more, sentence by sentence, against ml-paper-writing's writing requirements (subject close to verb, one idea per sentence, action in the verb rather than in a nominalization, old information before new, pronouns tied to a noun, no awkward X's Y, no filler words or intensifiers, specific words, one term per concept), and fix what breaks them without changing any claim or its strength.

## Output

Write exactly two files, and nothing else on disk:

- `<<DIR>>/runs/draft.md`: the <<SECTION>> in Markdown. The first line is `<<HEADING>>`. The file contains only the section text.
- `<<DIR>>/runs/draft_notes.md`, in six parts:
  1. the skill files you actually read, as paths;
  2. the skill steps you skipped, and why;
  3. terms you translated yourself (T3): the outline term, the English, the outline line;
  4. sentences that need the author's approval under B1: the sentence, its B1 category, and its basis in the outline;
  5. the final output of the check script, and how you handled each hint;
  6. places where ml-paper-writing's writing requirements conflicted with the project rules, and how you resolved each one.

When both files are written, reply with the two file paths and the word count of the <<SECTION>>.
