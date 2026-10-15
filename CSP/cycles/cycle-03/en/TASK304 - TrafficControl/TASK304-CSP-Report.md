# CSP-Report — TASK304 (TASK25.03) — Traffic Control (2025 Version)

## 1. Introduction

TASK304 concerns symbolic processing of vehicle records from sensors on the Aratu road in Salvador. The required solution counts light, heavy, and very heavy vehicles from the previous night and identifies the predominant category, using Turing Machines and theoretical justification.

### 1.1 Purpose within Cycle 3

Cycle 3 was designed to demonstrate reuse of mature specifications in Theory of Computation. Task authors, specifiers, and reviewers discussed reuse during task development. TASK304 reuses eight identifiers and introduces none: C17, C18, C23, and C05.01 originated in TASK25.00; C07, C09, and C10 in Task02; and C16 in Task204.

The application revisits the Traffic Control scenario from Cycle 1. The current task specifies JFLAP artifacts and an SBC-format report and does not list PBL whiteboards or logbooks as deliverables. Earlier applications also required formal models and theoretical reasoning; the change should not be interpreted as their first introduction. Church–Turing remains explicitly included in this task's knowledge and objectives, regardless of its different treatment in earlier task specifications.

### 1.2 Integrated Specification and Interactive Review

This report integrates instructional analysis, competency specifications, contextual activation, objective mapping, and the available decision rationale. It records consolidated content from the collaborative specification approach without asserting separate CSP-Review or CSP-Adjustments documents, independent evaluation, or a formal approval event. Section 9 makes retained decisions and consistency boundaries explicit.

The task header retains May 20, 2017, and its final note records reformulation by Laís Salvador in November 2025. The submission deadline is November 24, 2025. These statements are preserved as task metadata; they do not date competency reviews.

## 2. Instructional Entity Analysis

### 2.1 Identification

- Title: Traffic Control.
- Type: Problem-based task emphasizing formal modeling and computational analysis.
- Domain: Theory of Computation — Turing Machines and Computability.

### 2.2 Description

Sensor data are encoded as strings over an explicit alphabet. The category boundaries are: light, at most 6 tonnes; heavy, more than 6 and less than 10 tonnes; very heavy, at least 10 tonnes. The machine processes the finite input representing the previous night's records, counts occurrences, compares quantities, and reports the results.

The required output includes counts for every category as well as the predominant category, or explicit encodings of these results. The model uses tape symbols, auxiliary marks or counters, states, and transitions as appropriate. It must be executable in JFLAP and accompanied by a formal explanation.

The statement does not specify tie handling, empty-input behavior, or how entry and exit readings are reconciled into vehicle records. These conventions need to be stated for the chosen model. No particular rule is imposed here as an original requirement.

## 3. Expected Outcomes and Evidence

- One or more JFLAP machine files implementing category counting and comparison.
- A formal input and output encoding, with the interpretation of states, transitions, and auxiliary symbols.
- Documented simulations for different inputs and interpretation of observed behavior.
- An SBC-format technical report explaining the operation, design choices, computability, and correctness of the solution.

The two original deliverable categories remain machine files and the technical report. Submission is through UFBA Moodle by 6:00 p.m. on November 24, 2025. No minimum number of test examples is added where the task gives none.

The Church–Turing thesis relates effective computability to Turing computation. It is not a theorem certifying an individual program. Computability of the specified counting function can be supported by an explicit terminating procedure or machine construction; correctness requires arguments that its outputs satisfy the specification. Simulation supplies complementary evidence for tested cases.

## 4. Knowledge Enumeration

### 4.1 Computing Knowledge

- Computability Theory: computable functions, the Church–Turing thesis, and effective computation.
- Turing Machines: formal definition, states, tape symbols, transitions, halting, and variants.
- Languages and Decision: recognizable and decidable languages and decision formulations over strings.
- Data-Processing Models: symbolic sensor records, counting, comparison, and output encoding.
- Computational Simulation: JFLAP execution, test interpretation, and refinement.

