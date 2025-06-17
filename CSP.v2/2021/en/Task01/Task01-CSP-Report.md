# Competency Specification Report: Task01 - The Vending Machine for Sodas and Snacks

## Introduction

Building on the general structure defined in the CSP methodology, this report presents the application of the **Competency Specification Process** to the **Task1 – The Vending Machine for Sodas and Snacks**, a Problem-Based Learning (PBL) scenario that explores the use of **finite automata and regular expressions** in the design of vending machine software and hardware solutions.

## 1. Task Description Analysis

The PBL task titled **"The Vending Machine for Sodas and Snacks"** presents a problem related to **change calculation in vending machine transactions**, where payments are made using coins and banknotes. The task requires students to design a solution that enables the vending machine to accept payments, dispense change accurately, and operate according to predefined functional requirements.

To successfully address this problem, students must demonstrate their ability to:
- **Apply finite automata** concepts to model the vending machine’s behavior.
- **Simulate and validate** the automaton’s functionality using computational tools.
- **Document the development process** in a structured and technical manner.

This task not only assesses students’ understanding of **automata theory** but also evaluates their ability to:
1. **Analyze real-world constraints** and translate them into a formal computational model.
2. **Design and implement** an automaton that meets functional requirements.
3. **Justify and explain** design decisions through a well-structured technical report.

Additionally, the task introduces an optional challenge: implementing a **randomized bonus change feature**, where the vending machine occasionally provides an extra R$1.00 when the exact product price is paid. This adds a **stochastic element** to the system, encouraging students to consider **probabilistic behaviors** within their automaton design.

Through this structured **Problem-Based Learning (PBL) scenario**, students engage with a **real-world problem**, bridging theoretical knowledge with **practical computational modeling**, simulation, and technical documentation.


## 2. Knowledge Enumeration

To systematically enumerate the computing knowledge required for this task, the **ACM Computing Classification System (2012)** was used as a controlled vocabulary. This classification system is widely recognized and globally adopted, ensuring standardization and consistency in the categorization of computing knowledge.  

For **professional knowledge (FPK)**, we referenced the **ACM Computing Curriculum (CC) 2020**, which provides a structured framework for essential professional competencies.  

Based on the **task description**, the following set of required knowledge components was identified:  

### **Computing Knowledge**  
- **Automata over Infinite Objects**  
  - Involves the study and application of mathematical models that describe computational systems using **states and transitions**.  
  - Essential for designing **state-based vending machine logic**.  

- **Nondeterministic Finite Automata (NFA)**
  - Represents a class of automata that allows multiple possible transitions for a given input from a state.
  - Important for understanding the expressive power and design flexibility of regular language recognizers.
  - Provides foundational knowledge for modeling compact and versatile state machines, which may later be converted to deterministic forms for implementation.

- **Regular Languages (Regular Expressions)**  
  - Requires understanding and applying **formal techniques** to represent and manipulate string sets.  
  - Used primarily in **text processing, lexical analysis, and pattern matching** within the vending machine’s operational logic.  

- **Requirements Analysis**  
  - A systematic process for **collecting, analyzing, and specifying system requirements**.  
  - Ensures that **user needs and system expectations** are clearly understood and documented.  

- **Simulation Tools**  
  - Involves the use of **automata simulation tools** (such as JFLAP) to validate and analyze **proposed solutions**.  
  - Enables **testing, debugging, and refining** the vending machine’s automaton before implementation.  

### **Professional Knowledge (FPK)**  
- **Analytical and Critical Thinking**  
  - The ability to **break down complex problems into fundamental components**, evaluate results, and make well-reasoned decisions based on rigorous analysis.  

- **Problem Solving and Troubleshooting**  
  - Requires identifying, analyzing, and resolving **task-specific challenges** using **effective strategies and computational methods** to develop optimal solutions.  

- **Written Communication**  
  - The ability to **compose clear and structured technical reports** detailing the design, implementation, and validation processes.  
  - Ensures that findings and decisions are effectively communicated to stakeholders.  

