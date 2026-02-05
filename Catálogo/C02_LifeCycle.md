## **Competency C02 Specification**

# Ciclo de Vida


## 1. Definição Original — *CSP-Report (Ciclo 1)*

### Competency Specification**

### Competency Title  
    Determining When to Use Deterministic Finite Automata (DFA)  

### Competency Description  
This competency focuses on **understanding determinism in finite automata** and **determining when to apply non-determinism**. Students must analyze system constraints and **decide whether a deterministic or non-deterministic automaton** is the optimal choice for solving a given problem.

This competency requires the ability to:  
- **Differentiate deterministic and non-deterministic automata** based on their properties and practical applications.  
- **Assess problem requirements** to determine the most efficient automaton model.  
- **Justify the choice** of automaton type with logical reasoning and computational constraints.



### Knowledge Specification  
The following knowledge areas are essential for this competency:  

- **Automata over Infinite Objects**  
  - Understanding the characteristics, limitations, and applications of **deterministic vs. non-deterministic models**.  
  - Identifying scenarios where one model may be more advantageous than the other.  

- **Analytical and Critical Thinking (FPK)**  
  - Required for **evaluating system constraints and making informed decisions**.  
  - Enables students to develop **strategic reasoning** when choosing between DFA and NFA models.  



### Disposition Specification  
Similar to **Competency A**, this competency requires students to demonstrate key **behavioral attributes** that facilitate problem-solving and decision-making:  

- **Investigative Thinking** – Encourages curiosity and **critical analysis** of automaton properties and their applications.  
- **Collaboration** – Supports teamwork when discussing and justifying DFA vs. NFA choices.  
- **Responsibility** – Ensures logical consistency and accuracy in decision-making.  
- **Proactivity** – Promotes independent research and exploration of automata applications.  
- **Creativity** – Encourages innovative approaches to problem-solving when dealing with complex system constraints.  



### Knowledge-Skill Pairing  
This step pairs **knowledge areas with the corresponding skills** required to demonstrate competency.

#### Mapping Knowledge to Skills**  
To achieve this competency, students must demonstrate the ability to:  
- **Apply** Analytical and Critical Thinking to **differentiate deterministic and non-deterministic automata**.  
- **Understand** Automata over Infinite Objects to **correctly identify scenarios where a deterministic or non-deterministic automaton is more appropriate**.  



#### Bloom’s Taxonomy Alignment

To accurately assess the required skills for this competency, each knowledge component is aligned with **Bloom’s Revised Taxonomy**, ensuring a structured learning progression and appropriate cognitive challenge.  

- **Analytical and Critical Thinking (FPK) – Apply**  
  - Assesses the student's ability to **evaluate problem constraints and justify the choice** between **Deterministic Finite Automata (DFA) and Non-Deterministic Finite Automata (NFA)**.  
  - Requires the ability to **analyze the differences between DFA and NFA** and determine which model is **more suitable for a given problem scenario**.  
  - Ensures students can **logically argue their decisions** based on **computational efficiency, implementation complexity, and system constraints**.  

- **Automata over Infinite Objects (DFA/NFA) – Understand**  
  - Evaluates the student's **ability to differentiate and classify** deterministic and non-deterministic automata based on their properties.  
  - Requires the ability to **correctly identify when each type of automaton should be used**, recognizing their advantages and limitations.  
  - Ensures students develop **a conceptual understanding of the relationship between DFA, NFA, and problem constraints**, forming a solid foundation for decision-making.  


 #### Verb Annotation
- **Understand** → Automata over Infinite Objects → **Compare** DFA and NFA concepts.  
- **Apply** → Analytical and Critical Thinking → **Evaluate and decide** on the appropriate automaton model.  



### Summary Table for Competency C2

| Competency | Dispositions | Knowledge | Skill |
|---------------|-----------------|--------------|-----------|
| Determine when to use a DFA or NFA | **Investigative, Collaborative, Responsible, Proactive, Creative** | Automata over Infinite Objects | Understand (Compare) |
| | | Analytical and Critical Thinking (FPK) | Apply (Evaluate, Decide) |







## 2. Revisões — CSRP-Report (Ciclo 1: revisão por especialistas)

### Síntese das críticas diretamente relacionadas à C02

1. **Granularidade e taxonomia inadequadas**: a taxonomia usada (ACM CCS 2012) foi considerada “muito ampla”, dificultando anotar conteúdos como **DFA/NFA/regex** com precisão. 

2. **Ajustes **:

   * “**Review and reword the title** regarding when to use DFA or NFA”;
   * **remover** o par conhecimento–habilidade **“Equivalence of DFAs and NFAs - Understand (Compare)”**;
   * **remover referências a NFA** quando não estiverem ancoradas na descrição do caso/problema. 

3. Reforço de **relevância/ancoragem no caso PBL**: destacou-se, na revisão, que certos itens (ex.: equivalências DFA≡NFA e FA≡RE) **não estavam cobertos** no enunciado do caso e deveriam ser removidos. 

