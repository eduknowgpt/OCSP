# CSP Phase 2 — Expert Review: Task03 — The Farmer Robot

## 1. Introduction

This report documents CSP Phase 2 — Expert Review for the PBL task *The Farmer Robot*. It examines the preliminary Phase 1 competency specifications as educational artifacts, including their Knowledge, Skill, and Disposition (K–S–D) components.

The review considers:

- Theoretical accuracy and conceptual soundness, ensuring alignment with established foundations in Formal Languages, Automata Theory, and Computational Modeling;
- Clarity and internal consistency, promoting precise, unambiguous, and reusable competency definitions;
- Pedagogical alignment, verifying coherence between competencies, learning objectives, and expected student deliverables;
- Contextual applicability, evaluating the feasibility and instructional relevance of the competencies within the problem-based scenario.

The review follows a structured artifact-evaluation guide and records technical and pedagogical judgments about the adequacy, relevance, and coherence of the specifications. It does not evaluate learner performance or collect learner assessment evidence. This report does not request personal, sensitive, or behavioral information about reviewers; the applicable research ethics procedures are documented separately.

The following sections review the instructional entity, knowledge components, learning objectives, competency definitions, and knowledge–skill alignment before synthesizing the recommendations and review decision.

## 2. Instructional Entity Summary

This section summarizes the Phase 1A findings used to anchor the review.

- Title: The Farmer Robot

- Description: Learners are challenged to prototype a decision-making module that identifies the presence and counts specific herds—bovines, caprines, and swine—inside farm enclosures. This capability is essential for automating feed request logistics and optimizing farm management, all within operational needs and budget constraints.

| Aspect | Rating | Evaluator Notes |
| ------------------------ | ------------------------------- | ------------------------------------------------------------------------ |
| Task Title | Clear | The title accurately reflects the task’s focus and scope. |
| Problem Description | Clear | The herd-identification problem and company requirements are explicit. |
| Solution Development | Appropriate | The expected process supports finite-state modeling, simulation, and documentation. |
| Expected Outcomes | Well Specified | The JFLAP file, SBC report, examples, and company questions are clearly stated. |

### Decision Threshold

- Approved

## 3. Knowledge Component Review

### Knowledge Granularity and Relevance

The expert review identified the need to refine the granularity of the knowledge elements associated with the competency specifications. Several knowledge items were found to be overly abstract or excessively broad, which weakens their instructional utility and makes assessment less precise. The review therefore recommends shifting toward more specific, concrete, and task-relevant knowledge components that are directly exercised by learners during task execution.

In particular, the following adjustments were recommended:

- Refine knowledge focus from “Regular Languages” to “Regular Expressions.”
  In the competency *“Determine Regular Expressions that represent automata,”* the use of “Regular Languages” was deemed too abstract relative to the task requirements. Since learners are expected to construct and manipulate regular expressions as concrete artifacts, the knowledge element should be explicitly specified as “Regular Expressions,” ensuring closer alignment between declared knowledge, expected deliverables, and assessment criteria.

- Remove “Chomsky Hierarchy.”
  The Chomsky Hierarchy is not addressed in the task description, nor is it required by any of the expected learner outputs. Its inclusion introduces unnecessary theoretical breadth without contributing to observable or assessable performance. Removing this element sharpens the focus of the knowledge specification and reinforces alignment with the actual instructional scope of *The Farmer Robot* task.

Overall, these refinements improve the conceptual precision, instructional relevance, and assessability of the knowledge components, ensuring that all retained elements are explicitly exercised and pedagogically justified within the task context.

| Criterion | Assessment | Evaluator Notes |
| --------------------- | -------------------- | -------------------------------------------------------------------------- |
| Comprehensiveness | Yes | The specification contains the principal knowledge areas needed by the task. |
| Relevance | Partial | Most elements support the task, but the Chomsky Hierarchy does not. |
| Appropriateness | No | `Regular Languages` is too broad for the regular-expression artifact required by the task. |

### Decision Thresholds

- Needs Revision

## 4. Learning Objectives Review

Objective: Ensure that the learning objectives are explicit, aligned, and pedagogically sound.

