# CSP-Report — TASK302 (TASK25.01) — The Vending Machine for Soft Drinks and Snacks

## 1. Introduction

This report consolidates the competency specification for TASK302, a revised application of the vending-machine problem used in Task01. Learners model, analyze, and justify a discrete system through formal languages, finite automata, and regular expressions.

### 1.1 Purpose within Cycle 3

Cycle 3 was designed to demonstrate reuse of mature specifications in Theory of Computation. Task authors, specifiers, and reviewers discussed intended competencies during task development, considering additions where necessary. TASK302 reuses eight identifiers: C17, C18, C23, and C05.01 originated in TASK25.00; C02, C03, and C04 originated in Task01 and C06 in Task03, both in Cycle 1. No new competency is introduced here.

The revised vending-machine scenario updates product prices and emphasizes the JFLAP model, regular-expression investigation, construction method, and rigorous technical report. Monetary values can affect the state space under a chosen balance encoding, but their increase alone does not prove a larger minimal automaton. The task statement does not require the PBL whiteboards and logbooks used in some earlier applications. Formal reasoning, modeling, and testing were already present in Cycle 1; this application reconfigures their instructional use.

### 1.2 Integrated specification and interactive review

Specification and discussion were integrated during task development. This report brings together the resulting competency set, contextual activation, learning-objective mapping, and decision rationale. It records consolidated decisions rather than a transcript or an independently dated review. No separate CSP-Review or CSP-Adjustments report is asserted for this application. Section 9 distinguishes recorded decisions from consistency issues still requiring methodological resolution.

## 2. Instructional Entity Analysis

### 2.1 Identification

- Title: The Vending Machine for Soft Drinks and Snacks.
- Type: Problem-based instructional task emphasizing formal artifacts.
- Domain: Formal Languages, Finite Automata, and Regular Expressions.

### 2.2 Task Scope

The machine must offer at least three products, accept the specified R$1.00 and R$2.00 denominations, and provide change. Available prices are R$5.00 and R$7.00 for soft drinks and R$7.00 and R$10.00 for snack packets. The additional challenge concerns random R$1.00 bonus change when payment exactly equals the selected price.

The formal representation distinguishes valid from invalid sequences of payment and product selection. Modeling conventions must explain how state, input, acceptance, dispensing, and change relate to the scenario. The bonus remains an additional challenge; references to it in the specifications apply when that challenge is addressed. Nondeterminism describes alternative computational paths, not a probabilistic mechanism. The model and the account of random machine behavior must respect that distinction.

## 3. Expected Outcomes and Evidence

- An automaton file representing the machine and testable or simulatable in JFLAP.
- Explicit symbolic definitions of the alphabet, strings, and transaction conditions within the model and report.
- Simulation examples and interpretation of model behavior, distinguishing tested cases from general correctness arguments.
- Investigation of the relation to regular expressions, including an expression for a portion of the model and its construction method, or the justified alternative required by the task.
- A mathematically rigorous report in the SBC article format, explaining payment and product delivery and providing at least two operation examples.

The submission deadline is 11:59 p.m. on October 13, 2025, through UFBA Moodle. These descriptions elaborate the two original deliverables; they do not add independent submissions. JFLAP compatibility is preserved. Observed simulation behavior provides evidence for tested inputs, not an exhaustive proof of correctness or completeness.

## 4. Knowledge Enumeration

### 4.1 Computing Knowledge

- Language Theory: alphabets, strings, languages, and valid and invalid sequences.
- Formal Languages: concatenation, prefixes, suffixes, partial sequences, and recognized languages.
- Finite Automata: deterministic and nondeterministic models, states, transitions, acceptance, and language recognition.
- Regular Expressions: algebraic representation and equivalence with finite-automaton languages; distinction between theoretical expressibility and difficulties applying a construction method.

### 4.2 Foundational and Professional Knowledge

