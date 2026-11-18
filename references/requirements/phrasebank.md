# Phrasebank

The writer and the reviser consult this when looking for an English phrasing. The patterns are frames abstracted from sentences in top-venue papers; they are not quotations. Fill the brackets only from the outline and the experimental results of the paper; do not transplant facts from other papers. For However, a bare This as subject, semicolons and the word for a sample, still follow the default constraints, the enabled presets and the glossary.

## 1 Abstract

Expression:

- **Tense**: background, method and results mostly use the simple present; progress in the background often uses the present perfect. Recalling work already done, or giving specific comparison numbers, may use the past.
- **Subjects**: alternate between the objects of the field, prior work, we, the method name and Experiments; the method name can also sit in an object clause, with Experimental results as the subject of the main clause.
- **Common connectives**: turns with but, yet, However; responses with To address this limitation, To bridge this gap, To this end; elaboration with Specifically, In particular; addition with Additionally, Furthermore, Besides; examples with Notably, For instance. With the However preset enabled, However is reserved for the general-problem sentence.
- **Abbreviation load**: an abstract usually introduces zero or one new abbreviation of its own; introducing several in one sentence that never appear again burdens the reader. Treat abbreviations of the field and new names coined by the paper separately.
- **Do not copy the flaws of a model sentence**: when following a sentence, do not also copy its errors in number, spelling or capitalization.

Patterns:

1. Progress, then a turn: `[Models] show promise for [task] but often remain [problem] because [cause].`
2. Two lines of prior work: `While [line 1] is effective, it is usually costly …. [Line 2] provide(s) a practical alternative, but they [defect], which [consequence].`
3. Criticizing one-size-fits-all treatment: `… is fixed and applied uniformly to all [inputs], failing to [consequence].`
4. Challenges after a colon: `Specifically, [models] encounter two main issues in [stage]: they [problem 1], leading to [consequence 1], and they [problem 2], which [consequence 2].`
5. Challenge and solution in the same sentence: `We address three key challenges: First, we tackle [challenge 1] by [solution 1]. Second, we resolve [challenge 2] by [solution 2]. Third, we improve [aspect] by [solution 3].`
6. Overview, then each item: `Our framework is built on three key components. First, we propose [C1] ([abbr]), a [type] that …. Second, we introduce [C2] ….`
7. From signal to decision: `Specifically, [method] quantifies [signal], and then projects this signal to [decision].`
8. Decoupling: `By decoupling [A] and [B], we can [effect], enabling [benefit].`
9. Overall results: `Experiments on [n] [models] and [m] datasets show that [method] consistently outperforms [baselines].`

## 2 Experiments

Each pattern notes the kind of result it depends on; use it only when you have that result. When the results are clear, suggest may become show, demonstrate or another stronger verb.

Stating the purpose of an experiment:

1. `To examine whether [component] [does what], we compare [variants] while keeping [other settings] fixed.`
2. `If [factor] had no effect on [outcome], we would expect similar [metric] across [groups]. Table [X] shows that [metric] [changes systematically] as [factor] varies.` (needs results grouped by the factor)

Stating the controls:

3. `All variants keep the same or comparable [resource] and differ only in [criterion].`
4. `Since [baseline] also contains [a module for the same purpose], we replace [that module] with [ours] to compare the two designs directly.`

Reporting the main results:

5. `At [budget level], [ours] retains [value] of [reference], while the strongest baseline, [name], retains [value].`
6. `The results in Table [X] lead to several observations. (1) [Observation], which [bridge]. (2) Despite [general trend], [exception], which is consistent with our motivation that [hypothesis]. (3) [Ours] yields larger gains on [dataset type] than on [dataset type].`

Bridging:

7. `[The comparison] suggests that [our design choice] matters more than [alternative design choice].`
8. `[The observation] is consistent with our motivation that [hypothesis].`

Complementary components:

9. `Each [component] alone improves [baseline], with [A] providing the larger gain. Combining both yields the best results, which suggests that the two [components] contribute from different perspectives: [A] [role], and [B] then [role].`

Deriving a design from a comparison:

10. `Compared with [the variant without the design], [ours] improves [metric] on [datasets], indicating that [design decision], since [reason].`

Ruling out an alternative explanation:

11. `A natural question is whether [gain] simply comes from [alternative explanation]. To examine this, we [intervention or control]. [Result], indicating that [gain] does not stem from [alternative explanation].`

Showing that a criterion works:

12. `To understand how [signal] works, we partition the instances into [k] groups by [signal], from low to high. [Ours] achieves larger gains on the groups with higher [signal], which suggests that [mechanism].`
13. `Ideally, an adaptive [allocation] should be more accurate than [the low-cost setting] while using fewer [resources] than [the high-cost setting].` (at the start of the setup or of a research question)

Unfavorable results:

14. `For most [datasets], [observation]. On [dataset], in contrast, [result], which may be related to [dataset property].`
15. `An unexpected observation is that [phenomenon], which may indicate [hypothesis]. We leave its verification to future work.`

