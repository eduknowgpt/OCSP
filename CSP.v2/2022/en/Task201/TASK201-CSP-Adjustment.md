## CSP-Adjustment  
### Adjustment Derived from Competency Reuse Tension (C04)

**Source of Evidence:**  
CSRP-Report – Task201 (Expert Review, Phase 2)

**Competency Involved:**  
C04 – Define Regular Expressions for Finite Automata



## Identified Issue

The expert review conducted in Task201 identified a **scope tension** in the reuse of competency **C04**. Although the task did not require learners to explicitly construct regular expressions as formal artifacts, expert feedback indicated that students were nevertheless expected to engage in **symbolic and structural reasoning** about event patterns and Finite State Machine (FSM) complexity, particularly when deriving estimation rules for the number of states and transitions.

As a consequence, C04 was activated primarily at an **analytical and conceptual level**, rather than at a **notational or constructive level**, which is more directly suggested by the competency’s title and its typical artifact-oriented enactment. This observation revealed a discrepancy between the expected form of observable output and the cognitive processes effectively mobilized during task execution.

Importantly, this tension does not indicate a semantic inadequacy of the competency itself. Instead, it reflects the context-dependent nature of competency enactment during reuse. The analysis demonstrated that the same competency may legitimately be activated through different cognitive modes depending on instructional intent, task constraints, and expected learner actions.

This adjustment should therefore be interpreted not as the introduction of a new conceptual construct within the CSP, but as the **operational clarification and empirical validation** of activation-oriented refinements that emerged in earlier CSP iterations (TASK03–TASK05). Task201 provides evidence that such activation variability naturally arises when stable competencies are reused across distinct instructional contexts and must therefore be explicitly documented to preserve interpretability and semantic stability.




## Adjustment Rationale

The expert review concluded that the observed tension does **not reflect a semantic deficiency** in competency **C04**, nor does it justify the creation of a new derived competency. Instead, the tension reveals the need to **explicitly clarify the conditions and modes under which C04 may be legitimately activated** when reused across different instructional contexts.

The analysis demonstrated that the competency itself remained semantically stable; the variation emerged from differences in **how the competency was enacted**, rather than from changes in its conceptual scope. In Task201, C04 supported analytical and symbolic reasoning about event structures and FSM complexity without requiring the explicit construction of regular-expression artifacts. This confirms that competency activation may occur at different cognitive and operational levels depending on task design, instructional intent, and expected learner actions.

Creating a new competency to capture this analytical activation would therefore introduce unnecessary fragmentation into the competency set, weaken semantic continuity, and reduce reusability across instructional contexts. The appropriate refinement lies instead in **documenting activation characteristics at the level of competency reuse**, preserving the stability of competency definitions while allowing contextual variability in enactment.

This rationale consolidates activation-oriented refinements previously identified in earlier CSP iterations (TASK03–TASK05), providing empirical validation that competency reuse requires explicit documentation of activation context rather than structural modification of the competency framework.




## CSP Adjustment

The CSP is refined to explicitly account for **multiple activation modes** when competencies are reused across distinct instructional contexts, particularly in cases involving symbolic, analytical, or formal reasoning. This adjustment does not introduce a new conceptual element to the CSP; rather, it operationalizes and formalizes activation-oriented refinements that emerged in earlier CSP iterations and were empirically validated through the analysis of Task201.

Specifically, the following procedural adjustment is adopted:

- When reusing competencies whose titles emphasize the production of a concrete artifact (e.g., *Define Regular Expressions*), CSP authors must explicitly document **how the competency is activated within the instructional context**, including whether it is enacted in:
  - a **constructive mode**, in which learners produce formal artifacts or executable representations; or
  - an **analytical mode**, in which learners reason about structural, symbolic, or formal properties without necessarily producing the corresponding artifact.

This clarification must be recorded in the **Competency Definition / Reusability Note** and, when relevant, explicitly discussed in the corresponding **CSRP-Report**, ensuring that variations in enactment are interpreted as contextual differences rather than as changes in competency scope.

By relocating activation characteristics to the level of competency reuse, the CSP preserves the semantic stability of competencies while enabling context-sensitive instructional interpretation.



## Expected Impact

This adjustment is expected to:

- Improve transparency and interpretability of competency reuse across instructional entities;
- Reduce ambiguity during expert review cycles by making activation context explicit;
- Preserve the semantic stability and generality of existing competencies;
- Prevent unnecessary proliferation of derived competencies motivated solely by contextual variation in enactment;
- Strengthen alignment between competency definitions, instructional activities, and observable evidence.

Overall, the adjustment reinforces the CSP’s role as a **flexible yet controlled process**, capable of accommodating context-sensitive competency activation while maintaining a stable, reusable, and semantically coherent competency framework.



## Status

