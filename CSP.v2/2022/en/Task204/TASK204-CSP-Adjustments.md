# **CSP-Adjustments — TASK204: Online Judges at Logistic Solutions**

## 1. Purpose of the Adjustments

This document records the **formal adjustments applied to the CSP specification of TASK204** as a direct consequence of the **Expert Review (CSRP – Phase 2)**.

The adjustments aim to:

* incorporate **expert recommendations** regarding competency adequacy, scope, and observability;
* resolve cases of **semantic redundancy and over-specification** identified during expert analysis;
* formalize **activation semantics** (ActivationConstraint, ActivationMode, and ActivationRole);
* improve **traceability** between task requirements, competencies, and observable evidence.

The adjustments introduce **no new competencies** and do not alter existing competency definitions.  
Instead, they document **structural and procedural decisions** derived from expert evaluation, ensuring alignment between the CSP-Report, CSRP findings, and the methodological principles governing competency reuse.



## 2. Summary of CSRP Findings Informing the Adjustments

The CSRP-Report for TASK204 identified a set of findings with direct implications for the competency specification:

1. Among the two newly introduced competencies, only one is **strictly required** to satisfy the central learning objective of the task.
2. The second competency, while theoretically relevant, presents **semantic and evidentiary overlap**, lacking independent observability within the current task scope.
3. Reused competencies related to modeling, simulation, and documentation were **appropriately selected**, but required explicit clarification of their instructional roles.
4. Certain artifacts—particularly the FSM model and the technical report—were implicitly interpreted as learning goals rather than as **evidence-producing mechanisms** supporting conceptual competencies.

These observations motivated adjustments focused on **activation clarification and role differentiation**, rather than competency restructuring. The resulting refinements reinforce CSP principles established in previous cycles (TASK201–TASK203), namely:

* preservation of competency stability;
* avoidance of premature specialization or competency proliferation;
* and explicit representation of contextual activation as distinct from competency definition.




## 3. Adjustments to New Competencies

### 3.1 **C15 — Understand the Halting Problem and its Implications**

#### Adjustment Decision

* Retained as a **new competency**.
* Confirmed as the **single core theoretical competency** introduced for TASK204.

#### Rationale (from CSRP)

Expert reviewers agreed that explaining the **impossibility of detecting infinite loops** constitutes a **central and unavoidable cognitive requirement** of the task. The Halting Problem provides the theoretical foundation necessary to explain the operational limitations of Online Judge systems, making this competency both conceptually necessary and directly observable through task deliverables.

#### Final Activation (Adjusted)

* **ActivationConstraint**: `mandatory`
* **ActivationMode**: `analytical`, `justificatory`
* **ActivationRole**: `core`



### Competency Specification

#### Competency Title


    Understand the Halting Problem and its Implications


#### Refined Textual Description

This competency refers to the ability to **conceptually understand and clearly explain** the theoretical foundations and practical implications of the **Halting Problem**, one of the central results in Computation Theory.

Students must be able to explain why it is **undecidable to determine, in general, whether an arbitrary program halts on a given input**, and how this theoretical limitation constrains the design and behavior of **automated evaluation systems**, such as **Online Judges**.

Learners are expected to understand how the Halting Problem emerges from the expressive power of **Turing Machines**, and how it relates to **recursively enumerable languages** and **undecidability**, using these concepts to justify the impossibility of general-purpose loop detection.

This competency emphasizes **conceptual reasoning and theoretical justification**, rather than formal proofs or machine constructions. It includes the ability to discuss the **boundaries of algorithmic solvability**, critically reflect on the limitations of computational models, and relate abstract theoretical results to **observable behaviors in real-world computational systems**.

Within TASK204, students demonstrate this competency by providing a **theoretically grounded explanation** of why infinite loops cannot be algorithmically detected by Online Judges, articulating how this limitation reflects fundamental principles of Computation Theory.



#### Knowledge Specification

The following knowledge areas are critical for this competency:

* **The Halting Problem**
  * Establishes undecidability as a fundamental limit of computation.
  * Explains the inherent limits of algorithmic analysis of program behavior.

* **Computability (Conceptual Level)**
  * Provides the framework for distinguishing between decidable, semi-decidable, and undecidable problems.
  * Supports reasoning about what can and cannot be automated.

* **Turing Machines (Conceptual Reference Model)**
  * Serve as the formal basis for general computation.
  * Clarify why certain problems may be recognizable but not decidable.

* **Analytical and Critical Thinking (FPK)**
  * Supports evaluation of theoretical implications.
  * Enables logically coherent explanations linking theory and practice.



