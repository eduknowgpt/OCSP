# CSRP-Report  
## Competency Specification Review & Refinement  
### Task202 – Team Control


## 1. Introduction

This **Competency Specification Review & Refinement Report (CSRP-Report)** presents the results of an **expert-based review** of the competencies reused in **Task202 – Team Control**, conducted as part of **Phase 2 (Expert Review)** of the **Competency Specification Process (CSP)**.

The purpose of the review was to evaluate the **adequacy, scope, and activation modes** of the selected competencies when applied to a task that explicitly exceeds the expressive power of Finite State Machines and requires **memory-based computational models**, namely **Pushdown Automata (PDAs)**. The review also aimed to identify **scope tensions and refinement opportunities** emerging from competency reuse in this more theoretically demanding context.



## 2. Overview of Reviewed Competencies

Based on the CSP-Report for Task202, the following competencies were reviewed by domain experts:

- **C12** – Develop problem-solving solutions using Pushdown Automata  
- **C03** – Test Automata Using Simulators  
- **C13** – Interpret Rule-Based Notation  
- **C05** – Write a Technical Report  
- **C14** – Differentiate Classifications of Formal Grammars  

Overall, the expert review identified a **strong alignment** between the task objectives and the selected competencies, particularly with respect to **formal limitation analysis**, **model adequacy justification**, and **memory-based computation**.


## 3. Competency-Level Review Findings

### 3.1 C12 – Develop problem-solving solutions using Pushdown Automata

**Review Outcome:** Very strong alignment  
**Detected Tension:** None  

Experts consistently identified **C12** as the **core competency** of Task202. The task explicitly requires the design, implementation, and justification of a **memory-based automaton**, and the competency’s scope was found to fully support the modeling of stack-dependent constraints, such as volunteer-to-non-volunteer ratios.

The review confirmed that C12 is sufficiently expressive to support **realistic control and validation problems** while preserving formal rigor.



### 3.2 C03 – Test Automata Using Simulators

**Review Outcome:** Very strong alignment  
**Detected Tension:** None  

The review highlighted **C03** as one of the most clearly operationalized competencies in Task202. Simulation and validation using **JFLAP** are explicit task requirements and produce observable, verifiable artifacts.

No scope mismatch or ambiguity was identified. Experts characterized C03 as a **stable and highly reusable competency** across different automaton models.



### 3.3 C13 – Interpret Rule-Based Notation

**Review Outcome:** Partial alignment  
**Detected Tension:** Moderate  

The expert review detected a **semantic and scope tension** in the reuse of **C13**. While the task requires learners to interpret **formal rule representations**—particularly **context-free grammars** and symbolic constraints—the competency’s title and description were perceived as **overly generic**.

Experts noted ambiguity regarding whether C13 refers to:
- institutional or business rules,
- formal grammatical rules, or
- rule-based notations in a broader sense.

In Task202, C13 was activated specifically in relation to **formal grammatical and automaton-based rule systems**, rather than general rule interpretation.



### 3.4 C05 – Write a Technical Report

**Review Outcome:** Strong alignment  
**Detected Tension:** None  

Experts confirmed that **C05** aligned directly with the requirement to produce a structured technical report in **SBC format**, documenting modeling decisions, simulation results, and formal justifications.

The competency was consistently activated as a **transversal documentation competency**, with no task-specific ambiguities identified.



### 3.5 C14 – Differentiate Classifications of Formal Grammars

**Review Outcome:** Strong alignment  
**Detected Tension:** Low  

The review identified **C14** as essential for supporting the **theoretical justification** required in Task202. Distinguishing between regular and context-free languages was central to explaining why FSMs are insufficient and PDAs are required.

Experts emphasized that C14 was appropriately activated at a **conceptual and justificatory level**, reinforcing model adequacy decisions grounded in the Chomsky hierarchy.



## 4. Cross-Competency Observations

The expert review highlighted a clear differentiation in **competency activation modes**:

- **Model-construction competencies** (C12),
- **Artifact-validation competencies** (C03),
- **Theoretical-justification competencies** (C14),
- **Documentation competencies** (C05),
- **Interpretative/symbolic competencies** (C13).

Experts noted that, unlike Task201—where tensions were related to **activation depth**—Task202 revealed a tension related to **semantic scope and naming clarity**, particularly in C13.



## 5. Implications for CSP Refinement and Adjustment

Based on the review findings, experts concluded that:

- The CSP adequately supports the reuse of competencies across increasing levels of theoretical complexity.
- The tension identified in C13 does **not** immediately justify the creation of a new competency, but does warrant a **CSP-Adjustment** focused on **clarifying scope and intended activation**.
- Explicit documentation of **activation modes** (constructive, analytical, interpretative) remains essential when reusing broadly defined competencies.

Experts recommended that potential future refinements concerning C13 be evaluated **longitudinally**, across multiple tasks, before considering structural changes to the competency set.



## 6. Conclusion

The expert-based review of Task202 confirms the robustness of the CSP in supporting **formal model transitions**, such as the progression from FSMs to PDAs. The competencies reused in this task were largely found to be well aligned with task demands, with **C12 emerging as the central competency** and **C03 and C14** providing strong complementary support.

The scope tension identified in **C13** was interpreted as an opportunity for **semantic clarification rather than immediate structural change**, reinforcing the CSP’s emphasis on **controlled, evidence-driven refinement**.

Task202 thus provides a valuable empirical case demonstrating how expert review contributes to the **iterative maturation of competency specifications**, particularly in tasks that expose the formal limits of computational models.