- Analytical and Critical Thinking: decomposition of behavior, assessment of the model, and justification of design decisions.
- Written Communication: clear and mathematically precise definitions, arguments, and conclusions.

The reused specifications below retain their additional components, such as Requirements Engineering and Modeling and Simulation. Framework-related terminology follows the existing specifications; this report does not introduce a new external-framework mapping.

## 5. Learning Objectives

### General Objective

Model, analyze, and validate a vending-machine representation as a formal language recognized by a finite automaton, connecting symbolic modeling, simulation, and rigorous argumentation.

### Specific Objectives

- LO1 — Symbolic abstraction: associate relevant domain elements with formal symbols, explaining assumptions and conventions, including the bonus if addressed.
- LO2 — Formal sequences: represent valid and invalid uses as strings and characterize acceptable operations.
- LO3 — Recognizer construction: construct a finite automaton, deterministic or nondeterministic as appropriate, that recognizes the modeled valid sequences and represents balance, change, and the bonus if addressed.
- LO4 — Simulation: use JFLAP to examine input sequences, compare expected and observed behavior, identify errors, and assess the model against its specification.
- LO5 — Formal analysis: justify recognition, validity, and modeling limits; explain regular-expression representability and distinguish nondeterministic alternatives from random behavior.
- LO6 — Rigorous communication: document the model and reasoning in a structured technical report, distinguishing definitions, examples, simulation results, and formal arguments.

These six objectives preserve the report's elaboration of the task objectives. The theoretical clarifications delimit the claims made about their achievement.

## 6. Reused Competency Specifications

The following entries retain the competency identities, dispositions, knowledge–skill pairings, and contextual activation decisions. Contextual use does not redefine a competence. Activation modes and component-level cognitive levels describe different aspects of performance.

### C06 — Develop Problem-Solving Solutions Using Finite State Machines

Origin: Task03 — Cycle 1. Usage in TASK302: reused.

#### Competency Description

Design and implement computational solutions using finite state machines as formal models for systems governed by discrete states and transitions. Translate system requirements into precise, verifiable, and logically consistent FSM representations grounded in automata theory.

Learners analyze functional requirements, construct models through well-defined states and transitions, and validate their logical soundness, functional correctness, and suitability for the intended context.

#### Contextual Application and Scope

Construct the vending-machine automaton required by LO3, specifying states, transitions, and acceptance conditions for the chosen transaction representation. Relate these elements to payment, product selection, change, and the bonus challenge when addressed. The expected evidence is the submitted automaton together with the explanation of its construction in the technical report; no additional deliverable is introduced.

C06 directly represents recognizer construction. C18 supplies domain abstraction, C02 supports justification of the model, and C23 supports formal notation. Their scopes remain distinct. The reference definition pairs Finite State Machines with Create and its supporting knowledge with Apply. The constructive activation records the task-specific use of that definition.

#### Knowledge–Skill Pairing

- Finite State Machines — Create (Design, Develop, Construct).
- Requirements Engineering — Apply (Interpret, Specify, Translate).
- Analytical and Critical Thinking (FPK) — Apply (Analyze, Justify, Evaluate).

#### Dispositions

Inventive, Collaborative, Responsible, Proactive, Creative.

#### Activation

- ActivationRole: `core`
- ActivationMode: `constructive`
- ActivationConstraint: `mandatory`

#### Summary Table for Competency C06

| Competency | Dispositions | Knowledge | Skill |
| --- | --- | --- | --- |
| Develop Problem-Solving Solutions Using Finite State Machines | Inventive, Collaborative, Responsible, Proactive, Creative | Finite State Machines | Create (Design, Develop, Construct) |
|  |  | Requirements Engineering | Apply (Interpret, Specify, Translate) |
|  |  | Analytical and Critical Thinking (FPK) | Apply (Analyze, Justify, Evaluate) |

### C17 — Apply operations on formal languages

Origin: TASK25.00 — Cycle 3. Usage in TASK302: reused.

