# **Expert Review: Task 04 – *The Return of the Farmer Robot***

## **1. Introduction**

Building on the **Competency Specification Process (CSP)** framework, this report documents **Phase 2 — Competency Expert Review** for the Problem-Based Learning (PBL) task *“The Return of the Farmer Robot.”* This phase is dedicated to the **systematic technical validation** of the competency specifications associated with the task, focusing on their **Knowledge, Skills, and Dispositions (K–S–D)** structure.

The primary objective of this review is to evaluate the competency specifications according to the following quality dimensions:

* **Theoretical accuracy and conceptual soundness**, ensuring alignment with formal foundations in Automata Theory, Formal Languages, and Computational Modeling;
* **Clarity and internal consistency**, promoting precise, unambiguous, and reusable competency definitions;
* **Pedagogical alignment**, verifying coherence between competencies, learning objectives, expected deliverables, and assessment practices;
* **Contextual applicability**, assessing the feasibility and instructional relevance of the competencies within the task’s problem-based scenario.

The review is grounded in **qualified expert judgment** and follows a **structured, artifact-centered evaluation protocol**. Domain specialists examined the competency specifications using predefined criteria to assess the adequacy, relevance, and coherence of the associated K–S–D elements. The analysis focuses exclusively on the **educational artifact**—namely, the task description and its competency model—and does not involve the collection or interpretation of personal, behavioral, or identifiable participant data.

This report synthesizes the outcomes of the expert review and formulates **actionable recommendations** aimed at improving the conceptual precision, pedagogical coherence, and instructional usability of the competency specifications.

The findings are organized according to the stages of the **Competency Specification Protocol**, comprising:

* **Instructional-context analysis**, validating task scope, complexity, and competency coverage;
* **Item-level evaluation**, identifying strengths, inconsistencies, and elements requiring refinement;
* **Cross-criterion synthesis**, integrating findings related to accuracy, clarity, alignment, and relevance;
* **Recommendations**, proposing concrete adjustments to optimize the competency framework.

By situating this analysis within **Phase 2 of the CSP**, the report contributes to the **iterative refinement and stabilization** of competency specifications, ensuring that they are **theoretically rigorous, pedagogically robust, and suitable for reuse** across similar instructional contexts in Computing Education.





## 2. Instructional Entity Summary

Context: A concise recap of Phase 1A findings to anchor the review.

- Title: The Farmer Robot

- Description: Learners are challenged to prototype a **decision-making module** that identifies the presence and counts specific herds—**bovines, caprines, and swine**—inside farm enclosures. This capability is essential for automating feed request logistics and optimizing farm management, all within operational needs and budget constraints.


| **Aspect**               | **Rating Options**              | **Evaluator Notes**                                                      |
| ------------------------ | ------------------------------- | ------------------------------------------------------------------------ |
| **Task Title**           | ✅ Clear | The title accurately reflect the task’s focus and scope            |
| **Problem Description**  | ✅ Clear | The problem statement is explicit, complete, and contextually relevant  |
| **Solution Development** |  ✅ Appropriate    | Solution steps are actionable and aligned with defined competencies     |
| **Expected Outcomes**    | ✅ Well Specified | Outcomes clearly relate to the tasks and competencies being assessed |


### Decision Threshold

According to protocol guidelines:

- Approved → All aspects rated ✅




## 3. Knowledge Component Review

### Knowledge Granularity and Relevance

| **Criterion**         | **Yes / Maybe / No** | **Evaluator Notes**                                                        |
| --------------------- | -------------------- | -------------------------------------------------------------------------- |
| **Comprehensiveness** |  Maybe                    | Are all essential knowledge areas present?                                  |
| **Relevance**         |  No                 | Does each knowledge element directly support task or competency goals?     |
| **Appropriateness**   |  No                    | Is the level of detail correctly balanced—not too general or too granular? |


### **Reviewer Recommendations**