This **knowledge enumeration** serves as the foundation for competency specification, ensuring that students acquire both **theoretical and practical expertise** necessary to complete the task successfully.


## 3. Learning Objectives Identification

The **general objective** of this task is to develop **finite automata and regular expressions** to solve **real-world problems** by modeling a vending machine system. This objective emphasizes the practical application of **automata theory** in computational problem-solving.

### **Specific Learning Objectives**
To achieve this general objective, students must demonstrate the ability to:

1. **Identify system functionalities**  
   - Analyze the user’s conceptual model of the vending machine and define its expected behaviors.

2. **Align user requirements with automaton functionalities**  
   - Reconcile the vending machine's desired functionalities with the constraints and capabilities of the automaton being developed.

3. **Evaluate the role of non-determinism in finite automata**  
   - Assess when and how **non-deterministic finite automata (NFA)** can be used effectively in the system’s design.

4. **Understand equivalences between deterministic and non-deterministic automata**  
   - Demonstrate an understanding of the equivalence between **Deterministic Finite Automata (DFA)** and **Non-Deterministic Finite Automata (NFA)**, highlighting scenarios where one might be preferable over the other.

5. **Understand the equivalence between Finite Automata (FA) and Regular Expressions (RE)**  
   - Establish connections between **finite automata representations** and **regular expressions**, reinforcing their theoretical and practical interchangeability.

6. **Apply FA-to-RE equivalence in the development of regular expressions**  
   - Utilize existing finite automata to derive **corresponding regular expressions**, applying formal methods to convert automata into equivalent regex patterns.

7. **Associate vending machine options, coins, and banknotes with alphabet symbols**  
   - Map real-world elements of the vending machine (such as product selections and payment methods) onto the **formal alphabet** used in automaton design.

8. **Develop technical reports**  
   - Document the **design, implementation, and validation** of the automaton, ensuring clarity and precision in technical writing.

9. **Use finite automata simulation tools**  
   - Apply tools such as **JFLAP** to simulate, analyze, and verify the functionality of the designed automaton.

### **Importance of These Objectives**
These learning objectives provide a **structured pathway** for competency development, ensuring that students acquire:
- **A strong theoretical foundation** in automata and formal languages.
- **The ability to bridge theory and practice**, applying formal methods to solve computational problems.
- **Hands-on experience with simulation tools**, reinforcing practical problem-solving skills.
- **Technical communication skills**, essential for conveying solutions in professional and academic contexts.

By achieving these objectives, students will be equipped with both the **computational and analytical skills** necessary for modeling real-world systems using **finite automata and regular expressions**.


## 4. Competency Definition

Competencies are specified based on the **Learning Objectives (LOs)** identified in the task analysis.

### 4.1 Competency A Specification  

### A.1 Competency Title
    Designing Efficient Solutions with Automata

### A.2 Textual Description  

This competency involves the ability to design and implement **functional, optimized solutions** using **finite automata** as a formal computational model. It requires a **solid understanding of automata theory**, enabling students to interpret system requirements, translate them into formal specifications, and construct automata that are both **logically correct and technically feasible**.

Learners must demonstrate the capacity to **model system behavior** through state transitions, taking into account both **explicit functional requirements** and potential operational constraints. The competency also entails the ability to **validate and refine the automaton** through simulation and systematic testing, ensuring that it performs accurately across expected scenarios.

Furthermore, it includes the flexibility to incorporate **additional constraints or extensions**, reflecting a capacity for **adaptive problem-solving** and the integration of complex conditions into formal models. This ensures readiness for applying finite automata in a variety of real-world computational tasks.



### A.3 Knowledge Specification
The following knowledge areas are critical for this competency:  

- **Automata over Infinite Objects**  
  - Fundamental for modeling the vending machine’s operational logic.  
  - Involves designing states and transitions to represent system functionalities.  

- **Requirements Analysis**  
  - Ensures an accurate **identification and documentation of system requirements**.  
  - Bridges user needs with the technical capabilities of finite automata.  

