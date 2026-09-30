# Competency Specification Report: Task03 — The Farmer Robot

## Introduction

This report documents the preliminary competency specification produced in CSP Phase 1 for Task03 — The Farmer Robot. The instructional entity is a Problem-Based Learning (PBL) task in which learners use finite state machines and regular expressions to model a herd-identification module. The specification recorded here is the artifact subsequently examined in the expert review.

## 1. Instructional Entity Analysis

### Title

The Farmer Robot

### Description

Learners are challenged to prototype a module that identifies bovine, caprine, and swine herds and triggers feed requests when predefined minimum quantities are reached. The company also asks how finite-state complexity relates to the required herd thresholds so that it can estimate project costs.

### Solution Development Process

Learners are expected to:

- Classify animals from visual or sensor input into herd categories.
- Detect herd thresholds, triggering feed requests when minimum herd sizes are reached.
- Model module behavior using Finite State Machines (FSM) in JFLAP.
- Research and use regular expressions as part of the solution documentation.
- Analyze FSM complexity, investigating how thresholds affect the required number of states and transitions.
- Simulate and validate the FSM design using JFLAP.
- Produce a technical report in the SBC article format describing the module, at least two examples, and the documentation and budgeting questions raised by the company.
- Document the collaborative process through successive PBL Whiteboards and a shared Logbook.

### Expected Outcomes

Learners should submit:

- A JFLAP file containing the robot identification module.
- A detailed report in the SBC article format describing the module’s design and operation.
- At least two examples of the module’s operation within the report.
- A discussion in the report addressing the company’s documentation and budgeting questions, including the relationship between herd thresholds and the number of states and transitions.
- Successive PBL Whiteboards and a Logbook documenting the development process, as required by the task.

### Acquisition Context

- Setting: A collaborative PBL activity in a computing course.
- Process: Team meetings documented through successive PBL Whiteboards and a shared Logbook.
- Resources: JFLAP for constructing and simulating the module, with the UFBA virtual learning environment used for submission.

### Target Audience Profile

The Phase 1 specification assumes the following learner profile:

- Academic level: second- or third-year undergraduate Computer Science students.
- Domain background:

  - Familiar with finite state machines and regular expressions.
  - Experienced in algorithm design, modeling, and simulation.

- Task roles:

  - Designers of FSMs and regular expressions.
  - Model analysts optimizing FSM structure.
  - Report authors detailing logic, cost, and reasoning.

These characteristics are specification assumptions rather than information stated in the task document.

### Proficiency Scale

For this Phase 1 specification, competency performance is represented on a continuous numeric scale from 0.0 to 10.0, with increments of 0.1. Based on the assigned grade, performance is classified into one of the proficiency levels below. This scale is an assumption adopted for specification purposes; it is not defined in the task document.

- Novice *(0.0 ≤ grade ≤ 5.0)*
  Demonstrates an incomplete or incorrect Finite State Machine (FSM) or regular expression, failing to reliably detect herd thresholds or to correctly classify the specified cases.
  Typical issues include missing or incorrect transitions, inadequate state definitions, misclassification of threshold conditions, or inconsistency between the FSM and the corresponding regular expression.

- Competent *(5.0 < grade ≤ 9.0)*
  Presents an accurate and coherent FSM and corresponding regular expression, correctly detecting herd thresholds and classifying all required cases.
  The solution is successfully simulated and validated using JFLAP, exhibiting consistent behavior across representative inputs and alignment between the automaton and the regular expression.

- Advanced *(9.0 < grade ≤ 10.0)*
  Extends the correct solution with an optimized FSM, demonstrating reduced state complexity or improved structural efficiency.
  The solution includes a threshold analysis, an explicit FSM cost estimation, and a clear explanation in the technical report. These performance descriptors are assumptions adopted for specification rather than additional deliverables beyond the task.

## 2. Knowledge Enumeration

To successfully complete the *Farmer Robot* task, students must draw upon a combination of theoretical and professional knowledge domains. These knowledge areas are aligned with the ACM Computing Classification System (2012) for core computing knowledge and the ACM/IEEE CC2020 framework for foundational professional competencies (FPK).

