# Problem 4: Online Judges at Logistic Solutions

**Authors**: Lais Salvador, Edeyson A. Gomes, Luiz Gavaza
**Date**: June 8, 2022


## 1. Problem

Several students from the **Institute of Computing at UFBA** are preparing to participate in the **Brazilian Programming Marathon (SBC)** ([http://maratona.sbc.org.br](http://maratona.sbc.org.br)). In this competition, teams submit source code to solve problems, using evaluation systems known as **Online Judges (OJ)**.

An OJ assesses the code by running multiple test cases and returning one of the following results:

1. **AC – Accepted**: Passed all test cases.
2. **WA – Wrong Answer**: Incorrect answer in at least one test case.
3. **TLE – Time Limit Exceeded**: Program exceeded the time limit.
4. **CE – Compilation Error**: Program failed to compile (warnings are not errors).
5. **RE – Runtime Error**: Program crashed due to issues like invalid memory access or division by zero.

During marathon training, student Carlos encountered an interesting OJ problem related to logistics — the **Traveling Salesman Problem (TSP)**. He shared it with his startup team at **Logistic Solutions**, who began submitting code for it. After correcting compilation and runtime errors (CE and RE) and eliminating wrong answers (WA), all submissions still returned the same result: **TLE**.

Despite the team’s experience, they started to wonder:

* Was it a logic flaw or an inadequate approach?
* What strategies could lead to an **AC** result for the TSP?

Additionally, the startup managers became interested in the OJ's functionality and asked Carlos to investigate:

* Whether the OJ can evaluate other types of problems.
* Whether the OJ can detect if a program will enter an **infinite loop**.

Carlos brought these questions to his teammates in the **Theory of Computation** course. They realized that OJ behavior could be modeled using a **Finite State Machine (FSM)** to:

* Represent transitions between different evaluation outcomes (AC, WA, TLE, etc.).
* Illustrate how the OJ works and explain its logic to both programmers and management.

The main challenge is to:

1. Analyze why the TSP codes return **TLE**, and how to achieve **AC**.
2. Design a **Finite State Machine** that represents the OJ’s logic and explains its limitations, especially the theoretical impossibility of detecting infinite loops.



## 2. Deliverables

The team must submit a **report in SBC article format** containing all analyses and results. Submission is due via **UFBA Moodle** by **11:59 PM on 27/06/2022**. The report must include:

1. **Team discussions about the TSP in the OJ**:

   * Hypotheses regarding the results of the code submissions.
   * Characterization of the TSP: its definition, computational challenges, and possible causes for the TLE results.

2. **Responses to the startup managers**:

   * Detailed answers to the startup’s questions, supported by explanations and demonstrations.
   * Discussion on OJ’s capabilities and limitations, especially regarding detection of infinite loops.

3. **FSM representing OJ behavior**:

   * A model of the OJ using a **Finite State Machine**, including states, transitions, and conditions representing outputs like AC, WA, TLE, etc.
   * Explanation of how the FSM clarifies system operation and constraints.

The report must be clear, well-organized, and connect practical issues to the theoretical concepts from the course.



## 3. Schedule

| **Date** | **Tutorial Session**           |
| -------- | ------------------------------ |
| 08/06    | Tutorial Session 1 – Problem 4 |
| 15/06    | Tutorial Session 2 – Problem 4 |
| 20/06    | Tutorial Session 3 – Problem 4 |
| 27/06    | Tutorial Session 4 – Problem 4 |
| 27/06    | Final Submission               |


## 4. Learning Resources

* **HOPCROFT, J. E.; ULLMAN, J. D.; MOTWANI, R.**
  *Introduction to Automata Theory, Languages, and Computation*. Campus, 2002.

* **SIPSER, M.**
  *Introduction to the Theory of Computation*. Thomson Learning, 2007.

* **VIEIRA, Newton José**
  *Linguagens e Máquinas: Uma Introdução aos Fundamentos da Computação*, 2004.



## 5. Concepts Involved

1. Recursively Enumerable Language
2. Chomsky Hierarchy
3. Halting Problem
4. Universal Turing Machine
5. P, NP, and NP-Complete Problems
6. Finite State Machine



## 6. Learning Objectives

### 6.1 General Objective

Apply core concepts from Computation Theory to model, analyze, and solve practical problems involving Online Judge systems and the computational complexity of real-world challenges like the Traveling Salesman Problem.

### 6.2 Specific Objectives

1. Understand Finite State Machines and their application in automated evaluation systems (OJ).
2. Connect the Traveling Salesman Problem (TSP) to NP-Complete problems and real-world implications.
3. Relate OJ validations and outputs to the Chomsky Hierarchy.
4. Identify theoretical and practical limitations in program evaluation, including loop detection.
5. Model the OJ’s behavior using a Finite State Machine (FSM) with states such as AC, WA, TLE, etc.
6. Use FSMs to explain the OJ's behavior and system limitations.
7. Understand the Halting Problem and its implications for loop detection.
8. Explain how computational theory justifies OJ limitations.
9. Analyze why TSP submissions result in TLE.
10. Use Turing Machine and Recursively Enumerable Language concepts to discuss OJ capabilities.
11. Write a technical report in SBC format, with detailed analysis and theoretical justification.
12. Present concrete examples to demonstrate OJ behavior and TSP challenges.
13. Collaborate using Problem-Based Learning (PBL) methodology to structure problem-solving.
14. Document team progress using tools such as whiteboards and diagrams.
15. Implement and simulate the FSM in JFLAP to validate the model.

## Referências

**KIOTHEKA, Fernando; ALMEIDA, Raul.** *Introdução à Maratona de Programação*. v. 1.7, 2022.  
Disponível em: [https://www.inf.ufpr.br/maratona/livreto](https://www.inf.ufpr.br/maratona/livreto)

