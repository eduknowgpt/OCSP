# Problem 3: Parking Control

**Authors**: Lais Salvador, Edeyson A. Gomes, Luiz Gavaza
**Date**: May 11, 2022

---

## 1. Problem

The company **EstaciONE**, which owns a large parking lot in Salvador, faces challenges in efficiently managing its parking spots, which are divided among **daily users, monthly subscribers, and rotating customers**. Each spot is exclusively reserved for a specific category, so a customer can only park if there is an available spot in their corresponding category.

The problem arises due to high demand and limited parking spots, resulting in:

* **Parking requests being denied** when there are no available spots in the requested category.
* The need to record and analyze **denied requests by category** to adjust capacity or plan for future expansions.

The parking lot's behavior is dynamic throughout the day, with vehicles **entering and leaving continuously**, thus occupying and freeing up spots. A critical requirement is that when a customer's parking request is denied due to lack of space, the system must ensure that this event **does not interfere with the service of subsequent clients**.

Therefore, **EstaciONE** needs an automated system that can:

1. Track the occupancy of parking spots by category.
2. Monitor and count denied requests per category.
3. Ensure the service process remains efficient and fair.

One of the company’s partners, a Computing student at UFBA, brought this real-world problem to be worked on with their classmates in the **Formal Languages and Computation Theory** course. The group aims to design an **initial solution** for parking management based on theoretical models and machines studied in class.

The analysis and presentation of the solution must reflect not only its practical implementation but also its theoretical foundation, connecting the real-world issue to the concepts of **Formal Languages and Computation Theory**.

The suggested tool for simulating the parking control system is [JFLAP](http://www.jflap.org).

---

## 2. Deliverables

You must upload the following to UFBA Moodle by **11:59 PM on 06/06/2022**, in the designated space:

1. A file containing a machine model that solves the problem.
2. **A report in SBC (Brazilian Computer Society) article format**, describing in detail the design and functioning of the parking control system, with support for identifying the number of denied requests per category each day. The report should also include a justification for the choice of the machine model used.

---

## 3. Schedule

| **Date** | **Tutorial Session**           |
| -------- | ------------------------------ |
| 11/05    | Tutorial Session 1 – Problem 3 |
| 18/05    | Tutorial Session 2 – Problem 3 |
| 25/05    | Tutorial Session 3 – Problem 3 |
| 01/06    | Tutorial Session 4 – Problem 3 |
| 06/06    | Solution Submission            |

---

## 4. Learning Resources

* **RAMOS, M. V. M.; JOSÉ NETO, J.; VEGA, I. S.**
  *Linguagens Formais: Teoria, Modelagem e Implementação*. Bookman, 2009.

* **MENEZES, Paulo Blauth.**
  *Linguagens Formais e Autômatos*, 6th ed. Bookman, 2011.

* **VIEIRA, Newton José.**
  *Linguagens e Máquinas: Uma Introdução aos Fundamentos da Computação*, 2004.

---

## 5. Concepts Involved

1. Turing Machines
2. Church-Turing Thesis
3. Turing Machine Variants
4. Chomsky Hierarchy

---

## 6. Learning Objectives

### 6.1 General Objective

Develop skills to model, implement, and justify computational control systems using concepts from Turing Machines and Formal Languages, linking theoretical foundations with practical applications.

### 6.2 Specific Objectives

1. Identify and justify computational problems solvable with Turing Machines, relating their structure and functioning to parking space management.
2. Relate the parking control problem to the languages and models within the Chomsky Hierarchy.
3. Design a Turing Machine or appropriate variant to manage parking occupancy, considering categories and constraints.
4. Implement the model in JFLAP to simulate the system's behavior.
5. Justify the choice of computational machine model (e.g., Turing Machine or variant) based on the problem's characteristics.
6. Propose a solution that counts and monitors the number of denied requests per category to support future business decisions.
7. Write a technical report in SBC format detailing the proposed solution.
8. Include concrete examples and theoretical justifications in the report to demonstrate the system's effectiveness.
9. Use the Problem-Based Learning (PBL) approach to organize teamwork and document project progress.
10. Connect theoretical foundations of Computation Theory with real-world applications.
11. Use JFLAP to validate and simulate the system’s behavior, ensuring it meets the company’s specified requirements.