#### Competency Description

Apply, analyze, and justify operations on formal languages at a conceptual and algebraic level.

#### Contextual Application and Scope

Analyze concatenation, prefixes, and partial input sequences to characterize valid and invalid uses of the machine. Closure properties are not the principal focus of this application.

#### Knowledge–Skill Pairing

- Language Theory — Understand.
- Operations on Formal Languages — Apply / Analyze.
- Regular Expressions (conceptual) — Apply.
- Analytical and Critical Thinking (FPK) — Analyze.

#### Dispositions

Epistemic Rigor; Intellectual Responsibility; Persistence.

#### Activation

- ActivationRole: `core`
- ActivationMode: `analytical`
- ActivationConstraint: `mandatory`

#### Summary Table for Competency C17

| Competency | Dispositions | Knowledge | Skill |
| --- | --- | --- | --- |
| Apply operations on formal languages | Epistemic Rigor; Intellectual Responsibility; Persistence | Language Theory | Understand |
|  |  | Operations on Formal Languages | Apply / Analyze |
|  |  | Regular Expressions (conceptual) | Apply |
|  |  | Analytical and Critical Thinking (FPK) | Analyze |

### C18 — Model real-world problems using formal language concepts

Origin: TASK25.00 — Cycle 3. Usage in TASK302: reused.

#### Competency Description

Abstract a real-world domain through explicit alphabets, strings, and languages, justifying modeling choices and structural limitations.

#### Contextual Application and Scope

Represent coins, banknotes, products, balance, change, actions, and the bonus challenge through explicit symbolic conventions. Distinguish input symbols from information represented in states; not every domain entity needs to become an input symbol. C18 supports domain abstraction without being redefined as a general automaton-construction competence.

#### Knowledge–Skill Pairing

- Language Theory — Understand.
- Formal Languages — Apply.
- Homomorphisms and Codifications (conceptual) — Apply.
- Analytical and Critical Thinking (FPK) — Analyze.

#### Dispositions

Epistemic Rigor; Intellectual Responsibility; Reflectiveness.

#### Activation

- ActivationRole: `core`
- ActivationMode: `constructive`
- ActivationConstraint: `mandatory`

#### Summary Table for Competency C18

| Competency | Dispositions | Knowledge | Skill |
| --- | --- | --- | --- |
| Model real-world problems using formal language concepts | Epistemic Rigor; Intellectual Responsibility; Reflectiveness | Language Theory | Understand |
|  |  | Formal Languages | Apply |
|  |  | Homomorphisms and Codifications (conceptual) | Apply |
|  |  | Analytical and Critical Thinking (FPK) | Analyze |

### C23 — Interpret and apply algebraic notation for strings and languages

Origin: TASK25.00 — Cycle 3. Usage in TASK302: reused.

#### Competency Description

Interpret, apply, and justify algebraic notation for strings and languages.

#### Contextual Application and Scope

Use ε, concatenation, Σ*, and string and language notation to express sequences, acceptance conditions, and the formal account of machine behavior. C23 replaces the earlier C13.01 association because this use concerns algebraic notation rather than grammar-rule interpretation.

#### Knowledge–Skill Pairing

- Language Theory — Understand.
- Formal Languages — Apply.
- Written Communication (FPK) — Apply.
- Analytical and Critical Thinking (FPK) — Analyze.

#### Dispositions

Meticulous; Responsible.

#### Activation

- ActivationRole: `transversal`
- ActivationMode: `analytical`
- ActivationConstraint: `mandatory`

#### Summary Table for Competency C23

| Competency | Dispositions | Knowledge | Skill |
| --- | --- | --- | --- |
| Interpret and apply algebraic notation for strings and languages | Meticulous; Responsible | Language Theory | Understand |
|  |  | Formal Languages | Apply |
|  |  | Written Communication (FPK) | Apply |
|  |  | Analytical and Critical Thinking (FPK) | Analyze |

