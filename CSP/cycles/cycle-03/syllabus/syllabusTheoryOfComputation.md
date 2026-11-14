# Introduction to Formal Languages and Theory of Computation

## Course Overview

Institute of Computing, Federal University of Bahia (UFBA)  
Bachelor’s Degree in Computer Science  
Fourth semester, second year

The **Introduction to Formal Languages and Theory of Computation** course was delivered remotely using an interactive approach based on **Problem-Based Learning (PBL)**. Its main objective was to develop critical thinking and problem-solving skills through practical scenarios that connect theory with real-world applications.

Several tools supported collaborative learning:

- **Google Colab** for sharing course materials and hands-on exercises.
- **Google Meet, Discord, and WhatsApp** for live tutorials and question-and-answer discussions.
- **Moodle** for distributing course content, submitting assignments, and holding asynchronous discussions.
- **Email** as an additional channel for individual support.

Together, these tools provided flexibility and accessibility and supported the development of core competencies in Theory of Computation.

## Course Description

The course provides a broad introduction to formal languages and the theory of computation. It begins with fundamental concepts in formal languages, including the Chomsky hierarchy, and proceeds to regular and context-free languages. It covers regular expressions and key computational models, including deterministic and nondeterministic finite automata and pushdown automata.

Students also study context-free grammars and basic techniques in lexical and syntactic analysis relevant to programming language processing. The course introduces Turing machines as a formal model of computation and discusses recursively enumerable and recursive languages, decidability, and undecidability.

Through practical examples and theoretical discussion, students examine the **Halting Problem** and **Church’s Thesis** and consider their implications for the limits of computation. The course concludes with an overview of basic concepts in computational complexity and discusses decidable and undecidable problems in relation to the Chomsky hierarchy.

## Course Objectives

### General Objective

Develop students’ understanding of the languages in the **Chomsky hierarchy** and their relationships to formal models in the **theory of computation**.

### Specific Objectives

Develop the following skills and competencies:

- Recognize the concepts of an alphabet, a word, and a language.
- Work with languages, recognizers, and grammars.
- Design finite automata, pushdown automata, and Turing machines.
- Relate automata to the analysis components of a programming language compiler.
- Understand the limits of computation.
- Recognize how Church’s Thesis applies.
- Understand P and NP and the notion of NP-completeness.

### Additional Competencies Developed through PBL

Through **Problem-Based Learning**, the course also aims to develop students’ ability to:

- Formulate problem scenarios using concepts and tools from the theory of computation.
- Propose formal computational representations and solutions for real-world problems.
- Evaluate how formalisms with different expressive power can be used to represent and solve the problems presented.

## Course Content

1. **Motivation for Studying Formal Languages**
   - The Chomsky hierarchy
   - Programming language specification and compilers

2. **The Concept of a Formal Language**
   - Alphabets, words, Kleene closure, and languages

3. **Regular Languages**
   - Regular expressions
   - Deterministic finite automata (DFAs)
   - Nondeterministic finite automata (NFAs)
   - NFAs with λ-transitions
   - Lexical analysis of programming languages

4. **Context-Free Languages**
   - Pushdown automata
   - Context-free grammars (CFGs)
   - Parse trees
   - Ambiguity in CFGs
   - Syntactic analysis of programming languages

5. **Recursive and Recursively Enumerable Languages**
   - Turing machines
   - Church’s Thesis
   - The halting language

6. **P, NP, and NP-Complete Problems**

## Teaching and Learning Methodology

The course will use an active, problem-based approach. Each learning unit will center on students working together to solve a problem. Activities will include live tutorials and asynchronous discussions through the course’s **virtual learning environment (VLE)**.

The course will combine synchronous and asynchronous online activities, including:

- Interactive lectures
- Video lectures
- Activities, exercises, and problems
- Group discussions of problems, activities, and exercises
- Live tutorials with groups of students

## Target Competencies

The target competencies specify the **observable skills** students are expected to demonstrate as they progress from understanding computational models to **designing, analyzing, validating, and communicating** them. In line with the course content and the **PBL** approach, each competency integrates knowledge of formal languages and models, skills in modeling, analysis, implementation, and testing, and dispositions such as rigor, collaboration, and responsibility. Students produce evidence through **simulations of automata and Turing machines**, formal reasoning about **expressive power and the limits of computation**, and a **technical report** documenting design decisions, tests, and justifications.

For clarity, competencies C01–C16 are grouped by theme. The identifiers serve as reference labels, and the competencies can be developed in different orders.

- **Modeling and Construction:** C01, C06 (FSMs), C12 (PDAs), and C07 (TMs).
- **Expressive Power and Mappings:** C04 (regular expressions and finite automata), C13 (rule-based notation), and C14 (grammar classification).
- **Variants and Analysis of Computational Capabilities:** C08–C09 (Turing machine variants), C16 (system capabilities), and C15 (the Halting Problem).
- **Determinism and Patterns:** C02 (DFAs and justification) and C11 (pattern identification in FSMs).
- **Verification and Communication:** C03 and C10 (simulator-based testing), and C05 (technical reporting).

