## **Introduction**

Grounded in the principles of the **Competency Specification Process (CSP)**, this report documents the **Competency Authoring phase** applied to **TASK25.20 – Tic-Tac-Toe Implementation**. The task is situated in an introductory programming context and is designed to elicit observable evidence of students’ ability to **design, implement, and explain a complete interactive program** using fundamental concepts of **structured programming**.

TASK25.2 requires learners to construct a fully functional **3×3 Tic-Tac-Toe game**, integrating essential programming constructs such as **data representation through lists or matrices**, **control flow via conditionals and loops**, and **procedural decomposition using functions**. Beyond the production of a working artifact, the task explicitly demands that students **articulate the rationale behind their implementation choices** and **trace the execution flow of the program**, thereby linking practical coding activity to conceptual understanding.

From a CSP perspective, this task is particularly relevant because it naturally supports the identification and specification of competencies across the **Knowledge–Skill–Disposition (K–S–D)** triad. It combines:

- **Knowledge elements**, related to basic programming concepts and structures;
- **Skills**, evidenced through the construction, validation, and execution of a computational solution;
- **Dispositions**, manifested in collaborative work practices, individual accountability, and reflective explanation during oral assessment.

Accordingly, TASK25.20 provides a well-bounded instructional scenario for specifying **introductory computational competencies**, enabling systematic alignment between task requirements, expected evidence, and competency activation within the CSP framework.



## **1. Instructional Entity Analysis**

### Title

    Tic-Tac-Toe Implementation (3×3)

### Description

Learners are confronted with the task of **designing and implementing a complete Tic-Tac-Toe game**, in which two human players alternate turns while respecting the formal rules of the game. The solution must ensure **robust handling of user input**, enforce valid moves within the board boundaries, correctly identify **winning conditions** (rows, columns, and diagonals), and detect **draw scenarios**.  

Throughout the task, students are expected to apply and integrate **core structured programming concepts**, transforming a well-defined problem specification into a consistent and executable computational solution.



### Solution Development Process

The expected learner approach involves the following stages:

* **Analyze the problem constraints**, including turn alternation, move validity, board limits, winning patterns, and draw conditions.

* **Model the solution as a structured program**, selecting appropriate data representations (e.g., lists or matrices) and organizing logic through conditionals, loops, and clearly defined functions.

* **Iteratively simulate and validate the program execution**, testing representative scenarios such as row, column, and diagonal victories, as well as invalid or repeated inputs.

* **Document and justify design decisions**, using explanatory comments, modular code organization, and an **individual oral explanation** in which the learner demonstrates both conceptual understanding and procedural reasoning about the implemented solution.



### Expected Outcomes

Learners are expected to produce the following outcomes:

- A **fully functional and robust implementation** of a 3×3 Tic-Tac-Toe game that correctly enforces game rules and termination conditions.
- A **modular program structure**, decomposed into coherent and well-defined functions (e.g., board initialization, move validation, victory detection, and main game loop).
- A **clear and well-documented source code file or repository**, demonstrating appropriate use of lists or matrices, conditionals, loops, parameters, and basic modularization.
- A **practical demonstration** in which the program executes correctly across multiple scenarios, including valid and invalid moves, winning configurations, and draw situations.
- An **individual oral explanation** that justifies design decisions, evidences authorship, and clearly communicates the program logic using appropriate technical vocabulary.
- **Evidence of collaborative engagement** during development, reflected in equitable task distribution, peer respect, and constructive interaction within the group.



### Acquisition Context

This learning task is carried out within the **Programming Logic** course of the **Integrated Technical Program in Informatics (1st year)** at **IFBA – Valença Campus**.

The activity takes place in a **hands-on computer laboratory environment**, supported by prior instructional content covering fundamental aspects of structured programming, including lists, matrices, conditionals, loops, and basic function definition.

Students work in **pairs or small groups (two to three learners)** during the development phase; however, **individual accountability is ensured** through an oral assessment in which each student must independently defend and justify the implemented solution.

This context emphasizes the integrated development of **conceptual understanding**, **practical programming skills**, **ethical authorship**, and **technical communication abilities**.
 


### Target Audience Profile

- **Educational Level:** First-year students enrolled in an **Integrated Technical Program in Informatics**.
- **Prior Knowledge:** Introductory understanding of algorithms, variables, assignment statements, and basic input/output operations.
- **Programming Experience:** **Beginner level**, with initial exposure to structured programming concepts.
- **Learning Needs:** Access to clear examples, step-by-step instructional guidance, opportunities for hands-on practice with debugging, and structured moments to articulate and reflect on programming decisions.
- **Expected Dispositions:** Willingness to collaborate, attention to detail, openness to feedback, and ethical engagement in shared and individual work.



### Proficiency Scale

Learner performance is evaluated using a **numerical scale from 0.0 to 10.0**, with increments of **0.1**, based on the following dimensions:

