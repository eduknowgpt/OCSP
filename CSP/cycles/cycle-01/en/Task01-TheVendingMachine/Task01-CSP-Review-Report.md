# CSP Phase 2 — Expert Review: Task01 — *The Vending Machine for Sodas and Snacks*

## 1. Introduction

This report documents CSP Phase 2 — Expert Review for the Problem-Based Learning (PBL) task *The Vending Machine for Sodas and Snacks*. It examines the preliminary Phase 1 competency specifications as educational artifacts, with emphasis on their Knowledge, Skill, and Disposition (K–S–D) components.

The review considers:

- Theoretical accuracy and conceptual soundness, ensuring alignment with established foundations in Computing Education, Automata Theory, and Formal Languages;
- Clarity, precision, and internal consistency, promoting unambiguous, well-scoped, and reusable competency definitions;
- Pedagogical alignment, verifying coherence between the specified competencies, the stated learning objectives, and the instructional context of the task;
- Contextual applicability, evaluating whether the competencies are feasible, meaningful, and educationally relevant within a realistic PBL scenario.

The review follows a structured artifact-evaluation guide and records technical and pedagogical judgments about the adequacy, relevance, and coherence of the specifications. It does not evaluate learner performance or collect learner assessment evidence. This report does not request personal, sensitive, or behavioral information about reviewers; the applicable research ethics procedures are documented separately.

The following sections review the instructional entity, knowledge components, learning objectives, competency definitions, and knowledge–skill alignment before synthesizing the recommendations and review decision.

## 2. Instructional Entity Summary

This section provides a concise synthesis of the findings from Phase 1A (Instructional Entity Analysis), serving as an anchoring reference for the expert review.
The purpose of this summary is to contextualize the competency evaluation by reaffirming the scope, intent, and instructional characteristics of the task, without introducing new interpretative elements.

### Contextual Overview

- Title: *The Vending Machine for Sodas and Snacks*

- Description:
  Learners are presented with the problem of designing a vending machine system capable of accepting payments (coins and banknotes), calculating correct change, and reliably dispensing products under clearly defined functional requirements. The task emphasizes formal modeling, systematic reasoning, and technical documentation within a problem-based learning context.

The table below summarizes the expert appraisal of the instructional entity as a curricular artifact, focusing exclusively on its clarity, coherence, and alignment with the intended instructional objectives.

| Aspect               | Rating Options                    | Evaluator Notes                                                                 |
|--------------------------|--------------------------------------|-------------------------------------------------------------------------------------|
| Task Title           | Clear                                 | The title accurately reflects the task’s focus and instructional scope.              |
| Problem Description  | Clear                                 | The problem statement is explicit, complete, and contextually grounded.              |
| Solution Development | Appropriate                           | The proposed solution steps are actionable and aligned with the defined competencies.|
| Expected Outcomes    | Well Specified                        | The expected outcomes are clearly articulated and directly related to the targeted competencies. |

### Decision Threshold

In accordance with the CSP protocol guidelines, the instructional entity is considered approved for competency review when all evaluated aspects are rated as Clear, Appropriate, or Well Specified.

## 3. Knowledge Component Review

Objective:
To evaluate whether the knowledge components are comprehensive, relevant, and appropriately scoped for the problem description and targeted competencies.

### Knowledge Granularity and Relevance

The expert review identified systematic limitations related to the level of knowledge granularity adopted in the current competency specifications. The representation relies primarily on a high-level external taxonomy (ACM CCS 2012), whose degree of abstraction proved insufficient to precisely annotate the concrete knowledge elements mobilized by the task.

In particular, the category *Regular Languages* was found to be excessively broad to support explicit references to core concepts implicitly required by the task, such as Deterministic Finite Automata (DFA), Non-Deterministic Finite Automata (NFA), and Regular Expressions (RE). This lack of specificity introduces conceptual ambiguity, especially in cases where the task presupposes DFA-oriented reasoning and construction, without requiring formal treatment of non-determinism or equivalence results.

As a result, the current knowledge taxonomy does not provide sufficient semantic resolution to support a clear and unambiguous mapping between task requirements and the corresponding competency elements. From an artifact-oriented perspective, this finding indicates the need for refinement of the knowledge representation, either through a more fine-grained taxonomy or through task-specific specialization of existing knowledge categories.

### Knowledge Appropriateness

The review further identified misalignment between some declared knowledge elements and the operational demands of the PBL task. Several knowledge components included in the competency specifications are not directly exercised by the task, nor are they required to produce the expected artifacts.

Specifically, the following knowledge elements were assessed as outside the effective scope of the task:

- Equivalence between Deterministic Finite Automata (DFA) and Non-Deterministic Finite Automata (NFA);
- Equivalence between Finite Automata (FA) and Regular Expressions (RE);
- Application of FA–RE equivalence to derive regular expressions from existing automata.

