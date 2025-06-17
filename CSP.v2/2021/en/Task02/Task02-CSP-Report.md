# Competency Specification Report: Task02 – Traffic Control

## Introduction

This report applies the **Competency Specification Process (CSP)** to the Problem-Based Learning (PBL) scenario entitled **"Traffic Control"**, which engages students in designing a computational solution using **Turing Machines** to address vehicle monitoring and classification on highways. The task integrates formal methods and systems thinking to model a real-world problem posed by the Bahia Department of Transport Infrastructure (DERBA).

Through the CSP methodology, competencies are extracted and structured based on the analysis of the task description, relevant knowledge domains, learning objectives, and behavioral dispositions. The goal is to define a robust competency framework aligned with both **technical skill development** and **collaborative problem solving**.



## 1. Task Description Analysis

The *Traffic Control* task challenges students to develop a formal computational solution that addresses a real-world issue identified by the **Bahia Department of Transport Infrastructure (DERBA)**: the deterioration of highways due to excessive pressure from nighttime heavy vehicle traffic.

To support pavement wear prevention efforts, students must design a system capable of:

* **Processing sensor data** collected from vehicle entries and exits on the Aratu highway;
* **Classifying vehicles** into three weight categories (light, heavy, and very heavy);
* **Counting occurrences** for each category during the previous night; and
* **Identifying the most frequent category**, enabling DERBA to prioritize interventions.

The system must be modeled using **Turing Machines**, reflecting a theoretical yet expressive model of computation. Deliverables include one or more **JFLAP-based Turing Machine files** and a **technical report** compliant with SBC formatting standards, clearly explaining the classification logic, design rationale, and simulation process.

This task requires learners to:

* **Translate user-defined goals** into formal system specifications based on computability theory;
* **Model real-world constraints** (e.g., sensor input structure, weight classification logic) using Turing Machines;
* **Evaluate the use of Turing Machine variants** (e.g., multi-tape, non-deterministic) when standard models are insufficient;
* **Simulate and test** the model using appropriate tools to ensure functional correctness;
* **Collaborate effectively** during the problem-solving process, documenting all steps and decisions in a structured and reflective manner.

Through this problem-based learning scenario, students are expected to integrate **theoretical knowledge of computation** with **practical modeling and simulation**, producing a solution that is both educationally rigorous and socially relevant.




## 2. Knowledge Enumeration

To successfully complete the *Traffic Control* task, students must mobilize a set of interrelated theoretical and professional knowledge domains. These domains are aligned with recognized taxonomies: the **ACM Computing Classification System (2012)** for computing knowledge and the **ACM/IEEE CC2020** for professional competencies.

This knowledge foundation ensures that the problem is addressed not only from a technical perspective but also through analytical reasoning, formal specification, and effective communication.

### Computing Knowledge

* **Turing Machines**
  * Fundamental for representing the computational process required to classify vehicles and compute frequency statistics. Students must understand the structure, behavior, and expressive power of Turing Machines to encode real-world operations in a formal model.

* **Turing Machine Variants (Turing Machines)**
  * Knowledge of multi-tape or non-deterministic Turing Machines is essential when standard models are insufficient for performance or expressiveness. Variants allow for more efficient data manipulation and system simulation under complex constraints.

* **Church-Turing Thesis**
  * Provides the theoretical basis for the task, reinforcing the equivalence between algorithmic reasoning and Turing-computable functions. Students are expected to ground their solutions in this foundational concept.

* **Requirements Analysis**
  * Enables the identification, analysis, and formalization of user needs (e.g., DERBA’s demand for nighttime traffic classification) into computational requirements that guide system design.

* **Modeling and Simulation**
  * Involves abstracting system behaviors into formal representations and validating them through tools such as **JFLAP**. This knowledge area supports iterative refinement and verification of the proposed solution.

### Professional Knowledge (FPK)

* **Analytical and Critical Thinking**
  * Required to deconstruct the problem context (e.g., traffic monitoring and classification) into actionable components, and to formulate logical models that meet stakeholder expectations.

* **Problem Solving and Troubleshooting**
  * Essential for addressing implementation issues, such as handling non-standard input formats, optimizing tape usage, or debugging Turing Machine simulations.

