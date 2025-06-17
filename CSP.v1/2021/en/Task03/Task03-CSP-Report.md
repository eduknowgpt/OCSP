# Competency Specification Report: Task03 –  The Farmer Robot

## Introduction

This report applies the **Competency Specification Process (CSP)** to the Problem-Based Learning (PBL) scenario entitled **"The Farmer Robot"**, which engages students in developing a prototype system for **herd identification** in extensive livestock farming environments. The scenario is based on a real-world challenge proposed by the company *Farmer Robot*, which seeks a low-cost solution to automate the classification of animals—bovines, caprines, and swine—using a robotic system equipped with a visual identification module.

Students are required to model and simulate the robot’s decision-making process using **Finite State Machines (FSMs)** and **Regular Expressions**, producing a functional prototype in the **JFLAP** environment. The task fosters the integration of formal languages, computational modeling, and analytical reasoning within a collaborative development setting.

Through the CSP methodology, competencies are **derived and structured** from the analysis of the task description, required knowledge domains, specific learning objectives, and behavioral dispositions. The goal is to define a reusable and context-aware competency framework that supports both **technical development** and **educational relevance**.


## 1. Task Description Analysis

The *Farmer Robot* task challenges students to prototype a decision-making module capable of identifying the presence and quantity of specific herds (bovines, caprines, and swine) within farm enclosures. This capability is crucial for automating feed request logistics and optimizing farm management practices.

To meet the company's operational needs and budget constraints, students must design a **finite state machine** capable of:

* **Classifying animals** into distinct herd categories based on visual input;
* **Detecting minimum herd thresholds**, which trigger feed delivery requests;
* **Representing the module behavior** through a JFLAP simulation;
* **Producing regular expressions** that formalize the system logic;
* **Investigating correlations** between herd thresholds and the minimum number of states and transitions required.

In addition to the technical solution, students are required to produce a **technical report** in the SBC article format. This report must explain the system design, provide usage examples, and address company inquiries related to **documentation clarity** and **cost estimation** based on machine complexity.

This task requires learners to:

* **Apply theoretical knowledge** of FSMs and regular expressions to design a computationally expressive and efficient solution;
* **Translate stakeholder requirements** into formal specifications and logical representations;
* **Analyze patterns and structure** within FSMs to optimize design;
* **Simulate and validate** the solution using appropriate tools (JFLAP);
* **Collaborate effectively**, documenting the design process through structured PBL artifacts such as logbooks and whiteboards.

Through this problem-based scenario, students are expected to integrate **computational theory**, **formal modeling**, and **practical reasoning** into a unified, functional prototype aligned with the needs of a real-world stakeholder.



## 2. Knowledge Enumeration

To successfully complete the *Farmer Robot* task, students must draw upon a combination of theoretical and professional knowledge domains. These knowledge areas are aligned with the **ACM Computing Classification System (2012)** for core computing knowledge and the **ACM/IEEE CC2020** framework for foundational professional competencies (FPK).

This interdisciplinary knowledge base supports the development of an effective and optimized decision-making system for animal classification and feed management.

### Computing Knowledge

* **Finite State Machines (Finite Automata)**
  Fundamental for modeling the robot’s classification logic. FSMs allow students to design and simulate the decision process for herd detection using well-defined states and transitions.

* **Regular Expressions (Regular Languages)**
  Used to represent the behavior of the FSM and validate whether the robot’s input patterns match the expected animal classification formats.

* **Requirements Engineering**
  Enables the interpretation and translation of the company’s functional demands (e.g., low cost, minimum thresholds, interpretability) into system specifications and modeling constraints.

* **Modeling and Simulation**
  Supports the creation, execution, and refinement of FSMs within tools such as **JFLAP**, allowing students to test the system’s behavior and validate outcomes against expected scenarios.

### Professional Knowledge (FPK)

* **Analytical and Critical Thinking**
  Essential for decomposing the problem into solvable parts, identifying optimization opportunities (e.g., minimizing states), and interpreting system behavior through logical reasoning.

* **Problem Solving and Troubleshooting**
  Required for resolving design and implementation challenges, such as ambiguous patterns, state explosion, or regular expression inconsistencies.

* **Written Communication**
  Necessary for delivering a clear and well-structured technical report, providing rationale for design choices, and communicating solutions to stakeholders with varying technical backgrounds.




