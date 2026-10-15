# CSP-Report — TASK25.00 — *Music Collection*

## 1. Introduction

This report records the competency specification for TASK25.00 — Music Collection, in MATC94 — Introduction to Formal Languages and Theory of Computation. The task requires mathematically justified answers about musical scores, strings, collections, formal operations, and encodings.

### 1.1 Purpose within CSP Cycle 3

Cycle 3 was designed to demonstrate the reusability of mature competency specifications—specifications regarded by the collaborators as stable and previously reviewed—within the same Theory of Computation discipline. Task authors, competency specifiers, and reviewers discussed the tasks from their conception with intended reuse in view, considering new competencies where the available specifications did not adequately cover the required performance.

TASK25.00 accordingly documents which competencies are reused, how their use is qualified in this context, and why additional specifications are retained. Reuse is the design objective; it does not require every competency in the resulting set to be pre-existing. Stability of a reused specification is distinguished from the contextual role assigned to it.

### 1.2 Integrated specification and interactive review

Task authors, competency specifiers, and reviewers collaborated during task development and specification. Interactive review occurred within that work: the task demands, opportunities for reuse, boundaries of new competencies, and expected performance were discussed together. This report consolidates the resulting specification and the rationale for the decisions adopted.

Specification and interactive review are documented as one integrated activity with iterative discussion. A single report does not imply a single exchange or the absence of refinement. Sections 2–7 state the instructional analysis, components, objectives, and associations; Section 8 explains their implications for OntoKSD; Section 9 connects the issues considered to the decisions and their implementation in this report.

No separate CSP-Review or CSP-Adjustments document was produced for this application. The integrated record captures the substantive decisions available, without reconstructing an exchange-by-exchange chronology, attributing unrecorded comments to individuals, or assigning a separate approval event. A future formal review would constitute a further activity.

### 1.3 Instructional focus

The musical domain is represented through alphabets, strings, languages, formal operations, regular expressions, and symbolic encodings. The expected performance is conceptual, algebraic, and justificatory. The task requires explicit mathematical reasoning without requiring implementation, automaton construction, or simulation. The sections below preserve the recorded objectives, competency components, activation decisions, and composition relations.

## 2. Instructional Entity Analysis

### 2.1 Identification

- Title: Music Collection  
- Type: Theoretical-conceptual task with emphasis on formal modeling and mathematical justification  
- Domain: Formal Languages and Computation Theory.

### 2.2 Description

The task requires learners to abstract and model musical scores as formal objects, establishing an explicit correspondence between the musical domain and the core concepts of Formal Language Theory. In this model:

- musical notes are treated as symbols of an alphabet;
- songs are represented as finite strings;
- collections of songs are formalized as languages.

Based on this representation, learners must analyze structural properties and apply classical operations over strings and languages, such as concatenation, reversal, union, intersection, complement, and Kleene closure. The task strongly emphasizes mathematically justified answers, requiring explicit use of formal definitions, theoretical properties, and logical arguments. Informal or intuitive explanations are not considered sufficient.  

### 2.3 Expected Learner Approach

To solve the task appropriately, learners are expected to:

- analyze the domain restrictions carefully, recognizing that scores may involve simple or compound symbols and that songs are finite strings of arbitrary length;
- define explicitly the formal representation, including the chosen alphabet, the notion of song as string, and the characterization of collections as languages;
- establish a clear boundary between structural validity and semantic interpretation;
- apply operations over strings and languages with correct formal notation;
- justify each conclusion through formal definitions, minimal examples, conceptual demonstrations, and counterexamples when necessary;
- use automata or regular expressions only at a conceptual level, when they help support an argument;
- discuss codifications between symbolic representations, including the preservation or loss of structural properties;
- document all reasoning with precise terminology and consistent mathematical notation. 

### 2.4 Expected Outcomes

By the end of the task, learners should be able to:

- define and use correctly the concepts of alphabet, string, language, empty string, and language closure;
- apply and interpret operations over strings and languages, including concatenation, union, intersection, complement, reversal, and Kleene closure;
- analyze and justify structural properties of languages, such as membership, finiteness, or infinitude;
- identify structural patterns in symbolic sequences and relate them to formal properties;
- abstract real-world musical artifacts as formal symbolic representations;
- analyze, at a conceptual level, the role of finite automata and regular expressions in justifying language properties;
- evaluate symbolic codifications and homomorphisms between different representations;
- produce mathematically rigorous answers and reports with clear definitions, examples, arguments, and conclusions.  

### 2.5 Acquisition Context

- Theoretical course in Computation Theory  
- Evaluative task focused on formal argumentation and abstract modeling. 

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

- Analytical and Critical Thinking  
  Abstraction of real-world domains into formal models and rigorous assessment of claims in light of definitions and theoretical properties.

- Written Communication  
  Production of clear, well-structured, mathematically rigorous texts with precise terminology and consistent notation.

