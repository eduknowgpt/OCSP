# Competency Specification Report: Task201 – Surveillance Drone Prototype

**Team Members**: Lais Salvador, Edeyson A. Gomes, Luiz Gavaza  
**Date**: March 21, 2022


## Introduction

Building upon the methodological foundations established in earlier applications of the **Competency Specification Process (CSP)**, this report documents the application of the **Competency Authoring phase** to **Task201 – Surveillance Drone Prototype**. Differently from previous tasks, whose primary objective involved the identification and refinement of competencies emerging from instructional analysis, Task201 is situated at a later stage in the CSP lifecycle, in which the process is applied to an already established competency set. The task therefore serves not only as an instructional specification exercise, but also as an opportunity to examine the **reuse and contextual activation of previously defined competencies** within a new instructional scenario.

The task is situated in a **Problem-Based Learning (PBL)** context and challenges learners to address a realistic surveillance scenario through the **formal modeling of system behavior using Finite State Machines (FSMs)**. Within the scope of this activity, FSMs are employed to represent the **logical and reactive aspects** of the drone’s surveillance behavior—such as event detection, state transitions, and data transmission—rather than low-level physical control or continuous dynamics. This deliberate abstraction ensures conceptual coherence between the problem context and the chosen computational formalism, aligning the expected learner actions with the representational capabilities of the model.

From a methodological perspective, Task201 represents an important transition in CSP application. Competencies are treated as **stable semantic entities**, previously defined and validated through earlier CSP iterations, while their enactment is analyzed in relation to task-specific goals, constraints, and evidence of performance. This orientation allows the CSP to be exercised under conditions of controlled reuse, making it possible to evaluate whether competencies preserve semantic coherence when mobilized across distinct instructional contexts.

By grounding competency specification in an authentic and constraint-driven scenario, Task201 provides a concrete setting for examining how competencies related to **formal modeling, justification of computational models, simulation, and technical documentation** can be explicitly reused, contextualized, and aligned with observable learning outcomes. In doing so, the report illustrates not only the practical application of the CSP in a mature stage of its evolution, but also how iterative application and expert review contribute to methodological stabilization and to the emergence of requirements later formalized within the OntoKSD ontology.



## 1. Instructional Entity Analysis

### Title

  SOS Florestal Drone Surveillance Module


### Description

Learners are tasked with designing a **drone-based surveillance module** to support forest monitoring activities in a realistic and constraint-driven context. The module is required to detect and report environmental events—such as **deforestation**, **river siltation**, and **forest fires**—based on inputs from **optical**, **thermal**, and **GPS-based positional sensors**.

For the purposes of this task, the surveillance module is explicitly framed as a **logical and reactive system**, whose behavior can be formally represented through **discrete states and transitions**. This abstraction enables the use of **Finite State Machines (FSMs)** to model how the system responds to environmental events, manages state changes, and triggers data transmission, without addressing low-level physical control or continuous dynamics.

The system must support the **real-time transmission of photos and videos**, enriched with relevant **geolocation and sensor metadata**, allowing timely identification and assessment of critical situations in remote forest areas. All design decisions are made under explicit **budgetary and technical constraints**, as defined by the commissioning organization *SOS Florestal*. These constraints encourage reasoned trade-offs and highlight the importance of **formal modeling, justified architectural choices, and systematic technical documentation**, which are central to the competency-oriented approach adopted in this task.




### Solution Development Process

Students are expected to engage in a structured solution development process that emphasizes **formal modeling**, **systematic validation**, and **technical justification**. Specifically, they should:

* **Analyze sensor input structures** and explicitly define criteria for detecting relevant environmental events (e.g., deforestation, fire, siltation), identifying which inputs trigger state changes in the system.
* **Model the surveillance behavior using a Finite State Machine (FSM)**, specifying discrete states and transitions that represent event detection, data transmission, and control actions in response to environmental triggers.
* **Simulate and validate the FSM** using **JFLAP** or equivalent tools, ensuring that the modeled behavior is logically consistent, complete with respect to the specified events, and robust across representative input scenarios.
* **Design the system logic for data capture and transmission**, incorporating geolocation and sensor metadata into the transmitted artifacts (e.g., photos, videos, logs), in alignment with the modeled FSM behavior.
* **Produce a structured technical report** that documents the FSM design, event-detection rules, simulation results, and transmission specifications, providing clear justification for modeling and design decisions.
* **Optionally explore optimization strategies**, such as state minimization, power-efficient operation, or modular integration with existing drone control software, demonstrating the ability to abstract, generalize, and refine formal models under practical constraints.




### Expected Outcomes

Upon completion of the task, students must submit the following artifacts, which collectively provide evidence of competency acquisition through observable and verifiable outcomes:

* A **JFLAP FSM file** that formally models the surveillance behavior of the system, including states, transitions, and event-triggered responses.
* **Sample output artifacts** (e.g., simulated logs, message traces, or data packets) corresponding to each monitored environmental event, demonstrating correct system behavior under representative scenarios.
* A **technical report**, structured according to the SBC format, that documents and justifies the proposed solution. The report must include:
  * A clear description of the **FSM structure**, including states, transitions, and their semantic interpretation.
  * The **criteria adopted for environmental event detection** and their relation to sensor inputs.
  * The **data transmission model**, detailing the structure of transmitted information and associated metadata.
  * A **justification of design and modeling decisions**, including assumptions, constraints, and trade-offs considered during implementation.




### Acquisition Context

* **Environment**: Computer Science laboratory equipped with **JFLAP** and complementary tools for **Finite State Machine (FSM) modeling and simulation**.
* **Application**: Suitable for courses addressing **automata theory**, **formal methods**, **introductory system modeling**, or **computational aspects of environmental monitoring**, where abstract behavioral modeling is emphasized over physical implementation.



### Target Audience Profile

* **Academic Level**: 2nd–3rd year undergraduate Computer Science students.
* **Domain Experience**: Solid background in programming fundamentals, data structures, and introductory automata concepts; limited or no prior experience with hardware integration or complex cyber-physical systems.
* **Expected Roles**:
  * Design and formalize FSMs representing surveillance and monitoring behavior.
  * Simulate and debug state-based models using appropriate tools.
  * Analyze system behavior under different event scenarios.
  * Document modeling choices, assumptions, and formal justifications in a technical report.



### Proficiency Scale

The proficiency scale reflects increasing levels of competency enactment in terms of modeling completeness, correctness, and conceptual justification. Progression across levels corresponds to observable differences in the learner’s ability to construct, validate, and justify formal computational models.

* **Novice**:  
  Produces a partial FSM that captures only a subset of the required surveillance events. The model exhibits limited state coverage, incomplete transition handling, or inconsistent responses to edge cases. Demonstrates emerging understanding of state-based modeling but requires guidance to ensure completeness and correctness.

* **Competent**:  
  Develops a complete and coherent FSM that represents all specified environmental events and system reactions. Correctly defines states and transitions, and successfully simulates and validates system behavior across representative scenarios. Demonstrates the ability to apply FSM concepts consistently to satisfy task requirements.

* **Advanced**:  
  Produces an optimized FSM supported by explicit justification of modeling decisions, including state or transition minimization and abstraction strategies. Demonstrates analytical reasoning about model structure (e.g., generalizing rules for estimating FSM size based on monitored events) and communicates design decisions through clear, structured technical justification.






## 2. Knowledge Enumeration

To address the task effectively, students are expected to mobilize a set of **task-relevant knowledge elements** that directly support the modeling, analysis, and validation activities required by the surveillance module. In accordance with the refined CSP guidelines, knowledge enumeration is oriented by **competency enactment requirements**, rather than by exhaustive coverage of the theoretical domain. Consequently, only knowledge elements that are operationally mobilized through observable learner actions are included as part of the competency specification.

The following knowledge areas are therefore considered essential for task execution:

* **Finite State Machines (FSMs)**:  
  Understanding states, transitions, determinism, and behavioral abstraction, as well as the use of simulation tools such as **JFLAP** to validate state-based models. This knowledge supports the construction, simulation, and justification of formal behavioral models.

* **Regular Languages**:  
  Understanding the class of languages recognizable by FSMs and their role in characterizing admissible sequences of events and system behaviors. This knowledge enables learners to reason about the expressive limits and correctness of the proposed model.

* **Regular Expressions**:  
  Employing symbolic representations to describe event patterns and transition conditions that can be mapped to FSM structures, supporting abstraction and systematic model construction.

These knowledge components are mobilized to **formally model surveillance behavior**, **validate system logic through simulation**, and **reason about structural properties** of the FSM, including the estimation and justification of the number of states and transitions required as a function of monitored events.

Concepts related to broader classifications of formal languages (e.g., higher levels of the Chomsky hierarchy) are treated as **background theoretical knowledge**. Although pedagogically relevant within the broader domain of Formal Languages and Automata Theory, such concepts are not directly mobilized in task execution nor used as evaluation criteria. Their explicit exclusion reflects a methodological refinement introduced in later CSP iterations, in which competency scope is delimited by observable enactment rather than theoretical completeness.

From an ontological perspective, this distinction supports the separation between knowledge elements that participate in competency activation and those that remain contextual or explanatory, reinforcing the OntoKSD principle that knowledge enumeration should reflect operational relevance within instructional contexts.




## 3. Learning Objectives and Expected Outcomes

### General Objective

