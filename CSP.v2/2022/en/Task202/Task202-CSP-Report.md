# Competency Specification Report: Task202 - Team Control

* **Authors:** Luiz Gavaza, Daniel Cason, Lais Salvador, Roberta Oliveira
* **Contributors:** Jéssica Santana, Otávio Neto, Edeyson Gomes

### A. Task Description Analysis

This task extends the system designed in Task201 by introducing new behavioral rules: volunteers must outnumber non-volunteers in each monitored zone. Students are required to revise the automaton to support this logic, which cannot be expressed by a finite-state machine. This requires the use of memory-based automata (e.g., pushdown automata), validation via JFLAP, and the production of a technical report describing the problem, the solution, and the evaluation criteria.


### B. Knowledge Enumeration

* Finite State Machines
* Pushdown Automata
* Requirements Engineering
* Formal Languages (Context-Free Grammars)
* Written Communication
* Analytical and Critical Thinking
* Modeling and Simulation



### C. Learning Objectives and Expected Outcomes

* Identify limits of FSM and justify the use of PDA for memory-based control.
* Design and implement a PDA that enforces the "volunteers > non-volunteers" rule.
* Simulate and test the behavior of the PDA using JFLAP.
* Explain the formal mechanisms (e.g., grammar rules or stacks) required for compliance.
* Report technical decisions and implementation details clearly and collaboratively.



### D. Competency Specification

Based on the analysis of **Task202 – Team Control** and the available **Reusable Competences** from the EdukNow Competence Project, the following competencies have been selected as directly aligned with the task’s learning objectives, required knowledge domains, and expected deliverables. Each selected competence includes a justification for its reuse, grounded in the specific demands of the task:



* **EdukNow\_C14 – Develop problem-solving solutions using Pushdown Automata**

**Justification for Reuse:**
The core requirement of Task202 is to model a system that ensures the volunteer-to-non-volunteer ratio complies with institutional rules. This behavior cannot be represented by a simple Finite State Machine (FSM), as it requires stack-based memory to track dynamic input sequences. The use of Pushdown Automata (PDA) is essential to handle this logic, and this competence directly supports the design and implementation of memory-based computational models tailored to real-world control problems.



* **EdukNow\_C07 – Test Automata Using Simulators**

**Justification for Reuse:**
Task202 mandates the use of simulation tools, specifically JFLAP, to validate the behavior of automata models under realistic conditions. This competence addresses the ability to systematically test and refine automaton implementations, ensuring that the modeled PDA meets operational requirements, including the enforcement of team composition rules and the correct issuance of alerts.



* **EdukNow\_C15 – Interpret rule-based notation**

**Justification for Reuse:**
The task includes a request from the company *SOS Florestal* for a formal and structured representation of the rules that govern team formation. This competence focuses on understanding and interpreting rule-based formal notations, such as context-free grammars, which are well-suited to defining the symbolic structure and constraints associated with stack-based automata behavior.



* **EdukNow\_C04 – Write a Technical Report**

**Justification for Reuse:**
One of the required deliverables is a technical report formatted according to SBC guidelines. This competence supports the collaborative writing of structured technical documentation that clearly communicates system design decisions, implementation strategies, simulation results, and compliance with regulatory specifications—an essential component of the project’s final assessment.



* **EdukNow\_C16 – Differentiate classifications of formal grammars**

**Justification for Reuse:**
A critical aspect of the task is to justify the inadequacy of FSMs and the necessity of PDAs based on the expressive power of different formal language classes. This competence develops the ability to distinguish between regular and context-free languages and supports theoretical justification grounded in the Chomsky hierarchy. It enables students to make informed decisions about which computational models best suit the problem context.