### C05.01 — Write mathematically rigorous answers

Origin: TASK25.00 — Cycle 3. Usage in TASK302: reused.

#### Competency Description

Produce mathematically rigorous written answers connecting explicit definitions, precise notation, arguments, and conclusions.

#### Contextual Application and Scope

Justify the model, string validity, the role of nondeterminism, and the relation to regular expressions, using definitions, examples, and counterexamples where appropriate. The SBC report contains these justifications; this reuse does not introduce another written deliverable. C05.01 retains its specialization relation to C05.

#### Knowledge–Skill Pairing

- Written Communication (FPK) — Apply.
- Analytical and Critical Thinking (FPK) — Analyze / Evaluate.

#### Dispositions

Meticulous; Responsible.

#### Activation

- ActivationRole: `transversal`
- ActivationMode: `justificatory`
- ActivationConstraint: `mandatory`

#### Summary Table for Competency C05.01

| Competency | Dispositions | Knowledge | Skill |
| --- | --- | --- | --- |
| Write mathematically rigorous answers | Meticulous; Responsible | Written Communication (FPK) | Apply |
|  |  | Analytical and Critical Thinking (FPK) | Analyze / Evaluate |

### C02 — Justify the use of Deterministic Finite Automata (DFAs)

Origin: Task01 — Cycle 1. Usage in TASK302: reused.

#### Competency Description

Justify the suitability of deterministic finite automata using their properties, elicited requirements, and explicit modeling constraints.

#### Contextual Application and Scope

Explain how a finite state space represents the selected transaction model, including balances, change, and, if addressed, bonus alternatives. A nondeterministic representation and conversion to a DFA may support the language-level justification. Such conversion preserves the accepted language; it does not implement random selection or preserve a probability distribution. State any bounds or transaction conventions needed for a finite representation without attributing unstated rules to the original task.

#### Knowledge–Skill Pairing

- Deterministic Finite Automata (DFAs) — Understand (Interpret, Explain).
- Requirements Engineering — Apply.
- Analytical and Critical Thinking (FPK) — Apply.

#### Dispositions

Investigative, Collaborative, Responsible, Proactive, Creative.

#### Activation

- ActivationRole: `supporting`
- ActivationMode: `justificatory`
- ActivationConstraint: `mandatory`

#### Summary Table for Competency C02

| Competency | Dispositions | Knowledge | Skill |
| --- | --- | --- | --- |
| Justify the use of Deterministic Finite Automata (DFAs) | Investigative, Collaborative, Responsible, Proactive, Creative | Deterministic Finite Automata (DFAs) | Understand (Interpret, Explain) |
|  |  | Requirements Engineering | Apply |
|  |  | Analytical and Critical Thinking (FPK) | Apply |

### C03 — Test automata using simulators

Origin: Task01 — Cycle 1. Usage in TASK302: reused.

#### Competency Description

Systematically test automata using simulators, compare expected and observed behavior, diagnose discrepancies, and refine models.

#### Contextual Application and Scope

Use JFLAP to investigate sequences of payments and product selections. The original conditional activation is retained: it concerns the use of simulation as evidence for this competency. The task still requires a JFLAP-testable artifact and includes simulation as an instructional objective. The condition is not permission to omit those requirements, and sample executions alone do not prove completeness.

#### Knowledge–Skill Pairing

- Finite State Machines — Apply (Experiment, Relate, Simulate).
- Problem Solving and Troubleshooting (FPK) — Apply.
- Modeling and Simulation — Apply.

#### Dispositions

Collaborative, Responsible, Proactive, Creative.

#### Activation

- ActivationRole: `supporting`
- ActivationMode: `artifact-oriented`
- ActivationConstraint: `conditional`

#### Summary Table for Competency C03

| Competency | Dispositions | Knowledge | Skill |
| --- | --- | --- | --- |
| Test automata using simulators | Collaborative, Responsible, Proactive, Creative | Finite State Machines | Apply (Experiment, Relate, Simulate) |
|  |  | Problem Solving and Troubleshooting (FPK) | Apply |
|  |  | Modeling and Simulation | Apply |

