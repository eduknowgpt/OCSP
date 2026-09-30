# TASK25.20 – CSP-Report

## Introduction

This CSP-Report documents the competency specification of **TASK25.20 – Tic-Tac-Toe Implementation**, an introductory programming task situated in the **Programming Logic** course of the **Integrated Technical Program in Informatics (1st year)** at **IFBA – Valença Campus**.

The task requires learners to design, implement, test, debug, and explain a complete **3×3 Tic-Tac-Toe game**, using structured programming concepts such as data representation, conditionals, loops, functions, input validation, and execution tracing. The development is collaborative, but **individual accountability is ensured through an oral explanation of the implemented solution**. 

From the perspective of **OntoKSD**, TASK25.20 is relevant because it supports the specification of reusable, mostly atomic competencies, while also enabling qualified alignment with external curricular references, especially the **BNCC Computing Complement**.





## 1. Instructional Entity Analysis

### Title

    Tic-Tac-Toe Implementation (3×3)

### Description

Learners must implement a complete Tic-Tac-Toe game in which two human players alternate turns using the symbols **X** and **O**. The program must represent the board, validate user input, enforce legal moves, detect victory conditions, detect draw situations, and display the board state during execution.


### Expected Evidence

The task produces three main types of evidence:

1. **Source code**, representing the implemented computational artifact.
2. **Program execution**, demonstrating functional correctness and robustness.
3. **Individual oral explanation**, demonstrating conceptual understanding, authorship, and ability to justify implementation decisions. 


### Assessment Design Note

The requirement of an individual oral explanation is motivated by the growing use of AI-assisted programming tools. While such tools can support code production, they may obscure the learner’s actual understanding and authorship.

To mitigate this, TASK25.20 includes an individual oral defense in which *each learner must explain, justify, and trace the implemented solution*. This ensures that competence evidencing remains learner-specific, even when the produced artifact is collaborative or AI-assisted.



### OntoKSD Analytical Note

TASK25.20 should be modeled as a `LearningTask`. Its evidential structure is especially relevant because the source code may be produced collaboratively, while the oral explanation enables learner-specific evidence of competence.





## 2. Knowledge Enumeration

### 2.1 Fundamental Programming Knowledge

- **Algorithmic reasoning**
- **Variables and basic data handling**
- **Input and output operations**

### 2.2 Data Representation Knowledge

- **Lists and matrices**
- **State representation**

### 2.3 Control-Flow Knowledge

- **Conditional structures**
- **Repetition structures**
- **Logical and relational operators**

### 2.4 Modularization Knowledge

- **Functions, parameters, and return values**
- **Problem decomposition**
- **Variable scope**

### 2.5 Testing and Debugging Knowledge

- **Testing scenarios**
- **Debugging strategies**
- **Execution trace analysis**

### 2.6 Communication and Authorship Knowledge

- **Technical programming vocabulary**
- **Ethical authorship**
- **Oral communication**





## 3. Learning Objectives

By the end of TASK25.20, the learner should be able to:

1. **Describe** the behavior and execution flow of a Tic-Tac-Toe program.
2. **Represent** the game board using structured data formats.
3. **Control** program execution using conditionals and loops.
4. **Decompose** the program into cohesive functions.
5. **Validate** user input and preserve state consistency.
6. **Test and debug** the program using representative scenarios.
7. **Explain and justify** the implemented solution orally.
8. **Demonstrate ethical authorship** in a collaborative programming context.



# 4. Competency Definition

## General Competency

**Design, implement, test, debug, and explain introductory structured programming solutions in a collaborative and ethically accountable context.**

### General BNCC Alignment

This general competency is supported by broader BNCC Computing competencies for High School, especially those related to analyzing and constructing computational solutions, producing computational artifacts, developing projects collaboratively, communicating computational ideas, and acting ethically and responsibly. These broader correspondences should be represented as `GeneralFrameworkAlignment`, not as strict equivalences.





## Competency CT25.20.1 Specification

### Competency Title

    Analyze a programming problem and derive implementable requirements.

### Textual Description

