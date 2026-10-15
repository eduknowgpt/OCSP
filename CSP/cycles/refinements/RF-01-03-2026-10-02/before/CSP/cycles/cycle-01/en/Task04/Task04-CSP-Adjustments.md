# CSP Review Adjustments: Task04 — The Return of the Farmer Robot

## 1. Introduction

This report records the revisions made to the competency specification for *Task04 — The Return of the Farmer Robot* following the expert review in CSP Phase 2.

The adjustments address:

- knowledge granularity and relevance;
- consistency between computational models and formal languages;
- controlled vocabulary;
- Bloom levels and action verbs;
- justification of knowledge–skill pairings;
- textual clarity.

The revisions preserve the instructional task and its expected outcomes. They align the competency specification with memory-dependent navigation, Pushdown Automata, Context-Free Grammars, and the artifacts required by the task.

## 2. Implemented Adjustments

### 2.1 Computational model

Pushdown Automata replaced Finite Automata wherever the knowledge element represents the model used to solve the return-navigation problem. The revised specification now refers explicitly to states, transitions, stack operations, route recording, and return-path behavior.

Finite Automata remain only in the comparison between regular and context-free formalisms in C14.

### 2.2 Formal languages and grammars

Regular Languages were removed from C13 because that competency interprets the Context-Free Grammars associated with the task. C14 retains Regular Languages and Context-Free Languages because its purpose is to differentiate the two classifications and their corresponding computational models.

### 2.3 Bloom alignment

Bloom levels and actions were consolidated as follows:

- **Create** for designing and constructing the PDA model;
- **Understand** for interpreting rule-based notation and differentiating grammar classes;
- **Apply** for requirements analysis, model validation, and analytical reasoning.

Each knowledge element now has one consistent Bloom level and action set.

### 2.4 Competency reuse

The following competencies are reused:

- C03 — *Testing Automata Using Simulators*;
- C05 — *Collaborative Technical Report Writing*.

C03 supports implementation, execution, and verification of the PDA model in JFLAP. C05 supports documentation of the model, examples, decisions, and results. Their reuse maintains continuity with earlier tasks and avoids duplicate competency definitions.

## 3. Revised Competency Specifications

### 3.1 C12 — Develop Problem-Solving Solutions Using Pushdown Automata

#### Description

Design, construct, and validate a Pushdown Automaton that represents behavior requiring stack-based memory. In Task04, learners use the stack to record information needed to model the robot’s return path. The resulting model must be logically consistent and satisfy the task requirements.

#### Knowledge

- **Pushdown Automata:** states, transitions, input symbols, stack operations, and recognition of structured or nested sequences.
- **Requirements Engineering:** interpretation and formalization of the expected navigation behavior and constraints.
- **Analytical and Critical Thinking (FPK):** decomposition of the problem, evaluation of alternatives, and justification of modeling decisions.

#### Dispositions

- Inventive
- Collaborative
- Responsible
- Proactive
- Creative

#### Knowledge–skill pairing

| Knowledge | Bloom level | Observable actions |
| --- | --- | --- |
| Pushdown Automata | Create | Design, develop, construct |
| Requirements Engineering | Apply | Interpret, specify, translate |
| Analytical and Critical Thinking (FPK) | Apply | Decompose, evaluate, justify |

### 3.2 C13 — Interpret Rule-Based Notation

#### Description

Interpret formal rule-based notation, particularly Context-Free Grammars, used to represent structured symbol sequences and navigation behavior. Learners relate production rules to the corresponding stack-based computational model and examine the notation for clarity and consistency.

#### Knowledge

- **Context-Free Grammars:** production rules, derivations, and structured symbol sequences.
- **Pushdown Automata:** correspondence between context-free formalisms and computational models with stack memory.
- **Analytical and Critical Thinking (FPK):** examination of rule sets and identification of inconsistencies or ambiguities.

#### Dispositions

- Inventive
- Collaborative
- Responsible
- Proactive
- Creative

#### Knowledge–skill pairing

