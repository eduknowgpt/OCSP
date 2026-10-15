# CSP-Report — TASK25.05 — Online Judges at Logistic Solutions

## 1. Introduction

TASK25.05 examines automated program evaluation through finite-state modeling, computational complexity, computability, and the limits of program analysis. The scenario concerns persistent TLE results for TSP and timetabling submissions and questions about what an Online Judge can evaluate, predict, or diagnose.

### 1.1 Purpose within Cycle 3

Cycle 3 was designed around reuse of mature competency specifications, with discussion among task authors, specifiers, and reviewers during task development. TASK25.05 retains the relevant specifications associated with Task204 and places complexity analysis through C21 at the center alongside C15. C21 was created for TASK25.05 in Cycle 3 (2025) to specify the analysis of computational complexity, scalability, and the implications of NP-hardness. The other seven competencies are reused from earlier CSP applications.

### 1.2 Comparison with Task204

Task204 focused on TSP, FSM modeling of the OJ, and theoretical limits related to termination. TASK25.05 adds timetabling, input-size and algorithmic-strategy considerations, and a broader analysis of TLE diagnosis. It distinguishes practical performance constraints from general limits of automated reasoning. C15 remains central, while C21 explicitly represents the complexity dimension.

### 1.3 Integrated Specification

This report integrates instructional analysis and the specification decisions developed through discussion during task preparation. Competency descriptions, contextual activation, and objective associations document the resulting specification.

## 2. Instructional Entity Analysis

- Title: Online Judges at Logistic Solutions.
- Type: Problem-based task emphasizing formal modeling, complexity analysis, and computational limitations.
- Domain: Theory of Computation — Finite-State Models, Computability, and Computational Complexity.

Students analyze observed OJ outcomes, formulate grounded explanations of TLE, discuss strategies for meeting execution limits, and build an FSM describing the evaluation workflow. They also answer the startup managers' questions about problem classes and the limits of behavioral diagnosis.

AC denotes acceptance on the judge's tests, not proof of correctness for all possible inputs. TLE is an observed limit violation whose cause requires analysis; complexity, implementation choices, and nontermination are distinct explanatory possibilities. The task does not prescribe a single cause.

## 3. Expected Outcomes and Evidence

- An SBC-format article analyzing TSP and PT submissions, computational difficulties, and proposed strategies.
- Reasoned responses to the managers about practical capabilities and theoretical limitations.
- An FSM diagram illustrating evaluation states and transitions, with an explanation of its abstraction and limits.
- Examples and arguments connecting execution constraints with complexity and computability.
- FSM simulation when applicable under the report's C03 association; simulator use remains listed in the task objectives.

The extra challenge is evaluation of TSP and PT code in an OJ for different input sizes. It remains additional, rather than a newly mandatory deliverable. No separate JFLAP file requirement is introduced where the task specifies an FSM representation.

## 4. Knowledge Enumeration

### 4.1 Computing Knowledge

- Finite State Machines: states, transitions, and observable evaluation workflows.
- Computational Complexity: time growth, P, NP, NP-hardness, NP-completeness, and scalability.
- Computability: the Halting Problem and general limits of automated program analysis.
- Turing Machines and Recursively Enumerable Languages: conceptual reference models for capabilities and limits.
- Automated Program Evaluation: interpretation of AC, WA, CE, RE, and TLE in relation to algorithms and execution conditions.

Complexity statements require a specified problem variant and assumptions. NP-hardness concerns a problem class and does not determine the running time of every instance or implementation. Approximate or heuristic approaches must also be assessed against the judge's acceptance criteria; they do not automatically yield AC.

### 4.2 Foundational and Professional Knowledge

- Analytical and Critical Thinking: connect observations to justified explanations while distinguishing practical and theoretical limits.
- Written Communication: present models, arguments, examples, and references coherently.

## 5. Learning Objectives

### General Objective

Apply Theory of Computation concepts to model and explain Online Judges, connecting finite-state workflows, computational complexity, and theoretical limits of program analysis.

### Specific Objectives

