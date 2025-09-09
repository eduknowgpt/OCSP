# Competency Specification Report: Task05 - The Farmer Robot and the Feeder Robot

## Introduction

Building on the foundational CSP methodology, this report presents the application of the **Competency Authoring phase** within the Problem-Based Learning (PBL) scenario entitled **"The Farmer Robot and the Feeder Robot"**, which expands on previous challenges by integrating new functionalities and a second robotic agent. In this scenario, students are required to design computational solutions using **Turing Machines** to model the behavior of both the Farmer Robot and the newly introduced Feeder Robot.


## 1. Instructional Entity Analysis

### Title

* The Farmer Robot and the Feeder Robot


### Description

- The **The Farmer Robot and the Feeder Robot** task extends the company’s prior automation modules. A new **Feeder Robot** must collaborate with the **Farmer Robot**, combining herd-location alerts with path encoding to deliver supplies efficiently. Alongside this integration, the existing signaling module must be updated to accept a minimum herd-size threshold before activation.

The core challenge is to ensure that, during herd traversal and food delivery signaling, the Farmer Robot also communicates the path the Feeder Robot must follow. Furthermore, a unified abstract machine—capable of sequential read and write operations over unlimited memory—must be employed to implement the navigation modules of both robots. This decision aims to support system documentation standardization and simplify maintenance training.


### Solution Development Process

Students are expected to:

* **Analyze inter-robot coordination**, identifying data transfer needs between modules.
* **Revise the signaling module** to include herd threshold input logic.
* **Design a unified computational model** using a **Turing Machine** with unbounded, sequential read/write memory to encode path and signaling data.
* **Implement and simulate both modules** in **JFLAP**, verifying correct herd detection, path encoding, and threshold behavior.
* **Document the combined solution** through a technical report following SBC standards, including logic, design rationale, path examples, and coordination flow.
* **Collaborate using PBL tools**, maintaining structured whiteboard diagrams and logbook entries to track design decisions.



### Expected Outcomes

Learners should submit:

* A **JFLAP Turing Machine file** representing the signaling and feeding modules, including path encoding and herd threshold logic.

* A **technical report** (SBC format) containing:

  * Module interaction logic and coordination narrative
  * Turing Machine state and tape definitions
  * Examples demonstrating system execution (e.g., path and threshold scenarios)
  * Justification of design choices and system scalability considerations


### Acquisition Context

* **Environment:** Access to JFLAP or equivalent simulation tools
* **Application:** Useful for teaching computation theory, automata, data processing in CS curricula or infrastructure monitoring contexts



## Target Audience Profile


* **Academic Level**: 2nd–3rd year undergraduate CS students.

* **Domain Background:**
  * Knowledgeable in automata theory and Turing Machines
  * Familiar with programming, state modeling, and data simulation

* **Task Roles:**

  * Formal model designers and simulators
  * Data processors and classification system implementers
  * Technical report authors explaining computational rationale


## Proficiency Scale

| **Level**     | **Descriptor**                                                                                                          | **Grade Range (0–10)** |
| ------------- | ----------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| **Novice**    | Partial or incorrect TM model; fails to correctly process or count categories                                           | 0–5                    |
| **Competent** | Correct TM model with clear classification and counting; successfully simulated and validated                           | >5–9                    |
| **Advanced**  | TM model optimized with multi-tape or nondeterministic features; includes comparative analysis and strong justification | > 9                   |



## 2. Knowledge Enumeration

The successful execution of this task requires mobilizing knowledge from both theoretical computing and professional skills. The knowledge domains are categorized according to the **ACM Computing Classification System (2012)** and **ACM/IEEE CC2020** guidelines.

### Computing Knowledge

* **Turing Machines**
  Essential for modeling both the Farmer Robot and Feeder Robot modules, Turing Machines provide a universal foundation to represent logic that involves memory, control flow, and decision-making.

* **Turing Machine (Variants)**
  Knowledge of variations, such as multi-tape or non-deterministic Turing Machines, may be necessary to optimize the coordination between the two robots or improve efficiency in navigation logic.

* **Church-Turing Thesis**
  Provides the theoretical basis for the task, reinforcing the equivalence between algorithmic reasoning and Turing-computable functions. Students are expected to ground their solutions in this foundational concept.

  * **Requirements Engineering**
  Enables the identification, analysis, and formalization of user needs (e.g., DERBA’s demand for nighttime traffic classification) into computational requirements that guide system design.

* **Modeling and Simulation**
  Required for representing the robots’ behaviors formally and testing them through simulation environments like JFLAP.


### Professional Knowledge (FPK)

* **Analytical and Critical Thinking**
  Supports the analysis of functional dependencies between robots, exploration of abstract machine capabilities, and evaluation of design alternatives.

* **Problem Solving and Solution Design**
  Critical for adapting existing logic, resolving limitations in current modules, and proposing integrated multi-agent navigation strategies.

* **Written Communication**
  Students must produce a structured, technical report that documents the developed modules, justifies design decisions, and communicates results clearly to both technical and non-technical audiences.



## 3. Learning Objectives Identification

### General Objective

