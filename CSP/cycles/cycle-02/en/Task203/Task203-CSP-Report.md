# Competency Specification Report: Task203 – Parking Control

Team Members: Lais Salvador, Edeyson A. Gomes, Luiz Gavaza  
Contributors: Jéssica Santana, Otávio Neto, Roberta Oliveira  

Year: 2022

## 1. Task Description Analysis

The operational requirements include arrivals and departures, release of occupied spaces, daily denied-request counts by category, and continuation of service after a rejected request. The model and report must retain these requirements when explaining the chosen representation.

This task addresses a realistic and high-demand parking management scenario involving three distinct categories of users: daily users, monthly subscribers, and rotating customers. Each incoming parking request must be evaluated against category-specific availability constraints, ensuring that parking spaces are allocated consistently with predefined access rules. Requests must be rejected when no suitable space is available, and the system is required to record and maintain independent counters for denied requests in each category, providing structured information to support future operational or policy decisions.

Students are required to design a machine-based computational model capable of simulating this dynamic control process. The model must correctly manage multiple interdependent state variables, including current availability per user category and accumulated rejection counts, while ensuring that failed requests are properly isolated from the normal service flow and do not compromise system consistency.

Similarly to Task202, the instructional focus is placed on the adequacy of computational models with respect to problem semantics. While Task202 examined the limitations of finite-state representations and motivated the adoption of Pushdown Automata, Task203 extends this progression by introducing requirements that involve multiple independent counters and coordinated memory manipulation over time. A Turing Machine is adopted to represent these coordinated operations. The presence of several counters alone does not establish that every formulation of the parking problem exceeds FSM or PDA capabilities; such a claim depends on the bounds, operations, and input representation.

The task therefore explicitly motivates the adoption of Turing Machines or suitable variants, whose computational expressiveness allows the representation and coordination of multiple memory structures within a single formal model. In this sense, Task203 represents a natural continuation in the progression of computational expressiveness explored in previous tasks (FSM → PDA → TM), reinforcing the principle that model selection must emerge from problem requirements rather than from prior familiarity with specific computational formalisms.

The expected deliverables include:  
(i) a formal machine model, implemented and simulated using JFLAP, demonstrating correct handling of all request scenarios; and  
(ii) a technical report, formatted according to SBC standards, clearly explaining the system design, the selected computational model, and the theoretical rationale supporting the proposed solution.

## 2. Knowledge Enumeration

To effectively address the problem proposed in this task, students are expected to mobilize the following theoretical and practical knowledge areas, each supporting specific aspects of modeling, justification, or validation:

- Turing Machines  
  Knowledge of the structure and operation of Turing Machines is required to model systems that depend on multiple interacting memory structures, such as counters for availability and denied requests across distinct user categories.

- Variants of Turing Machines  
  Understanding common variants (e.g., multi-tape Turing Machines) supports clearer organization and modularization of control mechanisms, enabling more structured representations of complex system behavior without increasing computational power.

- Church–Turing Thesis  
  Familiarity with the Church–Turing Thesis provides the theoretical foundation for arguing that the selected model captures the class of effectively computable behaviors required by the problem.

- Chomsky Hierarchy  
  Knowledge of the Chomsky Hierarchy allows students to situate the problem within the landscape of formal languages and automata, supporting comparison of model capabilities under the assumptions of the parking representation.

- Modeling and Simulation  
  Competence in modeling and simulation tools—particularly JFLAP—is required to implement, execute, and validate the proposed machine model under representative input scenarios.

- Analytical and Critical Thinking  
  Analytical reasoning supports the justification of modeling choices and the evaluation of alternative representations.

- Written Communication  
  The ability to produce clear and structured technical documentation is required to communicate design decisions, theoretical justification, and validation results in the final report following SBC standards.

## 3. Learning Objectives and Expected Outcomes

Upon completion of this task, students are expected to demonstrate the following learning outcomes, integrating theoretical understanding, formal modeling, and technical communication:

1. Justify the use of Turing Machines or suitable variants as the appropriate computational model for the parking-control representation and its coordinated state updates, stating the assumptions about memory and counter bounds.

2. Design a formal machine model capable of correctly separating user categories, managing category-specific availability, and tracking denied requests while preserving system consistency.

3. Simulate and validate the proposed model using JFLAP, demonstrating correct system behavior across representative and edge-case input sequences.

4. Relate the problem and its solution to concepts from Computation Theory, particularly the Chomsky Hierarchy, to justify the expressive power required by the task.

5. Produce a structured technical report, following SBC standards, documenting problem analysis, modeling decisions, simulation results, and theoretical foundations.

6. Apply Problem-Based Learning (PBL) principles to collaboratively organize the problem-solving process and integrate theoretical reasoning with practical modeling activities.

## 4. Competency Specification

Based on the reusable competencies defined in the OntoKSD Competence Project, the following competencies were selected as directly relevant to Task203 – Parking Control. Their selection reflects alignment between the computational requirements of the problem, the formal models involved, and the expected learner artifacts.

### C07 – Develop Problem-Solving Solutions Using Turing Machines

Justification for Reuse:  
Task203 requires learners to model a control system that simultaneously manages multiple categories of parking spaces, dynamic availability, and independent counters for denied requests. The adopted TM representation provides flexible storage for the counters and their updates. A claim that unbounded memory is necessary would additionally require explicit assumptions about the execution horizon and counter bounds.

This competency directly supports the design and construction of Turing Machine–based solutions capable of representing and updating multiple interdependent variables over time. Accordingly, C07 constitutes the core competency of Task203 and represents the natural continuation of the modeling progression established in Task202.

### C08 – Identify Turing Machine Variants

Justification for Reuse:  
The task encourages learners to reason about alternative Turing Machine variants, such as multi-tape machines, as a means of improving conceptual organization or clarity of the solution.

This competency supports analytical comparison between alternative representations, enabling learners to justify structural design choices without necessarily requiring implementation of a specific variant.

### C09 – Apply Turing Machine Variants

Justification for Reuse:  
Task203 allows for the constructive application of Turing Machine variants when such choices improve the clarity or structure of the model. This competency addresses the learner’s ability to select and apply an appropriate variant when it contributes meaningfully to the organization of control logic or memory handling.

Its inclusion reflects the openness of the task to alternative solution strategies while acknowledging that activation may vary depending on the modeling approach adopted.

### C10 – Test Turing Machines Using Simulators

Justification for Reuse:  
Simulation and validation are explicit deliverables of Task203. This competency supports the systematic testing of Turing Machine models using tools such as JFLAP, ensuring correct behavior across valid inputs, edge cases, and rejection scenarios.

### C05 – Write a Technical Report

Justification for Reuse:  
Learners are required to submit a technical report formatted according to SBC standards, documenting problem analysis, modeling decisions, simulation results, and theoretical justification. This competency supports the clear and structured communication of technical solutions.

## 5. Final Remarks

The selected competencies collectively ensure coverage of the conceptual, constructive, justificatory, and communicative dimensions of Task203. The emphasis on Turing Machines reflects the adopted representation of the problem, which involves simultaneous control, memory manipulation, and counting mechanisms.

Within the CSP lifecycle, Task203 represents the consolidation stage of the computational expressiveness progression introduced in previous tasks (FSM → PDA → TM). While Task202 exposed the need for refinement in competency scope under increased theoretical demands, Task203 operates over an already stabilized competency set, providing a consistent instructional context for examining competency reuse under higher expressive requirements without requiring structural changes to competency definitions.
