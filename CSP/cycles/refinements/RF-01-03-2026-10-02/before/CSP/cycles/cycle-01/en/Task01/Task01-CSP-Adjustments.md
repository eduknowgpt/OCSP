# CSP Review Adjustments Report: Task 01 – *The Vending Machine for Sodas and Snacks*

## Introduction

The expert review identified revisions needed in the preliminary competency specification for Task01. The implemented changes address five dimensions:

- Knowledge Granularity — calibrating the level of detail to ensure conceptual precision without unnecessary abstraction;
- Knowledge Appropriateness — ensuring that all knowledge elements are directly relevant to, and operationalized by, the task requirements;
- Controlled Vocabulary — standardizing terminology to promote consistency, interoperability, and reuse across competency specifications;
- Bloom’s Taxonomy Verbs — refining action verbs to clearly express observable skills and intended cognitive levels;
- Textual Clarity — improving wording to eliminate ambiguity, redundancy, and overly prescriptive formulations.

This report records the revisions implemented after the Phase 2 decision, *Approved with Revisions*, and presents the resulting validated competency set.

## Review Findings and Implemented Adjustments

This section connects the accepted review findings to the revisions implemented in the competency specifications.

### Knowledge Granularity Refinement

The preliminary report used broad terms from the ACM Computing Classification System (CCS 2012). The revised specification adopts more specific knowledge terms aligned with the CS2013 reference used during adjustment, including *Finite State Machines*, *Deterministic Finite Automata*, and *Regular Expressions*. This change addresses the granularity problems identified by the review.

### Competency-Specific Adjustments

The following refinements were applied at the individual competency level to ensure tighter alignment between task requirements, knowledge components, and skill descriptors.

- Competency A — *Developing Problem Solutions Using Automata*

  - The knowledge element “Finite Automaton” was refined to “Finite State Machines”, improving conceptual specificity and alignment with the task scope.
  - The knowledge element “Requirements Analysis” was refined to “Requirements Engineering”, reflecting a more precise and standardized terminology.

- Competency B — *Justifying the Use of Deterministic Finite Automata (DFA)*

  - The competency title was reformulated to remove references to non-deterministic models and to emphasize justification within the task scope.
  - The knowledge element “Finite Automaton” was refined to “Deterministic Finite Automata (DFA)”, ensuring conceptual coherence.
  - The knowledge element “Requirements Analysis” was refined to “Requirements Engineering.”
  - The existing pairing “Analytical and Critical Thinking (FPK) — Apply” was retained and made explicit in the final specification because it supports the required justification.

- Competency C — *Testing Automata Using Simulators*

  - The knowledge element “Automata over Infinite Objects” was replaced with “Finite State Machines”, eliminating conceptual mismatch and improving clarity.
  - A new knowledge–skill pairing, “Modeling and Simulation — Apply,” was introduced to ensure that learners actively apply modeling concepts when validating automata behavior using simulation tools.

- Competencies D and E — Merging and Refinement

  - The competencies *“Determining Regular Expressions that Represent Automata”* and *“Relating Regular Expressions to Finite Automata”* were merged into a single competency: “Defining Regular Expressions for Finite Automata.”
  - Associated knowledge refinements included:

    - “Finite Automaton — Understand” refined to “Finite State Machines — Understand”;
    - “Regular Languages — Understand” refined to “Regular Expressions — Apply”;
    - “Analytical and Critical Thinking (FPK)” remained unchanged, as it continues to support reasoning across representations.

- Competency F — *Writing a Technical Report*

  - The competency title was refined from *“Collaborative Technical Report Writing”* to “Writing a Technical Report,” emphasizing the observable outcome rather than the collaboration mode.
  - “Written Communication (FPK),” already present in the preliminary specification, was retained as the relevant professional knowledge component.
  - The Bloom’s Taxonomy level was maintained at Apply, with action verbs such as *write, structure, revise,* and *refine*.

### Controlled Vocabulary Standardization

Terminology was standardized across competency titles, knowledge components, and Bloom-aligned actions in this revision. A broader vocabulary-mapping mechanism defining preferred terms and accepted synonyms remains future work and is not treated as an implemented Task01 adjustment.

## Competency Specification Adjustments

### Competency A Specification

#### A.1 Competency Title

Develop problem solutions using Automata

#### A.2 Competency Description

This competency refers to the ability to design, construct, and validate automaton-based solutions that address well-defined computational problems. Students are expected to interpret system requirements and model behavior using automata, applying formal methods to ensure logical consistency and operational correctness.

Students must:

- Translate problem specifications into automaton models using states and transitions.
- Implement automata using appropriate tools, ensuring their behavior aligns with the intended system logic.
- Refine and test the automaton through simulation, addressing edge cases and improving robustness.
- Integrate constraints or extensions when needed, demonstrating flexibility and adaptive problem-solving.

### Competency B Specification

#### B.1 Competency Title

Justify the use of Deterministic Finite Automata (DFAs)

#### B.2 Competency Description

This competency focuses on the ability to justify the use of a deterministic finite automaton for the task requirements. It combines understanding of DFA behavior with requirements analysis and reasoned justification of the selected representation.

Students must be able to:

- Identify the deterministic behavior required by the vending machine scenario.
- Relate the task requirements to the structure and operation of a DFA.
- Justify the use of a DFA for the proposed solution.

### Competency C Specification

#### C.1 Competency Title

Test Automata Using Simulators

#### C.2 Competency Description

This competency relates to the use of simulation tools (e.g., JFLAP) to verify the correctness and behavior of automata implementations. It emphasizes systematic testing and iterative refinement of state-machine models.

Students must be able to:

- Operate automata simulators to test input/output behavior and transitions.
- Interpret simulation outcomes, identifying discrepancies between expected and observed behavior.
- Diagnose and correct errors through debugging cycles.
- Apply problem-solving strategies to refine automata until desired performance is achieved.

### Competency D+E Specification

#### D+E.1 Competency Title

Define Regular Expressions for Finite Automata

#### D+E.2 Competency Description

This competency focuses on the ability to define and explain a regular expression associated with a relevant part of the finite-automaton solution, as requested by the instructional task.

Students must be able to:

- Identify the part of the automaton to be represented by a regular expression.
- Construct a regular expression for the selected behavior using standard notation.
- Explain how the expression relates to that part of the automaton.
- Check the expression against examples relevant to the task or justify why the expression cannot be provided.

### Competency F Specification

#### F.1 Competency Title

Write a Technical Report

#### F.2 Competency Description

This competency involves the collaborative production of a well-organized technical report that effectively communicates the design, implementation, and evaluation of automaton-based solutions.

Students must demonstrate the ability to:

- Write and structure a report that synthesizes the team's work in a coherent narrative.
- Apply technical writing conventions, ensuring clarity, precision, and logical flow.
- Document technical results and reasoning, including diagrams, formal representations, and testing outcomes.
- Revise and polish the report collaboratively, integrating peer feedback and adhering to presentation standards.

## Validated Competency Summary

| ID  | Competency | Dispositions | Knowledge | Skill |
|---------|--------|-----------|-----------|-------------------|
| (C01) | Develop problem solutions using Automata | Collaborative, Responsible, Proactive, Creative | Finite State Machines | Create (Construct, Develop, Design) |
|         |                                   |                                 | Requirements Engineering | Apply (Interpret, Implement, Organize) |
|         |                                   |                                 | Analytical and Critical Thinking (FPK) | Apply |
| (C02) | Justify the use of Deterministic Finite Automata (DFAs) | Investigative, Collaborative, Responsible, Proactive, Creative | Deterministic Finite Automata (DFAs) | Understand (Interpret, Explain) |
|         |                                   |                                 | Requirements Engineering | Apply |
|         |                                   |                                 | Analytical and Critical Thinking (FPK) | Apply |
| (C03) | Test automata using simulators | Collaborative, Responsible, Proactive, Creative | Finite State Machines | Apply (Experiment, Relate, Simulate) |
|         |                                   |                                 | Problem Solving and Troubleshooting (FPK) | Apply |
|         |                                   |                                 | Modeling and Simulation | Apply |
| (C04) | Define Regular Expressions for Finite Automata | Investigative, Collaborative, Responsible, Proactive, Creative | Finite State Machines | Understand |
|         |                                   |                                 | Regular Expressions | Apply |
|         |                                   |                                 | Analytical and Critical Thinking (FPK) | Apply |
| (C05) | Write a technical report | Collaborative, Meticulous, Responsible | Written Communication (FPK) | Apply (Write, Structure, Revise, Refine) |

## Conclusion

The implemented adjustments increase the specificity of the knowledge components, align the competency definitions with the Task01 requirements, merge the overlapping regular-expression competencies, and standardize the final terminology. The validated competency summary records the resulting specification after the Phase 2 review.

The planned vocabulary-mapping mechanism remains separate from these implemented adjustments. The validated Task01 specification provides input for the semantic structuring conducted in CSP Phase 3.