### C04 — Define Regular Expressions for Finite Automata

Origin: Task01 — Cycle 1. Usage in TASK302: reused.

#### Competency Description

Define and apply regular expressions corresponding to languages recognized by finite automata, using formal reasoning about equivalent representations.

#### Contextual Application and Scope

Investigate the relation between the selected finite-automaton representation and regular expressions, presenting at least one expression for a portion of the model and its construction method when that branch of the task is addressed. Preserve the alternative justification requested by the problem statement, but distinguish a difficulty with the representation, assumptions, or method from a claim of nonregularity: a language recognized by a finite automaton always has an equivalent regular expression. The conditional association does not make the investigation itself optional.

#### Knowledge–Skill Pairing

- Finite State Machines — Understand.
- Regular Expressions — Apply.
- Analytical and Critical Thinking (FPK) — Apply.

#### Dispositions

Investigative, Collaborative, Responsible, Proactive, Creative.

#### Activation

- ActivationRole: `extension`
- ActivationMode: `analytical`
- ActivationConstraint: `conditional`

#### Summary Table for Competency C04

| Competency | Dispositions | Knowledge | Skill |
| --- | --- | --- | --- |
| Define Regular Expressions for Finite Automata | Investigative, Collaborative, Responsible, Proactive, Creative | Finite State Machines | Understand |
|  |  | Regular Expressions | Apply |
|  |  | Analytical and Critical Thinking (FPK) | Apply |

## 7. Competency Activation Summary

| ID | Role | Mode | Constraint |
| --- | --- | --- | --- |
| C06 | core | constructive | mandatory |
| C17 | core | analytical | mandatory |
| C18 | core | constructive | mandatory |
| C23 | transversal | analytical | mandatory |
| C05.01 | transversal | justificatory | mandatory |
| C02 | supporting | justificatory | mandatory |
| C03 | supporting | artifact-oriented | conditional |
| C04 | extension | analytical | conditional |

These are associations between TASK302 and eight competencies. They do not constitute a composite competency. C20 remains specific to the musical-collection task and is not reused here. No new composite identifier is assigned. C05 is the base of C05.01; C13.01 is the superseded notation association, not an additional current target.

## 8. Learning Objective–Competency Mapping

| LO | Expected performance | Associated competencies |
| --- | --- | --- |
| LO1 | Abstract domain elements through formal symbols | C18, C23 |
| LO2 | Represent valid and invalid sequences | C17, C23 |
| LO3 | Construct a recognizer for the modeled valid sequences | C06, C18, C02, C23 |
| LO4 | Simulate and examine model behavior | C03, C02 |
| LO5 | Justify correctness, recognition, expressive limits, and nondeterminism | C05.01, C02, C04 |
| LO6 | Document the reasoning rigorously | C05.01, C23 |

The source's unresolved identifier “C0*” in LO4 is corrected to C03, the explicitly specified simulator-testing competency. The remaining associations are preserved, except for the explicit addition of C06 to LO3 described below.

LO3 is directly represented by C06, supported by C18 for abstraction, C02 for model justification, and C23 for notation. The mapping refinement adds the existing construction competency while preserving the original supporting associations. It leaves the objective and deliverables unchanged.

## 9. Integrated Decisions and Consistency Boundaries

### 9.1 Consolidated Specification Decisions

