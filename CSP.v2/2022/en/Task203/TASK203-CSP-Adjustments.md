# **CSP-Adjustment — Task203: Parking Control**

## 1. Rationale for Adjustment

The **CSP-Adjustment for Task203** was derived from the findings of the corresponding **CSRP-Report**, which identified a **potential functional ambiguity** in the reuse of the competency **C09 – Apply Turing Machine Variants**.

The expert review confirmed that the observed issue does **not result from a semantic inadequacy** of the competency itself, nor from a misalignment between task requirements and the overall competency set. Instead, the tension emerges from a **lack of explicit specification of the competency activation mode**, particularly in relation to the core modeling competency **C07 – Develop Problem-Solving Solutions Using Turing Machines**.

More specifically, the ambiguity arises at the boundary between a **core constructive competency** (C07), which is intrinsically required for task completion, and an **optional extension competency** (C09), whose activation may occur either analytically or constructively depending on the adopted solution strategy. The absence of explicit activation documentation may therefore lead to perceived functional overlap without indicating semantic redundancy.

Accordingly, the present adjustment introduces a **procedural clarification** within the CSP, reinforcing explicit activation documentation while preserving the semantic stability of the existing competency set. No new competencies are introduced, and no structural modification of competency definitions is required.



## 2. Adjustment Decision Regarding C09

### 2.1 No Structural Change to the Competency Set

Based on expert recommendations, the CSP **does not introduce a new specialized competency**, nor rename or fragment **C09**.  
The competency **C09 – Apply Turing Machine Variants** is therefore retained **unchanged at the semantic level**, preserving its stability and reuse potential across instructional contexts.

This decision is consistent with previous CSP refinement patterns, in which structural modifications were introduced only when supported by evidence of semantic insufficiency. In particular:

- **TASK201** addressed activation ambiguity through procedural clarification (C04), without altering competency structure;
- **TASK202** introduced specialization only when the semantic scope of a competency proved insufficient (C13 → C13.01).

In Task203, the identified issue concerns **activation clarity**, rather than semantic scope or competency adequacy. Consequently, procedural clarification is considered sufficient to resolve the observed tension while maintaining the integrity of the competency set.



### 2.2 Explicit Introduction of Activation Modes for C09

The CSP is adjusted to require **explicit documentation of the activation mode** whenever **C09** is reused. Activation mode is treated as a **contextual property of competency enactment**, not as a modification of the competency definition itself.

Two admissible activation modes are defined:

* **Analytical / Justificatory Activation**  
  C09 is activated when learners **analyze, compare, or justify** the use of a Turing Machine variant (e.g., multi-tape TM) in order to improve clarity, modularity, or conceptual organization, **without implementing the variant**. In this case, the competency supports reasoning about alternative representations rather than artifact construction.

* **Constructive / Implementational Activation**  
  C09 is activated when learners **explicitly implement a Turing Machine variant** as part of the solution, using the variant as the primary computational artifact.

In the specific context of **Task203**, the expected activation of **C09** is primarily **analytical**, unless the task specification explicitly requires the constructive implementation of a variant. This clarification prevents functional overlap with the core competency **C07**, while preserving flexibility for future reuse scenarios.




## 3. Relationship Between C07 and C09 After Adjustment

The CSP-Adjustment clarifies the **functional and contextual distinction** between competencies **C07** and **C09**, without altering their semantic definitions.

- **C07** remains the **core constructive competency** of Task203, responsible for the design and implementation of a Turing Machine that fully satisfies the problem requirements, including unbounded memory manipulation and coordinated control of multiple counters.

- **C09** is treated as an **optional extension competency**, whose activation—whether **analytical** or **constructive**—must be explicitly declared and justified in the CSP-Report, according to the adopted solution strategy.

This clarification prevents perceived functional overlap and establishes a **layered competency organization**, in which competencies are distinguished by their instructional role rather than by semantic specialization:

- *Core modeling* → **C07**  
- *Optional extension* → **C09**  
- *Theoretical justification* → **C08**

By making this distinction explicit, the CSP preserves semantic stability while ensuring transparency in competency enactment across complex modeling tasks.




## 4. Procedural Updates to CSP Artifacts

As a result of this adjustment, the CSP protocol is refined through the following procedural clarifications:

1. **CSP-Reports must explicitly declare the activation mode** of C09 whenever the competency is reused, specifying whether the activation is analytical/justificatory or constructive/implementational within the instructional context.

2. **CSRP-Reports must evaluate the consistency** between the declared activation mode and the actual task requirements, expected learner actions, and produced evidence, ensuring alignment between competency specification and instructional enactment.

3. **No new competency derivation or specialization is triggered** unless repeated empirical evidence, observed across multiple tasks, demonstrates a persistent semantic limitation in the scope of C09 rather than an activation-related ambiguity.

These updates reinforce the role of activation documentation as a mechanism for resolving reuse tensions while preserving the semantic stability of the competency set.



## 5. Impact on CSP Refinement

This adjustment contributes to the evolution of the CSP in three principal ways:

- It extends the requirement for **explicit activation mode documentation** to competencies associated with **high-expressiveness computational models**, where constructive and analytical uses may coexist.

- It reinforces the CSP principle of **procedural refinement over structural fragmentation**, ensuring that competency proliferation occurs only when justified by demonstrated semantic insufficiency.

- It strengthens governance of the competency set by clarifying the distinction between **core competencies** and **extension competencies** in complex modeling tasks, improving transparency and consistency in competency reuse across instructional contexts.





