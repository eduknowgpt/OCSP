# CSP Phase 3 — Semantic Structuring of Competencies for TASK25-00

## 1. Context and Scope

The instructional entity **TASK25-00 — Music Collection** requires learners to address a single, coherent problem involving the **formal modeling, manipulation, and justification of musical collections as formal languages**.  

Although the task is assessed through a unified mathematical report, its successful completion depends on the **integration of multiple distinct competencies**, each addressing a specific conceptual or epistemic dimension of Formal Languages and Theory of Computation.

In accordance with **CSP Phase 3 — Semantic Structuring**, the competencies associated with TASK25-00 were analyzed to identify **semantic roles, hierarchical relations, and compositional structures**, ensuring **modularity, reusability, and coherence** within the **OntoKSD ontology**.



## 2. Identification of Competency Roles

Based on scope, granularity, and pedagogical function, the competencies involved in TASK25-00 were classified into three semantic categories:

1. **Specialized (Atomic) Competencies**  
2. **Intermediate / Cross-Cutting Competencies**  
3. **Aggregated Task-Level Competency**

This classification supports explicit modeling of **generalization, specialization, and aggregation relations**.



## 3. Specialized (Atomic) Competencies

The following competencies are classified as **specialized**, as each targets a **well-defined conceptual capability** that can be reused across tasks and instructional contexts:

- **C17 — Apply operations on formal languages**  
  Focuses on algebraic manipulation of languages and reasoning about closure properties.

- **C18 — Model real-world problems using formal language concepts**  
  Addresses abstraction of concrete domains into symbols, strings, and languages.

- **C19 — Apply homomorphisms in formal languages**  
  Concerns formal mappings between representations and analysis of equivalence limits.

- **C04 — Specify languages using regular expressions**  
  Covers algebraic specification of regular languages.

- **C13′ — Justify formal properties using logical and mathematical argumentation**  
  Targets proof-oriented reasoning and epistemic justification.

- **C05′ — Produce mathematically rigorous technical documentation**  
  Addresses formal written communication.

### Semantic Role

These competencies are:

- conceptually **atomic**;
- **independently reusable** across multiple tasks;
- **necessary but not sufficient** to characterize the full performance required by TASK25-00.



## 4. Aggregated Task-Level Competency (C20)

To represent the **integrated performance** expected in TASK25-00, the following **composite competency** was introduced into the OntoKSD catalog:

> **C20 — Model and analyze real-world domains as formal languages**

### Rationale for Aggregation

Following CSP Phase 3 Guideline 4 (*Aggregate complementary competencies*), C20 aggregates competencies that:

- frequently co-occur in formal language analysis tasks;
- collectively define a **higher-order capability**;
- are assessed through a **single holistic artifact**.

C20 therefore functions as the **semantic anchor** of TASK25-00.



## 5. Semantic Relations Between Competencies

### 5.1 Composition Relations

C20 is formally defined as a **composite competency** that *composes* the following specialized competencies:

```text
C20 composes C17
C20 composes C18
C20 composes C19
C20 composes C04
C20 composes C13′
C20 composes C05′
```

This relation expresses that demonstrating C20 entails demonstrating each of its component competencies.


### 5.2 Task–Competency Relation

The instructional entity TASK25-00 is linked to C20 through the relation:

TASK25-00 targetsCompetence C20


This ensures a clear separation between:
- context-specific instructional entities (tasks), and
- context-independent competencies (catalog-level).


## 6. Generalization and Reuse Considerations

Although TASK25-00 is contextualized in the musical domain, the competencies involved — including C20 — are **domain-independent by design**.

From a semantic structuring perspective:

- C18 generalizes abstraction of real-world domains;

- C17 generalizes algebraic reasoning over languages;

- C19 generalizes representational mappings;

- C20 generalizes the integration of these capabilities.

As a result, C20 can be reused and specialized in tasks involving other symbolic domains, such as biological sequences, communication protocols, or programming language syntax.


## 7. OntoKSD Encoding Implications

Within the OntoKSD ontology:

- C20 is modeled as an instance of CompositeCompetence;

- its components are linked via hasSubCompetence;

- TASK25-00 references C20 through targetsCompetence.

