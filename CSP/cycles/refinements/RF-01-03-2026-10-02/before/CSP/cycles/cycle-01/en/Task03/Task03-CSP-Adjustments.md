# CSP Review Adjustments: Task03 — The Farmer Robot

## 1. Introduction

The expert review identified opportunities to improve the competency specification for *Task03 — The Farmer Robot*. The implemented adjustments address five areas:

- knowledge granularity;
- knowledge relevance;
- controlled vocabulary;
- alignment with Bloom’s Revised Taxonomy;
- textual clarity.

The revisions improve consistency among the task, learning objectives, knowledge components, and competency definitions. They refine the existing specification without changing the instructional task or its expected outcomes.

## 2. Implemented Adjustments

### 2.1 Knowledge classification and terminology

The knowledge classification was updated from CC2012 to CS2013 to provide more specific knowledge references.

The following terms were revised:

| Previous term | Revised term | Rationale |
| --- | --- | --- |
| Requirements Analysis | Requirements Engineering | Uses the broader term adopted for elicitation, specification, and validation activities. |
| Finite Automata | Finite State Machines | Matches the operational focus and terminology of the task. |
| Regular Languages | Regular Expressions | Refers directly to the formal representations produced in the task. |

The Chomsky Hierarchy was removed because it is not required by the task description or its expected outputs.

### 2.2 Competency definitions

The competency *Differentiate the Classifications of Formal Grammars* was removed from the task-level competency set because grammar classification is not exercised by the task or demonstrated in its deliverables.

The title *Infer and Identify Patterns in Finite State Machines* was revised to *Identify Patterns in Finite State Machines*. Its description and knowledge–skill pairings were also refined to focus on observable analysis of state and transition structures.

### 2.3 Competency reuse

The following previously specified competencies are reused in Task03:

- C03 — *Testing Automata Using Simulators*;
- C04 — *Define Regular Expressions for Finite Automata*;
- C05 — *Write a Technical Report*.

C04 was reviewed before reuse to improve its clarity and its alignment with the relationship between finite state machines and regular expressions. Reuse preserves continuity with earlier tasks and avoids creating duplicate competencies.

## 3. Revised Competency Specifications

### 3.1 C06 — Develop Problem-Solving Solutions Using Finite State Machines

#### Description

Design and implement computational solutions using Finite State Machines (FSMs) as formal models for systems governed by discrete states and transitions. Learners translate system requirements into precise and verifiable FSM representations and validate whether the resulting models are logically sound and suitable for the intended context.

#### Knowledge

- **Finite State Machines:** structure, semantics, and behavior of deterministic and non-deterministic FSMs and their use in modeling sequential systems.
- **Requirements Engineering:** identification, interpretation, and formalization of system requirements to guide FSM design.
- **Analytical and Critical Thinking (FPK):** analysis of constraints, comparison of alternatives, and justification of modeling decisions.

#### Dispositions

- Inventive
- Collaborative
- Responsible
- Proactive
- Creative

#### Knowledge–skill pairing

| Knowledge | Bloom level | Observable actions |
| --- | --- | --- |
| Finite State Machines | Create | Design, develop, construct |
| Requirements Engineering | Apply | Interpret, specify, translate |
| Analytical and Critical Thinking (FPK) | Apply | Analyze, justify, evaluate |

### 3.2 C11 — Identify Patterns in Finite State Machines

#### Description

Analyze the structure and behavior of Finite State Machines to identify recurring patterns, regularities, and redundancies that affect model complexity and efficiency. Learners examine states, transitions, and input classifications and use the results to support refinement or optimization decisions.

#### Knowledge

- **Finite State Machines:** structural properties of FSMs, including states, transitions, determinism, equivalence, and minimization.
- **Analytical and Critical Thinking (FPK):** logical reasoning and pattern recognition used to interpret FSM behavior and justify refinement decisions.

#### Dispositions

- Inventive
- Creative
- Meticulous

#### Knowledge–skill pairing

| Knowledge | Bloom level | Observable actions |
| --- | --- | --- |
| Finite State Machines | Analyze | Examine, evaluate, compare |
| Analytical and Critical Thinking (FPK) | Apply | Infer, justify, interpret |

## 4. Revised Competency Set

| ID | Competency | Status | Dispositions | Knowledge–skill pairing |
| --- | --- | --- | --- | --- |
| C06 | Develop Problem-Solving Solutions Using Finite State Machines | Revised | Inventive, Collaborative, Responsible, Proactive, Creative | Finite State Machines — Create; Requirements Engineering — Apply; Analytical and Critical Thinking (FPK) — Apply |
| C11 | Identify Patterns in Finite State Machines | Revised | Inventive, Creative, Meticulous | Finite State Machines — Analyze; Analytical and Critical Thinking (FPK) — Apply |
| C03 | Testing Automata Using Simulators | Reused | Investigative, Collaborative, Responsible, Proactive, Creative | Finite State Machines — Apply; Problem Solving and Troubleshooting (FPK) — Apply; Modeling and Simulation — Apply |
| C04 | Define Regular Expressions for Finite Automata | Reused | Investigative, Collaborative, Responsible, Proactive, Creative | Finite State Machines — Understand; Regular Expressions — Apply; Analytical and Critical Thinking (FPK) — Apply |
| C05 | Write a Technical Report | Reused | Collaborative, Meticulous, Responsible | Written Communication (FPK) — Apply |

The competency *Differentiate the Classifications of Formal Grammars* is excluded from the revised set.

## 5. Traceability of Review Recommendations

| Review recommendation | Implemented revision |
| --- | --- |
| Refine knowledge granularity | Updated the classification from CC2012 to CS2013 and adopted more specific knowledge terms. |
| Replace “Regular Languages” | Adopted “Regular Expressions” where the task requires construction of regular expressions. |
| Remove the Chomsky Hierarchy | Removed it from the knowledge specification. |
| Remove the grammar-classification competency | Excluded it from the revised competency set. |
| Clarify the pattern-identification competency | Renamed it and refined its description and knowledge–skill pairings. |
| Reassess Bloom levels | Consolidated one Bloom level and action set for each knowledge–skill pairing. |
| Improve textual clarity | Shortened descriptions, removed repetition, and standardized terminology. |

## 6. Historical Note on CSP Maturation

Task03 represents a transitional stage in the development of the CSP. At that point, the process did not yet formally distinguish target competencies from supporting theoretical knowledge or provide explicit mechanisms for qualified reuse and specialization.

The review therefore refined the scope and terminology of the task-level competencies and removed the grammar-classification competency from the revised set. The questions raised by this task later informed more explicit reuse and specialization mechanisms in subsequent CSP cycles.

Bloom’s Revised Taxonomy was applied to individual knowledge–skill pairings. Cross-competency cognitive progression was not yet modeled explicitly, which explains some overlap between analytical and operational actions in the original specification.

## 7. Conclusion

The implemented adjustments align the Task03 competency set more closely with the instructional task and its expected outputs. They remove knowledge and competencies that are not exercised, clarify the two revised competencies, and document the reuse of three existing competencies. This report records the changes resulting from the expert review and preserves their traceability within the CSP.