- **Technical Correctness:** The program executes without errors, enforces valid moves, and correctly detects winning and draw conditions.
- **Conceptual Understanding:** The learner demonstrates the ability to explain program flow, control structures, data representations, and the role of functions.
- **Code Quality and Organization:** Clarity of the code, appropriate modularization, meaningful naming conventions, and overall structural coherence.
- **Problem-Solving Process:** Evidence of systematic debugging, testing across scenarios, and analytical reasoning about edge cases.
- **Communication and Authorship:** Clarity of oral explanations, appropriate use of technical vocabulary, and ethical justification of individual contributions.
- **Collaboration:** Observable evidence of equitable participation, shared responsibility, and constructive interaction during group work.



## 2. Knowledge Enumeration

This section enumerates the **knowledge elements explicitly activated and mobilized** by TASK25.20, refined to improve **granularity, traceability, and alignment with CSP and OntoKSD principles**. The listed elements represent **conceptual knowledge required to support observable learner actions**, rather than implicit or background familiarity.


### 2.1. Fundamentals of Programming

* **K1 – Concept of algorithm**
  * Understanding an algorithm as a **finite, ordered, and unambiguous sequence of instructions** designed to solve a well-defined problem.
  * Recognition of algorithmic properties such as **initial state, processing steps, and termination**.

* **K2 – Basic data types and variables**
  * Use of primitive data types (e.g., integers, characters, strings).
  * Declaration and assignment of variables.
  * Understanding variable scope in simple program structures.

* **K3 – Input and output operations**
  * Reading user input from standard input.
  * Displaying messages, game states, and results to the user.
  * Formatting output to support user interaction and clarity.



### 2.2. Simple Data Structures

* **K4 – Lists and matrices (vectors and two-dimensional arrays)**
  * Index-based access and traversal.
  * Initialization and update of elements.
  * Conceptual distinction between one-dimensional and two-dimensional representations.

* **K5 – State representation using data structures**
  * Modeling system state through data structures.
  * Representing the game board as a **matrix or list of lists**.
  * Understanding how data structure updates reflect state transitions in the game.



### 2.3. Control Structures

* **K6 – Conditional structures (if / elif / else or equivalents)**
  * Construction of conditional expressions.
  * Use of conditionals to validate moves, enforce rules, and detect game outcomes.
  * Nesting and sequencing of conditionals for multi-criteria decision making.

* **K7 – Repetition structures (while / for loops)**
  * Iterative execution of code blocks.
  * Use of loops to control the main game cycle.
  * Definition of stopping conditions linked to game termination.



### 2.4. Decomposition and Modularization

* **K8 – Functions and procedures with parameters and return values**
  * Definition and invocation of functions.
  * Passing arguments and receiving return values.
  * Encapsulation of functionality to improve readability and reuse.

* **K9 – Problem decomposition into subproblems**
  * Breaking a complex problem into manageable components.
  * Identification of functional responsibilities such as:
    * board initialization and display;
    * move acquisition and validation;
    * win and draw detection;
    * orchestration of the main game loop.
  * Understanding the role of modular structure in program comprehension.



### 2.5. Logical Reasoning and Debugging

* **K10 – Logical and relational operators**
  * Use of equality, inequality, and relational comparisons.
  * Application of logical operators (AND, OR, NOT) in compound conditions.
  * Construction of Boolean expressions to encode rules and constraints.

* **K11 – Basic notions of testing and debugging**
  * Systematic testing of representative execution paths.
  * Validation of win conditions across rows, columns, and diagonals.
  * Identification and correction of logical and runtime errors.
  * Reasoning about edge cases, such as repeated or invalid moves.



### 2.6. Collaborative and Ethical Aspects

* **K12 – Teamwork fundamentals in software development**
  * Division of tasks and responsibilities within a small group.
  * Communication and coordination during collaborative development.
  * Shared ownership of the artifact while maintaining individual accountability.

* **K13 – Ethical authorship and academic integrity**
  * Recognition and explanation of individual contributions.
  * Respect for collaborative work without misrepresentation of authorship.
  * Ethical conduct during oral defense and code presentation.



**Analytical Note:**  
This knowledge enumeration prioritizes **task-relevant, observable, and teachable concepts**, avoiding unnecessary theoretical abstraction. Each knowledge item is directly traceable to **learner actions, expected evidence, and assessment criteria**, supporting its later pairing with skills and dispositions in the CSP competency model.




## 3. Learning Objectives Identification

> **By the end of TASK25.2, the learner should be able to:**

1. **LO1 – Describe**, in clear and structured natural language, the overall functioning of the Tic-Tac-Toe game and the execution flow of the program that implements it, from initialization to termination.

2. **LO2 – Represent** the game board state using appropriate data structures (lists or matrices), explaining how indexes and positions correspond to game elements and player moves.

