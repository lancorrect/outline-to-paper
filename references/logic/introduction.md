# Writing logic: Introduction

Each item gives what to write and what to check.

The introduction is a chain of reasoning: each link must follow from the one before it. The general chain has seven links:

| Link | Role | How it leads to the next link |
|---|---|---|
| Background | Start from the task and narrow, level by level, to the direction the paper focuses on | Its last sentence is the premise of the general problem |
| General problem | State the difficulty shared by this direction and explain its causes | The causes justify the paper's angle of attack |
| Existing work and its gaps | Show how existing work handles the general problem and why it falls short | Shows the general problem is still open and leads to the aspects that need improvement |
| Transition | State the aspects in which the general problem must be tackled | The number of aspects equals the number of challenges |
| Challenges | One concrete sub-problem per aspect | One-to-one with the components |
| Method | The overall idea and each component | Corresponds to the contributions |
| Contributions | Summarize what the paper achieves | The introduction ends here |

## Background

- What to write: First state the object of study, that is, the task definition (what goes in, what is decided). Then trace the development of the field, only down to the branch that concerns this paper; earlier lines of work get one or two sentences. End at the direction or paradigm the paper focuses on.
- Check: Narrow from broad to specific: the task, then the development relevant to this paper, then the paper's direction, with no detour into unrelated topics. Earlier lines of work are neither expanded nor evaluated here. When describing an existing paradigm, state only what it means and how it works, without naming specific works; citations go at the end of the sentence. The last sentence of the paragraph leads directly to the general problem.

## General problem

- What to write: The first sentence of the paragraph states the general problem. Its subject is the class of methods or the research direction, and it states a difficulty they all share. The rest of the paragraph analyzes the causes, each backed by evidence.
- Check:
  - The paragraph has exactly one general problem, and it comes first.
  - It is a shared difficulty, not the flaw of one method. A single method's flaw can only serve as an example, in the next link.
  - The general problem can be stated in one sentence without explaining the concepts in it.
  - The causes support the paper's angle: after reading them, the reader should see why the paper attacks the problem from this angle.
  - The causes may be split by source into several items, each with evidence.

## Existing work and its gaps

- What to write: First summarize the existing approaches by broad category. Mention in passing the categories that differ from the paper's route, and say why the paper does not take them. Then focus on the paper's own route: group the related work from the paper's angle, and give each group's approach and gaps. The gaps can be stated within each group or summarized at the end of the paragraph.
- Check:
  - The grouping follows the paper's angle; methods are not described one by one in detail.
  - Every gap can be traced to specific methods; the gap of one method is not attributed to its whole group.
  - Gaps are stated in terms of the core concepts of the general problem, naming the aspect in which they occur.
  - A sentence first written as the general problem that only describes the flaw of one method moves here, as an example or as part of the closing summary.

## Transition

- What to write: One sentence on the aspects in which the general problem must be improved, and hence how many challenges arise.
- Check: The number and order of the aspects match the challenges. The key words of the title appear here.

## Challenges

- What to write: One item per challenge. First say which aspect it belongs to. Then describe the phenomenon and its cause, explaining why this aspect goes wrong, citing literature when needed. Then give evidence, such as an example figure or data. Name the challenge last.
- Check:
  - It describes a problem, not a method: use problem-level words, and do not mention the paper's specific techniques.
  - The name alone tells the reader what the problem is. When the problem is that two things cannot be balanced, put both in the name and add a word such as "mismatch" or "dilemma". When the problem lies in one thing, name that thing and a word for its defect, such as "rigidity". The name also states where the problem occurs. For example, "Mismatch between Retrieval Granularity and Question Granularity in Long-Document QA" and "Cross-Domain Rigidity of Retrieval Strategies"; "Retrieval Risk" does not say what the problem is. Do not use words such as "risk" or "insufficiency" that do not say what the problem is, do not use metaphors, and keep modifiers free of praise. Keep the name short, and give a phrase as its short form.
  - The evidence demonstrates the challenge on its own and is understandable to the reader. When the challenge is about differences across some kind of object, the evidence covers more than one such object.
  - The challenges do not overlap, and together they cover the general problem.
  - They are ordered from most to least important.

## Method

- What to write: Give the full name of the method the first time it appears. State the overall idea in one sentence, that is, how it answers the general problem. State what it builds on. Then, for each component, give the challenge it addresses, its key step, and why this solves the challenge.
- Check: Components and challenges correspond one to one and follow the same order of importance. A single thread runs through the components, so they do not read as a patchwork. The components are described as in the method section.

## Contributions

- What to write: One item for the overall method; one item per component, stating which challenge it solves, its key step, and the advantage it brings; one item for the experiments.
- Check: Do not repeat the method paragraph. Focus on the advantages, where an advantage means the purpose the component was designed for. Component items carry no experimental results. The experiment item gives no specific numbers.

## Overall check of the introduction

- Every link holds: the background leads to the general problem, the causes support the angle, the challenges correspond to the components, and the components correspond to the contributions.
- Challenges, components and contributions match in number and order.
- The key words of the title run through the general problem, the challenges and the method.
- Every core concept used in the introduction is defined somewhere in the paper.
- The description of prior work agrees with the related work section.
