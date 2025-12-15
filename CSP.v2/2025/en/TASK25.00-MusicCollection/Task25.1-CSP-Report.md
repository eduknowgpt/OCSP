# Competency Specification Report: Task25.1 - Music Collection


## Introduction

Building upon the foundational **CSP methodology**, this report presents the application of the **Competency Authoring phase** in **Task25.1 – Music Collection**, a **Problem-Based Learning (PBL)** scenario that explores the use of **finite automata and regular expressions**.
Students are required to produce a report containing **clear, coherent, and rigorous answers**, including **formal definitions, minimal examples, proofs (including induction and closure properties)**, and **counterexamples** when appropriate.



## 1. Instructional Entity Analysis

### Title

* Music Collection

### Description

* Learners must analyze musical scores, represent them as sequences of symbols, and perform operations on these representations.

### Solution Development Process

Expected learner approach:

* **Analyze problem constraints:**

  * Scores may involve one or multiple instruments.
  * Each piece of music may contain an arbitrary number of symbols.
  * Each piece belongs to a musical genre.

* **Model the scores** as **finite automata** (states, transitions, actions).

* **Identify the genre** of each piece of music.

* **Document and report** design decisions and formal representations with **mathematical rigor**.


### Expected Outcomes

Upon completion of this task, learners will be able to:

> Formally define and use the notions of alphabet, string, language, empty language, and language closure within a precise mathematical framework.

> Apply algebraic operations on strings and languages, including concatenation, union, intersection, complement, reversal, and Kleene closure, interpreting their effects in concrete problem settings.

> Analyze and justify properties of languages, such as finiteness or infiniteness, using formal arguments and counterexamples when appropriate.

> Identify structural patterns in symbolic sequences and reason about language properties induced by real-world constraints.

> Model real-world musical artifacts (scores, recordings, genres) as formal languages through suitable symbol encodings and homomorphisms.

> Construct and analyze finite automata to recognize languages defined by musical structures or classification criteria.

> Simulate automata and language operations to validate recognition and classification results.

> Produce a mathematically rigorous technical report that clearly articulates definitions, examples, proofs, and formal reasoning, adhering to standards of precision and coherence.


### Acquisition Context

* Theoretical course on **Theory of Computation**
* **Assessment tasks** conducted as part of course evaluation


### Target Audience Profile

- Academic Level: 2nd–3rd year undergraduate CS students.

- Domain Experience: Solid grounding in data structures, and basic automata.

- Roles: Design FSMs; document technical decisions.


### Proficiency Scale

- Escala com notas entre 0 e 100 (representando notas como 8.5 no modelo de avaliação da disciplina, por exemplo, que corresponde a 85 na escala).



## 2. Knowledge Enumeration

To ensure systematic and semantically consistent knowledge modeling, this enumeration adopts the **ACM CS2023 Body of Knowledge** as a controlled vocabulary for disciplinary computing knowledge, and the **ACM Computing Curricula 2020 (CC2020)** for Foundational and Professional Knowledge (FPK).
Together, these elements constitute the Knowledge (K) dimension of the OntoKSD model for the task Music Collection.

The following knowledge components were identified based on the formal modeling, mathematical reasoning, and language-theoretic analysis required by the task.

### Computing Knowledge (CS2023-Aligned)

- Formal Languages
  - Alphabets, strings, languages, and the empty language.
  - Finite and infinite languages.
  - Substrings, prefixes, and suffixes of strings.

- Operations on Languages
  - Union, intersection, and complement.
  - Concatenation and Kleene closure.
  - Reversal of strings and languages.
  - Closure properties of language classes.

- Regular Languages
  - Regular expressions and their formal semantics.
  - Equivalence between regular expressions and finite automata.

- Finite Automata
  - Deterministic and nondeterministic finite automata (DFA/NFA).
  - Language recognition and automata equivalence.
  - Expressive power and limitations of finite automata.

- Homomorphisms and Encodings
  - Formal mappings between symbolic representations.
  - Preservation of language properties under homomorphisms.
  - Limits of representational equivalence (e.g., musical scores vs. recordings).