3. **LO3 – Implement** conditional and repetition structures to control the game flow, ensuring correct alternation of players and proper enforcement of stopping conditions (victory or draw).

4. **LO4 – Decompose** the solution into cohesive and well-defined functions (e.g., board display, move acquisition and validation, win/draw detection, main game loop), justifying the adopted modular structure.

5. **LO5 – Validate** user input by detecting and rejecting invalid or illegal moves, and provide clear and informative feedback messages to guide user interaction.

6. **LO6 – Test and Debug** the program using representative execution scenarios (row, column, and diagonal wins; draw situations), identifying, explaining, and correcting logical or runtime errors.

7. **LO7 – Explain Orally** the structure and behavior of the implemented code, detailing the interaction between functions and tracing the execution of a complete game match using appropriate technical vocabulary.

8. **LO8 – Collaborate** effectively within a small group, assuming responsibilities, contributing equitably to the development process, and demonstrating ethical authorship and respect for peers.


**Analytical Note:**  
These learning objectives are formulated using **observable and assessable action verbs**, facilitating their alignment with **Bloom’s Revised Taxonomy**, the **Knowledge–Skill–Disposition (K–S–D)** triad, and subsequent **Knowledge–Skill pairing** within the CSP framework.




## 4. Competency Definition

## General Competency (BNCC – Computing in Basic Education)

* **Understand, analyze, design, and implement computational solutions** for everyday problems, mobilizing concepts of algorithms, data representation, and control structures in an ethical, collaborative, and reflective manner.


## Competency CT25.20.1 Specification

### Competency Title

    Identify and specify functional constraints from a problem statement.


### Textual Description

This competency involves the ability to **analyze a concrete computational problem** in order to **identify, interpret, and explicitly specify its functional constraints and requirements** prior to implementation.

In the context of TASK25.2, the learner examines the rules and behavior of the Tic-Tac-Toe game, recognizing elements such as valid moves, turn alternation, winning conditions, draw situations, and termination criteria. These observations are then **translated into structured and explicit requirements** that guide subsequent algorithm design and coding decisions.

The competency emphasizes **analytical reasoning** to decompose the problem into relevant constraints, as well as **clear and organized expression** of these constraints. Although developed collaboratively, the competency requires each learner to demonstrate **individual understanding** of the identified requirements and their role in shaping the solution.



### Knowledge Specification

The following knowledge areas are critical for this competency:

* **Analytical Thinking (FPK)**

  * The learner must be able to **analyze** the behavior of a computational problem, decomposing it into observable logical components such as actions, conditions, and constraints. This analysis supports understanding of cause–effect relationships and anticipation of design decisions that must be addressed during implementation.

  * **Bloom’s Taxonomy Alignment:** Analyze  
  * **Knowledge–Skill Pairing:** Analytical Thinking / Analyze  
  * **Verb Annotation:** Analyze, Decompose, Identify, Examine

* **Requirements Identification and Specification**

  * The learner must be able to **apply basic principles of requirements specification**, expressing expected functionalities and constraints (e.g., valid inputs, stopping conditions, rule enforcement) in a structured and comprehensible manner that can be directly used to guide coding.

  * **Bloom’s Taxonomy Alignment:** Apply  
  * **Knowledge–Skill Pairing:** Requirements Specification / Apply  
  * **Verb Annotation:** Specify, Describe, Organize, Formulate



### Disposition Specification

* **Meticulous** — demonstrates attention to detail and completeness when identifying and expressing problem constraints, ensuring that essential rules and conditions are not overlooked.

* **Collaborative** — engages constructively in group discussions to compare interpretations, clarify ambiguities, and reach a shared understanding of the problem requirements.



### BNCC-Aligned Competencies

**General Competency 1 – Computing (High School)**  
> “Understand the possibilities and limits of Computing to solve problems (...), proposing and analyzing computational solutions for various domains of knowledge.”  
This competency directly supports the analysis of a problem and the identification of constraints that shape a viable computational solution.

**General Competency 5 – Computing (High School)**  
> “Develop projects to investigate contemporary challenges, build solutions (...), preferably in a collaborative manner.”  
Identifying and specifying requirements constitutes the initial stage of a collaborative computational project.

**Specific Competencies:**

* **EM13CO01** – Explore and construct problem solutions through the reuse and adaptation of parts of existing solutions.
* **EM13CO02** – Explore and refine computational solutions across levels of abstraction, from specification to implementation.



### Summary Table for Competency CT25.20.1

| **Code** | **Competency**                                                                 | **Dispositions**          | **Knowledge**                       | **Skill**                          |
| -------- | ------------------------------------------------------------------------------ | ------------------------- | ----------------------------------- | ---------------------------------- |
| CT25.20.1 | **Identify and specify functional constraints from a problem statement.**     | Meticulous, Collaborative | Analytical Thinking (FPK)           | **Analyze (Analyze, Decompose)**   |
|          |                                                                                |                           | Requirements Specification          | **Apply (Specify, Formulate)**     |


