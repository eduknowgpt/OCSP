# CSP Review Adjustments Report: Task02 — *Traffic Control*

## Purpose

This report documents the revisions implemented after the CSP Phase 2 decision, *Approved with Revisions*, for Task02 — *Traffic Control*. The revisions address knowledge granularity, knowledge relevance, terminology, Bloom-aligned actions, and textual clarity without expanding the instructional scope of the task.

## Review Findings and Implemented Adjustments

### Knowledge Granularity

The preliminary specification used broad terms from the ACM Computing Classification System (CCS 2012). The revised specification adopts more specific knowledge terms aligned with the CS2013 reference used during adjustment. This change improves the correspondence between the task requirements and the knowledge components.

`Requirements Analysis` was refined to `Requirements Engineering`, providing a consistent term for the elicitation, specification, and interpretation of the DERBA requirements used in the task.

### Knowledge Relevance

The Church–Turing Thesis was removed from the Task02 learning objectives and competency knowledge components. Although it appears in the source task and is theoretically valid, the expert review concluded that it is not operationalized by the required Turing Machine files, simulations, or technical report.

The revised specification retains the knowledge directly exercised by the task: Turing Machines, Turing Machine variants, Requirements Engineering, Modeling and Simulation, and the associated professional knowledge components.

### Competency Descriptions

The descriptions were revised to state the expected capability and outcome more directly:

- C07 focuses on constructing a Turing Machine solution from the task requirements.
- C08 focuses on recognizing and differentiating Turing Machine variants.
- C09 focuses on applying predefined variants to a well-defined modeling problem.
- C10 focuses on testing, diagnosing, and refining Turing Machine models through simulation.
- C05, the technical-report competency reused from Task01, remains part of the Task02 competency set.

The boundaries among C07–C09 preserve their foundational Task02 scope. More complex architectural or integrated applications may be represented through later reuse or specialization rather than being incorporated into these definitions.

## Validated Competency Specifications

### C07 — Develop Problem-Solving Solutions Using Turing Machines

This competency is the ability to design and implement a computational solution using a Turing Machine as a formal model. It involves interpreting well-defined requirements, translating them into an abstract machine specification, and constructing a model that realizes the intended behavior.

Learners coordinate states, transition functions, tape symbols, and input/output behavior to produce a logically correct and internally coherent machine. In Task02, the competency concerns direct modeling and simulation of the traffic-classification and counting problem.

### C08 — Identify Turing Machine Variants

This competency is the ability to recognize, describe, and differentiate variants of Turing Machines, such as multi-tape and nondeterministic models, based on their structural characteristics and operational properties.

In Task02, the emphasis is on conceptual understanding and classification. Learners identify the characteristics of predefined variants without being required to make broader architectural decisions or compare their theoretical computational power.

### C09 — Apply Turing Machine Variants

This competency is the ability to apply predefined Turing Machine variants, such as multi-tape or nondeterministic models, to represent or simulate a solution for a well-defined problem.

Learners analyze the task requirements and use an appropriate provided variant to improve modeling clarity or structural organization while preserving the required behavior. The competency emphasizes guided application and adaptation rather than theoretical comparison or optimization.

### C10 — Test Turing Machines Using Simulators

This competency is the ability to test, validate, and refine Turing Machine models using JFLAP or an equivalent simulation environment.

Learners:

- execute Turing Machine configurations and test transitions and halting conditions;
- compare observed execution traces and outputs with the expected results;
- identify errors such as incorrect transitions, missing states, or improper tape handling; and
- refine the model through structured testing and debugging.

### C05 — Write a Technical Report

This competency is reused from Task01. It concerns applying written communication to structure, explain, revise, and refine the technical report required by Task02.

## Validated Competency Summary

| ID | Competency | Dispositions | Knowledge | Skill |
| --- | --- | --- | --- | --- |
| C07 | Develop Problem-Solving Solutions Using Turing Machines | Collaborative, Responsible, Proactive, Creative, Inventive | Turing Machines | Create (Develop, Invent, Construct) |
|  |  |  | Requirements Engineering | Apply (Interpret, Organize) |
|  |  |  | Analytical and Critical Thinking (FPK) | Apply (Decompose, Identify) |
| C08 | Identify Turing Machine Variants | Investigative, Collaborative, Responsible, Proactive | Turing Machines | Understand (Differentiate, Recognize, Explain) |
|  |  |  | Analytical and Critical Thinking (FPK) | Apply |
| C09 | Apply Turing Machine Variants | Inventive, Responsible, Proactive, Collaborative, Creative | Turing Machines | Apply (Use, Adapt, Implement) |
|  |  |  | Analytical and Critical Thinking (FPK) | Apply |
| C10 | Test Turing Machines Using Simulators | Collaborative, Responsible, Proactive, Creative | Turing Machines | Apply (Simulate, Evaluate, Verify) |
|  |  |  | Problem Solving and Troubleshooting (FPK) | Apply (Diagnose, Debug, Refine) |
|  |  |  | Modeling and Simulation | Apply |
| C05 | Write a Technical Report *(reused)* | Collaborative, Meticulous, Responsible | Written Communication (FPK) | Apply (Write, Structure, Revise, Refine) |

## Conclusion

The implemented adjustments remove knowledge not operationalized by the task, refine the terminology and granularity of the remaining knowledge components, and clarify the boundaries among the Turing Machine competencies. The validated Task02 specification provides the input for semantic structuring and later controlled reuse or specialization.
