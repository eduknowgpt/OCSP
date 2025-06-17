# Competency Specification Report: Task05 - The Farmer Robot and the Feeder Robot

## Introduction

This report applies the **Competency Specification Process (CSP)** to the Problem-Based Learning (PBL) scenario entitled **"The Farmer Robot and the Feeder Robot"**, which expands on previous challenges by integrating new functionalities and a second robotic agent. In this scenario, students are required to design computational solutions using **Turing Machines** to model the behavior of both the Farmer Robot and the newly introduced Feeder Robot.

The core challenge is to ensure that, during herd traversal and food delivery signaling, the Farmer Robot also communicates the path the Feeder Robot must follow. Furthermore, a unified abstract machine—capable of sequential read and write operations over unlimited memory—must be employed to implement the navigation modules of both robots. This decision aims to support system documentation standardization and simplify maintenance training.

Through the CSP methodology, competencies are extracted and structured from the task description, relevant knowledge domains, learning objectives, and behavioral dispositions. The result is a structured framework for competency-based learning that integrates computational modeling, tool application, and collaborative problem-solving in real-world-inspired scenarios.



## 1. Task Description Analysis

The *Farmer Robot and Feeder Robot* task addresses the ongoing innovation efforts of the Farmer Robot company. After successful deployments of previous modules for signaling and navigation, the company aims to introduce a new robot, the **Feeder Robot**, that works in coordination with the **Farmer Robot** to deliver supplies to herds efficiently.

The main goal is to integrate the identification and navigation logic of both robots using a unified computational model—a **Turing Machine** with sequential read/write access to unbounded memory. The Farmer Robot must not only alert the herd's location but also encode and transmit the path that the Feeder Robot should follow. Additionally, the Farmer Robot's previous signaling module must be revised to allow input of a minimum threshold for herd member count.

The expected deliverables are:

* A **JFLAP file** implementing both robots' navigation modules using the shared abstract machine model.
* A **technical report** following the SBC article format, documenting the logic, design choices, and execution of the developed modules with examples.

This task requires students to:

* Understand the interaction and coordination between multiple robot modules.
* Revise and enhance existing computational solutions.
* Investigate abstract computational models and apply them to new design scenarios.
* Use **JFLAP** to simulate and validate system behavior.
* Collaborate effectively and maintain structured documentation through PBL tools such as the Whiteboard and Logbook.



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

To support the learning objectives of Task 05, the **competency set defined for Task 02 (*Traffic Control*) is intentionally reused**, as both tasks involve the design, simulation, and documentation of systems modeled using **Turing Machines**. This strategic reuse ensures alignment between instructional goals and promotes coherence across the curriculum.

The decision not to revise or generate a new Competency Specification Review Process (CSRP) for Task 05 is justified by the following pedagogical and methodological considerations:

* **Consistency**: Reinforces key cognitive processes and technical proficiencies—such as formal modeling, symbolic representation, and systematic problem-solving—through repeated application in varied contexts.

* **Efficiency**: Eliminates redundancy in the specification process, allowing instructional focus to shift from redefinition to deeper engagement with the same competency framework.

* **Scalability**: Demonstrates the applicability of well-structured competencies across multiple problem domains, fostering the transfer of learning and strengthening their instructional relevance.

* **Traceability**: Enhances the visibility and continuity of learner progress by preserving competency alignment across tasks, thereby supporting a competency-based education model rooted in transparent and cumulative achievement tracking.

As a result, Task 05 leverages an established and validated set of competencies without the need for additional review or adjustment.


## 5. Competency Reuse Table

| **Competency**                                     | **Dispositions**                                               | **Knowledge**                          | **Skill**                                          |
|----------------------------------------------------|----------------------------------------------------------------|----------------------------------------|----------------------------------------------------|
| **Develop Problem-Solving Solutions Using Turing Machines** | Collaborative, Responsible, Proactive, Creative, Inventive | Turing Machines                        | **Apply (Use, Implement, Execute)**                |
|                                                    |                                                                | Requirements Analysis                  | **Apply (Interpret, Organize)**                    |
|                                                    |                                                                | Analytical and Critical Thinking (FPK) | **Apply (Decompose, Identify)**                    |
|                                                    |                                                                |                                        |                                                    |
| **Identify Turing Machine Variants**               | Investigative, Collaborative, Responsible, Proactive           | Turing Machines                 | **Understand (Differentiate, Recognize, Explain)** |              |                                      
|                                                    |                                                                | Analytical and Critical Thinking (FPK) | **Apply (Evaluate, Decide, Justify)**              |
|                                                    |                                                                |                                        |                                                    |
| **Apply Turing Machine Variants**            | Inventive, Responsible, Proactive, Collaborative, Creative     | Turing Machines                 | **Apply (Use, Adapt, Implement)**                  |
|                                                    |                                                                | Analytical and Critical Thinking (FPK) | **Apply (Evaluate, Decide, Select)**               |
|  |                                        |       |       
| **Write a technical report.** | Collaborative, Meticulous, Responsible | Written Communication (FPK) | **Apply** |
|  |  |                                        |       |       
| **Testing Turing Machines Using Simulators** | Collaborative, Responsible, Proactive, Creative | Turing Machines                           | **Apply (Simulate, Evaluate, Verify)** |
|                                              |                                                     | Problem Solving and Troubleshooting | **Apply (Diagnose, Debug, Refine)**    |
|         |                                 | Modeling and Simulation | **Apply** |
