# CSP-Report — TASK25.00 — *Coleção de Músicas*

## 1. Introduction

This report applies the **Competency Specification Process (CSP)** to **TASK25.00 — Coleção de Músicas**, an instructional task in the course **MATC94 – Introdução às Linguagens Formais e Teoria da Computação**, whose central goal is to evaluate the learner’s ability to **abstract a real-world domain and model it rigorously as a formal system**. In this task, the musical domain is reinterpreted through the concepts of **alphabets, strings, languages, formal operations, regular expressions, and symbolic codifications**, all mobilized at a **conceptual and justificatory level** rather than through implementation or simulation.

The problem statement requires students to answer a set of questions about musical scores, excerpts, concatenation, reversal, set-theoretic operations over collections of songs, and the possible formal equivalence between different symbolic representations such as scores and recordings. 

Crucially, all answers must be **mathematically justified**, which shifts the center of the task from intuitive interpretation toward **formal reasoning, symbolic precision, and explicit argumentative rigor**. 

Unlike some earlier CSP cycles in which refinement was documented through distinct review artifacts, the specification of TASK25.00 was consolidated through an **interactive process of iterative discussion and revision between two authors/reviewers**, progressively stabilizing the competency set, semantic scopes, and activation decisions within the CSP-Report itself. For this reason, the present document should be understood as the **consolidated competency specification** for the task.

From a competency perspective, TASK25.00 requires learners not only to model musical artifacts formally, but also to **operate on strings and languages**, **use algebraic notation correctly**, **reason about codification and equivalence**, **characterize regularity and expressiveness**, and **produce mathematically rigorous written answers**. The task therefore integrates **constructive, analytical, interpretative, and justificatory dimensions of competence activation**, reinforcing formal abstraction and explicit justification as central features of competency-based learning in Computation Theory. 




## 2. Instructional Entity Analysis

### 2.1 Identification

- **Title:** Coleção de Músicas  
- **Type:** Theoretical-conceptual task with emphasis on formal modeling and mathematical justification  
- **Domain:** Formal Languages and Computation Theory.




### 2.2 Description

The task requires learners to **abstract and model musical scores as formal objects**, establishing an explicit correspondence between the musical domain and the core concepts of Formal Language Theory. In this model:

- **musical notes** are treated as **symbols of an alphabet**;
- **songs** are represented as **finite strings**;
- **collections of songs** are formalized as **languages**.

Based on this representation, learners must analyze structural properties and apply classical operations over strings and languages, such as concatenation, reversal, union, intersection, complement, and Kleene closure. The task strongly emphasizes **mathematically justified answers**, requiring explicit use of formal definitions, theoretical properties, and logical arguments. Informal or intuitive explanations are not considered sufficient.  




### 2.3 Expected Learner Approach

To solve the task appropriately, learners are expected to:

- analyze the domain restrictions carefully, recognizing that scores may involve simple or compound symbols and that songs are finite strings of arbitrary length;
- define explicitly the formal representation, including the chosen alphabet, the notion of song as string, and the characterization of collections as languages;
- establish a clear boundary between **structural validity** and **semantic interpretation**;
- apply operations over strings and languages with correct formal notation;
- justify each conclusion through formal definitions, minimal examples, conceptual demonstrations, and counterexamples when necessary;
- use automata or regular expressions only at a **conceptual level**, when they help support an argument;
- discuss codifications between symbolic representations, including the preservation or loss of structural properties;
- document all reasoning with precise terminology and consistent mathematical notation. 




### 2.4 Expected Outcomes

By the end of the task, learners should be able to:

- define and use correctly the concepts of **alphabet, string, language, empty string, and language closure**;
- apply and interpret operations over strings and languages, including concatenation, union, intersection, complement, reversal, and Kleene closure;
- analyze and justify structural properties of languages, such as membership, finiteness, or infinitude;
- identify structural patterns in symbolic sequences and relate them to formal properties;
- abstract real-world musical artifacts as formal symbolic representations;
- analyze, at a conceptual level, the role of finite automata and regular expressions in justifying language properties;
- evaluate symbolic codifications and homomorphisms between different representations;
- produce mathematically rigorous answers and reports with clear definitions, examples, arguments, and conclusions.  




### 2.5 Acquisition Context

- Theoretical course in Computation Theory  
- Evaluative task focused on **formal argumentation and abstract modeling**. 





## 3. Knowledge Enumeration

