
# **Introduction to Formal Languages and Theory of Computation**

## Course Overview

Institute of Computing – UFBA
Bachelor’s Degree in Computer Science
4th semester – 2nd year


The course **Introduction to Formal Languages and Theory of Computation** was delivered remotely, using a modern and interactive approach to learning. With the **PBL (Problem-Based Learning)** methodology. The central goal was to stimulate critical thinking and problem-solving through practical situations that bridge theory and real-world applications.

Various tools were employed to create a rich and collaborative learning experience:
- **Google Colab**: Provided materials and hands-on exercises.
- **Meet, Discord, and WhatsApp**: Used for real-time tutorials and Q&A forums.
- **Moodle**: Platform for distributing educational content, submitting assignments, and asynchronous discussions.
- **Email**: An additional communication channel for individual support.

The integration of these tools ensured flexibility and accessibility, fostering an environment conducive to the development of essential competencies in the Theory of Computation.

## Course Description

This course provides a comprehensive introduction to the theory of formal languages and computation. It explores the foundational concepts of formal languages, beginning with the Chomsky hierarchy and progressing through regular and context-free languages. Key models of computation are examined, including regular expressions, deterministic and nondeterministic finite automata, and pushdown automata.

Students will also study context-free grammars, along with fundamental techniques of lexical and syntactic analysis relevant to programming language processing. The course introduces Turing machines as a formal model of computation and discusses recursively enumerable and recursive languages, decidability, and undecidability.

Through practical examples and theoretical discussion, students will examine the Halting Problem and Church’s thesis, understanding their implications for what can and cannot be computed. The course concludes with an overview of basic concepts in computational complexity, including classes of decidable and undecidable problems within the Chomsky hierarchy.

## Course Objectives

### General Objective
To provide students with knowledge of the languages defined in the **Chomsky hierarchy** and their relationships with formal models in the **Theory of Computation**.

### Specific Objectives
Develop the following skills and competencies:
- Recognize the concepts of alphabet, word, and language.
- Manipulate languages, recognizers, and grammars.
- Develop finite automata, pushdown automata, and Turing machines.
- Relate automata to the analysis modules of a programming language compiler.
- Understand the limits of Computation.
- Recognize the application of Church’s Thesis.
- Understand the classes of problems **P**, **NP**, and **NP-Complete**.

### Additional Competencies with the PBL Methodology
With the adoption of **Problem-Based Learning (PBL)**, the course also aims to:
- Conceptualize problem situations using the tools of the Theory of Computation.
- Propose formal computational representations and solutions for real-world problems.
- Evaluate the application of formalisms with different expressive powers to represent and solve presented problems.


## Course Topics

1. Motivation for the Study of Formal Languages
    - Chomsky's Hierarchy
    - Specification of programming languages and compilers

2. Concept of Formal Language
    - Alphabet, word, Kleene closure, language

3. Regular Languages
    - Regular expressions
    - Deterministic finite automaton (DFA)
    - Nondeterministic finite automaton (NFA)
    - NFA with $\lambda$-transitions
    - Lexical analysis of programming languages

4. Context-Free Languages
    - Pushdown automaton
    - Context-free grammars (CFGs)
    - Parse trees
    - Ambiguity in CFGs
    - Syntactic analysis of programming languages

5. Recursive and Recursively Enumerable Languages
    - Turing machine
    - Church’s thesis
    - Halting language

6. P, NP and NP-Complete Problems


## Teaching and Learning Methodology
This course will follow a problem-based active learning methodology, in which each learning unit is structured around the collaborative solution of a problem. Activities will include synchronous tutorial sessions and asynchronous discussions via the adopted Virtual Learning Environment (VLE).

Specifically, the course will use a hybrid approach combining synchronous and asynchronous activities via the VLE, consisting of:

- Dialogued lectures
- Video lectures
- Activities, exercises, and problems
- Group discussions of problems, activities, and exercises
- Synchronous tutorial sessions with student groups

## Course Target Competences

The target competences specify the **observable abilities** students are expected to demonstrate as they progress from understanding to **designing, analyzing, validating, and communicating** computational models. Aligned with the course topics and the **PBL** approach, each competence integrates knowledge (formal languages and models), skills (modeling, analysis, implementation, testing), and dispositions (rigor, collaboration, responsibility). Evidence is produced through **automata/Turing-machine simulations**, formal reasoning about **expressiveness and limits of computation**, and a **technical report** that documents design decisions, tests, and justification.

For clarity, the competences (C01–C16) are organized across complementary themes; numbering does **not** imply a strict sequence:

* **Modeling & Construction:** C01, C06 (FSMs), C12 (PDAs), C07 (TMs).
* **Expressiveness & Mappings:** C04 (regex ↔ FA), C13 (rule-based notation), C14 (grammar classifications).
* **Variants & Capability Analysis:** C08–C09 (TM variants), C16 (system capabilities), C15 (Halting Problem).
* **Determinism & Patterns:** C02 (DFAs and justification), C11 (pattern identification in FSMs).
* **Verification & Communication:** C03, C10 (tool-based testing), C05 (technical report).

