# **CSP-Adjustments — TASK204: Online Judges at Logistic Solutions**

## 1. Purpose of the Adjustments

This document records the **formal adjustments applied to the CSP specification of TASK204** as a direct consequence of the **Expert Review (CSRP – Phase 2)**.

The adjustments aim to:

* Incorporate **expert recommendations** regarding competency adequacy and scope;
* Resolve **redundancy and over-specification** identified in the CSRP;
* Formalize **activation semantics** (Constraint, Mode, Role);
* Improve **traceability** between task requirements, competencies, and evidence.

These adjustments **do not introduce new competencies** and **do not redefine competency descriptions**.
They strictly document **structural decisions** resulting from expert evaluation.



## 2. Summary of CSRP Findings Informing the Adjustments

Based on the CSRP-Report, experts identified that:

1. Only **one of the two newly proposed competencies is strictly required** at the current scope of TASK204.
2. The second new competency presents **semantic and evidentiary overlap** with the first.
3. Several reused competencies were **correctly selected**, but required **explicit role differentiation**.
4. Modeling and reporting artifacts were sometimes **implicitly treated as cognitive goals**, rather than as **means of externalization or evidence**.

These findings directly motivated the adjustments described below.



## 3. Adjustments to New Competencies

## 3.1 *C15 - Understand the Halting Problem and its Implications*

**Adjustment Decision**

* Retained as a **new competency**.
* Confirmed as the **single core theoretical competency** introduced for TASK204.

**Rationale (from CSRP)**

Expert reviewers agreed that explaining the **impossibility of detecting infinite loops** is a **central and unavoidable cognitive requirement** of the task.

**Final Activation (Adjusted)**

* **ActivationConstraint**: `mandatory`
* **ActivationMode**: `analytical`, `justificatory`
* **ActivationRole**: `core`


### Competency Specification

### Competency Title

    Understand the Halting Problem and its Implications

### Refined Textual Description**

This competency refers to the ability to **conceptually understand and clearly explain** the theoretical foundations and practical implications of the **Halting Problem**, a fundamental result in Computation Theory.

Students must be able to explain why it is **undecidable to determine, in general, whether an arbitrary program halts on a given input**, and how this theoretical limitation constrains the design and behavior of **automated evaluation systems**, such as **Online Judges**.

Learners are expected to demonstrate an understanding of how the Halting Problem emerges from the expressive power of **Turing Machines** and its relationship with **recursively enumerable languages** and **undecidability**, using these concepts to **justify the impossibility of general-purpose loop detection**.

Importantly, this competency emphasizes **conceptual reasoning and justification**, rather than formal proofs or machine constructions. It also includes the ability to discuss the **boundaries of algorithmic solvability**, critically reflect on the limitations of formal computational models, and relate abstract theoretical results to **concrete system behaviors observed in real-world contexts**.

In the context of TASK204, students must provide a **theoretically grounded and coherent explanation** of why infinite loops cannot be detected algorithmically by Online Judges, articulating how this limitation reflects fundamental principles of Computation Theory.



### Knowledge Specification

The following knowledge areas are critical for this competency:

* **The Halting Problem**

  * Central result establishing **undecidability** in computation.
  * Explains the **inherent limits of algorithmic analysis** of program behavior.

* **Computability (Conceptual Level)**

  * Provides the framework for distinguishing between **decidable**, **semi-decidable**, and **undecidable** problems.
  * Supports reasoning about what **can and cannot be automated**.

* **Turing Machines (Conceptual Reference Model)**

  * Serve as the theoretical basis for general computation.
  * Explain why certain problems can be **recognized but not decided**.

* **Analytical and Critical Thinking (FPK)**

  * Required to **evaluate theoretical implications**.
  * Supports the construction of **logically coherent explanations** linking theory and practice.


### Disposition Specification

**Collaboration**

* The competency is developed within a **Problem-Based Learning (PBL)** setting, requiring continuous interaction among team members.
* Learners must exchange interpretations, challenge explanations, and collaboratively refine theoretical arguments.

**Responsibility**

* Students are expected to take responsibility for the **conceptual accuracy and clarity** of their explanations.
* This includes maintaining **theoretical rigor**, proper referencing, and adherence to academic standards when communicating complex limitations.

**Proactivity**

* Learners proactively seek to clarify abstract concepts related to undecidability and computability.
* They identify gaps in their understanding and refine explanations before submission.

**Creativity**

* Creativity supports the translation of abstract theoretical limitations into **clear explanations**, diagrams, or analogies.
* It enhances communicative effectiveness when explaining undecidability to non-specialist audiences.



### Knowledge–Skill Pairing

#### Mapping of Knowledge to Skills

* **Understand** the **Halting Problem** to explain and justify the impossibility of general loop detection.
* **Understand** the conceptual role of **Turing Machines** as a foundation for undecidability arguments.
* **Understand** **Computability** to distinguish solvable, semi-decidable, and unsolvable problems.
* **Apply** **Analytical and Critical Thinking** to structure coherent explanations connecting theory to observed system behavior.