- Epistemic Rigor  
  Explicit commitment to formal justification rather than informal intuition, and the ability to distinguish definitions, examples, arguments, and conclusions. 

## 4. Learning Objectives

### 4.1 General Learning Objective

The general objective of TASK25.00 is to enable the learner to abstract and model a real-world domain—songs and musical collections—as formal languages, using fundamental concepts of language theory, regular expressions, and recognizer models at a conceptual level, while also analyzing and justifying structural properties through formal definitions, operations over languages, and mathematically rigorous reasoning.

### 4.2 Specific Learning Objectives

#### LO1 — Formal Abstraction of the Domain
- LO1.1: define formally an alphabet (Σ) from the relevant musical symbols;
- LO1.2: model a song as a string over Σ;
- LO1.3: model a collection of songs as a language.

#### LO2 — Structural Analysis of Strings
- LO2.1: identify and define formally prefixes, suffixes, and substrings of a song;
- LO2.2: determine whether a song excerpt can be formally considered a valid song;
- LO2.3: justify the validity or invalidity of excerpts from the beginning, middle, or end of a song.

#### LO3 — Operations over Languages
- LO3.1: apply concatenation of strings to model song composition;
- LO3.2: analyze whether the result of concatenation belongs to the original language;
- LO3.3: apply union, intersection, and difference to combine collections;
- LO3.4: evaluate the complement of a language with respect to an explicitly defined universe.

#### LO4 — Kleene Closure and Language Cardinality
- LO4.1: apply Kleene closure to a musical language;
- LO4.2: interpret the role of the empty string and the empty language;
- LO4.3: classify languages as finite or infinite, with formal justification.

#### LO5 — Reversal and String Transformations
- LO5.1: define formally the reversal of strings;
- LO5.2: apply reversal to a song and analyze its structural validity;
- LO5.3: distinguish explicitly structural validity from semantic interpretation in reversal contexts.

#### LO6 — Regular Languages and Formal Expressiveness
- LO6.1: recognize when a collection of songs can be described by a regular language;
- LO6.2: specify musical languages through regular expressions;
- LO6.3: distinguish, at a conceptual level, regular and context-free languages, indicating expressive limits without requiring grammar construction.

#### LO7 — Automata and Model Equivalence (Conceptual Level)
- LO7.1: explain the theoretical equivalence between finite automata, regular expressions, and regular grammars;
- LO7.2: relate structural song patterns to conceptual states and transitions of an automaton as a justificatory instrument.

#### LO8 — Homomorphisms and Codifications
- LO8.1: define formally string homomorphisms;
- LO8.2: analyze whether score and recording can be treated as structurally equivalent codifications;
- LO8.3: justify the formal limits of interchangeability between symbolic representations.

#### LO9 — Formal Reasoning and Proof
- LO9.1: use formal definitions as the basis for the validity of answers;
- LO9.2: construct minimal examples to illustrate language properties;
- LO9.3: employ counterexamples to refute incorrect claims;
- LO9.4: apply inductive reasoning when appropriate.

#### LO10 — Technical and Epistemic Communication
- LO10.1: elaborate a technical report with logical structure, argumentative clarity, and appropriate terminology;
- LO10.2: present mathematically rigorous justifications;
- LO10.3: distinguish explicitly between informal intuition, illustrative example, and formal proof or argument.

## 5. Competency Set for TASK25.00

Based on the analysis of the task requirements, the following competencies were selected as directly aligned with TASK25.00.

### 5.1 Reused Competencies

Reuse refers to the existing competency identity and specification. The descriptions below justify its association with TASK25.00; they preserve the existing specification. The activation labels describe their use in this task.

#### C04 — Define Regular Expressions for Finite Automata

Justification for Reuse:  
Regular expressions constitute a relevant formal mechanism for the intensional specification of collections of songs in this task, especially when learners must characterize sets such as repeated songs, empty-song collections, or property-based subsets. In TASK25.00, this competency is activated at a conceptual and algebraic level, without requiring the operational construction of automata. It supports the learner’s ability to define regular languages formally and to relate them to structural descriptions of musical collections.

ActivationRole: `core`  
ActivationMode: `artifact-oriented`  
ActivationConstraint: `mandatory`

##### Specification and Scope

Knowledge–skill pairings: Finite State Machines — Analyze; Regular Expressions — Apply; Analytical and Critical Thinking (FPK) — Apply. Dispositions: Investigative, Collaborative, Responsible, Proactive, Creative.

C04 retains the correspondence between finite automata and regular expressions, including reasoning about equivalence. TASK25.00 activates that correspondence conceptually; the association does not introduce an automaton-construction or simulation deliverable. It also does not redefine C04 as unrestricted notation use, which is addressed by C23.

##### Summary Table for Competency C04

