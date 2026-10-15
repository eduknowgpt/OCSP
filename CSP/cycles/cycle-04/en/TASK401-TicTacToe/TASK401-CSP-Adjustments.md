# TASK401 - CSP Adjustment

## 1. Adjustment scope

This adjustment reformulates CM10 - Explain a computational solution as a composite of explanatory atomic competencies, preserving its identifier and integrative role. CM01-CM09 retain their definitions from the initial report; CM07 becomes mandatory under the modularization requirement introduced below. 

Each atomic competency below has a complete, stable set of constitutive KS pairs. CM10 has a fixed component set and the resulting union of those KS pairs. A task association references the whole competency; it does not select a subset of its pairs. Definitions and observable operations are reusable; TASK401 manifestations and evidence are situated.


## 2. Adjusted competency specifications

### CM12 - Explain arithmetic expression evaluation

**Definition:** explain how arithmetic expressions produce values according to their operands and operator precedence.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K04 - Arithmetic and literal expressions | Understand | Explain how operand values and operator precedence determine an arithmetic expression's result. |

**TASK401 manifestation:** explain an arithmetic expression used for index conversion, a counter or another implemented calculation, when present and requested.

**Evidence and criterion:** individual explanation of the expression; the learner correctly explains its operands, evaluation order and result. This competency targets the arithmetic aspect of the curricular area; it does not assert literal-expression performance.

**Disposition:** communicative and meticulous.



### CM13 - Explain data organization

**Definition:** explain how arrays or matrices organize data and allow elements to be located and accessed.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K10 - Arrays and matrices | Understand | Explain the organization of an indexed structure and the correspondence between indexes and stored elements. |

**TASK401 manifestation:** explain how nine cells are organized in the chosen board representation and how a position corresponds to an index or coordinates.

**Evidence and criterion:** individual explanation using the implemented representation; the correspondence between positions and elements is correct. A flat array or matrix is sufficient; these are alternatives within one curricular knowledge area, not task-selected KS pairs.

**Disposition:** communicative and meticulous.



### CM14 - Explain conditional execution

**Definition:** explain how Boolean conditions determine the actions executed by conditional structures.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K07 - Relational and logical operators | Understand | Explain how comparisons and logical combinations determine a condition's truth value. |
| K08 - Decision structures | Understand | Explain how condition results determine which branch is executed. |

**TASK401 manifestation:** explain move acceptance and the decisions that identify continuation, victory or draw.

**Evidence and criterion:** individual explanation of conditions and branches; the learner explains the predicate and its consequence, including why an empty line is not a win and a final winning move is not a draw.

**Disposition:** communicative and meticulous.



### CM15 - Explain repeated execution

**Definition:** explain how repetition structures control repeated execution and determine when it continues or stops.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K09 - Repetition structures | Understand | Explain the repeated action and the condition or iteration limit governing continuation and termination. |

**TASK401 manifestation:** explain the match loop and any loop used for repeated input or board traversal.

**Evidence and criterion:** individual explanation; the repeated action and stopping rule agree with the code and game behavior. Only the loop form used is required.

**Disposition:** communicative and meticulous.



### CM16 - Explain function organization

**Definition:** explain function responsibilities and how calls and parameter passing connect them in a computational solution.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K11 - Modularization: functions and parameter passing | Understand | Explain function responsibilities, invocation and the data exchanged through parameters and return values. |

**TASK401 manifestation:** explain the implemented functions for board display, validation or outcome checking and their relationships.

**Evidence and criterion:** individual explanation of responsibilities and data exchange; the account agrees with actual calls, parameters and returns. Do not claim this competency solely because the learner can name functions.

**Disposition:** communicative and meticulous.



### CM17 - Explain variable updates

**Definition:** explain how variable values are represented and changed by assignment statements.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K03 - Data types, constants and variables | Understand | Explain the role of data types, constants and variables in representing values. |
| K05 - Assignment statements | Understand | Explain how an assignment determines the newly stored value using the values available at that step. |

**TASK401 manifestation:** explain the values used for empty/X/O cells and the current player, and how accepted moves update those variables.

**Evidence and criterion:** individual explanation; the learner distinguishes stored values from their representations and explains relevant updates without confusing previous and current values.

**Disposition:** communicative and meticulous.



### CM10 - Explain a computational solution

**Type:** composite competency.

**Definition:** explain a computational solution by relating its data representation, state updates, decisions, repetition and function organization.

**Components:** CM13, CM14, CM15, CM16 and CM17. All five are constitutive; none is optional. CM12 is not a component.