- Formal Reasoning and Proof Techniques
  - Use of precise definitions and minimal examples.
  - Construction of formal arguments and counterexamples.
  - Justification of language properties and operations.


### Professional Knowledge (CC2020 FPK-Aligned)

- Analytical and Critical Thinking
  - Abstraction of real-world domains into formal models.
  - Rigorous evaluation of claims using formal reasoning.

- Technical Written Communication
  - Production of clear, structured, and mathematically precise texts.
  - Proper use of formal notation and terminology from Language Theory.

- Epistemic Rigor
  - Commitment to formal justification over intuitive reasoning.
  - Clear distinction between definitions, examples, general properties, and exceptions.




## 3. Learning Objectives Identification

Learners will be able to:


1. **Define and formalize Regular Expressions representing simple musical languages**  

2. **Interpret and apply algebraic notation to string representations**  
   - Use symbolic and algebraic operations to construct and manipulate strings derived from musical scores.  
   - Represent musical compositions as sequences within a defined alphabet.  
  
3. **Differentiate and classify formal grammars**  
   - Compare regular and context-free grammars based on their expressive capabilities.  

4. **Identify and model patterns using Finite State Machines (FSMs)**  
   - Construct deterministic automata that recognize patterns corresponding to musical genres or structures.  
   - Explain transitions, states, and acceptance criteria with formal notation.  

5. **Apply and justify operations on formal languages**  
   - Perform operations such as union, concatenation, intersection, complement, and Kleene star.  
   - Provide mathematical justification (proof or counterexample) for each operation’s validity in context.  

6. **Recognize and apply homomorphisms and encodings**  
   - Map elements from the musical domain (notes, instruments, genres) to symbolic representations in formal languages.  
   - Demonstrate equivalence or transformation between different representations (e.g., score ↔ MP3).  

7. **Simulate and validate automata behavior**  
   - Use computational tools to verify the recognition of musical genres and operations on strings.  
   - Interpret simulation results and explain discrepancies or limitations.  

8. **Produce a technical report with mathematical rigor**  
   - Document all modeling decisions, proofs, and results with clarity and coherence.  
   - Include formal definitions, minimal examples, induction proofs, closure properties, and counterexamples when appropriate.  
   *(Bloom: Create)*  





## 4. Competency Definition

Competencies are specified based on the **Learning Objectives (LOs)** identified in the task analysis.

### 4.1 Competency CT25.1-1 Specification  

  * **Code:** CT25.1.1  
  * **Source Task:** Task25.1 – Music Collection  
  * **Derived from:** Learning Objective 1 – Define and formalize Regular Expressions representing simple musical languages  


### Competency Title  
    Apply Regular Expressions to Define and Formalize Simple Musical Languages


### Textual Description  

This competency involves the ability to **define, formalize, and apply regular expressions** to represent **symbolic musical structures** (such as melodies or rhythmic sequences) as **formal languages**.  

Learners must demonstrate the capacity to:
- **Translate** musical elements (notes, patterns, and repetitions) into symbolic alphabets.  
- **Compose** and **compare** regular expressions that describe these musical patterns.  
- **Differentiate** between valid and invalid representations based on formal syntax and semantics.  



### Knowledge Specification
The following knowledge areas are critical for this competency:  

* Language Theory
  * Concepts of symbols, strings, alphabets, and operations in formal languages. 

* Regular Expressions 
  * Syntax, semantics, and algebraic properties of regular expressions.

* Pattern Matching
  * Construction and manipulation of symbolic patterns in string sets. 
  
* Analytical and Critical Thinking (FPK)
  * Ability to reason about correctness, completeness, and consistency of formal models. 



### Disposition Specification

- Creativity – generating expressive and elegant regular expressions to capture complex musical forms.  
- Persistence – engaging in iterative refinement of formal definitions until they satisfy correctness conditions.  
- Responsibility and collaboration – validating formalizations collaboratively and documenting reasoning transparently.  


 
### Knowledge-Skill Pairing and Bloom’s Taxonomy Alignment

To provide clarity on competency expectations, additional action verbs from Bloom’s Revised Taxonomy are used to specify the intended cognitive processes and observable learner behaviors.