#### Disposition Specification

**Collaboration**

* Developed within a **Problem-Based Learning (PBL)** context requiring collaborative interpretation and refinement of theoretical explanations.
* Learners exchange perspectives and jointly construct coherent arguments.

**Responsibility**

* Students are responsible for maintaining conceptual accuracy and clarity in theoretical explanations.
* Includes adherence to academic rigor and appropriate communication of computational limitations.

**Proactivity**

* Learners actively seek clarification of abstract concepts related to undecidability and computability.
* They refine explanations through iterative reasoning and discussion.

**Creativity**

* Supports the translation of abstract theoretical limitations into clear explanations, diagrams, or analogies.
* Enhances communicative effectiveness when addressing non-specialist audiences.



#### Knowledge–Skill Pairing

##### Mapping of Knowledge to Skills

* **Understand** the **Halting Problem** to explain and justify the impossibility of general loop detection.
* **Understand** the conceptual role of **Turing Machines** as the foundation of undecidability arguments.
* **Understand** **Computability** to distinguish solvable, semi-decidable, and undecidable problems.
* **Apply** **Analytical and Critical Thinking** to structure coherent explanations connecting theory to observed system behavior.

> The use of *Apply* is restricted to reasoning and argumentation, not to formal modeling or construction.



#### Bloom’s Taxonomy Alignment

* **Halting Problem — Understand**
  * Describe and justify undecidability.
  * Relate theoretical limits to practical systems.

* **Computability — Understand**
  * Conceptually classify problems as decidable or undecidable.

* **Turing Machines — Understand**
  * Explain their role as a reference model for general computation.

* **Analytical and Critical Thinking — Apply**
  * Structure arguments.
  * Evaluate implications.
  * Justify conclusions.



#### Verb Annotation (Adjusted)

* **Understand** → Halting Problem → *Describe, Explain, Justify*
* **Understand** → Computability → *Classify, Recognize, Explain*
* **Understand** → Turing Machines → *Explain, Relate*
* **Apply** → Analytical and Critical Thinking → *Evaluate, Structure, Argue*



#### Summary Table for Competency C15

| **Competency**                                      | **Dispositions**                                       | **Knowledge**                    | **Skill**                                     |
| --------------------------------------------------- | ------------------------------------------------------ | -------------------------------- | --------------------------------------------- |
| Understand the Halting Problem and its Implications | Collaboration, Responsibility, Proactivity, Creativity | Halting Problem                  | **Understand (Describe, Explain, Justify)**   |
|                                                     |                                                        | Computability                    | **Understand (Classify, Recognize, Explain)** |
|                                                     |                                                        | Turing Machines                  | **Understand (Explain, Relate)**              |
|                                                     |                                                        | Analytical and Critical Thinking | **Apply (Evaluate, Structure, Argue)**        |







## 3.2 *C16 — Apply Turing Machine Concepts to Analyze Computational System Capabilities*

### Adjustment Decision

- **Downgraded from core status** following expert review.
- Reclassified as a **supporting or extension competency**, depending on instructional emphasis and assessment scope.

### Rationale (from CSRP)

The expert review concluded that:

- TASK204 does **not require the explicit construction, simulation, or formal application of Turing Machines**;
- evidence associated with this competency is **not independently observable**, as it largely emerges through explanations already required by the Halting Problem competency (C15);
- the competency’s conceptual content is relevant, but its activation occurs primarily as a **theoretical interpretation framework**, rather than as a distinct learning outcome.

Accordingly, the identified issue concerns **activation scope**, not semantic inadequacy.

### Final Activation (Adjusted)

- **ActivationConstraint**: `optional` or `conditional`
- **ActivationMode**: `interpretative`
- **ActivationRole**: `supporting` or `extension`

> **Note**  
> Expert reviewers also indicated that, in future CSP iterations, the conceptual content of this competency may be incorporated as **supporting knowledge within C15**, should no independent evidence of activation emerge across subsequent tasks.


## Competency Specification

### Competency Title

    Interpret Turing Machine Concepts to Analyze Computational System Capabilities



> **Note**  
> The verb *Interpret* is intentionally adopted to reflect the expert recommendation that this competency should emphasize **conceptual understanding and explanatory reasoning**, rather than formal modeling or simulation.



### Refined Textual Description

This competency refers to the ability to **interpret and conceptually mobilize core ideas derived from the Turing Machine model** in order to analyze the **capabilities and inherent limitations of computational systems**.

Students are expected to use Turing Machines as a **conceptual reference model** for reasoning about what classes of problems can or cannot be decided algorithmically, and to explain how notions such as **Turing-completeness** relate to the expressive power and limitations of programming languages and automated evaluation systems.

