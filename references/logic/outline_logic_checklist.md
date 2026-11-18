# Outline logic checklist

Go through it item by item when auditing the logic of an outline. Check only two kinds of problems: hard flaws and missing design rationale. Do not record the order of components, the order of presentation, forward references, claims and evidence that await experiments, hyperparameter values, wording or English expression.

**Scope**: Definitions, rationales and mechanisms may be spread across sections; do not flag the order of components, the order of presentation or forward references. Do not check pending experiments, hyperparameter values, wording or English expression. Do not demand an exhaustive list of alternatives or proof that every engineering choice is uniquely optimal.

**Judgment**: When there is a conflict, a necessary concept cannot be pinned down, or the explanation of an effect goes beyond the computational definition, check whether it is a hard flaw. When the computation and its meaning hold but nothing explains why this design was chosen, record missing design rationale. An empirical link stated explicitly as a design assumption is not judged wrong just because experiments are still missing.

The quoted sentences come from these 15 papers:

| Short name | Paper | Venue |
|---|---|---|
| SEPM | Catch Your Emotion: Sharpening Emotion Perception in Multimodal Large Language Models | ICML 2025 |
| WETR | World-Model Inspired Emotion-aware Token Refinement for Training-Free Multimodal Emotion Recognition | ICML 2026 |
| SoV | Visual Prompting in LLMs for Enhancing Emotion Recognition | EMNLP 2024 |
| WisdoM | WisdoM: Improving Multimodal Sentiment Analysis by Fusing Contextual World Knowledge | ACM MM 2024 |
| MERMAID | MERMAID: Multi-perspective Self-reflective Agents with Generative Augmentation for Emotion Recognition | EMNLP 2025 |
| SparseVLM | SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference | ICML 2025 |
| AutoPrune | Each Complexity Deserves a Pruning Policy | NeurIPS 2025 |
| DivPrune | DivPrune: Diversity-based Visual Token Pruning for Large Multimodal Models | CVPR 2025 |
| CDPruner | Beyond Attention or Similarity: Maximizing Conditional Diversity for Token Pruning in MLLMs | NeurIPS 2025 |
| DART | Stop Looking for “Important Tokens” in Multimodal Language Models: Duplication Matters More | EMNLP 2025 |
| DRAGIN | DRAGIN: Dynamic Retrieval Augmented Generation based on the Information Needs of Large Language Models | ACL 2024 |
| Self-RAG | Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection | ICLR 2024 |
| RAPTOR | RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval | ICLR 2024 |
| OPERA | OPERA: Alleviating Hallucination in Multi-Modal Large Language Models via Over-Trust Penalty and Retrospection-Allocation | CVPR 2024 |
| AdaLLaVA | Learning to Inference Adaptively for Multimodal Large Language Models | ICCV 2025 |

## L01 Challenges and mechanisms line up

**Item**: Each component must match a challenge promised in the introduction, or a concrete gap derived from it, and explain what the mechanism changes to address that gap. Once the mechanism is described, it must return to the goal stated at the start: one sentence on how the design answers its challenge.

**Positive example**: SoV §3.1 Problem Definition answers the tension between cropping and keeping context by marking the whole image.

> Traditionally, this involves cropping the face from the image using face detectors. However, with the introduction of visual prompting, faces can be directly marked on the entire image, highlighting the facial region while preserving the background context and avoiding the obscuration of faces.

Examples of returning to the goal: MERMAID §4.4 “From our perspective, this design helps eliminate emotional ambiguity and produces results agreed upon across the two modalities.”; AutoPrune §3.3 “This procedure preserves the shape of curve while guaranteeing identical computational complexity across tasks.”

**Violation**: The method claims to fix some missing information, but its procedure only changes the output format, without explaining how that change supplies what was missing.

## L02 Key choices need a specific rationale

**Item**: For choices that affect whether the goal is met, explain why the chosen object or form suits the problem at hand, not just the steps performed.

