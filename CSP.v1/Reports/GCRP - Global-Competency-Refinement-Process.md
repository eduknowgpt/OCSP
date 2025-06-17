## Global Competency Refinement Process (GCRP)

### 1. Purpose and Motivation

While the **Competency Specification Process (CSP)** and the **Competency Specification Review Process (CSRP)** focus on identifying and validating competencies in relation to specific educational tasks, there remains a need for a **higher-level semantic analysis** across the entire set of competencies defined throughout the project.

The **Global Competency Refinement Process (GCRP)** is introduced as a complementary process designed to analyze the **repository of specified competencies as a whole**, with support from their formal representation in the **OntoKSD ontology**. Its primary goal is to infer **generalizations, specializations, and structural relationships** among competencies that emerge from multiple tasks, thereby enhancing **semantic coherence**, **curricular reusability**, and **support for automated reasoning**.


### 2. Objectives

* Identify **recurrent patterns** and overlapping scopes across task-specific competencies.
* Define **meta-competencies** that aggregate or generalize more specific ones.
* Detect **gaps, redundancies, or inconsistencies** in the competency repository.
* Refine the **granularity and hierarchical organization** of competencies.
* Establish **explicit ontological relationships** such as:

  * `ontoksd:hasComponent`
  * `ontoksd:isSpecializationOf`
  * `ontoksd:isBroaderThan`
  * `ontoksd:requiresCompetence`

* Enable **ontology-driven reasoning** for validation, evidence inference, and curriculum design support.



### 3. Process Phases

| **Phase**                                | **Description**                                                                                                                                                                            |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **1. Collection**                        | Gather all competencies specified and reviewed through CSP and CSRP, including metadata, task associations, and instantiations in OntoKSD.                                                 |
| **2. Thematic Clustering**               | Group competencies by domain (e.g., Automata Theory), knowledge area (e.g., FSM, PDA, TM), or taxonomy (e.g., Bloom’s levels, CC2020 categories).                                          |
| **3. Overlap and Specificity Analysis**  | Analyze similarities, abstraction levels, and content overlap among competencies to identify opportunities for generalization or refinement.                                               |
| **4. Definition of Meta-Competencies**   | Formulate new, generalized competencies that semantically encompass more specific ones—e.g., “Develop Problem-Solving Solutions Using Automata” as an umbrella for FSM, PDA, and TM.       |
| **5. Ontological Relationship Encoding** | Formalize relationships in OntoKSD using OWL/RDF properties (e.g., `hasComponent`), enabling SPARQL queries and DL reasoning to automate aggregation or prerequisite validation. |
| **6. Repository Update**                 | Incorporate the new meta-competencies and semantic relationships into the central repository and the ontology, improving navigation, consistency, and alignment with instructional design. |



### 4. Example: Automata-Based Competency Aggregation

The following hierarchical structure emerged from the global analysis conducted after the full CSP-CSRP cycles—including **Tasks 01–05** and **Tasks 201–204**:

```
C05: Develop Problem-Solving Solutions Using Automata
│
├── C12: Develop Problem-Solving Solutions Using Finite State Machines (FSM)
├── C14: Develop Problem-Solving Solutions Using Pushdown Automata (PDA)
└── C09: Develop Problem-Solving Solutions Using Turing Machines (TM)
```

In this structure, **Develop Problem-Solving Solutions Using Automata** is defined as a **meta-competence** that subsumes three task-specific competencies, each corresponding to a formal computational model within the **Chomsky Hierarchy**.

By representing these relations in OntoKSD, it becomes possible to:

* **Automatically infer** the demonstration of the meta-competence if all components are evidenced.
* Support **competency-based curriculum design** with rules and validations based on semantic inference.
* Enable SPARQL-based queries to track student progress or design instructional trajectories.



### 5. Benefits of GCRP

* Provides a **systemic and unified understanding** of the competency landscape.
* Improves **semantic precision** and eliminates redundancy or terminological ambiguity.
* Enables **ontology-driven automation** of competency aggregation, evidence tracking, and curriculum scaffolding.
* Supports **reusability and composability** of competencies across tasks, courses, and learning paths.
* Facilitates **analytics and visualization** through SPARQL queries and reasoning tools (e.g., OWL reasoners).
* Aligns educational design with **formal knowledge representation principles**, enhancing transparency and interoperability.
