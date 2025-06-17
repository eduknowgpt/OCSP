# Competency Specification Report: Task204 – Online Judges at Logistic Solutions

**Team Members**: Lais Salvador, Edeyson A. Gomes, Luiz Gavaza  
**Date**: June 8, 2022



## A. Task Description Analysis

Task204 explores the logic behind Online Judge (OJ) systems used to evaluate algorithmic solutions submitted by programmers. It is based on a real problem faced by a startup during programming marathon training, where code submissions for a Traveling Salesman Problem (TSP) instance consistently resulted in **TLE (Time Limit Exceeded)**.

The task challenges students to:
- Analyze the computational nature of the TSP and justify its difficulty.
- Explain why the OJ system cannot detect infinite loops.
- Construct a **Finite State Machine (FSM)** that models the OJ's behavior across outcomes such as **AC**, **WA**, **TLE**, **CE**, and **RE**.
- Connect the practical challenges to core concepts from Computation Theory (e.g., undecidability, the Halting Problem, and NP-completeness).

Deliverables include an SBC-format report containing: team hypotheses and analysis of the TSP scenario, responses to business-level questions, and a modeled FSM with explanations of system limitations.



## B. Knowledge Enumeration

To fulfill the task objectives, the following knowledge areas are required:

- **Finite State Machines** (FSM)
- **Deterministic and Non-deterministic Automata**
- **Turing Machines and Universal Turing Machines**
- **Halting Problem**
- **Recursively Enumerable Languages**
- **P, NP, and NP-Complete Problems**
- **Chomsky Hierarchy**
- **Formal Modeling and Simulation (JFLAP)**
- **Written Technical Communication**
- **Analytical and Critical Thinking**



## C. Learning Objectives and Expected Outcomes

1. Model and simulate the behavior of Online Judges using FSMs.
2. Analyze the TSP in the context of computational complexity and NP-completeness.
3. Explain the Halting Problem and justify the impossibility of detecting infinite loops.
4. Discuss the limits of automation in program evaluation based on formal language theory.
5. Connect real-world evaluation systems to foundational concepts in Computation Theory.
6. Produce a well-structured technical report in SBC format, including examples and theoretical justification.



## D. Competency Specification

Based on the **EdukNow Competence Project**, the following competencies were reused and/or proposed to address Task204:


### **EdukNow_C12 – Develop Problem-Solving Solutions Using Finite State Machines**

**Justification for Reuse:**  
Students are required to design and simulate a Finite State Machine representing the internal logic of the Online Judge system. This competency supports the design and implementation of FSMs that reflect real-world system behavior and decision-making processes.



### **EdukNow_C06 – Justify the Use of Deterministic Finite Automata (DFAs)**

**Justification for Reuse:**  
Part of the analysis involves evaluating the expressive power and limitations of FSMs in modeling the evaluation process. Competency C06 supports theoretical justification of FSM usage versus more expressive models, reinforcing discussions on modeling adequacy.



### **EdukNow_C07 – Test Automata Using Simulators**

**Justification for Reuse:**  
The FSM model of the OJ must be validated and refined using simulation tools like JFLAP. Competency C07 focuses on simulation-based testing and iterative improvement, aligning with the task’s deliverables.



### **EdukNow_C09 – Develop Problem-Solving Solutions Using Turing Machines**

**Justification for Reuse:**  
The task requires analysis of computational undecidability, especially the Halting Problem. Competency C09 supports the design and interpretation of Turing Machine-based solutions and their relevance to understanding the theoretical limits of OJ systems.



### **EdukNow_C16 – Differentiate Classifications of Formal Grammars**

**Justification for Reuse:**  
Students must relate the behavior of Online Judge systems to the Chomsky Hierarchy, understanding the position of FSMs and Turing Machines within the broader spectrum of language classes. Competency C16 supports this comparative classification and formal reasoning.



###  **EdukNow_C04 – Write a Technical Report**

**Justification for Reuse:**  
Task204 requires a structured, formal report that integrates analysis, modeling, and theoretical explanation. Competency C04 ensures that students can collaboratively produce technical documentation with clarity, rigor, and completeness.




## 4. Competency Definition

Competencies are specified based on the **Learning Objectives (LOs)** identified in the task analysis.

### 4.1 Competency B Specification

### A.1 Competency Title

    Understand the Halting Problem and its Implications


### A.2 Textual Description

This competency involves the ability to understand and articulate the theoretical foundations and practical implications of the **Halting Problem**, one of the central results in Computation Theory. Students must be able to explain why it is **undecidable to determine whether an arbitrary program halts** on a given input, and how this impacts the design and limitations of **automated systems such as Online Judges**.

Learners must demonstrate an understanding of the relationship between **Turing Machines**, **recursively enumerable languages**, and **undecidability**, and apply this knowledge to **justify the impossibility of general-purpose loop detection**. This competency also includes the ability to discuss the **boundaries of algorithmic solvability**, critically analyze the limitations of formal models, and connect abstract computational theory to real-world scenarios.