The task scenario emphasizes the construction, simulation, and validation of automata-based solutions for a vending machine system. It does not require formal reasoning about equivalence theorems or transformations between representational formalisms. Consequently, the inclusion of equivalence-related knowledge elements introduces unnecessary conceptual load and weakens alignment between the learning objectives, competency specifications, and the explicit requirements of the instructional task.

Additionally, one knowledge–skill pairing explicitly associated with *“Equivalence of DFA and NFA — Understand (Compare)”* was identified as unsupported by the task description. From a modeling standpoint, its presence reduces conceptual coherence and should therefore be excluded in future refinements of the artifact.

### Evaluation Summary

The table below synthesizes the expert assessment of the knowledge component, strictly in terms of its adequacy as part of a competency specification artifact.

| Criterion         | Assessment | Rationale                                                                                               |
|-----------------------|----------------|-------------------------------------------------------------------------------------------------------------|
| Comprehensiveness | No             | Core knowledge is present, but its representation lacks the necessary semantic granularity.                 |
| Relevance         | Partial        | Some knowledge elements directly support the task, while others are not operationalized in expected outputs.|
| Appropriateness   | No             | The knowledge scope is misaligned with task demands, being both overly abstract and, in places, unnecessary.|

### Decision Threshold

- Needs Revision

The knowledge component requires finer granularity, removal of non-essential elements, and stronger alignment with the explicit scope of the PBL task.

## 4. Learning Objectives Review

Objective:
To verify that the learning objectives are explicit, pedagogically coherent, and aligned with the instructional scope of the task.

The review distinguishes objectives stated in the instructional entity from objectives derived during the preliminary Phase 1 analysis. This distinction is necessary because some derived objectives introduce equivalence and transformation content that is not operationalized by the task.

The table below summarizes the expert appraisal of the learning objectives with respect to their adequacy and instructional alignment.

| Criterion    | Assessment | Evaluator Notes                                                                 |
|------------------|----------------|-------------------------------------------------------------------------------------|
| Completeness | Yes | The objectives cover the explicit task goals and the additional concepts identified during the preliminary analysis. |
| Relevance | Partial | The explicit objectives are relevant, but derived objectives concerning DFA–NFA equivalence, FA–RE equivalence, and formal transformation exceed the operational scope of the task. |

### Decision Threshold

- Needs Revision

The explicit objectives are retained. The derived objectives identified as outside the task scope should be removed or narrowed during revision, consistently with the knowledge-component recommendations in Section 3.

## 5. Competency Definitions Review

This section examines the clarity, internal consistency, and pedagogical adequacy of the competency titles and descriptions, as well as the alignment between knowledge–skill pairings and Bloom’s Revised Taxonomy.

### Competency Titles and Descriptions

The expert review identified the need for systematic refinement of competency titles and textual descriptions in order to improve clarity, reduce ambiguity, and promote consistency across the competency set.

Several competency descriptions were assessed as either overly directive or excessively generic, which may hinder interpretability and reuse in other instructional contexts. In particular, explanatory passages providing background information (e.g., general discussions on the *role of modeling and simulation* or *introductory explanations of regular expressions*) were identified as redundant within competency definitions. Such conceptual explanations are more appropriately placed in instructional or supporting materials, whereas competency statements should remain concise, action-oriented, and outcome-focused.

One competency related to regular expressions exhibited imprecise wording in its title, potentially obscuring the intended cognitive operation. The formulation *“Determine Regular Expressions that Represent Automata”* was found to be ambiguous with respect to whether the emphasis lies on construction, identification, or conceptual understanding. A reformulation highlighting the relationship between representational formalisms—for example, framing the competency in terms of *relating regular expressions to their equivalent automata*—was assessed as more explicit and pedagogically transparent.

The analysis also revealed functional redundancy among competency definitions, with two competencies (originally identified as D and E) expressing overlapping scope and intent. From a structural modeling perspective, these competencies should be consolidated into a single, unified definition to eliminate duplication and improve internal coherence.

Beyond individual cases, the review highlighted a broader issue of terminological inconsistency across competency descriptions and associated annotations. To support clarity, interoperability, and reuse—particularly within an ontology-driven framework such as OntoKSD—the adoption of a standardized terminology and an explicit term-mapping strategy is recommended.

### Knowledge–Skill Pairing and Bloom Alignment

The review confirmed that the adopted knowledge–skill pairing strategy is methodologically sound and that the systematic use of Bloom-aligned action verbs contributes positively to the explicitness of expected learner actions.

The selected verbs were assessed as appropriate to the task context and learning objectives, enabling clear differentiation between knowledge components and observable skills. This aspect of the competency specification constitutes a strength of the current artifact and should be preserved in subsequent refinements.

### Decision Threshold

- Needs Revision

Although the overall structure of the competency definitions is robust, textual refinement, terminological standardization, and the elimination of redundancies are required to ensure conceptual clarity, internal consistency, and effective reuse within competency-based and ontology-driven educational contexts.