This competency involves analyzing a concrete computational problem in order to identify relevant rules, constraints, and expected behaviors, transforming them into implementable requirements that guide design and coding decisions.

In TASK25.20, the learner identifies valid moves, turn alternation, victory conditions, draw situations, and termination criteria.

### Knowledge–Skill Pairing

| Knowledge | Bloom Level | Verbs |
|---|---|---|
| Algorithmic Reasoning | Analyze | Analyze, identify, derive, examine |
| Problem Decomposition | Analyze | Decompose, structure, organize, relate |



### Dispositions

- **Meticulous**
- **Investigative**



### Activation

| Dimension | Value |
|---|---|
| ActivationConstraint | mandatory |
| ActivationMode | analytical |
| ActivationRole | supporting |



### BNCC Alignment

| BNCC Reference | Alignment Type | Justification |
|---|---|---|
| High School Computing Competency 1 | `GeneralFrameworkAlignment` | The competence supports the broader BNCC goal of understanding and analyzing computational solutions. |
| High School Computing Competency 5 | `GeneralFrameworkAlignment` | The competence contributes to project-based solution development in collaborative contexts. |
| EM13CO02 | `CloseAlignment` | The competence directly supports refinement from specification to implementation. |
| EM13CO01 | `PartialAlignment` | Reuse or adaptation may occur, but it is not central to the task. |










## Competency CT25.20.2 Specification

### Competency Title

    Represent information and program state using structured data formats.

### Textual Description

This competency involves modeling relevant elements of a problem domain using appropriate structured data representations, so that program information can be stored, accessed, updated, and interpreted consistently.

In TASK25.20, the learner represents the Tic-Tac-Toe board and its evolving state through lists, nested lists, matrices, or equivalent indexed structures.

### Knowledge–Skill Pairing

| Knowledge | Bloom Level | Verbs |
|---|---|---|
| Data Structures | Apply | Represent, store, access, update |
| State Representation | Apply | Model, organize, maintain, reflect |
| Analytical Thinking | Analyze | Analyze, distinguish, relate, organize |

### Dispositions

- **Meticulous**
- **Collaborative**

### Activation

| Dimension | Value |
|---|---|
| ActivationConstraint | mandatory |
| ActivationMode | constructive |
| ActivationRole | core |

### BNCC Alignment

| BNCC Reference | Alignment Type | Justification |
|---|---|---|
| High School Computing Competency 1 | `GeneralFrameworkAlignment` | The competence supports the broader construction and analysis of computational solutions. |
| High School Computing Competency 4 | `GeneralFrameworkAlignment` | The competence contributes to producing computational artifacts using appropriate techniques. |
| EM13CO02 | `NarrowerThanExternalAlignment` | This competence addresses a specific part of the broader BNCC refinement process: data and state representation. |
| EF04CO01 | `CurricularContinuityAlignment` | Matrix-based board representation continues prior curricular work with coordinate-based matrix structures. |
| EF15CO01 | `CurricularContinuityAlignment` | Structured information representation is a prior-stage foundation for this competence. |








## Competency CT25.20.3 Specification

### Competency Title

    Control program execution using conditional and repetition structures.

### Textual Description

This competency involves controlling the dynamic behavior of a program by applying conditional and repetition structures that govern decisions, iteration, and termination.

In TASK25.20, the learner uses conditionals and loops to alternate turns, validate whether actions can proceed, maintain the game cycle, and terminate execution when a winning or draw condition is reached.

### Knowledge–Skill Pairing

| Knowledge | Bloom Level | Verbs |
|---|---|---|
| Conditional Structures | Apply | Select, decide, validate, determine |
| Repetition Structures | Apply | Iterate, repeat, maintain, control |
| Logical Reasoning | Apply | Compare, test, combine, express |

### Dispositions

- **Meticulous**
- **Persistent**
- **Collaborative**

### Activation

| Dimension | Value |
|---|---|
| ActivationConstraint | mandatory |
| ActivationMode | constructive |
| ActivationRole | core |

### BNCC Alignment

