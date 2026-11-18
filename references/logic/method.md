# Writing logic: Method

Each item gives what to write and what to check.

## Overview paragraph

- What to write: Refer to the overview figure first. State the setting the method works in. Give one sentence per component: what it does and in which subsection. Then walk through the components along the inference flow, making clear which comes first and which feeds which.
- Check: Components are presented in whatever order explains them best, usually the flow of the method rather than importance, and need not follow the order of the challenges, so this order may differ from the introduction. The correspondence between components and challenges is stated as in the introduction. The caption of the overview figure follows the flow of the method, not the top-to-bottom layout of the figure.

## Each component

Write in this order:

1. Open with the purpose and the design rationale: refer back to the challenge it addresses, and say why it is done this way and on what basis.
2. Define here the core concepts the paper introduces; state any containment between concepts.
3. When borrowing another method, say what inspired the design and why it suits this setting.
4. Describe the procedure, with formulas for the core computations.
5. When the design rests on an assumption, state the assumption and its supporting literature first, then explain the design under it; do not present the assumption as fact.
6. Spell out the interfaces with other components, and use the same name for the same quantity throughout the paper.

Write the following two only when needed; not every component has them:

- After a formula, explain what high and low values mean, and connect them to the direction of the action.
- For a signal used across stages or components, explain that it can already be computed at that point, and why it may be used.

- Check: Go through all 14 items of the outline logic checklist (L01 to L14, `outline_logic_checklist.md`). The method paragraph of the introduction, the contributions and the method section describe the components consistently. Do not volunteer how the paper's components differ from other methods; write it only when the outline or a reviewer asks. Do not repeat what earlier text already guarantees.