* **Regular Expressions - Create** 
  * *Design, Construct, Compose, Generate, Formalize*
  * Design and construct regular expressions that model symbolic musical sequences; generate new expressions to represent variations in rhythm, melody, or repetition.

* **Language Theory - Understand** 
  * *Explain, Describe, Interpret, Summarize, Illustrate* 
  *  Explain how formal symbols and strings represent musical notes, instruments, and temporal patterns in a defined alphabet. 

* **Pattern Matching - Apply** 
  * *Use, Implement, Manipulate, Operate, Demonstrate* 
  *Apply pattern-matching techniques to manipulate symbolic sequences and test recognition of musical structures.

* **Analytical and Critical Thinking (FPK) -  Analyze / Evaluate** 
  * *Verify, Differentiate, Compare, Justify, Assess* 
  *  Verify correctness and equivalence between musical representations and their corresponding formal models; justify reasoning through logical arguments and minimal examples.


 
### Summary Table for Competency CT25.1.1

| **Code**  | **Competency** | **Dispositions** | **Knowledge** | **Skill** |
|-----------|----------------|------------------|---------------|-----------|
|           |                |                  | Regular Expressions | **Create (Design, Construct, Compose, Generate, Formalize)** |
| CT25.1.1  | **Apply Regular Expressions to Define and Formalize Simple Musical Languages** | Collaborative, Responsible, Creative | Language theory | **Understand (Explain, Describe, Interpret, Summarize, Illustrate)**
|          | | | Pattern Matching | **Apply (Use, Implement, Manipulate, Operate, Demonstrate)** |
|          | | | Analytical and Critical Thinking (FPK) | **Apply (Verify, Differentiate, Compare, Justify, Assess)** |



### 4.2 Competency CT25.1-2 Specification  

**Code:** CT25.1.2  
**Source Task:** Task25.1 – Music Collection  
**Derived from:** Learning Objective 2 – Interpret and apply algebraic notation to string representations  


### Competency Title  
    Interpret and Apply Algebraic Notation to Represent Musical Strings

### Textual Description  

This competency involves the ability to **interpret and apply algebraic notation** to represent **musical compositions as symbolic strings** within a defined alphabet.  
Learners must demonstrate the capacity to:
- **Use** algebraic operators to construct and manipulate symbolic representations of musical phrases and sequences.  
- **Represent** musical compositions as ordered strings composed of defined symbols (notes, chords, rests, durations).  
- **Analyze** the structure of these strings to identify regularities, repetitions, or hierarchical relations.  
- **Apply** formal operations (concatenation, repetition, substitution) to transform or generate musical sequences. 



### Knowledge Specification  

#### Computing Knowledge
- **Algebraic Notation for Strings:** symbolic representation and manipulation of string patterns.  
- **Language Theory:** formal concepts of alphabets, concatenation, and closure operations.  
- **String Operations:** concatenation, repetition, reversal, and substitution within defined alphabets.  

#### Professional Knowledge (FPK)
- **Analytical and Critical Thinking:** evaluate and justify the correctness of algebraic manipulations.  


### Disposition Specification  

- **Precision** – maintaining syntactic and semantic accuracy in symbolic representations.  
- **Creativity** – exploring multiple equivalent formulations for the same musical structure.  
- **Persistence** – refining symbolic models until they reflect the musical intent accurately.  



### Knowledge–Skill Pairing and Bloom’s Taxonomy Alignment  

* **Algebraic Notation for Strings** - **Apply** 
  * *Use, Manipulate, Implement*
  * Apply algebraic notation to construct and manipulate symbolic strings representing musical sequences. 
  
* **Language Theory** - **Understand** 
  * *Interpret, Explain, Distinguish, Relate*
  * Interpret the relationship between musical elements and their formal symbolic counterparts within an alphabet.

 |
* **String Operations** - **Apply** 
  * *Combine, Modify, Transform*
  * Perform and justify algebraic operations (concatenation, repetition, substitution) on symbolic musical strings.


