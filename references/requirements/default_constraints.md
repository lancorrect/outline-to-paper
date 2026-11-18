# Default constraints

Every paper follows these rules. The writer, the reviser and the final check all apply them. The tag after each rule says how it is checked: [script] means the check script finds it; [reading] means someone has to read the draft; a script hint only points to suspects that still need reading.

## 1 Priority

- **P1 Content follows only the outline.** For how to write, the default constraints, the project constraints and the glossary take precedence over ml-paper-writing. When they conflict, follow the constraints, record the conflict in the process notes or the review notes, and point it out to the user first instead of extending it on your own. For example, ml-paper-writing suggests deleting words such as may and can; do not do this, because the strength of a claim follows the outline (B3).
- **P2 Follow both kinds of requirements at once.** The constraints and the glossary keep the text on topic and correct (content, terms, strength of claims, citations); ml-paper-writing keeps the expression academically sound (the seven principles of Gopen and Swan, the micro-level advice of Perez, the word-choice requirements of Lipton and Steinhardt).

## 2 Before writing

- **W1 Check the glossary first.** Scan the outline of the section and check every proper name, every recurring term and every word that is easily confused in the field against the glossary. Use confirmed entries as they are. Ask the user about pending entries this section needs before dispatching the work, and write them into the glossary once confirmed. The version given to the writer has no pending entries.
- **W2 Make the section glossary.** The same word in the outline may stand for different concepts. Mark each occurrence with its glossary ID, by concept, and send it with the task sheet; do not replace words uniformly by their surface form.

## 3 Wording

- **T1 Write proper names exactly as given**, including capitalization and abbreviations; the list is in the "Proper names" table of the glossary. [script]
- **T2 Write terms as the glossary gives them.** The forms in the "forbidden forms" column must not appear [script]; synonyms outside the "allowed variants" are not allowed either [reading].
- **T3 Words not in the glossary are translated by the writer, with one translation per concept throughout the paper.** The writer lists newly translated terms in the process notes; the final check adds them to the glossary, marked "pending" for the user to review.

## 4 Sentences beyond the outline

**B1 Handle added or rewritten sentences by this table.**

| Kind of addition or rewrite | Handling | Condition |
|---|---|---|
| Grammatical completion such as articles, number, a necessary subject | Allowed | Only makes an existing proposition grammatical; does not change participants, quantity or certainty |
| Splitting, merging or reordering sentences of the same proposition, non-technical paraphrase | Allowed | All atomic propositions and their dependencies are kept; fixed terms are not replaced |
| Compressing or deleting expressions that only repeat existing information | Allowed | Keep independent information and logic as in B6, record the grounds for merging or deleting repetition, and do not translate the whole text sentence by sentence |
| Neutral organizing sentences, true section signposts | Allowed | Only describe the structure of the text; add no contribution, effect, necessity or evaluation |
| Topic, transition and summary sentences | Allowed with conditions | Only refer back to propositions already in the outline; add no causation, universal generalization, superiority, research gap or strength |
| Definitional elaboration, explanation of logic the outline leaves implicit | Needs user approval | The writer may write it, but lists each sentence and its basis in the process notes |
| Derived numbers, extra comparisons, new propositions supported by added citations | Needs user approval | Same as above, and state the derivation |
| New facts, causes, mechanisms, evaluations, capabilities or scope | Forbidden | If truly needed, change the outline first |
| Deleting or weakening independent information the outline requires | Forbidden | Counts as a substantive change, like strengthening; deleting repeated expressions is not deleting independent information and follows B6 |

The reviser neither deletes nor passes sentences that need user approval: it keeps them as they are and marks them. The final check asks the user about all of them together; without approval they stay out of the final draft.

- **B2 Invariants under rewriting.** Neither revision nor polishing may change: facts, negation, modality, quantifiers, scope, assumptions, direction of comparison, causation, attribution, aggregation, numbers, formulas, citations. [reading]
- **B3 Compare the strength of each sentence with the outline; do not rely on a substitution list.** For example, when the outline says "hard to", the English must not say "cannot". Word pairs such as never and rare, or eliminate and alleviate, change the meaning, so there is no automatic substitution list. [reading]
- **B4 Map the draft and the outline in both directions.** In the final check, mark every sentence of the draft with the outline proposition it corresponds to, or with the kind in the B1 table it belongs to. Then check the other way: every independent proposition of the outline has a counterpart in the draft, so nothing is left out. The mapping works by proposition and does not require the same number of sentences or paragraphs or the same phrasing; repeated content may be mapped together, recorded as in B6. Content the user explicitly asked to delete is recorded by the annotation and not forced back in. A sentence that fits no kind in the B1 table means the table lacks a kind: ask the user, then extend the table. [reading]
- **B5 No over-defensive writing.** A conclusion may be written as long as it follows from the logic and the experimental results; when the results are clear, the wording may be strong. Only real logical errors are unacceptable, for example a conclusion that disagrees with the numbers in a table, or a wrong object or condition of comparison. When the writer, the reviser or the final check suggests wording, it does not add hedges or qualifications the outline does not have, and does not question sentence by sentence whether the wording goes beyond the evidence. The final check focuses on numbers: whether the writer invented any, whether derived differences, averages and ratios are right, and whether they agree with the results summary named in the project constraints. The strength of claims still follows the outline, as in B3. [reading]
- **B6 Write the text from the outline; do not translate it sentence by sentence.** The outline states the propositions and the logic; the text organizes the expression by ml-paper-writing and the writing logic of this skill. The writer, the reviser and the final check all judge which sentences only repeat information already kept, merge or delete such repetition, and shorten empty organizing phrases; do not copy redundancy to keep the original number of sentences. Compression must not change or lose independent facts, conditions, objects of comparison, causation, strength of claims, numbers or citations, and must not add explanations in the name of brevity. Record where text was deleted or changed and what it came from; independent content the user explicitly asked to delete is recorded by the annotation. [reading]