This interdisciplinary knowledge base supports the development of an effective and optimized decision-making system for animal classification and feed management.

### Computing Knowledge

- Finite State Machines (Finite Automata)
  - Fundamental for modeling the robot’s classification logic. FSMs allow students to design and simulate the decision process for herd detection using well-defined states and transitions.

- Regular Expressions (Regular Languages)
  - Used to represent the behavior of the FSM and validate whether the robot’s input patterns match the expected animal classification formats.

- Requirements Engineering
  - Enables the interpretation and translation of the company’s functional demands (e.g., low cost, minimum thresholds, interpretability) into system specifications and modeling constraints.

- Modeling and Simulation
  - Supports the creation, execution, and refinement of FSMs within tools such as JFLAP, allowing students to test the system’s behavior and validate outcomes against expected scenarios.

### Professional Knowledge (FPK)

- Analytical and Critical Thinking
  Essential for decomposing the problem into solvable parts, identifying optimization opportunities (e.g., minimizing states), and interpreting system behavior through logical reasoning.

- Problem Solving and Troubleshooting
  Required for resolving design and implementation challenges, such as ambiguous patterns, state explosion, or regular expression inconsistencies.

- Written Communication
  Necessary for delivering a clear and well-structured technical report, providing rationale for design choices, and communicating solutions to stakeholders with varying technical backgrounds.

## 3. Learning Objectives Identification

### General Objective

Develop a herd-identification module for the farmer robot prototype using finite state machines and regular expressions.

### Specific Learning Objectives

The formulations below correspond to the six objectives stated in the instructional entity, with terminology clarified during the preliminary Phase 1 analysis:

1. Identify the required functions of the robot identification module.
2. Apply finite state machines to solve the herd-identification problem.
3. Research and use regular expressions as part of the solution and its documentation.
4. Investigate the relationship between minimum herd quantities and the minimum states and transitions required by the finite state machine.
5. Use JFLAP to simulate the robot identification process.
6. Prepare a detailed report in the SBC article format describing the module’s operation and providing examples.

## 4. Competency Definitions

Competencies are specified based on the Learning Objectives (LOs) identified in the task analysis.

### Competency Reuse

To address Objective 6, "Test and simulate FSMs using tools such as JFLAP to validate correctness and effectiveness," we reuse the competency previously defined in Task01 – The Vending Machine for Sodas and Snacks:

  > Testing Automata Using Simulators

This competency remains fully relevant in the current task, where students are expected to validate their automaton models through formal simulation tools such as JFLAP. The learning outcomes include the ability to execute, observe, and analyze automata behavior in a simulated environment, ensuring functional correctness and alignment with system specifications.

Additionally, since one of the deliverables for this task is a technical report formatted according to the academic standards of the Brazilian Computer Society (SBC), we also reuse the previously defined competency from Task01:

> Collaborative Technical Report Writing

This competency involves planning, structuring, and composing a comprehensive document that clearly communicates the problem-solving process, decisions made, and justifications for the implemented model. It reinforces essential skills in technical writing, team collaboration, and documentation.

The reuse of these competencies supports the following principles:

- Pedagogical consistency in competency development across different learning tasks.
- Recognition and reinforcement of transversal skills, such as documentation and tool-based validation.
- Avoidance of redundancy through structured competency traceability.
- Alignment with competency-based education, where a well-defined learning outcome may be demonstrated in multiple instructional contexts.

By reusing validated competencies, we ensure that students build upon previously acquired abilities, promote cumulative learning, and facilitate assessment practices based on observable and transferable performance indicators.

### 4.1 Competency A Specification

#### A.1 Competency Title

Develop Problem-Solving Solutions Using Finite State Machines

#### A.2 Textual Description

Design and implement computational solutions using Finite State Machines (FSMs) to address real-world or instructional problems involving system modeling through states and transitions. This competency reflects the student's ability to apply theoretical knowledge of automata in constructing reliable and verifiable models that fulfill defined system requirements.

Students are expected to demonstrate not only mastery of FSMs, but also the ability to analyze system requirements and apply logical reasoning to model behavior, ensuring that the solution is both theoretically sound and practically relevant.