* **Analytical and Critical Thinking (FPK)** - **Apply** 
  * *Verify, Compare, Justify*
  * Verify correctness and logical soundness of algebraic operations applied to musical structures.


### Summary Table for Competency CT25.1.2  

| **Code** | **Competency** | **Dispositions** | **Knowledge** | **Skill (Bloom)** |
|-----------|----------------|------------------|----------------|------------------|
| CT25.1.2 | **Interpret and Apply Algebraic Notation to Represent Musical Strings** | Precise, Creative, Persistent | Algebraic Notation for Strings | **Apply (Use, Manipulate, Implement)** |
|   |   |   | Language Theory | **Understand  (Interpret, Explain, Distinguish, Relate)** |
|   |   |   | String Operations | **Apply  (Combine, Modify, Transform)** |
|   |   |   | Analytical & Critical Thinking (FPK) | **Analyze / Evaluate (Verify, Compare, Justify)** |





### 4.3 Competency CT25.1-3 Specification  

**Code:** CT25.1.3  
**Source Task:** Task25.1 – Music Collection  
**Derived from:** Learning Objective 3 – Differentiate and classify formal grammars  


### Competency Title  
    Differentiate and Classify Formal Grammars


### Textual Description  

This competency involves the ability to **differentiate and classify formal grammars** based on their **syntactic structure and expressive capabilities**, particularly distinguishing **regular** from **context-free grammars** within the hierarchy of formal languages.  

Learners must demonstrate the capacity to:  
- **Compare** the expressive power and limitations of different classes of grammars.  
- **Identify** the structural properties that distinguish regular and context-free grammars.  
- **Classify** examples of grammars according to their production rules and generative capabilities.  
- **Explain** how these classifications relate to automata models and language recognition.  



### Knowledge Specification  

#### Computing Knowledge
- **Formal Grammars:** definitions, components (terminals, non-terminals, production rules), and derivation processes.  
- **Chomsky Hierarchy:** classification of grammars and languages (Type 0–Type 3).  
- **Regular Grammars:** properties, forms, and equivalence with finite automata.  
- **Context-Free Grammars (CFGs):** generative power and relation to pushdown automata.  
- **Language Theory:** interrelations among grammar classes, automata, and formal language recognition.  

#### Professional Knowledge
- **Analytical and Critical Thinking (FPK):** evaluate the expressive scope and structural distinctions among formal grammars.  



### Disposition Specification  

- **Analytical** – maintaining precision in the classification and comparison of grammar types.  
- **Clarity** – expressing reasoning and distinctions using accurate formal notation.  
- **Persistence** – analyzing examples and counterexamples until classification is correctly justified.  
- **Critical** – evaluating the expressive adequacy of grammar forms for specific language classes.  



### Knowledge–Skill Pairing and Bloom’s Taxonomy Alignment  

To provide clarity on competency expectations, additional action verbs from Bloom’s Revised Taxonomy are used to specify the intended cognitive processes and observable learner behaviors.

* **Formal Grammars – Analyze**  
  * *Differentiate, Compare, Contrast, Examine, Categorize*  
  * Differentiate and compare grammars according to structural rules, production forms, and generative scope.  

* **Chomsky Hierarchy – Analyze**  
  * *Explain, Interpret, Distinguish, Classify*  
  * Classify grammars according to their expressive level in the Chomsky hierarchy and identify their associated automata.  

* **Regular Grammars – Understand**  
  * *Describe, Exemplify, Summarize*  
  * Describe the form and constraints of regular grammars and relate them to finite automata recognition.  

* **Context-Free Grammars – Apply**  
  * *Identify, Illustrate, Construct, Validate*  
  * Identify or construct examples of context-free grammars; validate their structural differences from regular grammars.  

* **Analytical & Critical Thinking (FPK) – Apply**  
  * *Evaluate, Compare*  
  * Evaluate the expressive adequacy of grammar classifications and justify reasoning with formal arguments.  



### Summary Table for Competency CT25.1.3  