## 5 Language and format

- **L1 Cite only keys in the reference table**, placed where the outline cites the work; they may move within the sentence. [script]
- **L2 Spell out an abbreviation the first time it appears.** [script hint]
- **L3 Fix the problems common when the outline is not in English**: inconsistent tense, wrong number, overlong chains of noun modifiers (for example a chain of "的" in Chinese turned into the X of the Y of the Z), sentences opening with Regarding X or As for X, every sentence opening with We. [reading]
- **L4 Prefer verbs to nominalizations**: write select tokens, not perform the selection of tokens. [reading]
- **L5 Make references explicit**: do not use a bare This as the subject (as in This shows that …); say what this refers to. [script hint]
- **L6 Treat lists of clichés, AI-sounding words and sentence length as hints only.** When one is hit, look at the context; a technically sound use may stay, with the reason recorded in the process notes. [script hint]
- **L7 In a list of words, put and or or only before the last item.** When three or more words or phrases are joined by and or or, separate the earlier items with commas and put and or or only before the last one; never write A and B and C or A or B or C. A comma before the final and or or is optional, but be consistent throughout the paper. Items that share a head noun count as separate items: rule-based, statistical, and neural methods is a list of three. Alternating words for "and" in the outline do not signal nested levels. Lists of only two items (including between A and B), coordinated predicates and coordinated clauses are not covered by this rule; for example, The method retrieves passages and reranks them by relevance needs no comma. [script hint, reading]
- **L8 Use semicolons sparingly, unless you are sure.** When two clauses can be split into two sentences, or joined by a comma and a conjunction (and, so, while and so on), do not use a semicolon. [script hint, reading]
- **L9 A sentence that explains the symbols of a formula starts with a lowercase where, not Here.** For example: where $\kappa_0$, $\eta$, $x_0$, and $\gamma$ are positive constants. Start where at the left margin: in Markdown drafts it begins a new paragraph with a lowercase letter; in LaTeX, leave no blank line between the formula and where, so it is not indented. Since where continues the sentence that contains the formula, a formula followed by where ends with a comma, not a period. Query boxes and prompt boxes are not formulas: to explain their placeholders, do not use where; write The placeholder(s) …. [script]
- **L10 Vary ordinary expressions; do not mechanically reuse the same verb or sentence pattern.** Not every "use" becomes use, and "exceed" need not appear again and again; choose how to express actions, results and comparisons by their meaning, and restructure the sentence when needed rather than just swapping synonyms. Fixed names and technical concepts stay consistent by T1 and T2: do not change terms to avoid repetition, and set no arbitrary frequency limit. [reading; the script only hints at repetition within a paragraph]

## 6 Sections

- **S1 Related work: keep the wording prior work uses for itself.** If a prior method calls itself pruning, write pruning; for the paper's own method, still follow the paper's glossary. [reading]
- **S2 Experiments: every number traces back to the original results**, with the results summary named in the project constraints as the reference; state the denominator and the aggregation, for example the full set or a subset. [reading]
- **S3 Experiments: research questions open with What or How.** [reading]
- **S4 Experiments: when drafting a research question, first find sentences from top-venue papers that pose the same kind of experimental question and model it on them, recording in the process notes which paper and sentence it follows.** Do this when a corpus is available; otherwise skip it. [reading]
- **S5 The conclusion is written in the simple present.** [reading]
- **S6 The first sentence of a table caption is a noun phrase**, saying what is compared and on which model or dataset. [reading]

## 7 Final check and the error log

- **E1 Check again after every change.** Any change invalidates earlier checks: on the final draft, rerun every [script] item and read every [reading] item again.
- **E2 Error log.** Each time the user corrects an error, record the wrong form, the right form, the context it applies to and the date. Corrections of terms go into the glossary; the others go into the error log at the end of the project constraints, and the corresponding rule is added to the body of the project constraints.