Based on the expert review, the following recommendations were identified to improve the alignment between the competency specifications and the instructional demands of *Task 04 – The Return of the Farmer Robot*:

* **Refine knowledge components for task alignment**
  The current knowledge elements were found to be **overly broad or insufficiently aligned** with the specific learning objectives of the task. It is recommended to refine these components to better reflect the conceptual and operational demands of the problem scenario.

* **Replace “Finite Automata” with “Pushdown Automata (PDAs)”**
  The use of **Finite Automata** was deemed inadequate to model the behaviors required by the task, particularly those involving **memory-dependent state transitions**. Replacing this knowledge element with **Pushdown Automata (PDAs)** more accurately captures the computational power and structural features necessary to represent the task’s requirements.

* **Strengthen contextual linkage of knowledge elements**
  Knowledge components should be explicitly tied to **context-specific modeling requirements**, especially in aspects where **stack-based memory** is essential, such as navigation, backtracking, or return-path behavior. This linkage reinforces the relevance and assessability of the competency specifications.






## 4. Learning Objectives Review

**Objective:** Ensure that the learning objectives are explicit, aligned, and pedagogically sound. 

| **Criterion**       | **Yes / Maybe / No** | **Evaluator Notes**                                                         |
| ------------------- | -------------------- | --------------------------------------------------------------------------- |
| **Completeness**    |  Yes                 | Do the LOs cover both explicit and implicit learning goals?           |
| **Relevance**       |  Yes                 | Are all LOs essential within the context of the task?               |

### **Decision Thresholds**

- Approved



Perfeito. Segue a **versão aprimorada apenas dessa primeira parte**, com **menos redundância**, **maior objetividade** e **tom mais técnico**, mantendo o conteúdo decisório intacto.



## **5. Competency Definitions Review**

### **Knowledge Evaluation**

The expert review identified the need for **focused refinements** in the knowledge components associated with the competencies of *Task 04 – The Return of the Farmer Robot*. These refinements are required to ensure **conceptual adequacy**, **cognitive coherence**, and **alignment between the declared computational models and the task’s operational demands**.


Following the knowledge misalignment identified in Section 3, the following competency-level adjustments were required:

#### **Develop Problem-Solving Solutions Using Automata**

* **Knowledge Update**

  * **Replace:** *Finite Automata*
  * **With:** *Pushdown Automata (PDAs)*

* **Rationale**
  The task involves behaviors that rely on **memory-dependent navigation**, such as returning to previously visited locations. **Pushdown Automata**, through their stack-based memory, provide the minimal expressive power required to model these behaviors, whereas Finite Automata are insufficient for this purpose.



#### **Interpret Rule-Based Notation**

* **Knowledge Update**

  * **Replace:** *Finite Automata*
  * **With:** *Pushdown Automata (PDAs)*

* **Language Knowledge Update**

  * **Replace:** *Regular Languages*
  * **With:** *Context-Free Grammars (CFGs)* and *Context-Free Languages (CFLs)*

* **Bloom Alignment**

  * **Understand** — focused on interpreting, recognizing, and relating symbolic rule structures to their corresponding grammatical and automata representations.

* **Rationale**
  The interpretation of rule-based notation in this task depends on **hierarchical and nested structures**, which exceed the expressive power of Finite Automata. Aligning this competency with **PDAs and context-free formalisms** ensures conceptual and pedagogical coherence.



#### **Differentiate Classifications of Formal Grammars**

* **Knowledge Update**

  * **Replace:** *Finite Automata*
  * **With:** *Pushdown Automata (PDAs)*

* **Language Knowledge Update**

  * **Replace:** *Regular Languages*
  * **With:** *Context-Free Grammars (CFGs)* and *Context-Free Languages (CFLs)*

* **Bloom Alignment**

  * **Understand** — supporting conceptual comparison and differentiation across grammar classes and their associated automata.