| **Code** | **Competency** | **Dispositions** | **Knowledge** | **Skill (Bloom)** |
|-----------|----------------|------------------|----------------|------------------|
| CT25.1.3 | **Differentiate and Classify Formal Grammars** | Analytical, Clear, Persistent, Critical | Formal Grammars | **Analyze (Differentiate, Compare, Contrast, Examine, Categorize)** |
|   |   |   | Chomsky Hierarchy | **Analyze (Explain, Interpret, Distinguish, Classify)** |
|   |   |   | Regular Grammars | **Understand (Describe, Exemplify, Summarize)** |
|   |   |   | Context-Free Grammars | **Apply (Identify, Illustrate, Construct, Validate)** |
|   |   |   | Analytical & Critical Thinking (FPK) | **Analyze (Evaluate, Compare)** |






### 4.4 Competency CT25.1-4 Specification  

**Code:** CT25.1.4  
**Source Task:** Task25.1 – Music Collection  
**Derived from:** Learning Objective 4 – Identify and model patterns using Finite State Machines (FSMs)  


### Competency Title  
    Identify and Model Patterns Using Finite State Machines (FSMs)


### Textual Description  

This competency involves the ability to **identify, construct, and analyze Finite State Machines (FSMs)** that recognize patterns corresponding to **musical genres or structural features** within symbolic compositions.  

Learners must demonstrate the capacity to:  
- **Model** musical structures as deterministic or non-deterministic automata.  
- **Explain** transitions, states, and acceptance criteria using formal notation and diagrams.  
- **Analyze** how automaton behavior reflects musical regularities or rules.  
- **Evaluate** and refine automata to ensure correctness, minimality, and expressiveness.  



### Knowledge Specification  

#### Computing Knowledge
- **Finite State Machines (FSMs):** conceptual foundations, deterministic and non-deterministic models.  
- **Deterministic Finite Automata (DFA):** formal definition, transition functions, acceptance states, and minimality.  
- **Regular Languages:** recognition of patterns and structures representable by FSMs.  
- **Language Theory:** relation between regular languages, automata, and expressions.  

#### Professional Knowledge (CC2020 FPK)
- **Analytical and Critical Thinking:** evaluate design correctness and optimize FSM structure.  


### Disposition Specification  

- **Creativity** – exploring alternative representations or simplifications of automata.  
- **Precision** – maintaining formal correctness in the definition of states, transitions, and acceptance conditions.  
- **Persistence** – refining automata until they achieve minimal and correct form.  
- **Collaboration** – validating automaton models through group reasoning and peer verification.  



### Knowledge–Skill Pairing and Bloom’s Taxonomy Alignment  

* **Finite State Machines (FSMs) - Create**
  * *Construct, Model, Represent, Develop, Implement*
  * Construct FSMs that recognize symbolic musical patterns and genres; represent state transitions formally. 

* **Deterministic Finite Automata (DFA) - Apply / Analyze** 
  * *Define, Illustrate, Demonstrate, Distinguish*
  * Define deterministic transitions and acceptance criteria; analyze how DFA structure corresponds to musical rules.
  
* **Regular Languages - Understand**
  * *Explain, Interpret, Associate, Exemplify*
  * Explain how FSMs capture regularities within musical structures. 

* **Language Theory - Understand** 
  * *Describe, Clarify, Summarize*
  * Describe theoretical relationships between regular expressions, automata, and languages.


* **Analytical & Critical Thinking (FPK) - Apply** 
  * *Verify, Optimize, Compare, Validate*
  * Verify FSM correctness, minimize redundant states, and justify equivalence among automata. 



### Summary Table for Competency CT25.1.4  

| **Code** | **Competency** | **Dispositions** | **Knowledge** | **Skill (Bloom)** |
|-----------|----------------|------------------|----------------|------------------|
| CT25.1.4 | **Identify and Model Patterns Using Finite State Machines (FSMs)** |  Creative, Precise, Persistent, Collaborative | Finite State Machines (FSMs) | **Create (Construct, Model, Represent, Develop, Implement)** |
|   |   |   | Deterministic Finite Automata (DFA) | **Apply / Analyze (Define, Illustrate, Demonstrate, Distinguish)** |
|   |   |   | Regular Languages | **Understand  (Explain, Interpret, Associate, Exemplify)** |
|   |   |   | Language Theory | **Understand (Describe, Clarify, Summarize)** |
|   |   |   | Analytical & Critical Thinking (FPK) | **Apply (Verify, Optimize, Compare, Validate)** |