| Issue | Recorded decision | Representation in this report |
| --- | --- | --- |
| Explicit coverage of recognizer construction | Reuse C06 as core, constructive, and mandatory; retain C18, C02, and C23 as supporting associations for LO3 | Existing construction performance is made explicit without redefining C18 or adding a deliverable |
| Reuse of formal abstraction and operations | Reuse C18 and C17 with task-specific scope | Domain modeling and structural sequence analysis |
| Algebraic notation versus grammar rules | Replace the earlier C13.01 association with C23 | Independent notation identity retained |
| Rigorous written justification | Reuse C05.01 | Mathematical arguments within the technical report |
| Suitability and testing of the model | Retain C02 and C03 with their distinct roles | Mandatory justification; conditional simulator-based competence evidence |
| Regular-expression analysis | Retain C04 as a conditional extension | Investigation and the original deliverable alternatives preserved |
| Composite identity | Do not reuse music-specific C20 | Eight task associations without a new composite identifier |

This table consolidates the specification decisions, including the adopted refinement of LO3 through reuse of C06. The earlier mapping contained only C18, C02, and C23; the added association explicitly represents construction. It does not reconstruct a transcript, reviewer count, approval event, or additional review round.

### 9.2 Clarifications and Scope of Validation

Three consistency corrections are explicit: LO4 names C03; the task grouping is not described as an aggregation by C20; and the current C04 title remains “Define Regular Expressions for Finite Automata.”

Theoretical clarification preserves the original instructional choices while avoiding unsupported claims. Nondeterminism is not a probability distribution. Finite-automaton languages have equivalent regular expressions. Finite simulation samples do not establish exhaustive correctness. Price changes alone do not establish increased minimal state complexity.

C03 and C04 retain their conditional activation labels. These are distinguished from the task's JFLAP requirements and regular-expression investigation. The bonus remains an additional challenge. The previously identified LO3 construction-coverage gap is addressed by the adopted reuse of C06. This is a substantive mapping refinement recorded in Section 9.1.

## 10. Final Competency Summary and Conclusion

| ID | Competency | Origin | Usage |
| --- | --- | --- | --- |
| C06 | Develop Problem-Solving Solutions Using Finite State Machines | Task03 — Cycle 1 | Reused |
| C17 | Apply operations on formal languages | TASK25.00 — Cycle 3 | Reused |
| C18 | Model real-world problems using formal language concepts | TASK25.00 — Cycle 3 | Reused |
| C23 | Interpret and apply algebraic notation for strings and languages | TASK25.00 — Cycle 3 | Reused |
| C05.01 | Write mathematically rigorous answers | TASK25.00 — Cycle 3 | Reused |
| C02 | Justify the use of Deterministic Finite Automata (DFAs) | Task01 — Cycle 1 | Reused |
| C03 | Test automata using simulators | Task01 — Cycle 1 | Reused |
| C04 | Define Regular Expressions for Finite Automata | Task01 — Cycle 1 | Reused |

The specified set contains eight reused identifiers and no newly created identifier. This count concerns the recorded associations, including conditional associations. It does not demonstrate that every competence was assessed or that every objective is fully covered.

TASK302 illustrates reuse across contrasting instructional contexts: competencies introduced for conceptual analysis of musical collections support a task that also requires construction and testing of a machine model. The distinction between identity and contextual use is preserved, as are specialization provenance and the boundary around the task-specific composite C20.

The report integrates specification and the available decision rationale in one document. It retains the seven previously specified competencies and adds C06 to make recognizer-construction coverage explicit. Their definitions and the conditional activation of C03 and C04 are preserved. This consolidation does not establish independent ontology validation, formal approval, or observed learner outcomes.

## Post-cycle reference alignment — RF-01-03

On 2 October 2026, repeated component tables were aligned with the documented reference specifications for C02, C03, C04, C06. This maintenance preserves competency identities, origins and existing task activation labels. The earlier file is retained in the refinement archive. The decisions and their scope are recorded in the [post-cycle refinement report](<../../../CSP-Post-Cycle-Refinement-Report.md>).

### Evidence conditions retained in RF-01-03

C03 contributes simulator-based evidence through the executions required by the task; the conditional label concerns the sufficiency of that evidence for the competency, not permission to omit testing. C04 contributes when regular-expression construction or analysis is demonstrated; the task’s investigation remains required.
