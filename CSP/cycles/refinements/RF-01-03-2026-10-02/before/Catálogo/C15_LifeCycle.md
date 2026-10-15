# **Competency Lifecycle — C15: Understand the Halting Problem and its Implications**


## 1. Original Definition — *CSP-Report (Cycle 1)*

### Competency Title

    Understand the Halting Problem and its Implications


### Original Intent

The original definition of C15 was introduced to support **theoretical explanation of system limitations** in tasks involving **program analysis and automated evaluation**, particularly within the context of **Online Judges**.

At this stage, the competency aimed to:

* Introduce the **Halting Problem** as a foundational result of Computation Theory;
* Enable students to explain why **infinite loops cannot be detected algorithmically**;
* Provide theoretical grounding for observed system behaviors such as **Time Limit Exceeded (TLE)**.



### Identified Characteristics (Cycle 1)

* Strong theoretical relevance to the task narrative;
* Broad reference to **Turing Machines** and **computability theory**;
* Implicit assumption that students would *apply* TM concepts, without clear evidence requirements;
* Risk of **overlap** with a second newly introduced competency focused on Turing Machines.



## 2. Expert Review — *CSRP-Report (Cycle 1)*

### Key Reviewer Findings

During the Expert Review phase, reviewers identified the following points:

* **Conceptual necessity**
  The Halting Problem was considered **unavoidable** for explaining the impossibility of general loop detection in Online Judges.

* **Scope misalignment risk**
  Reviewers noted that the competency could be **misinterpreted as requiring formal proofs or machine constructions**, which are not demanded by the task.

* **Redundancy with TM-focused competency**
  Much of the evidence supporting this competency overlapped with that of *Apply Turing Machine Concepts to Analyze Computational System Capabilities*.

* **Evidence observability**
  The competency is primarily demonstrated through **explanatory and justificatory text**, not through formal artifacts.



### **Reviewer Recommendations**

Experts recommended that C15 should:

* Be retained as the **single core theoretical competency** of the task;
* Be explicitly constrained to **conceptual understanding and justification**;
* Avoid formal modeling or construction requirements;
* Serve as the **anchor competency**, with TM-related reasoning treated as supporting knowledge.


### Decision Threshold

**CSRP Outcome (Cycle 1):**
**Approved with Scope Refinement**



## 3. Implemented Adjustments — *CSP-Adjustments*

### Declared Changes

Based on the CSRP recommendations, the following adjustments were applied:

* **Scope refinement**

  * Emphasis shifted from *applying* or *modeling* Turing Machines to **conceptual interpretation**.

* **Clarification of cognitive level**

  * Core Bloom level fixed at **Understand**, with **Apply** restricted to argumentation via Analytical and Critical Thinking (FPK).

* **Role consolidation**

  * C15 confirmed as the **single core theoretical competency** introduced for TASK204.

* **Redundancy control**

  * TM-focused competency (C16) downgraded to supporting / extension role.



### **Final Activation (Adjusted)**

* **ActivationConstraint**: `mandatory`
* **ActivationMode**: `analytical`, `justificatory`
* **ActivationRole**: `core`



## **4. Final Version — *Cycle 2 (Approved State)***

### Competency Title

    Understand the Halting Problem and its Implications

### Refined Textual Description

This competency refers to the ability to **conceptually understand and clearly explain** the theoretical foundations and implications of the **Halting Problem**, a fundamental result in Computation Theory.

Learners must be able to explain why it is **undecidable, in general, to determine whether an arbitrary program halts on a given input**, and how this result establishes intrinsic limits on what can be achieved through algorithmic analysis. This includes recognizing that no general-purpose procedure can correctly decide termination for all possible programs and inputs.

Students are expected to demonstrate an understanding of how the Halting Problem arises from the expressive power of **Turing Machines** and its relationship with **recursively enumerable languages** and **undecidability**, using these concepts to **justify fundamental constraints on automated reasoning about program behavior**.

Importantly, this competency emphasizes **conceptual reasoning and theoretical justification**, rather than formal proofs or the construction of abstract machines. It also includes the ability to discuss the **boundaries of algorithmic solvability**, critically reflect on the limitations of formal computational models, and relate abstract results from Computation Theory to **observable properties and behaviors of computational systems** in general.



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