* **Written Communication**
  * Needed to produce a well-structured and technically sound report that documents the design rationale, implementation decisions, and validation strategies. This ensures that results are effectively communicated to technical and non-technical audiences, such as DERBA.




## 3. Learning Objectives Identification

### General Objective

Develop and validate formal computational solutions to real-world problems by applying knowledge of **Turing Machines**, with a focus on modeling, classifying, and analyzing traffic data based on sensor input.

This objective highlights the practical application of theoretical computer science concepts, reinforcing the ability to design algorithmic solutions grounded in formal models.

### Specific Objectives

To achieve the general objective, students are expected to:

1. **Identify** system requirements and constraints based on stakeholder input, particularly the needs expressed by DERBA for traffic data analysis and classification.
2. **Translate and align** these requirements with the computational capabilities and limitations of Turing Machines, ensuring a faithful and executable system design.
3. **Evaluate** the adequacy of standard Turing Machines and determine when the use of **machine variants** (e.g., multi-tape, non-deterministic) is necessary to enhance expressiveness or performance.
4. **Apply** the **Church-Turing Thesis** to justify the feasibility of the proposed system, connecting formal computation models with the intuitive concept of algorithmic problem solving.
5.  Provide **Turing Machine** simulations in JFLAP format that demonstrate a functional solution to the problem.

### Importance of These Objectives

These learning objectives establish a **structured and progressive pathway** for competency development by integrating:

* **Theoretical understanding** of formal computation models;
* **Contextual analysis** of real-world problems;
* **Modeling and simulation skills** for system implementation and validation;
* **Critical reflection** on computational adequacy and design decisions.

Together, they ensure that learners are equipped to bridge the gap between **abstract theoretical concepts** and **practical problem-solving**, fostering a competency-based learning experience that is both rigorous and relevant to professional contexts in computing.




## 4. Competency Definitions

Competencies are specified based on the **Learning Objectives (LOs)** identified in the task analysis.


### Competency Reuse 

Since one of the deliverables for this task is a **technical report** formatted according to the academic standards of the **Brazilian Computer Society (SBC)**, we reuse the previously defined competency from *Task01*:

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
    Develop Problem-Solving Solutions Using Turing Machines


### A.2 Textual Description  
Design and implement a Turing Machine that processes and classifies vehicle data, transforming user requirements into a functional model. Validate the model through simulation and ensure alignment with practical constraints.


### A.3 Knowledge Specification
The following knowledge areas are critical for this competency:  

- **Turing Machines (nmT):**
    - Essential to achieving the overall objective, this knowledge involves understanding and applying the principles of Turing Machines to model the solution for traffic categorization and analysis.

- **Requirements Analysis:**
    - Necessary to accurately identify and formalize the needs of DERBA technicians, ensuring that system requirements are well understood and properly implemented.

- **Analytical and Critical Thinking (FPK):**
    - Fundamental for planning and developing the solution, enabling students to analyze available information, evaluate alternative strategies, and propose approaches that balance accuracy and efficiency.

### A.4 Disposition Specification

The analysis of the **Traffic Control on Aratu Road*** task highlights key behavioral dispositions required to solve the problem and deliver an effective solution. The main dispositions include:

**Collaborative**
- Work closely with team members to design and integrate all parts of the system, share insights, and ensure a cohesive solution.

**Responsible**
- Demonstrate commitment to the quality of the solution, meeting deadlines, and ensuring that DERBA's technical requirements are fully addressed.

**Proactive**
- Anticipate potential implementation challenges, propose improvements, and adapt the computational model to increase the accuracy of vehicle classification.

**Inventive**
- Explore different Turing Machine variants and their applicability to traffic control, analyzing the most effective ways to process sensor data from the highway.

**Creative**
- Develop innovative solutions to enhance the nighttime traffic data analysis, allowing the system to become more efficient and responsive to infrastructure management needs.

### A.5 Knowledge-Skill Pairing

This step maps **knowledge areas to the corresponding skills** required to successfully demonstrate competency in this task.  

**A.5.1 Mapping Knowledge to Skills**  

To achieve this competency, students must demonstrate the ability to: 