> Note: The use of *Apply* is restricted to **argumentation and reasoning**, not to formal modeling or construction.



### Bloom’s Taxonomy Alignment

* **Halting Problem – Understand**

  * Describe and justify undecidability.
  * Relate theoretical limits to practical systems.

* **Computability – Understand**

  * Classify problems conceptually as decidable or undecidable.

* **Turing Machines – Understand**

  * Explain their role as a reference model for general computation.

* **Analytical and Critical Thinking – Apply**

  * Structure arguments.
  * Evaluate implications.
  * Justify conclusions.



### Verb Annotation (Adjusted)

* **Understand** → Halting Problem → *Describe, Explain, Justify*
* **Understand** → Computability → *Classify, Recognize, Explain*
* **Understand** → Turing Machines → *Explain, Relate*
* **Apply** → Analytical and Critical Thinking → *Evaluate, Structure, Argue*



### Summary Table for Competency C15**

| **Competency**                                      | **Dispositions**                                       | **Knowledge**                    | **Skill**                                     |
| --------------------------------------------------- | ------------------------------------------------------ | -------------------------------- | --------------------------------------------- |
| Understand the Halting Problem and its Implications | Collaboration, Responsibility, Proactivity, Creativity | Halting Problem                  | **Understand (Describe, Explain, Justify)**   |
|                                                     |                                                        | Computability                    | **Understand (Classify, Recognize, Explain)** |
|                                                     |                                                        | Turing Machines                  | **Understand (Explain, Relate)**              |
|                                                     |                                                        | Analytical and Critical Thinking | **Apply (Evaluate, Structure, Argue)**        |







## 3.2 *C16 - Apply Turing Machine Concepts to Analyze Computational System Capabilities*

**Adjustment Decision**

* **Downgraded** from core status.
* Reclassified as **supporting / extension**, depending on instructional emphasis.

**Rationale (from CSRP)**

Experts concluded that:

* The task does **not require explicit application or modeling of Turing Machines**;
* Evidence for this competency is **not independently observable**;
* Its content largely overlaps with the Halting Problem competency.

**Final Activation (Adjusted)**

* **ActivationConstraint**: `optional` or `conditional`
* **ActivationMode**: `interpretative`
* **ActivationRole**: `supporting` or `extension`

> Note: Expert reviewers also indicated that this competency could alternatively be **absorbed as supporting knowledge** within the Halting Problem competency in future CSP iterations.


### Competency Specification

### Competency Title

    Interpret Turing Machine Concepts to Analyze Computational System Capabilities


> **Note**
> The verb *Interpret* is intentionally used to reflect the **expert review recommendation** that this competency should not require formal construction or simulation of Turing Machines.



### Refined Textual Description

This competency refers to the ability to **interpret and conceptually apply core ideas from the Turing Machine model** to analyze the **capabilities and inherent limitations of computational systems**.

Students are expected to use Turing Machines as a **theoretical reference model** to reason about **what classes of problems can or cannot be decided algorithmically**, and to explain how properties such as **Turing-completeness** influence the expressive power of programming languages and automated systems.

Rather than constructing or simulating Turing Machines, learners focus on **conceptual analysis and explanation**, using TM-related concepts to support arguments about **computability boundaries**, **semi-decidability**, and **the impossibility of fully automating certain program analyses**.

In the context of TASK204, this competency supports students in explaining why **Online Judges and similar systems are fundamentally limited**, complementing the Halting Problem discussion by providing a **theoretical interpretation framework**, not an independent modeling activity.



### Knowledge Specification

The following knowledge areas are fundamental for this competency:

* **Turing Machines (Conceptual Reference Model)**

  * Serve as the theoretical foundation for **general-purpose computation**.
  * Support reasoning about the **expressive limits of computational systems**.

* **Computability Theory (Conceptual Level)**

  * Provides the basis for distinguishing **decidable**, **semi-decidable**, and **undecidable** problems.
  * Enables interpretation of **algorithmic limitations** without formal proofs.

* **Universal Turing Machine (Conceptual Notion)**

  * Illustrates the idea of **programmable computation**.
  * Supports explanations of why modern systems inherit fundamental theoretical limits.

* **Analytical and Critical Thinking (FPK)**

  * Required to **interpret theoretical models**.
  * Supports the construction of **coherent explanatory arguments**.



### Disposition Specification

**Collaboration**

* Learners engage in collaborative discussions to align interpretations of abstract computational models.
* Peer interaction supports clarification of conceptual misunderstandings.

**Responsibility**

* Students are responsible for ensuring the **conceptual correctness and clarity** of their explanations.
* This includes avoiding overgeneralizations or misinterpretations of theoretical results.

**Proactivity**

* Learners proactively seek to understand the role of Turing Machines beyond surface definitions.
* They refine explanations when inconsistencies or ambiguities are identified.

**Creativity**

* Creativity supports the use of **analogies, diagrams, and explanatory metaphors** to communicate abstract limits of computation.
* It enhances accessibility of explanations for non-specialist audiences.



