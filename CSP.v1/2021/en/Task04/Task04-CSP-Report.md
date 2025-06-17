# Competency Specification Report: Task04 - The Return of the Farmer Robot

## Introduction

This report applies the **Competency Specification Process (CSP)** to the Problem-Based Learning (PBL) scenario titled **"The Return of the Farmer Robot"**. The task challenges students to design a navigation module that allows the robot to autonomously return to its initial location after issuing food delivery alerts. The module must be implemented using computational models and validated through simulation.

This scenario is rooted in a real-world agricultural context and emphasizes the application of **formal methods**, including **automata theory** and **context-free grammars**, to address autonomous navigation problems. The proposed solution must be developed in **JFLAP**, with results documented in a formal technical report following SBC (Brazilian Computing Society) standards.

Through the application of CSP, this report identifies and structures the competencies needed to complete the task, focusing on the integration of theoretical knowledge, analytical reasoning, and collaborative problem-solving practices.



## 1. Task Description Analysis

The *Return of the Farmer Robot* task was proposed by the company **Farmer Robot**, following the successful implementation of a previous food delivery signaling module. The new challenge is to enable the robot to autonomously return to its starting point once the alert has been issued.

The student team from UFBA identified that a **finite state machine (FSM)** alone is insufficient to solve the problem. By analyzing the navigation requirements, they concluded that an **auxiliary memory component**—such as a **stack**—was necessary to allow the robot to track its path and reverse its trajectory. This led to the adoption of **Pushdown Automata (PDA)** as the modeling solution.

The solution must simulate the robot’s navigation using **JFLAP**, and document the rules or notations used for path definition and return logic. Additionally, the task encourages teams to consider extending the original Food Delivery Module or designing a parallel solution capable of inter-module communication.

To solve this task, students must:

* Analyze the problem of robotic return navigation and identify the associated computational challenges;
* Use automata theory and memory-augmented machines (e.g., PDA) to model the return behavior;
* Investigate **formal notations** to express location-based rules;
* Implement and test the navigation logic using JFLAP;
* Produce a structured report detailing the solution and reflecting on modeling decisions.



## 2. Knowledge Enumeration

The task requires a combination of computing and professional knowledge domains. Some knowledge was explicitly stated in the task; others were inferred based on the expected activities.

### Computing Knowledge


* **Finite Automata – Pushdown Automata (PDA)**
  Used to model the robot’s navigation with memory, enabling stack-based return logic.

* **Regular Languages (Context-Free Grammars)**
  Supports the definition of formal rules and pattern generation for sequences of locations.

* **Requirements Analysis**
  Essential for identifying and formalizing the system’s functional requirements and constraints.

* **Modeling and Simulation**
  Applied through tools like JFLAP to test the correctness and feasibility of the proposed automaton.

### Professional Knowledge 

* **Analytical and Critical Thinking**
  Enables decomposition of the navigation problem and evaluation of alternatives for the return path.

* **Problem Solving and Solution Development**
  Required to identify, structure, and validate computational approaches to the navigation task.

* **Written Communication**
  Necessary to document the system’s design and simulation results in a formal technical report.



## 3. Learning Objectives Identification

### General Objective

Apply formal computational models—specifically memory-based automata and formal grammars—to develop and validate a robotic navigation system capable of returning to its point of origin.

### Specific Learning Objectives

1. **Understand** the navigation challenges and design constraints of the Farmer Robot system.
2. **Investigate** the use of stack-based memory in automata to enable path tracking and return.
3. **Analyze** the trade-offs between integrating the new module with the existing system or deploying a parallel solution.
4. **Research and define** formal rules using notations or grammars to specify location sequences.
5. **Simulate and test** the return logic using JFLAP, ensuring reliability and accuracy.



## 4. Competency Specification

### Competency Reuse 

To fulfill **Objective 4 — Use simulation tools for finite automata**, we **reuse the competency "Test Computational Automata Using Simulators"** previously defined in *Task01 – The Vending Machine for Sodas and Snacks*:

> Testing Automata Using Simulators

This competency remains fully relevant in the current task, where students are expected to validate their automaton models through formal simulation tools such as JFLAP. The learning outcomes include the ability to execute, observe, and analyze automata behavior in a simulated environment, ensuring functional correctness and alignment with system specifications.

Additionally, since one of the deliverables for this task is a **technical report** formatted according to the academic standards of the **Brazilian Computer Society (SBC)**, we also **reuse the previously defined competency from Task01**:

> Collaborative Technical Report Writing

This competency involves planning, structuring, and composing a comprehensive document that clearly communicates the problem-solving process, decisions made, and justifications for the implemented model. It reinforces essential skills in technical writing, team collaboration, and documentation.

The reuse of these competencies supports the following principles:

* **Pedagogical consistency** in competency development across different learning tasks.
* **Recognition and reinforcement of transversal skills**, such as documentation and tool-based validation.
* **Avoidance of redundancy** through structured competency traceability.
* **Alignment with competency-based education**, where a well-defined learning outcome may be demonstrated in multiple instructional contexts.