### 4.5 Competency CT25.1-5 Specification  

**Code:** CT25.1.5  
**Source Task:** Task25.1 – Music Collection  
**Derived from:** Learning Objective 5 – Apply and justify operations on formal languages  
 

### Competency Title  
    Apply and Justify Operations on Formal Languages


### Textual Description  

This competency involves the ability to **apply and justify formal operations** on languages, such as **union, concatenation, intersection, complement, and Kleene star**, demonstrating mathematical rigor in proofs or counterexamples that validate these operations in context.  

Learners must demonstrate the capacity to:  
- **Perform** algebraic and set-theoretic operations on formal languages using symbolic notation.  
- **Verify** the closure properties of languages under specific operations.  
- **Provide** mathematical proofs or counterexamples that justify the correctness or invalidity of results.  
- **Document** reasoning steps clearly, ensuring the consistency of formal derivations.  


### Knowledge Specification  

#### Computing Knowledge
- **Formal Languages:** structure, representation, and operations over language sets.  
- **Language Operations:** union, concatenation, intersection, complement, and Kleene star.  
- **Closure Properties:** theoretical validation of operations over language families (regular and context-free).  
- **Proof Techniques:** direct proof, proof by induction, and counterexamples.  
- **Language Theory:** algebraic laws and relationships among formal language operations.  

#### Professional Knowledge
- **Analytical and Critical Thinking (FPK):** evaluate the logical soundness of proofs and the validity of operations.  


### Disposition Specification  

- **Analytical** – maintaining logical consistency in proofs and derivations.  
- **Precision** – ensuring formal correctness in symbolic manipulation and mathematical notation.  
- **Perseverance** – sustaining focus through iterative testing and validation of operations.  
- **Critical Judgment** – questioning assumptions and testing language closure properties through counterexamples.  
- **Clarity** – articulating reasoning with coherent and mathematically precise explanations.  


### Knowledge–Skill Pairing and Bloom’s Taxonomy Alignment  

To provide clarity on competency expectations, additional action verbs from Bloom’s Revised Taxonomy are used to specify the intended cognitive processes and observable learner behaviors.

* **Formal Languages – Apply**  
  * *Perform, Operate, Implement, Verify*  
  * Apply formal operations (union, concatenation, intersection, complement, Kleene star) and verify results for correctness.  

* **Language Operations – Apply**  
  * *Use, Execute, Manipulate, Demonstrate*  
  * Perform symbolic manipulations to demonstrate how operations modify or combine languages.  

* **Closure Properties – Analyze**  
  * *Validate, Test, Examine, Prove*  
  * Analyze and validate whether language families remain closed under given operations.  

* **Proof Techniques – Evaluate**  
  * *Prove, Demonstrate, Construct, Refute, Justify*  
  * Construct formal proofs or counterexamples demonstrating the correctness or limitation of each operation.  

* **Analytical & Critical Thinking (FPK) – Apply**  
  * *Assess, Critique, Justify, Conclude*  
  * Evaluate reasoning quality and coherence in proofs, justifying conclusions through formal logic.  



### Summary Table for Competency CT25.1.5  

| **Code** | **Competency** | **Dispositions** | **Knowledge** | **Skill (Bloom)** |
|-----------|----------------|------------------|----------------|------------------|
| CT25.1.5 | **Apply and Justify Operations on Formal Languages** | Analytical, Precise, Perseverant, Critical, Clear | Formal Languages | **Apply / Evaluate (Perform, Operate, Implement, Verifyy)** |
|   |   |   | Language Operations | **Apply (Use, Execute, Manipulate, Demonstrate)** |
|   |   |   | Closure Properties | **Analyze (Validate, Test, Examine, Prove)** |
|   |   |   | Proof Techniques | **Evaluate (Prove, Demonstrate, Construct, Refute, Justify)** |
|   |   |   | Analytical & Critical Thinking (FPK) | **Apply (Assess, Critique, Justify, Conclude)** |



