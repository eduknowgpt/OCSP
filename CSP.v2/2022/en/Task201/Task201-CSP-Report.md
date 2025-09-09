# Competency Specification Report: Task201 - Surveillance Drone Prototype

**Team Members**: Lais Salvador, Edeyson A. Gomes, Luiz Gavaza
**Date**: March 21, 2022

## Introduction

Building on the foundational CSP methodology, this report presents the application of the **Competency Authoring phase** in **Task201 - Surveillance Drone Prototype**.


## 1. Instructional Entity Analysis

### Title

* **SOS Florestal Drone Surveillance Module**

### Description

Learners are challenged to design a **drone-based surveillance module** that supports forest monitoring activities. The module must be capable of detecting and reporting environmental events such as **deforestation**, **river siltation**, and **forest fires**, using input from **optical**, **thermal**, and **GPS-based positional sensors**.

The system should transmit **photos and videos in real time**, enriched with **location and sensor data**, enabling accurate and timely identification of critical situations in remote forest areas. This prototype is commissioned under **budget and technical constraints** by the organization *SOS Florestal*.



### Solution Development Process

Students are expected to:

* Analyze sensor input structures and define event detection criteria
* Model the surveillance behavior using a **Finite State Machine (FSM)**, defining states and transitions linked to environmental triggers
* Simulate and validate the FSM using **JFLAP** or other appropriate tools
* Design the system logic for **data capture and transmission**, incorporating environmental metadata
* Produce a **technical report** outlining the FSM logic, event-detection rules, and transmission specifications
* Optionally explore optimizations for power-efficient operation and modular integration with existing drone control software



### Expected Outcomes

Students must submit:

* A **JFLAP FSM file** that models surveillance behavior
* Sample output files (e.g., simulated logs or data packets) for each environmental event
* A **technical report** detailing:

  * FSM states and transition logic
  * Criteria used for event detection
  * Data transmission structure and metadata formats
  * Justification of design decisions and implementation strategy



### Acquisition Context

* **Environment**: CS laboratory equipped with JFLAP and tools for FSM simulation
* **Application**: Appropriate for courses on **automata theory**, **embedded systems**, or **environmental monitoring technologies**


### Target Audience Profile

- Academic Level: 2nd–3rd year undergraduate CS students.

- Domain Experience: Solid grounding in programming, data structures, and basic automata; minimal experience in hardware or complex system modeling.

- Roles: Design FSMs covering payment, change calculation, and product dispensing; debug and simulate behavior; document technical decisions.


### Proficiency Scale

- **Novice**: 	Partial FSM representation; handles limited scenarios; lacks handling of edge cases (grade range <= 5>).
- **Competent**:	Complete FSM that covers all payment and change scenarios; simulated and validated correctly (grade range > 5 and <= 9).
- **Advanced**:	Includes stochastic bonus implementation; clearly justified in logic; detailed technical explanation provided (grade range > 9).





## 2. Knowledge Enumeration

To solve the problem effectively, the following core knowledge areas are required:

* **Finite State Machines**: Understanding states, transitions, determinism, and simulation in tools like JFLAP.
* **Regular Languages**: Grasping the class of languages recognizable by FSMs.
* **Regular Expressions**: Using concise notation to describe language patterns that can be accepted by FSMs.

* **Chomsky Hierarchy**: Positioning FSMs and regular languages in the broader hierarchy of language classes.

This knowledge will be mobilized to model the system's behavior, validate it using simulation tools, and evaluate the feasibility of minimizing the number of states and transitions based on the number of monitored events.


## 3. Learning Objectives and Expected Outcomes

### General Objective

Develop and consolidate the ability to model, implement, and document computational systems grounded in formal language theory—particularly Finite State Machines—through the resolution of real-world problems.

### Specific Learning Objectives

* Model the system’s behavior using Finite State Machines (FSMs) to represent event monitoring, transmission, and control actions of the drone.

* Simulate and validate the FSM using tools such as JFLAP, demonstrating correct operation and consistent handling of input scenarios (e.g., zoom level changes, new coordinates, transmission triggers).

* Apply the concept of Regular Languages and Regular Expressions to express behavior rules and transitions within the FSM.

* Design a rule or formula that estimates the minimum number of states and transitions in the FSM, based on the number of monitored events (e.g., deforestation, fire, siltation).

* Produce a technical report in SBC format that documents the design rationale, formal modeling process, simulation results, and mathematical justifications for decisions (e.g., budget estimations, modeling choices).



## 4. Competency Definition


### Reusability Note

To address the learning objectives of Task201, we reused the following competencies:

- **C06 - Develop problem solutions using Finite Finite State Machines**  
  *Justification:* Task201 requires the development of a real-world prototype that models the surveillance behavior of a drone using Finite State Machines (FSMs). Students must analyze system requirements and construct a formal FSM that represents event detection, control actions, and data transmission. This competence directly supports the ability to design, implement, and validate FSM-based computational solutions that are logically consistent and verifiable. Its specific focus on FSMs makes it highly aligned with the learning objectives and deliverables of the task, including simulation, rule derivation, and formal justification of state minimization strategies.

- **C02 - Justify the use of Deterministic Finite Automata (DFAs)**  
  *Justification:* The task challenges students to evaluate and justify the suitability of FSMs in representing drone behavior. This involves comparing different automaton models (DFA vs. NFA), understanding trade-offs, and selecting the most appropriate model for a real-world application—core aspects of this competency.

- **C03 - Test Automata Using Simulators**  
  *Justification:* One of the deliverables includes simulated executions of the automaton model using JFLAP. This aligns perfectly with the competency, which emphasizes systematic testing, verification, and iterative refinement of FSMs through simulation tools.

- **C04 - Define Regular Expressions for Finite Automata**  
  *Justification:* The task includes the design of a mathematical expression or formula to estimate states and transitions, which supports abstraction and reasoning about FSM structure. Though not directly requesting a regular expression, this activity aligns with the analytical dimension of mapping behavior to symbolic representations.

- **C05 - Write a Technical Report**  
  *Justification:* Students are required to produce a structured technical report in SBC format that documents system modeling, simulation, and analysis. This aligns with the competency’s focus on effective written communication of technical artifacts.

- **C11 - Identify Patterns in Finite State Machines** 
  *Justification:* The estimation of minimal states and transitions requires identifying patterns or regularities in FSM behavior. This competency supports structural analysis to simplify or optimize models, which is a key step in abstracting general rules from specific models.