To support a systematic and semantically coherent competency specification, the knowledge mobilized in TASK25.00 is organized below according to the formal demands of the task.




### 3.1 Computing Knowledge

#### Formal Languages

- alphabets, strings, and languages;
- empty string and empty language;
- finite and infinite languages;
- prefixes, suffixes, and substrings.



#### Operations on Languages

- union, intersection, difference, and complement;
- concatenation of strings and languages;
- Kleene closure;
- reversal of strings and languages;
- closure properties of language classes, at a conceptual level.


#### Regular Languages

- regular expressions as algebraic notation for describing languages;
- regularity as an expressive class, without requiring operational construction.


#### Finite Automata (Conceptual Level)

- finite automata as abstract recognizers;
- the theoretical relation between automata, regular expressions, and regular languages;
- expressive limits of finite automata as support for formal argumentation.


#### Homomorphisms and Codifications

- homomorphisms over strings and languages;
- mappings between different symbolic representations;
- preserved and non-preserved structural properties under codification;
- formal limits of representational equivalence.


#### Formal Reasoning

- formal definitions as grounds for validity;
- minimal examples as explanatory tools;
- counterexamples as instruments of refutation;
- logical justification of structural language properties. 





### 3.2 Foundational and Professional Knowledge (FPK)

- **Analytical and Critical Thinking**  
  Abstraction of real-world domains into formal models and rigorous assessment of claims in light of definitions and theoretical properties.

- **Written Communication**  
  Production of clear, well-structured, mathematically rigorous texts with precise terminology and consistent notation.

- **Epistemic Rigor**  
  Explicit commitment to formal justification rather than informal intuition, and the ability to distinguish definitions, examples, arguments, and conclusions. 






## 4. Learning Objectives

### 4.1 General Learning Objective

The general objective of TASK25.00 is to enable the learner to **abstract and model a real-world domain**—songs and musical collections—as **formal languages**, using fundamental concepts of language theory, regular expressions, and recognizer models at a conceptual level, while also **analyzing and justifying structural properties** through formal definitions, operations over languages, and mathematically rigorous reasoning. :contentReference[oaicite:12]{index=12}

### 4.2 Specific Learning Objectives

#### LO1 — Formal Abstraction of the Domain
- define formally an **alphabet (Σ)** from the relevant musical symbols;
- model a **song as a string** over Σ;
- model a **collection of songs as a language**.

#### LO2 — Structural Analysis of Strings
- identify and define formally **prefixes, suffixes, and substrings** of a song;
- determine whether a song excerpt can be formally considered a valid song;
- justify the validity or invalidity of excerpts from the beginning, middle, or end of a song.

#### LO3 — Operations over Languages
- apply **concatenation** of strings to model song composition;
- analyze whether the result of concatenation belongs to the original language;
- apply **union, intersection, and difference** to combine collections;
- evaluate the **complement** of a language with respect to an explicitly defined universe.

#### LO4 — Kleene Closure and Language Cardinality
- apply **Kleene closure** to a musical language;
- interpret the role of the **empty string** and the **empty language**;
- classify languages as **finite or infinite**, with formal justification.

#### LO5 — Reversal and String Transformations
- define formally the **reversal of strings**;
- apply reversal to a song and analyze its structural validity;
- distinguish explicitly **structural validity** from **semantic interpretation** in reversal contexts.

#### LO6 — Regular Languages and Formal Expressiveness
- recognize when a collection of songs can be described by a **regular language**;
- specify musical languages through **regular expressions**;
- distinguish, at a conceptual level, **regular** and **context-free** languages, indicating expressive limits without requiring grammar construction.

#### LO7 — Automata and Model Equivalence (Conceptual Level)
- explain the theoretical equivalence between **finite automata, regular expressions, and regular grammars**;
- relate structural song patterns to **conceptual states and transitions** of an automaton as a justificatory instrument.

#### LO8 — Homomorphisms and Codifications
- define formally **string homomorphisms**;
- analyze whether score and recording can be treated as **structurally equivalent codifications**;
- justify the formal limits of interchangeability between symbolic representations.

#### LO9 — Formal Reasoning and Proof
- use **formal definitions** as the basis for the validity of answers;
- construct **minimal examples** to illustrate language properties;
- employ **counterexamples** to refute incorrect claims;
- apply **inductive reasoning** when appropriate.

