# **CSP-Adjustment — Task203: Parking Control**

## 1. Rationale for Adjustment

The **CSP-Adjustment for Task203** was derived from the findings of the **CSRP-Report**, which identified a **potential functional ambiguity** in the reuse of the competency **C09 – Apply Turing Machine Variants**.

The review confirmed that the issue does **not stem from a semantic inadequacy** of the competency itself, nor from a mismatch between task requirements and the overall competency set. Instead, the tension arises from a **lack of explicitness regarding the mode of competency activation**, particularly in relation to the core modeling competency **C07 – Develop Problem-Solving Solutions Using Turing Machines**.

Accordingly, the adjustment focuses on **procedural clarification**, rather than the creation of new competencies or structural modification of the existing set.



## 2. Adjustment Decision Regarding C09

### 2.1 No Structural Change to the Competency Set

Based on expert recommendations, the CSP **does not introduce a new specialized competency** nor rename or fragment **C09**.  
The competency **C09 – Apply Turing Machine Variants** is retained **unchanged at the semantic level**, preserving stability and reuse potential across tasks.

This decision aligns with previous CSP refinements, where:
- **TASK201** addressed activation ambiguity procedurally (C04);
- **TASK202** introduced specialization only when semantic scope was insufficient (C13 → C13.01).

In Task203, the issue concerns **activation clarity**, not semantic scope.



### 2.2 Explicit Introduction of Activation Modes for C09

The CSP is adjusted to require **explicit documentation of the activation mode** whenever **C09** is reused. Two admissible activation modes are defined:

* **Analytical / Justificatory Activation**  
  C09 is activated when learners **analyze, compare, or justify** the use of a Turing Machine variant (e.g., multi-tape TM) to improve clarity, modularity, or conceptual organization, **without implementing the variant**.

* **Constructive / Implementational Activation**  
  C09 is activated when learners **explicitly implement a Turing Machine variant** as part of the solution, using it as the primary computational artifact.

For Task203, the default and expected activation mode of **C09** is **analytical**, unless the task specification explicitly requires implementation of a variant.



## 3. Relationship Between C07 and C09 After Adjustment

The CSP-Adjustment clarifies the **functional distinction** between the two competencies:

- **C07** remains the **core constructive competency**, responsible for the design and implementation of a Turing Machine capable of solving the problem.

- **C09** is treated as an **optional extension competency**, whose activation—analytical or constructive—must be explicitly stated and justified in the CSP-Report.

This distinction prevents functional overlap and reinforces a **layered competency structure**:
- *Core modeling* → C07  
- *Optional extension* → C09  
- *Theoretical justification* → C08  



## 4. Procedural Updates to CSP Artifacts

As a result of this adjustment, the CSP protocol is refined as follows:

1. **CSP-Reports must explicitly declare the activation mode** of C09 whenever it is reused.

2. **CSRP-Reports must evaluate consistency** between the declared activation mode and the actual task requirements and deliverables.

3. **No new competency derivation is triggered** unless repeated empirical evidence indicates a semantic limitation of C09 across multiple tasks.



## 5. Impact on CSP Refinement

This adjustment contributes to the CSP in three key ways:

- It extends the notion of **activation mode documentation** to competencies associated with **high-expressiveness computational models**.
- It reinforces the CSP principle of **procedural refinement over structural fragmentation**.
- It strengthens governance of the competency set by clarifying **core vs. extension competencies** in complex modeling tasks.





## 6. Summary of the Adjustment


### Competencies Associated with TASK203 – Parking Control

| **ID**  | **Competency Title**                                   | **Role in TASK203**                                                     | **Primary Function**            | **Bloom Level (Pred.)** | **Notes on Use / Activation Mode** |
|--------|---------------------------------------------------------|-------------------------------------------------------------------------|----------------------------------|-------------------------|------------------------------------|
| **C07** | Develop problem-solving solutions using Turing Machines | Core competency for modeling parking control with multiple counters     | Model construction               | Apply / Analyze         | Nuclear competency; TM required for unbounded memory and control |
| **C08** | Identify Turing Machine Variants                        | Justification and comparison of alternative TM representations          | Theoretical justification        | Analyze                 | Analytical use only; no implementation required |
| **C09** | Apply Turing Machine Variants                           | Optional extension to structure or modularize the solution               | Extension / optional construction| Apply / Analyze         | **Activated analytically by default**; constructive use optional and must be declared |
| **C10** | Test Turing Machines Using Simulators                   | Validation of TM behavior using JFLAP                                    | Artifact validation              | Apply                   | Simulation-based verification |
| **C05** | Write a Technical Report                                | Documentation of modeling, simulation, and theoretical justification     | Technical communication          | Apply                   | Transversal; SBC format |



## Synthesis Framework — TASK203 → Evidence → CSP Refinement

| **Aspect Observed in TASK203** | **Empirical Evidence (CSP / CSRP)** | **Identified Issue or Insight** | **CSP Refinement Introduced** | **Methodological / Ontological Impact** |
|--------------------------------|-------------------------------------|--------------------------------|-------------------------------|------------------------------------------|
| Requirement for unbounded memory and multiple counters | CSP-Report shows need to track availability and rejected requests per category | FSMs and PDAs are insufficient | Reinforcement of **model adequacy principle** (TM required) | Confirms CSP scalability to highest computational expressiveness |
| Progression FSM → PDA → TM across tasks | TASK203 follows TASK201 and TASK202 in expressive escalation | Clear pedagogical and formal progression | Consolidation of **expressiveness progression pattern** | Strengthens CSP as curriculum-level design methodology |
| Core modeling competency (C07) | CSRP confirms TM construction is unavoidable | No tension in core competency | Validation of **nuclear competency identification** | Reinforces separation between core and auxiliary competencies |
| Reuse of TM variant competencies (C08, C09) | CSP-Report lists both identification and application of variants | Potential overlap between C07 and C09 | Detection of **activation ambiguity** in extension competency | Extends CSP governance to high-power models |
| Optional use of TM variants | Task allows but does not require multi-tape implementation | Competency may be activated analytically or constructively | Introduction of **explicit activation modes for C09** | Prevents semantic overlap without fragmenting competency set |
| Comparison with previous refinements | Similar pattern to C04 (TASK201) and pre-C13.01 (TASK202) | Tension concerns usage, not scope | Adoption of **procedural refinement over structural change** | Preserves ontological stability of competencies |
| Expert review influence | CSRP-Report highlights ambiguity in C09 | Review impacts process, not task design | Reinforcement of **CSRP-Report as decision artifact** | Confirms CSP as evidence-driven lifecycle |
| Avoidance of premature specialization | No repeated evidence of semantic inadequacy in C09 | New competency not justified | Explicit rule: **no specialization unless scope limitation recurs** | Establishes criterion for future CSP evolution |




In summary, the CSP-Adjustment for Task203 establishes that:

- **C09 is retained without semantic modification**.
- Its reuse requires **explicit declaration of activation mode**.
- In Task203, C09 is **primarily activated analytically**, not constructively.
- Structural changes to the competency set are **not justified at this stage**.

This adjustment ensures consistency, reuse stability, and methodological clarity, while preserving the CSP’s capacity to evolve based on accumulated empirical evidence.
