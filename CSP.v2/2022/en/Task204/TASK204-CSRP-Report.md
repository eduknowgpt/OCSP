# **CSRP-Report — TASK204: Online Judges at Logistic Solutions**

## 1. Introduction

This CSRP-Report presents the results of the **Expert Review phase (CSP – Phase 2)** conducted for **TASK204**.  
The review aimed to evaluate the **adequacy, clarity, and alignment of the competency set proposed in the CSP-Report**, with particular attention to the **newly introduced competencies** and their relationship to the previously consolidated competency structure.

The expert review focused exclusively on the **conceptual and methodological consistency** of the competency specification. No personal, behavioral, or identifiable participant data were collected or analyzed. The evaluation addressed the alignment between:

- task requirements and expected learning evidence;
- competency scope and instructional purpose;
- cognitive expectations and observable artifacts;
- and the adequacy of competency activation semantics, including **ActivationConstraint**, **ActivationMode**, and **ActivationRole**.

Expert feedback was analyzed to identify:

- potential misalignment between competencies and task evidence;
- overlapping or redundant competency scopes;
- inconsistencies between intended cognitive outcomes and expected deliverables;
- and opportunities for refinement in the explicit representation of activation semantics.

The review also examined whether the introduction of new competencies reflected a genuine semantic requirement or whether observed tensions could be resolved through procedural clarification within the CSP framework.



## 2. General Expert Assessment of the Competency Set

Experts agreed that the competency configuration proposed for TASK204 is **theoretically coherent**, pedagogically meaningful, and well aligned with foundational concepts in **Computation Theory**, particularly undecidability, computational limits, and formal modeling.

The task was recognized as a **conceptual deepening** of previous CSP applications, shifting emphasis from constructive model development toward **analytical and justificatory reasoning** about the limits of computation and automated evaluation systems. This shift was considered appropriate given the instructional objectives of relating real-world systems (Online Judges) to theoretical results such as the Halting Problem and NP-completeness.

However, reviewers emphasized that **competencies assume distinct pedagogical roles within the task**, and that these roles must be made explicit to avoid ambiguity during assessment and reuse. In particular, experts highlighted that:

- some competencies constitute the **cognitive core** of the task, directly supporting theoretical explanation and conceptual understanding;
- others function primarily as **supporting competencies**, enabling modeling, simulation, or contextualization of theoretical arguments;
- transversal competencies operate as **evidentiary vehicles**, allowing learners to externalize reasoning through artifacts such as reports and simulations.

The review therefore reinforced an important CSP principle already observed in TASK201–TASK203:  
differences perceived in competency relevance often originate not from semantic inadequacy, but from **implicit activation roles** that remain undocumented.

Experts also noted that the introduction of new competencies must be carefully justified to prevent **competency inflation**. In the case of TASK204, the newly introduced competencies were considered acceptable because they capture **theoretical reasoning capabilities not previously explicit** in the competency set, particularly those related to undecidability and computability limits. Nevertheless, their activation was characterized as primarily **analytical and justificatory**, rather than constructive.

This assessment confirmed that competency stability is preserved in TASK204, while variability emerges from differences in activation context and instructional intent rather than from structural expansion of the competency catalogue.



## 3. Expert Review of New Competency C15

### *Understand the Halting Problem and its Implications*

### 3.1 Alignment with Task Requirements

Experts unanimously recognized that TASK204 explicitly requires students to explain **why an Online Judge cannot algorithmically detect infinite loops**.  
This explanation necessarily depends on the conceptual understanding of the **Halting Problem**, making this competency **directly aligned with the task’s narrative, learning objectives, and expected explanatory outcomes**.

Reviewers emphasized that the competency emerges naturally from the problem scenario itself, as the managerial questions posed in the task can only be answered through reference to fundamental limits of computation. In this sense, the competency is not an external theoretical addition, but a **conceptual requirement derived from the task’s explanatory demands**.

The activation of this competency was considered clearly observable through:

- theoretical justification sections of the technical report;
- explicit explanations of undecidability and non-termination;
- arguments connecting computational theory to practical system limitations.



### 3.2 Scope and Knowledge Adequacy

Experts emphasized that TASK204 **does not require formal proofs of undecidability**, reductions, or advanced constructions from computability theory. Instead, the competency operates at a **conceptual and justificatory level**, where learners are expected to explain implications rather than formally derive results.

The review therefore clarified that:

- the competency should prioritize **conceptual understanding and explanatory reasoning**;
- the focus lies on interpreting theoretical results and relating them to real-world systems;
- constructive or proof-oriented activation would exceed the pedagogical scope of the task.

This clarification prevents cognitive misalignment between competency expectations and observable artifacts, ensuring consistency between intended learning outcomes and assessment evidence.



### 3.3 Expert Consensus

The expert panel concluded that this competency is:

- **necessary**, given the centrality of undecidability to the task’s explanatory goals;
- **appropriately scoped**, provided that activation remains conceptual rather than formal or constructive;
- consistent with CSP principles regarding the introduction of new competencies only when new semantic requirements emerge.

The competency was therefore validated as a **core analytical competency**, supporting theoretical justification within the task without introducing redundancy with existing modeling competencies.

**Expert Recommendation (Activation)**

- **ActivationConstraint**: mandatory  
- **ActivationMode**: analytical, justificatory  
- **ActivationRole**: core




## 4. Expert Review of New Competency C16

### *Apply Turing Machine Concepts to Analyze Computational System Capabilities*

### 4.1 Alignment with Task Requirements

