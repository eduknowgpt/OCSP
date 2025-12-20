# Competency Specification Report: Task202 - Team Control

* **Authors:** Luiz Gavaza, Daniel Cason, Lais Salvador, Roberta Oliveira
* **Contributors:** Jéssica Santana, Otávio Neto, Edeyson Gomes

### 1. Task Description Analysis

This task extends the system developed in **Task201** by introducing a new class of behavioral constraints related to **team composition control**. According to updated institutional regulations, the number of **volunteers (V)** must exceed the number of **non-volunteers (NV)** in each monitored zone, following predefined ratios associated with different event types.

Students are required to revise the previously adopted automaton-based solution to support this constraint. Through problem analysis, it is established that such behavior **cannot be correctly modeled using a Finite State Machine (FSM)**, as it requires the ability to **count, compare, and validate quantities dynamically**, which exceeds the expressive power of regular models.

Within the scope of this task, the solution is deliberately framed as a **logical validation and control problem**, rather than a physical or operational one. This motivates the adoption of **memory-based computational models**, particularly **Pushdown Automata (PDAs)**, to represent stack-supported state transitions that enforce the volunteer-to-non-volunteer ratio.

The task therefore challenges students to:
- recognize formal limitations of computational models,
- justify the transition from FSMs to PDAs,
- model and validate the revised system using **JFLAP**, and
- document the solution, design rationale, and evaluation criteria in a **structured technical report**.

This progression reinforces the instructional focus on **model adequacy, formal justification, and abstraction**, central to competency-based learning in Computation Theory.



### 2. Knowledge Enumeration

To address the task effectively, students are expected to mobilize the following **task-relevant knowledge areas**, organized according to their conceptual role within the CSP framework:

#### Core Formal Knowledge
* **Finite State Machines (FSMs)**: understanding their expressive limits and suitability for regular behaviors.
* **Pushdown Automata (PDAs)**: modeling systems with stack-based memory to support context-free constraints.
* **Formal Languages and Context-Free Grammars (CFGs)**: relating automaton behavior to language classes and grammatical representations.
* **Chomsky Hierarchy**: distinguishing computational models based on expressive power to justify model selection.

#### Supporting Technical Knowledge
* **Requirements Analysis**: interpreting regulatory constraints and translating them into formal system specifications.
* **Modeling and Simulation**: applying tools such as **JFLAP** to construct, test, and validate automaton-based solutions.

#### Background and Transversal Knowledge
* **Technical Writing Principles**: structuring and communicating formal models, assumptions, and results in an academic report format.

Concepts related to **analytical reasoning and critical judgment** are treated as **professional dispositions** rather than core knowledge elements and are addressed separately in the competency and disposition analysis.




### 3. Learning Objectives and Expected Outcomes

The learning objectives of Task202 are defined in terms of **observable and justifiable learner actions**, ensuring alignment between formal modeling activities, expected artifacts, and competency assessment.

Specifically, upon completion of the task, students are expected to:

- **Analyze the expressive limitations of Finite State Machines (FSMs)** and formally justify the need for **memory-based computational models**, particularly **Pushdown Automata (PDAs)**, when addressing problems that involve context-sensitive constraints.

- **Design and implement a Pushdown Automaton (PDA)** capable of enforcing constraints that depend on both state and memory conditions, such as ensuring that the number of volunteers exceeds the number of non-volunteers in a monitored zone.

- **Simulate and validate the behavior of the PDA** using **JFLAP**, demonstrating operational correctness, proper stack manipulation, and compliance with problem-specific constraints and institutional rules.

- **Explain and justify the formal mechanisms employed**—including **context-free grammars**, **stack operations**, and **state-transition logic**—that underpin the automaton’s behavior and ensure adherence to the defined constraints.

- **Produce a structured technical report**, following the **SBC academic format**, that documents modeling decisions, implementation strategies, simulation results, and the formal justification of the chosen computational model.

Together, these objectives emphasize not only the construction of formal models, but also the ability to **reason about model adequacy, validate behavior through simulation, and communicate technical decisions clearly and rigorously**.




### 4. Competency Specification

Based on the analysis of the task requirements and the set of **Reusable Competencies** from the EdukNow Competence Project, the following competencies were selected as **directly aligned** with Task202’s learning objectives, required knowledge domains, and expected deliverables.  
Each competency is reused with an explicit justification grounded in the **formal, analytical, and documentary demands** of the task.


* **C12 – Develop problem-solving solutions using Pushdown Automata**

  **Justification for Reuse:**  
  The core challenge of Task202 is to model and validate a system that enforces **volunteer-to-non-volunteer ratio constraints** defined by institutional regulations. Such constraints require the ability to **count, compare, and validate quantities dynamically**, which cannot be expressed by a Finite State Machine (FSM).  
  The use of **Pushdown Automata (PDAs)** is therefore essential, as stack-based memory enables the representation of context-free conditions inherent to the problem. This competency directly supports the **design, implementation, and formal justification** of memory-based computational models tailored to control and validation scenarios.



* **C03 – Test Automata Using Simulators**

  **Justification for Reuse:**  
  Task202 explicitly requires the **simulation and validation** of the proposed automaton using **JFLAP**. This competency supports the systematic testing of PDA behavior, including correct stack manipulation, state transitions, and compliance with the defined team composition rules.  
  Its reuse ensures that learners are able to **verify operational correctness**, identify inconsistencies, and iteratively refine their models based on observed execution traces.



* **C13 – Interpret Rule-Based Notation**

  **Justification for Reuse:**  
  The task includes a request from *SOS Florestal* for a **formal and structured representation of team formation rules**. This competency supports the ability to interpret **rule-based formal notations**, such as **context-free grammars**, which provide a symbolic description of constraints enforced by stack-based automata.  
  In Task202, C13 is primarily activated at an **analytical and interpretative level**, enabling learners to relate institutional rules to formal grammatical or automaton-based representations.



* **C05 – Write a Technical Report**

  **Justification for Reuse:**  
  One of the required deliverables is a **technical report** formatted according to **SBC guidelines**. This competency supports the collaborative production of structured documentation that clearly communicates modeling decisions, formal justifications, simulation results, and compliance with regulatory constraints.  
  Its reuse reinforces technical communication as a transversal competency supporting formal modeling tasks.



* **C14 – Differentiate Classifications of Formal Grammars**

  **Justification for Reuse:**  
  A critical aspect of Task202 is the **formal justification** for transitioning from FSMs to PDAs. This requires distinguishing between **regular and context-free language classes** and understanding their respective expressive power within the **Chomsky hierarchy**.  
  This competency enables learners to ground model selection decisions in formal language theory, reinforcing theoretical rigor and supporting informed, defensible choices of computational models.



Together, these competencies form a **coherent and complementary set** that supports Task202’s emphasis on **formal limitation analysis, model adequacy, memory-based computation, simulation-based validation, and rigorous technical communication**.