Rather than constructing or simulating Turing Machines, learners engage in **conceptual analysis and explanation**, employing TM-related concepts to support arguments concerning **computability boundaries**, **semi-decidability**, and the impossibility of fully automating certain forms of program analysis.

Within TASK204, this competency functions as an **interpretative complement** to the Halting Problem discussion (C15), providing theoretical context that supports explanation of why **Online Judges and similar systems are fundamentally limited**, without constituting an independent modeling activity.



### Knowledge Specification

The following knowledge areas support this competency:

- **Turing Machines (Conceptual Reference Model)**  
  - Provide the theoretical foundation for general-purpose computation.  
  - Enable reasoning about expressive limits of computational systems.

- **Computability Theory (Conceptual Level)**  
  - Supports differentiation between decidable, semi-decidable, and undecidable problems.  
  - Enables interpretation of algorithmic limitations without formal proofs.

- **Universal Turing Machine (Conceptual Notion)**  
  - Illustrates programmable computation and system simulation at an abstract level.  
  - Supports explanations of why modern computational systems inherit theoretical limits.

- **Analytical and Critical Thinking (FPK)**  
  - Supports interpretation of theoretical models.  
  - Enables the construction of coherent explanatory arguments.



### Disposition Specification

**Collaboration**

- Learners engage in collaborative discussions to align interpretations of abstract computational models.
- Peer interaction supports clarification of conceptual misunderstandings.

**Responsibility**

- Students are responsible for maintaining conceptual correctness and clarity in theoretical explanations.
- This includes avoiding overgeneralizations or misinterpretations of formal results.

**Proactivity**

- Learners actively seek to understand the implications of theoretical models beyond surface definitions.
- They refine explanations when inconsistencies or ambiguities are identified.

**Creativity**

- Creativity supports the use of analogies, diagrams, and explanatory representations to communicate abstract computational limits.
- It enhances accessibility of explanations for non-specialist audiences.



### Knowledge–Skill Pairing

#### Mapping of Knowledge to Skills

- **Understand** the conceptual role of **Turing Machines** as a foundation for general computation.
- **Understand** **Computability Theory** in order to interpret decidability and semi-decidability.
- **Apply** **Analytical and Critical Thinking** to analyze and explain system-level limitations.

> **Important**  
> The use of *Apply* refers exclusively to **reasoning and argumentation**, not to formal modeling, construction, or simulation.



### Bloom’s Taxonomy Alignment

- **Turing Machines — Understand**
  - Explain their role as a universal computational model.
  - Relate TM expressiveness to system capabilities.

- **Computability — Understand**
  - Conceptually classify problem classes.
  - Interpret algorithmic limits.

- **Analytical and Critical Thinking — Apply**
  - Analyze implications.
  - Structure explanations.
  - Justify conclusions.


### Verb Annotation

- **Understand** → Turing Machines → *Explain, Relate, Interpret*
- **Understand** → Computability → *Classify, Distinguish, Explain*
- **Apply** → Analytical and Critical Thinking → *Analyze, Structure, Justify*



### Summary Table for Competency C16

| **Competency** | **Dispositions** | **Knowledge** | **Skill** |
|---|---|---|---|
| Interpret Turing Machine Concepts to Analyze Computational System Capabilities | Collaboration, Responsibility, Proactivity, Creativity | Turing Machines | **Understand (Explain, Relate, Interpret)** |
| | | Computability | **Understand (Classify, Distinguish, Explain)** |
| | | Analytical and Critical Thinking | **Apply (Analyze, Structure, Justify)** |




## 4. Adjustments to Reused Competencies

This section records the adjustments applied to competencies reused in TASK204 as a result of the expert review. The adjustments do not modify competency semantics; instead, they clarify **instructional role**, **activation conditions**, and **evidentiary function**, ensuring consistency between task objectives, expected artifacts, and observable learner actions.

The adjustments reinforce a central CSP principle: **modeling and documentation activities function primarily as vehicles for externalizing reasoning**, rather than as independent cognitive goals.



### 4.1 Supporting Competencies

#### **C06 – Develop Problem-Solving Solutions Using Finite State Machines**

**Adjustment Decision**

- Explicitly classified as a **supporting competency**, rather than part of the cognitive core.
- The FSM serves as a representational mechanism through which students externalize reasoning about Online Judge behavior and system outcomes.

**Final Activation**

- **ActivationConstraint**: `mandatory`
- **ActivationMode**: `constructive`
- **ActivationRole**: `supporting`