| Competency | Dispositions | Knowledge | Skill |
| --- | --- | --- | --- |
| Define Regular Expressions for Finite Automata | Investigative; Collaborative; Responsible; Proactive; Creative | Finite State Machines | Analyze |
|  |  | Regular Expressions | Apply |
|  |  | Analytical and Critical Thinking (FPK) | Apply |

#### C14 — Differentiate classifications of formal grammars

Justification for Reuse:  
This competency supports conceptual distinctions between regular languages and more expressive classes. In TASK25.00, it is useful when learners discuss expressive limits, delimit the scope of formal constructions, or justify why certain collections may or may not fall within the regular class. Since such reasoning enriches but does not structure every answer, the competency is activated as an extension.

ActivationRole: `extension`  
ActivationMode: `analytical`  
ActivationConstraint: `optional`

##### Specification and Scope

C14 distinguishes regular and context-free grammars and languages through their structural properties, expressiveness, and associated recognizers. It excludes operational model construction and interpretation of particular rule sets from this classificatory scope.

Knowledge–skill pairings: Regular Languages — Understand; Context-Free Languages — Understand; Analytical and Critical Thinking — Apply. Dispositions: Inventive, Collaborative, Responsible, Proactive. The analytical activation mode does not replace these component-level Bloom mappings.

##### Summary Table for Competency C14

| Competency | Dispositions | Knowledge | Skill |
| --- | --- | --- | --- |
| Differentiate classifications of formal grammars | Inventive; Collaborative; Responsible; Proactive | Regular Languages | Understand |
|  |  | Context-Free Languages | Understand |
|  |  | Analytical and Critical Thinking | Apply |

### 5.2 New Competencies Introduced in TASK25.00

Six competency identifiers originate in TASK25.00: C17, C18, C19, and C23 are independent specifications; C05.01 specializes C05; and C20 is a composite competency.

#### C05.01 — Write mathematically rigorous answers
Specialization of: C05 — *Write a Technical Report*

Justification for Introduction:  
The main evidence required in TASK25.00 is not merely a technical report, but a set of mathematically rigorous written answers. The task demands explicit definitions, precise notation, structured arguments, minimal examples, and counterexamples where appropriate. Since the generic writing competency C05 does not fully capture this justificatory and epistemic requirement, a new specialized competency is introduced.

##### Competency Title
Write mathematically rigorous answers

##### Textual Description
This competency involves the ability to produce mathematically rigorous written answers that clearly justify conclusions through explicit definitions, precise notation, structured arguments, and appropriate supporting examples.

Learners demonstrate this competency by:

- stating relevant formal definitions clearly;
- organizing answers so that claims, justifications, and conclusions are explicitly connected;
- using examples or counterexamples when they help clarify or validate the reasoning;
- applying appropriate technical and mathematical notation consistently;
- presenting arguments with sufficient rigor to support the correctness of the conclusion.

This competency specializes technical report writing toward tasks in which the main evidence lies not only in presenting a result, but in formally justifying why the result is valid.

##### Knowledge Specification
- Written Communication (FPK)
- Analytical and Critical Thinking (FPK)

##### Disposition Specification
- Meticulous
- Responsible

##### Knowledge–Skill Pairing
- Written Communication (FPK) — Apply  
  → write, structure, document, clarify formal reasoning.
- Analytical and Critical Thinking (FPK) — Analyze / Evaluate  
  → distinguish assumptions, assess validity, support conclusions, identify inconsistencies.

##### ActivationRole
`transversal`

##### ActivationMode
`justificatory`

##### ActivationConstraint
`mandatory`

##### Summary Table for Competency C05.01

| Competency | Dispositions | Knowledge | Skill |
| --- | --- | --- | --- |
| Write mathematically rigorous answers | Meticulous; Responsible | Written Communication (FPK) | Apply |
|  |  | Analytical and Critical Thinking (FPK) | Analyze / Evaluate |

#### C17 — Apply operations on formal languages

Origin: TASK25.00 — CSP Cycle 3.

##### Justification for Introduction

TASK25.00 requires sustained application and analysis of operations over strings and languages, including concatenation, union, intersection, complement, Kleene closure, and reversal. Although some of these actions might partially overlap with other competencies, the task demands a sufficiently central and explicit competency focused on formal operations and their structural consequences.

##### Competency Title

Apply operations on formal languages

##### Textual Description

This competency involves the ability to apply, analyze, and justify formal operations over languages, including concatenation, union, intersection, difference, complement, Kleene closure, and reversal, with attention to their structural effects and theoretical properties.

Learners demonstrate this competency by:

- applying operations to languages over an explicitly defined alphabet and specifying the universe for complement;
- assessing the structural validity of the resulting languages;
- determining whether relevant properties, including class membership, finiteness, or infinitude, are preserved;
- justifying conclusions through definitions, examples, counterexamples, and known theoretical properties.

The scope is conceptual and algebraic; it does not require automaton construction, simulation, or implementation.

##### Knowledge Specification