| BNCC Reference | Alignment Type | Justification |
|---|---|---|
| High School Computing Competency 1 | `GeneralFrameworkAlignment` | The competence contributes to building computational solutions. |
| EM13CO02 | `NarrowerThanExternalAlignment` | This competence represents a specific implementation-level aspect of solution refinement. |
| EF69CO02 | `CurricularContinuityAlignment` | It continues prior curricular work with sequence, repetition, and selection in programming languages. |
| EF15CO02 | `CurricularContinuityAlignment` | It builds on earlier construction and simulation of algorithms with selections and repetitions. |







## Competency CT25.20.4 Specification

### Competency Title

    Decompose programs into cohesive and independent functions.

### Textual Description

This competency involves structuring a program modularly by decomposing a computational solution into coherent functions with clearly delimited responsibilities.

In TASK25.20, this includes functions for displaying the board, reading moves, validating actions, checking outcomes, and coordinating the main game loop.

### Knowledge–Skill Pairing

| Knowledge | Bloom Level | Verbs |
|---|---|---|
| Function Design | Create | Design, define, encapsulate, compose |
| Problem Decomposition | Apply | Decompose, separate, assign, organize |
| Variable Scope | Apply | Differentiate, apply, maintain, control |

### Dispositions

- **Meticulous**
- **Collaborative**

### Activation

| Dimension | Value |
|---|---|
| ActivationConstraint | mandatory |
| ActivationMode | constructive |
| ActivationRole | core |

### BNCC Alignment

| BNCC Reference | Alignment Type | Justification |
|---|---|---|
| High School Computing Competency 4 | `GeneralFrameworkAlignment` | Modularization supports production of computational artifacts with organization and quality. |
| High School Computing Competency 5 | `GeneralFrameworkAlignment` | Modular decomposition supports collaborative project development. |
| EM13CO02 | `NarrowerThanExternalAlignment` | This competence captures one specific aspect of refinement from specification to implementation. |
| EF15CO04 | `CurricularContinuityAlignment` | It continues prior curricular work on decomposition of complex problems. |







## Competency CT25.20.5 Specification

### Competency Title

    Test and debug programs using representative scenarios and execution tracing.

### Textual Description

This competency involves verifying program behavior systematically, identifying faults, and refining the implementation through testing, debugging, and execution tracing.

In TASK25.20, the learner tests valid moves, invalid inputs, victory conditions, draw situations, and unexpected behaviors, correcting logical or runtime problems when found.

### Knowledge–Skill Pairing

| Knowledge | Bloom Level | Verbs |
|---|---|---|
| Testing | Apply | Test, verify, exercise, check |
| Debugging | Apply | Debug, correct, refine, adjust |
| Execution Tracing | Analyze | Trace, diagnose, inspect, identify |

### Dispositions

- **Persistent**
- **Meticulous**

### Activation

| Dimension | Value |
|---|---|
| ActivationConstraint | mandatory |
| ActivationMode | analytical |
| ActivationRole | core |

### BNCC Alignment

| BNCC Reference | Alignment Type | Justification |
|---|---|---|
| High School Computing Competency 1 | `GeneralFrameworkAlignment` | Testing and debugging support the construction and analysis of computational solutions. |
| High School Computing Competency 4 | `GeneralFrameworkAlignment` | Program verification contributes to artifact quality. |
| EM13CO02 | `NarrowerThanExternalAlignment` | Testing and debugging are specific refinement practices within the broader specification-to-implementation process. |
| EF07CO02 | `CurricularContinuityAlignment` | This is a strong prior-stage reference for analyzing programs to detect and remove errors. |







## Competency CT25.20.6 Specification

### Competency Title

    Explain and justify computational solutions with ethical authorship.

### Textual Description

This competency involves explaining, justifying, and defending a computational solution, demonstrating conceptual understanding, clear communication, and ethical responsibility for the produced artifact.

In TASK25.20, each learner orally explains the structure and behavior of the implemented program, justifies implementation decisions, traces execution flow, and accounts honestly for their own contribution to the collaborative work.

### Knowledge–Skill Pairing

| Knowledge | Bloom Level | Verbs |
|---|---|---|
| Technical Programming Vocabulary | Understand | Explain, interpret, describe, clarify |
| Logical Explanation | Apply | Justify, connect, support, demonstrate |
| Oral Communication | Apply | Communicate, present, articulate, respond |
| Ethical Authorship | Apply | Acknowledge, account for, represent, justify |