## 6. Recommendations Synthesis

Based on the technical review, a set of coherent and convergent recommendations was identified to address issues of granularity, alignment, clarity, and structural consistency across the competency specifications. These recommendations are organized below according to their primary focus.

### 6.1 Knowledge Representation and Granularity

The current level of abstraction adopted for the knowledge components was found to be excessively coarse, limiting conceptual precision and hindering accurate annotation. To address this issue, the following actions are recommended:

* Refine the level of knowledge granularity, introducing more specific categories that directly reflect the concepts operationalized in the task;
* Remove Non-Deterministic Finite Automata (NFA) from the knowledge specification, as this concept is not required by the task description nor by the expected student outputs;
* Eliminate learning objectives and knowledge elements not explicitly exercised by the task, including:

  * Equivalence between Deterministic Finite Automata (DFA) and Non-Deterministic Finite Automata (NFA);
  * Equivalence between Finite Automata (FA) and Regular Expressions (RE);
  * Application of FA–RE equivalence to derive regular expressions from existing automata.

These adjustments aim to restore alignment between task requirements, learning objectives, and competency specifications, ensuring that each knowledge element has a clear instructional function.

### 6.2 Competency-Specific Revisions

Several competency definitions require targeted refinement to improve clarity, relevance, and internal consistency:

* Competency B

  * Review and reword the title to avoid references to decision-making between DFA and NFA, which exceeds the scope of the task;
  * Remove the knowledge–skill pair *“Equivalence of DFAs and NFAs – Understand (Compare)”*, as it is not supported by the task context;
  * Eliminate all references to NFA-related knowledge.

* Competency C

  * Remove explanatory content related to the *general purpose of modeling and simulation* (e.g., optimization, decision-making, safety, training), as this material is not directly tied to observable task outcomes.

* Competency D

  * Remove background explanations reviewing regular expressions and their theoretical equivalence to finite automata;
  * Reformulate the competency title to explicitly emphasize the relationship between representational formalisms, improving semantic clarity (e.g., *relating regular expressions to their equivalent automata*).

* Competency E

  * Merge this competency with Competency D, as both express overlapping scope and intent.

### 6.3 Textual Consistency and Terminology

In addition to content-level revisions, the review highlights the need for broader textual and terminological harmonization:

* Revise competency descriptions to avoid formulations that are either overly directive or excessively generic;
* Standardize terminology across competency titles, descriptions, and annotated resources;
* Adopt a controlled vocabulary or explicit term-mapping strategy, particularly to support reuse within the OntoKSD framework.

### Summary

Collectively, these recommendations aim to enhance the conceptual precision, pedagogical alignment, and reusability of the competency specifications. By refining knowledge granularity, removing non-essential elements, consolidating redundant competencies, and standardizing terminology, the revised model will better reflect the actual scope of the PBL task and support consistent application within competency-based and ontology-driven educational contexts.

## 7. Conclusion and Decision

Based on the expert review, a set of targeted and well-defined revisions will be implemented to enhance the clarity, relevance, and instructional adequacy of the competency specifications associated with the task.

A central outcome of the review is the identification of excessive abstraction in the current knowledge representation, which limits conceptual precision and weakens the effectiveness of competency annotation. To address this issue, the knowledge component will be restructured using a more fine-grained and task-aligned taxonomy, enabling clearer differentiation of concepts explicitly required by the PBL scenario. As part of this refinement, knowledge elements related to Non-Deterministic Finite Automata (NFA)—which are not exercised by the task—will be revised or removed.

Further improvements will focus on textual and structural refinement of competency definitions. Several competency statements exhibited formulations that were either overly generic or excessively directive. To improve coherence and usability, competency titles will be reformulated to emphasize observable outcomes, redundant competencies will be consolidated, and explanatory content not directly anchored in task requirements will be eliminated. In particular, competencies whose scope exceeded the problem context will be restructured to ensure tighter alignment with the intended learning outcomes.

In addition, learning objectives and associated knowledge elements will be revised to ensure a direct and explicit mapping to task demands, avoiding the inclusion of concepts that are not operationalized in the expected student solutions. This alignment is essential to preserve the internal consistency of the CSP model and to support reliable reuse of the competency specifications.

Looking forward, the adoption of a standardized terminology and a structured knowledge representation will strengthen consistency and interoperability across PBL tasks, particularly within the OntoKSD framework. The iterative character of the CSRP remains a key mechanism for continuously validating and refining competency specifications as instructional contexts evolve.

### Decision

* Approved with Revisions

Upon implementation of the revisions identified in this report, the competency specifications will constitute a theoretically sound, pedagogically aligned, and reusable artifact, suitable for application in competency-based and problem-based Computing Education. These refinements ensure that the competency model functions not only as an assessment reference but also as a reusable instructional and design instrument for future learning scenarios.