- Language Theory: alphabets, strings, languages, and finite and infinite languages.
- Operations on Formal Languages: concatenation, union, intersection, difference, complement, Kleene closure, reversal, and conceptual closure properties.
- Regular Expressions (conceptual): algebraic notation for describing and relating languages.
- Analytical and Critical Thinking (FPK): examination of arguments and justification of structural consequences.

##### Disposition Specification

- Epistemic Rigor
- Intellectual Responsibility
- Persistence

##### Knowledge–Skill Pairing

| Knowledge | Skill | Recorded performance |
| --- | --- | --- |
| Language Theory | Understand | Interpret and explain definitions and fundamental properties |
| Operations on Formal Languages | Apply / Analyze | Apply operations and analyze structural effects |
| Regular Expressions (conceptual) | Apply | Use algebraic notation to describe and relate languages |
| Analytical and Critical Thinking (FPK) | Analyze | Examine arguments, identify inconsistencies, justify conclusions |

##### ActivationRole

`core`

##### ActivationMode

`analytical`

##### ActivationConstraint

`mandatory`

##### Summary Table for Competency C17

| Competency | Dispositions | Knowledge | Skill |
| --- | --- | --- | --- |
| Apply operations on formal languages | Epistemic Rigor; Intellectual Responsibility; Persistence | Language Theory | Understand |
|  |  | Operations on Formal Languages | Apply / Analyze |
|  |  | Regular Expressions (conceptual) | Apply |
|  |  | Analytical and Critical Thinking (FPK) | Analyze |

#### C18 — Model real-world problems using formal language concepts

Origin: TASK25.00 — CSP Cycle 3.

##### Justification for Introduction

C18 was created for TASK25.00 to make formal domain abstraction explicit and distinguish it from operations under C17 and transformations under C19. TASK25.00 fundamentally requires learners to abstract musical artifacts as symbols, strings, and languages. This competency directly supports the formal modeling of the domain, including the explicit definition of alphabets, strings, collections, and representation constraints. It is one of the central competencies of the task.

##### Competency Title

Model real-world problems using formal language concepts

##### Textual Description

This competency involves the ability to abstract elements of a real-world domain and model them as formal language-based representations through explicit alphabets, strings, and languages that capture relevant structural features.

Learners demonstrate this competency by:

- establishing explicit mappings between domain entities and formal symbols;
- defining alphabets, strings, and languages appropriate to the selected representation;
- justifying modeling choices, including exclusions and simplifications;
- assessing the structural adequacy of the model and identifying its formal limitations;
- distinguishing structural correctness from semantic interpretation.

The scope is abstraction and modeling. Operations on the resulting languages are addressed by C17, and transformations between representations by C19. Conceptual mapping supports the initial abstraction without subsuming the separate analysis of homomorphisms.

##### Knowledge Specification

- Language Theory: alphabets, strings, languages, and foundations of formal abstraction.
- Formal Languages: collections as sets of strings and structural properties independent of interpretation.
- Homomorphisms and Codifications (conceptual): mappings between representations and preservation or loss of information as a limit of modeling.
- Analytical and Critical Thinking (FPK): assessment of modeling choices, structural adequacy, and limitations.

##### Disposition Specification

- Epistemic Rigor
- Intellectual Responsibility
- Reflectiveness

##### Knowledge–Skill Pairing

| Knowledge | Skill | Recorded performance |
| --- | --- | --- |
| Language Theory | Understand | Interpret and explain the relation between a domain and its formal representation |
| Formal Languages | Apply | Model through alphabets, strings, and languages |
| Homomorphisms and Codifications (conceptual) | Apply | Map domain entities to symbols |
| Analytical and Critical Thinking (FPK) | Analyze | Assess structural adequacy, justify choices, identify limitations |

##### ActivationRole

`core`

##### ActivationMode

`constructive`

##### ActivationConstraint

`mandatory`

##### Summary Table for Competency C18

| Competency | Dispositions | Knowledge | Skill |
| --- | --- | --- | --- |
| Model real-world problems using formal language concepts | Epistemic Rigor; Intellectual Responsibility; Reflectiveness | Language Theory | Understand |
|  |  | Formal Languages | Apply |
|  |  | Homomorphisms and Codifications (conceptual) | Apply |
|  |  | Analytical and Critical Thinking (FPK) | Analyze |

#### C19 — Apply homomorphisms in formal languages

Origin: TASK25.00 — CSP Cycle 3.

##### Justification for Introduction

C19 was created for TASK25.00 to specify the analysis of formal mappings and the limits of equivalence between representations. The task explicitly asks whether a musical score and its corresponding recording may be treated as codifications of one another. This requires reasoning about homomorphisms, symbolic mappings, and representational equivalence. C19 therefore supports the analysis of preserved structure and the formal limits of interchangeability between representations.

##### Competency Title

Apply homomorphisms in formal languages

##### Textual Description