### Activation Definition — Competency CT25.20.1

**ActivationConstraint:** `mandatory`  
This competency is required for TASK25.2, as identifying game rules and constraints (e.g., valid moves, turn alternation, victory and draw conditions) is essential to structure program flow, represent the board state, and define stopping criteria.

**ActivationMode:** `analytical`  
The activation is predominantly analytical, focusing on decomposing the game into rules and constraints, identifying cause–effect relationships, and abstracting system behavior prior to coding.

**ActivationRole:** `supporting`  
Within TASK25.2, this competency plays a supporting role, as it underpins core competencies related to data representation, control flow, and modularization, while being assessed indirectly through the coherence and correctness of the implemented solution.





## Competency CT25.20.2 Specification

### Competency Title

    Organize and represent information using structured data formats.



### Textual Description

This competency involves the ability to **model and represent problem-domain information using appropriate data structures**, transforming conceptual elements into computational representations that can be effectively manipulated by a program.

In the context of TASK25.2, the learner translates elements of the Tic-Tac-Toe game—such as the board, player moves, and intermediate game states—into **lists or nested lists (matrices)**. This representation enables correct enforcement of game rules, consistent state updates, and clear visualization of the game progression.

The competency emphasizes **precision and coherence in data representation**, ensuring that indexes, values, and structures faithfully reflect the intended domain model. Collaborative interaction supports the validation of representation choices and the resolution of inconsistencies, while individual understanding is required to correctly manipulate and explain the chosen structures.



### Knowledge Specification

The following knowledge areas are critical for this competency:

- **Data Structures**

  - The learner must be able to **apply structured data formats** (e.g., lists and matrices) to store and manipulate program state. This includes accessing, updating, and displaying data in a consistent and readable manner throughout execution.

  * **Bloom’s Taxonomy Alignment:** Apply  
  * **Knowledge–Skill Pairing:** Data Structures / Apply  
  * **Verb Annotation:** Use, Manipulate, Modify, Implement

- **Information Modeling**

  - The learner must be able to **model domain information** by identifying relevant entities and organizing them into computational structures that support clear processing and state transitions.

  * **Bloom’s Taxonomy Alignment:** Apply  
  * **Knowledge–Skill Pairing:** Information Modeling / Apply  
  * **Verb Annotation:** Represent, Structure, Organize, Construct

- **Analytical Thinking (FPK)**

  - The learner must apply **analytical reasoning** to determine what information must be represented, how elements relate to one another, and how these relationships affect data operations, avoiding redundancy and logical inconsistencies.

  * **Bloom’s Taxonomy Alignment:** Analyze  
  * **Knowledge–Skill Pairing:** Analytical Thinking / Analyze  
  * **Verb Annotation:** Analyze, Distinguish, Compare, Organize



### Disposition Specification

* **Meticulous** — demonstrates attention to detail when defining and manipulating data structures, avoiding indexing errors, inconsistent values, or ambiguous representations.

* **Collaborative** — engages constructively with peers to validate modeling decisions, discuss alternatives, and ensure coherence with previously defined constraints.



### BNCC-Aligned Competencies

**General Competency 1 – Computing (High School)**  
Representing information using structured formats supports the analysis and construction of viable computational solutions.

**General Competency 4 – Computing (High School)**  
Building computational artifacts involves selecting and applying appropriate techniques for data representation and manipulation.

**Specific Competencies:**

* **EF15CO01** – Identify structured ways to organize and represent information, including matrices and lists.  
* **EF04CO01** – Recognize objects represented by matrices with coordinate-based positions.  
* **EF07CO03** – Build computational solutions by selecting appropriate data structures, individually or collaboratively.  
* **EF09CO02** – Select adequate data types and structures for proposed situations.  
* **EM13CO02** – Refine computational solutions across levels of abstraction, from modeling to implementation.



### Summary Table for Competency CT25.20.2

| **Code** | **Competency**                                                         | **Dispositions**          | **Knowledge**              | **Skill**                                   |
|--------|-------------------------------------------------------------------------|---------------------------|----------------------------|---------------------------------------------|
| CT25.20.2 | **Organize and represent information using structured data formats.** | Meticulous, Collaborative | Data Structures            | **Apply (Use, Manipulate, Modify)**          |
|        |                                                                         |                           | Information Modeling       | **Apply (Represent, Structure, Organize)**   |
|        |                                                                         |                           | Analytical Thinking (FPK)  | **Analyze (Analyze, Distinguish, Compare)**  |



### Activation Definition — Competency CT25.20.2

**ActivationConstraint:** `mandatory`  
This competency is required, as correct data representation is essential for implementing game rules, maintaining state consistency, and enabling further control-flow and modularization competencies.

**ActivationMode:** `constructive`  
The activation is constructive, since learners actively **build and manipulate a concrete computational artifact** (lists or matrices) that embodies the game state.