#### LO10 — Technical and Epistemic Communication
- elaborate a **technical report** with logical structure, argumentative clarity, and appropriate terminology;
- present mathematically rigorous justifications;
- distinguish explicitly between **informal intuition**, **illustrative example**, and **formal proof or argument**. :contentReference[oaicite:13]{index=13}







## 5. Competency Set for TASK25.00

Based on the analysis of the task requirements and the consolidated competency catalog, the following competencies were selected as directly aligned with TASK25.00.

### 5.1 Reused Competencies

#### **C04 — Define Regular Expressions for Finite Automata**

**Justification for Reuse:**  
Regular expressions constitute a relevant formal mechanism for the intentional specification of collections of songs in this task, especially when learners must characterize sets such as repeated songs, empty-song collections, or property-based subsets. In TASK25.00, this competency is activated at a **conceptual and algebraic level**, without requiring the operational construction of automata. It supports the learner’s ability to define regular languages formally and to relate them to structural descriptions of musical collections.

**ActivationRole:** `core`  
**ActivationMode:** `artifact-oriented`  
**ActivationConstraint:** `mandatory`



#### **C14 — Differentiate classifications of formal grammars**

**Justification for Reuse:**  
This competency supports conceptual distinctions between **regular languages** and more expressive classes. In TASK25.00, it is useful when learners discuss expressive limits, delimit the scope of formal constructions, or justify why certain collections may or may not fall within the regular class. Since such reasoning enriches but does not structure every answer, the competency is activated as an **extension**.

**ActivationRole:** `extension`  
**ActivationMode:** `analytical`  
**ActivationConstraint:** `optional`



#### **C18 — Model real-world problems using formal language concepts**

**Justification for Reuse:**  
TASK25.00 fundamentally requires learners to abstract musical artifacts as symbols, strings, and languages. This competency directly supports the formal modeling of the domain, including the explicit definition of alphabets, strings, collections, and representation constraints. It is one of the central competencies of the task.

**ActivationRole:** `core`  
**ActivationMode:** `constructive`  
**ActivationConstraint:** `mandatory`



#### **C19 — Apply homomorphisms in formal languages**

**Justification for Reuse:**  
The task explicitly asks whether a musical score and its corresponding recording may be treated as codifications of one another. This requires reasoning about homomorphisms, symbolic mappings, and representational equivalence. C19 therefore supports the analysis of preserved structure and the formal limits of interchangeability between representations.

**ActivationRole:** `supporting`  
**ActivationMode:** `interpretative`  
**ActivationConstraint:** `mandatory`







### 5.2 New Competencies Introduced in TASK25.00

#### **C05.01 — Write mathematically rigorous answers**
**Specialization of:** C05 — *Write a Technical Report*

**Justification for Introduction:**  
The main evidence required in TASK25.00 is not merely a technical report, but a set of **mathematically rigorous written answers**. The task demands explicit definitions, precise notation, structured arguments, minimal examples, and counterexamples where appropriate. Since the generic writing competency C05 does not fully capture this justificatory and epistemic requirement, a new specialized competency is introduced.

##### Competency Title
**Write mathematically rigorous answers**

##### Textual Description
This competency involves the ability to produce **mathematically rigorous written answers** that clearly justify conclusions through explicit definitions, precise notation, structured arguments, and appropriate supporting examples.

Learners demonstrate this competency by:

- stating relevant formal definitions clearly;
- organizing answers so that claims, justifications, and conclusions are explicitly connected;
- using examples or counterexamples when they help clarify or validate the reasoning;
- applying appropriate technical and mathematical notation consistently;
- presenting arguments with sufficient rigor to support the correctness of the conclusion.

This competency specializes technical report writing toward tasks in which the main evidence lies not only in presenting a result, but in **formally justifying why the result is valid**.

##### Knowledge Specification
- **Written Communication (FPK)**
- **Analytical and Critical Thinking (FPK)**

##### Disposition Specification
- **Meticulous**
- **Responsible**

##### Knowledge–Skill Pairing
- **Written Communication (FPK) — Apply**  
  → write, structure, document, clarify formal reasoning.
- **Analytical and Critical Thinking (FPK) — Analyze / Evaluate**  
  → distinguish assumptions, assess validity, support conclusions, identify inconsistencies.

##### ActivationRole
`transversal`

##### ActivationMode
`justificatory`

##### ActivationConstraint
`mandatory`





#### **C17 — Apply operations on formal languages**