Visualization:

16. `Fig. [X] visualizes the [elements] retained by [baseline] and [ours]. Compared with [baseline], [ours] retains more [elements] on [regions related to the decision], which illustrates that [component] selects [cues] that better match [the decision].`

Summing up:

17. `These findings suggest that [practice] benefits from [recommendation], although [simpler practice] may suffice when [condition].`

## 3 Conclusion

Expression:

- **Tense**: by the default constraints, the conclusion is in the simple present.
- **Components may share a sentence**, but each one's role must still be visible; three components can take separate sentences, rather than being squeezed into one long noun chain to keep the conclusion short.
- **Abbreviations**: abbreviations already introduced need not be spelled out again in the conclusion, but what the method is and what the components do still get a brief statement. The rule of spelling out at first use in the paper still holds; it does not mean spelling out in every section.
- **Citations**: the conclusion is not barred from citing; keep a citation when the sentence needs to point to prior work, still using only keys in the reference table.
- **Strength**: demonstrate, confirm and superior in model sentences can serve as references; whether one fits a given conclusion is judged by the outline and the actual results. Do not add qualifications the outline lacks, and do not copy claims of being first or sweeping comparisons just because a top-venue sentence makes them.
- **When a finding leads to a recommendation**, say in what situation the recommendation applies.

Patterns:

| Function | Pattern | Use |
|---|---|---|
| Present the method and its contribution | `We propose [method], a [type of] framework for [task] that [core contribution].` | Get to the paper at once |
| Sum up how components work together | `[Component A] [key action] to [purpose], while [component B] [key action] to [purpose].` | Combine only when the two parts play different roles |
| Link an operation to its effect | `By [key operation], [method] [design advantage].` | Do not reduce it to a vague word for advantage |
| Sum up the overall result | `Experiments on [evaluation scope] demonstrate [overall finding].` | No need to squeeze numbers into this frame |
| Report component validation separately | `Ablation studies further validate [component-level conclusion].` | Use when the overall effect and the role of components must be told apart |
| Draw together an insight | `Our findings show that [central insight established in the paper].` | Do not put forward a new explanation |
| End with the value of the work | `[Method or finding] provides [specific value] for [application or research direction].` | Tie the value to the paper's results |
| Optional future direction | `In future work, we will investigate [specific unresolved issue].` | Only when the decision is to write future directions |

These are optional structures; the paragraph does not have to open every sentence with We.

## 4 Table and figure captions

Table captions:

1. Main results: `Comparison of [objects] on [datasets or models]`; `Overall results on [model]` and similar "topic + on" captions are the same type.
2. Defining a symbol in one sentence: `[Symbol] is [meaning].`, `[Column] refers to [meaning]; [column] = [value] indicates [reference].`
3. Scope of the experiment: `Experiments are conducted on [datasets] on [models].`
4. Mapping variant names: `[Name A], [B], and [C] represent [meaning A], [B], and [C], respectively.`; `“[Name]” denotes [meaning].`
5. Explaining bold, in the caption: `The best results are in bold.`; in a table note, with its scope: `The best results in each setting are highlighted in bold`, `The best result among [set] of each metric is in bold`.
6. Why settings differ: `Due to [difference between datasets], the optimal [configuration] of each dataset is different.`
7. Placeholders of a template: `“[Placeholder]” … are placeholders meant to be replaced with [content].`

Figure captions:

8. Title of a results figure: `The effect of different [variable] on the [dataset] dataset.`, `[Topic] in terms of [metric]`.
9. Marking the best items: `The maximum results for each [group] are highlighted.`
10. Roles of the elements in a figure: `In each bar chart, the title represents [A]. The x-axis shows [B], and [C] are indicated by different colors in the legend.`
11. Fixed settings: `Using [setting] for all [objects].`, `Results reported using [model] on [dataset].`
12. Overview figure by stage: `[Method] [does what] through a two-stage process: [stage A] and [stage B]. [Stage A] (illustrated in the [position]) [role] at the [stage], …; [stage B] (illustrated in the [position]) ….`
13. Overview figure by component: `The model comprises two main components: [A] and [B]. [A] [role], [effect]. [B] [role], [effect].`
14. Panels: `Left: [content]. Right: [content].`, `From left to right: [columns].`, `[A] (top) and [B] (bottom)`.
15. Occlusion: `The occluded part represents dropped [elements].`
16. A note on color: `(colour figure online)`, the form used by Springer journals.

Trade-offs when using them:

- "Bold is the best." is colloquial; when a model caption lacks an article, as in "β is drop rate", add it when borrowing.
- Entries in the form "Name: meaning" look fragmented when several are used in a row.
- Numbering several findings in a table caption makes it long; compress it when it overlaps with the main text. This does not mean result sentences cannot go into captions.
- Putting color swatches in a table caption as a legend relies on color and is lost in black-and-white print.
