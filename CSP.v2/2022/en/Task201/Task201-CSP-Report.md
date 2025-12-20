# Competency Specification Report: Task201 - Surveillance Drone Prototype

**Team Members**: Lais Salvador, Edeyson A. Gomes, Luiz Gavaza
**Date**: March 21, 2022


## Introduction

Building on the foundational principles of the **Competency Specification Process (CSP)**, this report documents the application of the **Competency Authoring phase** to **Task201 – Surveillance Drone Prototype**. This task is situated in a **Problem-Based Learning (PBL)** context and challenges learners to address a realistic surveillance scenario through the **formal modeling of system behavior using Finite State Machines (FSMs)**.

Within the scope of this activity, FSMs are employed to represent the **logical and reactive aspects** of the drone’s surveillance behavior—such as event detection, state transitions, and data transmission—rather than low-level physical control or continuous dynamics. This deliberate abstraction ensures conceptual coherence between the problem context and the chosen formalism.

By grounding competency specification in an authentic, constraint-driven scenario, Task201 provides a concrete setting for examining how competencies related to **formal modeling, justification of computational models, simulation, and technical documentation** can be explicitly articulated, reused, and aligned with observable learning outcomes. The report thus illustrates both the practical application of the CSP and the methodological refinements that emerge from its iterative use in complex instructional contexts.



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

* **Novice**:  
  Produces a partial FSM that captures only a subset of the required surveillance events; limited state coverage and incomplete handling of transitions or edge cases.

* **Competent**:  
  Develops a complete and coherent FSM that models all specified environmental events; successfully simulates and validates system behavior across representative scenarios.

* **Advanced**:  
  Presents an optimized FSM with justified state and transition minimization; articulates abstraction strategies or general rules (e.g., estimating FSM size based on monitored events) and provides a clear, well-structured technical justification.





## 2. Knowledge Enumeration

To address the task effectively, students are expected to mobilize the following **task-relevant knowledge areas**, directly supporting the modeling, analysis, and validation activities required by the surveillance module:

* **Finite State Machines (FSMs)**:  
  Understanding states, transitions, determinism, and behavioral abstraction, as well as the use of simulation tools such as **JFLAP** to validate state-based models.

* **Regular Languages**:  
  Comprehending the class of languages recognizable by FSMs and their role in characterizing admissible sequences of events and system behaviors.

* **Regular Expressions**:  
  Employing symbolic representations to describe event patterns and transition conditions that can be mapped to FSM structures.

These knowledge components are mobilized to **formally model the surveillance behavior**, **validate system logic through simulation**, and **reason about structural properties** of the FSM—such as estimating or justifying the number of states and transitions required as a function of the monitored events.

Concepts related to broader classifications of formal languages (e.g., higher levels of the Chomsky hierarchy) are considered **background theoretical knowledge** and are not directly required for task execution or performance evaluation.



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

To address the learning objectives of **Task201**, the following competencies were **reused from the reference competency set**. Their selection reflects a deliberate alignment between the task’s formal modeling requirements, expected artifacts, and the observable actions performed by learners.

- **C06 – Develop problem solutions using Finite State Machines**  
  *Justification:* Task201 requires learners to design and validate a surveillance module whose behavior is formally modeled using **Finite State Machines (FSMs)**. Students must analyze system requirements and construct an FSM that represents environmental event detection, state transitions, and data transmission logic. This competency directly supports the development of **logically consistent, verifiable, and formally grounded solutions**, aligning with key task deliverables such as FSM simulation, structural reasoning, and justification of modeling choices.

- **C02 – Justify the use of Deterministic Finite Automata (DFAs)**  
  *Justification:* The task implicitly requires learners to reason about the **appropriateness of deterministic state-based models** for representing reactive surveillance behavior. This involves comparing alternative automaton models (e.g., DFA vs. NFA), understanding trade-offs, and justifying the selection of a DFA as a suitable abstraction for the problem context.

- **C03 – Test Automata Using Simulators**  
  *Justification:* Simulation and validation of the FSM using **JFLAP** are explicit task requirements. This competency supports the systematic testing of formal models, enabling learners to verify correctness, identify inconsistencies, and iteratively refine state transitions based on observed behavior.

- **C04 – Define Regular Expressions for Finite Automata**  
  *Justification:* Although the task does not explicitly require the construction of regular expressions, learners are expected to reason symbolically about **event patterns and transition structures**. This competency supports the analytical abstraction of system behavior and underpins the derivation of rules or formulas relating FSM structure to the number of monitored events.

- **C05 – Write a Technical Report**  
  *Justification:* The production of a structured technical report in **SBC format** is a core deliverable. This competency addresses the ability to document formal models, simulation results, assumptions, and design justifications in a clear, coherent, and professional manner.

- **C11 – Identify Patterns in Finite State Machines**  
  *Justification:* Estimating the minimum number of states and transitions required by the surveillance module demands the identification of **structural patterns and regularities** in FSM design. This competency supports abstraction, optimization, and generalization from specific models to broader rules or design principles.


### Professional Dispositions (Non-Evaluative)

In addition to the technical competencies explicitly targeted by Task201, the activity implicitly fosters a set of **professional dispositions** that are relevant to the problem context and to computing practice more broadly. These dispositions are not directly assessed as standalone outcomes; rather, they emerge naturally from engagement with the task and support effective competency development.

In particular, Task201 encourages learners to demonstrate:

* **Analytical responsibility**, by carefully interpreting problem constraints and selecting appropriate levels of abstraction when modeling complex real-world scenarios using formal methods.
* **Attention to correctness and rigor**, reflected in the systematic validation of FSM models and the justification of design decisions based on formal reasoning rather than ad hoc solutions.
* **Context awareness**, as students must consider environmental, operational, and budgetary constraints when proposing and documenting surveillance solutions.
* **Technical communication awareness**, manifested in the clear and structured documentation of assumptions, models, and results for an external stakeholder (*SOS Florestal*).

These dispositions complement the specified knowledge and skills by reinforcing professional attitudes aligned with formal modeling, problem-based learning, and responsible system design, without introducing additional evaluative requirements into the CSP framework.