### 4.6 Competency CT25.1-6 Specification  

**Code:** CT25.1.6  
**Source Task:** Task25.1 – Music Collection  
**Derived from:** Learning Objective 6 – Recognize and apply homomorphisms and encodings  


### Competency Title  
    Recognize and Apply Homomorphisms and Encodings

### Textual Description  

This competency involves the ability to **recognize, define, and apply homomorphisms and symbolic encodings** that map elements from the **musical domain** (e.g., notes, instruments, genres) to corresponding representations in **formal languages**.  

Learners must demonstrate the capacity to:  
- **Map** musical features into symbolic alphabets used in automata or grammar models.  
- **Demonstrate** equivalence or transformation between representations (e.g., *score ↔ MP3*).  
- **Analyze** how encoding choices affect structure, expressiveness, and recognition.  
- **Validate** transformations through proofs or systematic comparisons.  


### Knowledge Specification  

#### Computing Knowledge
- **Homomorphisms:** definition, properties, and examples in formal languages.  
- **Encoding Systems:** mapping between symbols, alphabets, and representations.  
- **Equivalence and Transformation:** conditions for isomorphism and meaning preservation.  
- **Language Representation:** interpretation of symbolic domains and transformations between them.  

#### Professional Knowledge
- **Analytical and Critical Thinking (FPK):** evaluate mapping consistency and representation validity.  

### Disposition Specification  

- **Analytical Rigor** – verifying structural correctness in mappings and transformations.  
- **Creativity** – designing expressive and efficient encoding strategies.  
- **Precision** – maintaining exact correspondence between musical and formal symbols.  
- **Curiosity** – exploring multiple valid mappings for the same conceptual domain.  


### Knowledge–Skill Pairing and Bloom’s Taxonomy Alignment  

To provide clarity on competency expectations, additional action verbs from Bloom’s Revised Taxonomy are used to specify the intended cognitive processes and observable learner behaviors.

* **Homomorphisms – Apply**  
  * *Map, Transform, Convert, Compare, Verify*  
  * Apply homomorphisms to translate musical elements into formal symbols; verify the correctness of transformations.  

* **Encodings – Apply**  
  * *Represent, Implement, Express, Use*  
  * Represent musical structures using appropriate symbolic encodings; demonstrate their interpretability.  

* **Equivalence and Transformation – Analyze**  
  * *Examine, Validate, Justify, Assess*  
  * Analyze how transformations preserve or alter the semantics of musical structures.  

* **Analytical & Critical Thinking (FPK) – Apply**  
  * *Compare, Verify, Reason, Validate*  
  * Evaluate and justify the adequacy of symbolic mappings and transformations.  



### Summary Table for Competency CT25.1.6  

| **Code** | **Competency** | **Dispositions** | **Knowledge** | **Skill (Bloom)** |
|-----------|----------------|------------------|----------------|------------------|
| CT25.1.6 | **Recognize and Apply Homomorphisms and Encodings** | Analytical, Creative, Precise, Curious | Homomorphisms | **Apply  (Map, Transform, Convert, Compare, Verify)** |
|   |   |   | Encodings | **Apply (Represent, Implement, Express, Use)** |
|   |   |   | Equivalence and Transformation | **Analyze (Examine, Validate, Justify, Assess)** |
|   |   |   | Analytical & Critical Thinking (FPK) | **Apply (CCompare, Verify, Reason, Validate)** |




### 4.7 Competency CT25.1-7 Specification  
    Reuse C03 - Test Automata Using Simulators



### 4.8 Competency CT25.1-8 Specification  

**Code:** CT25.1.8  
**Source Task:** Task25.1 – Music Collection  
**Derived from:** Learning Objective 8 – Produce a technical report with mathematical rigor  

### Competency Title  
    Produce a Technical Report with Mathematical Rigor

  Specializes C05 - Write a Technical Report

    C05.1 - Write a Technical Report with Mathematical Rigor