**ActivationRole:** `core`  
Within TASK25.2, this competency plays a core role, as structured data representation is central to the correctness, clarity, and functionality of the implemented solution.





## Competency CT25.20.3 Specification

### Competency Title

    Control program flow using conditional and repetition structures.



### Textual Description

This competency involves the ability to **control the dynamic behavior of a program** through the correct and coherent use of **conditional structures and loops**, ensuring that execution follows the intended logical flow from initialization to termination.

In the context of TASK25.2, the learner applies decision and iteration constructs to manage **turn alternation**, **input validation**, and **game termination conditions** (victory or draw). This requires translating game rules into Boolean expressions, defining stopping conditions, and coordinating multiple control structures so that the program behaves consistently in all scenarios.

While creativity and experimentation may emerge during development, the core of this competency lies in **systematic application of control-flow mechanisms**, supported by meticulous reasoning to prevent logical errors. Collaborative interaction contributes to discussing alternative control strategies and jointly validating correctness, but individual mastery of control flow is essential.



### Knowledge Specification

The following knowledge areas are critical for this competency:

- **Conditional Structures (if / elif / else)**

  - The learner must be able to **apply conditional structures** to make decisions during program execution, such as validating moves, detecting winning configurations, and identifying draw conditions.

  * **Bloom’s Taxonomy Alignment:** Apply  
  * **Knowledge–Skill Pairing:** Conditional Structures / Apply  
  * **Verb Annotation:** Use, Implement, Select, Determine, Evaluate

- **Repetition Structures (while / for)**

  - The learner must be able to **apply repetition structures** to construct iterative execution flows, including the main game loop, repeated input handling, and controlled termination based on predefined conditions.

  * **Bloom’s Taxonomy Alignment:** Apply  
  * **Knowledge–Skill Pairing:** Repetition Structures / Apply  
  * **Verb Annotation:** Iterate, Execute, Repeat, Maintain, Control

- **Relational and Logical Operators**

  - The learner must be able to **apply relational and logical operators** to build Boolean expressions that encode rules and constraints, enabling precise and efficient control of decisions and loop conditions.

  * **Bloom’s Taxonomy Alignment:** Apply  
  * **Knowledge–Skill Pairing:** Logical Reasoning / Apply  
  * **Verb Annotation:** Compare, Test, Validate, Combine, Construct



### Disposition Specification

* **Meticulous** — maintains careful attention to logical coherence, avoiding contradictions, unreachable conditions, or control-flow failures.
* **Persistent** — systematically tests and refines control logic to resolve errors and unexpected behaviors.
* **Collaborative** — engages with peers to discuss control strategies and verify correct execution across scenarios.



### BNCC-Aligned Competencies

**General Competency 1 – Computing (High School)**  
Apply algorithms and control structures to solve concrete problems through computational solutions.

**General Competency 5 – Computing (High School)**  
Develop computational projects that address real-world challenges, requiring robust and well-controlled execution flow.

**Specific Competencies:**

* **EF15CO02** – Develop and simulate algorithms involving sequences, selections, and repetitions.  
* **EF03CO02** – Work with simple conditional repetitions in algorithms.  
* **EF04CO03** – Elaborate algorithms involving simple and nested repetitions.  
* **EF69CO02** – Create algorithms using selection and repetition structures across different programming languages.



### Summary Table for Competency CT25.20.3

| **Code** | **Competency**                                                      | **Dispositions**                    | **Knowledge**                   | **Skill**                                   |
|--------|----------------------------------------------------------------------|------------------------------------|---------------------------------|---------------------------------------------|
| CT25.20.3 | **Control program flow using conditional and repetition structures.** | Meticulous, Persistent, Collaborative | Conditional Structures          | **Apply (Use, Implement, Select)**           |
|        |                                                                      |                                    | Repetition Structures           | **Apply (Iterate, Execute, Maintain)**       |
|        |                                                                      |                                    | Logical / Relational Operators  | **Apply (Compare, Test, Validate, Combine)** |



### Activation Definition — Competency CT25.20.3

**ActivationConstraint:** `mandatory`  
This competency is mandatory, as correct control of execution flow is essential for implementing game rules, managing interaction, and ensuring proper termination of the program.

**ActivationMode:** `constructive`  
The activation is constructive, since learners actively build and refine executable control-flow structures within the program.

**ActivationRole:** `core`  
Within TASK25.2, this competency plays a core role, as conditional and repetition structures directly determine the correctness and robustness of the implemented solution.





## Competency CT25.20.4 Specification

### Competency Title

    Decompose programs into cohesive and independent functions.



### **Textual Description**

This competency involves the ability to **structure a program in a modular manner**, decomposing a computational problem into **independent and cohesive functions**, each responsible for a clearly defined part of the solution.