- **Analytical and Critical Thinking (FPK)**  
  - Required for **problem decomposition and strategic planning**.  
  - Helps in aligning user requirements with technical feasibility while optimizing computational resources.  


### A.4 Disposition Specification
The **"Vending Machine for Sodas and Snacks"** task highlights key behavioral attributes necessary for problem-solving and effective team collaboration. These include:  

 **Collaboration**  
- The task follows the **Problem-Based Learning (PBL) methodology**, requiring continuous team interaction.  
- Essential for developing solutions collaboratively through **PBL whiteboard sessions**, maintaining the **logbook**, and **documenting each project phase**.  
- Encourages **knowledge-sharing** and iterative improvements.  

 **Responsibility**  
- Ensures adherence to **project deadlines**, accurate **documentation**, and a **functional automaton design**.  
- Requires individual accountability for contributions, ensuring that the **final deliverable meets user expectations** and project standards.  

 **Proactivity**  
- Encourages anticipating challenges, such as the **randomized bonus change feature (R$1.00 extra)**, which requires **additional research and technical adjustments**.  
- Involves actively seeking knowledge, including the **relationship between regular expressions and finite automata**.  
- Supports a proactive approach to debugging, refining, and improving the system.  

 **Creativity**  
- Necessary for adapting automata **functionalities to specific user requirements**.  
- Encourages exploring **alternative implementations**, such as incorporating **randomized elements** in automata behavior.  
- Enhances **technical documentation**, making system operations visually and conceptually engaging.  


### A.5 Knowledge-Skill Pairing

This step maps **knowledge areas to the corresponding skills** required to successfully demonstrate competency in this task.  

**A.5.1 Mapping Knowledge to Skills**  
To achieve this competency, students must demonstrate the ability to:  

- **Apply** Analytical and Critical Thinking along with knowledge of **Automata over Infinite Objects** to **solve the vending machine’s change calculation problem**.  
- **Identify and interpret** system requirements, demonstrating proficiency in **Requirements Analysis**.  


**A.5.2 Bloom’s Taxonomy Alignment**  
To ensure a structured and progressive learning approach, each knowledge component is aligned with Bloom’s Revised Taxonomy, providing a clear framework for competency assessment.

- **Analytical and Critical Thinking (FPK) – Apply**  
  - Assesses the student's ability to **decompose complex problems** into fundamental components.  
  - Evaluates the ability to **analyze relationships, identify patterns, and formulate logical strategies** for problem-solving.  
  - Ensures students can effectively **bridge theoretical knowledge with practical implementation**.  

- **Automata over Infinite Objects – Apply**  
  - Measures the student's capability to **design and implement automata-based solutions** for a defined problem.  
  - Assesses the ability to **translate real-world system constraints into automata models** using states and transitions.  
  - Ensures that students can effectively **apply computational modeling techniques** to solve vending machine transaction issues.  

- **Requirements Analysis – Apply**  
  - Evaluates the student's ability to interpret and translate system constraints and user requirements into formal specifications.
  - Assesses the capacity to apply structured analysis techniques in identifying functional and non-functional requirements.
  - Ensures students can logically organize and integrate requirements into a coherent computational model.




**A.5.3 Verb Annotation**  
To provide clarity on competency expectations, the following verb annotations define the required actions:  

- **Create** → Automata over Infinite Objects → **Construct, Develop, Design** a functional automaton that satisfies computational constraints.
- **Apply** → Requirements Analysis → **Interpret, Implement, Organize** structured system requirements into a computational framework. 




### A.6 Summary Table for Competency A

| **Competency** | **Dispositions** | **Knowledge** | **Skill** |
|------------|-----------|------------|----|
|  |   | Automata over Infinite Objects | **Apply (Construct, Develop, Design)** |
| **Develop problem solutions using Automata** | Collaborative, Responsible, Proactive, Creative | Requirements Analysis | **Apply (Interpret, Implement, Organize)** |
| | | Analytical and Critical Thinking (FPK) | **Apply** |