**Justification for Introduction:**  
TASK25.00 requires sustained application and analysis of operations over strings and languages, including concatenation, union, intersection, complement, Kleene closure, and reversal. Although some of these actions might partially overlap with other competencies, the task demands a sufficiently central and explicit competency focused on formal operations and their structural consequences.

##### Competency Title
**Apply operations on formal languages**

##### Textual Description
This competency involves the ability to **apply, analyze, and justify formal operations over languages**, such as concatenation, union, intersection, complement, Kleene closure, and reversal, with explicit attention to their **structural effects** and **theoretical properties**.

Learners demonstrate this competency by:

- evaluating the structural pertinence of resulting languages;
- determining whether resulting languages preserve relevant properties, such as class membership, finiteness, or infinitude;
- justifying conclusions through definitions, examples, counterexamples, and known theoretical properties.

This competency is exercised **exclusively at a conceptual and algebraic level**, without requiring automaton construction, simulation, or implementation.

##### ActivationRole
`core`

##### ActivationMode
`analytical`

##### ActivationConstraint
`mandatory`



#### **C20 — Model and analyze musical collections as formal languages**

**Justification for Introduction:**  
TASK25.00 requires an integrated performance that cannot be reduced to any single atomic competency. Learners must model the domain, apply formal operations, reason about codifications, specify some collections through regular expressions, and justify all conclusions rigorously. A task-level composite competency is therefore introduced to represent this integrative performance.

##### Competency Title
**Model and analyze musical collections as formal languages**

##### Textual Description
This task-level competency involves the ability to **integrate concepts, operations, and representations from Formal Language Theory** in order to **model musical collections as formal languages** and **analyze rigorously their structural properties**.

Learners demonstrate this competency by:

- abstracting musical artifacts as symbols, strings, and languages;
- applying algebraic operations and regular expressions to characterize musical collections;
- analyzing formal codifications and transformations between representations;
- justifying structural properties, limitations, and implications through explicit definitions, minimal examples, counterexamples, and logical argumentation.

This competency synthesizes previously defined atomic competencies into a **coherent formal analysis of a real-world problem**, without requiring implementation or operational recognizer construction.

##### Competency Composition
C20 is composed of:
- **C18** — Model real-world problems using formal language concepts
- **C17** — Apply operations on formal languages
- **C19** — Apply homomorphisms in formal languages
- **C04** — Define Regular Expressions for Finite Automata
- **C23** — Interpret and apply algebraic notation for strings and languages
- **C05.01** — Write mathematically rigorous answers

##### ActivationRole
`core`

##### ActivationMode
`integrative`

##### ActivationConstraint
`mandatory`



#### **C23 — Interpret and apply algebraic notation for strings and languages**

**Justification for Introduction:**  
TASK25.00 requires a transversal competence in the interpretation and use of **algebraic notation for strings and languages**, including symbols such as ε, Σ, concatenation, exponentiation, reversal, substructures, set-theoretic language operations, and closure notation. This need is distinct from the interpretation of **rule-based notation** or **grammar-based rules**, and therefore should not be treated as a specialization of C13 or C13.01. A new independent competency is introduced to preserve semantic clarity in the catalog.

##### Competency Title
**Interpret and apply algebraic notation for strings and languages**

##### Textual Description
This competency involves the ability to **interpret, use, and justify formal algebraic notation for strings and languages** in order to represent, analyze, and communicate structural properties of symbolic systems.

Learners demonstrate this competency by:

- interpreting standard notation for **strings**, such as ε, Σ, |x|, concatenation, exponentiation, reversal, prefixes, suffixes, and substrings;
- interpreting and applying standard notation for **languages**, such as union, intersection, complement, concatenation, \(L^n\), and \(L^*\);
- using algebraic notation consistently to express structural properties, operations, and relations over strings and languages;
- connecting formal notation to conceptual reasoning about symbolic structures and language behavior;
- justifying the meaning and use of notation in formally rigorous answers.

This competency supports instructional contexts in which learners must **reason explicitly through symbolic notation**, not merely recognize concepts informally.

##### Knowledge Specification
- **Language Theory**
- **Formal Languages**
- **Written Communication (FPK)**
- **Analytical and Critical Thinking (FPK)**

##### Disposition Specification
- **Meticulous**
- **Responsible**

##### Knowledge–Skill Pairing
- **Language Theory — Understand**  
  → interpret, explain, identify formal notation for strings and symbolic structures.