In the context of TASK25.2, the learner organizes the program into functions that encapsulate responsibilities such as initializing and displaying the board, reading and validating moves, checking victory or draw conditions, and coordinating the main execution flow. This requires defining **appropriate parameters and return values**, understanding how data flows between functions, and ensuring that each component can be **understood, tested, and modified in isolation**.

Modularization reflects **maturity in computational reasoning**, supporting code clarity, reuse, and maintainability. While collaboration contributes to the integration of components developed by different group members, individual mastery of functional decomposition and scope management is essential.



### Knowledge Specification

- **Functions, Parameters, and Return Values**

  - The learner must be able to **design and create functions** that encapsulate specific responsibilities within the program. This includes defining suitable parameters, planning return values, and composing functions in a way that supports the overall program logic.

  * **Bloom’s Taxonomy Alignment:** Create  
  * **Knowledge–Skill Pairing:** Function Design / Create  
  * **Verb Annotation:** Design, Create, Construct, Develop, Compose

- **Variable Scope**

  - The learner must correctly **apply the concept of variable scope**, distinguishing between local and global variables to ensure predictable behavior, avoid unintended side effects, and maintain semantic clarity across functions.

  * **Bloom’s Taxonomy Alignment:** Apply  
  * **Knowledge–Skill Pairing:** Variable Scope / Apply  
  * **Verb Annotation:** Apply, Utilize, Differentiate, Maintain



### Disposition Specification

* **Meticulous** — demonstrates careful attention to semantic consistency when defining functions, parameters, and return values, minimizing redundancy and errors.
* **Collaborative** — contributes constructively to the division of responsibilities and integration of program components, communicating clearly with peers.



### BNCC-Aligned Competencies

**General Competency 4 – Computing (High School)**  
Build computational artifacts by applying techniques and technologies that support clarity, organization, and quality.

**General Competency 5 – Computing (High School)**  
Develop computational projects collaboratively, requiring modular design to support teamwork and maintainability.

**Specific Competency:**

* **EM13CO02** – Refine computational solutions across levels of abstraction, including decisions about how to decompose programs into functions and coordinate their interaction.



### Summary Table for Competency CT25.20.4

| **Code** | **Competency**                                                     | **Dispositions**          | **Knowledge**                        | **Skill**                                |
|--------|---------------------------------------------------------------------|---------------------------|--------------------------------------|-------------------------------------------|
| CT25.20.4 | **Decompose programs into cohesive and independent functions.** | Meticulous, Collaborative | Function Design                      | **Create (Design, Create, Compose)**       |
|        |                                                                     |                           | Variable Scope                       | **Apply (Apply, Differentiate, Maintain)** |



### Activation Definition — Competency CT25.20.4

**ActivationConstraint:** `mandatory`  
This competency is mandatory, as modular decomposition is essential for managing program complexity, supporting testing, and ensuring maintainability of the solution.

**ActivationMode:** `constructive`  
The activation is constructive, since learners actively design and implement functional components that constitute the executable program.

**ActivationRole:** `core`  
Within TASK25.2, this competency plays a core role, as modularization directly impacts program correctness, readability, and the integration of other core competencies such as data representation and control flow.





## Competency CT25.20.5 Specification

### Competency Title

    Explain and justify computational solutions with ethical authorship.


### Textual Description

This competency involves the ability to **explain, justify, and defend a computational solution**, demonstrating conceptual understanding, clear communication, and ethical responsibility for the produced artifact.

In the context of TASK25.2, the learner must orally explain the structure and behavior of the implemented program, justify key implementation decisions, and accurately describe the interaction between data structures, control flow, and functions. This explanation must reflect **authentic authorship**, evidencing individual understanding even when the solution was developed collaboratively.

The competency integrates **technical communication**, **logical reasoning**, and **ethical conduct**, ensuring that learners not only produce a correct solution but are also able to **account for it transparently and responsibly** in an academic setting.



### Knowledge Specification

- **Programming Technical Vocabulary**

  - The learner must **understand and correctly use technical programming terminology**, such as function, loop, conditional, variable, and data structure, enabling precise interpretation and explanation of the code.

  * **Bloom’s Taxonomy Alignment:** Understand  
  * **Knowledge–Skill Pairing:** Technical Vocabulary / Understand  
  * **Verb Annotation:** Explain, Interpret, Describe, Clarify

- **Logical Reasoning**

  - The learner must **apply logical reasoning** to justify the sequence of operations and design choices in the program, articulating cause–effect relationships between requirements, algorithms, and observed behaviors.

  * **Bloom’s Taxonomy Alignment:** Apply  
  * **Knowledge–Skill Pairing:** Logical Reasoning / Apply  
  * **Verb Annotation:** Justify, Connect, Support, Demonstrate

- **Oral Communication**

  - The learner must **apply oral communication skills** to present the solution clearly and coherently, using appropriate technical vocabulary and responding accurately to questions during the oral assessment.

  * **Bloom’s Taxonomy Alignment:** Apply  
  * **Knowledge–Skill Pairing:** Oral Communication / Apply  
  * **Verb Annotation:** Communicate, Present, Articulate, Respond