## 3. Learning Objectives Identification

### General Objective

Apply formal methods—specifically **Finite State Machines** and **Regular Expressions**—to design and simulate a decision-making system for herd classification in a robotic agricultural context.


### Specific Learning Objectives

1. **Model** the behavior of a herd classification system using Finite State Machines.
2. **Generate** Regular Expressions that represent or validate patterns accepted by the FSM.
3. **Identify** the minimal number of states and transitions required for efficient system behavior.
4. **Analyze** correlations between FSM complexity and real-world constraints such as classification thresholds and cost.
5. **Translate** functional requirements into formal specifications using Requirements Engineering techniques.
6. **Test and simulate** FSMs using tools such as JFLAP to validate correctness and effectiveness.
7. **Document** the system behavior, logic, and implementation decisions using structured technical writing.



### Importance of These Objectives

These objectives serve as a **structured pathway for competency development**, enabling students to:

* Connect **abstract formal models** with **concrete real-world applications**;
* Strengthen skills in **formal specification**, **pattern recognition**, and **computational reasoning**;
* Develop autonomy in **evaluating trade-offs** between expressive power, complexity, and performance;
* Improve **collaborative and reflective practices**, such as articulating rationale and sharing modeling decisions;
* Reinforce core competencies aligned with **professional computing practices**, especially in the context of embedded systems and automation.





## 4. Competency Definitions

Competencies are specified based on the **Learning Objectives (LOs)** identified in the task analysis.


### Competency Reuse 

To address Objective 6, "Test and simulate FSMs using tools such as JFLAP to validate correctness and effectiveness," we reuse the competency previously defined in Task01 – The Vending Machine for Sodas and Snacks:

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

### A.1 Competency Title

  Develop Problem-Solving Solutions Using Finite State Machines


### A.2 Textual Description

Design and implement computational solutions using **Finite State Machines (FSMs)** to address real-world or instructional problems involving system modeling through states and transitions. This competency reflects the student's ability to apply theoretical knowledge of automata in constructing reliable and verifiable models that fulfill defined system requirements.

Students are expected to demonstrate not only mastery of FSMs, but also the ability to analyze system requirements and apply logical reasoning to model behavior, ensuring that the solution is both theoretically sound and practically relevant.



### A.3 Knowledge Specification

The following knowledge areas are critical for this competency:

* **Finite Automata (Finite State Machines)**
  Understand and apply the structure, behavior, and applications of deterministic and non-deterministic automata to model sequential systems.

* **Requirements Analysis**
  Identify, interpret, and translate system requirements into formal specifications for FSM design.

* **Analytical and Critical Thinking (FPK)**
  Break down the problem, assess constraints and goals, and select appropriate modeling strategies to guide the design process.



### A.4 Disposition Specification

Given the collaborative nature of the task and the need for creative model development, the following behavioral dispositions are essential:

* **Inventive**
  Propose novel modeling strategies and explore different ways of structuring FSMs to reflect system behavior.

* **Collaborative**
  Cooperate with peers in discussing requirements, designing the machine, and validating its behavior.

* **Responsible**
  Take ownership of the solution's quality, ensuring consistency with task expectations and timelines.

* **Proactive**
  Anticipate implementation challenges and adapt the design to improve accuracy and functionality.

* **Creative**
  Transform system requirements into intuitive and innovative models, making abstract behaviors operational through states and transitions.



### A.5 Knowledge-Skill Pairing

This step maps **knowledge areas to the corresponding skills** required to successfully demonstrate competency in this task.

**A.5.1 Mapping Knowledge to Skills**
To demonstrate this competency, students must show the ability to:

* **Apply** knowledge of **Finite Automata** to design models that reflect real-world behaviors through structured state transitions.

* **Apply** **Requirements Analysis** to understand the user’s expectations and translate them into clear formal specifications that guide FSM design.

* **Apply** **Analytical and Critical Thinking (FPK)** to interpret the problem, analyze possible design paths, and justify modeling decisions based on logic and feasibility.



**A.5.2 Bloom’s Taxonomy Alignment**

* *Apply* is used for all three knowledge areas to assess students’ ability to transfer theoretical knowledge into practice.



**A.5.3 Verb Annotation**
To provide clarity on competency expectations, the following verb annotations define the required actions:

* **Apply** → Finite State Machines → *Use, Implement, Create*
* **Apply** → Requirements Analysis → *Interpret, Specify, Translate*





### A.6 Summary Table for Competency A

| **Competency**                                                    | **Dispositions**                                           | **Knowledge**                          | **Skill**                                 |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | -------------------------------------- | ----------------------------------------- |
| **Develop Problem-Solving Solutions Using Finite State Machines** | Inventive, Collaborative, Responsible, Proactive, Creative | Finite Automata                  | **Apply (Use, Implement, Create)**                        |
|                                                                   |                                                            | Requirements Analysis                  | **Apply (Interpret, Specify, Translate)** |
|                                                                   |                                                            | Analytical and Critical Thinking (FPK) | **Apply**    |




### 4.3 Competency B Specification

### B.1 Competency Title

  Determine Regular Expressions that Represent Automata

### **B.2 Textual Description**

This competency focuses on understanding the relationship between **regular expressions** and **finite automata**, enabling students to interpret automaton structures and express their behavior using equivalent formal representations. It also involves applying **requirements analysis** to identify system needs and translate them into valid components of regular languages.

Learners must demonstrate theoretical comprehension of **regular languages** and their expressive power, as well as the ability to apply systematic analysis to refine or validate the regular expressions corresponding to given automata.


### **B.3 Knowledge Specification**

The following knowledge areas are essential for this competency:

* **Regular Languages**
  * Understand the syntax, semantics, and expressive limits of regular expressions and their formal equivalence to finite automata.

* **Requirements Analysis**
  * Apply methods to identify, interpret, and translate system or task requirements into formal specifications suitable for FSM design.

* **Analytical and Critical Thinking (FPK)**
  * Apply analytical thinking to test and refine regular expressions for correctness, minimality, and functional adequacy.


### **B.4 Disposition Specification**

The following behavioral dispositions support the effective development of this competency:

* **Inventive**
  * Explore alternative regular expressions that preserve equivalence while optimizing for clarity or minimality.

* **Collaborative**
  * Cooperatively analyze and validate the correspondence between automata and regular expressions.

* **Responsible**
  * Ensure that constructed expressions are formally correct and aligned with task requirements.

* **Proactive**
  * Take initiative in testing, iterating, and improving the regular expressions produced.

* **Creative**
  * Demonstrate creativity in modeling approaches that balance simplicity, precision, and expressiveness.


### **B.5 Knowledge-Skill Pairing**

#### **B.5.1 Mapping Knowledge to Skills**

To demonstrate this competency, students must:

* **Understand** knowledge of **Regular Languages** to interpret automata and express equivalent behavior through regular expressions.
* **Apply** knowledge of **Requirements Analysis** to decompose task descriptions and derive relevant regular language representations.
* **Apply** knowledge of **Analytical and Critical Thinking (FPK)** to  iteratively refine regular expressions.

#### **B.5.2 Bloom’s Taxonomy Alignment**

* *Understand* → Regular Languages
* *Apply* → Requirements Analysis
* *Apply* → Analytical and Critical Thinking (FPK)

#### **B.5.3 Verb Annotation**

* **Understand** → Regular Languages → *Interpret, Relate, Represent*
* **Apply** → Requirements Analysis → *Decompose, Translate, Compare*




### B.6 Summary Table for Competency B

| **Competency**                                            | **Dispositions**                                           | **Knowledge**                             | **Skill**                                 |
| --------------------------------------------------------- | ---------------------------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| **Determine Regular Expressions that Represent Automata** | Inventive, Collaborative, Responsible, Proactive, Creative | Regular Languages                         | **Understand (Interpret, Relate, Represent)** |
|                                                           |                                                            | Requirement Analisys                     | **Apply (Decompose, Translate, Compare)** |
|                                                           |                                                            | Analytical and Critical Thinking (FPK) | **Apply**         |






### 4.3 Competency C Specification

### C.1 Competency Title

  Infer and Identify Patterns in Finite State Machines


### C.2 Textual Description

Analyze the structure and behavior of **Finite State Machines (FSMs)** to draw inferences and identify emerging patterns that influence model complexity and performance. This competency involves recognizing relationships between input classifications, state transitions, and the number of states required for effective modeling.