- **Apply** *Analytical and Critical Thinking* along with knowledge of *Turing Machines* to develop a computational solution that processes and classifies traffic data. This includes modeling sensor behavior and vehicle categorization within the formal structure of a Turing Machine.

- **Use** *Turing Machines* to represent and simulate the logic of counting and categorizing vehicles, ensuring that the model correctly processes the data and delivers an efficient solution to the problem.

- **Apply** *Requirements Analysis* to correctly identify and specify the essential requirements of the system. Students must elicit DERBA’s needs, interpret sensor data, and define criteria for traffic analysis, ensuring that user requirements are translated into practical functionalities in the developed solution.


**A.5.2 Bloom’s Taxonomy Alignment**  

To ensure a structured and progressive learning approach, each knowledge component is aligned with Bloom’s Revised Taxonomy, providing a clear framework for competency assessment.

- **MTuring Machines - Apply**
- Apply level is used to assess students’ ability to employ the concept of Turing Machines in modeling and solving the traffic control problem.

- **Requirements Analysis - Apply**
- Apply level is used to evaluate whether students can interpret and structure system requirements based on the problem’s needs.

- **Analytical and Critical Thinking (FPK) - Apply**
- Apply level is selected to assess students’ ability to break down the problem into manageable components and develop effective strategies for solving it.

**A.5.3 Verb Annotation**  
To provide clarity on competency expectations, the following verb annotations define the required actions:  

#### **Turing Machines – Apply**

* **Use** a Turing machine model to represent system behavior.
* **Implement** configurations and transitions in a simulation environment.
* **Execute** processes defined by the machine to solve structured problems.

 **Verbs**: *Use*, *Implement*, *Execute*


#### **Requirements Analysis – Apply**

* **Interpret** the functional and non-functional needs described in the problem.
* **Organize** those needs into formal specifications.
* **Apply** principles of requirement modeling to guide system design.

 **Verbs**: *Interpret*, *Organize*, *Apply*


#### **Analytical and Critical Thinking (FPK) – Apply**

* **Decompose** the system into manageable logical components.
* **Identify** key variables and interactions.
* **Apply** structured reasoning to map problem characteristics into formal models.

 **Verbs**: *Decompose*, *Identify*, *Apply*



### A.6 Summary Table for Competency A

| **Competency** | **Dispositions** | **Knowledge** | **Skill** |
|------------|-----------|------------|----|
|  |   | Turing Machines  | **Apply (Use, Implement, Execute)** |
| **Develop Problem-Solving Solutions Using Turing Machines** | **Collaborative, Responsible, Proactive, Creative, Inventive** | Requirements Analysis | **Apply (interpret, Organize)** |
| | | Analytical and Critical Thinking (FPK) | **Apply (Decompose, Identify)** |



### 4.2 Competency B Specification

### B.1 Competency Title

    Identify Turing Machine Variants


### B.2 Textual Description

Understand and identify different **variants of Turing Machines**—such as multi-tape, non-deterministic, or other extensions—by analyzing their computational capabilities and constraints. Students are expected to evaluate whether the use of standard Turing Machines is sufficient or if extended models are necessary to effectively address system requirements.

This competency reflects a conceptual understanding of the **Church-Turing Thesis**, and requires students to apply **Analytical and Critical Thinking (FPK)** to assess system needs and propose appropriate modeling approaches based on the specific characteristics of Turing Machine variants.


### B.3 Knowledge Specification

The following knowledge areas are critical for this competency:

* **Turing Machine Variants**
  * Involves recognizing different types of Turing Machines (e.g., multi-tape, non-deterministic) and understanding their operational implications for modeling and problem-solving.

* **Church-Turing Thesis**
  * Provides a theoretical foundation to assess the expressive power and feasibility of formal models used in real-world algorithmic problems.

* **Analytical and Critical Thinking (FPK)**
  * Supports the evaluation of system requirements and the selection of the most appropriate computational models to meet functional objectives.



### B.4 Disposition Specification

As the *Traffic Control* task is carried out collaboratively, and involves analysis and decision-making under complex conditions, the following behavioral dispositions are essential:

* **Inventive**
  Demonstrate curiosity and rigor in exploring the computational implications of various Turing Machine extensions.