Apply knowledge of Turing Machines to develop and integrate identification and navigation modules for both the Farmer Robot and the Feeder Robot.

### Specific Objectives

1. **Understand** the functionalities and new demands related to both robots.
2. **Investigate** the abstract machine model capable of sequential reading and writing to an unlimited memory device and apply it to robotic navigation.
3. **Revise** the food delivery signaling solution, incorporating the specification of minimum herd sizes as input.
4. **Develop** modular and reusable navigation systems for both robots using a unified computational model.
5. **Simulate** robot behavior using the JFLAP tool to validate the modules.

These learning objectives ensure that students combine theoretical and applied knowledge, strengthen algorithmic reasoning, and use simulation tools to prototype functional robotic systems aligned with formal models of computation.


## **4. Competency Specification**

To support the learning objectives of **Task 05 – Farmer & Feeder Robots**, the reviewed competency set originally defined for **Task 02 – Traffic Control** has been intentionally reused. This decision is grounded in strong pedagogical alignment across both tasks and ensures instructional coherence through several key parallels:

### 1. Shared Computational Modeling with Turing Machines

Both tasks require learners to design, implement, and validate **Turing Machine (TM)** models. Task 02 focuses on vehicle classification and counting, while Task 05 extends TM usage to manage multi-agent coordination, path encoding, and threshold logic. The underlying computational concepts—state transitions, tape management, and machine variants—are consistent across both contexts, making the Turing Machine-based competencies directly applicable.

### 2. Common Simulation and Validation Process

Both tasks utilize **JFLAP** or equivalent TM simulators for model execution and correctness testing. Students must demonstrate proficiency in constructing, running, and debugging Turing Machines, reflecting a shared technical skill set emphasized in the reused competencies.

### 3. Uniform Technical Reporting Standards

Both tasks require a **structured technical report** following SBC format. Report expectations—such as system logic, model justification, results, and design rationale—are identical, reinforcing the competencies related to technical communication and documentation.

### 4. Consistent Cognitive Demands

The tasks engage learners in higher-order cognitive activities aligned with Bloom’s taxonomy:

* *Analyze* task requirements
* *Construct* TM models
* *Simulate* and test system behavior
* *Evaluate* and justify design decisions
  This shared cognitive framework further supports competency reuse.



### Pedagogical Benefits of Reuse

* **Curriculum Coherence & Sequencing**
  Reusing competencies creates a clear, scaffolded progression in the curriculum. Students revisit and extend core TM skills from Task 02 in a more complex Task 05 scenario, reinforcing mastery and deepening understanding.

* **Efficiency in Design & Assessment**
  Maintaining consistent competency definitions streamlines instructional design and evaluation. Learners benefit from familiar criteria, reducing cognitive load and providing a stable basis for performance expectations.

* **Enhanced Transferability**
  By applying similar competencies in varied contexts, students demonstrate transfer of learning—a key indicator of skilled computational thinking and flexible problem-solving.


The reuse of Task 02 competencies for Task 05 is therefore not only justified but strategically sound. It aligns the instructional intent, supports deeper skill development, and provides a cohesive learning trajectory centered on formal computational modeling with Turing Machines.

These competencies will be integrated as-is into the Task 05 specification, ensuring alignment and continuity across both tasks.


## 5. Competency Reuse Table


| **ID**  | **Competency**  | **Dispositions**  | **Knowledge** | **Skill**  |
|---------|-----------------|-------------------|---------------|------------|
| (C07) | **Develop Problem-Solving Solutions Using Turing Machines** | Collaborative, Responsible, Proactive, Creative, Inventive | Turing Machines                     | **Create (Develop, Invent, Construct)**                |
|                                                    |                                                                | Requirements Engineering                  | **Apply (Interpret, Organize)**                    |
|                                                    |                                                                | Analytical and Critical Thinking (FPK) | **Apply (Decompose, Identify)**                    |
|                                                    |                                                                |                                        |                                                    |
| (C08) | **Identify Turing Machine Variants**               | Investigative, Collaborative, Responsible, Proactive           | Turing Machines                 | **Understand (Differentiate, Recognize, Explain)** |              |                                      
|                                                    |                                                                | Analytical and Critical Thinking (FPK) | **Apply**              |
|                                                    |                                                                |                                        |                                                    |
| (C09) | **Apply Turing Machine Variants**            | Inventive, Responsible, Proactive, Collaborative, Creative     | Turing Machines                 | **Apply (Use, Adapt, Implement)**                  |
|                                                    |                                                                | Analytical and Critical Thinking (FPK) | **Apply**               |
|                                        |                                                    |
| (C10) | **Testing Turing Machines Using Simulators** | Collaborative, Responsible, Proactive, Creative | Turing Machines                           | **Apply (Simulate, Evaluate, Verify)** |
|                                              |                                                     | Problem Solving and Troubleshooting | **Apply (Diagnose, Debug, Refine)**    |
|         |                                 | Modeling and Simulation | **Apply** |
|  |                                        |       |       
| (C05) | *Write a technical report (REUSED)* | Collaborative, Meticulous, Responsible | Written Communication | Apply |