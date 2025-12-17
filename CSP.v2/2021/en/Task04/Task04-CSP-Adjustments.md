# **CSP Review Adjustments Report: Task 04 – *The Return of the Farmer Robot***

## **Introduction**

Based on the outcomes of the **expert review (CSRP – Phase 2)**, this report documents the **adjustments implemented during the CSP-Adjustments stage** for *Task 04 – The Return of the Farmer Robot*. The purpose of this report is to explicitly register the **concrete modifications applied to the competency specifications**, ensuring traceability between expert recommendations and the finalized competency model.

The review process identified **key improvement dimensions** that guided the implemented changes:

* **Knowledge Granularity** — refining broad concepts into task-relevant and assessable knowledge units;
* **Knowledge Appropriateness** — aligning declared knowledge with the computational models genuinely required by the task;
* **Controlled Vocabulary** — standardizing terminology to ensure conceptual precision and reuse across tasks;
* **Bloom’s Taxonomy Verbs** — refining action verbs to accurately reflect intended cognitive engagement;
* **Textual Clarity** — revising descriptions to eliminate ambiguity and improve instructional readability.

In response to these findings, **targeted refinements were implemented** to enhance the **conceptual coherence, pedagogical alignment, and reusability** of the competency specifications. These adjustments ensure that the competencies are **faithfully aligned with the task’s computational demands**—particularly those involving **memory-dependent navigation and return behavior**—and are ready for **Phase 3 – Semantic Structuring** within the CSP.



## **Revised Competency Specification for Task 04**

### **Competency Reuse**

Two previously specified competencies are **reused without modification** in the context of *Task 04 – The Return of the Farmer Robot*:

* **Testing Automata Using Simulators**
* **Write a Technical Report**

The expert review confirmed that both competencies remain **fully applicable** to Task 04 and are aligned with the same **Target Audience Profile**. Their reuse is justified as follows:

* **Testing Automata Using Simulators**
  This competency supports learners’ ability to **implement, execute, and verify PDA-based navigation models** using simulation tools such as *JFLAP*. Simulation and validation of automata behavior constitute a **core activity** of Task 04, particularly in evaluating stack-based return-path logic.

* **Write a Technical Report**
  This competency reflects the requirement that learners **document modeling decisions, formal notations, and system behavior** using structured technical formats (e.g., SBC standards). Clear and systematic reporting is integral to both the learning process and the assessment strategy of the task.

Given that these competencies **naturally emerge from the instructional context** and directly support the task’s execution and evaluation, the reviewers recommended their **verbatim reuse**. This decision promotes **consistency across tasks**, **efficiency in competency modeling**, and **alignment between competency definitions, learner activities, and assessment practices**.





### Competency C12 Specification

#### Competency Title

  Develop problem-solving solutions using Pushdown Automata

#### Textual Description

This competency addresses the ability to design, construct, and validate computational models based on Pushdown Automata (PDAs) to represent behaviors that require stack-based memory and context-sensitive control. Learners are expected to model systems in which memory is essential for tasks such as backtracking, recognition of nested structures, and sequential navigation.

Demonstrating this competency requires understanding how state transitions, input symbols, and stack operations interact to govern system behavior. Students must apply formal principles to construct PDA models that are logically correct, computationally adequate, and aligned with task-specific requirements.

Through this competency, learners develop the capacity to apply formal automata-based reasoning to practical problem scenarios—such as robotic navigation, language parsing, or symbolic processing—bridging theoretical foundations with effective computational solutions.


#### Table for Competency C12

| **Competency**                                            | **Dispositions**                                               | **Knowledge**                          | **Skill**                  |
| --------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------- | -------------------------- |
| Develop problem-solving solutions using Pushdown Automata | Inventive, Collaborative, Responsible, Proactive, Creative | Pushdown Automata                      | **Create (Design, Develop, Construct)** |
|                                                           |                                                                | Requirements Engineering               | **Apply (Interpret, Specify, Translate)**             |
|                                                           |                                                                | Analytical and Critical Thinking | **Apply**                  |





### Competency C13 Specification

#### Competency Title

  Interpret rule-based notation

#### Textual Description