- LO1 — Explain the evaluation workflow through an FSM with states and transitions associated with outcomes such as AC, WA, CE, RE, and TLE.
- LO2 — Analyze TLE results for TSP and PT in relation to complexity, input size, and algorithmic choices.
- LO3 — Discuss strategies for meeting OJ limits and achieving acceptance on difficult problems.
- LO4 — Explain general theoretical limitations of automated analysis and prediction of program behavior.
- LO5 — Interpret Turing Machine and computability concepts in relation to OJ capabilities and limits.
- LO6 — Communicate the analyses and conclusions in a rigorous technical article.
- LO7 — Simulate and examine the OJ FSM when applicable, using tools such as JFLAP.
- LO8 — Relate the analysis to computational complexity and appropriately formulated NP-complete problems.

These eight objectives consolidate the eleven specific objectives in the task statement. LO8 expresses the complexity classification dimension. Conditional and optional associations are specified in the activation summary.

## 6. Competency Specifications

### C21 — Analyze Computational Complexity and the Implications of NP-Hardness

Origin: TASK25.05 — Cycle 3 (2025). Created for this task.

#### Competency Description

Analyze computational complexity and interpret the implications of NP-hardness for scalability, performance limits, and the practical feasibility of algorithmic solutions.

#### Contextual Application

Relate TSP and PT submissions to input size, algorithmic strategy, and execution limits. Distinguish inefficient implementation from inherent problem difficulty. Identify the problem formulation before assigning a complexity class: standard decision TSP is NP-complete, while its optimization form is NP-hard; timetabling classifications depend on the stated constraints and formulation. NP-hardness does not establish that every instance times out or that efficient exact algorithms have been proved impossible. This analytical competence does not add algorithm construction or reduction proofs as requirements.

#### Knowledge–Skill Pairing

- Computational Complexity — Analyze (*Decompose, Relate, Interpret*).
- Complexity Classes and Intractability (P, NP, NP-hard, NP-complete) — Understand (*Explain, Distinguish, Justify*).
- Algorithmic Scalability (Conceptual Perspective) — Understand (*Relate, Interpret, Explain*).
- Analytical and Critical Thinking (FPK) — Analyze (*Evaluate, Structure, Argue*).

#### Dispositions

Collaborative, Responsible, Proactive, Creative.

#### Activation

- ActivationRole: `core`
- ActivationMode: `analytical`
- ActivationConstraint: `mandatory`

#### Summary Table for Competency C21

| Competency | Dispositions | Knowledge | Skill |
| --- | --- | --- | --- |
| Analyze Computational Complexity and the Implications of NP-Hardness | Collaborative, Responsible, Proactive, Creative | Computational Complexity | Analyze (*Decompose, Relate, Interpret*) |
|  |  | Complexity Classes and Intractability (P, NP, NP-hard, NP-complete) | Understand (*Explain, Distinguish, Justify*) |
|  |  | Algorithmic Scalability (Conceptual Perspective) | Understand (*Relate, Interpret, Explain*) |
|  |  | Analytical and Critical Thinking (FPK) | Analyze (*Evaluate, Structure, Argue*) |

### C15 — Understand the Halting Problem and its Implications

Origin: Task204 — Cycle 2.

#### Competency Description

Explain the Halting Problem and the general limits it places on algorithmic analysis of arbitrary programs and inputs.

#### Contextual Application

Explain why there is no general procedure deciding termination for every arbitrary program and input. TLE means a time limit was exceeded, not that nontermination has been proved. Particular causes can sometimes be diagnosed; general undecidability should not be used to claim that every diagnosis is impossible. Conceptual reasoning and theoretical justification remain the focus.

#### Knowledge–Skill Pairing

- Halting Problem — Understand (Describe, Explain, Justify).
- Computability — Understand (Classify, Recognize, Explain).
- Turing Machines — Understand (Explain, Relate).
- Analytical and Critical Thinking — Apply (Evaluate, Structure, Argue).

#### Dispositions

Collaboration, Responsibility, Proactivity, Creativity.

#### Activation

- ActivationRole: `core`
- ActivationMode: `analytical; justificatory`
- ActivationConstraint: `mandatory`

#### Summary Table for Competency C15