| Criterion | Assessment | Evaluator Notes |
| ------------------- | -------------------- | --------------------------------------------------------------------------- |
| Completeness | Yes | The objectives cover the functions, FSM model, regular expressions, complexity question, JFLAP simulation, and report. |
| Relevance | Yes | Each objective corresponds to a requirement or expected product in the instructional entity. |

### Decision Thresholds

- Approved

## 5. Competency Definitions Review

### Competency Title & Description

| Subcomponent | Assessment | Evaluator Notes |
| -------------------------- | -------------------- | ---------------------------------------------------------- |
| Title Clarity | No | The titles using `Determine` and `Infer and Identify` do not express the intended actions precisely. |
| Description Precision | No | Several descriptions are either generic or overly prescriptive. |
| Contextual Application | No | Some definitions introduce theoretical content not exercised by Task03. |
| Scope Coverage | Maybe | The set covers the task but includes an out-of-scope grammar-classification competency. |

#### Reviewer Recommendations

Based on the expert review, the following recommendations were identified to improve the clarity, alignment, and instructional effectiveness of the competency specifications associated with *Task 03 – The Farmer Robot*:

- Revise competency descriptions to improve operational clarity
  Reformulate competency descriptions to eliminate language that is either overly generic or excessively prescriptive. Competencies should clearly articulate intended learning outcomes and observable behaviors without constraining learners to specific procedural steps.

- Rename the competency *“Determine Regular Expressions that Represent Automata”*
  The verb “Determine” was considered insufficiently expressive and weakly aligned with the intended cognitive level. It is recommended to replace it with a verb that better reflects productive and constructive outcomes, such as *Design*, *Construct*, or *Formulate*, in accordance with Bloom’s Revised Taxonomy.

- Remove the competency *“Differentiate the classifications of formal grammars”*
  This competency was found to be misaligned with the task’s instructional scope, as the classification of formal grammars is neither required by the problem description nor exercised through the expected learner deliverables. Its removal is recommended to maintain focus on task-relevant competencies.

- Clarify and reformulate the competency *“Infer and Identify Patterns in Finite State Machines”*
  The title and instructional intent of this competency were deemed ambiguous and potentially confusing. The review recommends the following reformulation to improve clarity and focus:

  > “Identify patterns in finite state machines”

  In addition, the associated knowledge component should be revised to reflect this updated focus, with its level of detail adjusted to ensure alignment with observable task activities.

### Decision Threshold

- Needs Revision

### Knowledge Evaluation

Objective: Ensure that each competency’s knowledge components are robust, accurate, and contextually relevant.

| Criterion | Assessment | Evaluator Notes |
| ------------------------ | -------------------- | ------------------------------------------------------------------------------- |
| Theoretical Validity | Maybe | The concepts are theoretically valid, but some mappings do not match the intended competency focus. |
| Comprehensiveness | No | The revised pattern-identification competency requires a more coherent knowledge set. |
| Relevance | No | The grammar-classification content is not required by Task03. |
| Granularity and Scope | No | `Regular Languages` is too broad and the Chomsky Hierarchy exceeds the task scope. |

#### Reviewer Recommendations

Based on the expert review, the following recommendations were formulated to improve the clarity and alignment of the competency specifications:

- Review and realign the associated knowledge components
  Ensure that the knowledge elements associated with the revised competency are directly aligned with its instructional intent and observable outcomes. The following knowledge areas were identified as appropriate and sufficient to support the competency:

  - Finite State Machines;
  - Regular Expressions;
  - Analytical and Critical Thinking (FPK).

- Reformulate the title and instructional focus of Competency C
  The original title and purpose of *Competency C* were considered ambiguous and potentially misleading. To improve clarity and instructional coherence, the following reformulation is recommended:

  > “Identify patterns in finite state machines”

  In conjunction with this change, the associated knowledge components should be revised to reflect the updated focus, and their level of granularity should be adjusted to ensure consistency with the expected learner actions and assessment criteria.

### Decision Threshold

- Needs Revision

### Knowledge–Skill Pairing & Bloom Alignment

Objective: Verify that each knowledge–skill pairing is logically justified and aligned with the correct cognitive level per Bloom’s Revised Taxonomy.