By **reusing validated competencies**, we ensure that students build upon previously acquired abilities, promote cumulative learning, and facilitate assessment practices based on observable and transferable performance indicators.


### 4.1 Competency A Specification

#### A.1 Competency Title

  Develop problem-solving solutions using Pushdown Automata

#### A.2 Textual Description

Design and implement a Pushdown Automaton (PDA) capable of representing a navigation strategy for a robotic system, focusing on the return path after food delivery. The solution must simulate how memory structures enable backtracking and route inference.

### **A.3 Knowledge Specification**

The following knowledge areas are essential for mastering this competency:

* **Pushdown Automata and Finite Automata**
  *Understand the principles of state-based computation with memory, focusing on stack operations, transition functions, and language recognition. Apply this knowledge to simulate navigation behavior that requires remembering and reversing sequences.*

* **Requirements Analysis**
  *Identify, structure, and formalize behavioral requirements derived from task analysis. Translate real-world navigation goals into functional and non-functional requirements relevant to PDA design.*

* **Analytical and Critical Thinking**
  *Use systematic reasoning and problem decomposition to model navigation logic. Evaluate design alternatives and justify modeling choices based on behavioral constraints and system goals.*


### **A.4 Disposition Specification**

Effective engagement with this task requires the following behavioral dispositions:

* **Inventive** – Propose novel approaches to modeling navigation logic using PDAs.
* **Collaborative** – Work effectively in teams to refine shared solutions.
* **Responsible** – Demonstrate accountability in modeling decisions and validation.
* **Proactive** – Anticipate challenges in model behavior and adjust accordingly.
* **Creative** – Construct innovative solutions that go beyond straightforward implementations.



### **A.5 Knowledge–Skill Pairing**

#### **A.5.1 Mapping Knowledge to Skills**

To demonstrate this competency, students must be able to:

* **Apply** knowledge of **Pushdown Automata** to model navigation strategies that require memory and backtracking, simulating return paths using stack-based logic.

* **Apply** knowledge of **Requirements Analysis** to extract, structure, and prioritize behavioral specifications aligned with the robot’s goals.

* **Employ** **Analytical and Critical Thinking** to deconstruct complex task requirements, evaluate the adequacy of models, and refine solutions through iterative reasoning.



#### **A.5.2 Bloom’s Taxonomy Alignment**

The primary cognitive processes involved in this competency are aligned with the following Bloom’s levels:

* **Apply** – For using PDA concepts in system modeling and requirements-driven design.


#### **A.5.3 Verb Annotation**

Representative action verbs associated with this competency include:

* *Develop*, *Apply*, *Model*, *Simulate*, *Interpret*, *Construct*, *Refine*, *Justify*




#### A.6 Summary Table for Competency A

| **Competency**                                            | **Dispositions**                                               | **Knowledge**                          | **Skill**                  |
| --------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------- | -------------------------- |
| Develop problem-solving solutions using Pushdown Automata | Inventive, Collaborative, Responsible, Proactive, Creative | Finite Automata                      | **Apply (Develop, Model)** |
|                                                           |                                                                | Requirements Analysis               | **Apply**             |
|                                                           |                                                                | Analytical and Critical Thinking (FPK) | **Apply**                  |




### 4.2 Competency B Specification

#### B.1 Competency Title

  Interpret rule-based notation

#### B.2 Textual Description

Understand and interpret formal notations based on production rules, such as context-free grammars, to represent system behavior and enable navigation control through symbol sequences.

#### B.3 Knowledge Specification

The following knowledge areas are essential for mastering this competency:

* Context-Free Grammars and Regular Languages
  * Understand how these formal languages define structured symbol sequences and how to construct grammars for recognizing or generating specific behavior patterns.

* Pushdown Automata and Finite Automata
  * Understand the correspondence between rule-based languages and automata capable of recognizing them, particularly the role of memory in parsing nested structures.

* Analytical and Critical Thinking (FPK)
  * Apply reasoning skills to interpret rule sets, validate symbolic behavior representations, and refine grammars for clarity, completeness, and correctness.

#### B.4 Disposition Specification

The development of formal, rule-based models requires the following behavioral dispositions:

* Inventive – Propose creative grammar constructs to capture complex behaviors.

* Collaborative – Co-develop and review rule-based models with peers.

* Responsible – Ensure accuracy and consistency in symbolic representations.

* Proactive – Anticipate rule interactions and model ambiguities.

* Creative – Explore multiple grammar structures to represent the same behavior elegantly.

#### B.5 Knowledge-Skill Pairing

**B.5.1 Mapping Knowledge to Skills**
To demonstrate this competency, students must be able to:

* Understand knowledge of Context-Free Grammars and Regular Languages to define symbolic representations of system behavior through production rules.

* Apply knowledge of Automata (PDA and FA) to simulate and validate rule-based control logic in accordance with language constraints.

* Employ Analytical and Critical Thinking to evaluate rule sets, identify ambiguities or redundancies, and improve grammar structures for better alignment with system requirements.