### **4.2 Competency B Specification**

### B.1 Competency Title  
    Determining When to Use Deterministic Finite Automata (DFA)  

### B.2 Competency Description  
This competency focuses on **understanding determinism in finite automata** and **determining when to apply non-determinism**. Students must analyze system constraints and **decide whether a deterministic or non-deterministic automaton** is the optimal choice for solving a given problem.

This competency requires the ability to:  
- **Differentiate deterministic and non-deterministic automata** based on their properties and practical applications.  
- **Assess problem requirements** to determine the most efficient automaton model.  
- **Justify the choice** of automaton type with logical reasoning and computational constraints.



### B.3 Knowledge Specification  
The following knowledge areas are essential for this competency:  

- **Automata over Infinite Objects**  
  - Understanding the characteristics, limitations, and applications of **deterministic vs. non-deterministic models**.  
  - Identifying scenarios where one model may be more advantageous than the other.  

- **Analytical and Critical Thinking (FPK)**  
  - Required for **evaluating system constraints and making informed decisions**.  
  - Enables students to develop **strategic reasoning** when choosing between DFA and NFA models.  



### B.4 Disposition Specification  
Similar to **Competency A**, this competency requires students to demonstrate key **behavioral attributes** that facilitate problem-solving and decision-making:  

- **Investigative Thinking** – Encourages curiosity and **critical analysis** of automaton properties and their applications.  
- **Collaboration** – Supports teamwork when discussing and justifying DFA vs. NFA choices.  
- **Responsibility** – Ensures logical consistency and accuracy in decision-making.  
- **Proactivity** – Promotes independent research and exploration of automata applications.  
- **Creativity** – Encourages innovative approaches to problem-solving when dealing with complex system constraints.  



### B.5 Knowledge-Skill Pairing  
This step pairs **knowledge areas with the corresponding skills** required to demonstrate competency.

 **B.5.1 Mapping Knowledge to Skills**  
To achieve this competency, students must demonstrate the ability to:  
- **Apply** Analytical and Critical Thinking to **differentiate deterministic and non-deterministic automata**.  
- **Understand** Automata over Infinite Objects to **correctly identify scenarios where a deterministic or non-deterministic automaton is more appropriate**.  



**B.5.2 Bloom’s Taxonomy Alignment**  

To accurately assess the required skills for this competency, each knowledge component is aligned with **Bloom’s Revised Taxonomy**, ensuring a structured learning progression and appropriate cognitive challenge.  

- **Analytical and Critical Thinking (FPK) – Apply**  
  - Assesses the student's ability to **evaluate problem constraints and justify the choice** between **Deterministic Finite Automata (DFA) and Non-Deterministic Finite Automata (NFA)**.  
  - Requires the ability to **analyze the differences between DFA and NFA** and determine which model is **more suitable for a given problem scenario**.  
  - Ensures students can **logically argue their decisions** based on **computational efficiency, implementation complexity, and system constraints**.  

- **Automata over Infinite Objects (DFA/NFA) – Understand**  
  - Evaluates the student's **ability to differentiate and classify** deterministic and non-deterministic automata based on their properties.  
  - Requires the ability to **correctly identify when each type of automaton should be used**, recognizing their advantages and limitations.  
  - Ensures students develop **a conceptual understanding of the relationship between DFA, NFA, and problem constraints**, forming a solid foundation for decision-making.  


 **B.5.3 Verb Annotation**  
- **Understand** → Automata over Infinite Objects → **Compare** DFA and NFA concepts.  
- **Apply** → Analytical and Critical Thinking → **Evaluate and decide** on the appropriate automaton model.  



### B.6 Summary Table for Competency B  

| **Competency** | **Dispositions** | **Knowledge** | **Skill** |
|---------------|-----------------|--------------|-----------|
| **Determine when to use a DFA or NFA** | **Investigative, Collaborative, Responsible, Proactive, Creative** | **Automata over Infinite Objects** | **Understand (Compare)** |
| | | **Analytical and Critical Thinking (FPK)** | **Apply (Evaluate, Decide)** |