#### A.3 Knowledge Specification

The following knowledge areas are critical for this competency:

- Finite Automata (Finite State Machines)
  Understand and apply the structure, behavior, and applications of deterministic and non-deterministic automata to model sequential systems.

- Requirements Analysis
Identify, interpret, and translate system requirements into formal specifications for FSM design.

- Analytical and Critical Thinking (FPK)
  Break down the problem, assess constraints and goals, and select appropriate modeling strategies to guide the design process.

#### A.4 Disposition Specification

Given the collaborative nature of the task and the need for creative model development, the following behavioral dispositions are essential:

- Inventive
  Propose novel modeling strategies and explore different ways of structuring FSMs to reflect system behavior.

- Collaborative
  Cooperate with peers in discussing requirements, designing the machine, and validating its behavior.

- Responsible
  Take ownership of the solution's quality, ensuring consistency with task expectations and timelines.

- Proactive
  Anticipate implementation challenges and adapt the design to improve accuracy and functionality.

- Creative
  Transform system requirements into intuitive and innovative models, making abstract behaviors operational through states and transitions.

#### A.5 Knowledge-Skill Pairing

This step maps knowledge areas to the corresponding skills required to successfully demonstrate competency in this task.
##### A.5.1 Mapping Knowledge to Skills

To demonstrate this competency, students must show the ability to:

- Apply knowledge of Finite Automata to design models that reflect real-world behaviors through structured state transitions.

- Apply Requirements Analysis to understand the user’s expectations and translate them into clear formal specifications that guide FSM design.

- Apply Analytical and Critical Thinking (FPK) to interpret the problem, analyze possible design paths, and justify modeling decisions based on logic and feasibility.
##### A.5.2 Bloom’s Taxonomy Alignment

- Create level is used to assess students’ ability to employ the concept of Finite Automata in modeling and developing a solution to the Farm Robot problem.
##### A.5.3 Verb Annotation

To provide clarity on competency expectations, the following verb annotations define the required actions:

- Create → Finite State Machines → *Design, Develop, Construct*
- Apply → Requirements Analysis → *Interpret, Specify, Translate*

### 4.2 Competency B Specification

#### B.1 Competency Title

  Determine Regular Expressions that Represent Automata

#### B.2 Textual Description

This competency focuses on understanding the relationship between regular expressions and finite automata, enabling students to interpret automaton structures and express their behavior using equivalent formal representations. It also involves applying requirements analysis to identify system needs and translate them into valid components of regular languages.

Learners must demonstrate theoretical comprehension of regular languages and their expressive power, as well as the ability to apply systematic analysis to refine or validate the regular expressions corresponding to given automata.

#### B.3 Knowledge Specification

The following knowledge areas are essential for this competency:

- Regular Languages
  - Understand the syntax, semantics, and expressive limits of regular expressions and their formal equivalence to finite automata.

- Requirements Analysis
  - Apply methods to identify, interpret, and translate system or task requirements into formal specifications suitable for FSM design.

- Analytical and Critical Thinking (FPK)
  - Apply analytical thinking to test and refine regular expressions for correctness, minimality, and functional adequacy.

#### B.4 Disposition Specification

The following behavioral dispositions support the effective development of this competency:

- Inventive
  - Explore alternative regular expressions that preserve equivalence while optimizing for clarity or minimality.

- Collaborative
  - Cooperatively analyze and validate the correspondence between automata and regular expressions.

- Responsible
  - Ensure that constructed expressions are formally correct and aligned with task requirements.

- Proactive
  - Take initiative in testing, iterating, and improving the regular expressions produced.

- Creative
  - Demonstrate creativity in modeling approaches that balance simplicity, precision, and expressiveness.

#### B.5 Knowledge-Skill Pairing

##### B.5.1 Mapping Knowledge to Skills

To demonstrate this competency, students must:

- Understand knowledge of Regular Languages to interpret automata and express equivalent behavior through regular expressions.
- Apply knowledge of Requirements Analysis to decompose task descriptions and derive relevant regular language representations.
- Apply knowledge of Analytical and Critical Thinking (FPK) to  iteratively refine regular expressions.