The traffic task is naturally a function computation with counts and category outputs. A decision-problem formulation must state how its answers relate to those requested outputs; acceptance or rejection alone should not silently replace them.

### 4.2 Foundational and Professional Knowledge

- Analytical and Critical Thinking: problem decomposition, model assessment, and justified design choices.
- Written Communication: precise definitions, arguments, and conclusions.

The component specifications below retain additional established knowledge such as Requirements Engineering and Problem Solving and Troubleshooting. Their cognitive mappings are kept distinct from contextual activation modes.

## 5. Learning Objectives

### General Objective

Model, implement, and formally justify data-processing systems using Turing Machines to compute counting and comparison results over symbolic input.

### Specific Objectives

- LO1 — Symbolic abstraction: represent sensor readings and categories as alphabet symbols and input strings.
- LO2 — Problem specification: define the counting and predominant-category computation as a computable function or an explicitly related decision formulation.
- LO3 — Machine construction: design a functional Turing Machine that processes the input and produces the specified counts and category result.
- LO4 — Simulation: test machine behavior in JFLAP on different inputs.
- LO5 — Computability and correctness: justify the effective computation and correctness of the proposed solution; explain the conceptual role of the Church–Turing thesis without treating it as proof of correctness.
- LO6 — Technical communication: present the model, simulations, and arguments in a rigorous report.
- LO7 — Variants: evaluate the need or suitability of Turing Machine variants or extensions.

LO7 was already present in the original mapping and in the task statement. It is included here to align the objective list with those records, rather than to add a new instructional requirement.

## 6. Competency Specifications and Activations

All eight competencies are reused. Contextual descriptions explain their task association without changing their identities or introducing specialized identifiers.

### C17 — Apply operations on formal languages

Origin: TASK25.00 — Cycle 3. Usage in TASK304: reused.

#### Competency Description

Apply, analyze, and justify formal language operations at a conceptual and algebraic level.

#### Contextual Application and Scope

Analyze the structure and segmentation of symbolic input to support counting and comparison. The source also describes scanning and marking; these are machine operations when performed on a tape and belong to the constructed solution under C07. They do not automatically demonstrate formal language operations under C17. Its recorded association remains core, analytical, and mandatory, with this boundary explicit.

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

Origin: TASK25.00 — Cycle 3. Usage in TASK304: reused.

#### Competency Description

Abstract a real-world domain through explicit alphabets, strings, and languages, justifying modeling choices and limitations.

#### Contextual Application and Scope

Encode sensor readings and vehicle categories as symbols and input strings. Explain how the encoding represents the domain and the intended records. This is initial abstraction, distinct from the algorithm that processes the strings.

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

### C07 — Develop problem-solving solutions using Turing Machines

Origin: Task02 — Cycle 1. Usage in TASK304: reused.

#### Competency Description

Design, construct, and validate complete solutions using Turing Machines. Translate requirements into states, tape alphabets, transitions, and halting conditions.

#### Contextual Application and Scope

Construct the machine that counts occurrences by category, compares the counts, and returns the required result. Preserve both outputs requested by the task: category counts and the predominant category. Explain how each is made available in the final tape or documented output representation. C07 directly covers construction in LO3.

#### Knowledge–Skill Pairing

- Turing Machines — Create (Develop, Invent, Construct).
- Requirements Engineering — Apply (Interpret, Organize).
- Analytical and Critical Thinking (FPK) — Apply (Decompose, Identify).

#### Dispositions

Collaborative, Responsible, Proactive, Creative, Inventive.

#### Activation

- ActivationRole: `core`
- ActivationMode: `constructive`
- ActivationConstraint: `mandatory`

#### Summary Table for Competency C07

