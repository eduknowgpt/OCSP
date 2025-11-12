# About OntoKSD

**OntoKSD** (*Ontology for Knowledge–Skill–Disposition*) is an ontology developed to formally represent educational competencies in the domain of Computing, according to the *Competency-Based Education* (CBE) model and the international references of **ACM/IEEE CC2020**.
It enables the description of a competence as a composite entity that articulates three fundamental dimensions:

1. **Knowledge (K)** – the conceptual or factual knowledge that the student must mobilize;
2. **Skill (S)** – the cognitive or practical action that the student must perform, associated with a level of Bloom’s Taxonomy (e.g., *Understand, Apply, Analyze, Create*);
3. **Disposition (D)** – the attitudes, values, or postures demonstrated by the student while performing the task (e.g., *meticulous, collaborative, ethical*).

This structure aims to make competencies **observable, assessable, and semantically interoperable**, allowing them to be reused, validated, and aligned with reference frameworks (BNCC Computing, CC2020, CS2023, etc.).

In the context of this task — **Implementation of the Tic-Tac-Toe Game** — OntoKSD is applied to map programming learning (data structures, control flow, modularization, and communication) to evidence of performance and observable dispositions during practical activity and oral assessment.

## Meaning of (KS) Pairs

**(KS) pairs** represent the association between a specific knowledge and a cognitive skill derived from Bloom’s Taxonomy. Each pair defines **what** the student mobilizes (K) and **what they do** with that knowledge (S) in the context of the task.

**Knowledge (K)** is always identified from standardized vocabularies (CC2020, CS2013, BNCC Computing, or fundamental domains such as `AnalyticalThinking`, `DataStructures`, `RequirementsSpecification`).

**Skill (S)** is a cognitive action verb — such as *Understand, Apply, Analyze, Create* — that expresses the expected level of proficiency and is mapped in the ontology through the property `hasBloomLevel`.

**Example:**

**(KS): Data Structures / Apply**
The student uses their knowledge of **data structures** (K) to **apply** (S) lists or arrays in the game’s representation.

## Meaning of Dispositions (D)

**Dispositions (D)** represent attitudes and observable behavioral traits that qualify the way the student applies knowledge and skill. They do not describe **what** the student knows or does, but **how** they act cognitively and socially while doing so.

These dispositions may be of the following nature:

* **Cognitive**: meticulous, analytical, creative;
* **Interpersonal**: collaborative, communicative;
* **Ethical and professional**: responsible, ethical.