### **4.3 Competency C Specification**

### C.1 Competency Title  
    Test Automata Using Simulators

### C.2 Competency Description
This competency refers to the ability to simulate and evaluate the behavior of computational models—such as Finite Automata, Pushdown Automata, and Turing Machines—using specialized tools like JFLAP or equivalent. It ensures that students can test automata-based solutions for correctness, completeness, and alignment with formal specifications.

This competency requires learners to demonstrate the ability to:

* **Utilize simulation tools effectively** to test and validate the functionality of computational automata (e.g., Finite Automata, Pushdown Automata, Turing Machines).
* **Interpret and evaluate automaton behavior** by comparing simulated outputs with expected outcomes based on formal specifications.
* **Diagnose and correct design flaws** through systematic debugging and iterative refinement.
* **Apply structured problem-solving approaches** to enhance the accuracy, efficiency, and robustness of the automaton model.



### C.3 Knowledge Specification  
The following knowledge areas are essential for this competency:  

- **Automata over Infinite Objects**  
  - Understanding automata behavior in simulated environments.  
  - Using computational tools to test automaton properties and validate their execution.  

- **Problem Solving and Troubleshooting (FPK)**  
  - Required for **diagnosing and resolving errors** in automaton simulations.  
  - Enables students to refine models iteratively, ensuring accuracy and robustness.  



### C.4 Disposition Specification  
Similar to **previous competencies**, this competency requires students to demonstrate essential **behavioral attributes** that facilitate testing, debugging, and improving automata:  

- **Collaboration** – Encourages teamwork in analyzing automaton behavior and discussing debugging strategies.  
- **Responsibility** – Ensures **methodical testing**, documentation of issues, and refinement of automaton designs.  
- **Proactivity** – Promotes initiative in identifying weaknesses in automaton models and applying fixes.  
- **Creativity** – Supports innovation in **troubleshooting techniques** and **experimenting with different simulation approaches**.  



### C.5 Knowledge-Skill Pairing  
This step maps **knowledge areas with the corresponding skills** required to demonstrate competency.

 **C.5.1 Mapping Knowledge to Skills**  
To achieve this competency, students must demonstrate the ability to:  
- **Apply** Automata over Infinite Objects to **simulate and validate the designed automaton**.  
- **Apply** Problem Solving and Troubleshooting (FPK) to **identify and resolve errors during simulation**.  



**C.5.2 Bloom’s Taxonomy Alignment**  

The **knowledge areas** required for this competency are aligned with **Bloom’s Revised Taxonomy**, ensuring a structured learning process that progresses from understanding concepts to applying them in practical scenarios.  

Students must **apply** their knowledge of **Automata over Infinite Objects** by experimenting with, relating, and simulating automata to validate system behavior. This ensures they can effectively **execute, test, and analyze automaton simulations**, verifying their correctness and identifying areas for improvement.  

Similarly, students are expected to **apply** **Problem Solving and Troubleshooting (FPK)** by diagnosing and correcting errors in automaton design during simulation. This involves **identifying, debugging, and optimizing automaton behavior** based on the results of the simulations, ensuring that the system functions as expected.  

By demonstrating proficiency in both areas, students will develop essential problem-solving skills that allow them to refine computational models iteratively.  


**C.5.3 Verb Annotation**  

To clarify the expected learning outcomes, the following verb annotations define the key actions students must demonstrate:  

- **Apply** knowledge of Automata over Infinite Objects to **experiment with, relate, and simulate** automata.  
- **Apply** Problem Solving and Troubleshooting → Diagnose, Debug, Refine automaton simulations. 


### **C.6 Summary Table for Competency C**  