Students are expected to demonstrate the ability to **analyze FSMs**, detect design regularities or redundancies, and apply **Analytical and Critical Thinking (FPK)** to refine and interpret system behavior.


### C.3 Knowledge Specification

The following knowledge areas are critical for this competency:

* **Finite State Machines**
  * Understand structural properties of FSMs, including states, transitions, and minimization principles, and how these influence computational modeling.

* **Analytical and Critical Thinking (FPK)**
  * Apply logical reasoning to identify hidden structures, draw meaningful conclusions, and justify design decisions based on pattern recognition and model analysis.



### C.4 Disposition Specification

Given the abstract nature of the task and the cognitive demands of pattern recognition and inference, the following behavioral dispositions are essential:

* **Inventive**
  * Approach FSM analysis with originality, exploring non-obvious or alternative interpretations of structural behavior.

* **Creative**
  * Devise innovative methods to visualize, interpret, or generalize state-based patterns.

* **Meticulous**
  * Pay careful attention to detail when identifying similarities, redundancies, or inefficiencies in state design and transitions.


### **C.5 Knowledge-Skill Pairing**

This section maps the **knowledge areas** to the corresponding **skills** required to successfully demonstrate this competency.

#### **C.5.1 Mapping Knowledge to Skills**

To demonstrate this competency, students must:

* **Analyze** knowledge of **Finite Automata** to examine state structures, recognize patterns, and determine how input categories influence the number of states and transitions required.
* **Apply** knowledge of **Analytical and Critical Thinking (FPK)** to make informed inferences, detect behavioral regularities, and refine FSM designs based on logical reasoning and task-specific constraints.



#### **C.5.2 Bloom’s Taxonomy Alignment**

The **Analyze** level of Bloom’s Taxonomy is used to assess learners' ability to examine components of FSMs, explain their functional behavior, and justify structural or behavioral improvements based on evidence and reasoning.



#### **C.5.3 Verb Annotation**

To clarify expectations, the following verbs are aligned with the knowledge areas at the Analyze level:

* **Analyze** → Finite Automata → *Analyze, Evaluate, Compare*



### C.6 Summary Table for Competency C

| **Competency**                                           | **Dispositions**                | **Knowledge**                          | **Skill**                              |
| -------------------------------------------------------- | ------------------------------- | -------------------------------------- | -------------------------------------- |
| **Infer and Identify Patterns in Finite State Machines** | Inventive, Creative, Meticulous | Finite Automata                  | **Analyze (Evaluate, Compare)** |
|                                                          |                                 | Analytical and Critical Thinking (FPK) | **Apply**  |





### 4.4 Competency D Specification

### D.1 Competency Title

  Differentiate the Classifications of Formal Grammars



### D.2 Textual Description

Understand and differentiate the various **classes of formal grammars**—as defined by the Chomsky hierarchy—based on their generative power and relation to automata. This competency involves identifying characteristics that distinguish regular, context-free, context-sensitive, and unrestricted grammars, and recognizing their applicability to computational problem-solving.

In the context of the *Robotic Farmer* task, this competency reinforces the theoretical foundation required to select and justify the appropriate computational model (e.g., Finite Automaton) based on system constraints and requirements. 

Students are expected to demonstrate a **conceptual understanding** of grammar classification and apply this understanding when specifying system behaviors, translating requirements into executable logic through **Requirements Engineering** and **Analytical and Critical Thinking (FPK).**



### D.3 Knowledge Specification

The following knowledge areas are critical for this competency:

* **Regular Languages**
  Understand the hierarchical organization of grammars and their relationship to classes of automata and language recognition.

* **Requirements Engineering**
  Translate user needs into system specifications that are compatible with the expressive power of the selected formal language model.

* **Analytical and Critical Thinking (FPK)**
  Interpret system constraints, evaluate grammar applicability, and reason about which classification best suits a given computational problem.



### D.4 Disposition Specification

Given the analytical depth and collaborative demands of the task, the following behavioral dispositions are essential:

* **Collaborative**
  Participate actively in team-based discussions to classify grammars and align them with solution strategies.

* **Responsible**
  Ensure accuracy in theoretical classification and maintain alignment between system specifications and computational models.

* **Proactive**
  Anticipate limitations in modeling choices and explore alternatives within the Chomsky hierarchy.

