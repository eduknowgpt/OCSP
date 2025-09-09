# CSP Phase 3 – Semantic Structuring Report: Enhancing Reusability and Coherence in Competency Models


The third phase of the **Competency Specification Process (CSP)** focuses on the *semantic structuring* of competencies that were previously specified and validated in Phases 1 and 2. This stage leverages outputs from multiple CSP cycles to detect ontological patterns, define taxonomic and part-whole relationships, and organize competencies into hierarchies that reflect both theoretical foundations and instructional logic.

## Dual Representation: Abstract and Composite Competencies

During semantic analysis in the **automata-based problem-solving domain**, it became evident that a single high-level learning outcome needed to be represented in *two distinct but complementary forms* within the **OntoKSD ontology**:

1. **Abstract (Taxonomic) Competence** — serving as a *general superclass* in a subsumption hierarchy.
2. **Composite (Aggregative) Competence** — representing the *combined mastery* of several component competencies.

This modeling choice reflects a fundamental distinction: an *abstract competence* (also referred to as a *generalization node*) does not imply that its specializations must all be mastered simultaneously, while a *composite competence* explicitly requires demonstrated proficiency in *all* its component parts.

## Subsumption Hierarchy in Automata-Based Problem Solving

Following the specification and review of competencies in **Tasks 01–05**, a clear subsumption hierarchy emerged:


```
C01_ABS: Develop Problem-Solving Solutions Using Automata (Abstract)
|
|--- C06: Develop ... Using Finite State Machines (FSM)
|--- C12: Develop ... Using Pushdown Automata (PDA)
|--- C07: Develop ... Using Turing Machines (TM)
```


In this structure:

- **C01_ABS** is an *abstract* superclass that generalizes competencies for three major classes of automata in the **Chomsky Hierarchy**.
- **C06**, **C12**, and **C07** are *specializations* of C01_ABS, contextualized respectively in:
  - **C06**: FSM — Regular Languages
  - **C12**: PDA — Context-Free Languages
  - **C07**: TM — Recursively Enumerable Languages

A separate **C01_CC** instance models the *composite* version of C01, in which mastery requires demonstrable evidence for *all* three component competencies (C06, C12, C07). This dual modeling supports both taxonomic reasoning and explicit aggregation for curriculum and assessment.

This composite representation follows the **Composite Competence** concept as defined in the *Computing Curricula 2020* (CC2020) [@CC2020], in which a competence is achieved through the demonstrable mastery of all its constituent competencies. The aggregation is not merely taxonomic but reflects an intentional instructional design pattern that groups interdependent competencies toward a broader learning outcome.

## Ontological Encoding and Pedagogical Implications

The formal encoding of this two-level representation in the OntoKSD ontology enables several semantic and pedagogical affordances:

- **Subsumption Reasoning and Inference Support**  
  In OWL ontologies, if a learner demonstrates C06, C12, or C07, a reasoner can infer that they hold the *abstract* competence C01_ABS (unless competencies are declared disjoint). In the *composite* variant C01_CC, the reasoner infers mastery only when *all* components are evidenced.
  
- **Support for Curricular Scaffolding**  
  The hierarchy informs course design, allowing learners to progress from FSMs to PDAs and then to TMs, converging on the general learning outcome C01_ABS. C01_CC formalizes a milestone requiring comprehensive mastery.
  
- **Learning Analytics and Progression Tracking**  
  With this structure, SPARQL queries can:
  - Identify learners who have met abstract vs. composite versions of a competence.
  - Detect partial completion toward composite milestones.
  - Generate coverage reports across learning cohorts.
  
- **Competency Validation through Aggregation**  
  From an assessment perspective, C01_CC allows explicit validation of high-level outcomes through the accumulation of evidence across its components, whereas C01_ABS supports broader inference without aggregation constraints.

## Conclusion

The dual modeling of **C01** as both *abstract* and *composite* competence represents a significant refinement in Phase 3 of the CSP. It reconciles ontological best practices with pedagogical needs, enabling fine-grained control over inference, progression tracking, and assessment. This approach ensures that the competency structure remains both semantically precise and instructionally actionable, supporting coherent curriculum design and robust learning analytics.