| Criterion | Assessment | Evaluator Notes |
| --------------------------- | -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Bloom-Level Suitability | No | Some recorded levels do not match the cognitive demand expressed by the competency. |
| Verb Effectiveness | Yes | Most verbs are action-oriented, although `Determine` requires replacement. |
| Pairing Justification | No | Several mappings do not explain clearly how the knowledge supports the expected performance. |

#### Reviewer Recommendations

Based on the expert review, the following recommendations were identified to improve the cognitive alignment and instructional precision of the competency specifications:

- Review and adjust Bloom’s Taxonomy levels
  Reassess the Bloom level associated with each knowledge component to ensure that it accurately reflects the expected depth of understanding and the type of cognitive processing required for the task. This alignment is essential to maintain coherence between learning objectives, competency descriptions, and assessment criteria.

- Rename the competency *“Determine Regular Expressions that Represent Automata”*
  The verb “Determine” was considered insufficiently expressive of the intended cognitive demand. It is recommended to replace it with a verb that more accurately reflects a constructive or productive learning outcome, such as *Design*, *Construct*, or *Formulate*, in accordance with Bloom’s Revised Taxonomy.

These adjustments will contribute to clearer competency definitions and more reliable assessment of learner performance.

### Decision Thresholds

- Needs Revision

## 6. Recommendations Synthesis

Based on the expert review and the criteria established by the Competency Specification Process (CSP), a set of action-oriented recommendations was formulated to enhance the competency framework associated with *Task 03 – The Farmer Robot*. These recommendations focus exclusively on the instructional artifact—namely, the task description and its competency specifications—and address issues of scope, clarity, cognitive alignment, and instructional relevance.

- Refine Knowledge Components

  - Decompose broad or aggregated topics into discrete, task-relevant knowledge elements that directly support observable learner actions (e.g., refining *Finite State Machine theory* into elements such as state–transition representations, pattern identification, or minimization concepts, where applicable).
  - Replace “Regular Languages” with “Regular Expressions” to ensure alignment with the concrete artifacts and formal representations expected as task deliverables.
  - Remove theoretical topics not exercised by the task, such as the Chomsky Hierarchy, thereby maintaining focus on knowledge that is both instructionally relevant and assessable.

- Clarify Competency Titles and Descriptions

  - Adopt precise, Bloom-aligned action verbs (e.g., *Design*, *Construct*, *Formulate*) in place of generic terms such as *Determine*, improving the expressiveness and cognitive accuracy of competency titles.
  - Ensure that each competency title and description explicitly reflects the Task 03 problem scenario and the intended learning outcomes, avoiding vague or overly prescriptive formulations.
  - Review the competency set as a whole to eliminate redundancy and preserve clear differentiation of instructional scope and intent.

- Align Knowledge–Skill Pairings with Bloom’s Taxonomy

  - Reassess the cognitive levels associated with each knowledge–skill pairing to ensure consistency with the nature and complexity of the task activities (e.g., *Apply*, *Analyze*, *Create*).
  - Where appropriate, include concise justifications explaining how specific knowledge elements support the demonstration of the associated competency.

Collectively, these recommendations aim to produce a more focused, coherent, and instructionally effective competency specification, tightly aligned with the actual cognitive and practical demands of *The Farmer Robot* task.

## 7. Conclusion and Decision

Implementing the recommended adjustments will significantly enhance the quality, clarity, and instructional robustness of the competency specification for *Task 03 – The Farmer Robot*. By refining knowledge granularity, removing non-relevant theoretical content, and improving the precision of competency descriptions, the revised framework becomes more closely aligned with the task’s intended learning outcomes and assessment practices.

Moreover, improved alignment with Bloom’s Revised Taxonomy and clearer justification of knowledge–skill pairings provide more explicit guidance for instructors and learners, while preserving flexibility in how solutions are conceived and implemented. These refinements ensure that the competencies are appropriately scoped, pedagogically sound, and clearly articulated, supporting effective implementation within a competency-based and problem-based learning context.

### Decision

- Approved with Revisions

### Next Steps

1. Incorporate the proposed adjustments into the official competency specification for Task 03.
2. Conduct a follow-up expert validation cycle, if necessary, focusing on the revised artifact.
3. Prepare the refined specification for subsequent CSP phases, including semantic structuring and reuse analysis.

The implemented revisions and their rationale should be recorded in the Task03 adjustments report, preserving traceability from the preliminary specification to the validated competency set.