### Disposition Specification

* **Ethical** — acknowledges authorship, avoids plagiarism, and demonstrates intellectual honesty when explaining contributions and limitations.
* **Communicative** — expresses ideas clearly and coherently, facilitating mutual understanding.
* **Responsible** — commits to accurate explanations and truthful representation of the implemented solution.



### BNCC-Aligned Competencies

**General Competency 4 – Computing (High School)**  
Produce computational artifacts considering quality, communication, and critical reflection.

**General Competency 6 – Computing (High School)**  
Express and communicate ideas clearly using computational objects and languages.

**General Competency 7 – Computing (High School)**  
Act ethically, responsibly, and with commitment to the common good.

**Specific Competencies:**

* **EM13CO19** – Present, argue, and negotiate computational solution proposals in collaborative contexts.  
* **EM13CO21** – Communicate complex ideas through computational artifacts, considering different audiences and languages.



### Summary Table for Competency CT25.20.5

| **Code** | **Competency**                                                     | **Dispositions**                    | **Knowledge**              | **Skill**                                   |
|--------|---------------------------------------------------------------------|-------------------------------------|----------------------------|---------------------------------------------|
| CT25.20.5 | **Explain and justify computational solutions with ethical authorship.** | Ethical, Communicative, Responsible | Technical Vocabulary       | **Understand (Explain, Clarify)**            |
|        |                                                                     |                                     | Logical Reasoning          | **Apply (Justify, Connect, Support)**        |
|        |                                                                     |                                     | Oral Communication         | **Apply (Present, Articulate, Respond)**     |



### Activation Definition — Competency CT25.20.5

**ActivationConstraint:** `mandatory`  
This competency is mandatory, as individual oral explanation and ethical authorship are explicit assessment requirements of TASK25.2.

**ActivationMode:** `justificatory`  
The activation is justificatory, since the primary evidence is the **oral defense of the solution**, focusing on explanation, reasoning, and accountability rather than artifact construction.

**ActivationRole:** `supporting`  
Within TASK25.2, this competency plays a supporting role, reinforcing the validity and transparency of core technical competencies by ensuring that learners can explain and ethically justify their implemented solutions.





## Competency CT25.20.6 Specification

### Competency Title

    Validate user input and enforce constraints in interactive programs.


### Textual Description

This competency involves the ability to **validate user input and enforce operational constraints** to ensure correct, safe, and consistent program behavior during interaction.

In the context of TASK25.2, the learner must detect and reject invalid inputs (e.g., out-of-range positions, already occupied cells), enforce game rules (turn alternation and state consistency), and provide clear feedback messages that guide correct user interaction. Effective input validation prevents inconsistent states and supports reliable execution from start to termination.

The competency emphasizes **systematic checking of conditions**, **state integrity**, and **responsible handling of user interaction**, ensuring that the program remains robust under erroneous or unexpected inputs.



### Knowledge Specification

- **Input Handling**

  - The learner must be able to **process and interpret user input**, converting raw input into valid internal representations and identifying malformed or unacceptable values.

  * **Bloom’s Taxonomy Alignment:** Apply  
  * **Knowledge–Skill Pairing:** Input Handling / Apply  
  * **Verb Annotation:** Read, Parse, Check, Handle

- **Conditional Structures**

  - The learner must **apply conditional logic** to validate inputs against defined constraints and rules, ensuring that only permissible actions modify program state.

  * **Bloom’s Taxonomy Alignment:** Apply  
  * **Knowledge–Skill Pairing:** Conditional Structures / Apply  
  * **Verb Annotation:** Validate, Enforce, Reject, Allow

- **State Validity**

  - The learner must ensure **state consistency**, verifying that updates preserve the integrity of the program’s data model (e.g., no overwriting of occupied positions).

  * **Bloom’s Taxonomy Alignment:** Apply  
  * **Knowledge–Skill Pairing:** State Validity / Apply  
  * **Verb Annotation:** Verify, Preserve, Maintain, Ensure



### Disposition Specification

* **Meticulous** — carefully checks input conditions and edge cases to avoid inconsistent or invalid states.
* **Responsible** — ensures reliable interaction by preventing incorrect operations and providing clear user feedback.



### BNCC-Aligned Competencies

**General Competency 1 – Computing (High School)**  
Apply computational reasoning and control structures to ensure correct and reliable solutions.

**General Competency 4 – Computing (High School)**  
Build computational artifacts with quality and robustness, considering correctness and reliability.

**Specific Competencies:**

* **EF15CO02** – Develop and simulate algorithms involving selections and repetitions.  
* **EF07CO03** – Build computational solutions by enforcing rules and constraints.  
* **EM13CO02** – Refine computational solutions from specification to implementation, including validation mechanisms.