| Competency | Dispositions | Knowledge | Skill |
| --- | --- | --- | --- |
| Understand the Halting Problem and its Implications | Collaboration, Responsibility, Proactivity, Creativity | Halting Problem | Understand (Describe, Explain, Justify) |
|  |  | Computability | Understand (Classify, Recognize, Explain) |
|  |  | Turing Machines | Understand (Explain, Relate) |
|  |  | Analytical and Critical Thinking | Apply (Evaluate, Structure, Argue) |

### C06 — Develop Problem-Solving Solutions Using Finite State Machines

Origin: Task03 — Cycle 1.

#### Competency Description

Design and construct finite-state solutions from requirements, using explicit states, transitions, and formal reasoning about the model.

#### Contextual Application

Construct an FSM illustrating the OJ evaluation workflow and outcomes AC, WA, CE, RE, and TLE. Explain the meaning of states and transitions within the selected abstraction. The FSM represents the workflow; it does not model unrestricted submitted-program execution or solve the Halting Problem. Its constructive contribution remains supporting, as in Task204.

#### Knowledge–Skill Pairing

- Finite State Machines — Apply (Design, Construct, Model, Validate).
- Requirements Engineering — Apply (Interpret, Specify, Translate).
- Analytical and Critical Thinking (FPK) — Apply (Analyze, Evaluate, Justify).

#### Dispositions

Analytical; Responsible; Proactive; Collaborative.

#### Activation

- ActivationRole: `supporting`
- ActivationMode: `constructive`
- ActivationConstraint: `mandatory`

#### Summary Table for Competency C06

| Competency | Dispositions | Knowledge | Skill |
| --- | --- | --- | --- |
| Develop Problem-Solving Solutions Using Finite State Machines | Analytical; Responsible; Proactive; Collaborative | Finite State Machines | Apply (Design, Construct, Model, Validate) |
|  |  | Requirements Engineering | Apply (Interpret, Specify, Translate) |
|  |  | Analytical and Critical Thinking (FPK) | Apply (Analyze, Evaluate, Justify) |

### C16 — Interpret Turing Machine Concepts to Analyze Computational System Capabilities

Origin: Task204 — Cycle 2.

#### Competency Description

Interpret Turing Machine concepts to analyze computational capabilities and limitations.

#### Contextual Application

Use Turing Machines, the Universal Turing Machine, computability, and recursively enumerable languages as conceptual references for OJ analysis. Preserve the interpretative, conditional association. Universal Turing Machine remains part of the detailed conceptual knowledge; the existing paired summary groups it under Turing Machines without introducing a separate cognitive mapping.

#### Knowledge–Skill Pairing

- Turing Machines — Understand (Explain, Interpret).
- Computability — Understand (Classify, Distinguish).
- Analytical and Critical Thinking (FPK) — Apply (Analyze, Justify).

#### Dispositions

Collaborative, Responsible, Proactive, Creative.

#### Activation

- ActivationRole: `supporting`
- ActivationMode: `interpretative`
- ActivationConstraint: `conditional`

#### Summary Table for Competency C16

| Competency | Dispositions | Knowledge | Skill |
| --- | --- | --- | --- |
| Interpret Turing Machine Concepts to Analyze Computational System Capabilities | Collaborative, Responsible, Proactive, Creative | Turing Machines | Understand (Explain, Interpret) |
|  |  | Computability | Understand (Classify, Distinguish) |
|  |  | Analytical and Critical Thinking (FPK) | Apply (Analyze, Justify) |

### C03 — Test Automata Using Simulators

Origin: Task01 — Cycle 1.

#### Competency Description

Test automata with simulators, compare expected and observed behavior, and diagnose and refine models.

#### Contextual Application

Use JFLAP to test and illustrate the FSM when that exploration is part of the presented solution. This preserves the source report’s conditional association. The task statement also includes simulator use among its learning objectives; that objective is retained. Simulation results support the tested behavior rather than proving all model properties.

#### Knowledge–Skill Pairing

- Finite State Machines — Apply (Simulate, execute, validate).
- Modeling and Simulation — Apply (Test, Validate).
- Problem Solving and Troubleshooting (FPK) — Apply (Diagnose, Correct).