### Dispositions

- **Ethical**
- **Communicative**
- **Responsible**

### Activation

| Dimension | Value |
|---|---|
| ActivationConstraint | mandatory |
| ActivationMode | justificatory |
| ActivationRole | supporting |

### BNCC Alignment

| BNCC Reference | Alignment Type | Justification |
|---|---|---|
| High School Computing Competency 4 | `GeneralFrameworkAlignment` | The competence supports responsible production and explanation of computational artifacts. |
| High School Computing Competency 6 | `GeneralFrameworkAlignment` | The competence supports expression and sharing of computational ideas and solutions. |
| High School Computing Competency 7 | `GeneralFrameworkAlignment` | The competence supports ethical and responsible action. |
| EM13CO19 | `CloseAlignment` | The oral explanation directly involves exposing and arguing about a computational product. |
| EM13CO21 | `PartialAlignment` | The competence partially overlaps with clear communication of complex ideas, although the task does not require the specific digital objects mentioned by BNCC. |






## 5. External Alignment Modeling Note

The BNCC correspondences in this report should be represented as **qualified curricular alignments**, not as undifferentiated equivalences.

In OntoKSD, the direct property `ontoksd:alignedWith` may be used for simplified links between an OntoKSD competence and an external competence. However, when the nature of the alignment matters, a qualified alignment relator should be used with an explicit `AlignmentType`.

The following alignment types are relevant for this task and for other BNCC mappings:

| Alignment Type | Meaning |
|---|---|
| `EquivalentAlignment` | The internal and external competences have essentially equivalent scope and intent. |
| `CloseAlignment` | The competences correspond strongly, but strict equivalence is not asserted. |
| `PartialAlignment` | The competences overlap only partially. |
| `BroaderThanExternalAlignment` | The OntoKSD competence is broader than the external competence. |
| `NarrowerThanExternalAlignment` | The OntoKSD competence is narrower than the external competence. |
| `CurricularContinuityAlignment` | The external competence represents a prior-stage curricular antecedent or developmental precursor. |
| `GeneralFrameworkAlignment` | The external reference provides broader curricular support rather than fine-grained skill equivalence. |

This distinction is important because a relation such as:

    CT25.20.2 alignedWith EM13CO02

does not have the same meaning as:

    CT25.20.2 alignedWith EF04CO01

The former is a high-school-level alignment with a broader BNCC skill, while the latter expresses curricular continuity with a prior-stage representation skill.





## 6. Evidence and Assessment Interpretation

TASK25.20 supports three evidential layers in OntoKSD:

### 6.1 Artifact-Level Evidence

The source code represents the produced computational artifact.

### 6.2 Performance-Level Evidence

The program execution demonstrates whether the artifact behaves correctly under representative conditions.

### 6.3 Learner-Level Evidence

The oral explanation enables learner-specific interpretation of understanding, authorship, and justification. 

This evidential distinction is important because the task is developed collaboratively, while part of the assessment is individualized.





## 7. Summary Table

| Code | Competency Title | Main Role | Activation Mode | Main BNCC Alignment Type |
|---|---|---|---|---|
| CT25.20.1 | Analyze a programming problem and derive implementable requirements | Supporting | Analytical | Close / Partial / GeneralFramework |
| CT25.20.2 | Represent information and program state using structured data formats | Core | Constructive | NarrowerThanExternal / CurricularContinuity |
| CT25.20.3 | Control program execution using conditional and repetition structures | Core | Constructive | NarrowerThanExternal / CurricularContinuity |
| CT25.20.4 | Decompose programs into cohesive and independent functions | Core | Constructive | NarrowerThanExternal / CurricularContinuity |
| CT25.20.5 | Test and debug programs using representative scenarios and execution tracing | Core | Analytical | NarrowerThanExternal / CurricularContinuity |
| CT25.20.6 | Explain and justify computational solutions with ethical authorship | Supporting | Justificatory | Close / Partial / GeneralFramework |





