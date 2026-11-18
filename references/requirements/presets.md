# Optional presets

These rules depend on the venue or on personal habit; they are not general norms. At the start of a new project, ask the user about each one, and record the ones enabled in the project constraints. Each preset states what the check script looks for once it is enabled.

## 1 Language and format

- **H Only a sentence that states the general problem may use However.** When enabled, it covers the five points below, plus a note and what the script checks:
  - However must open the sentence and stand on its own, written as "However, …". If the outline of a section has no sentence stating the general problem, do not use However there. Other "however" in the outline that do not state the general problem are not written as However; the final check lists them for the user. [position checked by script; whether it states the general problem checked by reading]
  - Do not use However for the limitations of prior methods; use Although, While, but, yet, whereas and so on, according to the actual logical relation. [reading]
  - A limitation may be joined to the sentence describing the method with a comma and yet, but or whereas, or given its own sentence, whichever reads better. For example: Method A selects tokens by attention, yet it applies the same ratio to every input. [reading]
  - There is no limit on the number of However, and do not mechanically replace it with nevertheless or nonetheless; choose the word by whether the relation is concession, contrast or a turn. [reading]
  - In related work, However appears only in the last paragraph of each subsection; elsewhere in the subsection, use another connective that fits the actual logical relation. [reading]
  - Note: top-venue papers mostly use However to introduce the limitations of prior work. This rule is stricter than common practice; it is a personal writing standard, not a rule of English grammar.
  - Script: find every however in the text (including ", however,") and check the count against the number of general-problem sentences the user gives.
- **American spelling instead of British.** Script: looks for common British spelling stems (analyse, colour, modelling, optimise and so on).
- **No em dash.** Script: looks for the em dash character.

## 2 Sections

- **Format of the contribution list.** Every item except the last one (the experiments) opens with We. Each component gets one item of about two sentences: what was proposed and which challenge it solves, a brief note on how, and the advantage this brings. Vary the sentence patterns and verbs across items; the second sentence may take the component as its subject. Component items carry no experimental results, and the contributions give no specific numbers. [reading]
- **Write borrowed methods as inspired by**, not as used or adopted directly. This applies when the borrowed method has been modified; when it is reused unchanged, following or we adopt is more accurate. [reading]