In the context of the Online Judge task, students must provide a **theoretically sound explanation** of why infinite loops cannot be detected algorithmically, and how this limitation reflects fundamental principles of Computation Theory.



### A.3 Knowledge Specification

The following knowledge areas are critical for this competency:

* **The Halting Problem**

  * Central to understanding **undecidability** in computation.
  * Explains the **limits of algorithmic detection** of program behavior.

* **Computability**

  * Provides the formal framework for defining **general computation**.
  * Used to model and reason about the **behavior of arbitrary programs**.

* **Turing Machines**

  * Essential to understanding what **can be semi-decided** by Turing Machines.
  * Clarifies why some problems can only be partially resolved through computation.

* **Analytical and Critical Thinking (FPK)**

  * Required for **evaluating complex theoretical implications**.
  * Supports the **construction of logical arguments** and theoretical justifications.


### A.4 Disposition Specification


**Collaboration**

* The task is grounded in the **Problem-Based Learning (PBL) methodology**, which requires active and continuous interaction among team members.
* Students must **share insights**, **analyze different perspectives**, and **coordinate decisions** related to model design, theoretical justifications, and report writing.
* Collaboration fosters a productive learning environment that supports **peer feedback**, **joint problem-solving**, and **consensus-building** around complex computational concepts.

**Responsibility**

* Each team member must take ownership of specific deliverables, ensuring that contributions are **timely**, **accurate**, and **aligned with project goals**.
* Responsibility includes managing task dependencies, **upholding academic rigor** in the theoretical analysis, and ensuring that the **final report adheres to SBC standards**.
* It also involves the **ethical presentation of results**, particularly when discussing undecidability and system limitations to non-technical audiences.

**Proactivity**

* Proactive learners **anticipate conceptual difficulties**, such as the implications of the **Halting Problem** or **NP-completeness**, and take initiative to explore relevant literature.
* They contribute actively during PBL sessions, **pose critical questions**, and seek clarification on abstract topics (e.g., limits of machine recognition).
* Proactivity also involves identifying and addressing **inconsistencies** in the FSM model or the logical structure of the argumentation before submission.

**Creativity**

* Creativity is essential for **translating theoretical constraints** (e.g., undecidability) into **clear, illustrative FSM models** that simulate the Online Judge system behavior.
* Students are encouraged to **explore alternative representations**, for instance by simulating error paths, integrating timeout transitions, or annotating rejection logic.
* It also enhances the **clarity and engagement** of the report by encouraging the use of **diagrams, metaphors, and real-world analogies** to explain abstract concepts.




### A.5 Knowledge-Skill Pairing

#### A.5.1 Mapping Knowledge to Skills

* **Understand** the **Halting Problem** to justify the impossibility of infinite loop detection.
* **Apply** the concept of Turing Machines to reason about undecidability and computational boundaries.
* **Understand** Computability, including which problems are solvable or semi-decidable.
* **Apply** Analytical and Critical Thinking (FPK) to develop logically coherent arguments linking theory to practice.


#### A.5.2 Bloom’s Taxonomy Alignment

* **Halting Problem – Understand**

    * Enables students to describe, justify, and relate the concept of undecidability to real-world evaluation systems.

    * Evaluates their ability to analyze implications of non-termination in computation.

* **Turing Machines – Apply**

    * Assesses the ability to use the Turing Machine abstraction to explore limits of recognizability and decidability.

    * Supports modeling of theoretical systems such as universal machines and online judges.

* **Understand - Computability**
    * Assesses the student’s capacity to identify and classify problems based on whether they are computable, semi-decidable, or undecidable.

* **Apply - Analytical and Critical Thinking**


#### A.5.3 Verb Annotation

* **Understand** → Halting Problem → **Describe, Justify, Relate**
* **Apply** → Turing Machines → **Use, Model, Explain**
* **Understand** → Computability → **Classify, Recognize, Explain**
* **Apply** → Analytical and Critical Thinking → **Evaluate, Structure, Argue**


### A.6 Summary Table for Competency B

| **Competency**                                      | **Dispositions**                                      | **Knowledge**                    | **Skill**                                     |
| --------------------------------------------------- | ----------------------------------------------------- | -------------------------------- | --------------------------------------------- |
| Understand the Halting Problem and its Implications | Curiosity, Rigor, Responsibility, Analytical Thinking | Halting Problem                  | **Understand (Describe, Justify, Relate)**    |
|                                                     |                                                       | Turing Machines                  | **Apply (Use, Model, Explain)**               |
|                                                     |                                                       | Computability                    | **Understand (Classify, Recognize, Explain)** |
|                                                     |                                                       | Analytical and Critical Thinking | **Apply (Evaluate, Structure, Argue)**        |



## Final Remarks

Task204 combines practical programming challenges with deep theoretical insights, including undecidability, machine modeling, and computational complexity. The selected competencies ensure full coverage of the task's analytical, modeling, simulation, and communication dimensions. Together, they promote the development of theoretical understanding and applied problem-solving skills in real-world contexts such as Online Judge systems and NP-complete problems.


