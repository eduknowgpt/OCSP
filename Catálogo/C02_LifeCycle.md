## **Competency C02 Specification**

# Lifecycle

## 1. Original Definition — *CSP Report (Cycle 1)*

### Competency Specification

### Competency Title
    Determining When to Use Deterministic Finite Automata (DFA)

### Competency Description
This competency focuses on **understanding determinism in finite automata** and **determining when to apply non-determinism**. Students must analyze system constraints and **decide whether a deterministic or non-deterministic automaton** is the most appropriate choice for solving a given problem.

This competency requires the ability to:
- **Differentiate deterministic and non-deterministic automata** based on their properties and practical applications.
- **Assess problem requirements** to determine the most suitable automaton model.
- **Justify the choice** of automaton type using logical reasoning and computational constraints.

### Knowledge Specification
The following knowledge areas are essential for this competency:

- **Automata over Infinite Objects**
  - Understanding the characteristics, limitations, and applications of **deterministic and non-deterministic models**.
  - Identifying scenarios in which one model may be more advantageous than the other.

- **Analytical and Critical Thinking (FPK)**
  - Required for **evaluating system constraints and making informed decisions**.
  - Enables students to develop **strategic reasoning** when choosing between DFA and NFA models.

### Disposition Specification
Similar to **Competency A**, this competency requires students to demonstrate key **behavioral attributes** that support problem-solving and decision-making:

- **Investigative Thinking** – Encourages curiosity and **critical analysis** of automaton properties and their applications.
- **Collaboration** – Supports teamwork when discussing and justifying DFA versus NFA choices.
- **Responsibility** – Ensures logical consistency and accuracy in decision-making.
- **Proactivity** – Promotes independent research and exploration of automata applications.
- **Creativity** – Encourages innovative approaches to problem-solving when dealing with complex system constraints.

### Knowledge–Skill Pairing
This step pairs **knowledge areas with the corresponding skills** required to demonstrate the competency.

#### Mapping Knowledge to Skills
To achieve this competency, students must demonstrate the ability to:
- **Apply** Analytical and Critical Thinking to **differentiate deterministic and non-deterministic automata**.
- **Understand** Automata over Infinite Objects in order to **correctly identify scenarios in which a deterministic or non-deterministic automaton is more appropriate**.

#### Bloom’s Taxonomy Alignment

To accurately assess the required skills for this competency, each knowledge component is aligned with **Bloom’s Revised Taxonomy**, ensuring a structured learning progression and an appropriate cognitive challenge.

- **Analytical and Critical Thinking (FPK) – Apply**
  - Assesses the student's ability to **evaluate problem constraints and justify the choice** between **Deterministic Finite Automata (DFA)** and **Non-Deterministic Finite Automata (NFA)**.
  - Requires the ability to **analyze the differences between DFA and NFA** and determine which model is **more suitable for a given problem scenario**.
  - Ensures that students can **logically justify their decisions** based on **computational efficiency, implementation complexity, and system constraints**.

- **Automata over Infinite Objects (DFA/NFA) – Understand**
  - Evaluates the student's **ability to differentiate and classify** deterministic and non-deterministic automata based on their properties.
  - Requires the ability to **correctly identify when each type of automaton should be used**, recognizing their advantages and limitations.
  - Ensures that students develop **a conceptual understanding of the relationship between DFA, NFA, and problem constraints**, forming a solid foundation for decision-making.

#### Verb Annotation
- **Understand** → Automata over Infinite Objects → **Compare** DFA and NFA concepts.
- **Apply** → Analytical and Critical Thinking → **Evaluate and decide** on the appropriate automaton model.

### Summary Table for Competency C02

| Competency | Dispositions | Knowledge | Skill |
|------------|--------------|-----------|-------|
| Determine when to use a DFA or NFA | **Investigative, Collaborative, Responsible, Proactive, Creative** | Automata over Infinite Objects | Understand (Compare) |
| | | Analytical and Critical Thinking (FPK) | Apply (Evaluate, Decide) |

## 2. Revisions — *CSRP Report (Cycle 1: Expert Review)*

### Summary of Critiques Directly Related to C02

1. **Inadequate granularity and taxonomy**: the taxonomy used (ACM CCS 2012) was considered **too broad**, making it difficult to annotate content such as **DFA/NFA/regex** with sufficient precision.

2. **Recommended adjustments**:
   * “**Review and reword the title** regarding when to use DFA or NFA”;
   * **remove** the knowledge–skill pair **“Equivalence of DFAs and NFAs – Understand (Compare)”**;
   * **remove references to NFA** when they are not grounded in the case/problem description.

3. Reinforcement of **relevance and grounding in the PBL case**: the review highlighted that certain elements (e.g., DFA≡NFA and FA≡RE equivalences) were **not covered** in the problem statement and therefore should be removed.

**Cycle decision:** *Needs Revision* (the report indicated that several elements required revision in order to improve precision and adherence to the case).

