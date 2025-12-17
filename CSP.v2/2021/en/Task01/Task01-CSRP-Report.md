# Expert Review: Task1 – The Vending Machine for Sodas and Snacks


## 1. Introduction

Building on the **Competency Specification Process (CSP) framework**, this report documents **Phase 2 — Competency Expert Review** for the PBL task *“The Vending Machine for Sodas and Snacks.”* This phase is dedicated to the **technical validation of the competency specifications** associated with the task, encompassing their **knowledge, skills, and dispositions (K–S–D)** components.

The primary objective of this review is to assess the competency specifications with respect to:

* **Theoretical accuracy and conceptual soundness**, ensuring alignment with established foundations in Computing Education and Automata Theory;
* **Clarity and internal consistency**, promoting precise, unambiguous, and reusable competency descriptions;
* **Pedagogical alignment**, verifying coherence with the intended learning objectives and instructional context;
* **Contextual applicability**, evaluating the feasibility and educational relevance of the competencies within a realistic problem-based learning scenario.

The review is grounded in **qualified expert judgment** and follows a **structured, artifact-centered evaluation guide**. Domain specialists were invited to conduct a **technical review of the competency specifications**, applying predefined evaluation criteria to examine the adequacy, relevance, and coherence of the K–S–D elements mapped to the task. No personal, behavioral, or sensitive data were collected; the focus of the analysis remains exclusively on the **educational artifact** under review.

This report synthesizes the results of the expert review and formulates **actionable recommendations** aimed at improving the clarity, alignment, and instructional value of the competency specifications.

The analysis is organized according to the stages of the **Competency Specification Protocol**, comprising:

* **Instructional-context analysis**, validating task complexity and the scope of the targeted competencies;

* **Item-level evaluation**, identifying strengths, inconsistencies, and elements requiring refinement;

* **Cross-criterion synthesis**, integrating findings related to accuracy, clarity, pedagogical alignment, and contextual relevance;

* **Recommendations**, proposing concrete adjustments to enhance the robustness and reusability of the competency model.

By situating this review within **Phase 2 of the CSP**, the report contributes to the iterative refinement of competency specifications, ensuring that they are **theoretically rigorous, pedagogically sound, and suitable for reuse** in competency-based and problem-based Computing Education contexts.






## 2. Instructional Entity Summary

Context: A concise recap of Phase 1A findings to anchor the review.

- Title: The Vending Machine for Sodas and Snacks

- Description: Learners face the problem of designing a vending machine system that accepts payments (coins/banknotes), calculates correct change, and dispenses products reliably under defined functional requirements.

| **Aspect**               | **Rating Options**              | **Evaluator Notes**                                                      |
| ------------------------ | ------------------------------- | ------------------------------------------------------------------------ |
| **Task Title**           | Clear | The title accurately reflect the task’s focus and scope            |
| **Problem Description**  | Clear | The problem statement is explicit, complete, and contextually relevant  |
| **Solution Development** |  Appropriate    | Solution steps are actionable and aligned with defined competencies     |
| **Expected Outcomes**    | Well Specified | Outcomes clearly relate to the tasks and competencies being assessed |


### Decision Threshold

According to protocol guidelines:

- Approved → All items rated Clear / Appropriate / Well Specified.




## 3. Knowledge Component Review

**Objective:** To evaluate whether the knowledge components associated with the task are **comprehensive, relevant, and appropriately scoped** with respect to the problem description and the targeted competencies.

### Knowledge Granularity and Relevance

The technical review identified **systematic issues related to the level of knowledge granularity** adopted in the competency specifications. The current representation relies on a **high-level taxonomy (ACM CCS 2012)** whose abstraction level proved insufficient to precisely annotate the knowledge elements required by the task.

In particular, the category *regular languages* was found to be **too broad** to support explicit references to key concepts implicitly required by the task, such as **Deterministic Finite Automata (DFA)**, **Non-Deterministic Finite Automata (NFA)**, and **Regular Expressions (RE)**. This mismatch hindered accurate annotation and introduced conceptual ambiguity, especially where the task implicitly assumes DFA-based reasoning but does not require formal treatment of NFA or equivalence results.

As a consequence, the review indicates that the current knowledge taxonomy **does not provide sufficient granularity** to support clear mapping between task requirements and competency elements. A refinement of the knowledge representation—either through a more fine-grained taxonomy or through task-specific specialization of existing categories—is therefore necessary.



### Knowledge Appropriateness

The review further revealed **misalignment between certain declared knowledge elements and the actual demands of the PBL task**. Several knowledge components included in the competency specifications are **not explicitly required** to solve the problem as described, nor are they operationalized in the expected student outputs.

In particular, the following knowledge elements were identified as **out of scope** for the task:

* Equivalence between **Deterministic Finite Automata (DFA)** and **Non-Deterministic Finite Automata (NFA)**;
* Equivalence between **Finite Automata (FA)** and **Regular Expressions (RE)**;
* Application of FA–RE equivalence to derive **regular expressions from existing automata**.

The task scenario focuses on the **construction and validation of automata-based solutions** for a vending machine system, without requiring formal reasoning about model equivalence or transformations across representational formalisms. Consequently, the inclusion of equivalence-related knowledge introduces unnecessary complexity and weakens alignment between **learning objectives**, **competency specifications**, and **task requirements**.

Additionally, one knowledge–skill pair explicitly associated with *“Equivalence of DFAs and NFAs – Understand (Compare)”* was found to be unsupported by the task description and should therefore be removed to preserve conceptual coherence.



### Evaluation Summary

| **Criterion**         | **Assessment** | **Rationale**                                                                                          |
| --------------------- | -------------- | ------------------------------------------------------------------------------------------------------ |
| **Comprehensiveness** | No             | Essential knowledge is present, but its representation is overly coarse.                               |
| **Relevance**         | Maybe          | Some knowledge elements support the task, while others are not operationalized.                        |
| **Appropriateness**   | No             | The level of detail is misaligned with task demands, being both too broad and, in places, unnecessary. |



### Decision Threshold

* **Needs Revision**

The knowledge component requires **refinement of granularity**, **removal of non-essential elements**, and **stronger alignment with the explicit scope of the PBL task**, in order to function effectively within the CSP and OntoKSD frameworks.






## 4. Learning Objectives Review

**Objective:** Ensure that the learning objectives are explicit, aligned, and pedagogically sound. 

| **Criterion**       | **Yes / Maybe / No** | **Evaluator Notes**                                                         |
| ------------------- | -------------------- | --------------------------------------------------------------------------- |
| **Completeness**    |  Yes                 | Do the LOs cover both explicit and implicit learning goals?           |
| **Relevance**       |  Yes                 | Are all LOs essential within the context of the task?               |

### **Decision Thresholds**

- Approved




## 5. Competency Definitions Review

This section examines the **clarity, consistency, and pedagogical adequacy** of the competency titles and descriptions, as well as the alignment between **knowledge–skill (K–S) pairings** and **Bloom’s Revised Taxonomy**.

### Competency Titles and Descriptions

The technical review identified the need for **systematic refinement of competency titles and textual descriptions** in order to improve clarity, reduce ambiguity, and ensure consistency across the competency set.

Several competency descriptions were found to be **either overly directive or excessively generic**, which may hinder interpretability and reuse in other instructional contexts. In particular, explanatory passages describing background concepts (e.g., general discussions on the *purpose of modeling and simulation* or *reviews of regular expressions*) were identified as **redundant** within competency definitions and should be removed. Such conceptual explanations are more appropriately located in instructional materials rather than in competency statements, which should remain **action-oriented and outcome-focused**.

One competency related to regular expressions exhibited **insufficiently precise wording** in its title. The formulation *“Determine Regular Expressions that Represent Automata”* was found to be ambiguous with respect to the intended cognitive operation. A reformulation emphasizing the **relationship between representational formalisms**—for example, *relating regular expressions to their equivalent automata*—was identified as more explicit and pedagogically transparent.

Additionally, the analysis revealed **redundancy among competency definitions**, with two competencies (originally labeled D and E) expressing equivalent intent and scope. These entries should therefore be **merged into a single, consolidated competency** to avoid duplication and improve structural coherence.

Beyond individual cases, the review highlighted a broader issue of **terminological inconsistency** across competency descriptions and annotated resources. To enhance clarity, interoperability, and reuse—particularly within the OntoKSD framework—a **standardized terminology and explicit term-mapping strategy** should be adopted.



### Knowledge–Skill Pairing and Bloom Alignment

The review confirmed that the **knowledge–skill pairing strategy** is generally sound and that the use of **multiple Bloom-aligned action verbs** contributes positively to the explicitness of expected learner actions.

The selected verbs were found to be **appropriately aligned with the task context and learning objectives**, supporting clear differentiation between knowledge components and observable skills. This aspect of the competency specification represents a **strength of the current model** and should be preserved in the revised version.



### Decision Threshold

* **Needs Revision**

While the overall structure of the competency definitions is robust, **textual refinement, terminological standardization, and removal of redundancies** are required to ensure conceptual clarity, internal consistency, and effective reuse within competency-based and ontology-driven educational settings.




## 6. Recommendations Synthesis

Based on the technical review, a set of **coherent and convergent recommendations** was identified to address issues of granularity, alignment, clarity, and structural consistency across the competency specifications. These recommendations are organized below according to their primary focus.


### 6.1 Knowledge Representation and Granularity