## 6. Summary of the Adjustment

The CSP-Adjustment for Task203 consolidates the functional roles and activation conditions of the competencies involved, clarifying their relationship within the instructional context while preserving the semantic stability of the competency set. The adjustment confirms the distinction between **core modeling**, **theoretical justification**, **optional extension**, **validation**, and **transversal communication** competencies, ensuring transparent competency enactment without introducing structural changes.

### Competencies Associated with TASK203 – Parking Control

| **ID**  | **Competency Title**                                   | **Role in TASK203**                                                     | **Primary Function**            | **Bloom Level (Pred.)** | **Notes on Use / Activation Mode** |
|--------|---------------------------------------------------------|-------------------------------------------------------------------------|----------------------------------|-------------------------|------------------------------------|
| **C07** | Develop problem-solving solutions using Turing Machines | Core competency for modeling parking control with multiple counters     | Model construction               | Apply / Analyze         | Core competency; Turing Machine required for unbounded memory and coordinated control |
| **C08** | Identify Turing Machine Variants                        | Justification and comparison of alternative TM representations          | Theoretical justification        | Analyze                 | Activated analytically; supports reasoning and model comparison without implementation |
| **C09** | Apply Turing Machine Variants                           | Optional extension to structure or modularize the solution               | Extension / optional construction| Apply / Analyze         | In Task203, primarily activated analytically; constructive activation optional and must be explicitly declared |
| **C10** | Test Turing Machines Using Simulators                   | Validation of TM behavior using JFLAP                                    | Artifact validation              | Apply                   | Simulation-based verification of operational correctness |
| **C05** | Write a Technical Report                                | Documentation of modeling, simulation, and theoretical justification     | Technical communication          | Apply                   | Transversal competency; SBC format |

This summary reflects the outcome of the expert review and the resulting procedural clarification, demonstrating how competency reuse can be preserved while contextual activation is made explicit within the CSP lifecycle.



## Synthesis Framework — TASK203 → Evidence → CSP Refinement

The following synthesis summarizes how observations emerging from Task203, as documented in the CSP-Report and validated through the CSRP-Report, contributed to the refinement and consolidation of CSP principles. The table emphasizes the relationship between empirical evidence, identified methodological insights, and their resulting impact on CSP governance and ontological consolidation.

| **Aspect Observed in TASK203** | **Empirical Evidence (CSP / CSRP)** | **Identified Issue or Insight** | **CSP Refinement Introduced** | **Methodological / Ontological Impact** |
|--------------------------------|-------------------------------------|--------------------------------|-------------------------------|------------------------------------------|
| Requirement for unbounded memory and multiple counters | CSP-Report demonstrates the need to track availability and rejected requests independently across categories | FSMs and PDAs are insufficient to represent task semantics | Reinforcement of the **model adequacy principle** (TM required) | Confirms CSP scalability to tasks requiring maximal computational expressiveness |
| Progression FSM → PDA → TM across tasks | TASK203 follows TASK201 and TASK202 in expressive escalation | Clear pedagogical and formal progression across tasks | Consolidation of the **expressiveness progression pattern** | Strengthens CSP as a curriculum-level competency design methodology |
| Core modeling competency (C07) | CSRP confirms TM construction as unavoidable for task completion | No tension in core competency definition or activation | Validation of **nuclear competency identification** | Reinforces separation between core and auxiliary competencies |
| Reuse of TM variant competencies (C08, C09) | CSP-Report includes both identification and application of TM variants | Boundary ambiguity between core modeling and extension competencies | Identification of **activation ambiguity** in extension competency | Extends CSP governance to complex modeling contexts |
| Optional use of TM variants | Task allows but does not require variant implementation | Competency may be activated analytically or constructively | Introduction of **explicit activation mode documentation for C09** | Prevents functional overlap while preserving semantic stability |
| Comparison with previous refinements | Similar activation-related patterns observed in C04 (TASK201) and scope-related tension in C13 (TASK202) | Tension concerns enactment rather than semantic scope | Adoption of **procedural refinement over structural change** | Preserves ontological stability and prevents premature specialization |
| Expert review influence | CSRP-Report identifies ambiguity in C09 activation | Review impacts process clarification rather than task or competency structure | Reinforcement of the **CSRP-Report as a decision-support artifact** | Confirms CSP as an evidence-driven lifecycle |
| Avoidance of premature specialization | No recurring evidence of semantic inadequacy in C09 | Structural change not empirically justified | Explicit rule: **specialization only when semantic limitation recurs across tasks** | Establishes governance criteria for controlled competency evolution |

This synthesis demonstrates that Task203 contributes primarily to the **procedural consolidation** of the CSP, confirming that competency reuse tensions at advanced levels of computational expressiveness can be resolved through explicit activation documentation rather than through structural modification of the competency set.





In summary, the CSP-Adjustment for Task203 establishes that:

- **C09 is retained without semantic modification**, preserving its scope and reuse potential across instructional contexts.
- Its reuse requires **explicit declaration of activation mode**, ensuring transparency between competency definition and contextual enactment.
- In the specific context of Task203, **C09 is primarily activated analytically**, rather than constructively, unless variant implementation is explicitly required by the task specification.
- Structural changes to the competency set are **not justified at this stage**, as the observed tension concerns activation clarity rather than semantic inadequacy.

This adjustment reinforces consistency, reuse stability, and methodological clarity within the CSP lifecycle, while preserving the framework’s capacity to evolve through accumulated empirical evidence and expert validation.

