# Competency Specification Report: Task202 – Team Control

* Authors: Luiz Gavaza, Daniel Cason, Lais Salvador, Roberta Oliveira  
* Contributors: Jéssica Santana, Otávio Neto, Edeyson Gomes  

## 1. Task Description Analysis

This task extends the system developed in Task201 by introducing a new class of behavioral constraints related to team composition control. According to updated institutional regulations, team composition must satisfy Vi ≥ ni × NVi, with ni > 0 defined for each event type i. Equality satisfies the stated condition; the requirement is not simply that volunteers outnumber non-volunteers.

Task202 introduces the comparison and validation of quantities and adopts a PDA as the instructional model for memory-based control. A finite-state representation has only finitely many distinguishable configurations; claims about its insufficiency depend on whether counts are unbounded and on how inputs and operations are represented. The team-composition requirement motivates the memory-based model adopted here, but the ratio alone is not a proof that every bounded formulation excludes an FSM.

Within the scope of this task, the problem is deliberately framed as a logical validation and control problem, rather than a physical or operational one. The instructional emphasis is therefore placed on the formal adequacy of computational models with respect to problem semantics. As a consequence, students are required to adopt memory-based computational models, particularly Pushdown Automata (PDAs), whose stack-based memory enables the representation of context-free constraints such as volunteer-to-non-volunteer ratios.

The task thus promotes a structured progression in which learners must:

- recognize the formal limitations of computational models and relate these limitations to problem requirements;
- formally justify the transition from FSMs to PDAs based on expressive power and modeling adequacy;
- design, simulate, and validate the revised system using JFLAP, ensuring correct stack manipulation and constraint enforcement; and
- document the solution, design rationale, modeling decisions, and validation results in a structured technical report.

From a competency perspective, Task202 emphasizes not only the construction of computational artifacts but also the ability to reason about model adequacy, interpret formal rule systems, and justify design decisions using concepts from formal language theory. The task therefore integrates constructive, analytical, and justificatory forms of competence activation, reinforcing abstraction, formal reasoning, and explicit justification as central elements of competency-based learning in Computation Theory.

This progression consolidates an important instructional transition within the CSP lifecycle: learners move from applying previously known models toward evaluating the suitability of computational models themselves, thereby strengthening the alignment between task semantics, formal knowledge, and competency activation.

## 2. Knowledge Enumeration

To address the task effectively, students are expected to mobilize the following task-relevant knowledge areas, organized according to their conceptual role within the CSP framework. This organization reflects not only disciplinary content but also the functional role that each knowledge group plays in supporting competency activation within the instructional context.

### Core Formal Knowledge

The following knowledge elements constitute the formal foundation required for reasoning about model adequacy, expressive power, and the correct representation of system constraints:

* Finite State Machines (FSMs): understanding their operational structure, expressive limits, and suitability for modeling regular behaviors represented through finite control.
* Pushdown Automata (PDAs): modeling computational systems that require stack-based memory, enabling the representation of counting, nesting, and context-free constraints.
* Formal Languages and Context-Free Grammars (CFGs): understanding how grammatical rules describe structural constraints and how these relate to automaton behavior and language recognition.
* Chomsky Hierarchy: distinguishing classes of formal languages and computational models according to expressive power, supporting justified transitions between modeling approaches.

These knowledge elements support the learner’s ability to analyze the limitations of computational models and to justify the adoption of more expressive formalisms when required by task semantics.

### Supporting Technical Knowledge

The following knowledge areas support the operationalization of formal concepts into executable and verifiable models:

* Requirements Analysis: interpreting regulatory and problem-domain constraints and translating them into formal system specifications.
* Modeling and Simulation: applying tools such as JFLAP to construct, simulate, test, and validate automaton-based solutions, ensuring alignment between formal models and expected system behavior.

These elements enable learners to connect theoretical reasoning with practical implementation and validation activities.

### Background and Transversal Knowledge

The following knowledge supports communication, documentation, and integration of results across the task lifecycle:

* Technical Writing Principles: structuring and communicating formal models, assumptions, design decisions, and validation results in an academic report format consistent with SBC guidelines.

## 3. Learning Objectives and Expected Outcomes

The task statement remains the reference for deliverables: the surveillance and team-control modules, their integration or communication, and an SBC report with at least two usage examples addressing documentation and budgeting. The PBL board, logbook, and investigation of states, transitions, and rules remain part of the stated process and objectives.

The learning objectives of Task202 are defined in terms of observable and justifiable learner actions, ensuring alignment between formal modeling activities, expected artifacts, and competency assessment.

Specifically, upon completion of the task, students are expected to:

- Analyze the expressive limitations of Finite State Machines (FSMs) and formally justify the need for memory-based computational models, particularly Pushdown Automata (PDAs), when addressing the memory-dependent team-composition constraints adopted in this task.

- Design and implement a Pushdown Automaton (PDA) capable of enforcing constraints that depend on both state and memory conditions, such as enforcing Vi ≥ ni × NVi for each monitored event type.

- Simulate and validate the behavior of the PDA using JFLAP, demonstrating operational correctness, proper stack manipulation, and compliance with problem-specific constraints and institutional rules.

- Explain and justify the formal mechanisms employed—including context-free grammars, stack operations, and state-transition logic—that underpin the automaton’s behavior and ensure adherence to the defined constraints.