This competency involves the ability to define and apply homomorphisms over symbols, strings, and languages, using formal encodings to relate symbolic representations of the same domain or different domains.

Learners demonstrate this competency by:

- defining mappings on symbols and applying their extensions to strings and languages;
- identifying which structural properties are preserved, modified, or lost;
- analyzing the conditions under which representations can be related by a formal encoding;
- justifying the limits of equivalence while distinguishing structural correspondence from semantic equivalence.

The scope is conceptual and interpretative, without implementation of encoding functions. The task's declared correspondence between a score and its recording motivates the analysis; it does not by itself prove a homomorphism or structural equivalence. Initial domain modeling is addressed by C18 and language operations by C17.

##### Knowledge Specification

- Formal Languages: alphabets, strings, languages, and relevant structural properties.
- Homomorphisms: definition on symbols, extension to strings and languages, and preservation or transformation of properties.
- Codifications: formal mappings and conditions of equivalence and non-equivalence between representations.
- Analytical and Critical Thinking (FPK): analysis of preserved properties and justification of encoding limits.

##### Disposition Specification

- Epistemic Rigor
- Intellectual Responsibility
- Reflectiveness

##### Knowledge–Skill Pairing

| Knowledge | Skill | Recorded performance |
| --- | --- | --- |
| Formal Languages | Understand | Interpret language structure and properties |
| Homomorphisms | Apply | Define and apply homomorphisms to symbols, strings, and languages |
| Codifications | Apply | Map and translate symbolic representations |
| Analytical and Critical Thinking (FPK) | Analyze | Examine preserved properties and justify equivalence limits |

##### ActivationRole

`supporting`

##### ActivationMode

`interpretative`

##### ActivationConstraint

`mandatory`

##### Summary Table for Competency C19

| Competency | Dispositions | Knowledge | Skill |
| --- | --- | --- | --- |
| Apply homomorphisms in formal languages | Epistemic Rigor; Intellectual Responsibility; Reflectiveness | Formal Languages | Understand |
|  |  | Homomorphisms | Apply |
|  |  | Codifications | Apply |
|  |  | Analytical and Critical Thinking (FPK) | Analyze |

#### C20 — Model and analyze musical collections as formal languages

Justification for Introduction:  
TASK25.00 requires an integrated performance that cannot be reduced to any single atomic competency. Learners must model the domain, apply formal operations, reason about codifications, specify some collections through regular expressions, and justify all conclusions rigorously. A task-level composite competency is therefore introduced to represent this integrative performance.

##### Competency Title
Model and analyze musical collections as formal languages

##### Textual Description
This task-level competency involves the ability to integrate concepts, operations, and representations from Formal Language Theory in order to model musical collections as formal languages and analyze rigorously their structural properties.

Learners demonstrate this competency by:

- abstracting musical artifacts as symbols, strings, and languages;
- applying algebraic operations and regular expressions to characterize musical collections;
- analyzing formal codifications and transformations between representations;
- justifying structural properties, limitations, and implications through explicit definitions, minimal examples, counterexamples, and logical argumentation.

This competency synthesizes the component competencies specified for this task into a coherent formal analysis of a real-world problem, without requiring implementation or operational recognizer construction.

##### Competency Composition
C20 is composed of:
- C18 — Model real-world problems using formal language concepts
- C17 — Apply operations on formal languages
- C19 — Apply homomorphisms in formal languages
- C04 — Define Regular Expressions for Finite Automata
- C23 — Interpret and apply algebraic notation for strings and languages
- C05.01 — Write mathematically rigorous answers

##### ActivationRole
`core`

##### ActivationMode
`integrative`

##### ActivationConstraint
`mandatory`

##### Integrated Knowledge and Expected Evidence

C20 integrates the component competencies without replacing them or adding isolated knowledge content. Its evidence is the coherence of the complete, mathematically justified response: the alphabet and modeling assumptions, operations, encodings, notation, and conclusions must remain mutually consistent. This is the expected form of evidence, not a claim about learner work already collected.

The following knowledge–skill pairings describe the integrated performance.

| Integrated knowledge | Skill | Recorded performance |
| --- | --- | --- |
| Language Theory | Understand | Interpret fundamental formal-modeling concepts |
| Formal Languages | Apply | Model collections and apply operations |
| Regular Expressions | Apply | Specify languages algebraically |
| Homomorphisms and Codifications | Apply | Relate symbolic representations |
| Analytical and Critical Thinking (FPK) | Analyze | Integrate, evaluate, and justify formal models |
| Technical Written Communication (FPK) | Create | Produce coherent, rigorous documentation |

Dispositions: Epistemic Rigor, Intellectual Responsibility, Reflectiveness, Persistence. These remain distinct from the dispositions and mappings of C05.01 and C23; composition does not replace their individual specifications.

