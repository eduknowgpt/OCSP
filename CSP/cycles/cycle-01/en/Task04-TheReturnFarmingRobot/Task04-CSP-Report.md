# CSP Phase 1 Report: Task04 — The Return of the Farmer Robot

## Introduction

This report applies CSP Phase 1 to the Problem-Based Learning scenario *The Return of the Farmer Robot*. The task asks learners to design a navigation module that enables the robot to return to its starting point after issuing a food-delivery alert.

The scenario introduces a memory-based computational model because a finite state machine alone is insufficient for recording and reversing the robot’s route. Learners investigate Pushdown Automata (PDA), Context-Free Grammars, and simulation with JFLAP. They document the proposed model and its behavior in a technical report.

## 1. Instructional Entity Analysis

### 1.1 Title

*The Return of the Farmer Robot*

### 1.2 Description

The task extends the Farmer Robot scenario developed in Task03. The new navigation module must allow the robot to return to its starting point after traveling through the herd and issuing the food-delivery alert.

The task states that a simple Finite State Machine is insufficient for this navigation problem and suggests adding an auxiliary memory device. This leads learners to investigate a stack-based model represented by a Pushdown Automaton.

Learners may extend the original Food Delivery Module or develop a separate navigation module that communicates with it. The company is also interested in a notation system for specifying rules that generate location sequences.

### 1.3 Solution development process

Learners are expected to:

1. analyze the navigation problem and identify why auxiliary memory is needed;
2. investigate a stack-based computational model for recording and reversing a route;
3. model the navigation module as a Pushdown Automaton;
4. simulate and test the model in JFLAP;
5. investigate a rule-based notation for generating location sequences;
6. document the solution, examples, decisions, and difficulties in a technical report.

The work follows the PBL process described in the task. Teams record questions, facts, hypotheses, and actions on the PBL Whiteboard and maintain a logbook of meetings, contributions, discussions, and challenges.

### 1.4 Expected outcomes

The required deliverables are:

- a JFLAP file containing the robot’s navigation module;
- a technical report in the SBC article format.

The report must explain the operation of the navigation module and provide at least two examples. If the team develops a rule-based notation, the report must also show examples of location-sequence generation. Otherwise, it must describe the main difficulties encountered.

### 1.5 Acquisition context

- **Instructional approach:** collaborative Problem-Based Learning.
- **Environment:** coursework involving JFLAP, team meetings, a PBL Whiteboard, and a shared logbook.
- **Application context:** formal modeling of a robotic navigation problem.
- **Learner roles:** model design, simulation and analysis, collaborative documentation, and presentation of decisions.
- **Assessment evidence:** the JFLAP model, the technical report, worked examples, the PBL Whiteboards, the logbook, and records of participation.

### 1.6 Proficiency scale

Performance is represented on the numeric scale used in the task context, from 0.0 to 10.0, and mapped to the following levels:

- **Novice (0.0–5.0):** presents an incomplete or incorrect navigation model. The stack operations or return behavior are not represented reliably, the simulation does not demonstrate the required behavior, or the report does not adequately explain the solution.
- **Competent (5.1–9.0):** presents a coherent Pushdown Automaton that uses auxiliary memory to model the return route. The solution is simulated in JFLAP, demonstrates the required behavior through examples, and is explained clearly in the technical report.
- **Advanced (9.1–10.0):** presents a correct and well-justified model, evaluates relevant design choices, demonstrates the behavior through clear examples, and provides a precise technical explanation of the stack-based navigation strategy.

## 2. Knowledge Enumeration

### 2.1 Computing knowledge

- **Pushdown Automata:** state-based computation with stack memory, including transitions and stack operations used to record and reverse navigation sequences.
- **Context-Free Grammars:** production rules and the generation of structured symbol sequences, when used to describe location sequences.
- **Requirements Analysis:** identification and formalization of the navigation module’s expected behavior and constraints.
- **Modeling and Simulation:** representation and validation of the proposed model in JFLAP.

### 2.2 Foundational and professional knowledge

- **Analytical and Critical Thinking (FPK):** decomposition of the navigation problem, analysis of memory requirements, and evaluation of modeling alternatives.
- **Problem Solving and Troubleshooting (FPK):** development, testing, and correction of the computational model.
- **Written Communication (FPK):** documentation of the model, examples, decisions, and results.
- **Collaborative work:** construction and review of a shared solution and maintenance of the PBL records.

## 3. Learning Objectives

### 3.1 General objective

Develop a navigation module for the Farmer Robot that enables it to return to its starting point after issuing a food-delivery alert.

### 3.2 Specific objectives

1. Understand the functions and challenges of the Farmer Robot navigation problem.
2. Investigate the use of auxiliary memory in a computational model for returning to the starting point.
3. Analyze whether to extend the Food Delivery Module or develop communicating modules.
4. Research and propose a rule-based notation for generating location sequences.
5. Use JFLAP to simulate the robot’s navigation process and generate location sequences.

