# CSP Review Adjustments Report: Task 01 – *The Vending Machine for Sodas and Snacks*

## Introduction

The expert review process identified a set of **systematic improvement opportunities** within the competency specification associated with Task 01. These opportunities emerged from a structured technical analysis of the competency model and were consolidated into **five core adjustment dimensions**, each addressing a distinct aspect of conceptual, pedagogical, or representational quality:

* **Knowledge Granularity** — calibrating the level of detail to ensure conceptual precision without unnecessary abstraction;
* **Knowledge Appropriateness** — ensuring that all knowledge elements are directly relevant to, and operationalized by, the task requirements;
* **Controlled Vocabulary** — standardizing terminology to promote consistency, interoperability, and reuse across competency specifications;
* **Bloom’s Taxonomy Verbs** — refining action verbs to clearly express observable skills and intended cognitive levels;
* **Textual Clarity** — improving wording to eliminate ambiguity, redundancy, and overly prescriptive formulations.

In response to these findings, a set of **targeted revisions** was implemented to strengthen the **specificity, coherence, and reusability** of the competency specifications. These adjustments ensure tighter alignment between the problem context, learning objectives, and competency definitions, while reinforcing the role of the CSP as a systematic and iterative process for developing high-quality, reusable competency artifacts.




## **Review Findings and Implemented Adjustments**

This section summarizes the **key findings of the expert review** and the **adjustments effectively implemented** in response to the identified issues. The revisions aim to improve **conceptual precision**, **pedagogical alignment**, and **reusability** of the competency specifications associated with Task 01.



### **Knowledge Granularity Refinement**

In response to the limitations identified in the initial knowledge representation, the **knowledge classification system was updated from CC2012 to CS2013**, which provides a **more fine-grained, hierarchical, and education-oriented taxonomy**. This transition enables more precise annotation of knowledge elements, supports clearer differentiation among concepts, and enhances the **reusability and interoperability** of competencies across instructional contexts.


### **Competency-Specific Adjustments**

The following refinements were applied at the individual competency level to ensure tighter alignment between **task requirements**, **knowledge components**, and **skill descriptors**.

* **Competency A — *Developing Problem Solutions Using Automata***

  * The knowledge element **“Finite Automaton”** was refined to **“Finite State Machines”**, improving conceptual specificity and alignment with the task scope.
  * The knowledge element **“Requirements Analysis”** was refined to **“Requirements Engineering”**, reflecting a more precise and standardized terminology.

* **Competency B — *Justifying the Use of Deterministic Finite Automata (DFA)***

  * The competency title was reformulated to remove references to non-deterministic models and to emphasize justification within the task scope.
  * The knowledge element **“Finite Automaton”** was refined to **“Deterministic Finite Automata (DFA)”**, ensuring conceptual coherence.
  * The knowledge element **“Requirements Analysis”** was refined to **“Requirements Engineering.”**
  * A new **knowledge–skill pairing**, **“Analytical and Critical Thinking (FPK) — Apply,”** was introduced to explicitly capture the reasoning and justification processes required by the competency.

* **Competency C — *Testing Automata Using Simulators***

  * The knowledge element **“Automata over Infinite Objects”** was replaced with **“Finite State Machines”**, eliminating conceptual mismatch and improving clarity.
  * A new **knowledge–skill pairing**, **“Modeling and Simulation — Apply,”** was introduced to ensure that learners actively apply modeling concepts when validating automata behavior using simulation tools.

* **Competencies D and E — Merging and Refinement**

  * The competencies *“Determining Regular Expressions that Represent Automata”* and *“Relating Regular Expressions to Finite Automata”* were **merged** into a single competency: **“Defining Regular Expressions for Finite Automata.”**
  * Associated knowledge refinements included:

    * **“Finite Automaton — Understand”** refined to **“Finite State Machines — Understand”;**
    * **“Regular Languages — Understand”** refined to **“Regular Expressions — Apply”;**
    * **“Analytical and Critical Thinking (FPK)”** remained unchanged, as it continues to support reasoning across representations.

* **Competency F — *Writing a Technical Report***

  * The competency title was refined from *“Collaborative Technical Report Writing”* to **“Writing a Technical Report,”** emphasizing the observable outcome rather than the collaboration mode.
  * The knowledge element **“Technical Report”** was refined to **“Written Communication (FPK),”** aligning the competency with transversal professional knowledge.
  * The Bloom’s Taxonomy level was maintained at **Apply**, with action verbs such as *write, structure, revise,* and *refine*.



### **Controlled Vocabulary Standardization**

The review confirmed that the use of **multiple Bloom-aligned action verbs** within competency descriptions enhances the explicitness of expected learner actions. To support consistency and reuse, a **controlled vocabulary strategy** was adopted, ensuring alignment between competency descriptions, knowledge elements, and learning objectives.

To further strengthen semantic coherence, a **structured vocabulary-mapping mechanism** will be established, defining **preferred terms and accepted synonyms**. This approach supports interoperability across competency specifications and facilitates integration within the **OntoKSD** framework.







## **Competency Specification Adjustments**

## **Competency A Specification**

### A.1 Competency Title

    Develop problem solutions using Automata

### A.2 Competency Description

This competency refers to the ability to **design, construct, and validate automaton-based solutions** that address well-defined computational problems. Students are expected to interpret system requirements and model behavior using **automata**, applying formal methods to ensure **logical consistency and operational correctness**.

Students must:

* **Translate problem specifications into automaton models** using states and transitions.
* **Implement automata using appropriate tools**, ensuring their behavior aligns with the intended system logic.
* **Refine and test the automaton** through simulation, addressing edge cases and improving robustness.
* **Integrate constraints or extensions** when needed, demonstrating flexibility and adaptive problem-solving.