- **Formal Languages — Apply**  
  → use, express, derive, manipulate notation for operations over languages.
- **Written Communication (FPK) — Apply**  
  → write, structure, clarify formal symbolic expressions in technically correct form.
- **Analytical and Critical Thinking (FPK) — Analyze**  
  → justify, distinguish, relate, validate symbolic interpretations.

##### ActivationRole
`transversal`

##### ActivationMode
`analytical`

##### ActivationConstraint
`mandatory`







## 6. Competency Activation Summary

| **Competency** | **ActivationRole** | **ActivationMode** | **ActivationConstraint** |
|---|---|---|---|
| C17 | core | analytical | mandatory |
| C18 | core | constructive | mandatory |
| C19 | supporting | interpretative | mandatory |
| C04 | core | artifact-oriented | mandatory |
| C23 | transversal | analytical | mandatory |
| C05.01 | transversal | justificatory | mandatory |
| C14 | extension | analytical | optional |
| C20 | core | integrative | mandatory |



## 7. LO × Competency Mapping

| **LO** | **Competencies Mobilized** |
|---|---|
| LO1.1 | C18, C23 |
| LO1.2 | C18, C23 |
| LO1.3 | C18, C23 |
| LO2.1 | C23, C17 |
| LO2.2 | C23, C17 |
| LO2.3 | C05.01, C23 |
| LO3.1 | C17, C23 |
| LO3.2 | C17 |
| LO3.3 | C17, C23 |
| LO3.4 | C17 |
| LO4.1 | C17 |
| LO4.2 | C23, C17 |
| LO4.3 | C17 |
| LO5.1 | C23, C17 |
| LO5.2 | C17, C05.01 |
| LO5.3 | C05.01, C18 |
| LO6.1 | C04, C14 |
| LO6.2 | C04, C23 |
| LO6.3 | C14 |
| LO7.1 | C04 |
| LO7.2 | C04 |
| LO8.1 | C19, C23 |
| LO8.2 | C19, C18 |
| LO8.3 | C19, C05.01 |
| LO9.1 | C05.01 |
| LO9.2 | C05.01 |
| LO9.3 | C05.01 |
| LO9.4 | C05.01, C17 |
| LO10.1 | C05.01 |
| LO10.2 | C05.01 |
| LO10.3 | C05.01 |



## 8. Ontological Reading of the Competency Set

The competency structure of TASK25.00 can be interpreted ontologically as follows:

- **C18** provides the foundational abstraction of the real-world domain into symbols, strings, and languages.
- **C17** supports the formal treatment of operations and their structural consequences.
- **C19** addresses codifications and equivalence between symbolic representations.
- **C04** contributes regular-expression-based intentional specification of languages.
- **C23** functions as a transversal notational competency, enabling learners to reason explicitly through the algebraic language of strings and languages.
- **C05.01** functions as a transversal justificatory competency, ensuring that answers are formally explicit and epistemically rigorous.
- **C20** integrates all of the above into the task-level performance expected in the formal analysis of musical collections.

This organization distinguishes clearly between:
- **domain abstraction**,
- **formal operations**,
- **representational transformation**,
- **algebraic notation**,
- **mathematical justification**, and
- **integrated task performance**.



## 9. Conclusion

The consolidated **CSP-Report of TASK25.00 — Coleção de Músicas** establishes a clear, traceable, and ontologically coherent competency structure for a task centered on the **formal modeling and analysis of symbolic collections** in a real-world-inspired domain. The task requires not only the construction of formal representations, but also the explicit justification of conclusions through algebraic notation, operations over languages, codification analysis, and mathematically rigorous written reasoning. 



The resulting competency set combines reused competencies whose semantic scopes remain stable across contexts (**C04, C14, C18, C19**) with new competencies introduced to address task-specific needs (**C05.01, C17, C20, and C23**). In particular, the introduction of **C23 — Interpret and apply algebraic notation for strings and languages** resolves the semantic mismatch that would arise from overextending grammar-based competencies to a distinctly algebraic-notational context. Likewise, **C05.01** captures the task’s requirement that evidence take the form of **mathematically rigorous answers**, not merely conventional technical documentation.

As a result, TASK25.00 is positioned not merely as an exercise in language manipulation, but as a task of **competency-based formal reasoning in Computation Theory**, in which learner performance can be assessed through explicit, structured, and semantically grounded evidence. This strengthens the alignment between the task demands, the competency catalog, and the OntoKSD model itself.