### Textual Description  

  This competency involves the ability to **produce a coherent and mathematically rigorous technical report**, documenting all decisions, proofs, and results from formal modeling activities.  












## Table of Competencies for Task25.1 - Music Collection

| **Code**  | **Competency** | **Dispositions** | **Knowledge** | **Skill** |
|-----------|----------------|------------------|---------------|-----------|
|           |                |                  | Regular Expressions | **Create (Design, Construct, Compose, Generate, Formalize)** |
| CT25.1.1  | **Apply Regular Expressions to Define and Formalize Simple Musical Languages** | Collaborative, Responsible, Creative | Language theory | **Understand (Explain, Describe, Interpret, Summarize, Illustrate)**
|          | | | Pattern Matching | **Apply (Use, Implement, Manipulate, Operate, Demonstrate)** |
|          | | | Analytical and Critical Thinking (FPK) | **Apply (Verify, Differentiate, Compare, Justify, Assess)** |
| | | | | |
| CT25.1.2 | **Interpret and Apply Algebraic Notation to Represent Musical Strings** | Precise, Creative, Persistent | Algebraic Notation for Strings | **Apply (Use, Manipulate, Implement)** |
|   |   |   | Language Theory | **Understand  (Interpret, Explain, Distinguish, Relate)** |
|   |   |   | String Operations | **Apply  (Combine, Modify, Transform)** |
|   |   |   | Analytical & Critical Thinking (FPK) | **Analyze / Evaluate (Verify, Compare, Justify)** |
| | | | | |
| CT25.1.3 | **Differentiate and Classify Formal Grammars** | Analytical, Clear, Persistent, Critical | Formal Grammars | **Analyze (Differentiate, Compare, Contrast, Examine, Categorize)** |
|   |   |   | Chomsky Hierarchy | **Analyze (Explain, Interpret, Distinguish, Classify)** |
|   |   |   | Regular Grammars | **Understand (Describe, Exemplify, Summarize)** |
|   |   |   | Context-Free Grammars | **Apply (Identify, Illustrate, Construct, Validate)** |
|   |   |   | Analytical & Critical Thinking (FPK) | **Analyze (Evaluate, Compare)** |
| | | | | |
| CT25.1.4 | **Identify and Model Patterns Using Finite State Machines (FSMs)** |  Creative, Precise, Persistent, Collaborative | Finite State Machines (FSMs) | **Create (Construct, Model, Represent, Develop, Implement)** |
|   |   |   | Deterministic Finite Automata (DFA) | **Apply / Analyze (Define, Illustrate, Demonstrate, Distinguish)** |
|   |   |   | Regular Languages | **Understand  (Explain, Interpret, Associate, Exemplify)** |
|   |   |   | Language Theory | **Understand (Describe, Clarify, Summarize)** |
|   |   |   | Analytical & Critical Thinking (FPK) | **Apply (Verify, Optimize, Compare, Validate)** |
| | | | | |
| CT25.1.5 | **Apply and Justify Operations on Formal Languages** | Analytical, Precise, Perseverant, Critical, Clear | Formal Languages | **Apply / Evaluate (Perform, Operate, Implement, Verifyy)** |
|   |   |   | Language Operations | **Apply (Use, Execute, Manipulate, Demonstrate)** |
|   |   |   | Closure Properties | **Analyze (Validate, Test, Examine, Prove)** |
|   |   |   | Proof Techniques | **Evaluate (Prove, Demonstrate, Construct, Refute, Justify)** |
|   |   |   | Analytical & Critical Thinking (FPK) | **Apply (Assess, Critique, Justify, Conclude)** |
| | | | | |
| CT25.1.6 | **Recognize and Apply Homomorphisms and Encodings** | Analytical, Creative, Precise, Curious | Homomorphisms | **Apply  (Map, Transform, Convert, Compare, Verify)** |
|   |   |   | Encodings | **Apply (Represent, Implement, Express, Use)** |
|   |   |   | Equivalence and Transformation | **Analyze (Examine, Validate, Justify, Assess)** |
|   |   |   | Analytical & Critical Thinking (FPK) | **Apply (CCompare, Verify, Reason, Validate)** |