* **Investigative**
  Explore the theoretical implications of grammar choice and examine edge cases in grammar-automaton equivalence.



### D.5 Knowledge-Skill Pairing

This step maps **knowledge areas to the corresponding skills** required to successfully demonstrate competency in this task.

**D.5.1 Mapping Knowledge to Skills**
To demonstrate this competency, students must show the ability to:

* **Understand** the classes of **Regular Languages** and relate them to their corresponding automata and computational properties.

* **Apply** **Requirements Engineering** to ensure that chosen formal models meet stakeholder needs and system constraints.

* **Apply** **Analytical and Critical Thinking (FPK)** to reason through grammar selection, justify modeling choices, and interpret theoretical implications in practical contexts.



**D.5.2 Bloom’s Taxonomy Alignment**

* *Understand* level is used to assess the student’s conceptual ability to classify grammars and associate them with the correct type of automaton.

* *Apply* level is used to evaluate the student’s capacity to translate system requirements and theoretical knowledge into appropriate model selection and implementation.



**D.5.3 Verb Annotation**
To provide clarity on competency expectations, the following verb annotations define the required actions:

* **Understand** → Regular Languages → *Differentiate, Compare, Classify*
* **Apply** → Requirements Engineering → *Align*
* **Apply** → Analytical and Critical Thinking 



### D.6 Summary Table for Competency D

| **Competency**                                           | **Dispositions**                                     | **Knowledge**                               | **Skill**                                         |
| -------------------------------------------------------- | ---------------------------------------------------- | ------------------------------------------- | ------------------------------------------------- |
| **Differentiate the Classifications of Formal Grammars** | Collaborative, Responsible, Proactive, Investigative | Regular Languages | **Understand (Differentiate, Compare, Classify)** |
|                                                          |                                                      | Requirements Engineering                    | **Apply (Align)**             |
|                                                          |                                                      | Analytical and Critical Thinking (FPK)      | **Apply**          |





## Table of Competencies for Task: *The Farmer Robot*

| **Competency**                                                    | **Dispositions**                                           | **Knowledge**                          | **Skill**                                 |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | -------------------------------------- | ----------------------------------------- |
| **Develop Problem-Solving Solutions Using Finite State Machines** | Inventive, Collaborative, Responsible, Proactive, Creative | Finite Automata                        | **Apply (Use, Implement, Create)**        |
|                                                                   |                                                            | Requirements Analysis                  | **Apply (Interpret, Specify, Translate)** |
|                                                                   |                                                            | Analytical and Critical Thinking (FPK) | **Apply (Analyze, Justify, Evaluate)**    |
|                          |                                                    |
| **Determine Regular Expressions that Represent Automata** | Inventive, Collaborative, Responsible, Proactive, Creative | Regular Languages                         | **Understand (Interpret, Relate, Represent)** |
|                                                           |                                                            | Requirements Analysis                     | **Apply (Decompose, Translate, Compare)** |
|                                                           |                                                            | Analytical and Critical Thinking (FPK) | **Apply (Analyze, Test, Refine)**         |
|                          |                                                    |
| **Infer and Identify Patterns in Finite State Machines** | Inventive, Creative, Meticulous | Finite Automata                        | **Analyze (Evaluate, Compare)**        |
|                                                          |                                 | Analytical and Critical Thinking (FPK) | **Apply (Infer, Justify, Interpret)**  |
|                          |                                                    |
| **Differentiate the Classifications of Formal Grammars** | Collaborative, Responsible, Proactive, Investigative | Regular Languages         | **Understand (Differentiate, Compare, Classify)** |
|                                                          |                                                      | Requirements Engineering                    | **Apply (Align)**                                 |
|                                                          |                                                      | Analytical and Critical Thinking (FPK)      | **Apply**                                         |
|  |  |                                        |       | 
| *Testing Automata Using Simulators (REUSED)* | Collaborative, Responsible, Proactive, Creative | Automata over Infinite Objects | Apply (Experiment, Relate, Simulate) |
|  |  | Problem Solving and Troubleshooting (FPK) | Apply (Diagnose, Debug, Refine) |
|  |  |                                        |       | 
| *Collaborative Technical Report Writing (REUSED)* | Collaborative, Meticulous, Responsible | Written Communication (FPK) | Apply (Write, Structure, Revise, Refine) |

