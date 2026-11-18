# <<Paper title>>: project constraints

- These are this paper's own rules, kept together with the glossary. The default constraints of outline-to-paper apply to every paper and are not copied here; this file records which presets are enabled, the wording rules specific to this paper, and the rules for individual sections.
- Where a rule here conflicts with a default constraint, this file wins; record in the change log which default rule it overrides.
- End every rule with its source, such as [user 2026-11-18]. Rules the main agent inferred on its own do not go here; propose them to the user as suggestions.
- Number the rules PR1, PR2 and so on through the whole file, so they do not clash with the IDs of the default constraints.
- Rules the script can check also go into check_rules.json as word lists; when you change one, change the other.

## 1 Project information

| Item | What to record |
|---|---|
| Outline | Where it is: a file path inside the project, or the page name and link of an online document; the language of the outline |
| Citations | The format of the citation marks in the outline; where the reference table comes from |
| Experimental numbers | Which results summary is the reference (default constraints S2) |
| Target venue | Its name; where the author guidelines are; the caption format (for example whether "Fig." is bold, or the punctuation after the number) follows the guidelines |
| Marking outline edits | How changes are marked when the online outline is edited (for example red text) |

## 2 Enabled presets

| Preset | Enabled | Source |
|---|---|---|
| H: only the sentence that states the general problem may use However | <<yes / no>> | <<[user date]>> |
| American spelling | <<yes / no>> | <<[user date]>> |
| No em dash | <<yes / no>> | <<[user date]>> |
| Format of the contribution list | <<yes / no>> | <<[user date]>> |
| Borrowed methods written as inspired by | <<yes / no>> | <<[user date]>> |

The script checks the first three; set the same values under presets in check_rules.json and keep the two in step.

## 3 Wording specific to this paper

Rules on wording that only this paper has, for example how one word must always be written or which two quantities must never be swapped. How a single entry is written belongs in the glossary; this section holds rules that span entries.

- PR1 <<rule>>. <<[user date]>>

## 4 Rules for individual sections

List this paper's rules for each section under its heading; leave a heading empty if there are none.

### Introduction

- PR<<n>> <<rule>>. <<[user date]>>

### Related work

### Preliminaries

### Method

### Experiments

### Conclusion

### Abstract

### Captions

## 5 Pending decisions

Matters to settle when the corresponding sentence is written.

## 6 Error log (default constraints E2)

| Date | Wrong form | Right form | Context | Rule |
|---|---|---|---|---|

Corrections of terms go straight into the glossary, not here.

## 7 Change log

- <<date>>: what changed and why.