This competency involves the ability to understand and interpret formal rule-based notations, such as context-free grammars, used to define and control system behavior through structured symbol sequences. Learners are expected to analyze how production rules govern valid sequences of operations, enabling the representation of decision-making logic, procedural flows, or communication protocols.

This competency is applicable across domains that require symbolic modeling, such as language processing, robotic control, and formal specification. It emphasizes the comprehension of syntax and rule hierarchies, and the capacity to interpret how such notations define constraints and guide execution within computational systems.

#### Knowledge Specification

The following knowledge areas are essential for mastering this competency:

* Context-Free Grammars and Regular Languages (Context-Free Languages)
  * Understand how these formal languages define structured symbol sequences and how to construct grammars for recognizing or generating specific behavior patterns.

* Pushdown Automata 
  * Understand the correspondence between rule-based languages and automata capable of recognizing them, particularly the role of memory in parsing nested structures.

* Analytical and Critical Thinking 
  * Apply reasoning skills to interpret rule sets, validate symbolic behavior representations, and refine grammars for clarity, completeness, and correctness.


#### Knowledge-Skill Pairing

#### Mapping Knowledge to Skills
To demonstrate this competency, students must be able to:

* **Understand** knowledge of Context-Free Grammars and Regular Languages to interpret and construct rule-based representations that define valid symbol sequences governing system behavior.
    * Verbs: Interpret, Construct, Relate

* **Understand** knowledge of Pushdown Automata to recognize the computational mechanisms capable of processing rule-based structures—particularly those involving hierarchy, recursion, or nested patterns—and relate these models to the expressive power of the grammars.
    * Verbs: Recognize, Explain, Compare

* **Apply** Analytical and Critical Thinking to examine rule sets, detect inconsistencies or ambiguities, and refine grammar structures to enhance correctness, clarity, and applicability in the system’s domain.
    * Verbs: Analyze, Refine, Validate

#### B.6 Table for Competency C13

| **Competency**                | **Dispositions**                                               | **Knowledge**                          | **Skill**                  |
| ----------------------------- | -------------------------------------------------------------- | -------------------------------------- | -------------------------- |
| Interpret rule-based notation | Inventive, Collaborative, Responsible, Proactive, Creative | Pushdown Automata                      | **Understand (Recognize, Explain, Compare)**             |
|                               |                                                                | Context-Free Grammars                      | **Understand ( Interpret, Construct, Relate)** |
| | | Regular Languages                      | **Understand (Interpret, Construct, Relate)** |
|                               |                                                                | Analytical and Critical Thinking  | **Apply (Refine, Validate)**                  |




### Competency C14 Specification

#### Competency Title

  Differentiate classifications of formal grammars

#### Textual Description

This competency focuses on the ability to understand and differentiate between formal grammar classes, such as regular and context-free grammars, along with their respective computational models (e.g., finite automata and pushdown automata). Learners are expected to analyze the structural characteristics and expressive power of each grammar type and to evaluate their suitability for modeling different types of symbolic control systems or language-based behaviors.

The competency supports critical understanding of the Chomsky hierarchy, enabling students to classify problems according to their grammatical complexity and to make informed decisions when selecting formal representations for system design or analysis.


#### Knowledge Specification

The following knowledge areas are essential for mastering this competency:

* **Context-Free Languages**
    * Understand the principles of context-free grammars, including their structure, derivation rules, and ability to describe hierarchical patterns. Recognize their expressive limits and the types of automata (e.g., pushdown automata) used to recognize these languages.

* **Regular Languages**
    * Understand the definition and construction of regular grammars and the corresponding use of finite automata to represent flat or repetitive patterns. Identify the limitations of regular languages in comparison to context-free languages.

* **Analytical and Critical Thinking**
    * Apply logical reasoning to compare grammar classes based on structure, expressiveness, and computational requirements. Evaluate which grammar type is most appropriate for modeling specific system behaviors and justify the classification based on formal criteria.

#### C.4 Knowledge–Skill Pairing

#### C.4.1 Mapping Knowledge to Skills

To effectively demonstrate this competency, students must be able to:

