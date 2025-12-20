## CSP-Adjustment  
### Adjustment Derived from Competency Reuse Tension (C04)

**Source of Evidence:**  
CSRP-Report – Task201 (Expert Review, Phase 2)

**Competency Involved:**  
C04 – Define Regular Expressions for Finite Automata



### Identified Issue

The expert review of Task201 identified a **scope tension** in the reuse of competency **C04**. While the task did not require learners to explicitly construct regular expressions as artifacts, expert feedback indicated that students were expected to engage in **symbolic and structural reasoning** about event patterns and Finite State Machine (FSM) complexity—particularly when deriving estimation rules for states and transitions.

This resulted in the activation of C04 at an **analytical and conceptual level**, rather than at a **notational or constructive level**, which is more directly suggested by the competency’s title.



### Adjustment Rationale

The review concluded that the observed tension does **not reflect a semantic deficiency** in C04, nor does it justify the creation of a new derived competency. Instead, it reveals the need to **clarify the conditions and modes under which C04 may be legitimately activated** during task-based reuse.

Creating a new competency to capture this analytical activation would introduce unnecessary fragmentation into the competency set and reduce reusability across instructional contexts.



### CSP Adjustment

The CSP is adjusted to explicitly account for **multiple activation modes** of reused competencies, particularly those involving symbolic or formal reasoning.

Specifically, the following procedural adjustment is adopted:

- When reusing competencies whose titles emphasize a concrete artifact (e.g., *Define Regular Expressions*), CSP authors should explicitly document whether the competency is being activated in:
  - a **constructive mode** (e.g., producing formal artifacts), or
  - an **analytical mode** (e.g., reasoning about structure, patterns, or formal properties without producing the artifact).

This clarification must be recorded in the **Competency Definition / Reusability Note** and, when applicable, discussed in the corresponding **CSRP-Report**.



### Expected Impact

This adjustment:
- Improves transparency and interpretability of competency reuse;
- Reduces ambiguity during expert review cycles;
- Preserves the semantic stability and generality of existing competencies;
- Prevents unnecessary proliferation of derived competencies.

The adjustment reinforces the CSP’s role as a **flexible yet controlled process**, capable of accommodating context-sensitive competency activation while maintaining a stable and reusable competency framework.



### Status

**Adjustment Type:** Procedural / Documentation Refinement  
**Structural Change to Competency Set:** None  
**Ontological Impact (OntoKSD):**  
Supports future modeling of *Competency Activation Mode* as contextual metadata, without altering competency hierarchy.


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




### Conclusion

> The tension observed in the reuse of C04 does not justify the creation of a derived competency. Instead, it reveals the need to **explicitly document activation modes during competency reuse**, reinforcing the CSP’s commitment to semantic stability, reusability, and controlled refinement.