Assessment emphasizes **correctness, completeness, and adherence to formal specifications**, as well as the ability to **justify choices**, compare alternatives, and **communicate results** clearly.


### Key Competences

* **C01 – Develop problem solutions using Automata**
  Ability to interpret requirements and design automata-based solutions (FA, PDA, TM), validating models against formal specifications and representative test cases.

* **C02 – Justify the use of Deterministic Finite Automata (DFAs)**
  Analyze problem constraints to argue when DFAs are appropriate, explaining determinism trade-offs and impacts on design, complexity, and implementation.

* **C03 – Test automata using simulators**
  Use tools (e.g., JFLAP) to simulate automata, designing systematic tests to verify correctness, completeness, and conformance to the specification.

* **C04 – Define Regular Expressions for Finite Automata**
  Translate automaton behavior into equivalent regular expressions (and vice versa) and validate equivalence with edge-case examples.

* **C05 – Write a technical report**
  Produce a structured report (e.g., SBC format) documenting design decisions, implementation strategies, experiments/simulations, results, and justification.

* **C06 – Develop Problem-Solving Solutions Using Finite State Machines**
  Model system behavior with FSMs to meet stated requirements, ensuring verifiability and reliability through formal reasoning and tests.

* **C07 – Develop Problem-Solving Solutions Using Turing Machines**
  Specify and implement Turing-machine models that process or classify inputs, mapping requirements to formal operations and demonstrating correctness.

* **C08 – Identify Turing Machine Variants**
  Recognize and characterize variants (e.g., multi-tape, nondeterministic, other extensions), comparing computational power and constraints.

* **C09 – Apply Turing Machine Variants**
  Select and apply suitable TM variants to solve problems efficiently, justifying adequacy and trade-offs relative to the standard model.

* **C10 – Testing Turing Machines Using Simulators**
  Simulate and evaluate TMs with dedicated tools, checking correctness, termination conditions, and adherence to the formal specification.

* **C11 – Identify Patterns in Finite State Machines**
  Analyze FSM structure and behavior to detect patterns, redundancies, and input/transition relationships that inform complexity and refinements.

* **C12 – Develop problem-solving solutions using Pushdown Automata**
  Design PDA-based models for context-free problems, articulating stack behavior and validating acceptance conditions.

* **C13 – Interpret rule-based notation**
  Read and reason about rule-based formalisms (e.g., production rules, transition tables), relating them to automata/regex behavior.

* **C14 – Differentiate classifications of formal grammars**
  Classify grammars within the Chomsky hierarchy and connect each class to its recognizers and expressive power.

* **C15 – Understand the Halting Problem and its Implications**
  Explain decidability and undecidability via the Halting Problem, using reductions to reason about problem limits.

* **C16 – Apply Turing Machine Concepts to Analyze Computational System Capabilities**
  Use TM theory to classify problems as computable, semi-decidable, or undecidable and to reason about the capabilities/limits of practical systems.



## Learning Assessment
Student performance will be assessed based on:

- Active participation in course activities, forums, and wikis
- Completion of exercises and/or quizzes
- Development of problem solutions
- Individual self-assessment
- Peer evaluation

- Assessments use a grading scale from 0 to 10


## References
Basic References
INTRODUÇÃO À TEORIA DA COMPUTAÇÃO. MICHAEL SIPSER. 2ª EDIÇÃO NORTE AMERICANA. THOMSON.

Linguagens Formais: Teoria, Modelagem e Implementação. Marcus Vinícius Midena Ramos, João José Neto, Ítalo Santiago Vega. Editora Bookman. 2009.

Compiladores : princípios e práticas. LOUDEN, Kenneth C. São Paulo: Thomson Pioneira, 2004.


Additional References
Introdução à Teoria de Autômatos, Linguagens e Computação. John E. Hopcroft, Jeffery D. Ullman; Rajeev Motwani. Tradução da segunda edição americana. Editora Campus. 2003.

Linguagens Formais e Autômatos. Paulo Blauth Menezes. Editora Sagra Luzzatto. Série Livros Didáticos – Instituto de Informática da UFRGS.

ELEMENTOS DE TEORIA DA COMPUTAÇÃO  (ORIGINAL: ELEMENTS OF THE THEORY OF COMPUTATION. PRENTICE-HALL, INC., 1998). HARRY R. LEWIS, CHRISTOS H. PAPADIMITRIOU. EDITORA BOOKMAN.

Machines, Languages and Computation. Peter J. Denning; Jack B. Dennis; Joseph E. Qualitz. Prentice-Hall. 1978.

Compilers: Principles, Techniques, and Tools. Alfred V., Monica S. Lam, Ravi Sethi, Jeffrey D. Ullman. Addison Wesley; 2nd edition, 2008.