### Knowledge–Skill Pairing

#### Mapping of Knowledge to Skills

* **Understand** the conceptual role of **Turing Machines** as a foundation for general computation.
* **Understand** **Computability Theory** to interpret decidability and semi-decidability.
* **Apply** **Analytical and Critical Thinking** to analyze and explain system-level limitations.

> **Important**
> *Apply* here refers to **reasoning and argumentation**, not to formal modeling, construction, or simulation.



### Bloom’s Taxonomy Alignment

* **Turing Machines – Understand**

  * Explain their role as a universal computational model.
  * Relate TM expressiveness to system capabilities.

* **Computability – Understand**

  * Conceptually classify problem classes.
  * Interpret algorithmic limits.

* **Analytical and Critical Thinking – Apply**

  * Analyze implications.
  * Structure explanations.
  * Justify conclusions.



### Verb Annotation

* **Understand** → Turing Machines → *Explain, Relate, Interpret*
* **Understand** → Computability → *Classify, Distinguish, Explain*
* **Apply** → Analytical and Critical Thinking → *Analyze, Structure, Justify*



### **Summary Table for Competency C16**

| **Competency**                                                                 | **Dispositions**                                       | **Knowledge**                    | **Skill**                                       |
| ------------------------------------------------------------------------------ | ------------------------------------------------------ | -------------------------------- | ----------------------------------------------- |
| Interpret Turing Machine Concepts to Analyze Computational System Capabilities | Collaboration, Responsibility, Proactivity, Creativity | Turing Machines                  | **Understand (Explain, Relate, Interpret)**     |
|                                                                                |                                                        | Computability                    | **Understand (Classify, Distinguish, Explain)** |
|                                                                                |                                                        | Analytical and Critical Thinking | **Apply (Analyze, Structure, Justify)**         |




## 4. Adjustments to Reused Competencies

### 4.1 Supporting Competencies

#### **C06 – Develop Problem-Solving Solutions Using Finite State Machines**

**Adjustment Decision**

* Explicitly classified as **supporting**, not core.

**Final Activation**

* **ActivationConstraint**: `mandatory`
* **ActivationMode**: `constructive`
* **ActivationRole**: `supporting`



#### **C03 – Test Automata Using Simulators**

**Adjustment Decision**

* Explicitly marked as **conditional**.

**Final Activation**

* **ActivationConstraint**: `conditional`
* **ActivationMode**: `artifact-oriented`
* **ActivationRole**: `supporting`



### 4.2 Extension Competencies

#### **C02 – Justify the Use of Deterministic Finite Automata**

**Adjustment Decision**

* Retained as **theoretical enrichment only**.

**Final Activation**

* **ActivationConstraint**: `optional`
* **ActivationMode**: `justificatory`
* **ActivationRole**: `extension`



#### **C14 – Differentiate Classifications of Formal Grammars**

**Adjustment Decision**

* Retained as **extension**, with no impact on task success.

**Final Activation**

* **ActivationConstraint**: `optional`
* **ActivationMode**: `analytical`
* **ActivationRole**: `extension`



### 4.3 Transversal Competency

#### **C05 – Write a Technical Report**

**Adjustment Decision**

* Reclassified as **transversal**, not cognitive core.

**Final Activation**

* **ActivationConstraint**: `mandatory`
* **ActivationMode**: `artifact-oriented`
* **ActivationRole**: `transversal`



## 5. Consolidated Activation Configuration (Final)

| Competency                                                   | Constraint             | Mode                      | Role                   |
| ------------------------------------------------------------ | ---------------------- | ------------------------- | ---------------------- |
| Understand the Halting Problem and its Implications          | mandatory              | analytical, justificatory | core                   |
| Apply Turing Machine Concepts to Analyze System Capabilities | optional / conditional | interpretative            | supporting / extension |
| C06 – Develop Solutions Using FSMs                           | mandatory              | constructive              | supporting             |
| C03 – Test Automata Using Simulators                         | conditional            | artifact-oriented         | supporting             |
| C02 – Justify the Use of DFAs                                | optional               | justificatory             | extension              |
| C14 – Differentiate Formal Grammar Classifications           | optional               | analytical                | extension              |
| C05 – Write a Technical Report                               | mandatory              | artifact-oriented         | transversal            |



## 6. Impact of the Adjustments

As a result of these adjustments, TASK204 now exhibits:

* **Strict alignment with Expert Review findings**;
* Clear separation between **cognitive objectives**, **supporting mechanisms**, and **evidence artifacts**;
* Reduced **competency inflation** and improved semantic precision;
* Stronger **methodological consistency** with the CSP–CSRP lifecycle and OntoKSD activation semantics.



## 7. Final Remark

These CSP-Adjustments formalize the transition from **expert judgment (CSRP)** to **authoritative specification (CSP)**.

They ensure that TASK204 stands as a **methodologically robust reference case**, clearly illustrating how **Expert Review informs controlled competency reuse and refinement** within the OntoKSD-driven CSP framework.




