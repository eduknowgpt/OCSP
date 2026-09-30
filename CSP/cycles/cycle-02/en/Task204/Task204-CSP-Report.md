# Competency Specification Report: Task204 – Online Judges at Logistic Solutions

Team Members: Lais Salvador, Edeyson A. Gomes, Luiz Gavaza  
Contributors: Jéssica Santana, Otávio Neto, Roberta Oliveira  

## 1. Task Description Analysis

Task204 investigates the operational logic of Online Judge (OJ) systems used to evaluate algorithmic solutions submitted by programmers. The task is grounded in a real scenario observed during programming marathon training at a startup, where repeated submissions for a Traveling Salesman Problem (TSP) instance resulted in TLE (Time Limit Exceeded) outcomes.

The task challenges students to:

- Analyze the computational characteristics of the TSP and justify its algorithmic difficulty.
- Explain why no general algorithm can decide termination for every arbitrary program and input, and how this limitation relates to an OJ.
- Construct a Finite State Machine (FSM) that externalizes the observable behavior of the OJ across outcomes such as AC, WA, TLE, CE, and RE.
- Relate the practical limitations of automated evaluation systems to fundamental concepts from Computation Theory, particularly undecidability and the Halting Problem, and to complexity-related considerations such as NP-completeness.

Within the instructional scope of this task, the FSM serves as a behavioral model of system outcomes, enabling students to represent observable execution states while recognizing that the underlying computational limitations arise from theoretical properties of computation rather than from implementation details.

The expected deliverables include an SBC-format technical report containing: team hypotheses and analysis of the TSP scenario, responses to business-oriented questions regarding system behavior and limitations, and a formally modeled FSM accompanied by explanations of the system’s theoretical constraints.

## 2. Knowledge Enumeration

To fulfill the task objectives, students are expected to mobilize the following knowledge areas, organized according to their functional role within the task:

### Core Theoretical Knowledge