#### Dispositions

Investigative, Collaborative, Responsible, Proactive, Creative.

#### Activation

- ActivationRole: `supporting`
- ActivationMode: `artifact-oriented`
- ActivationConstraint: `conditional`

#### Summary Table for Competency C03

| Competency | Dispositions | Knowledge | Skill |
| --- | --- | --- | --- |
| Test Automata Using Simulators | Investigative, Collaborative, Responsible, Proactive, Creative | Finite State Machines | Apply (Simulate, execute, validate) |
|  |  | Modeling and Simulation | Apply (Test, Validate) |
|  |  | Problem Solving and Troubleshooting (FPK) | Apply (Diagnose, Correct) |

### C02 — Justify the use of Deterministic Finite Automata (DFAs)

Origin: Task01 — Cycle 1.

#### Competency Description

Justify the suitability of deterministic finite automata through their properties and the requirements of a defined problem.

#### Contextual Application

Provide an optional justification of why a deterministic finite-state abstraction is suitable for the observable OJ workflow. This does not imply that the full computational power of the OJ or its submitted programs is finite-state. No additional mandatory evidence is introduced.

#### Knowledge–Skill Pairing

- Deterministic Finite Automata (DFAs) — Understand (Identify, Explain, Recognize).
- Requirements Elicitation — Apply (Identify, Interpret, Organize).
- Analytical and Critical Thinking (FPK) — Apply (Analyze, Evaluate, Justify).

#### Dispositions

Investigative, Collaborative, Responsible, Proactive.

#### Activation

- ActivationRole: `extension`
- ActivationMode: `justificatory`
- ActivationConstraint: `optional`

#### Summary Table for Competency C02

| Competency | Dispositions | Knowledge | Skill |
| --- | --- | --- | --- |
| Justify the use of Deterministic Finite Automata (DFAs) | Investigative, Collaborative, Responsible, Proactive | Deterministic Finite Automata (DFAs) | Understand (Identify, Explain, Recognize) |
|  |  | Requirements Elicitation | Apply (Identify, Interpret, Organize) |
|  |  | Analytical and Critical Thinking (FPK) | Apply (Analyze, Evaluate, Justify) |

### C14 — Differentiate classifications of formal grammars

Origin: Task04 — Cycle 1.

#### Competency Description

Compare and differentiate formal grammar and language classes, particularly regular and context-free formalisms and their associated recognizers.

#### Contextual Application

Optionally relate the discussion to language classes and recognition models. The grammar hierarchy and complexity classes describe different classifications; C14 does not replace C21 for P, NP, or NP-completeness. Its contribution to LO8 applies when the analysis explicitly makes the language-model connection.

#### Knowledge–Skill Pairing

- Regular Languages — Understand.
- Context-Free Languages — Understand.
- Analytical and Critical Thinking — Apply.

#### Dispositions

Inventive; Collaborative; Responsible; Proactive.

#### Activation

- ActivationRole: `extension`
- ActivationMode: `analytical`
- ActivationConstraint: `optional`

#### Summary Table for Competency C14

| Competency | Dispositions | Knowledge | Skill |
| --- | --- | --- | --- |
| Differentiate classifications of formal grammars | Inventive; Collaborative; Responsible; Proactive | Regular Languages | Understand |
|  |  | Context-Free Languages | Understand |
|  |  | Analytical and Critical Thinking | Apply |

### C05 — Write a Technical Report

Origin: Task01 — Cycle 1.

#### Competency Description

Produce clear, structured, technically accurate reports presenting context, modeling decisions, methods, and results.

#### Contextual Application

Prepare the SBC article connecting the FSM model, TSP and PT analysis, practical limitations, and theoretical explanations. Preserve the original choice of C05; it is not replaced by C05.01 merely because rigorous reasoning is expected.

#### Knowledge–Skill Pairing

- Written Communication (FPK) — Apply (Document, Present, Write, Revise).

#### Dispositions

Collaborative, Meticulous, Responsible.

#### Activation