## **Competency B Specification**

### B.1 Competency Title

    Justify the use of Deterministic Finite Automata (DFAs)

### B.2 Competency Description

This competency focuses on students' ability to **distinguish between deterministic and non-deterministic finite automata**, and **evaluate which model is best suited** to a given problem. Emphasis is placed on understanding the implications of determinism in automata design and on making reasoned decisions based on system constraints and complexity.

Students must be able to:

* **Compare DFA and NFA models** based on structural and behavioral differences.
* **Analyze task requirements** to identify whether determinism is essential or optional.
* **Select and justify** the most appropriate model for implementation.



## **Competency C Specification**

### C.1 Competency Title

    Test Automata Using Simulators
    

### C.2 Competency Description

This competency relates to the **use of simulation tools** (e.g., JFLAP) to verify the correctness and behavior of automata implementations. It emphasizes systematic testing and iterative refinement of state-machine models.

Students must be able to:

* **Operate automata simulators** to test input/output behavior and transitions.
* **Interpret simulation outcomes**, identifying discrepancies between expected and observed behavior.
* **Diagnose and correct errors** through debugging cycles.
* **Apply problem-solving strategies** to refine automata until desired performance is achieved.



## **Competency D+E Specification**

### D+E.1 Competency Title

    Define Regular Expressions for Finite Automata

### D+E.2 Competency Description

This competency focuses on the ability to **relate regular expressions to finite automata**, both theoretically and in practice.

Students must be able to:

* **Understand the equivalence** between regular expressions and finite automata.
* **Construct regular expressions** that capture the same language accepted by a given finite automaton.
* **Translate automaton structures into expressions**, using standard notation and simplification rules.
* **Validate correctness** by comparing the behavior of both representations through testing or formal proof.


## **Competency F Specification**

### F.1 Competency Title

    Write a Technical Report

### F.2 Competency Description

This competency involves the **collaborative production of a well-organized technical report** that effectively communicates the design, implementation, and evaluation of automaton-based solutions.

Students must demonstrate the ability to:

* **Write and structure a report** that synthesizes the team's work in a coherent narrative.
* **Apply technical writing conventions**, ensuring clarity, precision, and logical flow.
* **Document technical results and reasoning**, including diagrams, formal representations, and testing outcomes.
* **Revise and polish the report collaboratively**, integrating peer feedback and adhering to presentation standards.



 ## Table of Competencies for Task: *The Vending Machine for Sodas and Snacks*

| **ID**  | **Competency** | **Dispositions** | **Knowledge** | **Skill** |
|---------|--------|-----------|-----------|-------------------|
| (C01) | **Develop problem solutions using Automata** | Collaborative, Responsible, Proactive, Creative | Finite State Machines | **Create (Construct, Develop, Design)** |
|         |                                   |                                 | Requirements Engineering | **Apply (Interpret, Implement, Organize)** |
|         |                                   |                                 | Analytical and Critical Thinking (FPK) | **Apply** |
|  |  |                                        |       |       
| (C02) | **Justify the use of Deterministic Finite Automata (DFAs)** | Investigative, Collaborative, Responsible, Proactive | Deterministic Finite Automata (DFAs) | **Understand (Compare)** |
|         |                                   |                                 | Requirements Engineering | **Apply** |
|         |                                   |                                 | Analytical and Critical Thinking (FPK) | **Apply** |
|  |  |                                        |       |       
| (C03) | **Test automata using simulators** | Investigative, Collaborative, Responsible, Proactive, Creative | Finite State Machines | **Apply (Experiment, Relate, Simulate)** |
|         |                                   |                                 | Problem Solving and Troubleshooting (FPK) | **Apply** |
|         |                                   |                                 | Modeling and Simulation | **Apply** |
|  |  |                                        |       |       
| (C04) | **Define Regular Expressions for Finite Automata** | Investigative, Collaborative, Responsible, Proactive, Creative | Finite State Machines | **Understand** |
|         |                                   |                                 | Regular Expressions | **Apply** |
|         |                                   |                                 | Analytical and Critical Thinking (FPK) | **Apply** |
|  |  |                                        |       |       
| (C05) | **Write a technical report** | Collaborative, Meticulous, Responsible | Written Communication (FPK) | **Apply (Write, Structure, Revise, Refine)** |




## Conclusion

The expert review process resulted in **substantial and well-founded improvements** to the competency specification associated with Task 01. The implemented adjustments refined competency definitions, increased conceptual specificity, standardized terminology, and enhanced overall textual clarity, thereby strengthening the internal coherence of the competency framework.

The adoption of a **more fine-grained knowledge taxonomy (CS2013)** enabled more precise representation of domain concepts and improved the **reusability and interoperability** of competencies across instructional contexts. In parallel, the introduction of a **controlled vocabulary and structured terminology mapping** ensured greater consistency and semantic alignment among competency titles, descriptions, and associated knowledge–skill pairings.

The consolidation of redundant competencies, along with targeted refinements to knowledge elements and skill descriptors, contributed to a **more coherent, structured, and pedagogically aligned competency model**. These revisions improved the correspondence between task requirements, learning objectives, and observable outcomes, reinforcing the role of the CSP as a systematic mechanism for competency design.

Looking forward, **continuous iterative refinement and structured expert validation** will remain essential to maintaining the quality and relevance of the competency specification model. Through successive review cycles, the framework can adapt to evolving instructional contexts while preserving conceptual clarity and alignment with educational objectives. Collectively, these practices support a more effective and sustainable **competency-based learning approach**, grounded in precise, applicable, and reusable competency definitions.


 