| **Competency** | **Dispositions** | **Knowledge** | **Skill** |
|---------------|-----------------|--------------|-----------|
| **Testing Automata Using Simulators** | **Collaborative, Responsible, Proactive, Creative** | **Automata over Infinite Objects** | **Apply (Experiment, Relate, Simulate)** |
| | | **Problem Solving and Troubleshooting (FPK)** | **Apply (Diagnose, Debug, Refine)** |



### **4.4 Competency D Specification**  

### D.1 Competency Title
    Determining Regular Expressions that Represent Automata

### D.2 Competency Description
This competency focuses on the ability to **represent finite automata using regular expressions**. Students must demonstrate proficiency in translating **state-based computational models** into equivalent **formal language representations**, ensuring that the generated regular expressions accurately describe the automaton’s behavior.  

To achieve this, students will:  
- **Understand the relationship between finite automata and regular expressions**, ensuring correct transformation between models.  
- **Apply formal language concepts** to construct appropriate regular expressions.  
- **Test and refine** regular expressions to verify their correctness.  


### D.3 Knowledge Specification
The following knowledge areas are essential for this competency:  

- **Automata over Infinite Objects** - Provides foundational knowledge on automaton structure and behavior, serving as a prerequisite for expressing automata through regular languages.  
- **Regular Languages** - Covers formal methods for defining and manipulating sets of strings using **regular expressions**, ensuring students can construct **accurate representations** of automata.  
- **Problem Solving and Troubleshooting (FPK)** - Develops the ability to **identify, analyze, and correct errors** in the **transformation process from automata to regular expressions**.  


### D.4 Disposition Specification  
As with previous competencies, **behavioral attributes** play a crucial role in successfully completing this task:  

- **Investigative Thinking** – Encourages exploration of alternative approaches to defining **equivalent regular expressions** for automata.  
- **Collaboration** - Supports teamwork in testing and validating regular expressions through peer review.  
- **Responsibility** - Ensures accuracy in formal representations and adherence to theoretical principles.  
- **Proactivity** - Promotes initiative in refining and optimizing regular expressions for efficiency.  
- **Creativity** - Encourages innovative techniques for minimizing and restructuring regular expressions while maintaining correctness.  



### D.5 Knowledge-Skill Pairing
This step pairs **knowledge areas with corresponding skills**, ensuring that students develop both **theoretical understanding** and **practical application**.  

**D.5.1 Mapping Knowledge to Skills**  
To demonstrate this competency, students must be able to:  
- **Understand** Automata over Infinite Objects to correctly **decompose** state-based systems into formal language representations.  
- **Apply** knowledge of Regular Languages to **construct regular expressions that accurately represent finite automata**.  
- **Apply** Problem Solving and Troubleshooting (FPK) to **test and refine regular expressions**, ensuring correctness and completeness.  


**D.5.2 Bloom’s Taxonomy Alignment**  
The skills required for this competency align with **Bloom’s Revised Taxonomy**, ensuring a structured learning approach:  

- **Understanding Automata over Infinite Objects** is essential, as **comprehension of automaton structure is a prerequisite** for correctly translating it into a regular expression.  
- **Applying Regular Languages** is necessary because students must **construct regular expressions that accurately model automaton behavior**, demonstrating proficiency in formal language representation.  
- **Applying Problem Solving and Troubleshooting** ensures students can **validate, test, and refine their regular expressions**, identifying and correcting errors to guarantee that the expressions truly represent the associated automata.  

By mastering these skills, students gain **a deep understanding of formal language transformations**, enhancing their ability to work with **computational models and theoretical foundations** of automata.  



**D.5.3 Verb Annotation**  
To clarify expected learning outcomes, the following action verbs define key student activities:  

- **Understand** → Automata over Infinite Objects → **Decompose** automata into equivalent language representations.  
- **Apply** → Regular Languages → **Construct, Model, Express** automata using regular expressions.  
- **Apply** → Problem Solving and Troubleshooting → **Validate, Test, Refine** regular expressions to ensure accuracy.  


### D.6 Summary Table for Competency D