| Competency | Dispositions | Knowledge | Skill |
| --- | --- | --- | --- |
| Develop problem-solving solutions using Turing Machines | Collaborative, Responsible, Proactive, Creative, Inventive | Turing Machines | Create (Develop, Invent, Construct) |
|  |  | Requirements Engineering | Apply (Interpret, Organize) |
|  |  | Analytical and Critical Thinking (FPK) | Apply (Decompose, Identify) |

### C16 — Interpret Turing Machine Concepts to Analyze Computational System Capabilities

Origin: Task204 — Cycle 2. Usage in TASK304: reused.

#### Competency Description

Interpret Turing Machine concepts as a theoretical reference for analyzing computational capabilities and limitations.

#### Contextual Application and Scope

Explain the suitability of the formalism and relate effective procedures to Turing computation. Distinguish this conceptual interpretation from machine construction under C07. The Church–Turing thesis provides conceptual context, not a proof that a particular transition system is correct. The Universal Turing Machine remains part of the existing conceptual knowledge specification; the paired summary groups the discussion under Turing Machines without assigning a new separate cognitive mapping.

#### Knowledge–Skill Pairing

- Turing Machines — Understand (Explain, Relate, Interpret).
- Computability — Understand (Classify, Distinguish, Explain).
- Analytical and Critical Thinking — Apply (Analyze, Structure, Justify).

#### Dispositions

Collaboration, Responsibility, Proactivity, Creativity.

#### Activation

- ActivationRole: `supporting`
- ActivationMode: `analytical`
- ActivationConstraint: `mandatory`

#### Summary Table for Competency C16

| Competency | Dispositions | Knowledge | Skill |
| --- | --- | --- | --- |
| Interpret Turing Machine Concepts to Analyze Computational System Capabilities | Collaboration, Responsibility, Proactivity, Creativity | Turing Machines | Understand (Explain, Relate, Interpret) |
|  |  | Computability | Understand (Classify, Distinguish, Explain) |
|  |  | Analytical and Critical Thinking | Apply (Analyze, Structure, Justify) |

### C23 — Interpret and apply algebraic notation for strings and languages

Origin: TASK25.00 — Cycle 3. Usage in TASK304: reused.

#### Competency Description

Interpret, use, and justify algebraic notation for strings and languages.

#### Contextual Application and Scope

Describe input strings, alphabets, and language-related aspects of tape contents and configurations consistently. This preserves the decision to use C23 instead of the earlier C13′/C13.01 association for grammar-rule interpretation. Machine-specific transition semantics remain part of C07; C23 is not broadened into every kind of machine notation.

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

Origin: TASK25.00 — Cycle 3. Usage in TASK304: reused.

#### Competency Description

Produce mathematically rigorous written answers connecting definitions, assumptions, arguments, and conclusions.

#### Contextual Application and Scope

Justify the machine behavior, computability, and correctness in the SBC report. Keep simulation examples distinct from general arguments and distinguish Church–Turing interpretation from the proof obligations of the actual algorithm. C05.01 retains its specialization of C05, without adding another written deliverable.

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

### C10 — Test Turing Machines Using Simulators

Origin: Task02 — Cycle 1. Usage in TASK304: reused.

#### Competency Description

Test, validate, and refine Turing Machines with simulation tools; compare observed behavior with the specification and diagnose errors.

#### Contextual Application and Scope

Use JFLAP to execute the constructed machine, observe tape behavior, transitions, halting, and outputs for different inputs, and document corrections. Test results establish behavior for the tested cases; they do not alone prove correctness or termination for every permitted input.

#### Knowledge–Skill Pairing

- Turing Machines — Apply (Simulate, Evaluate, Verify).
- Problem Solving and Troubleshooting (FPK) — Apply (Diagnose, Debug, Refine).
- Modeling and Simulation — Apply.

#### Dispositions

Collaborative, Responsible, Proactive, Creative.

#### Activation