Develop and consolidate the ability to **formally model, validate, and document computational systems** grounded in formal language theory—particularly **Finite State Machines (FSMs)**—by applying these concepts to the resolution of a realistic, context-driven problem.

### Specific Learning Objectives

* **Model surveillance behavior using Finite State Machines (FSMs)**, representing environmental event detection, state transitions, and control or transmission actions of the drone in a formally consistent manner.

* **Simulate and validate FSM models** using tools such as **JFLAP**, demonstrating correct and complete system behavior across representative input scenarios (e.g., event detection, repositioning commands, transmission triggers).

* **Express behavioral rules and event patterns** through concepts from **Regular Languages and Regular Expressions**, relating symbolic representations to corresponding FSM transitions and structures.

* **Derive and justify a rule or formula** for estimating the **minimum number of states and transitions** required in the FSM as a function of the number and type of monitored events (e.g., deforestation, fire, siltation).

* **Produce a structured technical report**, following the **SBC format**, that documents the formal modeling process, simulation results, and analytical justifications for design decisions, assumptions, and trade-offs considered during system development.




## 4. Competency Definition

### Reusability Note

In accordance with the refined principles of the **Competency Specification Process (CSP)**, Task201 does not introduce new competencies. Instead, it deliberately reuses competencies previously defined in the reference competency set. This decision reflects the methodological assumption that competencies represent **stable and reusable capabilities**, whose applicability is determined by their contextual activation within specific instructional entities rather than by task-specific redefinition.

The selection of competencies is therefore guided by the alignment between (i) the formal modeling requirements of the task, (ii) the expected learner-produced artifacts, and (iii) the observable actions through which competency enactment can be evidenced. In this context, competency reuse preserves conceptual identity while allowing variation in activation mode, instructional role, and evidence type, in accordance with the CSP maturation established in previous tasks.

The following competencies are activated in Task201:


- **C06 – Develop problem solutions using Finite State Machines**  

  *Justification:* Task201 requires learners to design and validate a surveillance module whose behavior is formally modeled using **Finite State Machines (FSMs)**. Students must analyze system requirements and construct an FSM representing environmental event detection, state transitions, and data transmission logic. This competency supports the development of logically consistent and verifiable formal models, directly aligning with task deliverables such as FSM construction, simulation, structural reasoning, and justification of modeling decisions. In this task, C06 is activated primarily in a **constructive and analytical mode**, as learners both create and evaluate formal models.


- **C02 – Justify the use of Deterministic Finite Automata (DFAs)**  

  *Justification:* The task requires learners to reason about the suitability of deterministic state-based models for representing reactive surveillance behavior. This involves understanding the implications of determinism, comparing alternative automaton models (e.g., DFA vs. NFA), and justifying the selection of DFA as an appropriate abstraction. The competency is activated in a **justificatory and analytical mode**, emphasizing model adequacy rather than model construction itself.


- **C03 – Test Automata Using Simulators**  

  *Justification:* Simulation and validation of the FSM using **JFLAP** are explicit task requirements. This competency supports systematic testing of formal models, enabling learners to verify correctness, identify inconsistencies, and iteratively refine state transitions based on observed behavior. In this context, C03 is activated in an **artifact-oriented mode**, where simulation results constitute primary evidence of competency enactment.


- **C04 – Define Regular Expressions for Finite Automata**  

  *Justification:* Although the explicit construction of regular expressions is not a mandatory task deliverable, learners are expected to reason symbolically about event patterns and transition conditions. This competency supports abstraction and analytical reasoning about system behavior, enabling learners to relate event structures to FSM representations. Accordingly, C04 operates as a **supporting competency**, contributing to conceptual reasoning rather than serving as a primary learning objective.


- **C05 – Write a Technical Report**  

  *Justification:* The production of a structured technical report in **SBC format** constitutes a core artifact of the task. This competency addresses the ability to document formal models, simulation results, assumptions, and design decisions in a clear, coherent, and professionally structured manner. In Task201, C05 functions as a **transversal competency**, supporting the communication and evaluation of computational work.



- **C11 – Identify Patterns in Finite State Machines**  

  *Justification:* Estimating the number of states and transitions required by the surveillance module demands the identification of structural regularities in FSM design. This competency supports abstraction and generalization from specific models to broader design principles, enabling learners to reason about scalability and structural optimization. Its activation occurs primarily in an **analytical mode**, supporting higher-level reasoning about model structure.


From a methodological perspective, this competency configuration illustrates the maturation of the CSP toward a **reuse-oriented specification strategy**, in which competencies are not recreated for each task but systematically activated under different instructional conditions. From an ontological perspective, this distinction reinforces the OntoKSD principle that competencies remain stable entities, while their contextual enactment—including activation mode, instructional role, constraints, and evidence—is modeled at the relational level between competence and instructional entity.