**B.5.2 Bloom’s Taxonomy Alignment**

This competency engages learners at the following cognitive levels:

* **Understand** – To recognize, interpret, and describe the structure and purpose of rule-based models.

* **Apply** – To construct grammars and use symbolic rules to represent and control system behavior.



**B.5.3 Verb Annotation**
Interpret, Apply, Recognize, Analyze

#### B.6 Summary Table for Competency B

| **Competency**                | **Dispositions**                                               | **Knowledge**                          | **Skill**                  |
| ----------------------------- | -------------------------------------------------------------- | -------------------------------------- | -------------------------- |
| Interpret rule-based notation | Inventive, Collaborative, Responsible, Proactive, Creative | Finite Automata                      | **Understand**             |
|                               |                                                                | Regular Languages                      | **Apply (Utilize, Solve)** |
|                               |                                                                | Analytical and Critical Thinking  | **Apply**                  |





### 4.3 Competency C Specification

#### C.1 Competency Title

  Differentiate classifications of formal grammars

#### C.2 Textual Description

Understand and distinguish among formal grammar types (e.g., regular, context-free) and their corresponding automata. Use these distinctions to model and evaluate the behavior of language-based control systems.

#### C.3 Knowledge Specification

The following knowledge areas are essential for this competency:

* **Formal Grammar Classification** (Regular and Context-Free Languages)
  * Understand the Chomsky hierarchy, including grammar types, production rules, and the automata capable of recognizing each class of language.

* **Analytical and Critical Thinking**
  * Apply logical reasoning to differentiate grammar classes, analyze their modeling capabilities, and match them to appropriate system behaviors or constraints.

#### C.4 Disposition Specification

Effectively performing this classification task requires the following dispositions:

* Inventive – Explore alternative representations for grammar-driven systems.

* Collaborative – Engage in peer discussion to refine understanding of grammar distinctions.

* Responsible – Maintain conceptual rigor and consistency when comparing formal models.

* Proactive – Seek deeper insights into language hierarchies and their practical implications.

#### C.5 Knowledge-Skill Pairing

**C.5.1 Mapping Knowledge to Skills**

To demonstrate this competency, students must be able to:

* Understand knowledge of Formal Grammar Classifications to recognize structural and functional distinctions among grammar types.

* Apply Analytical and Critical Thinking to compare grammar properties, relate them to system modeling tasks, and determine the most suitable language class for a given behavior.


**C.5.2 Bloom’s Taxonomy Alignment**

This competency primarily engages learners at the following cognitive levels:

* Understand – For identifying, describing, and classifying types of grammars.

* Apply – For associating grammar types with practical examples in behavior modeling.

**C.5.3 Verb Annotation**
Differentiate, Classify, Compare, Contrast, Identify, Justify

#### C.6 Summary Table for Competency D

| **Competency**                                   | **Dispositions**                                     | **Knowledge**                          | **Skill**                          |
| ------------------------------------------------ | ---------------------------------------------------- | -------------------------------------- | ---------------------------------- |
| Differentiate classifications of formal grammars | Inventive, Collaborative, Responsible, Proactive | Regular Languages                        | **Understand (Differentiate, Compare, Contrast)** |
|                                                  |                                                      | Analytical and Critical Thinking | **Apply**                          |



## Summary Table of Competencies A, B, and C


| **Competency**                                                | **Dispositions**                                           | **Knowledge**                          | **Skill**                                         |
| ------------------------------------------------------------- | ---------------------------------------------------------- | -------------------------------------- | ------------------------------------------------- |
| **Develop problem-solving solutions using Pushdown Automata** | Inventive, Collaborative, Responsible, Proactive, Creative | Pushdown Automata                      | **Apply (Develop, Model)**                        |
|                                                               |                                                            | Requirements Analysis                  | **Apply**                                         |
|                                                               |                                                            | Analytical and Critical Thinking (FPK) | **Apply**                                         |
| **Interpret rule-based notation**                             | Inventive, Collaborative, Responsible, Proactive, Creative | Pushdown Automata                      | **Understand**                                    |
|                                                               |                                                            | Regular Languages                      | **Apply (Utilize, Solve)**                        |
|                                                               |                                                            | Analytical and Critical Thinking       | **Apply**                                         |
| **Differentiate classifications of formal grammars**          | Inventive, Collaborative, Responsible, Proactive           | Regular Languages                      | **Understand (Differentiate, Compare, Contrast)** |
|                                                               |                                                            | Analytical and Critical Thinking       | **Apply**                                         |
|  |  |                                        |       | 
| *Testing Automata Using Simulators (REUSED)* | Collaborative, Responsible, Proactive, Creative | Automata over Infinite Objects | Apply (Experiment, Relate, Simulate) |
|  |  | Problem Solving and Troubleshooting (FPK) | Apply (Diagnose, Debug, Refine) |
|  |  |                                        |       | 
| *Collaborative Technical Report Writing (REUSED* | Collaborative, Meticulous, Responsible | Written Communication (FPK) | Apply (Write, Structure, Revise, Refine) |