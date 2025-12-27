# **CSRP-Report — TASK204: Online Judges at Logistic Solutions**

## 1. Introduction

This CSRP-Report presents the results of the **Expert Review phase (CSP – Phase 2)** conducted for **TASK204**.
The review aimed to evaluate the **adequacy, clarity, and alignment of the competency set proposed in the CSP-Report**, with particular attention to the **two newly introduced competencies**.

Expert feedback was analyzed to identify:

* Misalignment between competencies and task evidence;
* Overlapping or redundant competency scopes;
* Inconsistencies between intended cognitive outcomes and observable artifacts;
* Necessary refinements in **activation semantics** (Constraint, Mode, Role).



## 2. General Expert Assessment of the Competency Set

Experts agreed that the overall competency set proposed for TASK204 is **theoretically coherent** and aligned with core concepts of **Computation Theory**.
However, reviewers emphasized that **not all competencies play the same pedagogical role**, and that **explicit differentiation is required** to avoid ambiguity during assessment.

In particular, reviewers highlighted that:

* Some competencies represent the **cognitive core** of the task;
* Others function primarily as **supporting mechanisms** or **evidentiary vehicles**;
* The introduction of new competencies must be carefully justified to prevent **competency inflation**.



## 3. Expert Review of New Competency N1

### *Understand the Halting Problem and its Implications*

### 3.1 Alignment with Task Requirements

Experts unanimously recognized that the task explicitly requires students to explain **why an Online Judge cannot detect infinite loops**.
This explanation necessarily relies on the **Halting Problem**, making this competency **directly aligned with the task narrative**.

Reviewers noted that the competency is:

* Clearly grounded in the task description;
* Essential for responding to the managerial questions posed in the scenario;
* Directly observable through explanatory sections of the technical report.

### 3.2 Scope and Knowledge Adequacy

Experts emphasized that the task **does not demand formal undecidability proofs** or advanced computability constructions.
Accordingly, they recommended that this competency be interpreted at a **conceptual and justificatory level**, focusing on explanation rather than formal derivation.

### 3.3 Expert Consensus

The expert panel concluded that this competency is:

* **Necessary and appropriate**;
* Adequate **only when its scope is explicitly constrained** to conceptual understanding.

**Expert Recommendation (Activation)**

* **ActivationConstraint**: mandatory
* **ActivationMode**: analytical, justificatory
* **ActivationRole**: core



## 4. Expert Review of New Competency N2

### *Apply Turing Machine Concepts to Analyze Computational System Capabilities*

### 4.1 Alignment with Task Requirements

Experts raised concerns regarding the necessity of this competency as an **independent learning outcome**.
While Turing Machines are referenced in the theoretical background, the task:

* Does not require students to construct or simulate Turing Machines;
* Does not require explicit TM-based classification or modeling;
* Uses Turing Machines mainly as a **theoretical reference supporting the Halting Problem discussion**.

### 4.2 Redundancy and Observability

Reviewers consistently observed that:

* Evidence supporting this competency **overlaps almost entirely** with evidence already produced for the Halting Problem competency;
* There is no distinct artifact or action that would allow this competency to be assessed independently.

As a result, experts identified a **high risk of semantic redundancy** between N1 and N2.

### 4.3 Expert Consensus

The expert panel concluded that this competency:

* Is **theoretically relevant**, but
* **Not independently observable** at the current task scope.

Experts recommended that it should **not be treated as a core competency**, unless the task is redesigned to explicitly require Turing Machine–based modeling or analysis.

**Expert Recommendation (Activation)**

* **ActivationConstraint**: optional or conditional
* **ActivationMode**: interpretative
* **ActivationRole**: supporting or extension

Alternatively, experts suggested integrating its content as **supporting knowledge within N1**, rather than maintaining it as a standalone competency.



## 5. Expert Review of Reused Competencies

### 5.1 Supporting Competencies

Experts agreed that **FSM modeling and validation** are essential to externalize reasoning about Online Judge behavior, but not the primary cognitive goal.

* **C06 – Develop Problem-Solving Solutions Using FSMs**
  → Appropriate as **supporting**, with mandatory activation.

* **C03 – Test Automata Using Simulators**
  → Appropriate as **conditional supporting**, depending on instructional emphasis.

### 5.2 Extension Competencies

Experts viewed the following as valuable but non-essential:

* **C02 – Justify the Use of DFAs**
* **C14 – Differentiate Classifications of Formal Grammars**

Both were considered suitable as **extension competencies**, enriching theoretical discussion without being required for task completion.

### 5.3 Transversal Competency

* **C05 – Write a Technical Report**

Experts emphasized that the report functions as **the primary evidence artifact**, not as a cognitive end.
Thus, it should be treated as **transversal**, not core.



## 6. Expert-Recommended Activation Summary

| Competency                                                   | Constraint             | Mode                      | Role                   |
| ------------------------------------------------------------ | ---------------------- | ------------------------- | ---------------------- |
| Understand the Halting Problem and its Implications          | mandatory              | analytical, justificatory | core                   |
| Apply Turing Machine Concepts to Analyze System Capabilities | optional / conditional | interpretative            | supporting / extension |
| C06 – Develop Solutions Using FSMs                           | mandatory              | constructive              | supporting             |
| C03 – Test Automata Using Simulators                         | conditional            | artifact-oriented         | supporting             |
| C02 – Justify the Use of DFAs                                | optional               | justificatory             | extension              |
| C14 – Differentiate Formal Grammar Classifications           | optional               | analytical                | extension              |
| C05 – Write a Technical Report                               | mandatory              | artifact-oriented         | transversal            |



## 7. CSRP Conclusion

The Expert Review indicates that **only one of the two newly introduced competencies is strictly required** for TASK204 as currently designed.

While both competencies are theoretically grounded, treating them as **independent core competencies** would introduce redundancy and reduce semantic precision.
Experts therefore recommend **retaining the Halting Problem competency as core** and **downgrading the Turing Machine competency**, ensuring tighter alignment between task demands, evidence, and competency structure.

These findings provide the basis for the subsequent **CSP-Adjustments phase**, where the competency specification is formally revised.