| Component | Constitutive KS pairs | Contribution to the coordinated explanation |
|---|---|---|
| CM13 - Explain data organization | K10 × Understand | Explain how stored elements correspond to the problem representation |
| CM14 - Explain conditional execution | K07 × Understand; K08 × Understand | Explain how predicates select actions |
| CM15 - Explain repeated execution | K09 × Understand | Explain how repeated behavior continues and terminates |
| CM16 - Explain function organization | K11 × Understand | Explain responsibilities and data exchange between functions |
| CM17 - Explain variable updates | K03 × Understand; K05 × Understand | Explain represented values and their updates |

The complete KS set is K03, K05, K07, K08, K09, K10 and K11, each paired with Understand. These pairs are obtained from the component specifications rather than selected independently for each task. Coordinating the explanation does not automatically raise its Bloom level to Analyze.

**TASK401 manifestation:** explain how the board stores the game state, accepted moves update it, conditions enforce rules, loops control the match and functions organize those responsibilities.

**Evidence and criterion:** individual explanation using the implemented code; all component criteria are satisfied, and the learner relates them coherently. A question about one component alone is insufficient to evidence the whole composite. Missing evidence for a component means CM10 is not fully evidenced; it does not establish failure of every other component.

**Disposition:** communicative, meticulous and responsible.

**Adjusted task requirement:** organize the solution into functions with explicit responsibilities and data exchange, and require each learner to explain that organization together with the representation, updates and control flow. The initial task anticipated functions without prescribing a modular architecture; this adjustment makes the requirement explicit for future application.

The task selects CM10 as a whole. Its atoms remain catalog entries and may be referenced in assessment criteria without adding duplicate direct task associations.



## 3. BNCC alignment of the resulting competencies

For CM10 and CM12-CM17, **BNCC General Competency 4 (GC4)** supports communication through different languages, and **Computing-Specific Competency 6 for High School (CE6)** supports expressing and sharing computational ideas and solutions. These are **GeneralFrameworkAlignment** contributions, not equivalences.

| Competency | Contribution to GC4 and CE6 |
|---|---|
| CM10 | Coordinates explanation of data, updates, decisions, repetition and functions as one solution |
| CM12 | Communicates how arithmetic expressions are evaluated |
| CM13 | Communicates how data is organized and accessed |
| CM14 | Communicates the relationship between conditions and executed actions |
| CM15 | Communicates the control of repeated execution |
| CM16 | Communicates responsibilities and data exchange between functions |
| CM17 | Communicates how values are represented and updated |

A conditional **PartialAlignment** with **EM13CO19** applies when an explanation uses code or program execution as digital presentation resources. Each competency contributes a bounded explanatory aspect of the product; none alone establishes negotiation or the complete media/tool scope. Ordinary oral or paper explanation alone does not establish the digital-resource condition.

The decomposition and aggregation do not add new external equivalences. CM10 has the same qualified GC4/CE6 framework contributions and conditional partial EM13CO19 alignment; composition does not establish full external-skill coverage. It makes the previously recorded communication alignment traceable to the resulting performances.


## 4. Updated TASK401 activation associations

CM01-CM09 remain directly associated with the task. The composite CM10 replaces separate direct explanatory associations with CM13-CM17. CM12 remains a conditional extension.

| Code | Activation constraint | Activation mode | Activation role | Condition or requirement | Main evidence |
|---|---|---|---|---|---|
| CM01 | conditional | analytical | supporting | Explicit requirements-analysis question or activity | Relationship between rules, inputs and expected behavior |
| CM02 | mandatory | constructive | core | Data representation and updates required | Code and individual update demonstration |
| CM03 | mandatory | constructive | core | Decisions required by the game rules | Conditions and branches exercised with contrasting cases |
| CM04 | mandatory | constructive | core | Repetition and termination required | Loop continuation and termination |
| CM05 | mandatory | constructive | core | User interaction required | Input/output demonstration |
| CM06 | mandatory | constructive | core | Invalid-input and illegal-move rejection required | Rejection and preservation of valid state |
| CM07 | mandatory | analytical;constructive | core | Function organization explicitly required by this adjustment | Responsibilities, data exchange and integration |
| CM08 | conditional | operational;evaluative | core | Explicit verification against expected results requested | Test record and conclusion |
| CM09 | conditional | analytical | supporting | Failure observed or provided for diagnosis | Relevant execution steps and causal explanation |
| CM10 | mandatory | explanatory | core | Complete individual explanation, including function organization, required by this adjustment | Coordinated explanation satisfying all five component criteria |
| CM12 | conditional | explanatory | extension | Arithmetic expression present and its explanation requested | Explanation of operands, precedence and result |

`mandatory` identifies a required performance; `conditional` identifies dependence on the stated condition. Modes describe how competencies are mobilized. `core`, `supporting` and `extension` describe their task roles. These are prospective task-specification records, not demonstrated learner mastery.

CM07's implementation performance and CM10's explanatory performance are distinct. Requiring functions makes CM07 mandatory but does not automatically evidence its Create pairing: independently designed organization must still be demonstrated for that level.


