## CSP Phase 3 — Semantic Structuring

CSP Phase 3 organizes reviewed competence specifications into a coherent semantic structure supported by OntoKSD. While earlier phases focus on instructional entity analysis and task-level competence specification, this phase treats competences as a repository, enabling reuse, specialization, aggregation, and external alignment.

The goal is not to proliferate competences, but to control their evolution. New competences should only be created when existing ones cannot adequately represent the intended meaning. Otherwise, competences should be reused, specialized, or linked to new instructional contexts through explicit OntoKSD constructs.

Semantic structuring enhances curriculum coherence by making relationships among competences explicit. It supports the distinction between atomic and composite competences, controlled specialization, reuse across tasks, and alignment with external frameworks such as CC2020, CS2023, and BNCC Computing.



### Semantic Structuring Guidelines

1. **Check for reusable competences**
   Review the repository before creating new competences. Prefer reuse when the same competence can be activated in a new context without semantic change.

2. **Identify overlaps and redundancies**
   Detect near-duplicates or terminological inconsistencies. Merge, rename, or relate equivalent competences as needed.

3. **Generalize when reuse is too narrow**
   If a competence is overly tied to a specific task or artifact, abstract its core meaning to increase applicability.

4. **Specialize when context requires precision**
   When a competence is too broad, create a controlled specialization that preserves its conceptual base while adding contextual constraints.

5. **Aggregate into composite competences**
   Group complementary competences when meaning depends on their coordinated mobilization.

6. **Separate activation from competence identity**
   Do not create new competences solely due to contextual variation. Represent usage through activation (e.g., target, required, assessed).

7. **Document external alignment explicitly**
   Link competences to frameworks (e.g., CC2020, CS2023, BNCC) without replacing internal OntoKSD definitions.

8. **Record modeling rationale**
   Document the reasoning behind reuse, specialization, aggregation, or creation decisions.

9. **Encode relations in OntoKSD**
   Represent validated relations in RDF/OWL while preserving human-readable documentation.



### Inputs

* Reviewed competence specifications from prior CSP phases
* Instructional entity analysis reports
* Reviewer feedback and implemented revisions
* Existing OntoKSD competence repository
* Controlled vocabularies (knowledge, skills, Bloom levels, dispositions)
* External curricular frameworks (when applicable)



### Outputs

* **Semantically organized competence set**
  (reuse, specialization, aggregation, or creation)

* **Explicit competence relations**
  (e.g., specialization, aggregation, equivalence, dependency, alignment)

* **Activation-aware mappings**
  (distinguishing competence identity from contextual use)

* **External alignment records**
  (links to CC2020, CS2023, BNCC, etc.)

* **Rationale documentation**
  (supporting traceability and future reuse)

* **RDF/OWL-ready representations**
  (for ontology instantiation and querying)



### Conclusion

Semantic structuring transforms isolated competence specifications into a coherent and reusable repository. By enabling controlled reuse, specialization, aggregation, and contextual activation, this phase strengthens both consistency and maintainability.

A key principle in OntoKSD is the separation between competence identity and instructional activation. This allows the same competence to be reused across contexts, activated differently, linked to diverse evidence, and aligned with external frameworks—without semantic drift.

The resulting structure supports both human interpretation and machine-processable representation, enabling ontology instantiation, querying, validation, and curriculum analysis in competency-oriented Computing Education.