## 3. Implemented Changes — *CSP Adjustments (Post-CSRP, Cycle 1)*

### Declared Changes

- **Title redefined** as: *“Justifying the Use of Deterministic Finite Automata (DFA)”*;
- Knowledge element **“Finite Automaton”** redefined as **“Deterministic Finite Automata (DFA)”**;
- Inclusion of a new pair: **Requirements Engineering – Apply**.

## 4. Current Version of C02 — Full Specification

## **Competency C02 Specification**

### Competency Title

    Justify the use of Deterministic Finite Automata (DFAs)

### Competency Description

> This competency focuses on students’ ability to justify the use of Deterministic Finite Automata (DFAs) as appropriate formal models for solving well-defined computational problems. Emphasis is placed on recognizing the implications of determinism for automaton design and on providing reasoned justifications for adopting DFAs based on problem requirements, representational clarity, and implementation constraints.

> Students must be able to:

- Recognize and explain the defining properties of DFAs that make them suitable for a given problem.
- Analyze task requirements in order to determine whether a deterministic model is appropriate.
- Justify the adoption of a DFA through clear and logically grounded arguments based on formal and practical considerations.

### Knowledge Specification

The following knowledge areas are essential for this competency:

- **Deterministic Finite Automata (DFAs)**
  - Understanding the structure, behavior, and limitations of DFAs, including states, transitions, and acceptance conditions.
  - Ability to recognize the formal properties of DFAs that make them suitable for modeling specific computational problems.

- **Analytical and Critical Thinking (FPK)**
  - Required to evaluate system constraints and reason about the suitability of deterministic versus non-deterministic solutions.
  - Supports informed decision-making based on computational efficiency and problem requirements.

- **Requirements Engineering**
  - Enables alignment between problem specifications and the selected automaton model.

### Disposition Specification
- **Investigative** – Encourages curiosity and **critical analysis** of automaton properties and their applications.
- **Collaboration** – Supports teamwork in discussing problem requirements, model suitability, and the formal justification for adopting DFAs.
- **Responsibility** – Ensures logical consistency and accuracy in decision-making.
- **Proactivity** – Promotes independent research and exploration of automata applications.

### Knowledge–Skill Pairing

This section defines explicit **Knowledge–Skill (KS) pairs**, clarifying how each knowledge area is operationalized through observable actions.

#### Knowledge–Skill Mapping

To demonstrate this competency, students must be able to:

- **Deterministic Finite Automata (DFAs) – Understand**
  - Identify the structural and behavioral properties that characterize DFAs.
  - Explain how determinism constrains and guides automaton behavior.
  - Recognize problem situations in which DFAs provide an appropriate formal model.

- **Analytical and Critical Thinking (FPK) – Apply**
  - Evaluate problem constraints, such as input determinism, state complexity, and implementation requirements.
  - Analyze how problem constraints, representational clarity, and implementation requirements support the adoption of a deterministic solution.
  - Justify the selection of a DFA based on logical reasoning and computational considerations.

- **Requirements Engineering – Apply**
  - Interpret functional and non-functional requirements of the problem.
  - Translate system requirements into constraints that guide the choice of an automaton model.
  - Align the selected DFA model with the specified problem requirements.

### Bloom’s Taxonomy Alignment

Each KS pair is aligned with Bloom’s Revised Taxonomy to ensure appropriate cognitive demand and assessable performance:

- **Understand (DFAs)**
  - Focuses on conceptual comprehension and explanation of the defining properties of DFAs.
  - Establishes the theoretical basis required to justify the use of deterministic automata in appropriate problem settings.

- **Apply (Analytical and Critical Thinking – FPK)**
  - Emphasizes the application of reasoning strategies to real problem constraints.
  - Requires students to justify decisions rather than merely recognize differences.

- **Apply (Requirements Engineering)**
  - Involves applying structured analysis techniques to interpret and organize requirements.
  - Supports evidence-based justification for adopting a deterministic automaton.

### Verb Annotation (Summary)

- **Understand** → *Deterministic Finite Automata (DFAs)* → Identify, explain, recognize.
- **Apply** → *Analytical and Critical Thinking (FPK)* → Analyze, evaluate, justify.
- **Apply** → *Requirements Engineering* → Interpret, organize, align.

### Table — Competency C02 (Post-Adjustments)

| **ID** | **Competency** | **Dispositions** | **Knowledge** | **Skill (Bloom)** |
|------|-----------------|------------------|---------------|-------------------|
| C02 | **Justify the use of Deterministic Finite Automata (DFAs)** | Investigative, Collaborative, Responsible, Proactive | Deterministic Finite Automata (DFAs) | **Understand (Identify, Explain, Recognize)** |
|     |                 |                  | Requirements Engineering | **Apply (Interpret, Organize, Align)** |
|     |                 |                  | Analytical and Critical Thinking (FPK) | **Apply (Analyze, Evaluate, Justify)** |