#### **C03 – Test Automata Using Simulators**

**Adjustment Decision**

- Explicitly marked as **conditional**, since simulation depth may vary depending on instructional emphasis.
- Simulation primarily supports validation and illustration of the FSM model, rather than introducing additional conceptual requirements.

**Final Activation**

- **ActivationConstraint**: `conditional`
- **ActivationMode**: `artifact-oriented`
- **ActivationRole**: `supporting`



### 4.2 Extension Competencies

#### **C02 – Justify the Use of Deterministic Finite Automata**

**Adjustment Decision**

- Retained as an **extension competency**, contributing theoretical enrichment without being required for successful task completion.
- Its activation strengthens discussions on modeling adequacy but does not generate independent assessment evidence.

**Final Activation**

- **ActivationConstraint**: `optional`
- **ActivationMode**: `justificatory`
- **ActivationRole**: `extension`



#### **C14 – Differentiate Classifications of Formal Grammars**

**Adjustment Decision**

- Maintained as an **extension competency**, supporting broader theoretical connections with the Chomsky hierarchy.
- Its activation enhances conceptual depth but is not necessary for fulfilling the core learning objectives of TASK204.

**Final Activation**

- **ActivationConstraint**: `optional`
- **ActivationMode**: `analytical`
- **ActivationRole**: `extension`



### 4.3 Transversal Competency

#### **C05 – Write a Technical Report**

**Adjustment Decision**

- Reclassified as a **transversal competency**, emphasizing its role as the primary **evidence artifact** rather than a cognitive objective.
- The report externalizes analysis, justification, and modeling decisions produced by other competencies.

**Final Activation**

- **ActivationConstraint**: `mandatory`
- **ActivationMode**: `artifact-oriented`
- **ActivationRole**: `transversal`



## 5. Consolidated Activation Configuration (Final)

The following table summarizes the **final activation configuration** for TASK204 after incorporation of the CSRP findings and CSP adjustments.  
The configuration reflects the explicit differentiation between **core conceptual competencies**, **supporting modeling competencies**, **extension competencies**, and **transversal evidence-producing competencies**, ensuring alignment between task objectives, expected learner actions, and observable artifacts.

| **Competency** | **ActivationConstraint** | **ActivationMode** | **ActivationRole** |
|---|---|---|---|
| **C15 – Understand the Halting Problem and its Implications** | mandatory | analytical, justificatory | core |
| **C16 – Interpret Turing Machine Concepts to Analyze System Capabilities** | optional / conditional | interpretative | supporting / extension |
| **C06 – Develop Problem-Solving Solutions Using FSMs** | mandatory | constructive | supporting |
| **C03 – Test Automata Using Simulators** | conditional | artifact-oriented | supporting |
| **C02 – Justify the Use of DFAs** | optional | justificatory | extension |
| **C14 – Differentiate Formal Grammar Classifications** | optional | analytical | extension |
| **C05 – Write a Technical Report** | mandatory | artifact-oriented | transversal |

This consolidated configuration makes explicit that TASK204 is conceptually centered on **analytical and justificatory reasoning about computational limits**, while modeling, simulation, and documentation activities function primarily as **supporting or evidentiary mechanisms** within the competency structure.


## 6. Impact of the Adjustments

As a result of these adjustments, TASK204 now exhibits:

- **Full alignment with the findings of the Expert Review (CSRP)**, ensuring consistency between intended learning outcomes and observable evidence;
- A clear separation between **cognitive objectives**, **supporting modeling mechanisms**, and **transversal evidence artifacts**, reducing ambiguity in competency interpretation and assessment;
- Reduced risk of **competency inflation**, achieved through the consolidation of overlapping theoretical content and clearer activation boundaries;
- Improved semantic precision in competency reuse, particularly through explicit specification of **ActivationConstraint**, **ActivationMode**, and **ActivationRole**;
- Stronger methodological consistency with the CSP–CSRP lifecycle and with the activation semantics formalized in OntoKSD.

Collectively, these adjustments reinforce the principle that competency stability is preserved by clarifying contextual activation rather than by introducing structural changes to the competency set.



## 7. Final Remark

These CSP-Adjustments formalize the transition from **expert judgment (CSRP)** to **authoritative competency specification (CSP)**.

TASK204 therefore stands as a **methodologically robust reference case**, demonstrating how expert review contributes to controlled, evidence-based refinement while preserving competency stability. The task illustrates how the CSP operationalizes competency reuse through explicit activation semantics, ensuring that theoretical rigor, instructional clarity, and ontological consistency are maintained within the OntoKSD-driven framework.





