# Problem 1: Drone Monitoring

**Authors**: Lais Salvador, Edeyson A. Gomes, Luiz Gavaza
**Date**: March 21, 2022

## 1. Problem

The company *SOS Florestal* is developing a prototype surveillance drone for forest monitoring, aimed at identifying events such as deforestation, river siltation, and forest fires. This drone will be equipped with a state-of-the-art optical module capable of zooming up to 60x, along with infrared and heat detection sensors. During monitoring, it transmits real-time images and videos to its base, allowing data analysis and identification of deforested areas, silted rivers, or fire outbreaks, including early-stage fires.

For each transmission (photo or video), the drone associates additional information gathered from its advanced GPS system, such as geolocation, altitude, speed (to be calculated), barometric data, and estimated ground temperature. There are future plans to include more sensors to expand data collection.

Upon receiving the data, the control base can send commands to reposition the drone to a new coordinate and altitude (within a 5 km range), request new photos with different zoom levels, or videos with specific duration and zoom settings.

When a monitored event is detected, a specialized team is dispatched to assess or resolve the issue. The team size depends on the severity of the event—such as the area of the fire, the extent of deforestation, or the length of the silted section.

A technician from SOS Florestal, who is also a computing student at UFBA, brought this problem to be tackled collaboratively by their classmates, aiming to develop a functional prototype of the drone's surveillance module.

Due to economic constraints, SOS Florestal is seeking a low-cost solution for this initial prototype. During preliminary research, students identified that the problem could be modeled and solved using a finite state machine. This conclusion raised an interesting question: how did they arrive at this solution?

Additionally, the students discovered a simple mathematical expression commonly used in protocols, which could be included in the project documentation. According to them, this expression can be designed once the system is implemented using a finite state machine. The company showed interest in exploring this approach further.

The company is also interested in investigating the feasibility of establishing a rule to determine the minimum number of states and transitions required for the finite state machine based on the number of monitored events. This would help create more accurate budgets and optimize prototype development.

The recommended tool to simulate the drone surveillance module is [JFLAP](http://www.jflap.org).


## 2. Process

To build the solution, the **Problem-Based Learning (PBL)** methodology will be adopted. PBL is known for using real-world problems as a starting point to foster essential skills such as critical thinking, teamwork, and problem-solving. It also contributes significantly to building knowledge around a specific topic.

The process documentation will be done through a PBL whiteboard, structured into four main columns: **QUESTIONS**, **FACTS**, **IDEAS/HYPOTHESES**, and **ACTIONS**. Each team must fill in and update the whiteboard during each meeting, ensuring the documentation of the problem-solving steps. This material will be an important component in group assessment, reflecting progress and collective reasoning.

In addition, a shared document will be provided for teams to maintain a **Logbook**, as instructed during the initial synchronous meeting. The logbook will serve as a complementary record detailing the activities performed, decisions made, and challenges encountered during development.

This integrated approach ensures not only the organization and tracking of progress but also promotes continuous reflection and collaborative learning among participants.



## 3. Deliverables

One team member must upload to the UFBA Virtual Learning Environment (AVA), by **11:59 PM on 04/03/2022**, a **JFLAP file** containing the **drone surveillance module**, along with a **technical report in SBC (Brazilian Computer Society) article format** that details the design and operation of the module.

The report should describe the system's operations and include at least **two examples of system execution**. It should also address the company's interests regarding documentation and budgeting.



## 4. Schedule

| Date  | Tutorial Session             |
| ----- | ---------------------------- |
| 03/24 | Tutorial Session – Problem 1 |
| 03/31 | Tutorial Session – Problem 1 |
| 04/03 | Solution Submission          |



## 5. Learning Resources

* **RAMOS, M. V. M.; JOSÉ NETO, J.; VEGA, I. S.**
  *Linguagens Formais: Teoria, Modelagem e Implementação*. Bookman, 2009.

* **MENEZES, Paulo Blauth.**
  *Linguagens Formais e Autômatos*, 6th ed. Bookman, 2011.



## 6. Concepts Involved

1. Finite State Machines
2. Regular Languages
3. Regular Expressions
4. Chomsky Hierarchy


## 7. Learning Objectives

### 7.1 General Objective

Develop the skills necessary to model, implement, and document computational systems using core concepts from formal languages and computation theory, with a focus on solving real-world problems.

### 7.2 Specific Objectives

1. **Model the system’s behavior using Finite State Machines (FSMs)** to represent event monitoring, transmission, and control actions of the drone.

2. **Simulate and validate the FSM** using tools such as **JFLAP**, demonstrating correct operation and consistent handling of input scenarios (e.g., zoom level changes, new coordinates, transmission triggers).

3. **Apply the concept of Regular Languages and Regular Expressions** to express behavior rules and transitions within the FSM.

4. **Design a rule or formula** that estimates the **minimum number of states and transitions** in the FSM, based on the number of monitored events (e.g., deforestation, fire, siltation).

5. **Produce a technical report** in SBC format that documents the design rationale, formal modeling process, simulation results, and mathematical justifications for decisions (e.g., budget estimations, modeling choices).







