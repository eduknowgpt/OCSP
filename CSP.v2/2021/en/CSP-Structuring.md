## CSP Phase 3 – Semantic Structuring Report: Enhancing Reusability and Coherence in Competency Models


### Automata-Based Competency Aggregation

Following the completion of the full CSP cycles across **Tasks 01 to 05**, a semantic consolidation process revealed a clear hierarchical pattern within the domain of **automata-based problem solving**. This led to the formulation of an aggregated, reusable competency structure grounded in formal computational models:

```
C05: Develop Problem-Solving Solutions Using Automata
│
├── C12: Develop Problem-Solving Solutions Using Finite State Machines (FSM)
├── C14: Develop Problem-Solving Solutions Using Pushdown Automata (PDA)
└── C09: Develop Problem-Solving Solutions Using Turing Machines (TM)
```

In this structure:

* **C05** functions as a **meta-competency** that abstracts the core ability to design, construct, and validate automaton-based solutions for computational problems.
* Each child competency—**C12**, **C14**, and **C09**—represents a concrete instantiation tied to a distinct level of the **Chomsky Hierarchy**, respectively addressing:

  * Finite-State Machines (Regular Languages)
  * Pushdown Automata (Context-Free Languages)
  * Turing Machines (Recursively Enumerable Languages)

This hierarchical organization reflects both theoretical foundations and practical instructional contexts, enabling vertical integration across tasks and levels of complexity.

#### Ontological Encoding and Pedagogical Implications

By formally encoding these relationships in the **OntoKSD ontology**, the following affordances become possible:

* **Semantic Inference**: If evidence of C12, C14, and C09 is recorded (e.g., through learning tasks or assessment artifacts), inference rules can deduce that C05 has been satisfied—enabling automated tracking of broader capabilities.

* **Curricular Design Support**: Curriculum planners can define instructional paths that scaffold from specific to general competencies, facilitating vertical alignment and modular reuse across learning units.

* **Learning Analytics and Querying**: Using SPARQL queries over the OntoKSD triple store, stakeholders can retrieve:

  * Learners who satisfy a meta-competency
  * Which automata-based model(s) a learner has demonstrated proficiency in
  * Gaps in the pathway toward achieving broader problem-solving competencies

* **Competency Validation**: Educators can validate whether learners have achieved an overarching learning outcome even when it is not directly assessed, based on the aggregation of semantically related, evidentiated competencies.

This aggregation serves as a model for other families of computational competencies, establishing a scalable pattern for structuring knowledge, skills, and dispositions in a way that supports adaptive and evidence-based education.






