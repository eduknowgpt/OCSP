# Competency Specification Report: Task201 - Surveillance Drone Prototype

**Team Members**: Lais Salvador, Edeyson A. Gomes, Luiz Gavaza
**Date**: March 21, 2022


## 1. Task Description Analysis

The problem scenario presented by SOS Florestal involves the development of a prototype surveillance module for a drone used in forest monitoring. The module must be capable of detecting and reporting deforestation, river siltation, and forest fires using optical, thermal, and positional data. The real-time transmission of photos and videos, enriched with GPS coordinates and sensor readings, enables the system to identify critical events and respond accordingly.

Given the functional requirements and limited budget, students proposed modeling the system behavior using a **Finite State Machine (FSM)**. This approach allows for representing the system's states and transitions triggered by input events, ensuring a deterministic and transparent operation model. The use of FSM also aligns with the learning objectives of the course, enabling students to apply theoretical concepts to a practical, real-world problem.


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

* Interpret the Chomsky Hierarchy to position FSMs within the broader classification of formal languages and justify their suitability for the problem.

* Design a rule or formula that estimates the minimum number of states and transitions in the FSM, based on the number of monitored events (e.g., deforestation, fire, siltation).

* Produce a technical report in SBC format that documents the design rationale, formal modeling process, simulation results, and mathematical justifications for decisions (e.g., budget estimations, modeling choices).


## 4. Competency Definition


### Reusability Note

To address the learning objectives of Task201, we reused the following competencies originally defined for Task01 – *The Vending Machine for Sodas and Snacks*, due to the conceptual and technical similarities between the tasks (e.g., finite automata modeling and simulation):

- **EdukNow_C12 – Develop problem solutions using Finite Finite State Machines**  
  *Justification:* Task201 requires the development of a real-world prototype that models the surveillance behavior of a drone using Finite State Machines (FSMs). Students must analyze system requirements and construct a formal FSM that represents event detection, control actions, and data transmission. This competence directly supports the ability to design, implement, and validate FSM-based computational solutions that are logically consistent and verifiable. Its specific focus on FSMs makes it highly aligned with the learning objectives and deliverables of the task, including simulation, rule derivation, and formal justification of state minimization strategies.

- **EdukNow_C06 – Justify the use of Deterministic Finite Automata (DFAs)**  
  *Justification:* The task challenges students to evaluate and justify the suitability of FSMs in representing drone behavior. This involves comparing different automaton models (DFA vs. NFA), understanding trade-offs, and selecting the most appropriate model for a real-world application—core aspects of this competency.

- **EdukNow_C07 – Test Automata Using Simulators**  
  *Justification:* One of the deliverables includes simulated executions of the automaton model using JFLAP. This aligns perfectly with the competency, which emphasizes systematic testing, verification, and iterative refinement of FSMs through simulation tools.

- **EdukNow_C08 – Define Regular Expressions for Finite Automata**  
  *Justification:* The task includes the design of a mathematical expression or formula to estimate states and transitions, which supports abstraction and reasoning about FSM structure. Though not directly requesting a regular expression, this activity aligns with the analytical dimension of mapping behavior to symbolic representations.

- **EdukNow_C04 – Write a Technical Report**  
  *Justification:* Students are required to produce a structured technical report in SBC format that documents system modeling, simulation, and analysis. This aligns with the competency’s focus on effective written communication of technical artifacts.

- **EdukNow_C13 – Identify Patterns in Finite State Machines** 
  *Justification:* The estimation of minimal states and transitions requires identifying patterns or regularities in FSM behavior. This competency supports structural analysis to simplify or optimize models, which is a key step in abstracting general rules from specific models.