Assessment emphasizes **correctness, completeness, and conformance to formal specifications**, as well as students’ ability to **justify choices**, compare alternatives, and **communicate results** clearly.

### Key Competencies

**C01 – Develop Problem Solutions Using Automata**  
Interpret requirements and design solutions using formal models such as finite automata, pushdown automata, and Turing machines. Validate the models against formal specifications and representative test cases.

**C02 – Justify the Use of Deterministic Finite Automata (DFAs)**  
Analyze problem constraints to justify when DFAs are appropriate. Explain the trade-offs of determinism and its effects on design, complexity, and implementation.

**C03 – Test Automata Using Simulators**  
Use tools such as JFLAP to simulate automata and design systematic tests to verify correctness, completeness, and conformance to the specification.

**C04 – Define Regular Expressions for Finite Automata**  
Translate the behavior of a finite automaton into an equivalent regular expression and perform the reverse translation. Validate equivalence using edge cases.

**C05 – Write a Technical Report**  
Produce a structured report, using a format such as the Brazilian Computer Society (SBC) template, to document design decisions, implementation strategies, experiments or simulations, results, and justifications.

**C06 – Develop Problem-Solving Solutions Using Finite State Machines (FSMs)**  
Model system behavior with FSMs to meet specified requirements. Use formal reasoning and testing to make the models verifiable and reliable.

**C07 – Develop Problem-Solving Solutions Using Turing Machines**  
Specify and implement Turing machine models that process or classify inputs. Map requirements to formal operations and demonstrate correctness.

**C08 – Identify Turing Machine Variants**  
Recognize and characterize variants, including multitape and nondeterministic Turing machines and other extensions. Compare their computational power and constraints.

**C09 – Apply Turing Machine Variants**  
Select and apply suitable Turing machine variants to solve problems efficiently. Justify their suitability and explain the trade-offs relative to the standard model.

**C10 – Test Turing Machines Using Simulators**  
Use dedicated tools to simulate and evaluate Turing machines. Verify correctness, termination conditions, and conformance to the formal specification.

**C11 – Identify Patterns in Finite State Machines**  
Analyze the structure and behavior of FSMs to detect patterns, redundancies, and relationships among inputs, transitions, and state configurations. Use these findings to guide changes that address model complexity.

**C12 – Develop Problem-Solving Solutions Using Pushdown Automata**  
Design pushdown automaton models for context-free problems. Make stack behavior explicit and validate the acceptance conditions.

**C13 – Interpret Rule-Based Notation**  
Read and reason about rule-based formalisms, such as production rules and transition tables. Relate those formalisms to the behavior described by automata or regular expressions.

**C14 – Differentiate Classifications of Formal Grammars**  
Classify grammars within the Chomsky hierarchy and relate each class to its recognizers and expressive power.

**C15 – Understand the Halting Problem and Its Implications**  
Explain decidability and undecidability through the Halting Problem. Use reductions to reason about the limits of computation for particular problems.

**C16 – Apply Turing Machine Concepts to Analyze Computational System Capabilities**  
Use Turing machine theory to classify problems as computable, semidecidable, or undecidable and to reason about the capabilities and limits of practical systems.

## Assessment of Learning

Student performance will be assessed through:

- Active participation in activities, forums, and wikis
- Completion of exercises and quizzes
- Development of solutions to problems
- Individual self-assessment
- Peer assessment

Assessments use a scale from 0 to 10.

## References

### Required Reading

- Sipser, Michael. *Introdução à Teoria da Computação* [*Introduction to the Theory of Computation*]. Second U.S. edition. Thomson.
- Ramos, Marcus Vinícius Midena, João José Neto, and Ítalo Santiago Vega. *Linguagens Formais: Teoria, Modelagem e Implementação*. Bookman, 2009.
- Louden, Kenneth C. *Compiladores: Princípios e Práticas*. São Paulo: Thomson Pioneira, 2004.

### Supplementary Reading

- Hopcroft, John E., Jeffrey D. Ullman, and Rajeev Motwani. *Introdução à Teoria de Autômatos, Linguagens e Computação*. Portuguese translation of the second U.S. edition. Campus, 2003.
- Menezes, Paulo Blauth. *Linguagens Formais e Autômatos*. Sagra Luzzatto. Textbook Series, Institute of Informatics, Federal University of Rio Grande do Sul (UFRGS).
- Lewis, Harry R., and Christos H. Papadimitriou. *Elementos de Teoria da Computação*. Bookman. Originally published as *Elements of the Theory of Computation*, Prentice-Hall, 1998.
- Denning, Peter J., Jack B. Dennis, and Joseph E. Qualitz. *Machines, Languages and Computation*. Prentice-Hall, 1978.
- Aho, Alfred V., Monica S. Lam, Ravi Sethi, and Jeffrey D. Ullman. *Compilers: Principles, Techniques, and Tools*. Second edition. Addison-Wesley, 2008.