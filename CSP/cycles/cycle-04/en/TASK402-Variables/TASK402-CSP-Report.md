# TASK402 - CSP Report

## 1. Context and specification scope

**Task:** Variable Manipulation - execution tracing of a C program.  
**Target audience:** learners in introductory programming, including upper secondary technical education in Informatics.  
**Task creator:** Prof. Marcos Bião, MSc, Univasf - Salgueiro Campus.  
**Contributors listed in the task:** Edeyson Gomes and Jéssica Santana.

This report follows the simplified structure used for TASK401. Knowledge remains at curricular-topic level; competency definitions and operations are independent of the example program. The school year and actual application cycle of TASK402 are not established by the supplied description.

**Catalog decision:** CM11 retains its tracing specification. New composite **CM18 - Explain variable updates and arithmetic evaluation** replaces the former TASK402 association with CM10. Its complete components, CM17 and CM12, reuse the definitions and KS pairs recorded in the TASK401 adjustment. No identities from CSP Cycles 1-3 are reused.

### Task requirements

Given inputs 10, 15, 20 and 25, the learner follows successive assignments and arithmetic expressions in a C program and selects the alternative corresponding to the final values of `a`, `b`, `c` and `d`.

The source task uses the corrected `%f` input format for `float` variables and assumes successful input. The selected alternative is the original deliverable. A table of variable values after each assignment is recommended supplementary evidence. An explanation can also be requested to make the reasoning observable.

The task concerns interpreting supplied code, not constructing a program or diagnosing a defect. A selected alternative alone is insufficient to establish the learner's execution-tracing procedure.

## 2. Knowledge anchored in curricular topics

The five knowledge areas use the identifiers already adopted for TASK401. Their curricular anchors refer to the supplied Algorithms and Programming Logic course plan as a terminology reference, not evidence that TASK402 was applied in that specific course or class.

| ID | Knowledge area | Curricular anchor | TASK402 application |
|---|---|---|---|
| K01 | Algorithms: concept, properties and construction | 2. Algorithms | Follow the ordered execution of the supplied instructions |
| K03 | Data types, constants and variables | 4. Fundamentals | Interpret numeric values stored in `float` variables |
| K04 | Arithmetic and literal expressions | 4. Fundamentals | Evaluate arithmetic expressions with operator precedence |
| K05 | Assignment statements | 4. Fundamentals | Determine the value stored after each assignment |
| K06 | Input and output statements | 4. Fundamentals | Interpret the values read by `scanf` using `%f` |

Only the relevant aspects of each topic are mobilized: algorithm construction, literal expressions and output statements are not required merely because they belong to these broader knowledge areas. Sequential execution and operator precedence are details within the curricular topics, not separate knowledge identities. Format compatibility is background knowledge for interpreting the corrected input, not a debugging objective.

## 3. Implicit learning objectives

| Code | Objective | Bloom level |
|---|---|---|
| LO1 | Determine variable values after successive assignments, respecting execution order. | Apply |
| LO2 | Evaluate arithmetic expressions using current values and operator precedence. | Apply |
| LO3 | Simulate sequential program execution and determine its final state. | Apply |

CM11 integrates these objectives. When individual explanation is requested, CM18 additionally requires explaining how assignment updates and arithmetic evaluation jointly produce the result. An unexplained answer or trace table does not establish that explanatory performance.

## 4. Competency specifications

### CM11 - Trace program execution

**Definition:** determine successive control steps and data values for specified inputs by following the program's execution rules.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K01 - Algorithms | Apply | Follow instructions in execution order to determine successive states. |
| K03 - Data types, constants and variables | Understand | Interpret the types and values used by the program. |
| K05 - Assignment statements | Apply | Determine variable values after successive assignments using current values. |
| K04 - Arithmetic and literal expressions | Apply | Evaluate arithmetic expressions according to operator precedence and current operand values. |
| K06 - Input and output statements | Understand | Interpret the input operations and the values supplied to the program. |

**TASK402 manifestation:** follow the assignments to `a`, `b`, `c` and `d`, calculate the subsequent expressions and determine the final values.

**TASK402 evidence and criterion:** selected alternative and, when collected, a table or explanation of successive states; the learner uses updated values, respects assignment order and operator precedence, and obtains a final state consistent with the instructions. The supplementary record supports attribution of the procedure to the individual learner.

**Disposition:** meticulous.

**Alignment:**

BNCC General Competency 2 (GC2) supports examining and solving problems through systematic reasoning. Computing-Specific Competency 1 for High School (CE1) supports analyzing computational solutions. These are **GeneralFrameworkAlignment** contributions rather than equivalences.



### Reused atomic components

The definitions and constitutive KS pairings below are unchanged from `TASK401-CSP-Adjustment.md`. Only task manifestations and evidence are contextualized.

### CM12 - Explain arithmetic expression evaluation

**Type:** atomic; reused catalog specification.