## Summary Tables for TASK25.20 Competencies

### CT25.20.1 — Analyze a programming problem and derive implementable requirements

| Code      | Competency                                                           | Dispositions              | Knowledge             | Skill   |
| --------- | -------------------------------------------------------------------- | ------------------------- | --------------------- | ------- |
| CT25.20.1 | Analyze a programming problem and derive implementable requirements. | Meticulous, Investigative | Algorithmic Reasoning | Analyze |
| CT25.20.1 | Analyze a programming problem and derive implementable requirements. | Meticulous, Investigative | Problem Decomposition | Analyze |



### CT25.20.2 — Represent information and program state using structured data formats

| Code      | Competency                                                             | Dispositions              | Knowledge            | Skill   |
| --------- | ---------------------------------------------------------------------- | ------------------------- | -------------------- | ------- |
| CT25.20.2 | Represent information and program state using structured data formats. | Meticulous, Collaborative | Data Structures      | Apply   |
| CT25.20.2 | Represent information and program state using structured data formats. | Meticulous, Collaborative | State Representation | Apply   |
| CT25.20.2 | Represent information and program state using structured data formats. | Meticulous, Collaborative | Analytical Thinking  | Analyze |



### CT25.20.3 — Control program execution using conditional and repetition structures

| Code      | Competency                                                             | Dispositions                          | Knowledge              | Skill |
| --------- | ---------------------------------------------------------------------- | ------------------------------------- | ---------------------- | ----- |
| CT25.20.3 | Control program execution using conditional and repetition structures. | Meticulous, Persistent, Collaborative | Conditional Structures | Apply |
| CT25.20.3 | Control program execution using conditional and repetition structures. | Meticulous, Persistent, Collaborative | Repetition Structures  | Apply |
| CT25.20.3 | Control program execution using conditional and repetition structures. | Meticulous, Persistent, Collaborative | Logical Reasoning      | Apply |



### CT25.20.4 — Decompose programs into cohesive and independent functions

| Code      | Competency                                                  | Dispositions              | Knowledge             | Skill  |
| --------- | ----------------------------------------------------------- | ------------------------- | --------------------- | ------ |
| CT25.20.4 | Decompose programs into cohesive and independent functions. | Meticulous, Collaborative | Function Design       | Create |
| CT25.20.4 | Decompose programs into cohesive and independent functions. | Meticulous, Collaborative | Problem Decomposition | Apply  |
| CT25.20.4 | Decompose programs into cohesive and independent functions. | Meticulous, Collaborative | Variable Scope        | Apply  |



### CT25.20.5 — Test and debug programs using representative scenarios and execution tracing

| Code      | Competency                                                                    | Dispositions           | Knowledge         | Skill   |
| --------- | ----------------------------------------------------------------------------- | ---------------------- | ----------------- | ------- |
| CT25.20.5 | Test and debug programs using representative scenarios and execution tracing. | Persistent, Meticulous | Testing           | Apply   |
| CT25.20.5 | Test and debug programs using representative scenarios and execution tracing. | Persistent, Meticulous | Debugging         | Apply   |
| CT25.20.5 | Test and debug programs using representative scenarios and execution tracing. | Persistent, Meticulous | Execution Tracing | Analyze |



### CT25.20.6 — Explain and justify computational solutions with ethical authorship

| Code      | Competency                                                           | Dispositions                        | Knowledge                        | Skill      |
| --------- | -------------------------------------------------------------------- | ----------------------------------- | -------------------------------- | ---------- |
| CT25.20.6 | Explain and justify computational solutions with ethical authorship. | Ethical, Communicative, Responsible | Technical Programming Vocabulary | Understand |
| CT25.20.6 | Explain and justify computational solutions with ethical authorship. | Ethical, Communicative, Responsible | Logical Explanation              | Apply      |
| CT25.20.6 | Explain and justify computational solutions with ethical authorship. | Ethical, Communicative, Responsible | Oral Communication               | Apply      |
| CT25.20.6 | Explain and justify computational solutions with ethical authorship. | Ethical, Communicative, Responsible | Ethical Authorship               | Apply      |