### Summary Table for Competency CT25.20.6

| **Code** | **Competency**                                                     | **Dispositions**            | **Knowledge**            | **Skill**                          |
|--------|---------------------------------------------------------------------|-----------------------------|--------------------------|------------------------------------|
| CT25.20.6 | **Validate user input and enforce constraints in interactive programs.** | Meticulous, Responsible     | Input Handling           | **Apply (Read, Check, Handle)**    |
|        |                                                                     |                             | Conditional Structures   | **Apply (Validate, Enforce)**      |
|        |                                                                     |                             | State Validity            | **Apply (Verify, Preserve)**       |


### Activation Definition — Competency CT25.20.6

**ActivationConstraint:** `mandatory`  
This competency is mandatory, as robust input validation and constraint enforcement are essential for correct execution and fair gameplay in TASK25.2.

**ActivationMode:** `constructive`  
The activation is constructive, since learners implement validation logic and constraint checks directly within the executable program.

**ActivationRole:** `core`  
Within TASK25.2, this competency plays a core role, as enforcing valid interaction is fundamental to program correctness and user experience.




## Competency CT25.20.7 Specification

### Competency Title

    Test and debug programs using representative scenarios and edge cases.



### Textual Description

This competency involves the ability to **systematically test and debug programs** in order to identify, analyze, and correct logical or runtime errors.

In the context of TASK25.2, the learner must execute the program under **representative scenarios**—including valid matches, invalid inputs, victory configurations (rows, columns, diagonals), and draw situations—to verify correctness and robustness. When unexpected behavior occurs, the learner analyzes execution flow, inspects program state, and applies debugging strategies to locate and resolve fault causes.

The competency emphasizes **reasoned fault analysis**, **iterative refinement**, and **careful tracing of execution**, supporting the development of reliable and well-tested computational solutions.



### Knowledge Specification

- **Testing Notions**

  - The learner must be able to **apply basic testing concepts**, selecting representative scenarios and edge cases that exercise different execution paths and validate expected outcomes.

  * **Bloom’s Taxonomy Alignment:** Apply  
  * **Knowledge–Skill Pairing:** Testing / Apply  
  * **Verb Annotation:** Test, Verify, Check, Execute

- **Debugging Strategies**

  - The learner must apply **debugging strategies** to locate errors, such as inspecting variable values, isolating faulty conditions, and incrementally refining code.

  * **Bloom’s Taxonomy Alignment:** Apply  
  * **Knowledge–Skill Pairing:** Debugging / Apply  
  * **Verb Annotation:** Debug, Fix, Adjust, Refine

- **Execution Trace Analysis**

  - The learner must **analyze execution traces** to understand program behavior step by step, identifying inconsistencies between expected and observed results.

  * **Bloom’s Taxonomy Alignment:** Analyze  
  * **Knowledge–Skill Pairing:** Execution Tracing / Analyze  
  * **Verb Annotation:** Trace, Analyze, Diagnose, Identify


### Disposition Specification

* **Persistent** — demonstrates perseverance when investigating faults, iteratively refining the solution until correct behavior is achieved.
* **Meticulous** — carefully examines execution details and edge cases to avoid overlooking subtle errors.



### BNCC-Aligned Competencies

**General Competency 1 – Computing (High School)**  
Apply computational reasoning to verify, test, and improve solutions.

**General Competency 4 – Computing (High School)**  
Build reliable computational artifacts through systematic testing and refinement.

**Specific Competencies:**

* **EF15CO02** – Develop and simulate algorithms, validating their behavior.  
* **EF07CO03** – Build computational solutions through testing and correction.  
* **EM13CO02** – Refine computational solutions through analysis, testing, and debugging.



### Summary Table for Competency CT25.20.7

| **Code** | **Competency**                                                       | **Dispositions**        | **Knowledge**              | **Skill**                                   |
|--------|-----------------------------------------------------------------------|-------------------------|----------------------------|---------------------------------------------|
| CT25.20.7 | **Test and debug programs using representative scenarios and edge cases.** | Persistent, Meticulous | Testing Notions            | **Apply (Test, Verify, Execute)**            |
|        |                                                                       |                         | Debugging Strategies       | **Apply (Debug, Fix, Refine)**               |
|        |                                                                       |                         | Execution Trace Analysis   | **Analyze (Trace, Diagnose, Identify)**      |



### Activation Definition — Competency CT25.20.7

**ActivationConstraint:** `mandatory`  
This competency is mandatory, as systematic testing and debugging are required to ensure correctness and robustness of the implemented program.

**ActivationMode:** `analytical`  
The activation is predominantly analytical, since learners examine execution behavior, trace logic paths, and reason about fault causes before applying corrections.

**ActivationRole:** `core`  
Within TASK25.2, this competency plays a core role, directly supporting program correctness and providing explicit alignment with **Learning Objective LO6**.