| Component | Contribution to the integrated performance |
| --- | --- |
| C18 | Formal abstraction and explicit modeling choices |
| C17 | Operations and their structural consequences |
| C19 | Encoding analysis and limits of equivalence |
| C04 | Regular-expression descriptions and conceptual representational correspondence |
| C23 | Consistent algebraic notation |
| C05.01 | Rigorous written justifications |

##### Summary Table for Competency C20

| Competency | Dispositions | Knowledge | Skill |
| --- | --- | --- | --- |
| Model and analyze musical collections as formal languages | Epistemic Rigor; Intellectual Responsibility; Reflectiveness; Persistence | Language Theory | Understand |
|  |  | Formal Languages | Apply |
|  |  | Regular Expressions | Apply |
|  |  | Homomorphisms and Codifications | Apply |
|  |  | Analytical and Critical Thinking (FPK) | Analyze |
|  |  | Technical Written Communication (FPK) | Create |

#### C23 — Interpret and apply algebraic notation for strings and languages

Justification for Introduction:  
TASK25.00 requires a transversal competence in the interpretation and use of algebraic notation for strings and languages, including symbols such as ε, Σ, concatenation, exponentiation, reversal, substructures, set-theoretic language operations, and closure notation. This need is distinct from the interpretation of rule-based notation or grammar-based rules, and therefore should not be treated as a specialization of C13 or C13.01. A new independent competency is introduced to preserve the distinction between algebraic notation and grammar-rule interpretation.

##### Competency Title
Interpret and apply algebraic notation for strings and languages

##### Textual Description
This competency involves the ability to interpret, use, and justify formal algebraic notation for strings and languages in order to represent, analyze, and communicate structural properties of symbolic systems.

Learners demonstrate this competency by:

- interpreting standard notation for strings, such as ε, Σ, |x|, concatenation, exponentiation, reversal, prefixes, suffixes, and substrings;
- interpreting and applying standard notation for languages, such as union, intersection, complement, concatenation, \(L^n\), and \(L^*\);
- using algebraic notation consistently to express structural properties, operations, and relations over strings and languages;
- connecting formal notation to conceptual reasoning about symbolic structures and language behavior;
- justifying the meaning and use of notation in formally rigorous answers.

This competency supports instructional contexts in which learners must reason explicitly through symbolic notation, not merely recognize concepts informally.

##### Knowledge Specification
- Language Theory
- Formal Languages
- Written Communication (FPK)
- Analytical and Critical Thinking (FPK)

##### Disposition Specification
- Meticulous
- Responsible

##### Knowledge–Skill Pairing
- Language Theory — Understand  
  → interpret, explain, identify formal notation for strings and symbolic structures.
- Formal Languages — Apply  
  → use, express, derive, manipulate notation for operations over languages.
- Written Communication (FPK) — Apply  
  → write, structure, clarify formal symbolic expressions in technically correct form.
- Analytical and Critical Thinking (FPK) — Analyze  
  → justify, distinguish, relate, validate symbolic interpretations.

##### ActivationRole
`transversal`

##### ActivationMode
`analytical`

##### ActivationConstraint
`mandatory`

##### Summary Table for Competency C23

| Competency | Dispositions | Knowledge | Skill |
| --- | --- | --- | --- |
| Interpret and apply algebraic notation for strings and languages | Meticulous; Responsible | Language Theory | Understand |
|  |  | Formal Languages | Apply |
|  |  | Written Communication (FPK) | Apply |
|  |  | Analytical and Critical Thinking (FPK) | Analyze |

## 6. Competency Activation Summary

| Competency | ActivationRole | ActivationMode | ActivationConstraint |
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

Subobjective identifiers refer to the explicitly numbered bullets in Section 4.2. The table records the associations between subobjectives and competencies. C20 integrates the six components listed in its specification and is not inserted as an additional atomic mapping in every row. LO6.3 describes the extension associated with optional C14. Its inclusion in the objective mapping does not make this extension mandatory.

| LO | Competencies Mobilized |
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

## 8. Contribution to OntoKSD Requirements

### 8.1 Change in instructional emphasis

Cycle 1 tasks primarily involved modeling the behavior of vending machines, traffic-control systems, and robots through finite-state, pushdown, or Turing-machine models, with simulation and technical documentation. Task201–Task203 continued this emphasis through drone monitoring, team control, and parking control. Task204 already emphasized conceptual reasoning about computational limits, supported by modeling and reporting.

TASK25.00 extends the conceptual emphasis by making formal abstraction, algebraic operations, symbolic transformations, and mathematical justification the principal performance. No executable machine model or simulation is required. The difference lies in the expected performance and evidence within the same Theory of Computation discipline.

This change helps explain why two existing competencies are reused and six identifiers are introduced. Reuse remains a design objective, while the expanded specification makes explicit performances that the available task associations did not adequately distinguish. The number of introduced competencies does not itself measure the number of new ontology requirements.

### 8.2 Representational needs made explicit