| Knowledge | Bloom level | Observable actions |
| --- | --- | --- |
| Context-Free Grammars | Understand | Interpret, recognize, describe |
| Pushdown Automata | Understand | Recognize, explain, relate |
| Analytical and Critical Thinking (FPK) | Apply | Examine, identify, validate |

### 3.3 C14 — Differentiate Classifications of Formal Grammars

#### Description

Differentiate regular and context-free grammars and relate each class to its corresponding computational model. Learners compare their structure and expressive power and use the distinction to explain why the Task04 navigation problem requires stack-based memory.

#### Knowledge

- **Regular Languages:** regular grammars, their relationship with Finite Automata, and their expressive limits.
- **Context-Free Languages:** Context-Free Grammars, their relationship with Pushdown Automata, and their capacity to represent structured or nested sequences.
- **Analytical and Critical Thinking (FPK):** comparison of formal models and justification of their suitability for a given behavior.

#### Dispositions

- Inventive
- Collaborative
- Responsible
- Proactive

#### Knowledge–skill pairing

| Knowledge | Bloom level | Observable actions |
| --- | --- | --- |
| Regular Languages | Understand | Identify, classify, compare |
| Context-Free Languages | Understand | Recognize, describe, differentiate |
| Analytical and Critical Thinking (FPK) | Apply | Analyze, evaluate, justify |

## 4. Revised Competency Set

| ID | Competency | Status | Dispositions | Knowledge–skill pairing |
| --- | --- | --- | --- | --- |
| C12 | Develop Problem-Solving Solutions Using Pushdown Automata | Revised | Inventive, Collaborative, Responsible, Proactive, Creative | Pushdown Automata — Create; Requirements Engineering — Apply; Analytical and Critical Thinking (FPK) — Apply |
| C13 | Interpret Rule-Based Notation | Revised | Inventive, Collaborative, Responsible, Proactive, Creative | Context-Free Grammars — Understand; Pushdown Automata — Understand; Analytical and Critical Thinking (FPK) — Apply |
| C14 | Differentiate Classifications of Formal Grammars | Revised | Inventive, Collaborative, Responsible, Proactive | Regular Languages — Understand; Context-Free Languages — Understand; Analytical and Critical Thinking (FPK) — Apply |
| C03 | Testing Automata Using Simulators | Reused | Investigative, Collaborative, Responsible, Proactive, Creative | Finite State Machines — Apply; Problem Solving and Troubleshooting (FPK) — Apply; Modeling and Simulation — Apply |
| C05 | Collaborative Technical Report Writing | Reused | Collaborative, Meticulous, Responsible | Written Communication (FPK) — Apply |

## 5. Traceability of Review Recommendations

| Review recommendation | Implemented revision |
| --- | --- |
| Use Pushdown Automata for the navigation solution | Replaced Finite Automata with Pushdown Automata in C12 and C13. |
| Use context-free formalisms | Replaced Regular Languages with Context-Free Grammars in C13. |
| Preserve formal comparison where relevant | Retained regular and context-free classifications in C14 and identified their corresponding automata. |
| Connect knowledge to task behavior | Added stack operations, route recording, and return-path behavior to C12. |
| Refine Bloom alignment | Consolidated Create, Understand, and Apply according to the expected learner actions. |
| Improve knowledge–skill justification | Added descriptions and observable actions for every pairing. |
| Check terminology across the artifact | Standardized competency titles, knowledge names, and FPK labels. |
| Preserve reusable competencies | Retained C03 and C05 and documented their roles in Task04. |

## 6. Conclusion

The implemented revisions align the Task04 competency set with the computational demands of the return-navigation problem. Pushdown Automata are now the principal model for the solution, Context-Free Grammars support rule-based notation, and regular formalisms appear only in the comparison required by C14.

The report also consolidates Bloom levels and observable actions, documents the reuse of C03 and C05, and records how each expert recommendation was incorporated. These changes provide a consistent basis for subsequent semantic structuring.