This structure enables:

- automated inference of demonstrated sub-competencies;

- curriculum-wide coherence analysis;

- learning pathway generation;

- semantic validation of competency coverage.


## 8. Conceptual Structure Overview

````
TASK25-00
   └── targetsCompetence
        └── C20 — Model and analyze real-world domains as formal languages
              ├── composes C18 (Modeling)
              ├── composes C17 (Operations)
              ├── composes C19 (Homomorphisms)
              ├── composes C04 (Regular Expressions)
              ├── composes C13′ (Formal Justification)
              └── composes C05′ (Technical Communication)

````

## 9. Specialization of Catalog Competencies (C05′ and C13′)

During the semantic structuring of competencies for **TASK25-00**, two competencies from the reference catalog — **C05** and **C13** — were identified as **necessary but insufficient in their original form**.  
Both required **task-specific specialization** to adequately reflect the epistemic and representational demands of the problem.



### 9.1 Specialization of C13 → C13′ (Algebraic Notation for Strings and Languages)

**C13 — Interpret rule-based notation** broadly addresses the comprehension of formal notations, such as grammars and rule-based systems. However, the *Music Collection* task does not require grammar construction or rule interpretation per se. Instead, it requires **precise manipulation of algebraic notation over strings and languages**.

The task explicitly mobilizes:

- ε, Σ, Σ\*, |x|;
- concatenation, powers (xⁿ), and reversal (xᴿ);
- language operations (∪, ∩, complement, Lⁿ, L\*);
- substrings, prefixes, and suffixes;
- homomorphisms and codifications.

To capture this narrower but deeper requirement, **C13′** was defined as a **specialization of C13**, focusing on **algebraic and symbolic manipulation** rather than rule-based grammar interpretation.

```text
C13′ specializes C13
```
This specialization preserves the conceptual core of C13 while aligning it with the formal language algebra emphasized in the task.


### 9.2 Specialization of C05 → C05′ (Mathematically Rigorous Argumentation)

**C05 — Write a technical report** emphasizes clarity, structure, and documentation of results. While necessary, this competency does not fully capture the mathematical rigor demanded by TASK25-00.

The task requires students to:

- state formal definitions;

- construct minimal examples;

- provide proofs and justifications (including closure and induction);

- present counterexamples when claims are false;

- explicitly distinguish between intuition, example, and proof.

These requirements motivate the definition of C05′, a specialization of C05 focused on formal mathematical exposition and epistemic rigor.

````
C05′ specializes C05
````

C05′ thus reflects a discipline-specific refinement of technical communication appropriate to Formal Languages and Theory of Computation.


### 9.3 Role of C05′ and C13′ in the Competency Structure

Both C05′ and C13′ are:

- specialized competencies derived from catalog-level definitions;

- reusable across multiple FLTC tasks;

- essential components of the aggregated task-level competency C20.

They ensure that the competency model captures not only what students do, but how rigorously and formally they must do it.


### 9.4 Resulting Semantic Relations

````
C13′ specializes C13
C05′ specializes C05
C20 composes C13′
C20 composes C05′
````
These relations reinforce the semantic coherence, modularity, and reusability of the competency model within the OntoKSD framework.


## 10. Conclusion

The CSP Phase 3 semantic structuring of **TASK25-00** transforms an initially fragmented set of competency specifications into a **coherent, modular, and reusable competency network**. By explicitly modeling **specialization, aggregation, and composition relations**, this structuring clarifies the functional role of each competency within the task and across the broader curriculum.

Specifically, the resulting structure:

- aligns **assessment practices** with **integrated task-level performance**, rather than isolated skill execution;
- preserves the **reusability of specialized competencies**, enabling their application across multiple tasks and domains;
- supports **ontological reasoning and inference** within the OntoKSD framework, facilitating validation, traceability, and automated analysis;
- enhances **curricular scalability and maintainability**, allowing competency models to evolve without loss of coherence.

Overall, this case demonstrates how **CSP Phase 3** elevates competency modeling from task-bound, ad hoc descriptions to a **conceptually robust, interoperable, and semantically grounded framework**, capable of supporting both human interpretation and machine-based reasoning in competency-based education.
