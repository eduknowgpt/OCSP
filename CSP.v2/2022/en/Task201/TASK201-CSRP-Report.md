# CSRP-Report  
## Competency Specification Review & Refinement  
### Task201 – Surveillance Drone Prototype


## 1. Introduction

This **Competency Specification Review Report (CSRP-Report)** presents the results of an **expert-based review** of the competencies reused in **Task201 – Surveillance Drone Prototype**, conducted as part of **Phase 2 (Expert Review)** of the **Competency Specification Process (CSP)**.

Following the exploratory and consolidation phases represented by TASK01–TASK05, Task201 constitutes the first CSP application in which **competency reuse was established as a deliberate methodological objective** rather than an emergent outcome of competency authoring. Consequently, the purpose of the expert review was not to expand or redefine the competency catalogue, but to evaluate whether previously specified competencies remained **semantically stable, instructionally coherent, and operationally adequate** when enacted in a new instructional context.

Within this perspective, competencies are treated as **stable semantic entities**, defined independently of a particular task, while their manifestation within the instructional entity is understood as **context-dependent**. The review therefore focused on examining how reused competencies were activated under the specific constraints of the surveillance scenario, considering the expected learner actions, produced artifacts, and forms of observable evidence.

The review aimed to analyze three complementary dimensions:

- the **alignment** between reused competencies and task objectives;
- the **adequacy of competency scope** under new instructional conditions; and
- the **activation patterns** through which competencies became operational within the task.

Rather than proposing new competencies, the expert analysis concentrated on identifying **tensions, clarification needs, and procedural refinements** emerging from competency reuse. Importantly, several observations initially perceived as scope mismatches were later interpreted as differences in **contextual activation**, revealing that variability across tasks did not originate from deficiencies in competency definitions, but from the absence of explicit mechanisms for representing how competencies are enacted in distinct instructional contexts.

In this sense, Task201 represents an important methodological milestone in the evolution of the CSP. The expert review contributes not only to the validation of competency reuse, but also to the consolidation of the distinction between **competency specification** and **competency activation**, a distinction that later informed the formal modeling decisions incorporated into the OntoKSD ontology.



## 2. Overview of Reviewed Competencies

Based on the CSP-Report for Task201, the following competencies were selected for expert review:

- C02 – Justify the use of Deterministic Finite Automata (DFAs)  
- C03 – Test Automata Using Simulators  
- C04 – Define Regular Expressions for Finite Automata  
- C05 – Write a Technical Report  
- C06 – Develop problem solutions using Finite State Machines  
- C11 – Identify Patterns in Finite State Machines  

These competencies originate from the previously established competency set consolidated during earlier CSP applications and were deliberately reused in Task201 to support formal modeling, validation, and documentation activities within the surveillance drone scenario. Their selection reflects an explicit alignment between task requirements, expected learner actions, and observable instructional artifacts, including FSM models, simulation results, and technical reports.

From a methodological perspective, this review does not aim to reassess the intrinsic validity of the competencies themselves, but rather to examine their **adequacy under contextual reuse conditions**. The expert analysis therefore focused on verifying whether the competencies maintained semantic stability while supporting different forms of enactment within a new instructional setting.

Overall, the review identified a **strong correspondence** between the selected competencies, the task objectives, and the expected learner artifacts, particularly with respect to formal modeling, simulation-based validation, analytical reasoning, and technical communication. The observed variations across competencies were interpreted not as structural inconsistencies, but as manifestations of context-dependent activation patterns, reinforcing the need for explicit documentation of how competencies are enacted within specific instructional entities.




## 3. Competency-Level Review Findings

### 3.1 C06 – Develop problem solutions using Finite State Machines

**Review Outcome:** Strong alignment  
**Detected Tension:** None significant  

The expert review identified **C06** as the central competency supporting Task201, directly underpinning the formal modeling of the drone’s surveillance behavior through Finite State Machines (FSMs). Experts agreed that the competency scope adequately covers event interpretation, state-transition design, and behavioral validation through simulation.

In this task, C06 is predominantly activated in a **constructive mode**, as learners are required to design and implement FSM models that respond coherently to environmental events and system constraints. This activation is clearly observable through the produced modeling artifacts and simulation results.

No scope mismatch or overgeneralization was identified. The competency demonstrated **semantic stability under reuse**, confirming its adequacy as a reusable core competency across different instructional contexts while preserving formal rigor.




### 3.2 C02 – Justify the use of Deterministic Finite Automata (DFAs)

**Review Outcome:** Strong alignment  
**Detected Tension:** Low  

The expert review indicated that **C02** was primarily activated at a **reasoning and justificatory level**, supporting learners in explaining the suitability of deterministic models for representing the drone’s surveillance behavior. Although explicit DFA–NFA comparisons were not required as standalone deliverables, learners were expected to justify modeling decisions related to determinism and abstraction within their FSM designs.

This competency was therefore enacted mainly in a **justificatory mode**, complementing the constructive activation of C06. The review confirmed that C02 adequately supports analytical justification even when not expressed through a dedicated artifact, demonstrating stable reuse within the instructional context.




### 3.3 C03 – Test Automata Using Simulators

**Review Outcome:** Very strong alignment  
**Detected Tension:** None  

Expert feedback consistently identified **C03** as one of the most clearly operationalized competencies in Task201. Simulation using **JFLAP** constituted an explicit task requirement and was directly observable through the produced FSM artifacts and validation procedures.

From an activation perspective, C03 was enacted predominantly in an **artifact-oriented mode**, as competency evidence emerged from the execution, testing, and validation of the constructed models. No refinements were recommended for this competency within the context of this task, confirming its stable and unambiguous reuse.