Experts raised reservations regarding the necessity of this competency as an **independent learning outcome** within the current scope of TASK204.  
Although Turing Machines are explicitly referenced in the theoretical background, reviewers observed that their role in the task is primarily **explanatory rather than operational**.

Specifically, the task:

- does not require students to construct or simulate Turing Machines;
- does not require explicit modeling or classification using Turing Machine formalisms;
- employs Turing Machines mainly as a **theoretical reference supporting the discussion of the Halting Problem and undecidability**.

As a result, the competency was considered **conceptually relevant**, but only indirectly activated by the task requirements.



### 4.2 Redundancy and Observability

Reviewers consistently noted that the observable evidence associated with this competency substantially overlaps with that produced for **C15 – Understand the Halting Problem and its Implications**.

In particular:

- explanations involving Turing Machines appear as part of the justification of undecidability rather than as independent analytical activities;
- no distinct artifact, modeling action, or assessment element allows this competency to be evaluated separately from C15;
- the expected learner output does not require application of Turing Machine concepts beyond conceptual reference.

Consequently, experts identified a **high risk of semantic redundancy**, as both competencies would be supported by the same explanatory evidence in the technical report.



### 4.3 Expert Consensus

The expert panel concluded that this competency is:

- **theoretically appropriate**, given its relevance within Computability Theory;
- **not independently observable** under the current task design;
- therefore unsuitable as a core competency in TASK204 without additional task requirements explicitly demanding Turing Machine–based analysis or modeling.

Experts recommended that, at this stage, the competency should be interpreted as:

- supporting conceptual background for C15; or
- an extension competency activated only when learners go beyond minimum task requirements.

This interpretation preserves conceptual completeness while preventing unnecessary expansion of the competency set.

**Expert Recommendation (Activation)**

- **ActivationConstraint**: optional or conditional  
- **ActivationMode**: interpretative, analytical  
- **ActivationRole**: supporting or extension



## 5. Expert Review of Reused Competencies

### 5.1 Supporting Competencies

Experts agreed that competencies related to **FSM modeling and validation** play an essential role in making the system behavior explicit and observable, but do not constitute the primary cognitive objective of TASK204.

- **C06 – Develop Problem-Solving Solutions Using Finite State Machines**  
  → Considered appropriate as a **supporting competency**, with mandatory activation.  
  The FSM serves as a representational mechanism that externalizes reasoning about Online Judge outcomes, enabling students to structure and communicate system behavior. However, the modeling activity itself is not the central learning objective, which remains focused on theoretical interpretation and limitation analysis.

- **C03 – Test Automata Using Simulators**  
  → Considered appropriate as a **conditional supporting competency**, depending on instructional emphasis.  
  Simulation supports validation and clarification of the FSM model but was not considered essential for demonstrating the task’s core theoretical understanding.

### 5.2 Extension Competencies

Experts evaluated the following competencies as **conceptually valuable but non-essential** for successful task completion:

- **C02 – Justify the Use of Deterministic Finite Automata (DFAs)**
- **C14 – Differentiate Classifications of Formal Grammars**

Both competencies were regarded as suitable **extension competencies**, enriching theoretical discussion and allowing deeper formal analysis when instructional time or learner interest permits. Nevertheless, neither competency was considered necessary for achieving the primary learning outcomes of TASK204.

### 5.3 Transversal Competency

- **C05 – Write a Technical Report**

Experts emphasized that the technical report functions primarily as the **main evidence artifact** through which reasoning, modeling decisions, and theoretical explanations become observable.  

Accordingly, C05 should be interpreted as a **transversal competency**, supporting communication and documentation across the task rather than representing an independent cognitive objective. Its role is evidentiary and integrative, enabling assessment of other competencies rather than constituting a core learning target.




## 6. Expert-Recommended Activation Summary

The expert review consolidated the expected activation configuration for TASK204 by distinguishing between competencies that constitute the **cognitive core of the task**, those that provide **representational or analytical support**, and those that function as **transversal evidentiary mechanisms


| Competency                                                   | Activation Constraint   | Activation Mode            | Activation Role        |
| ------------------------------------------------------------ | ----------------------- | -------------------------- | ---------------------- |
| C15 – Understand the Halting Problem and its Implications    | mandatory               | analytical, justificatory | core                   |
| C16 – Apply Turing Machine Concepts to Analyze System Capabilities | optional / conditional | interpretative             | supporting / extension |
| C06 – Develop Problem-Solving Solutions Using FSMs           | mandatory               | constructive               | supporting             |
| C03 – Test Automata Using Simulators                          | conditional             | artifact-oriented          | supporting             |
| C02 – Justify the Use of Deterministic Finite Automata (DFAs) | optional                | justificatory              | extension              |
| C14 – Differentiate Classifications of Formal Grammars       | optional                | analytical                 | extension              |
| C05 – Write a Technical Report                               | mandatory               | artifact-oriented          | transversal            |





## 7. CSRP Conclusion

The review identified **C15 – Understand the Halting Problem and its Implications** as the **core competency** of the task, since the central learning objective requires students to explain the fundamental limits of automated program evaluation. The competency was considered both necessary and directly observable through the explanatory and justificatory components of the technical report.

The analysis further indicated that **C16 – Apply Turing Machine Concepts to Analyze Computational System Capabilities**, while theoretically relevant, does not produce independently observable evidence at the current task scope. Consequently, experts recommended treating it as a **supporting or extension competency**, activated only when students explicitly mobilize Turing Machine concepts beyond the conceptual explanation required for the Halting Problem.