The decision version of TSP is NP-complete; the optimization version is NP-hard. This classification does not by itself explain an individual TLE result, which depends on the algorithm, input, implementation, and time limit. A timeout establishes that the limit was exceeded, not that execution would continue forever. Undecidability concerns a general termination procedure for arbitrary programs and inputs; it does not exclude conclusions about particular programs. These distinctions follow the standard treatments of [computability](https://www.cs.cornell.edu/courses/cs4820/2019sp/handouts/computability.pdf) and [TSP complexity](https://www.cs.cornell.edu/courses/cs6820/2020fa/handouts/Kozen_21-24.pdf).

- Halting Problem  
  Understanding the undecidability of program termination and its implications for automated evaluation systems.

- Computational Complexity (P, NP, NP-Complete Problems)  
  Understanding the decision and optimization formulations of TSP and examining complexity alongside input size, implementation, and execution limits when explaining TLE.

### Supporting Formal Knowledge

- Finite State Machines (FSM)  
  Modeling observable system behavior and representing evaluation outcomes through formal state transitions.

- Chomsky Hierarchy  
  Positioning computational models within a broader theoretical framework to support reasoning about expressive limitations.

- Turing Machines and Universal Turing Machines  
  Understanding Turing Machines as reference models for computability, supporting conceptual reasoning about undecidability rather than requiring construction or simulation.

- Recursively Enumerable Languages  
  Interpreting acceptance and semi-decidability in relation to program execution and termination behavior.

### Supporting Technical and Transversal Knowledge

- Formal Modeling and Simulation (JFLAP)  
  Implementing and validating FSM representations of system behavior.

- Written Technical Communication  
  Producing structured documentation that explains modeling decisions, theoretical justification, and system limitations.

- Analytical and Critical Thinking  
  Supporting reasoning about computational limits, model adequacy, and interpretation of system behavior.

## 3. Learning Objectives and Expected Outcomes

Upon completion of this task, students are expected to demonstrate the following learning outcomes:

1. Explain the limitations of automated program evaluation, particularly the impossibility of a general termination decision for arbitrary programs and inputs, based on the Halting Problem and the theoretical limits of computation.

2. Analyze the Traveling Salesman Problem (TSP) in the context of computational complexity, distinguishing its decision and optimization formulations and examining possible causes of Time Limit Exceeded (TLE).

3. Model and simulate the observable behavior of Online Judge systems using Finite State Machines (FSMs), representing evaluation outcomes and system responses without assuming full knowledge of program execution.

4. Discuss the limits of automation in program evaluation, relating practical system behavior to foundational concepts from Computation Theory, including undecidability and expressive limitations of computational models.

5. Relate real-world evaluation systems to core concepts in Computation Theory, integrating theoretical reasoning with practical system analysis.

6. Produce a well-structured technical report in SBC format, clearly documenting problem analysis, modeling decisions, theoretical justification, and examples supporting the proposed explanations.

## 4. Competency Specification

The TSP and complexity analysis remains an explicit task objective. The selected set below does not contain a separately specified complexity competency; therefore, this mapping is not presented as exhaustive coverage of every learning objective. No additional competency is introduced to infer such coverage.

Based on the EdukNow Competence Project, the following competencies were reused to address Task204. Their selection reflects the distinction between core theoretical reasoning, supporting modeling activities, and transversal communication competencies, as validated through expert review.

### C06 – Develop Problem-Solving Solutions Using Finite State Machines

Justification for Reuse:  
Students are required to construct a Finite State Machine representing the observable behavior of the Online Judge system across evaluation outcomes (AC, WA, TLE, CE, RE).  

In Task204, FSM construction serves as a behavioral externalization mechanism, allowing learners to represent system responses and evaluation states without modeling internal program execution. Accordingly, C06 supports the constructive representation of system behavior while remaining secondary to the theoretical explanation of computational limits.

### C02 – Justify the Use of Deterministic Finite Automata (DFAs)

Justification for Reuse:  
The task requires students to discuss the adequacy and limitations of FSMs as modeling tools. Competency C02 supports analytical reasoning about model selection and expressive power, enabling learners to justify why FSMs are suitable for representing observable outcomes without treating this outcome model as a general decision procedure for program termination.

### C03 – Test Automata Using Simulators

Justification for Reuse:  
The FSM model must be validated through simulation using tools such as JFLAP. Competency C03 supports simulation-based verification and refinement of the model, ensuring that the represented system behavior is consistent with the defined evaluation scenarios.

### C14 – Differentiate Classifications of Formal Grammars

Justification for Reuse:  
Students relate the behavior of Online Judge systems to the broader theoretical framework of computation by positioning FSMs and Turing Machines within the Chomsky Hierarchy. Competency C14 supports comparative reasoning about expressive power and contributes to the theoretical justification of system limitations.

### C05 – Write a Technical Report

Justification for Reuse:  
Task204 requires the production of a structured technical report integrating problem analysis, FSM modeling, and theoretical justification. Competency C05 supports the clear and rigorous communication of technical reasoning and serves as a transversal competency, providing the primary artifact through which learning evidence is expressed.

The following competencies were introduced to address Task204. While previous tasks focused on model construction and expressive adequacy (FSMs and PDAs), Task204 introduces a scenario in which the central learning objective concerns the theoretical limits of computation itself. The task requires learners to explain why certain system behaviors—such as detecting infinite loops in arbitrary programs—cannot be algorithmically determined. 

This requirement revealed the absence of an explicit competency addressing undecidability and its practical implications, leading to the introduction of C15 as a core analytical and justificatory competency. A second related competency (C16) emerges subsequently to support interpretative reasoning about Turing Machine concepts, without constituting an independent constructive objective.

## 4.1 Competency Specification

### C15 – Understand the Halting Problem and its Implications

#### A.1 Competency Title

Understand the Halting Problem and its Implications

#### A.2 Textual Description

This competency involves the ability to understand and articulate the theoretical foundations and practical implications of the Halting Problem, one of the central results in Computation Theory. Learners must be able to explain why it is undecidable to determine whether an arbitrary program halts on a given input and how this limitation affects the design and behavior of automated computational systems, such as Online Judges.

Students demonstrate this competency by relating the Halting Problem to the broader notions of computability, Turing Machines, and recursively enumerable languages, and by using these concepts to justify the impossibility of general-purpose loop detection. The emphasis of this competency lies in analytical and justificatory reasoning, rather than in the construction or simulation of computational models.

Within the context of Task204, learners are expected to provide a theoretically grounded explanation of why termination cannot be decided algorithmically for all arbitrary programs and inputs and to connect this limitation to observable system outcomes such as TLE. The competency therefore bridges abstract computational theory and real-world system behavior, highlighting the boundaries of algorithmic solvability.

#### A.3 Knowledge Specification

The following knowledge areas are central to this competency:

* The Halting Problem

  * Core result establishing undecidability in computation.
  * Explains fundamental limits of algorithmic reasoning about program behavior.

* Computability

  * Provides the formal framework for reasoning about what problems can or cannot be solved algorithmically.
  * Supports classification of problems as decidable, semi-decidable, or undecidable.

* Turing Machines

  * Serve as the reference model for general computation.
  * Support conceptual reasoning about recognizability and undecidability without requiring constructive modeling.

* Analytical and Critical Thinking (FPK)

  * Supports the development of logically coherent explanations and theoretical argumentation.
  * Enables learners to relate abstract theory to practical system limitations.

#### A.4 Disposition Specification

The following dispositions support effective enactment of this competency:

Analytical Rigor

* Encourages careful reasoning when interpreting theoretical results and their implications.
* Supports precision and consistency in explanations involving undecidability and computational limits.

Responsibility

* Involves maintaining academic rigor when communicating theoretical limitations, particularly when translating technical concepts to non-technical audiences.
* Includes ensuring conceptual correctness in written explanations and justifications.

Collaboration

* Supports collective reasoning and peer discussion within the PBL context.
* Enables refinement of theoretical explanations through shared analysis and feedback.

Proactivity

* Encourages learners to engage actively with abstract concepts and seek clarification when confronting theoretical boundaries or counterintuitive results.

#### A.5 Knowledge–Skill Pairing

##### A.5.1 Mapping Knowledge to Skills

* Understand the Halting Problem in order to justify the impossibility of general infinite loop detection.
* Understand Computability to classify problems according to solvability and recognizability.
* Analyze the role of Turing Machines as reference models for reasoning about undecidability.
* Apply analytical and critical thinking to construct coherent theoretical explanations linking computation theory to system behavior.

##### A.5.2 Bloom’s Taxonomy Alignment

* Halting Problem – Understand / Analyze

  * Enables learners to explain undecidability and relate it to real-world automated evaluation systems.

* Computability – Understand

  * Assesses the ability to classify computational problems according to solvability.

* Turing Machines – Analyze

  * Supports reasoning about limits of computation without requiring model construction.

* Analytical and Critical Thinking – Apply

  * Supports the construction of logically consistent theoretical arguments.

##### A.5.3 Verb Annotation

* Understand → Halting Problem → *Describe, Explain, Justify*
* Analyze → Turing Machines → *Relate, Examine, Interpret*
* Understand → Computability → *Classify, Recognize, Explain*
* Apply → Analytical and Critical Thinking → *Evaluate, Structure, Argue*

#### A.6 Summary Table for Competency C15

The table summarizes the pairing structure. The complete disposition list remains the one specified in A.4, including Proactivity.

| Competency                                      | Dispositions                                   | Knowledge                    | Skill                                      |
| --------------------------------------------------- | -------------------------------------------------- | -------------------------------- | ---------------------------------------------- |
| Understand the Halting Problem and its Implications | Analytical Rigor, Responsibility, Collaboration    | Halting Problem                  | Understand / Analyze                       |
|                                                     |                                                    | Turing Machines                  | Analyze (Relate, Interpret)                |
|                                                     |                                                    | Computability                    | Understand (Classify, Explain)             |
|                                                     |                                                    | Analytical and Critical Thinking | Apply (Evaluate, Structure, Argue)         |

### C16 – Apply Turing Machine Concepts to Analyze Computational System Capabilities

#### B.1 Competency Title

Apply Turing Machine Concepts to Analyze Computational System Capabilities

#### B.2 Textual Description

This competency involves the ability to apply the conceptual framework of Turing Machines to analyze and interpret the capabilities and limitations of computational systems. Rather than focusing on the construction of Turing Machine artifacts, this competency emphasizes the interpretative and analytical use of the Turing Machine model as a reference abstraction for reasoning about computation.

Learners are expected to understand how Turing Machines provide a universal model of algorithmic computation, enabling the analysis of system behavior and the classification of problems as computable, semi-decidable, or undecidable. This includes the ability to relate abstract computational models to practical systems such as Online Judges, compilers, and program analyzers, explaining how their operational limits emerge from fundamental computational principles.

Within the context of Task204, this competency supports the explanation of how Turing-completeness underlies modern programming systems and why a general algorithm cannot decide non-termination for every arbitrary program and input. The competency therefore operates primarily in an analytical and interpretative mode, complementing C15 by providing the conceptual framework through which undecidability results are understood and contextualized.

#### B.3 Knowledge Specification

The following knowledge areas are fundamental for this competency:

* Turing Machines

  * Reference abstraction for general-purpose computation.
  * Provides the conceptual basis for reasoning about algorithmic capabilities and limitations.

* Computability Theory

  * Framework for analyzing solvability and recognizability of computational problems.
  * Supports classification of computational phenomena observed in practical systems.

* Universal Turing Machine

  * Illustrates programmability and simulation as fundamental properties of computation.
  * Supports understanding of how modern computational systems emulate arbitrary algorithms.

* Analytical and Critical Thinking (FPK)

  * Enables interpretation of theoretical models and evaluation of system limitations.
  * Supports the construction of coherent explanations linking theory and practice.

#### B.4 Disposition Specification

The following dispositions support the effective enactment of this competency:

Analytical Rigor

* Encourages precise interpretation of formal models and careful reasoning about computational limits.
* Supports conceptual consistency when relating abstract theory to system behavior.

Responsibility

* Involves maintaining conceptual accuracy in theoretical explanations and written argumentation.
* Ensures that computational limitations are communicated correctly and without oversimplification.

Collaboration

* Supports collective reasoning during PBL activities, enabling clarification of abstract concepts through discussion and peer feedback.

Proactivity

* Encourages learners to explore conceptual connections between formal computation models and real-world systems beyond minimal task requirements.

#### B.5 Knowledge–Skill Pairing

##### B.5.1 Mapping Knowledge to Skills

* Apply Turing Machine concepts to interpret computational system behavior and limitations.
* Understand Computability Theory to classify problems according to solvability and recognizability.
* Apply analytical and critical thinking to structure arguments relating formal models to practical systems.

##### B.5.2 Bloom’s Taxonomy Alignment

* Turing Machines – Apply / Analyze

  Enables learners to use the Turing Machine abstraction as an explanatory framework for computational capabilities and limits.

* Computability – Understand

  Assesses conceptual clarity in distinguishing decidable, semi-decidable, and undecidable problems.

* Analytical and Critical Thinking – Apply

  Supports argumentation and synthesis of theoretical insights with real-world computational scenarios.

##### B.5.3 Verb Annotation

* Apply → Turing Machines → *Use, Interpret, Explain*
* Understand → Computability → *Classify, Distinguish, Describe*
* Apply → Analytical and Critical Thinking → *Analyze, Structure, Justify*

#### B.6 Summary Table for Competency C16

The table summarizes the pairing structure. The complete specification also includes Proactivity and Universal Turing Machine in B.4 and B.3, respectively; their absence as separate table entries does not remove them.

| Competency                                                             | Dispositions                                   | Knowledge                    | Skill                                        |
| -------------------------------------------------------------------------- | -------------------------------------------------- | -------------------------------- | ------------------------------------------------ |
| Apply Turing Machine Concepts to Analyze Computational System Capabilities | Analytical Rigor, Responsibility, Collaboration    | Turing Machines                  | Apply / Analyze (Use, Interpret, Explain)   |
|                                                                            |                                                    | Computability                    | Understand (Classify, Distinguish, Describe) |
|                                                                            |                                                    | Analytical and Critical Thinking | Apply (Analyze, Structure, Justify)          |