| **Competency** | **Dispositions** | **Knowledge** | **Skill** |
|---------------|-----------------|--------------|-----------|
|  |  | **Automata over Infinite Objects** | **Understand** |
| **Determining Regular Expressions that Represent Automata** | Investigative, Collaborative, Responsible, Proactive, Creative | **Regular Languages** | **Apply** |
| | | **Problem Solving and Troubleshooting (FPK)** | **Apply** |




### **4.5 Competency E Specification**  

### E.1 Competency Title
    Relating Regular Expressions to Finite Automata

### E.2 Competency Description
This competency focuses on the ability to **establish the relationship between finite automata and regular expressions**.  

Students must demonstrate an understanding of how **finite automata can be represented using regular expressions** and vice versa, ensuring they can accurately transition between these two formal models.  

To achieve this, students will:  
- **Analyze the structural equivalence between finite automata and regular expressions**.  
- **Identify the corresponding regular expression for a given finite automaton**.  
- **Demonstrate comprehension of regular language properties** that connect these two representations.  


### E.3 Knowledge Specification
The following knowledge areas are essential for this competency:  

- **Automata over Infinite Objects** – Provides the theoretical foundation to **analyze and understand finite automata** and their structure.  
- **Regular Languages** – Covers the principles of **formal language representations**, ensuring students can establish equivalences between finite automata and regular expressions.  


### E.4 Disposotion Specification
To successfully achieve this competency, students must demonstrate key **behavioral attributes**, including:  

- **Collaboration** – Engaging with peers to analyze different automata and their equivalent regular expressions.  
- **Responsibility** – Ensuring accuracy in the identification of equivalences between formal models.  
- **Proactivity** – Actively seeking multiple approaches to relate regular expressions and automata representations.  



### E.5 Knowledge-Skill Pairing 
This step maps **knowledge areas with corresponding skills**, ensuring a structured learning approach.

**E.5.1 Mapping Knowledge to Skills**  
To demonstrate this competency, students must be able to:  
- **Understand** Automata over Infinite Objects to correctly **analyze finite automata structures** and their transformation into regular expressions.  
- **Understand** Regular Languages to **identify the equivalent regular expression for a given finite automaton**.  


**E.5.2 Bloom’s Taxonomy Alignment**  
The knowledge areas required for this competency align with **Bloom’s Revised Taxonomy** at the **"Understand" level**, ensuring students:  
- **Recognize and interpret** the relationship between **finite automata and regular expressions**.  
- **Identify and classify** equivalent representations within **formal language theory**.  

By achieving this level of comprehension, students develop a **solid conceptual foundation**, allowing them to apply this knowledge in more complex problem-solving scenarios.  


**E.5.3 Verb Annotation**  
To clarify expected learning outcomes, the following action verbs define key student activities:  

- **Understand** → Automata over Infinite Objects → **Interpret** automaton structures and their equivalence to regular expressions.  
- **Understand** → Regular Languages → **Identify, Classify** corresponding regular expressions for given automata.  


### E.6 Summary Table for Competency E

| **Competency** | **Dispositions** | **Knowledge** | **Skill** |
|---------------|-----------------|--------------|-----------|
| **Relating Regular Expressions to Finite Automata** | Collaborative, Responsible, Proactive | **Automata over Infinite Objects** | **Understand** |
| | | **Regular Languages** | **Understand** |




### **4.6 Competency F Specification**  

### F.1 Competency Title
    Collaborative Technical Report Writing

### F.2 Competency Description
This competency focuses on the ability to **collaboratively produce a well-structured technical report**. It requires students to **apply technical writing principles** to synthesize findings, explain methodologies, and document results in a clear, logical, and professional manner.  

To achieve this, students must:  
- **Write a structured and coherent report**, integrating contributions from multiple team members.  
- **Apply professional technical writing standards**, ensuring clarity, consistency, and logical flow.  
- **Effectively communicate technical findings**, making complex concepts accessible to both technical and non-technical audiences.  
- **Revise and refine content**, ensuring accuracy, readability, and adherence to formatting guidelines.  