* **Collaborative**
  Engage in collective analysis and justification of modeling decisions, contributing to team-based evaluation of alternatives.

* **Responsible**
  Ensure that modeling decisions are logically consistent, grounded in theory, and meet the problem’s specifications.

* **Proactive**
  Take initiative in exploring and proposing more expressive computational solutions where needed.



### B.5 Knowledge-Skill Pairing

This step maps **knowledge areas to the corresponding skills** required to successfully demonstrate competency in this task.

**B.5.1 Mapping Knowledge to Skills**
To demonstrate this competency, students must show the ability to:

* **Apply** Analytical and Critical Thinking to evaluate system requirements and determine whether standard or variant Turing Machines should be used.

* **Understand** Turing Machine Variants to distinguish between their capabilities and select the model best suited to the problem’s constraints.

* **Understand** the Church-Turing Thesis to justify, at a conceptual level, the feasibility and completeness of using extended Turing Machine models.



**B.5.2 Bloom’s Taxonomy Alignment**

* *Apply* level is used to assess the ability to analyze the problem, evaluate modeling options, and justify the selection of computational variants.

* *Understand* level is used to evaluate conceptual knowledge of both the **Turing Machine variants** and the **Church-Turing Thesis**, ensuring students can explain and justify their modeling decisions.



**B.5.3 Verb Annotation**
To provide clarity on competency expectations, the following verb annotations define the required actions:

* **Apply** → Analytical and Critical Thinking → *Evaluate, Decide, Justify*
* **Understand** → Turing Machine  → *Differentiate, Recognize, Explain*
* **Understand** → Church-Turing Thesis → *Interpret, Justify, Reflect*



### B.6 Summary Table for Competency B

| **Competency**                       | **Dispositions**                                     | **Knowledge**                          | **Skill**                                          |
| ------------------------------------ | ---------------------------------------------------- | -------------------------------------- | -------------------------------------------------- |
| **Identify Turing Machine Variants** | Investigative, Collaborative, Responsible, Proactive | Turing Machines                | **Understand (Differentiate, Recognize, Explain)** |
|                                      |                                                      | Church-Turing Thesis                   | **Understand (Interpret, Justify)**                |
|                                      |                                                      | Analytical and Critical Thinking (FPK) | **Apply (Evaluate, Decide, Justify)**              |




### 4.3 Competency C Specification

### C.1 Competency Title

  Make Use of Turing Machine Variants


### C.2 Textual Description

Understand and apply different **variants of Turing Machines**—such as multi-tape and non-deterministic models—to develop optimized solutions for computational problems.This competency involves analyzing system requirements and determining whether standard Turing Machines are sufficient or if extended capabilities are needed.

Students are expected to demonstrate a conceptual understanding of the **Church-Turing Thesis**, associating the formal model of computation with the intuitive notion of an algorithm. They must also apply analytical reasoning to identify the most suitable computational model for the problem at hand.


### C.3 Knowledge Specification

The following knowledge areas are critical for this competency:

* **Turing Machine Variants**
  Understanding alternative computational models (e.g., multi-tape, non-deterministic) and their expressive and operational differences compared to standard Turing Machines.

* **Church-Turing Thesis**
  Grasping the theoretical basis that connects formal models of computation with algorithmic reasoning, and using this to justify the feasibility and completeness of proposed solutions.

* **Analytical and Critical Thinking (FPK)**
  Essential for evaluating problem requirements and selecting the most appropriate modeling approach based on complexity, efficiency, and expressiveness.



### C.4 Disposition Specification

The analysis of the *Traffic Control on Aratu Road* task highlights behavioral attributes that support the critical evaluation and adaptation of computational models to suit practical needs. The main dispositions include:

* **Investigative**
  Explore alternative computational models and assess their relevance to the problem context.

* **Responsible**
  Justify modeling decisions with theoretical and practical consistency, ensuring that chosen solutions meet the required objectives.

* **Proactive**
  Anticipate potential limitations in standard models and propose improved alternatives through variants.

* **Collaborative**
  Discuss and validate modeling choices with peers to enhance the robustness of the solution.

* **Creative**
  Combine formal knowledge and contextual insight to construct alternative models that are efficient and innovative.



### C.5 Knowledge-Skill Pairing

