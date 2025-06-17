# Competency Specification Report: Task203 – Parking Control

**Team Members**: Lais Salvador, Edeyson A. Gomes, Luiz Gavaza  
**Date**: May 11, 2022



## A. Task Description Analysis

This task addresses the real-world problem of managing parking spots in a high-demand scenario involving three categories of users: daily users, monthly subscribers, and rotating customers. Each parking request must be matched with availability within the correct category, and requests must be rejected if no suitable space is available. Additionally, the system must count and track the number of denied requests per category to inform future decisions.

Students must design a machine-based model to simulate this dynamic control process, ensuring the fair and correct allocation of resources and the isolation of failed requests from the normal flow of service. Due to the complexity of managing concurrent state and memory (such as spot availability per category and rejection counters), the problem requires a computational model capable of maintaining and updating multiple interdependent variables. The task explicitly encourages the use of Turing Machines or their variants.

Deliverables include a machine model (to be implemented and simulated in JFLAP) and a technical report, formatted according to SBC standards, that explains the solution’s design and theoretical foundation.



## B. Knowledge Enumeration

To effectively address the problem, the following knowledge areas are required:

- **Turing Machines**: For modeling complex, memory-dependent systems.
- **Variants of Turing Machines**: To simplify or specialize control mechanisms (e.g., multi-tape or oracle machines).
- **Church-Turing Thesis**: To support theoretical justification of computational capability.
- **Chomsky Hierarchy**: For understanding the position of Turing-recognizable languages and problems.
- **Modeling and Simulation**: For validating the system in JFLAP.
- **Analytical and Critical Thinking**: For justifying model design and optimizing the control structure.
- **Written Communication**: For producing the final technical report.



## C. Learning Objectives and Expected Outcomes

1. Justify the use of Turing Machines (or variants) to solve control problems involving memory and counters.
2. Design a machine model that separates categories and tracks denied requests with integrity.
3. Simulate the proposed solution in JFLAP to confirm behavior under various input sequences.
4. Relate the problem to concepts from the Chomsky Hierarchy and Computation Theory.
5. Document all aspects of the solution in a structured technical report, including examples and theoretical analysis.
6. Apply the Problem-Based Learning (PBL) methodology to structure collaboration and task resolution.



## D. Competency Specification

Based on the competencies defined in the EdukNow Competence Project, the following reusable competencies are selected as relevant to Task203:



### **EdukNow_C09 – Develop Problem-Solving Solutions Using Turing Machines**

**Justification for Reuse:**  
The parking control task requires modeling dynamic state transitions, tracking occupancy across multiple categories, and counting denied requests. These capabilities exceed the power of finite or pushdown automata, making the use of Turing Machines necessary. This competency covers the design and implementation of Turing Machine-based models to solve structured, memory-intensive problems, aligning directly with the requirements of Task203.



### **EdukNow_C10 – Identify Turing Machines Variants**

**Justification for Reuse:**  
The task involves evaluating alternative modeling strategies and selecting the most appropriate Turing Machine variant for efficiency or clarity. This competency supports the theoretical understanding and comparison of Turing Machine extensions—such as multi-tape machines—that may simplify or optimize the parking system’s design.



### **EdukNow_C11 – Apply Turing Machine Variants**

**Justification for Reuse:**  
This task may benefit from implementing a machine variant (e.g., multi-tape) to separately manage counters and category queues. Competence C11 ensures that students are capable of selecting and applying these variants effectively, enhancing the model’s expressiveness and alignment with operational goals.



### **EdukNow_C17 – Test Turing Machines Using Simulators**

**Justification for Reuse:**  
The deliverables require simulation and validation using JFLAP. This competence emphasizes testing machine-based models to ensure correctness, completeness, and compliance with specification constraints, which are all vital for Task203.



### **EdukNow_C04 – Write a Technical Report**

**Justification for Reuse:**  
The task requires submission of a detailed technical report in SBC format. This competence supports the production of well-structured documentation that explains the modeling decisions, simulation outcomes, and theoretical justification of the implemented solution.



## E. Final Remarks

The selected competencies ensure coverage of all essential aspects of Task203, including model design, formal justification, simulation, and documentation. The focus on Turing Machines reflects the complexity of the task, which involves both real-time state control and memory manipulation. The Competency Specification supports a robust learning process aligned with the objectives of the Computation Theory course and the practical needs of EstaciONE.