- ActivationRole: `supporting`
- ActivationMode: `artifact-oriented`
- ActivationConstraint: `mandatory`

#### Summary Table for Competency C10

| Competency | Dispositions | Knowledge | Skill |
| --- | --- | --- | --- |
| Test Turing Machines Using Simulators | Collaborative, Responsible, Proactive, Creative | Turing Machines | Apply (Simulate, Evaluate, Verify) |
|  |  | Problem Solving and Troubleshooting (FPK) | Apply (Diagnose, Debug, Refine) |
|  |  | Modeling and Simulation | Apply |

### C09 — Apply Turing Machine Variants

Origin: Task02 — Cycle 1. Usage in TASK304: reused.

#### Competency Description

Select and apply suitable Turing Machine variants using explicit problem requirements and justified modeling choices.

#### Contextual Application and Scope

Evaluate whether a variant provides clearer organization or a more suitable representation. The recorded activation is analytical and conditional, while the task requires evaluation of extensions. A justified choice of the standard model can answer that objective; it does not demonstrate the full performance of applying a variant. If a variant is used, its adaptation and use provide the additional evidence. The existing Apply-level pairings are preserved; no optimization result or equivalence proof is inferred.

#### Knowledge–Skill Pairing

- Turing Machines — Apply (Use, Adapt, Implement).
- Analytical and Critical Thinking (FPK) — Apply.

#### Dispositions

Inventive, Responsible, Proactive, Collaborative, Creative.

#### Activation

- ActivationRole: `extension`
- ActivationMode: `analytical`
- ActivationConstraint: `conditional`

#### Summary Table for Competency C09

| Competency | Dispositions | Knowledge | Skill |
| --- | --- | --- | --- |
| Apply Turing Machine Variants | Inventive, Responsible, Proactive, Collaborative, Creative | Turing Machines | Apply (Use, Adapt, Implement) |
|  |  | Analytical and Critical Thinking (FPK) | Apply |

## 7. Competency Activation Summary

| ID | Role | Mode | Constraint |
| --- | --- | --- | --- |
| C17 | core | analytical | mandatory |
| C18 | core | constructive | mandatory |
| C07 | core | constructive | mandatory |
| C16 | supporting | analytical | mandatory |
| C23 | transversal | analytical | mandatory |
| C05.01 | transversal | justificatory | mandatory |
| C10 | supporting | artifact-oriented | mandatory |
| C09 | extension | analytical | conditional |

C17, C18, and C07 support structural analysis, abstraction, and solution construction. C23 and C05.01 contribute notation and justification across the task. C16 supplies conceptual interpretation, C10 simulator-based evidence, and C09 a conditional extension. These associations do not define a new composite competency. C05 remains the specialization base of C05.01, not an additional target.

## 8. Learning Objective–Competency Mapping

| LO | Expected performance | Associated competencies |
| --- | --- | --- |
| LO1 | Abstract sensor readings and categories as symbols and strings | C18, C23 |
| LO2 | Define counting and the predominant-category computation | C18, C17, C05.01 |
| LO3 | Construct the machine and produce the specified result | C07, C18, C17 |
| LO4 | Simulate and examine machine behavior | C10, C07, C05.01 |
| LO5 | Justify computability, model suitability, and correctness | C16, C05.01, C07 |
| LO6 | Communicate the model, tests, and arguments | C05.01, C23 |
| LO7 | Evaluate extensions or variants | C09, C16 |

The original identifier associations are preserved. Unlike the construction gaps identified in some earlier reports, LO3 explicitly includes C07. LO7 requires evaluation; C09 remains conditional and its full application performance should only be claimed when supported by evidence of variant use, not merely discussion.

## 9. Integrated Decisions and Consistency Boundaries

### 9.1 Consolidated Decisions