- ActivationRole: `transversal`
- ActivationMode: `artifact-oriented`
- ActivationConstraint: `mandatory`

#### Summary Table for Competency C05

| Competency | Dispositions | Knowledge | Skill |
| --- | --- | --- | --- |
| Write a Technical Report | Collaborative, Meticulous, Responsible | Written Communication (FPK) | Apply (Document, Present, Write, Revise) |

## 7. Competency Activation Summary

| ID | Role | Mode | Constraint |
| --- | --- | --- | --- |
| C21 | core | analytical | mandatory |
| C15 | core | analytical; justificatory | mandatory |
| C06 | supporting | constructive | mandatory |
| C16 | supporting | interpretative | conditional |
| C03 | supporting | artifact-oriented | conditional |
| C02 | extension | justificatory | optional |
| C14 | extension | analytical | optional |
| C05 | transversal | artifact-oriented | mandatory |

C21 and C15 constitute the theoretical core. C06 supports constructive externalization of the workflow, while C16 and C03 retain conditional interpretative and simulation roles. C02 and C14 remain optional extensions. C05 supports the article across the task. This grouping describes task associations and does not introduce a composite competency.

## 8. Learning Objective–Competency Mapping

| LO | Expected performance | Associated competencies |
| --- | --- | --- |
| LO1 | Explain the OJ workflow through FSMs | C06, C02 |
| LO2 | Analyze TLE results for TSP and PT | C21 |
| LO3 | Discuss strategies for acceptance under execution limits | C21, C05 |
| LO4 | Explain theoretical limitations of the OJ | C15, C16 |
| LO5 | Interpret Turing Machines and computability | C16, C15 |
| LO6 | Communicate analyses and conclusions | C05 |
| LO7 | Simulate and examine the FSM when applicable | C03, C06 |
| LO8 | Relate OJ analysis to complexity and NP-complete problems | C21, C14 |

The identifier associations are preserved. Optional or conditional contributors are read with the activation table: for example, C14 supplies a language-class extension to LO8 rather than its main complexity content, which is represented by C21.

## 9. Consolidated Specification Decisions

| Decision | Result in TASK25.05 |
| --- | --- |
| Create C21 for complexity analysis | C21 addresses TSP, PT, scalability, and execution limits |
| Preserve the theoretical termination limit | C15 remains core, analytical, and justificatory |
| Keep construction as support for explanation | C06 builds the FSM as an abstraction of evaluation workflow |
| Retain conceptual and simulation qualifications | C16 and C03 remain conditional |
| Retain optional extensions | C02 and C14 enrich particular analyses without becoming the core |
| Preserve technical reporting | C05 remains the transversal writing competency |

These decisions consolidate the existing specification and its contextual changes from Task204. They do not establish an additional review interaction or a new approval procedure.

## 10. Final Competency Summary and Conclusion

| ID | Competency | Role in the specification |
| --- | --- | --- |
| C21 | Analyze Computational Complexity and the Implications of NP-Hardness | Created in TASK25.05 — Cycle 3 (2025) |
| C15 | Understand the Halting Problem and its Implications | Reused |
| C06 | Develop Problem-Solving Solutions Using Finite State Machines | Reused |
| C16 | Interpret Turing Machine Concepts to Analyze Computational System Capabilities | Reused |
| C03 | Test Automata Using Simulators | Reused |
| C02 | Justify the use of Deterministic Finite Automata (DFAs) | Reused |
| C14 | Differentiate classifications of formal grammars | Reused |
| C05 | Write a Technical Report | Reused |

The task associates eight competencies: one created for this task (C21) and seven reused (C15, C06, C16, C03, C02, C14, and C05). Counting each associated identifier once, reuse accounts for 7 of 8 associations (87.5%). This total includes mandatory, conditional, and optional associations; their instructional requirements remain distinguished in the activation summary.

TASK25.05 extends the Task204 scenario through explicit timetabling analysis and greater emphasis on complexity and execution limits. It retains the distinction between modeling a workflow, interpreting computational capabilities, explaining general undecidability, and communicating justified conclusions. Expected evidence consists of the model and analysis described in the task; no observed learner results or independent ontology validation are asserted.