* **Rationale**
  This competency emphasizes **conceptual classification rather than construction or execution**. The proposed alignment ensures engagement with the **appropriate abstraction level** and the formal models actually required by the task.


### **Decision Threshold**

* **Needs Revision**





### Knowledge–Skill Pairing & Bloom Alignment

**Objective:** Verify that each knowledge–skill pairing is logically justified and aligned with the correct cognitive level per Bloom’s Revised Taxonomy. 


| **Criterion**               | **Yes / Maybe / No** | **Evaluator Notes**                                                                                                                                                                |
| --------------------------- | -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Bloom-Level Suitability** |  No                    | Does the described action (skill) align with an appropriate Bloom’s level?  |
| **Verb Effectiveness**      |   Yes                   | Are verbs specific and action-oriented (e.g., “construct,” “analyze,” “evaluate”)                   |
| **Pairing Justification**   |   No                   | Is it clear how the knowledge element supports the skill?                          |

These results indicate that competency descriptions must be reformulated to explicitly reflect PDA-based reasoning and its corresponding cognitive demands.

## **6. Recommendations Synthesis**

Based on the expert review and the criteria established by the **Competency Specification Process (CSP)**, the following **prioritized recommendations** are proposed to strengthen the competency framework for *Task 04 – The Return of the Farmer Robot*:

1. **Realign Knowledge Components to PDA-Based Modeling**

   * Replace all references to **Finite Automata** with **Pushdown Automata (PDAs)** to accurately reflect the **stack-based memory requirements** inherent to return-path and navigation behaviors.
   * Replace **Regular Languages** with **Context-Free Grammars (CFGs)** and **Context-Free Languages (CFLs)** to ensure consistency between grammatical formalisms and the selected computational model.
   * Explicitly relate knowledge components to **stack operations, nested structures, and path-reversal mechanisms** exercised by the task.

2. **Clarify Cognitive Scope at the Competency Level**

   * Standardize **Bloom’s Taxonomy levels** at **Understand** for competencies focused on **interpretation, recognition, and conceptual differentiation** (e.g., grammar classes, rule-based notation).
   * Review and refine action verbs to ensure they accurately reflect the **intended depth of cognitive engagement** and avoid ambiguity between conceptual understanding and procedural execution.

3. **Strengthen Knowledge–Skill Pairing Justification**

   * For each knowledge–skill pairing, include a **concise rationale** explaining how the selected knowledge (e.g., PDAs) supports the expected skill.
   * Ensure that the relationship between **computational model, learner action, and task requirement** is explicit and logically grounded.

4. **Refine Bloom Alignment and Verb Usage**

   * Maintain **Understand** for interpretation-oriented competencies.
   * Where competencies involve **implementation, extension, or modeling activities**, consider higher-order verbs (e.g., *Design*, *Construct*) aligned with **Apply** or **Create**, provided these actions are genuinely required by the task.

5. **Validate Scope Consistency Across the Competency Set**

   * Verify that all competencies consistently reference **PDAs and context-free formalisms** where required.
   * Eliminate any residual references to **Finite Automata** or theoretical constructs not exercised within the task.



## **7. Conclusion and Decision**

The current competency framework for *Task 04 – The Return of the Farmer Robot* **requires revision prior to approval** due to:

* Inconsistent alignment between declared knowledge and task requirements (PDAs vs. Finite Automata);
* Insufficient justification in some **knowledge–skill pairings**;
* Residual inconsistencies in **terminology, Bloom alignment, and model scope**.

### **Next Steps**

1. Implement the recommended adjustments within the competency specification.
2. Conduct a **follow-up expert review** with the original panel or additional reviewers.
3. Prepare the revised specification for **Phase 3 – Semantic Structuring**.

Once these revisions are completed, the competency framework will be **conceptually coherent, pedagogically sound, and methodologically consistent**, effectively supporting the instructional objectives of *The Return of the Farmer Robot* within a competency-based and problem-based learning context.






