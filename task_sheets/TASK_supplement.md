# Writer supplement list: the <<SECTION>> section, independent list

## Background

The logic of this section's outline has been audited, and the fixes are in the outline. Next, the outline will be written as English prose. The outline is brief, and in some places a writer following it could not produce prose. This round lists **what the writer needs to add, and who decides**. The main agent writes its own list independently at the same time, and the two are cross-checked in the next round. **Do not read the main agent's list in `<<DIR>>/runs/`.**

All paths are relative to the project root, which is your working directory.

## Materials

- Outline: `<<DIR>>/outline.md`. For context, see <<CONTEXT_FILES>>.
- Rules: `<<DIR>>/skill/default_constraints.md`, above all table B1 (what may be added, what needs the user's approval, what is not allowed); the rules for this section in `<<RULES_DIR>>/project_constraints.md`; `<<RULES_DIR>>/glossary.md`; what the user has decided not to write: <<SETTLED_FILES>>.
- The writing logic of this section: `<<DIR>>/skill/logic/<<SECTION_FILE>>.md`.
- ml-paper-writing: `<<DIR>>/skill/ml-paper-writing/SKILL.md` and its `references/`; read only the parts about this section.
- Papers: the same section in papers of the same field under <<PAPER_DIRS>>. Look for what they write that our outline lacks, for example the description of an overview figure, an algorithm box, which section holds implementation details, or a complexity analysis. **Local PDFs only; do not go online.**
- Implementation code (read only): <<CODE_DIR>>, to check that the definitions in the outline match the implementation. When you cite it, say "from the code, not from the paper". If there is no code, delete this item.

## Do not record

Logic problems already fixed, wording and English expression, claims that await experiments, and the values of hyperparameters (but do record where a hyperparameter should be introduced). Do not be over-defensive; fewer and solid is better.

## For each item

- an ID;
- **Location**: a passage copied verbatim from outline.md that identifies the place uniquely (10 to 40 characters or words, unchanged); write "whole section" for an item that concerns the whole section;
- **Tier**:
  - A, the writer may add it directly: transitions, section pointers, symbol reminders and the like that only point back to propositions already in the outline;
  - B, needs the user's approval: definitional expansions, explanations of logic the outline does not state;
  - C, settle the scope or revise the outline first: new facts, a mismatch between the outline and the implementation, a question of which section the content belongs in;
- **Problem**: one or two sentences;
- **Basis**: a rule ID, a paper (paper, section, PDF page) or code (file, line);
- **Suggestion**: who decides, and the default handling.

## Deliverable

Write `<<DIR>>/runs/<<OUTPUT>>` in <<USER_LANGUAGE>>, the language the user reads, sorted C, B, A. End with three to five lines on typical cases you checked and judged to need no addition. Do not change any other file. When you are done, reply "supplement done" on screen.