This step maps **knowledge areas to the corresponding skills** required to successfully demonstrate competency in this task.

**C.5.1 Mapping Knowledge to Skills**
To demonstrate this competency, students must show the ability to:

* **Apply** Analytical and Critical Thinking to examine system requirements and determine whether standard or variant Turing Machines are more appropriate.

* **Use** Turing Machine Variants to model and optimize computational solutions in scenarios where standard machines are insufficient.

* **Understand** the Church-Turing Thesis to conceptually justify the use of formal computation models in real-world problem-solving.



**C.5.2 Bloom’s Taxonomy Alignment**

* *Apply* level is used to assess the student's ability to analyze requirements and choose the appropriate Turing Machine model accordingly.

* *Understand* level is used to evaluate the student’s comprehension of the Church-Turing Thesis and their ability to justify solution feasibility based on it.



**C.5.3 Verb Annotation**
To provide clarity on competency expectations, the following verb annotations define the required actions:

* **Apply** → Analytical and Critical Thinking → *Evaluate, Decide, Select*
* **Apply** → Turing Machine  → *Use, Adapt, Implement*
* **Understand** → Church-Turing Thesis → *Explain, Justify, Interpret*



### C.6 Summary Table for Competency B

| **Competency**                          | **Dispositions**                                               | **Knowledge**                          | **Skill**                            |
| --------------------------------------- | -------------------------------------------------------------- | -------------------------------------- | ------------------------------------ |
| **Make Use of Turing Machine Variants** | Inventive, Responsible, Proactive, Collaborative, Creative | Turing Machines                | **Apply (Use, Adapt, Implement)**    |
|                                         |                                                                | Church-Turing Thesis                   | **Understand (Explain, Justify)**    |
|                                         |                                                                | Analytical and Critical Thinking (FPK) | **Apply (Evaluate, Decide, Select)** |




### 4.4 Competency D Specification

### D.1 Competency Title

  Test Turing Machines Using Simulators

### D.2 Competency Description

This competency involves the ability to simulate and assess the behavior of **Turing Machines** using dedicated computational tools such as **JFLAP** or equivalent simulators. It ensures that students can validate Turing Machine models by checking their correctness, completeness, and adherence to formal problem specifications.

This competency requires learners to demonstrate the ability to:

* **Effectively utilize simulation tools** to execute and test Turing Machine configurations and transitions.
* **Interpret and evaluate Turing Machine behavior** by comparing simulation results with expected outputs derived from formal definitions.
* **Diagnose design errors and inconsistencies**, iteratively refining machine configurations through systematic testing.
* **Apply analytical and structured problem-solving strategies** to enhance the performance and correctness of Turing Machine implementations.



### D.3 Knowledge Specification

The following knowledge areas are fundamental for achieving this competency:

* **Turing Machines**

  * Understanding the formal structure and execution model of Turing Machines.
  * Utilizing simulation tools to test state transitions, tape movements, and halting conditions.

* **Problem Solving and Troubleshooting (FPK)**

  * Critical for identifying design flaws, unexpected behaviors, or infinite loops during simulation.
  * Enables students to debug and optimize Turing Machine behavior systematically.



### D.4 Disposition Specification

Consistent with previous competencies, this one also demands the demonstration of key behavioral dispositions that support effective simulation and debugging of Turing Machines:

* **Collaboration** – Fosters group work in analyzing complex machine behaviors and co-developing correction strategies.
* **Responsibility** – Emphasizes systematic testing, traceability of errors, and accountability in model refinement.
* **Proactivity** – Encourages initiative in identifying hidden flaws and improving machine logic.
* **Creativity** – Supports innovative approaches to designing and troubleshooting machine configurations and transition functions.



### D.5 Knowledge-Skill Pairing

**D.5.1 Mapping Knowledge to Skills**
To fulfill this competency, students must be able to:

* **Apply** knowledge of Turing Machines to **simulate, evaluate, and verify machine execution**.
* **Apply** Problem Solving and Troubleshooting (FPK) to **diagnose, debug, and refine Turing Machine configurations**.

**D.5.2 Bloom’s Taxonomy Alignment**
This competency aligns with **Bloom’s Revised Taxonomy** at the **Apply** level, where students operationalize theoretical understanding through practical execution and analysis.