| Issue | Decision retained | Result |
| --- | --- | --- |
| Abstraction, analysis, and construction | Reuse C18, C17, and C07 with distinct scopes | Construction is explicitly represented |
| Conceptual interpretation versus implementation | Reuse C16 separately from C07 | Church–Turing discussion does not replace machine-specific correctness arguments |
| Algebraic notation versus grammar rules | Use C23 for the current association | Earlier C13′/C13.01 wording does not add a grammar competency |
| Rigorous explanation | Reuse C05.01 | Mathematical justification remains within the technical report |
| Machine testing | Reuse mandatory C10 | TM-specific simulation scope is preserved |
| Variants | Retain analytical, conditional C09 | Evaluation remains required; actual application depends on the solution |

This table organizes the available rationale, without asserting a transcript, separate review round, approval, or reviewer agreement statistic.

### 9.2 Consistency Findings

- The objective list and mapping now contain the same seven identifiers LO1–LO7. LO7 was recovered from the existing mapping and enunciated objective.
- Eight competence specifications correspond to eight activation entries. Their existing activation triples are preserved.
- Church–Turing remains within the task's instructional scope. Its conceptual interpretation is distinguished from proof of computability by construction and proof of correctness of the chosen machine.
- Both counts and the predominant category remain required; the latter does not replace the former.
- C17's scope is language operations; tape scanning and marking alone do not establish that competence. C23 supports algebraic notation rather than every aspect of machine semantics.
- C09's analytical activation does not redefine its Apply-level component mappings. The detailed and summary disposition wording differs; the local convention is stated in its specification.
- Input reconciliation, ties, and empty input require declared modeling conventions. The report does not invent a single original policy for those cases.

These checks establish consistency of the record and make semantic boundaries inspectable. They do not establish observed learner mastery or independent ontology validation.

## 10. Final Competency Summary and Conclusion

| ID | Competency | Origin | Usage |
| --- | --- | --- | --- |
| C17 | Apply operations on formal languages | TASK25.00 — Cycle 3 | Reused |
| C18 | Model real-world problems using formal language concepts | TASK25.00 — Cycle 3 | Reused |
| C07 | Develop problem-solving solutions using Turing Machines | Task02 — Cycle 1 | Reused |
| C16 | Interpret Turing Machine Concepts to Analyze Computational System Capabilities | Task204 — Cycle 2 | Reused |
| C23 | Interpret and apply algebraic notation for strings and languages | TASK25.00 — Cycle 3 | Reused |
| C05.01 | Write mathematically rigorous answers | TASK25.00 — Cycle 3 | Reused |
| C10 | Test Turing Machines Using Simulators | Task02 — Cycle 1 | Reused |
| C09 | Apply Turing Machine Variants | Task02 — Cycle 1 | Reused |

TASK304 records eight reused identifiers and no creation. Conditional C09 is included because it is a specified association, not because its full performance has necessarily been observed.

The application demonstrates the intended combination of competencies from different tasks: symbolic abstraction, notation, and rigorous writing support machine construction, conceptual interpretation, and testing. Its representational contribution concerns preservation of identity under contextual activation and the distinction between construction, justification, and empirical test evidence. Reuse does not by itself establish complete assessment or ontology sufficiency.

The report integrates the specification and available interactive-review decisions, preserving the task's scope while making theoretical and evidential limits explicit.

## Post-cycle reference alignment — RF-01-03

On 2 October 2026, repeated component tables were aligned with the documented reference specifications for C07, C09, C10, C16. This maintenance preserves competency identities, origins and existing task activation labels. The earlier file is retained in the refinement archive. The decisions and their scope are recorded in the [post-cycle refinement report](<../../../CSP-Post-Cycle-Refinement-Report.md>).

### Evidence conditions retained in RF-01-03

C09 supports evaluation of variants. Its full application performance requires evidence of selecting and using a variant; discussion alone is not counted as a separately demonstrated implementation. C17 requires language-operation reasoning beyond tape scanning. C16 supports conceptual interpretation without replacing C07 construction.