- Produce a structured technical report, following the SBC academic format, that documents modeling decisions, implementation strategies, simulation results, and the formal justification of the chosen computational model.

Together, these objectives emphasize not only the construction of formal models, but also the ability to reason about model adequacy, validate behavior through simulation, and communicate technical decisions clearly and rigorously.

## 4. Competency Specification

Based on the analysis of the task requirements and the set of Reusable Competencies, the following competencies were selected as directly aligned with Task202’s learning objectives, required knowledge domains, and expected deliverables.  

The selection reflects the CSP principle that competencies should be reused when their semantic scope and expected learner actions remain stable across instructional contexts. In Task202, competencies are activated through a combination of constructive, analytical, and justificatory modes, reflecting the task’s emphasis on model construction, formal reasoning, and explicit justification of design decisions.

Each competency is therefore reused with an explicit justification grounded in the formal, analytical, and documentary demands of the task.

### C12 – Develop problem-solving solutions using Pushdown Automata

Justification for Reuse:  

The core challenge of Task202 is to model and validate a system that enforces volunteer-to-non-volunteer ratio constraints defined by institutional regulations. Such constraints require the ability to count, compare, and validate quantities dynamically, for which this task adopts stack-based memory. Any claim of finite-state insufficiency must be tied to the bounds and encoding of those quantities.

Pushdown Automata (PDAs) are the selected formalism: stack-based memory supports the context-free representation adopted for the team-composition constraints. Within the task, learners must not only construct a computational model but also justify why a memory-based formalism is required, linking system behavior to expressive power within formal language theory.

This competency directly supports the design, implementation, and formal justification of memory-based computational models tailored to control and validation scenarios. Its activation occurs primarily in a constructive mode, supported by analytical reasoning regarding model adequacy and correctness.

### C03 – Test Automata Using Simulators

Justification for Reuse:  

Task202 explicitly requires the simulation and validation of the proposed automaton using JFLAP, making operational testing an essential component of the problem-solving process. This competency supports the systematic verification of PDA behavior, including correct stack manipulation, state transitions, and compliance with the defined team composition constraints.

Within the instructional context, simulation serves as the bridge between formal specification and observable behavior, allowing learners to confront theoretical models with execution evidence. Through simulation, students are expected to identify inconsistencies, validate constraint enforcement, and iteratively refine their models based on execution traces and observed outcomes.

The reuse of this competency supports learners in developing the ability to verify operational correctness, relate formal design decisions to runtime behavior, and support the validation of modeling choices through empirical evidence. Its activation occurs primarily in an artifact-oriented mode, complementing the constructive activation of modeling competencies and reinforcing the analytical evaluation of system correctness.

### C13 – Interpret Rule-Based Notation

Justification for Reuse:  

The task includes a request from *SOS Florestal* for a formal and structured representation of team formation rules, requiring learners to interpret rule-based specifications expressed through symbolic and formal representations. This competency supports the ability to interpret rule-based notations, including context-free grammars, which provide a formal description of constraints enforced by stack-based automata.

Within Task202, learners must relate institutional constraints expressed in natural or semi-formal language to their corresponding formal representations, interpreting how symbolic rules constrain admissible behaviors and system states. This interpretative activity supports the understanding of how formal rule systems encode structural and quantitative requirements within the memory-based representation adopted for the task.

In this task, C13 is primarily activated at an analytical and interpretative level, enabling learners to connect problem-domain rules with grammatical and automaton-based representations. The competency supports reasoning about the meaning and implications of formal rules rather than the construction of grammatical artifacts, thereby complementing the constructive activation of modeling competencies and the justificatory reasoning required for model adequacy.

### C05 – Write a Technical Report

Justification for Reuse:  

One of the required deliverables of Task202 is a technical report formatted according to SBC guidelines, in which students must document modeling decisions, formal assumptions, simulation procedures, results, and the justification of the adopted computational model. This requirement positions technical writing not merely as a reporting activity, but as an integral component of the problem-solving process.

This competency supports the collaborative production of structured documentation that clearly communicates the rationale underlying model selection, the relationship between formal representations and system behavior, and the validation evidence obtained through simulation. The report therefore functions as a medium through which analytical reasoning and formal justification become explicit and assessable.

The reuse of this competency reinforces technical communication as a transversal competency, enabling learners to articulate complex formal reasoning in a precise and coherent manner, while ensuring traceability between problem requirements, modeling decisions, and obtained results.

### C14 – Differentiate Classifications of Formal Grammars

Justification for Reuse:  

A critical aspect of Task202 is the formal justification for transitioning from Finite State Machines (FSMs) to Pushdown Automata (PDAs). This transition requires learners to distinguish between regular and context-free language classes, as well as to understand their respective expressive power within the Chomsky hierarchy.

This competency supports the ability to analyze the limitations of computational models and to justify model selection decisions based on formal language theory rather than solely on implementation convenience. Learners are expected to justify the adopted memory-based representation, relating counting and validation to explicit assumptions about input encoding and bounds.

The reuse of this competency reinforces theoretical rigor by grounding modeling decisions in formally established classifications of computational expressiveness. Its activation occurs primarily in an analytical and justificatory mode, supporting informed and defensible choices of computational models and complementing the constructive and interpretative competencies mobilized throughout the task.

Together, these competencies form a coherent and complementary set that supports Task202’s emphasis on formal limitation analysis, model adequacy, memory-based computation, simulation-based validation, and rigorous technical communication.