**Positive example 1**: DivPrune §3.2 Token Pruning explains why visual tokens are pruned first.

> Since visual tokens tend to have more redundancy, they are generally selected for pruning.

**Positive example 2**: RAPTOR §3 Methods, Clustering Algorithm paragraph, explains why it chooses soft clustering, which allows multiple membership.

> One of the unique aspects of our clustering approach is the use of soft clustering, where nodes can belong to multiple clusters without requiring a fixed number of clusters. This flexibility is essential because individual text segments often contain information relevant to various topics, thereby warranting their inclusion in multiple summaries.

**Violation**: The method gives a filtering or aggregation scheme without explaining why its properties fit the goal.

## L03 Borrowed methods need a justification of fit

**Item**: When borrowing a prior method, identify the sub-problem to be solved and the relevant property of the borrowed method, and explain why this tool fits here.

**Positive example**: RAPTOR §3 Methods, Clustering Algorithm paragraph, justifies introducing a dimensionality-reduction tool by the problem of distances in high dimensions.

> The high dimensionality of vector embeddings presents a challenge for traditional GMMs, as distance metrics may behave poorly when used to measure similarity in high-dimensional spaces (Aggarwal et al., 2001). To mitigate this, we employ Uniform Manifold Approximation and Projection (UMAP), a manifold learning technique for dimensionality reduction (McInnes et al., 2018).

**Violation**: The method only says an existing technique is borrowed and gives its formula, without stating what relation it captures or what need it meets.

## L04 Adaptations must match differences in conditions

**Item**: When a borrowed mechanism meets differences in input or model structure, state which conditions still hold, which parts must be replaced, and which difference each replacement answers; when nothing needs to change, state why it can be reused as is.

**Positive example**: CDPruner §3.3 Instruction relevance distinguishes two sources of features by whether a paired text encoder exists.

> For MLLMs [Liu et al., 2023, 2024b, Li et al., 2024a] that employ visual encoders paired with corresponding text encoders (e.g., CLIP [Radford et al., 2021]), we use features extracted from both as visual and text embeddings, respectively. For MLLMs [Bai et al., 2025, Zhu et al., 2025] only contain dedicated visual encoders, we instead use the output of the multimodal projector as the visual embeddings, and take the average of all token embeddings corresponding to the instruction from the language model as the text embedding.

**Violation**: The original mechanism relies on an input or a structure that does not exist here, yet it is copied without comment; or the input source changes, but the original justification is still applied.

## L05 Combined components must be complementary

**Item**: When combining several components, state what each adds or when each applies, and why one cannot replace another. One way is to split the problem into sub-problems first and let each design answer one.

**Positive example**: OPERA §3.3 Retrospection-Allocation Strategy. The two quoted sentences give, respectively, the remaining failure case of the penalty and the new action taken by retrospection.

> While there still exists a few cases that all of the candidates get penalized and the hallucination already occurred.

> Specifically, when the decoding procedure encounters the knowledge aggregation pattern and the hallucination is inevitable, it rolls back to the summary token and selects other candidates for the next token prediction except for the candidates selected before.

Examples of splitting into sub-problems: AutoPrune §3.3 “Then the next questions are: (1) how to formulate a reliable indicator for assessing the sample and task complexity? and (2) how to translate this indicator into a policy …”; DRAGIN §3.1 and §3.2 answer “when to retrieve” and “what to retrieve” separately.

**Violation**: Several components all claim to improve the same result, with no division of labor, and nothing explains what weakness of a single mechanism their combination makes up for.

## L06 Interfaces between components must keep their meaning

**Item**: When a result is used across components or stages, state what is passed and what it is used for downstream, and keep its type and meaning consistent.

**Positive example**: MERMAID §4.3 Multi-Perspective Self-reflection Agents, Textual self-reflection agent paragraph, distinguishes the status indicator from the feedback used in the next round of prediction.

