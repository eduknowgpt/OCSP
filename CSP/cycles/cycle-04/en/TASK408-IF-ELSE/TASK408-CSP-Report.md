# TASK408 — CSP Report

## 1. Context and scope

**Task:** Choosing Between IF–ELSE and Two Independent IF Statements.  
**Creator:** Prof. MSc Marcos Bião — Univasf, Salgueiro Campus.  
**Target audience:** learners in introductory programming.

The learner examines two supplied pseudocode fragments that classify an integer as positive or nonpositive. Version A uses two independent IF statements with complementary conditions; Version B uses IF–ELSE. The input value remains unchanged, and displaying a message has no effect on it.

The required deliverable is a selected alternative and a brief justification explaining output equivalence under these assumptions, the number of condition evaluations and the limits of inferring actual execution time from those counts. No implementation, execution, benchmark or formal complexity analysis is required.

Condition evaluations are counted according to the pseudocode, without assuming compiler optimizations. Version A evaluates two conditions and Version B evaluates one for every integer input. Both produce the same output under the stated assumptions. This difference in source-level evaluations does not guarantee a runtime advantage in every language and execution environment.

The report follows the revised task rather than the original question's unconditional association between fewer tests and greater efficiency.

## 2. Knowledge mobilized

Existing identifiers and curricular granularity follow the previous reports. The Algorithms and Programming Logic course plan used in TASK401 remains a terminology reference.

| ID | Knowledge area | TASK408 application |
|---|---|---|
| K03 | Data types, constants and variables | Interpret integer input and the assumption that its value remains unchanged |
| K06 | Input and output statements | Interpret the input and displayed classifications without executing the pseudocode |
| K07 | Relational and logical operators | Recognize that `x > 0` and `x <= 0` are complementary for integers |
| K08 | Decision structures | Explain independent decisions and mutually exclusive IF–ELSE branches |

Counting which conditions are evaluated is treated as a detail of conditional execution within K08. 

K03 and K06 support interpretation of the supplied fragments. They do not imply separate requirements to implement data representation or input/output operations.

## 3. Learning objectives

| Objective | Bloom level | Competency |
|---|---|---|
| Explain why the conditions are complementary and how each structure selects its output | Understand | CM14 |
| Explain why the fragments produce the same output under the stated assumptions | Understand | CM14 |
| Explain why independent IF statements evaluate both conditions while IF–ELSE evaluates one | Understand | CM14 |



## 4. Competency specifications

### CM14 — Explain conditional execution

**Status:** reused from the TASK401 adjustment and subsequently used in TASK407. Its definition and complete constitutive knowledge–Bloom pairings are preserved.

**Definition:** explain how Boolean conditions determine the actions executed by conditional structures.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K07 — Relational and logical operators | Understand | Explain how comparisons and logical combinations determine a condition's truth value |
| K08 — Decision structures | Understand | Explain how condition results determine which branch is executed |

**Manifestation and evidence:** the required justification explains that exactly one of `x > 0` and `x <= 0` is true for any integer. Version A evaluates both independent conditions, while Version B selects one of its two branches after evaluating one condition. Output equivalence depends on the complementary conditions and the unchanged value. Two independent IF statements are not universally interchangeable with IF–ELSE.

**Disposition:** communicative and meticulous.




## 5. Activation and performance criteria

| Code | Constraint | Mode | Role | Requirement or condition |
|---|---|---|---|---|
| CM14 | mandatory | explanatory | core | Explain conditional behavior and output equivalence under the stated assumptions |

There is one direct mandatory association and no competency composition. The selected alternative and required justification provide the evidence; no supplementary assessment is imposed.

**Expected performance:** the learner selects **(c), I and II only**, and supports the selection by explaining complementary conditions, identical outputs under the assumptions, the two-versus-one evaluation count and the absence of a universal runtime guarantee. The justification also rejects the assertion that arbitrary independent IF statements always behave like IF–ELSE.

A correct alternative without justification is insufficient to establish CM14. The explanation must connect the conditions to the branches executed and the resulting outputs. The runtime caveat prevents an overgeneralization; it does not introduce assessment of algorithmic efficiency. These specifications describe intended performances and do not, by themselves, establish individual learner mastery.