### 3.4 C04 – Define Regular Expressions for Finite Automata

**Review Outcome:** Partial alignment  
**Detected Tension:** Moderate  

The expert review identified a **scope tension** in the reuse of **C04**. Although the task did not explicitly require the construction of regular expressions as deliverable artifacts, experts observed that learners engaged in **symbolic and structural reasoning** about event patterns and FSM complexity, particularly when deriving estimation rules for states and transitions.

In this context, C04 was activated primarily in an **analytical and conceptual mode**, rather than through artifact production. The review therefore indicated that the perceived misalignment did not originate from inadequacy in the competency definition itself, but from the absence of explicit documentation of activation context during reuse.

As a result, reviewers recommended that activation modes be explicitly recorded in CSP artifacts, allowing competencies to be reused flexibly without requiring scope modification or unnecessary specialization.




### 3.5 C11 – Identify Patterns in Finite State Machines

**Review Outcome:** Strong alignment  
**Detected Tension:** Low  

The expert review identified **C11** as well aligned with the abstraction and generalization demands of Task201. Experts emphasized that recognizing structural regularities in FSM design supported reasoning about state minimization and the derivation of general estimation rules relating system behavior to model structure.

In this context, C11 was primarily activated in an **analytical mode**, complementing the constructive activation of C06 by enabling learners to move beyond concrete model construction toward pattern recognition and generalization. The competency therefore reinforces higher-level reasoning processes without introducing scope conflicts or redundancy within the competency set.



### 3.6 C05 – Write a Technical Report

**Review Outcome:** Strong alignment  
**Detected Tension:** None  

Experts confirmed that **C05** aligned directly with the requirement to produce a structured technical report in **SBC format**, serving as the primary mechanism through which learners documented modeling decisions, simulation results, and technical justifications.

In Task201, the competency was predominantly activated in an **artifact-oriented and justificatory mode**, as the written report functioned both as a deliverable artifact and as evidence of conceptual understanding and reasoning. No task-specific refinements were identified, and the competency demonstrated stable reuse within the instructional context.



## 4. Cross-Competency Observations

The expert review revealed that the reused competencies were activated through **distinct contextual modes**, reflecting differences in instructional intent, expected learner actions, and forms of observable evidence within Task201. The following activation patterns were consistently identified:

- **Artifact-oriented activation** (C03, C05), in which competency enactment is directly evidenced through produced artifacts such as simulation outputs and technical reports;
- **Constructive activation** (C06), where learners actively design and implement formal models to satisfy task requirements;
- **Reasoning-oriented activation** (C02, C11), characterized by analytical justification, abstraction, and interpretation of modeling decisions;
- **Analytical or symbolic activation** (C04), involving conceptual reasoning about structural patterns and formal properties without necessarily producing dedicated artifacts.

Experts emphasized that this variation does not indicate misalignment between competencies and task objectives. Instead, it reflects the **context-sensitive nature of competency enactment**, in which a stable competency definition may be mobilized differently depending on instructional constraints and assessment expectations.





## 5. Implications for CSP Application and Refinement

The findings of the expert review provide empirical confirmation of procedural refinements previously incorporated into the **Competency Specification Process (CSP)** following earlier application cycles. Rather than introducing structural modifications to the CSP or redefining the competency set, the observations derived from Task201 clarify how existing CSP phases and artifacts operate when competencies are intentionally reused across distinct instructional contexts.

In particular, the review reinforced the importance of **explicitly documenting the mode of competency activation** during reuse. Expert analysis demonstrated that a single competency may be enacted through different cognitive and operational modes—such as constructive, analytical, justificatory, or artifact-oriented—depending on task requirements and expected learner actions. In Task201, variations in activation did not correspond to changes in competency meaning, but rather to differences in instructional enactment. Making activation modes explicit therefore improves transparency in competency reuse and supports consistent interpretation during expert review without requiring modification of competency definitions.

Additionally, the review highlighted the relevance of **systematically recording scope tensions** observed during reuse, especially in competencies involving symbolic or analytical reasoning. The partial alignment identified in C04 illustrated situations in which conceptual engagement occurs without the production of explicit artifacts. Experts interpreted such cases not as evidence of misalignment, but as indicators that activation context or instructional role should be clarified. Documenting these tensions within the CSP review cycle supports informed methodological decisions while preventing unnecessary proliferation or fragmentation of competencies.

Taken together, these observations confirm that the CSP supports competency reuse through clarification of contextual enactment rather than through continuous restructuring of competency definitions. Task201 thus illustrates how expert review contributes to the progressive stabilization of competency specifications by refining interpretative practices while preserving semantic consistency across applications.



## 6. Conclusion

The expert-based CSRP-Report for Task201 demonstrates that the CSP effectively supports not only the specification of competencies but also their **contextual validation through iterative reuse**. The tensions identified during the review—most notably in the reuse of C04—were interpreted as opportunities to improve semantic clarity and documentation practices rather than as deficiencies in the competency framework itself.

More importantly, Task201 provides empirical evidence that competencies defined in earlier CSP cycles remain semantically stable when enacted in new instructional contexts, provided that activation characteristics and contextual conditions are explicitly documented. In this sense, Task201 constitutes a validation milestone within the CSP lifecycle, confirming that the methodological refinements introduced in previous cycles enable consistent competency reuse without loss of conceptual coherence.

The review therefore illustrates how expert feedback contributes to the progressive maturation and operational reliability of competency models developed through the CSP, supporting their reuse across heterogeneous instructional scenarios while maintaining semantic stability.




