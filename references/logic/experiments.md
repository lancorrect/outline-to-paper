# Writing logic: Experiments

Each item gives what to write and what to check.

## Overall structure and order

- What to write: The main comparison and the component ablation are always present, and the logic check focuses on these two. The other blocks are optional; when the user has such experiments, write them by the matching item in the table.

| Block | Required or optional | Item |
|---|---|---|
| Setup | Required | Setup |
| Main comparison | Required | Main comparison |
| Component ablation | Required | Component ablation |
| Focused analysis, visualization | Optional | Focused analysis and visualization |
| Efficiency | Optional | Efficiency |
| Discussion and limitations | Only when the user asks | Discussion and limitations |

- Order: By default the main comparison comes first, then the ablations and analyses. When a later method or comparison needs an analysis to explain it, that analysis can move earlier. Small, tied or unfavorable results are written in whichever block they occur.
- When the section is organized by research questions (RQs): list the RQs at the start of the section, each with the subsection that answers it, and mark the RQ number where it is answered.
- Check: Every RQ is answered by an experiment. The RQs map to components and match the components in the contributions and the method section.

## Research questions

- What to write: Each RQ asks one question that an experiment must answer.
- Check:
  - The question does not presuppose its answer: ask "How do the two retrieval methods differ on documents of different lengths?", not "Which retrieval method is most effective on long documents?".
  - When comparing the paper's method with a baseline, name both methods in the question; do not hide the baseline.
  - One RQ may be answered across two subsections.
- The phrasing of the question (opening with What or How, modeling it on sentences from top-venue papers) belongs to the writing requirements.

## Setup

- What to write:
  - Datasets: one sentence each, with the size and the number of classes, ideally also what it tests.
  - Baselines: listed in groups, with the reason for choosing them and how comparability is ensured.
  - The baselines must be convincing: you can add a variant of the base method that changes only one part, to show that the gain does not come merely from swapping that part.
  - When methods of different kinds cannot be compared directly, first state the evaluation standard.
  - Give the values of the key hyperparameters in one place. Conventions the reader needs to interpret the results go in the main text; other implementation details may go to the appendix.
- Check: The differences between the baselines are clear. The evaluation standard is stated before any results.

## Main comparison

- What to write: Give the overall conclusion first, then pick useful numbers; do not restate the table cell by cell. Each number has a job, such as showing an extreme condition, a representative condition or an exception. Numbers usually come with a reference point, typically the strongest baseline.
- Check: Each chosen number has a job you can name. The scope of the conclusion matches the table.

## How a results paragraph connects to the claim

This item applies to every results paragraph: the main comparison, the ablations and the analyses.

- What to write: The usual order is: what is compared and which table to look at; the conclusion; numbers with a reference point; the reason; the link back to the claim. First what is observed, then what it means. The link back has a clear target: an assumption from the motivation, the design purpose of a component, or an RQ number.
- Check:
  - Change one variable only, and state what is held fixed.
  - When another cause could also explain the gain, rule it out with a control, such as a random control, or replacing the baseline's own module that serves the same function.
  - Quantifiers match the table: an average gain is not a gain in every condition.
  - Every number states its model and its dataset.
  - A conclusion that follows from the logic and the numbers may be stated strongly, without added hedges (see "no over-defensive writing" in the writing requirements).

## Component ablation

- What to write: Use grouped comparisons to show what each component does: whether each helps on its own, whether combining them is better, and whether they only help in combination. Adding the components step by step also works.
- Check: Not just two rows, "full method" and "without component X". When components depend on each other and cannot be removed separately, say so.

## Focused analysis and visualization

- What to write: Four kinds of focused analysis are common: swapping the criterion, sensitivity, gains grouped by the signal, and analysis of the criterion or the routing itself. For a visualization, first describe what the figure removes and keeps, then say which component's effect this shows.
- Check: When showing that a criterion is useful, give the reference value expected when there is no pattern, such as chance level. State how the visualized examples were chosen.

## Small, tied or unfavorable results

- What to write: Report them as they are. When the gain on a dataset is small, show the value of the method from another angle, such as efficiency, and argue that it is effective overall.
- Check: Do not explain why the gain is small. The majority of conditions and the few exceptions can be contrasted in the same paragraph. Close results may be called comparable.

## Efficiency

- What to write: Gains and costs each use their own units. Report theoretical computation and measured time separately. State the measurement conditions and what each metric counts.
- Check: When computation and latency disagree, report it as it is and give the reason.

## Discussion and limitations

- What to write: Write this part only when the user asks for it. The writer and the reviser must not add it because they find a result surprising. When it is written, explain the results the user names in a separate paragraph.
- Check: Causes that have not been verified are stated as hypotheses.

## Decide before writing

Before writing, ask the user which experiments they have, and write each by the matching item above. Experiments with no matching item are written by the user.

- Which experiments there are
- Whether to organize the section by RQs
- Whether the RQ numbers go into the subsection titles or are marked only where each RQ is answered