**Decisão do ciclo:** *Needs Revision* (o relatório marca que vários elementos precisavam de revisão para ganhar precisão e aderência ao caso). 



## 3. Alterações implementadas — CSP-Adjustments (pós-CSRP, ciclo 1)


### Mudanças declaradas

* **Título redefinido** para: *“Justifying the Use of Deterministic Finite Automata (DFA)”*;

* Conhecimento **“Finite Automaton”** redefinido como **“Deterministic Finite Automata (DFA)”**;

* Inclusão de novo par: **Requirements Engineering - Apply**. 



## 4. Versão atual da C02 — íntegra

### Competency Title

    Justify the use of Deterministic Finite Automata (DFAs)

### Competency Description

> This competency focuses on students' ability to **distinguish between deterministic and non-deterministic finite automata**, and **evaluate which model is best suited** to a given problem. Emphasis is placed on understanding the implications of determinism in automata design and on making reasoned decisions based on system constraints and complexity.

> Students must be able to:

- **Compare DFA and NFA models** based on structural and behavioral differences.
- **Analyze task requirements** to identify whether determinism is essential or optional.
- **Select and justify** the most appropriate model for implementation. 


### Knowledge Specification

The following knowledge areas are essential for this competency:

- **Deterministic Finite Automata (DFAs)**
  - Understanding the structure, behavior, and limitations of DFAs, including states, transitions, and acceptance conditions.
  - Ability to distinguish DFAs from non-deterministic models when analyzing problem constraints.

- **Analytical and Critical Thinking (FPK)**
  - Required to evaluate system constraints and reason about the suitability of deterministic versus non-deterministic solutions.
  - Supports informed decision-making based on computational efficiency and problem requirements.

- **Requirements Engineering**
  - Enables alignment between problem specifications and the selected automaton model.



### Disposition Specification  
- **Investigative** – Encourages curiosity and **critical analysis** of automaton properties and their applications.  
- **Collaboration** – Supports teamwork when discussing and justifying DFA vs. NFA choices.  
- **Responsibility** – Ensures logical consistency and accuracy in decision-making.  
- **Proactivity** – Promotes independent research and exploration of automata applications.  
- **Creativity** – Encourages innovative approaches to problem-solving when dealing with complex system constraints.  



### Knowledge–Skill Pairing

This section defines explicit **Knowledge–Skill (KS) pairs**, clarifying how each knowledge area is operationalized through observable actions.

#### Knowledge–Skill Mapping

To demonstrate this competency, students must be able to:

- **Deterministic Finite Automata (DFAs) – Understand**
  - Compare deterministic and non-deterministic finite automata.
  - Identify structural and behavioral properties that characterize DFAs.
  - Recognize scenarios in which determinism is required or advantageous.

- **Analytical and Critical Thinking (FPK) – Apply**
  - Evaluate problem constraints, such as input determinism, state complexity, and implementation requirements.
  - Analyze trade-offs between deterministic and non-deterministic solutions.
  - Justify the selection of a DFA based on logical reasoning and computational considerations.

- **Requirements Engineering – Apply**
  - Interpret functional and non-functional requirements of the problem.
  - Translate system requirements into constraints that guide the choice of an automaton model.
  - Align the selected DFA model with the specified problem requirements.




### Bloom’s Taxonomy Alignment

Each KS pair is aligned with Bloom’s Revised Taxonomy to ensure appropriate cognitive demand and assessable performance:

- **Understand (DFAs)**
  - Focuses on conceptual comprehension, comparison, and classification of DFA and NFA models.
  - Establishes the theoretical basis required for informed model selection.

- **Apply (Analytical and Critical Thinking – FPK)**
  - Emphasizes the application of reasoning strategies to real problem constraints.
  - Requires students to justify decisions rather than merely recognize differences.

- **Apply (Requirements Engineering)**
  - Involves applying structured analysis techniques to interpret and organize requirements.
  - Supports evidence-based justification for adopting a deterministic automaton.
 

### Verb Annotation (Summary)

- **Understand** → *Deterministic Finite Automata (DFAs)* → Compare, classify, recognize.
- **Apply** → *Analytical and Critical Thinking (FPK)* → Analyze, evaluate, justify.
- **Apply** → *Requirements Engineering* → Interpret, organize, align.



### Table — Competency C02 (Post-Adjustments)

| **ID** | **Competency** | **Dispositions** | **Knowledge** | **Skill (Bloom)** |
|------|-----------------|------------------|---------------|-------------------|
| C02 | **Justify the use of Deterministic Finite Automata (DFAs)** | Investigative, Collaborative, Responsible, Proactive | Deterministic Finite Automata (DFAs) | **Understand (Compare)** |
|     |                 |                  | Requirements Engineering | **Apply (Interpret, Organize)** |
|     |                 |                  | Analytical and Critical Thinking (FPK) | **Apply (Analyze, Evaluate, Justify)** |








