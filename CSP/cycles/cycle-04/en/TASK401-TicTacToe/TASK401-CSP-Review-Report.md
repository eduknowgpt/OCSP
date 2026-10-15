# TASK401 - CSP Review Report

## 1. Review scope

**Artifact:** `TASK401-CSP-Report.md`, particularly CM10 - Explain a computational solution.

The review examines competency identity, constitutive Knowledge-Skill (KS) pairs, granularity and reuse within the TASK401 specification.


## 2. Findings

The initial CM10 specification combines several independently assessable explanatory performances in a single competency. This limits reuse when another instructional activity requires only one of those performances.

The issue is not the number of knowledge areas alone, but their aggregation without explicit component competencies. Refining the granularity makes the individual performances available for reuse while preserving their coordinated explanation through a composite CM10.


## 3. Decision and rationale

Define smaller explanatory competencies with stable KS compositions, and reformulate CM10 - Explain a computational solution as a composite of the relevant components.

| Code | Atomic competency | Constitutive KS pairs |
|---|---|---|
| CM12 | Explain arithmetic expression evaluation | K04 - Arithmetic and literal expressions × Understand |
| CM13 | Explain data organization | K10 - Arrays and matrices × Understand |
| CM14 | Explain conditional execution | K07 - Relational and logical operators × Understand; K08 - Decision structures × Understand |
| CM15 | Explain repeated execution | K09 - Repetition structures × Understand |
| CM16 | Explain function organization | K11 - Modularization: functions and parameter passing × Understand |
| CM17 | Explain variable updates | K03 - Data types, constants and variables × Understand; K05 - Assignment statements × Understand |

CM13-CM17 make the constituent explanatory performances explicit. CM12 is an additional explanatory extension for arithmetic expressions, not a component required by the initial broad definition. Its KS pairing targets the arithmetic aspect of K04; it does not assert performance concerning literal expressions.

The definitions of CM01-CM09 remain unchanged. Their task activation is reviewed separately where the adjusted requirements affect it.


### Explanatory composition

**CM10 - Explain a computational solution** aggregates **CM13, CM14, CM15, CM16 and CM17**. Its composition is fixed. CM12 remains a separate conditional extension, activated when an arithmetic expression is present and its explanation is requested.

The composite coordinates explanation of data organization, state updates, conditions, repetition and functions. Its constitutive KS set is the union of the component pairs: K03, K05, K07, K08, K09, K10 and K11, each paired with Understand.

Evidence must show that the learner explains both the component aspects and their relationships within the solution. Naming the components separately is insufficient. Coordinating an explanation does not automatically raise its cognitive level from Understand to Analyze.

The task is associated directly with CM10 for this integrated explanatory performance. CM13-CM17 remain catalog components and are not counted as additional direct task associations solely because they belong to CM10. The same evidence may support component-level interpretation, but composite and component results must not be counted as independent achievements.


### Instructional implications

Because CM16 is a component, the adjusted TASK401 must explicitly require organization into functions and individual explanation of that organization. This requirement makes CM07 mandatory in the adjusted specification, without automatically establishing its Create pairing.

This is an explicit adjustment for future application, not a retrospective assertion about the original task. If function organization is not required, CM10 cannot be treated as a fully required or evidenced composite under this fixed composition.


### Specification continuity

CM10 retains its identifier, title and integrative role, but changes from a broad specification to an explicitly composite specification. This structural revision must be preserved in the specification history; it is not merely an editorial change.

K01 - Algorithms and K15 - Code comments remain in the TASK401 knowledge catalog but are not constitutive pairs of the adjusted CM10. Consequently, exact equivalence with every pair of the initial specification is not asserted. Earlier evidence is not automatically transferred to the revised composite or its atomic components.