> Specifically, the status indicator within $F_{\mathrm{text}}$ determines whether further iterations are necessary, while the suggestion and explanatory feedback jointly form the query $Q_{\mathrm{text}}$, capturing the cognitive reasoning behind the evaluation. This information is subsequently passed on to the decision agent to guide the next round of prediction.

**Violation**: Upstream produces a score, a label or a feedback text, and downstream uses it as a different kind of object without conversion, so the computation or the explanation does not connect.

## L07 The meaning of a concept must be compatible with its computational definition

**Item**: Key concepts that enter a computation or a decision need a clear object and an operational definition; their verbal meaning must be compatible with how they are computed, and the same quantity must not change meaning without notice. For quantities with a scope (which stage, which layer, which tokens), state the scope; when the same letter refers to different objects at different stages, say so.

**Positive example 1**: DRAGIN §3.1 Real-time Information Need Detection states which distribution's entropy measures token uncertainty.

> RIND begins by quantifying the uncertainty of each token generated during the LLM’s inference process. This is accomplished by recording the entropy of the token’s probability distribution across the vocabulary.

**Positive example 2**: DART §3.3 Token Duplication: Rethinking Reduction, Definition 2 and Eq. (7), states which vectors the duplication score compares, instead of simply calling duplication importance.

> The token duplication score between a pivot token $p_i$ and a visual token $x_j$ is defined as: $\operatorname{dup}(p_i,x_j)=\frac{p_i^\top x_j}{\|p_i\|\|x_j\|}$, where $\|\cdot\|$ denotes the Euclidean norm.

Example of stating the scope: WETR §3.1 “We use index sets to distinguish token types: Iv … for visual tokens and It … for text tokens.”

**Violation**: The formula computes a distributional difference between certain objects, but the text interprets it directly as another, undefined property; or the meaning of the same symbol silently changes across components.

## L08 Separate the ideal target from the proxy signal

**Item**: When the ideal target cannot be computed directly, distinguish the target from the proxy signal, and state which judgment the proxy is used for; do not present the value of the proxy as a measurement of the target itself.

**Positive example**: WETR §3.3 NTS: Noise-suppressed Token Selection. The two quoted sentences state, respectively, that the information gain is not directly accessible and which proxy is computed instead.

> Since $\Delta_i^\star$ is not directly accessible in frozen MLLMs, NTS estimates a computable proxy $\widehat{\Delta}_i$ during inference and admits the top-scoring tokens into $K$.

> To obtain a computable proxy for the conditional gain in Eq. (3), we score each token by contrastive querying.

**Violation**: An easily computed relevance or attention score is named as the true contribution, and the name is then used as grounds that the two are equal.

## L09 Adaptive criteria must connect to the direction of the action (when needed)

**Item**: Check this item only when the method makes decisions from a criterion, such as routing or budgets. Give an interpretation of each state that is compatible with how the criterion is defined, and explain why that state calls for the chosen direction of action, rather than only listing threshold branches.

**Positive example**: AutoPrune §3.3 Complexity-Adaptive Pruning, Mutual Information for Cross-Modal Alignment paragraph, links high and low values, their interpretation as a constraint between image and text, and the pruning action.

> As shown in Fig. 2, a large value of $I(V,T)$ indicates that the textual prompt sharply constrains the space of plausible visual interpretations, allowing the model to confidently localize the relevant region early and perform aggressive front-loaded pruning of non-essential visual tokens (orange curve). Conversely, a small mutual information means weak or indirect correspondence, so the network must preserve multiple visual hypotheses across layers, leading to a gradual, unstable reduction of attention (blue curve) [44, 45].

**Violation**: The method only says to give more resources when the score is high and fewer when it is low, without saying what processing need the score reflects, or with a direction of action that contradicts the stated meaning.

## L10 Adaptive changes must close under the resource constraint

**Item**: When claiming adaptivity under a resource constraint, explain with one consistent measure how local decisions satisfy the global constraint; quantities at different levels or in different units must not be equated directly.

**Positive example**: AdaLLaVA §3.3 Learning to Schedule Execution Plans, Modeling paragraph, enforces the budget constraint by restricting the states available to the distribution over execution plans.