##### B.5.2 Bloom’s Taxonomy Alignment

- *Understand* → Regular Languages
- *Apply* → Requirements Analysis
- *Apply* → Analytical and Critical Thinking (FPK)

##### B.5.3 Verb Annotation

- Understand → Regular Languages → *Interpret, Relate, Represent*
- Apply → Requirements Analysis → *Decompose, Translate, Compare*

### 4.3 Competency C Specification

#### C.1 Competency Title

  Infer and Identify Patterns in Finite State Machines

#### C.2 Textual Description

Analyze the structure and behavior of Finite State Machines (FSMs) to draw inferences and identify emerging patterns that influence model complexity and performance. This competency involves recognizing relationships between input classifications, state transitions, and the number of states required for effective modeling.

Students are expected to demonstrate the ability to analyze FSMs, detect design regularities or redundancies, and apply Analytical and Critical Thinking (FPK) to refine and interpret system behavior.

#### C.3 Knowledge Specification

The following knowledge areas are critical for this competency:

- Finite State Machines
  - Understand structural properties of FSMs, including states, transitions, and minimization principles, and how these influence computational modeling.

- Analytical and Critical Thinking (FPK)
  - Apply logical reasoning to identify hidden structures, draw meaningful conclusions, and justify design decisions based on pattern recognition and model analysis.

#### C.4 Disposition Specification

Given the abstract nature of the task and the cognitive demands of pattern recognition and inference, the following behavioral dispositions are essential:

- Inventive
  - Approach FSM analysis with originality, exploring non-obvious or alternative interpretations of structural behavior.

- Creative
  - Devise innovative methods to visualize, interpret, or generalize state-based patterns.

- Meticulous
  - Pay careful attention to detail when identifying similarities, redundancies, or inefficiencies in state design and transitions.

#### C.5 Knowledge-Skill Pairing

This section maps the knowledge areas to the corresponding skills required to successfully demonstrate this competency.

##### C.5.1 Mapping Knowledge to Skills

To demonstrate this competency, students must:

- Analyze knowledge of Finite Automata to examine state structures, recognize patterns, and determine how input categories influence the number of states and transitions required.
- Apply knowledge of Analytical and Critical Thinking (FPK) to make informed inferences, detect behavioral regularities, and refine FSM designs based on logical reasoning and task-specific constraints.

##### C.5.2 Bloom’s Taxonomy Alignment

The Analyze level of Bloom’s Taxonomy is used to assess learners' ability to examine components of FSMs, explain their functional behavior, and justify structural or behavioral improvements based on evidence and reasoning.

##### C.5.3 Verb Annotation

To clarify expectations, the following verbs are aligned with the knowledge areas at the Analyze level:

- Analyze → Finite Automata → *Analyze, Evaluate, Compare*

### 4.4 Competency D Specification

#### D.1 Competency Title

  Differentiate the Classifications of Formal Grammars

#### D.2 Textual Description

Understand and differentiate the various classes of formal grammars—as defined by the Chomsky hierarchy—based on their generative power and relation to automata. This competency involves identifying characteristics that distinguish regular, context-free, context-sensitive, and unrestricted grammars, and recognizing their applicability to computational problem-solving.

In the context of the *Robotic Farmer* task, this competency reinforces the theoretical foundation required to select and justify the appropriate computational model (e.g., Finite Automaton) based on system constraints and requirements.

Students are expected to demonstrate a conceptual understanding of grammar classification and apply this understanding when specifying system behaviors, translating requirements into executable logic through Requirements Engineering and Analytical and Critical Thinking (FPK).

#### D.3 Knowledge Specification

The following knowledge areas are critical for this competency:

- Regular Languages
  Understand the hierarchical organization of grammars and their relationship to classes of automata and language recognition.

- Requirements Engineering
  Translate user needs into system specifications that are compatible with the expressive power of the selected formal language model.

- Analytical and Critical Thinking (FPK)
  Interpret system constraints, evaluate grammar applicability, and reason about which classification best suits a given computational problem.