* **Understand** knowledge of Context-Free Languages
    * Verb association: Recognize, Describe, Differentiate
    * Learners should be able to recognize structural characteristics of context-free grammars, describe their derivation patterns, and differentiate their expressive capabilities from those of regular languages.

* **Understand** knowledge of Regular Languages
    * Verb association: Identify, Classify, Compare
    * Learners must identify features of regular grammars and finite automata, classify language constructs according to grammatical complexity, and compare regular and context-free languages in terms of expressiveness and modeling potential.

* **Apply Analytical** and Critical Thinking
    * Learners should analyze the suitability of different grammar types for specific modeling scenarios, contrast their structural and computational properties, and justify the selection of a grammar class based on system requirements.


#### C.5.2 Bloom’s Taxonomy Alignment
This competency engages the following levels of cognitive processing:

* **Understand** – For identifying, describing, and classifying grammar types and their structural features.

* **Apply** – For analyzing modeling needs and selecting appropriate grammar classes based on formal criteria and system constraints.


#### C.6 Summary Table for Competency D

| **Competency**                                   | **Dispositions**                                     | **Knowledge**                          | **Skill**                          |
| ------------------------------------------------ | ---------------------------------------------------- | -------------------------------------- | ---------------------------------- |
| Differentiate classifications of formal grammars | Inventive, Collaborative, Responsible, Proactive | Regular Languages                        | **Understand (Identify, Classify, Compare)** |
|                                                  |                                                      | Context-Free Languages | **Understand (Recognize, Describe, Differentiate)**                          |
|                                                  |                                                      | Analytical and Critical Thinking | **Apply**                          |


### **Unified Summary Table for Competencies A, B, and C**

Claro! Aqui está a **tabela unificada** com todas as informações combinadas das competências A, B e C. Ela mantém uma estrutura consistente, evitando duplicações de competências ou conhecimentos, e alinhando claramente **disposições**, **conhecimentos** e **habilidades com verbos anotados** segundo a Taxonomia de Bloom.

---

### **Unified Summary Table for Competencies A, B, and C**

| **ID**  | **Competency**  | **Dispositions**  | **Knowledge** | **Skill**  |
|---------|-----------------|-------------------|---------------|------------|
|  (C12)  | **Develop problem-solving solutions using Pushdown Automata** | Inventive, Collaborative, Responsible, Proactive, Creative | Pushdown Automata                | **Create (Design, Develop, Construct)**                          |
|                                                           |                                                            | Requirements Engineering         | **Apply (Interpret, Specify, Translate)**                      |
|                                                           |                                                            | Analytical and Critical Thinking | **Apply** (*Decompose, Evaluate*)                     |
|                                        |                                                    |
|  (C13) | **Interpret rule-based notation**                             | Inventive, Collaborative, Responsible, Proactive, Creative | Pushdown Automata                | **Understand** (*Recognize, Explain, Compare*)        |
|                                                           |                                                            | Context-Free Grammars            | **Understand** (*Interpret, Construct, Relate*)       |
|                                                           |                                                            | Regular Languages                | **Understand** (*Interpret, Construct, Relate*)       |
|                                                           |                                                            | Analytical and Critical Thinking | **Apply** (*Refine, Validate*)                        |
|                                        |                                                    |
|  (C14)  | **Differentiate classifications of formal grammars**          | Inventive, Collaborative, Responsible, Proactive           | Regular Languages                | **Understand** (*Identify, Classify, Compare*)        |
|                                                           |                                                            | Context-Free Languages           | **Understand** (*Recognize, Describe, Differentiate*) |
|                                                           |                                                            | Analytical and Critical Thinking | **Analyze**                      |
|  |  |                                        |       |       
|  (C03)  |  *Test automata using simulators (REUSED)* | Investigative, Collaborative, Responsible, Proactive, Creative | Finite State Machines | Apply (Experiment, Relate, Simulate) |
|         |                                                                   | Problem Solving and Troubleshooting (FPK) | Apply |
|         |                                                                   | Modeling and Simulation | Apply |
|  |  |                                        |       |       
|  (C05)  | *Write a technical report (REUSED)* | Collaborative, Meticulous, Responsible | Written Communication (FPK) | Apply |

