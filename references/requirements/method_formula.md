# Writing the formulas of the method section

Follow these 20 rules when writing formulas in the method section.

## 1 Keep formulas simple

1. **Give formulas only for the core computations**: scoring, the basis of selection, merging and the like. Operations such as selecting, keeping or removing are said in one sentence (for example "keep the most important tokens by their scores and remove the rest"), without argmax or set notation.
2. **When attention is involved, do not write attention heads** unless the user asks; write attention as one matrix.
3. **Do not write layer indices or per-layer configurations**, such as in which layers something happens or how many items each layer keeps; the specific values of hyperparameters appear only in the experimental setup.
4. **Use few Greek letters.** Ratios, coefficients and counts get no symbols; their values go to the implementation details. Common notation may stay.
5. **Avoid rare notation, and do not explain common operations**: do not write all-ones vectors, do not explain the direction of a Softmax normalization, do not explain "the i-th row of the matrix".
6. **Give the dimension of every vector, and make scalars recognizable at a glance**: write $\mathbf{c}\in\mathbb{R}^{M}$, and give the mean separately as $\bar{c}=\frac{1}{M}\sum_a c_a$.
7. **Replace multi-letter subscripts with a single letter**, for example $n_{\mathrm{nb}}$ becomes $K$.
8. **Write piecewise definitions in the format of the paper they come from**: put the condition under min, use if and otherwise for the cases, and change only the symbols.

## 2 Writing what is borrowed

9. **Put the citation right after "inspired by"**: "Inspired by the [mechanism] of X [citation], our component …".
10. **Once the opening has said what inspired the design, do not write "following the [part] of X" later**, which reads as copying; state the purpose of the step directly, for example "To reduce the information lost by removing tokens, …".
11. **A classic algorithm that is borrowed** is cited inline where it is used.

## 3 Definitions and connections

12. **Define a term the first time it appears.** First say what is selected and why, then give it a name.
13. **A name should say what the thing is**: for example, recycled tokens should be described as "the most important part of the removed tokens".
14. **Before introducing a new symbol, check whether the preliminaries already define it**; if not, define it in its own sentence within the component.
15. **Every sentence connects to the one before it**; no sentence appears out of nowhere.
16. **Do not repeat what earlier definitions already guarantee.**
17. **Remove subheadings such as scoring, removal and merging**, and remove sentences that only describe implementation details.
18. **Cut redundant wording**, for example "assess the importance of each token" becomes "assess importance".

## 4 When the original paper and the code disagree

19. **Let the user decide; do not decide on your own.** The rule of thumb: differences that change what is computed follow what actually runs; differences in detail keep the formula of the original paper in the text.
20. **When the user questions something, check the code** and give the file and line numbers; if the user's guess is wrong, say so plainly.