**Definition:** explain how arithmetic expressions produce values according to their operands and operator precedence.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K04 - Arithmetic and literal expressions | Understand | Explain how operand values and operator precedence determine an arithmetic expression's result. |

**TASK402 manifestation:** explain the operand values and precedence in `a + b / 2`, `c + b` and `d + (b * 2) - a`.

**Evidence and criterion:** individual explanation, when requested; the explanation correctly relates operand values, operator precedence and the expression result. This pairing targets the arithmetic aspect of K04, not literal-expression performance.

**Disposition:** communicative and meticulous.



### CM17 - Explain variable updates

**Type:** atomic; reused catalog specification.

**Definition:** explain how variable values are represented and changed by assignment statements.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K03 - Data types, constants and variables | Understand | Explain the role of data types, constants and variables in representing values. |
| K05 - Assignment statements | Understand | Explain how an assignment determines the newly stored value using the values available at that step. |

**TASK402 manifestation:** explain how successive assignments replace the values of `a`, `b`, `c` and `d`, distinguishing initial and current values.

**Evidence and criterion:** individual explanation, when requested; the explanation correctly relates the numeric type, represented values and assignment updates using the values available at each step.

**Disposition:** communicative and meticulous.



### CM18 - Explain variable updates and arithmetic evaluation

**Type:** composite competency.

**Definition:** explain how variable updates and arithmetic expression evaluation jointly determine values during program execution.

**Components:** CM17 - Explain variable updates and CM12 - Explain arithmetic expression evaluation. Both are constitutive; neither is optional.

| Component | Constitutive KS pairs | Contribution |
|---|---|---|
| CM17 | K03 × Understand; K05 × Understand | Explain represented values and assignment updates |
| CM12 | K04 × Understand | Explain operand values and operator precedence |

The complete KS set is K03, K04 and K05, each paired with Understand. Composition preserves both atoms' complete pairings; no task-specific selection of internal pairs is introduced. K01 and K06 remain part of the tracing context through CM11, not additional pairs of CM18.

**TASK402 manifestation:** explain how assignments change the values used in subsequent arithmetic expressions and how these expressions produce the final variable values.

**Evidence and criterion:** an individual oral or written explanation, when requested; both component criteria are satisfied and their relationship is explained coherently. A selected answer or unexplained trace table alone does not establish CM18. Missing evidence for one component means the complete composite is not fully evidenced.

**Disposition:** communicative and meticulous.

**Alignment:** BNCC General Competency 4 (GC4) supports communication, and Computing-Specific Competency 6 for High School (CE6) supports sharing computational ideas and solutions. These are GeneralFrameworkAlignment contributions. A conditional PartialAlignment with EM13CO19 applies when digital resources are used to present the solution; negotiation and the full media/tool scope are not established. The same qualified alignment applies to each explanatory atom within its own scope.



## 5. Competency activation and evidence

| Code | Activation constraint | Activation mode | Activation role | Condition or requirement | Main evidence |
|---|---|---|---|---|---|
| CM11 | mandatory | operational | core | Determine the result by following the supplied program | Selected alternative; a trace record strengthens evidence of the procedure |
| CM18 | conditional | explanatory | supporting | Individual explanation of updates and arithmetic evaluation is requested | Coordinated explanation satisfying both component criteria |

`mandatory` means required by the task; `conditional` means dependent on the stated assessment addition. Modes describe the operation performed, and roles distinguish the core task from complementary explanation. Intended activation does not establish individual mastery.

CM12 and CM17 remain catalog components, not additional direct task associations. Composite and component results must not be counted as independent achievements from the same evidence. There are two direct task associations and two composition links.

### Performance criteria

- **Initial:** recognizes statements but makes recurring errors when tracking updates.
- **Developing:** determines some states correctly, with inconsistencies in assignments or expression evaluation.
- **Expected:** determines successive states and the final result correctly, demonstrating the procedure when supplementary evidence is collected. If CM18 is assessed, the learner also explains the relationship between updates and arithmetic evaluation.

These levels describe task performance, not general programming proficiency. Apply characterizes carrying out a trace; Understand characterizes the explanatory KS pairs. Analyze is not inferred merely from examining source code.

## 6. Consolidated BNCC alignment and reuse

GC denotes a BNCC General Competency for Basic Education and CE a Computing-Specific Competency for High School. These are local abbreviations; EM13COxx are official skill codes.

| Direct association | General BNCC | Computing-specific | Skill alignment |
|---|---|---|---|
| CM11 | GC2 - Investigation and problem solving | CE1 - Analysis of computational solutions | No direct EM13CO alignment asserted for baseline tracing |
| CM18 | GC4 - Communication | CE6 - Expression and sharing of computational solutions | EM13CO19: conditional partial |

Framework contribution is not equivalence. Ordinary oral or paper explanation alone does not establish EM13CO19's digital-resource condition. Tracing does not itself establish refinement from specification to implementation or software evaluation by characteristics and measures.

