# Outline logic audit: the <<SECTION>> section, independent review

The main agent audits the same outline independently at the same time, and the two audits are cross-checked in the next round. Do not read the main agent's audit in `<<DIR>>/runs/` if one appears there.

All paths are relative to the project root, which is your working directory.

## Materials

- What you audit: `<<DIR>>/outline.md`, the full outline of this section, identical to the original outline.
- Context: <<CONTEXT_FILES>>. Check only how they connect to this section; do not audit them.
- Basis: the writing logic of this section, `<<DIR>>/skill/logic/<<SECTION_FILE>>.md`, and the checklist `<<DIR>>/skill/logic/outline_logic_checklist.md` (L01 to L14).
- What the user has already settled: `<<RULES_DIR>>/project_constraints.md`, `<<RULES_DIR>>/glossary.md`<<SETTLED_FILES>>. Do not raise these again unless you believe one of them is a real hard flaw; then mark it separately as "touches a settled decision" and explain why it must be raised.
- Papers: local PDFs only; do not go online. Scope: <<PAPER_DIRS>>.
- Implementation code (read only): <<CODE_DIR>>. When you cite it, say "from the code, not from the paper". If there is no code, delete this item.

## Record only two kinds of problems

- **Hard flaws**: contradictions, or one quantity with conflicting meanings; a method that does not match the challenge it is meant to address; a concept used without a definition, so that the text cannot be understood; a broken chain of reasoning, where the claimed effect does not follow from the method.
- **Missing design rationale**: a component or key design says what it does but not why, including a borrowed method without an explanation of why it fits here.

**Do not record**: the order of components or of presentation, and forward references (as long as later text explains them); claims that lack evidence or content that awaits experiments; hyperparameter values; wording and English expression; transitions the writer will add anyway. Recording these is over-defensive. If you are unsure whether something is a hard flaw, leave it out, or mention it in one sentence under "Uncertain" at the end.

## Deliverable

Write `<<DIR>>/runs/<<OUTPUT>>` in <<USER_LANGUAGE>>, the language the user reads. For each problem give:

- an ID;
- **Location**: a passage copied verbatim from outline.md that identifies the place uniquely (15 to 40 characters or words, unchanged, without ellipsis); write "global" for a problem of the whole section;
- **Grade**: hard flaw or optional;
- **Type**: hard flaw or missing design rationale, and the checklist item (for example L05);
- **Problem**: one or two sentences;
- **Basis**: reasoning, a paper (paper, section, PDF page) or code (file, line);
- **Suggested fix**: in outline form, where to change and which layer of meaning to add; no prose.

There is no minimum number of items; fewer and solid is better. Sort by grade, hard flaws first. End with three to five lines on typical cases you checked and judged not to be problems, so the next round does not argue them again. Do not change any other file. When you are done, reply "audit done" on screen.
