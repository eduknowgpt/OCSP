# Competency Specification Report: Task203 – Parking Control

**Team Members**: Lais Salvador, Edeyson A. Gomes, Luiz Gavaza  
**Date**: May 11, 2022



## 1. Task Description Analysis

This task addresses a **realistic and high-demand parking management scenario** involving three distinct categories of users: **daily users**, **monthly subscribers**, and **rotating customers**. Each incoming parking request must be evaluated against **category-specific availability constraints**, ensuring that spaces are allocated fairly and consistently with predefined access rules. Requests must be **rejected when no suitable space is available**, and the system is required to **record and maintain separate counters for denied requests in each category**, providing structured information to support future operational or policy decisions.

Students are required to design a **machine-based computational model** that simulates this dynamic control process. The model must correctly manage **simultaneous and interdependent state variables**, such as current availability per user category and accumulated rejection counts, while ensuring that failed requests are **properly isolated from the normal service flow** and do not compromise system consistency.

Given the need to **maintain and update multiple forms of unbounded memory** and to coordinate their interaction over time, the problem exceeds the expressive power of Finite State Machines and Pushdown Automata. The task therefore **explicitly motivates the use of Turing Machines or suitable variants**, as these models provide the necessary computational expressiveness to represent and manipulate multiple counters and control structures.

The expected deliverables include:  
(i) a **formal machine model**, implemented and simulated using **JFLAP**, that demonstrates correct handling of all request scenarios; and  
(ii) a **technical report**, formatted according to **SBC standards**, that clearly explains the system design, the chosen computational model, and the theoretical rationale underlying the proposed solution.




## B. Knowledge Enumeration

To effectively address the problem proposed in this task, students are expected to mobilize the following **theoretical and practical knowledge areas**, each of which supports a specific aspect of the modeling, justification, or validation process:

- **Turing Machines**  
  Knowledge of the structure and operation of Turing Machines is required to model systems that depend on **multiple, interacting forms of memory**, such as counters for availability and rejected requests across user categories.

- **Variants of Turing Machines**  
  Understanding common variants (e.g., **multi-tape Turing Machines**) supports the simplification and clarification of control mechanisms, enabling more structured representations of complex system behavior without increasing computational power.

- **Church–Turing Thesis**  
  Familiarity with the Church–Turing Thesis provides the **theoretical foundation** for arguing that the proposed model captures the full range of effectively computable behaviors required by the problem.

- **Chomsky Hierarchy**  
  Knowledge of the Chomsky Hierarchy allows students to **position the problem within the landscape of formal languages and automata**, justifying why the task exceeds the expressive capabilities of finite-state and pushdown models.

- **Modeling and Simulation**  
  Competence in modeling and simulation tools—particularly **JFLAP**—is required to implement, execute, and validate the proposed machine model under representative input scenarios.

- **Analytical and Critical Thinking**  
  Analytical reasoning supports the **justification of modeling choices**, the identification of constraints and trade-offs, and the evaluation of alternative representations or optimizations.

- **Written Communication**  
  The ability to produce clear and structured technical documentation is required to **communicate design decisions, theoretical justifications, and validation results** in the final report, following **SBC standards**.




## 3. Learning Objectives and Expected Outcomes

Upon completion of this task, students are expected to demonstrate the following learning outcomes, which integrate **theoretical understanding**, **formal modeling**, and **technical communication**:

1. **Justify the use of Turing Machines or suitable variants** as the appropriate computational model for control problems that require **unbounded memory, multiple counters, and interdependent state updates**.

2. **Design a formal machine model** capable of correctly separating user categories, managing category-specific availability, and **tracking denied requests with integrity**, ensuring that rejected inputs do not interfere with the normal service flow.

3. **Simulate and validate the proposed model using JFLAP**, demonstrating correct system behavior across representative and edge-case input sequences.

4. **Relate the problem and its solution to concepts from Computation Theory**, particularly the **Chomsky Hierarchy**, to justify the expressive power required by the task.

5. **Produce a structured technical report**, following **SBC standards**, that documents the problem analysis, modeling decisions, simulation results, and theoretical foundations of the solution.

6. **Apply the principles of Problem-Based Learning (PBL)** to collaboratively structure the problem-solving process, coordinate responsibilities, and integrate theoretical reasoning with practical modeling activities.




## 4. Competency Specification

Based on the reusable competencies defined in the **OntoKSD Competence Project**, the following competencies were selected as directly relevant to **Task203 – Parking Control**. Their selection reflects a deliberate alignment between the **computational complexity of the problem**, the **formal models required**, and the **expected learner artifacts**.


### **C07 – Develop Problem-Solving Solutions Using Turing Machines**

**Justification for Reuse:**  
Task203 requires learners to model a control system that simultaneously manages **multiple categories of parking spaces**, **dynamic availability**, and **independent counters for denied requests**. These requirements demand **unbounded and flexible memory manipulation**, exceeding the expressive capabilities of finite or pushdown automata.  

This competency directly supports the **design and construction of Turing Machine–based solutions** capable of representing and updating multiple interdependent variables over time. As such, **C07 constitutes the core (nuclear) competency** of Task203, aligning precisely with its modeling and implementation demands.



### **C08 – Identify Turing Machine Variants**

**Justification for Reuse:**  
The task encourages learners to reason about **alternative Turing Machine variants**—such as multi-tape machines—as a means of improving **clarity, modularity, or conceptual organization** of the solution.  

This competency supports the **analytical comparison of Turing Machine variants**, enabling students to justify why a particular representation may be more suitable for structuring counters, categories, or control logic, without necessarily requiring its implementation.



### **C09 – Apply Turing Machine Variants**

**Justification for Reuse:**  
Task203 may benefit from the **constructive application of a Turing Machine variant** (e.g., multi-tape) to separate concerns such as availability tracking and rejection counting. This competency addresses the learner’s ability to **select and apply an appropriate variant** when such a choice meaningfully improves the structure or transparency of the model.

Its inclusion reflects the task’s openness to **design alternatives**, while acknowledging that the activation of this competency may vary depending on the chosen solution strategy.



### **C10 – Test Turing Machines Using Simulators**

**Justification for Reuse:**  
Simulation and validation are explicit deliverables of Task203. This competency supports the **systematic testing of Turing Machine models** using tools such as **JFLAP**, ensuring that the proposed solution behaves correctly across valid inputs, edge cases, and rejection scenarios.



### **C05 – Write a Technical Report**

**Justification for Reuse:**  
Learners are required to submit a **technical report formatted according to SBC standards**, documenting problem analysis, modeling decisions, simulation results, and theoretical justification. This competency supports the **clear and structured communication of technical solutions**, which is essential for demonstrating both conceptual understanding and professional practice.


## E. Final Remarks

The selected competencies collectively ensure comprehensive coverage of the **conceptual, constructive, justificatory, and communicative dimensions** of Task203. The emphasis on **Turing Machines** reflects the intrinsic complexity of the problem, which involves **simultaneous control, memory manipulation, and counting mechanisms**.

From a CSP perspective, Task203 represents a **natural progression in computational expressiveness** (FSM → PDA → TM) and provides a robust instructional context for examining the interaction between **core modeling competencies**, **theoretical justification**, **simulation**, and **technical documentation** within a competency-oriented framework.
