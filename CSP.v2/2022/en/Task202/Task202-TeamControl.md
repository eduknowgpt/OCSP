# Problem 2: Team Control

**Authors**: Lais Salvador, Edeyson A. Gomes, Luiz Gavaza
**Date**: April 12, 2022

---

## 1. Problem

The company *SOS Florestal* was satisfied with the prototypes delivered for the drone monitoring problem. However, a new institutional regulation requires adaptations to the surveillance system to comply with safety regulations for specialized teams dispatched to handle detected issues (such as deforestation, river siltation, and fires).

According to the regulation, each team must be composed of a fixed ratio of volunteers (V) to non-volunteers (NV), depending on the type of event. This ratio is expressed by the formula:
**Vi ≥ ni × NVi**, where **ni > 0** is a factor defined for each event type $i$ (deforestation, river siltation, or fires).

To comply with the regulation, the drone will be equipped with a receiver capable of capturing signals emitted by the team members’ individual signal devices, which transmit:

* Geographical location
* Unique identification
* Volunteer status (V or NV)

Due to the low transmission power of the signal device, the drone must fly over the area to collect the data. If the volunteer-to-non-volunteer ratio in a given area does not meet the regulatory requirement, the drone must issue an alert to the base.

The student team from UFBA, responsible for developing the prototype, analyzed the new requirement and concluded that **a simple finite state machine is not sufficient to solve the problem**. This raises an important question: what factors led them to this conclusion?

In order to meet the team composition regulation, the students realized that for the first prototype of the team control module, it would be necessary to fix the number of volunteers for each non-volunteer, based on the required ratio for each monitored event.

Upon deeper analysis, they identified that including **an auxiliary memory device in the state machine** would enable an adequate modeling of the solution. This addition allows real-time recording and validation of the volunteer/non-volunteer ratio, ensuring compliance with the regulation.

Furthermore, the students noted that the initial surveillance module developed in **Problem 1** could be extended to include team control functionality. Alternatively, the two modules could be implemented as **independent solutions**, operating in parallel but **communicating with each other** to share relevant data.

Lastly, *SOS Florestal* expressed interest in a **formal notation** that would document the rules for generating teams in a clear and structured manner. This notation would be useful for both operational control and future improvements.

The suggested tool to simulate the team control module is [JFLAP](http://www.jflap.org).

---

## 2. Process

To build the solution, the **Problem-Based Learning (PBL)** methodology will be adopted. PBL is known for using real-world problems as a starting point to stimulate the development of essential skills such as critical thinking, teamwork, and problem-solving. This approach significantly contributes to the construction of knowledge around a specific theme.

The documentation of the process will be carried out using a PBL whiteboard, structured in four main columns: **QUESTIONS**, **FACTS**, **IDEAS/HYPOTHESES**, and **ACTIONS**. Each team must complete and update the whiteboard during every meeting, ensuring the documentation of their problem-solving journey. This material will be an important component of group assessment.

Additionally, a shared document will be provided for teams to fill out a **Logbook**, as instructed during the initial synchronous session. The Logbook will serve as a complementary record of activities, decisions, and challenges encountered during development.

This integrated approach ensures not only organization and progress tracking, but also promotes continuous reflection and collaborative learning among participants.

---

## 3. Deliverables

One team member must submit, through the UFBA Virtual Learning Environment (AVA), by **6:00 PM on 05/02/2022**, the following deliverables:

* A **JFLAP file** with the **drone surveillance and team control modules**.
* A **technical report in the SBC (Brazilian Computer Society) article format** describing in detail the design and operation of the modules.

The report must include all system operations and at least two usage examples. Additionally, it should address the company’s expectations regarding documentation and budgeting.

---

## 4. Schedule

| Date  | Tutorial Session               |
| ----- | ------------------------------ |
| 04/13 | Tutorial Session 1 – Problem 2 |
| 04/20 | Tutorial Session 2 – Problem 2 |
| 04/27 | Tutorial Session 3 – Problem 2 |
| 05/04 | Solution Submission            |

---

## 5. Learning Resources

* **RAMOS, M. V. M.; JOSÉ NETO, J.; VEGA, I. S.**
  *Linguagens Formais: Teoria, Modelagem e Implementação*. Bookman, 2009.

* **MENEZES, Paulo Blauth.**
  *Linguagens Formais e Autômatos*, 6th ed. Bookman, 2011.

* **VIEIRA, Newton José.**
  *Linguagens e Máquinas: Uma Introdução aos Fundamentos da Computação*, 2004.

---

## 6. Concepts Involved

1. Finite State Machines
2. Context-Free Languages
3. Context-Free Grammars
4. Pushdown Automata
5. Chomsky Hierarchy

---

## 7. Learning Objectives

### 7.1 General Objectives

1. Develop skills to model, implement, and analyze computational systems using formal language and automata concepts.
2. Apply knowledge of Computation Theory to solve practical problems related to monitoring and operational control in real-world scenarios.

### 7.2 Specific Objectives

1. Recognize computational problems that require memory-based models, such as Pushdown Automata.
2. Design a system using Finite State Machines combined with memory devices to meet specific requirements (e.g., volunteer/non-volunteer ratios).
3. Model and simulate system behavior in JFLAP, ensuring compliance with institutional regulations.
4. Relate machine operation to concepts of Context-Free Languages and Grammars.
5. Determine and justify the minimal number of states, transitions, and rules needed for efficient implementation.
6. Develop a technical report in SBC format, detailing system operations and presenting concrete examples.
7. Simulate and validate system behavior in JFLAP, demonstrating compliance with operational requirements.
8. Work collaboratively to integrate knowledge and propose creative, grounded solutions.
9. Evaluate the limitations of Finite State Machines and discuss how memory devices expand their capabilities.