> Our design requires that the sampled execution plan strictly adheres to the latency budget while maximizing resource utilization. To achieve this, we restrict the support of $p(s\mid\{z_{v|q}\},l,\omega)$ to the states $s$ that have exactly $k$ activated switches, where $k$ is the maximum number of switches allowed to be turned on without violating $l$.

**Violation**: Only a local count is limited, yet the overall resource budget is claimed to be met, without explaining how the local count relates to the overall cost.

## L11 Multi-stage conditions must state their reliability limits

**Item**: When the output of an earlier stage restricts the candidates of a later stage or sets a key condition for it, state what happens when that condition is unreliable, or the limits of its use; do not assume the earlier stage is always right.

**Positive example**: SEPM §3.2 Confidence-Guided Coarse-to-Fine Inference, Confidence Assessment paragraph, keeps the full candidate set for low-confidence results.

> Therefore, we set a threshold, denoted as $\alpha$, where results with a confidence score lower than $\alpha$ are considered unreliable samples. For these, we retain all emotion categories in the fine-grained stage and add ambiguous-related descriptions reflecting the behavior from the first stage, enhancing the prompting effect.

**Violation**: The correct candidate for the later stage can be excluded by a single earlier judgment, yet the method treats that condition as ground truth and says nothing about handling its failure or about the limit it accepts.

## L12 Changes to evidence must explain how loss or interference is controlled

**Item**: When removing, compressing or adding evidence, explain how the information loss or irrelevant interference this causes is controlled; do not treat everything removed as useless or everything added as useful.

**Positive example 1**: SparseVLM §3.3 Visual Token Recycling justifies adding a recycling mechanism by the information still held in low-scoring tokens.

> Despite being less significant, the pruned visual tokens with relatively large values in $P$ still contain certain information. To efficiently preserve more visual details with fewer tokens, we propose a token recycling strategy to aggregate and reconstruct tokens to be pruned.

**Positive example 2**: WisdoM §3.2.4 Stage 3: Contextual Fusion justifies fusing predictions conditionally by the noise that added context may bring.

> However, the context may contain irrelevant information that could disturb performance. Therefore, we first determine hard samples and then fuse the $P_i$ and $\hat{P}_i$ in the hard sample.

**Violation**: The method asserts that removal loses no useful information just because a component scores low, or that added external knowledge causes no interference just because it was added.

## L13 Signals and modules must be available in the stated setting

**Item**: The variables and modules the method relies on at run time must be obtainable in the stated setting. Distinguish what is learned or built offline from what happens during online inference, and do not cross that boundary without saying so.

**Positive example**: Self-RAG §3.1 Problem Formalization and Overview, Training overview paragraph, explains that reflection tokens come from the critic model during training and from the generator itself at inference.

> Using the critic model, we update the training corpus by inserting reflection tokens into task outputs offline. Subsequently, we train the final generator model (M) using the conventional LM objective (Section 3.2.2) to enable M to generate reflection tokens by itself without relying on the critic at inference time.

**Violation**: An online rule depends on information that only training labels, future outputs or an extra learned module can provide, without explaining how it is obtained or how this relates to the claimed setting.

## L14 Approximations must not pose as exact equivalence

**Item**: When an ideal computation is solved approximately, identify the approximation actually used and how it differs from the original computation; do not carry over exact equivalence, optimality or unconditional guarantees without saying so.

**Positive example**: AdaLLaVA §3.4 Training and Inference, Adaptive inference paragraph, explicitly calls the replacement of marginalization over the distribution by the choice of the most probable plan an approximation.

> In theory, decoding the answer $X_a$ requires marginalizing over this distribution, which is infeasible due to the large number of configurations. In practice, we approximate the inference by selecting the most probable execution plan from the scheduler.

**Violation**: After a single path or a heuristic replaces the original optimization or integral, the two computations are still written as identical, and guarantees that hold only for the original problem are applied.