**Adjustment Type:** Procedural / Documentation Refinement  
**Structural Change to Competency Set:** None  

**Ontological Impact (OntoKSD):**  
Confirms the need to represent *Competency Activation Mode* as contextual metadata associated with the competence–instructional entity relation, without altering competency hierarchy or semantic scope.




### Competencies Associated with TASK201 – Surveillance Drone Prototype

| **ID**  | **Competency Title**                                      | **Role in TASK201**                                              | **Primary Function**           | **Bloom Level (Pred.)** | **Notes on Use / Activation Mode** |
|--------|------------------------------------------------------------|------------------------------------------------------------------|--------------------------------|-------------------------|------------------------------------|
| **C06** | Develop problem solutions using Finite State Machines     | Core competency for modeling drone surveillance behavior         | Model construction             | Apply / Analyze         | Central competency; FSMs sufficient for the task scope |
| **C02** | Justify the use of Deterministic Finite Automata (DFAs)   | Justification of the chosen automaton model                      | Model justification            | Analyze                 | Analytical use; no artifact construction |
| **C03** | Test Automata Using Simulators                             | Validation of FSM behavior using JFLAP                           | Artifact validation            | Apply                   | Simulation-based verification |
| **C04** | Define Regular Expressions for Finite Automata            | Symbolic and structural reasoning about event patterns           | Formal/symbolic reasoning      | Understand / Analyze    | Activated analytically (no explicit RE construction) |
| **C05** | Write a Technical Report                                   | Documentation of modeling, simulation, and decisions             | Technical communication        | Apply                   | Transversal; SBC format |
| **C11** | Identify Patterns in Finite State Machines                | Abstraction and generalization of FSM structures                 | Structural abstraction         | Analyze                 | Supports optimization and reasoning about state growth |



## Synthesis Framework — TASK201 → Evidence → CSP Refinement

| **Aspect Observed in TASK201** | **Empirical Evidence (CSP / CSRP)** | **Identified Issue or Insight** | **CSP Refinement Introduced** | **Methodological Impact** |
|-------------------------------|--------------------------------------|--------------------------------|-------------------------------|---------------------------|
| Reuse of symbolic competency (C04) | CSRP-Report identified non-constructive use of Regular Expressions | Competency was activated analytically, not through explicit artifact construction | Introduction of **competency activation modes** (constructive vs. analytical) | Improves transparency in competency reuse without fragmenting the catalog |
| Broad competency reuse across tasks | CSP-Report showed competencies reused in different task contexts | Same competency may support different cognitive roles depending on task design | Explicit documentation of **context-dependent activation** in CSP artifacts | Strengthens interpretability during expert review cycles |
| FSM sufficiency for task scope | CSP-Report justified FSMs as adequate abstraction | No need for more expressive automata models | Reinforcement of **model adequacy principle** | Prevents over-modeling and preserves instructional alignment |
| Symbolic reasoning without formal artifacts | CSRP-Report highlighted reasoning about patterns and growth of FSMs | Symbolic reasoning may occur without producing formal symbolic artifacts | Recognition of **analytical symbolic reasoning** as valid evidence of competency | Expands evidentiary basis for competency assessment |
| Expert feedback integration | CSRP-Report documented structured expert review | Feedback revealed process-level improvements, not just task corrections | Formalization of **CSRP-Report as a CSP lifecycle artifact** | Consolidates CSP as an iterative, evidence-driven process |
| Avoidance of competency proliferation | Review suggested tension, not deficiency, in C04 | Creating a new competency would be unjustified | Adoption of **procedural refinement instead of structural fragmentation** | Preserves semantic stability of the competency set |
| Alignment between task, competencies, and artifacts | CSP-Report showed tight coupling between FSM task and deliverables | Strong alignment validated CSP authoring guidelines | Reinforcement of **task–competency–artifact alignment rule** | Improves consistency and replicability of CSP applications |




## Conclusion

The tension observed in the reuse of competency **C04** does not justify the creation of a derived competency or modification of the existing competency definition. Instead, it reveals the necessity of **explicitly documenting activation modes during competency reuse**, ensuring that variations in enactment are interpreted as contextual differences rather than as semantic inconsistencies.

This adjustment reinforces a central principle of the CSP: competencies are treated as **stable and reusable semantic entities**, while their realization within instructional contexts may vary according to task requirements, expected learner actions, and forms of observable evidence. By making activation context explicit, the CSP preserves semantic stability while enabling flexibility in instructional design.

More broadly, the adjustment illustrates how expert review contributes to the **controlled evolution of the CSP**, allowing methodological refinement without fragmentation of the competency framework. In this sense, Task201 functions as a validation point in the CSP lifecycle, demonstrating that explicit modeling of contextual activation supports consistent competency reuse while maintaining coherence, interpretability, and long-term reusability of the competency set.
