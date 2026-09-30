## CSP Phase 3 — Semantic Structuring

CSP Phase 3 organizes validated competency specifications into a coherent semantic structure. While the earlier phases focus on instructional entity analysis, competency specification, and expert review, this phase analyzes competencies as a set, making reuse, specialization, aggregation, equivalence, contextual activation, and external alignment explicit.

The goal is to control the evolution of the competency set. A new competency is created when an existing competency cannot adequately represent the intended meaning. Otherwise, an existing competency may be reused, generalized, specialized, aggregated, or associated with a new instructional context, according to the semantic distinctions identified during the CSP applications.

Semantic structuring improves consistency by making relationships among competencies explicit. It supports the distinction between atomic and composite competencies, controlled generalization and specialization, reuse across instructional entities, and alignment with external frameworks such as CC2020, CS2023, and BNCC Computing. Within this thesis, the resulting decisions provide requirement evidence for OntoKSD and may be represented through OntoKSD constructs when applicable.

### Semantic Structuring Guidelines

1. **Check for reusable competencies**

   Review the existing competency set before creating a new competency. Prefer reuse when the same competency can be mobilized in a new context without changing its conceptual meaning.

2. **Identify overlaps and redundancies**

   Detect conceptual overlaps, near-duplicates, and terminological inconsistencies. Merge, rename, or relate equivalent competencies as appropriate.

3. **Generalize when a competency is too narrowly defined**

   When a competency is overly tied to a specific task or artifact, abstract its core meaning to support reuse while preserving the intended conceptual basis.

4. **Specialize when greater precision is required**

   When a competency is too broad to represent a relevant distinction, define a controlled specialization that preserves its conceptual basis while expressing the more specific scope or constraints.

5. **Aggregate complementary competencies**

   Organize complementary competencies into composite competencies when the broader meaning depends on their coordinated mobilization.

6. **Separate activation from competency identity**

   Do not create a new competency solely because the instructional context changes. Represent contextual use through activation distinctions, such as target, required, or assessed activation, without changing the conceptual identity of the competency.

7. **Document external alignment explicitly**

   Link competencies to external frameworks, such as CC2020, CS2023, or BNCC Computing, without replacing their internal definitions.

8. **Record the modeling rationale**

   Document the reasoning supporting reuse, generalization, specialization, aggregation, equivalence, alignment, or creation decisions.

9. **Represent relations in OntoKSD when applicable**

   Preserve the validated semantic relations in human-readable documentation and, when applicable, represent them as RDF/OWL assertions using OntoKSD.

### Inputs

- Validated competency specifications produced in Phase 2;
- Instructional Entity Analysis Reports;
- reviewer feedback and implemented revisions;
- the existing competency repository represented or analyzed through OntoKSD;
- controlled vocabularies for knowledge, skills, Bloom levels, and dispositions; and
- external curricular frameworks, when applicable.

### Outputs

- **Semantically organized competency set**  
  Documenting reuse, generalization, specialization, aggregation, or creation decisions.

- **Explicit competency relations**  
  Such as generalization, specialization, aggregation, equivalence, dependency, and alignment.

- **Activation-aware mappings**  
  Distinguishing competency identity from its contextual use.

- **External alignment records**  
  Linking competencies to frameworks such as CC2020, CS2023, or BNCC Computing.

- **Rationale documentation**  
  Supporting traceability and future reuse.

- **RDF/OWL-ready representations**  
  Supporting ontology instantiation and querying when formal representation is applicable.

### Conclusion

Semantic structuring organizes validated competency specifications into a coherent and reusable set. Controlled reuse, generalization, specialization, aggregation, equivalence, and contextual activation improve the consistency and maintainability of the resulting structure.

A central OntoKSD distinction is that between competency identity and its activation in an instructional entity. This distinction allows the same competency to be reused across contexts and mobilized under different conditions without changing its conceptual identity.

The resulting structure supports human interpretation and, when represented in RDF/OWL, machine-processable analysis. Within this thesis, the documented semantic relations and their rationale provide requirement evidence for OntoKSD constructs, ontology instantiation, querying, validation, and curriculum analysis in competency-oriented Computing Education.