The current level of abstraction adopted for the knowledge components was found to be **excessively coarse**, limiting conceptual precision and hindering accurate annotation. To address this issue, the following actions are recommended:

* **Refine the level of knowledge granularity**, introducing more specific categories that directly reflect the concepts operationalized in the task;
* **Remove Non-Deterministic Finite Automata (NFA)** from the knowledge specification, as this concept is not required by the task description nor by the expected student outputs;
* **Eliminate learning objectives and knowledge elements not explicitly exercised by the task**, including:

  * Equivalence between **Deterministic Finite Automata (DFA)** and **Non-Deterministic Finite Automata (NFA)**;
  * Equivalence between **Finite Automata (FA)** and **Regular Expressions (RE)**;
  * Application of FA–RE equivalence to derive **regular expressions from existing automata**.

These adjustments aim to restore alignment between **task requirements**, **learning objectives**, and **competency specifications**, ensuring that each knowledge element has a clear instructional function.



### 6.2 Competency-Specific Revisions

Several competency definitions require targeted refinement to improve clarity, relevance, and internal consistency:

* **Competency B**

  * Review and reword the title to avoid references to decision-making between DFA and NFA, which exceeds the scope of the task;
  * Remove the knowledge–skill pair *“Equivalence of DFAs and NFAs – Understand (Compare)”*, as it is not supported by the task context;
  * Eliminate all references to **NFA-related knowledge**.

* **Competency C**

  * Remove explanatory content related to the *general purpose of modeling and simulation* (e.g., optimization, decision-making, safety, training), as this material is not directly tied to observable task outcomes.

* **Competency D**

  * Remove background explanations reviewing **regular expressions** and their theoretical equivalence to finite automata;
  * Reformulate the competency title to explicitly emphasize the **relationship between representational formalisms**, improving semantic clarity (e.g., *relating regular expressions to their equivalent automata*).

* **Competency E**

  * Merge this competency with **Competency D**, as both express overlapping scope and intent.



### 6.3 Textual Consistency and Terminology

In addition to content-level revisions, the review highlights the need for broader **textual and terminological harmonization**:

* Revise competency descriptions to avoid formulations that are either **overly directive** or **excessively generic**;
* Standardize terminology across competency titles, descriptions, and annotated resources;
* Adopt a **controlled vocabulary or explicit term-mapping strategy**, particularly to support reuse within the **OntoKSD** framework.



### Summary

Collectively, these recommendations aim to enhance the **conceptual precision**, **pedagogical alignment**, and **reusability** of the competency specifications. By refining knowledge granularity, removing non-essential elements, consolidating redundant competencies, and standardizing terminology, the revised model will better reflect the actual scope of the PBL task and support consistent application within competency-based and ontology-driven educational contexts.



## 7. Conclusion and Decision

Based on the technical review, a set of **targeted and well-defined revisions** will be implemented to enhance the **clarity, relevance, and instructional adequacy** of the competency specifications associated with the task.

A central outcome of the review is the identification of **excessive abstraction in the current knowledge representation**, which limits conceptual precision and weakens the effectiveness of competency annotation. To address this issue, the knowledge component will be **restructured using a more fine-grained and task-aligned taxonomy**, enabling clearer differentiation of concepts explicitly required by the PBL scenario. As part of this refinement, knowledge elements related to **Non-Deterministic Finite Automata (NFA)**—which are not exercised by the task—will be revised or removed.

Further improvements will focus on **textual and structural refinement of competency definitions**. Several competency statements exhibited formulations that were either overly generic or excessively directive. To improve coherence and usability, **competency titles will be reformulated to emphasize observable outcomes**, **redundant competencies will be consolidated**, and **explanatory content not directly anchored in task requirements will be eliminated**. In particular, competencies whose scope exceeded the problem context will be restructured to ensure tighter alignment with the intended learning outcomes.

In addition, **learning objectives and associated knowledge elements** will be revised to ensure a **direct and explicit mapping to task demands**, avoiding the inclusion of concepts that are not operationalized in the expected student solutions. This alignment is essential to preserve the internal consistency of the CSP model and to support reliable reuse of the competency specifications.

Looking forward, the adoption of a **standardized terminology and a structured knowledge representation** will strengthen consistency and interoperability across PBL tasks, particularly within the **OntoKSD** framework. The **iterative character of the CSRP** remains a key mechanism for continuously validating and refining competency specifications as instructional contexts evolve.

### Decision

* **Approved with Revisions**

Upon implementation of the revisions identified in this report, the competency specifications will constitute a **theoretically sound, pedagogically aligned, and reusable artifact**, suitable for application in competency-based and problem-based Computing Education. These refinements ensure that the competency model functions not only as an assessment reference but also as a **reusable instructional and design instrument** for future learning scenarios.