* Students must **apply** their understanding of **Turing Machines** by constructing, simulating, and analyzing machine behavior using formal inputs and observing outputs and halting conditions.
* They must also **apply** **Problem Solving and Troubleshooting (FPK)** skills to locate errors in transition functions or logic, revise configurations, and ensure that machines terminate with correct results.

These activities foster higher-order thinking and develop practical competencies aligned with algorithmic reasoning and formal methods.

**D.5.3 Verb Annotation**
To clarify learning expectations, the following verb annotations highlight key actions:

* **Apply** Turing Machines → **Simulate, Evaluate, Verify** machine behavior.
* **Apply** Problem Solving and Troubleshooting → **Diagnose, Debug, Refine** machine logic.



### **D.6 Summary Table for Competency D**

| **Competency**                               | **Dispositions**                                    | **Knowledge**                                 | **Skill**                              |
| -------------------------------------------- | --------------------------------------------------- | --------------------------------------------- | -------------------------------------- |
| **Testing Turing Machines Using Simulators** | **Collaborative, Responsible, Proactive, Creative** | Turing Machines                           | **Apply (Simulate, Evaluate, Verify)** |
|                                              |                                                     | Problem Solving and Troubleshooting (FPK) | **Apply (Diagnose, Debug, Refine)**    |
|         |                                 | Modeling and Simulation | **Apply** |


---


## Table of Competencies for Task: *Traffic Control*

| **Competency**                                     | **Dispositions**                                               | **Knowledge**                          | **Skill**                                          |
|----------------------------------------------------|----------------------------------------------------------------|----------------------------------------|----------------------------------------------------|
| **Develop Problem-Solving Solutions Using Turing Machines** | Collaborative, Responsible, Proactive, Creative, Inventive | Turing Machines                        | **Apply (Use, Implement, Execute)**                |
|                                                    |                                                                | Requirements Analysis                  | **Apply (Interpret, Organize)**                    |
|                                                    |                                                                | Analytical and Critical Thinking | **Apply (Decompose, Identify)**                    |
|                                                    |                                                                |                                        |                                                    |
| **Identify Turing Machine Variants**               | Investigative, Collaborative, Responsible, Proactive           | Turing Machines                 | **Understand (Differentiate, Recognize, Explain)** |
|                                                    |                                                                | Church-Turing Thesis                   | **Understand (Interpret, Justify)**                |
|                                                    |                                                                | Analytical and Critical Thinking  | **Apply (Evaluate, Decide, Justify)**              |
|                                                    |                                                                |                                        |                                                    |
| **Make Use of Turing Machine Variants**            | Inventive, Responsible, Proactive, Collaborative, Creative     | Turing Machines                 | **Apply (Use, Adapt, Implement)**                  |
|                                                    |                                                                | Church-Turing Thesis                   | **Understand (Explain, Justify)**                  |
|                                                    |                                                                | Analytical and Critical Thinking | **Apply (Evaluate, Decide, Select)**               |
|                                        |                                                    |
| **Testing Turing Machines Using Simulators** | Collaborative, Responsible, Proactive, Creative | Turing Machines                           | **Apply (Simulate, Evaluate, Verify)** |
|                                              |                                                     | Problem Solving and Troubleshooting | **Apply (Diagnose, Debug, Refine)**    |
|         |                                 | Modeling and Simulation | **Apply** |
|  |  |                                        |       | 
| *Collaborative Technical Report Writing (REUSED)* | Collaborative, Meticulous, Responsible | Written Communication (FPK) | Apply (Write, Structure, Revise, Refine) |



## Conclusion

The application of the Competency Specification Process (CSP) to Task 2 illustrates how competencies can be systematically derived, structured, and contextualized to bridge the gap between theoretical knowledge and practical problem-solving in computing education. The competencies defined in this report provide a foundation for a competency-based learning model that promotes not only conceptual understanding and technical proficiency, but also the development of essential skills such as simulation, modeling, analytical reasoning, and collaborative reporting.

By aligning learning objectives with real-world tasks, the CSP fosters meaningful and transferable learning experiences, equipping students with the competencies needed to tackle authentic challenges in the field of computer science.