## 4. Competency Specification

### 4.1 Reused competencies

Two competencies specified in Task01 are reused:

- *Testing Automata Using Simulators*;
- *Collaborative Technical Report Writing*.

The first supports the execution and analysis of the JFLAP model. The second supports collaborative preparation of the report required by the task. Their reuse records continuity across tasks and avoids duplicate specifications.

### 4.2 Competency A — Develop Problem-Solving Solutions Using Pushdown Automata

#### Description

Design and implement a Pushdown Automaton that represents a navigation strategy for returning a robot to its starting point. The model uses stack-based memory to record information needed for the return route and must satisfy the behavioral requirements of the task.

#### Knowledge

- **Pushdown Automata:** states, transitions, stack operations, and language recognition in computational models with memory.
- **Requirements Analysis:** identification and formalization of the navigation behavior and its constraints.
- **Analytical and Critical Thinking (FPK):** decomposition of the problem, evaluation of alternatives, and justification of modeling decisions.

#### Dispositions

- Inventive
- Collaborative
- Responsible
- Proactive
- Creative

#### Knowledge–skill pairing

| Knowledge | Bloom level | Observable actions |
| --- | --- | --- |
| Pushdown Automata | Create | Design, develop, construct |
| Requirements Analysis | Apply | Interpret, specify, translate |
| Analytical and Critical Thinking (FPK) | Apply | Analyze, evaluate, justify |

### 4.3 Competency B — Interpret Rule-Based Notation

#### Description

Interpret formal notation based on production rules, such as a Context-Free Grammar, when it is used to represent location sequences or navigation behavior.

#### Knowledge

- **Context-Free Grammars:** production rules and structured symbol sequences used to generate or represent navigation paths.
- **Pushdown Automata:** the relationship between stack-based automata and Context-Free Grammars.
- **Analytical and Critical Thinking (FPK):** interpretation and evaluation of rules for clarity, consistency, and correctness.

#### Dispositions

- Inventive
- Collaborative
- Responsible
- Proactive
- Creative

#### Knowledge–skill pairing

| Knowledge | Bloom level | Observable actions |
| --- | --- | --- |
| Context-Free Grammars | Understand | Interpret, recognize, describe |
| Pushdown Automata | Apply | Relate, simulate, validate |
| Analytical and Critical Thinking (FPK) | Apply | Analyze, identify, evaluate |

### 4.4 Competency C — Differentiate Classifications of Formal Grammars

#### Description

Distinguish regular and context-free grammars and relate each class to its corresponding computational model. Learners use these distinctions to explain why the navigation problem requires a model with auxiliary memory.

#### Knowledge

- **Formal Grammar Classification:** distinctions between regular and context-free grammars and the automata associated with them.
- **Analytical and Critical Thinking (FPK):** comparison of grammar classes and evaluation of their suitability for representing system behavior.

#### Dispositions

- Inventive
- Collaborative
- Responsible
- Proactive

#### Knowledge–skill pairing

| Knowledge | Bloom level | Observable actions |
| --- | --- | --- |
| Formal Grammar Classification | Understand | Differentiate, compare, contrast |
| Analytical and Critical Thinking (FPK) | Apply | Relate, evaluate, justify |

## 5. Competency Summary

| Competency | Status | Dispositions | Knowledge–skill pairing |
| --- | --- | --- | --- |
| Develop Problem-Solving Solutions Using Pushdown Automata | Defined in Task04 | Inventive, Collaborative, Responsible, Proactive, Creative | Pushdown Automata — Create; Requirements Analysis — Apply; Analytical and Critical Thinking (FPK) — Apply |
| Interpret Rule-Based Notation | Defined in Task04 | Inventive, Collaborative, Responsible, Proactive, Creative | Context-Free Grammars — Understand; Pushdown Automata — Apply; Analytical and Critical Thinking (FPK) — Apply |
| Differentiate Classifications of Formal Grammars | Defined in Task04 | Inventive, Collaborative, Responsible, Proactive | Formal Grammar Classification — Understand; Analytical and Critical Thinking (FPK) — Apply |
| Testing Automata Using Simulators | Reused from Task01 | Collaborative, Responsible, Proactive, Creative | Automata over Infinite Objects — Apply; Problem Solving and Troubleshooting (FPK) — Apply |
| Collaborative Technical Report Writing | Reused from Task01 | Collaborative, Meticulous, Responsible | Written Communication (FPK) — Apply |

## 6. Conclusion

Task04 extends the Farmer Robot scenario by introducing navigation that depends on auxiliary memory. The competency specification connects this requirement to Pushdown Automata, Context-Free Grammars, requirements analysis, simulation, reasoning, and technical communication.

The report defines three task-level competencies and reuses two competencies from Task01. Together, they represent the abilities needed to model the return route, interpret rule-based notation, distinguish the relevant formal models, validate the solution in JFLAP, and document the work.