#### D.4 Disposition Specification

Given the analytical depth and collaborative demands of the task, the following behavioral dispositions are essential:

- Collaborative
  Participate actively in team-based discussions to classify grammars and align them with solution strategies.

- Responsible
  Ensure accuracy in theoretical classification and maintain alignment between system specifications and computational models.

- Proactive
  Anticipate limitations in modeling choices and explore alternatives within the Chomsky hierarchy.

- Investigative
  Explore the theoretical implications of grammar choice and examine edge cases in grammar-automaton equivalence.

#### D.5 Knowledge-Skill Pairing

This step maps knowledge areas to the corresponding skills required to successfully demonstrate competency in this task.
##### D.5.1 Mapping Knowledge to Skills

To demonstrate this competency, students must show the ability to:

- Understand the classes of Regular Languages and relate them to their corresponding automata and computational properties.

- Apply Requirements Engineering to ensure that chosen formal models meet stakeholder needs and system constraints.

- Apply Analytical and Critical Thinking (FPK) to reason through grammar selection, justify modeling choices, and interpret theoretical implications in practical contexts.
##### D.5.2 Bloom’s Taxonomy Alignment

- *Understand* level is used to assess the student’s conceptual ability to classify grammars and associate them with the correct type of automaton.

- *Apply* level is used to evaluate the student’s capacity to translate system requirements and theoretical knowledge into appropriate model selection and implementation.
##### D.5.3 Verb Annotation

To provide clarity on competency expectations, the following verb annotations define the required actions:

- Understand → Regular Languages → *Differentiate, Compare, Classify*
- Apply → Requirements Engineering → *Align*
- Apply → Analytical and Critical Thinking

## 5. Competency Summary

| Competency                                                    | Dispositions                                           | Knowledge                          | Skill                                 |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | -------------------------------------- | ----------------------------------------- |
| Develop Problem-Solving Solutions Using Finite State Machines | Inventive, Collaborative, Responsible, Proactive, Creative | Finite Automata                        | Create (Design, Develop, Construct)        |
|                                                                   |                                                            | Requirements Analysis                  | Apply (Interpret, Specify, Translate) |
|                                                                   |                                                            | Analytical and Critical Thinking (FPK) | Apply (Analyze, Justify, Evaluate)    |
| Determine Regular Expressions that Represent Automata | Inventive, Collaborative, Responsible, Proactive, Creative | Regular Languages                         | Understand (Interpret, Relate, Represent) |
|                                                           |                                                            | Requirements Analysis                     | Apply (Decompose, Translate, Compare) |
|                                                           |                                                            | Analytical and Critical Thinking (FPK) | Apply (Analyze, Test, Refine)         |
| Infer and Identify Patterns in Finite State Machines | Inventive, Creative, Meticulous | Finite Automata                        | Analyze (Evaluate, Compare)        |
|                                                          |                                 | Analytical and Critical Thinking (FPK) | Apply (Infer, Justify, Interpret)  |
| Differentiate the Classifications of Formal Grammars | Collaborative, Responsible, Proactive, Investigative | Regular Languages         | Understand (Differentiate, Compare, Classify) |
|                                                          |                                                      | Requirements Engineering                    | Apply (Align)                                 |
|                                                          |                                                      | Analytical and Critical Thinking (FPK)      | Apply                                         |
| *Testing Automata Using Simulators (REUSED)* | Collaborative, Responsible, Proactive, Creative | Automata over Infinite Objects | Apply (Experiment, Relate, Simulate) |
|  |  | Problem Solving and Troubleshooting (FPK) | Apply (Diagnose, Debug, Refine) |
| *Collaborative Technical Report Writing (REUSED)* | Collaborative, Meticulous, Responsible | Written Communication (FPK) | Apply (Write, Structure, Revise, Refine) |

## Conclusion

This Phase 1 report records the preliminary competency specifications derived from Task03, including the reuse of the simulation and technical-report competencies defined for Task01. The specifications provide the input for CSP Phase 2, where their scope, terminology, knowledge–skill alignment, and consistency are examined through expert review.