| Competency | Contribution to the task specification | Implication for OntoKSD |
| --- | --- | --- |
| C17 | Operations and analysis of structural consequences | Represent conceptual and algebraic performance, with component-level cognitive mappings and evidence that need not be executable |
| C18 | Abstraction separated from operations and recognizer construction | Distinguish identities by expected performance and scope even when they share knowledge components |
| C19 | Transformations, preserved properties, and limits of equivalence | Relate evidence to the particular transformation or equivalence claim it supports; distinguish this performance from initial modeling |
| C05.01 | Mathematical justification as a specialization of technical writing | Preserve the base relation and specify the narrower performance and expected evidence |
| C23 | Algebraic notation distinguished from grammar-rule interpretation | Support an independent identity when scope differs, without inferring specialization from similar vocabulary |
| C20 | Coherent integration of six components | Represent composition while preserving component identities and distinguishing integrated evidence from evidence of individual performances |

These implications strengthen the empirical basis for competence identity, knowledge–skill pairing, specialization, composition, contextual activation, and evidence traceability. Specialization and contextual qualification already appeared in earlier cycles. TASK25.00 gives these requirements further concrete applications and provides an explicit composite specification through C20. Establishing whether any implication requires a new ontology construct requires comparison with the corresponding ontology version; the creation of an identifier alone does not establish a structural extension.

### 8.3 Expected evidence and its interpretation

The written answers can contain evidence for several competencies. Their relevance depends on the performance expressed, rather than on the document type alone. The following reading summarizes the existing specifications and adds no separate deliverable or scoring procedure.

| Competency | Expected evidence within the answers |
| --- | --- |
| C17 | Formally expressed operations and justified conclusions about their structural effects |
| C18 | Explicit alphabet, strings, languages, modeling choices, and limitations |
| C19 | Defined mappings and arguments concerning preserved properties and equivalence limits |
| C04 | Regular-expression descriptions and conceptual reasoning about the represented languages |
| C23 | Consistent interpretation and use of notation for strings and languages |
| C05.01 | Explicit connections among definitions, assumptions, claims, arguments, and conclusions |
| C14 | Comparison of regular and context-free formalisms when the optional extension is addressed |
| C20 | Coherence among the modeling choices, operations, transformations, notation, and justifications across the complete response |

A shared written response may support several claims, but its existence alone does not demonstrate every component. C20 concerns their integration; it neither replaces the components nor duplicates their task associations. The statements above describe expected evidence, not learner results already assessed.

## 9. Interactive Review Decisions and Consolidated Specification

### 9.1 Issues, rationale, and resulting decisions

The table consolidates the substantive issues and decisions underlying the specification. The issue wording organizes the rationale; it is not a transcript, a newly conducted review, or evidence of additional review rounds.

| Issue considered | Rationale and decision | Result in this report |
| --- | --- | --- |
| Which existing competencies fit the task? | Reuse C04 for conceptual regular-expression performance and C14 for an optional classificatory extension | Reuse justifications in Section 5.1 and activation labels in Section 6 |
| Should operations, modeling, and transformations share one identity? | Distinguish their expected performances despite overlapping knowledge; introduce C17, C18, and C19 for this task | Separate specifications in Section 5.2 and distinct LO associations in Section 7 |
| Does application require implementation? | Retain conceptual and algebraic application, analysis, and justification without requiring an executable model | Scope statements for C17–C19; component-level Bloom mappings preserved |
| Does general technical writing express the required rigor? | Specialize C05 as C05.01 to make mathematically justified answers explicit | C05.01 specification and its transversal, justificatory activation |
| Is algebraic notation a form of grammar-rule interpretation? | Preserve the semantic distinction by introducing independent C23 | C23 specification; no specialization link to C13 or C13.01 |
| How is the complete performance represented? | Introduce composite C20 to express coherent integration without replacing the components or adding isolated knowledge | Six-component composition and integrated knowledge–skill pairings in Section 5.2 |
| Must grammar-class comparison be mandatory? | Retain C14 as an optional extension and interpret LO6.3 accordingly | Sections 6 and 7 preserve the optional association |

Creation identifies where a competency originates; reuse identifies an association with a competency originating elsewhere. C17, C18, C19, C23, C05.01, and C20 originate in TASK25.00. Their refinement does not change that origin. C04 and C14 remain reused specifications.

### 9.2 Consistency of the consolidated record

The consolidated specification contains eight task-associated identifiers, with one activation entry per identifier. The 31 subobjectives in Section 4.2 have corresponding entries in Section 7, and all referenced competency identifiers belong to the specified set. C20 is represented through its six component links and integrated performance rather than repeated as an atomic association for each objective. C05 is the specialization base of C05.01 and is not an additional task target.

The specification distinguishes the conceptual use of C04 from an operational automaton-construction requirement, and the interpretative use of C19 from its Apply-level component pairings. Activation mode and Bloom level describe different aspects of performance. The optional status of C14 is preserved, including the corresponding extension objective.