This competency emphasizes **practical application of writing skills**, requiring students to produce a polished and well-organized document that reflects their collective expertise.  


### F.3 Knowledge Specification
The following knowledge area is essential for this competency:  

- **Written Communication (FPK)** – Involves the ability to **apply structured writing techniques** to explain and document the solution process effectively.  


### F.4 Disposition Specification**  
To successfully achieve this competency, students must demonstrate key **behavioral attributes**, including:  

- **Collaboration** – Working effectively as a team to create a unified, well-organized document.  
- **Meticulousness** – Ensuring accuracy, clarity, and consistency in the report’s content and structure.  
- **Responsibility** – Taking ownership of assigned sections and contributing meaningfully to the final report.  



### F.5 Knowledge-Skill Pairing
This step maps **knowledge areas with corresponding skills**, ensuring a structured learning approach.

**F.5.1 Mapping Knowledge to Skills**  
To demonstrate this competency, students must be able to:  
- **Apply** Written Communication (FPK) to **write, structure, and refine a technical report**, effectively explaining the solution process.  



**F.5.2 Bloom’s Taxonomy Alignment**  
The **"Apply" level** of **Bloom’s Taxonomy** is the most appropriate for this competency because it requires students to:  
- **Use technical writing skills in practice**.  
- **Synthesize and communicate findings effectively**, ensuring clarity and coherence.  
- **Format, revise, and refine** the document to meet professional standards.  

By mastering this competency, students develop **practical writing skills essential for professional and academic communication**.  



**F.5.3 Verb Annotation**  
To clarify expected learning outcomes, the following action verbs define key student activities:  

- **Apply** → Written Communication (FPK) → **Write, Structure, Revise, Refine** technical documentation.  


### F.6 Summary Table for Competency F

| **Competency** | **Dispositions** | **Knowledge** | **Skill** |
|---------------|-----------------|--------------|-----------|
| **Collaborative Technical Report Writing** | Collaborative, Meticulous, Responsible | **Written Communication (FPK)** | **Apply (Write, Structure, Revise, Refine)** |

---

## Table of Competencies for Task: *The Vending Machine for Sodas and Snacks*

| **Competency** | **Dispositions** | **Knowledge** | **Skill** |
|----------------|------------------|---------------|-----------|
| **Develop problem solutions using Automata** | Collaborative, Responsible, Proactive, Creative | Automata over Infinite Objects | Apply (Construct, Develop, Design) |
|  |  | Requirements Analysis | Apply (Interpret, Implement, Organize) |
|  |  | Analytical and Critical Thinking (FPK) | Apply |
|  |  |                                        |       |       
| **Determine when to use a DFA or NFA** | Investigative, Collaborative, Responsible, Proactive, Creative | Automata over Infinite Objects | Understand (Compare) |
|  |  | Analytical and Critical Thinking (FPK) | Apply (Evaluate, Decide) |
|  |  |                                        |       | 
| **Testing Automata Using Simulators** | Collaborative, Responsible, Proactive, Creative | Automata over Infinite Objects | Apply (Experiment, Relate, Simulate) |
|  |  | Problem Solving and Troubleshooting (FPK) | Apply (Diagnose, Debug, Refine) |
|  |  |                                        |       | 
| **Determining Regular Expressions that Represent Automata** | Investigative, Collaborative, Responsible, Proactive, Creative | Automata over Infinite Objects | Understand |
|  |  | Regular Languages | Apply |
|  |  | Problem Solving and Troubleshooting (FPK) | Apply |
|  |  |                                        |       | 
| **Relating Regular Expressions to Finite Automata** | Collaborative, Responsible, Proactive | Automata over Infinite Objects | Understand |
|  |  | Regular Languages | Understand |
|  |  |                                        |       | 
| **Collaborative Technical Report Writing** | Collaborative, Meticulous, Responsible | Written Communication (FPK) | Apply (Write, Structure, Revise, Refine) |