### 9.3 Scope of the integrated record

This document combines the task analysis, competency specifications, interactive-review rationale, and resulting decisions. It therefore provides an integrated specification-and-review record without requiring separate reports for the work described here. Its completeness concerns the consolidated content, not a full history of every discussion. It does not establish independent evaluation, individual reviewer agreement, or formal approval beyond the collaborative process stated in Section 1.2.

## 10. Final Competency Summary and Conclusion

TASK25.00 combines two reused competencies, C04 and C14, with six competency identifiers created for this task: C17, C18, C19, C23, C05.01, and C20. The distinction below records identity-level decisions; it is not a count of independent learner performances.

### 10.1 Task Competencies

| ID | Competency title | Creation / reuse and relation | Role | Mode | Constraint |
| --- | --- | --- | --- | --- | --- |
| C04 | Define Regular Expressions for Finite Automata | Reused | core | artifact-oriented | mandatory |
| C14 | Differentiate classifications of formal grammars | Reused | extension | analytical | optional |
| C05.01 | Write mathematically rigorous answers | Created; specialization of C05 | transversal | justificatory | mandatory |
| C17 | Apply operations on formal languages | Created; independent | core | analytical | mandatory |
| C18 | Model real-world problems using formal language concepts | Created; independent | core | constructive | mandatory |
| C19 | Apply homomorphisms in formal languages | Created; independent | supporting | interpretative | mandatory |
| C20 | Model and analyze musical collections as formal languages | Created; composite | core | integrative | mandatory |
| C23 | Interpret and apply algebraic notation for strings and languages | Created; independent | transversal | analytical | mandatory |

### 10.2 Knowledge, Skills, and Dispositions

The following table consolidates the specified components. Each knowledge item retains its associated cognitive level; activation modes in the preceding table do not replace these mappings. For C20, the entries describe integrated performance rather than additional isolated knowledge requirements.

| ID | Dispositions | Knowledge–skill pairings |
| --- | --- | --- |
| C04 | Investigative; Collaborative; Responsible; Proactive; Creative | Finite State Machines — Analyze; Regular Expressions — Apply; Analytical and Critical Thinking (FPK) — Apply |
| C14 | Inventive; Collaborative; Responsible; Proactive | Regular Languages — Understand; Context-Free Languages — Understand; Analytical and Critical Thinking — Apply |
| C05.01 | Meticulous; Responsible | Written Communication (FPK) — Apply; Analytical and Critical Thinking (FPK) — Analyze / Evaluate |
| C17 | Epistemic Rigor; Intellectual Responsibility; Persistence | Language Theory — Understand; Operations on Formal Languages — Apply / Analyze; Regular Expressions (conceptual) — Apply; Analytical and Critical Thinking (FPK) — Analyze |
| C18 | Epistemic Rigor; Intellectual Responsibility; Reflectiveness | Language Theory — Understand; Formal Languages — Apply; Homomorphisms and Codifications (conceptual) — Apply; Analytical and Critical Thinking (FPK) — Analyze |
| C19 | Epistemic Rigor; Intellectual Responsibility; Reflectiveness | Formal Languages — Understand; Homomorphisms — Apply; Codifications — Apply; Analytical and Critical Thinking (FPK) — Analyze |
| C20 | Epistemic Rigor; Intellectual Responsibility; Reflectiveness; Persistence | Language Theory — Understand; Formal Languages — Apply; Regular Expressions — Apply; Homomorphisms and Codifications — Apply; Analytical and Critical Thinking (FPK) — Analyze; Technical Written Communication (FPK) — Create |
| C23 | Meticulous; Responsible | Language Theory — Understand; Formal Languages — Apply; Written Communication (FPK) — Apply; Analytical and Critical Thinking (FPK) — Analyze |

C20 integrates C18, C17, C19, C04, C23, and C05.01. C14 remains an optional extension outside that composition. The complete descriptions and action verbs are retained in Section 5.

### 10.3 Conclusion

There are eight task-associated identifiers, including the composite C20, and seven non-composite entries. C05 is preserved as the base of C05.01 and is not added as a separate task target. C20's six composition links are relations between competencies, not six further task associations. Composition does not establish independent assessment evidence for each component.

The resulting specification illustrates the cycle's intended approach: design an instructional task around opportunities for reuse, qualify the contextual use of existing competencies, and retain justified additions when the required performance calls for them. C05.01 captures mathematical justification, C23 distinguishes algebraic notation from grammar-rule interpretation, C17 makes formal operations explicit, C18 specifies domain abstraction, C19 specifies homomorphism and encoding analysis, and C20 records the integrated task performance.

This report consolidates the specification and interactive review of TASK25.00 in one document. It preserves the distinction between language operations, formal abstraction, representational transformations, notation, justification, and integrated performance. The specification identifies expected performance and evidence without asserting a separate review event or observed learning outcomes.
