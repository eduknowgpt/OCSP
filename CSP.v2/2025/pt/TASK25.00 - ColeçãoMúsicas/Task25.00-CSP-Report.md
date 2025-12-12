# Competency Specification Report: Task25.00 - Coleção de Músicas


## Introduction

Building on the foundational CSP methodology, this report presents the application of the **Competency Authoring phase** in **Task25.1 – Coleção de Músicas**, a Problem-Based Learning (PBL) scenario that explores the use of **finite automata and regular expressions** e produzir um relatório com respostas claras, coerentes e rigorosas, com definições formais, exemplos mínimos, demonstrações (incluindo indução e fechos), e contraexemplos quando apropriado.


## 1. Instructional Entity Analysis

### Title

- Coleção de Músicas

### Description
- Os aprendizes devem analisar partituras e representá-as como sequencias de símbolos e fazer operações sobre estas.


### Solution Development Process

Describe the expected learner approach:

- Analyze problem constraints:
    - As partituras podem ter 1 ou vários instrumentos.
    - Cada música pode ter um número arbitrário de símbolos.
    - Cada música tem um gênero.

- Modelar as partituras como autômatos finitos (states, transitions, actions).

- Precisa identificar o gênero de cada música.

- Document and report design choices and formal representation com rigor matemático.




### Expected Outcomes
Learners should produce:

- Definições de Regular Expressions
- Interpretação e aplicação de algebraic notation for strings
- Differentiate classifications of formal grammars
- Identify Patterns in Finite State Machines
- Aplicar Operações com Linguagens Formais
- Modelelar real-world problems using formal language concepts
- Reconhecer e aplicar Homomorfismos / Codificações
- Simulation results demonstrating a correta determinação de gêneros e operações sobre strings.
- Elaborar um relatório técnico com explicações claras, coerentes e matematicamente rigorosas, com definições formais, exemplos mínimos, demonstrações (incluindo indução e fechos), e contraexemplos quando apropriado.


### Acquisition Context

- Disciplina teórica de Teoria da Computação

- Tarefas avaliativas



### Target Audience Profile

- Academic Level: 2nd–3rd year undergraduate CS students.

- Domain Experience: Solid grounding in data structures, and basic automata.

- Roles: Design FSMs; document technical decisions.


### Proficiency Scale

- Escala com notas entre 0 e 100 (representando notas como 8.5 no modelo de avaliação da disciplina, por exemplo, que corresponde a 85 na escala).



## 2. Knowledge Enumeration

To systematically enumerate the computing knowledge required for this task, the **ACM CS2023** was used as a controlled vocabulary. This Body of Knowledge is widely adopted by ACM CS2023 report, ensuring standardization and consistency in the categorization of computing knowledge.  

For **professional knowledge (FPK)**, we referenced the **ACM Computing Curriculum 2020 (CC2020)**, which provides a structured framework for essential professional competencies.  

Based on the **task description**, the following set of required knowledge components was identified:  


cs2023:Topic/FPL-Syntax_6 a cs2023:Topic,  
    skos:definition "Language theory"

cs2023:Topic/AL-Models_2_a_i a cs2023:Topic,      skos:definition "Regular Expressions"

cs2023:Topic/FPL-Syntax_1 a cs2023:Topic,  
    skos:definition "Regular grammars vs context-free grammars (See also: AL-Models)" ;

cs2023:Topic/FPL-Constructs_8 a cs2023:Topic,  
    skos:definition "String manipulation via pattern-matching (regular expressions)" ;
    skos:broader cs2023:KU/FPL-Constructs ;

cs2023:Topic/AL-Foundational_16_c a cs2023:Topic,  
    skos:definition "Regular expression matching" ;

cs2023:Topic/AL-Models_7 a cs2023:Topic,  
    skos:definition "Deterministic and nondeterministic automata" ;

cs2023:Topic/SF-Foundations_5 a cs2023:Topic,  ontoksd:Knowledge ;
    skos:definition "Finite state machines (e.g., NFA, DFA) (See also: AL-Models)" ;



### **Computing Knowledge**  
- Finite State Machines 
- Deterministic Finite Automata (DFAs)
- Linguagens Formais
- Homomorfismos 
- **Regular Languages (Regular Expressions)**  
  - Requires understanding and applying **formal techniques** to represent and manipulate string sets.  
  - Used primarily in **text processing, lexical analysis, and pattern matching** within the vending machine’s operational logic.  

- **Requirements Analysis**  
  - A systematic process for **collecting, analyzing, and specifying system requirements**.  
  - Ensures that **user needs and system expectations** are clearly understood and documented.  


### **Professional Knowledge (FPK)**  
- **Analytical and Critical Thinking**  
  - The ability to **break down complex problems into fundamental components**, evaluate results, and make well-reasoned decisions based on rigorous analysis.  

- **Written Communication**  
  - The ability to **compose clear and structured technical reports** detailing the design, implementation, and validation processes.  
  - Ensures that findings and decisions are effectively communicated to stakeholders.  

This **knowledge enumeration** serves as the foundation for competency specification, ensuring that students acquire both **theoretical and practical expertise** necessary to complete the task successfully.



## 3. Learning Objectives Identification

The **general objective** of this task is to develop **finite automata and regular expressions** to solve **real-world problems** by modeling músicas como strings.

### **Specific Learning Objectives**

- Definições de Regular Expressions
- Interpretação e aplicação de algebraic notation for strings
- Differentiate classifications of formal grammars
- Identify Patterns in Finite State Machines
- Aplicar Operações com Linguagens Formais

- Reconhecer e aplicar Homomorfismos / Codificações
- Simulation results demonstrating a correta determinação de gêneros e operações sobre strings.
- Elaborar um relatório técnico com explicações claras, coerentes e matematicamente rigorosas, com definições formais, exemplos mínimos, demonstrações (incluindo indução e fechos), e contraexemplos quando apropriado.



1. **Identify system functionalities**  
   - Analyze the user’s conceptual model de músicas em múltiplos gêneros.

2. Modelelar real-world problems using formal language concepts

2. **Align user requirements with automaton functionalities**  
   - Reconcile the desired functionalities do músico with the constraints and capabilities of the automaton being developed.

5. **Understand the equivalence between Finite Automata (FA) and Regular Expressions (RE)**  
   - Establish connections between **finite automata representations** and **regular expressions**, reinforcing their theoretical and practical interchangeability.

6. **Apply FA-to-RE equivalence in the development of regular expressions**  
   - Utilize existing finite automata to derive **corresponding regular expressions**, applying formal methods to convert automata into equivalent regex patterns.

7. **Associate músicas with alphabet symbols**  
   - Map real-world elements  onto the **formal alphabet** used in automaton design.

8. **Develop technical reports**  
   - Document the **design, implementation, and validation** of the automaton, ensuring clarity and precision in technical writing.



### **Importance of These Objectives**
These learning objectives provide a **structured pathway** for competency development, ensuring that students acquire:
- **A strong theoretical foundation** in automata and formal languages.
- **The ability to bridge theory and practice**, applying formal methods to solve computational problems.
- **Hands-on experience with simulation tools**, reinforcing practical problem-solving skills.
- **Technical communication skills**, essential for conveying solutions in professional and academic contexts.


By achieving these objectives, students will be equipped with both the **computational and analytical skills** necessary for modeling real-world systems using **finite automata and regular expressions**.



## 4. Competency Definition

Competencies are specified based on the **Learning Objectives (LOs)** identified in the task analysis.

### 4.1 Competency C17 Specification  

### A.1 Competency Title
    Apply operations on formal languages

### A.2 Textual Description  

This competency involves the ability de aplicar operações formais sobre linguagens (concatenação, união, interseção, complemento, fecho de Kleene, reversão), analisando seus efeitos e propriedades.

Os aprendizes devem evidenciar a capacidade de ...



### A.3 Knowledge Specification
The following knowledge areas are critical for this competency:  

cs2023:Topic/FPL-Syntax_6 - "Language theory"

cs2023:Topic/AL-Models_2_a_i - "Regular Expressions"


- **Analytical and Critical Thinking (FPK)**  
  - Required for **problem decomposition and strategic planning**.  
  - Helps in aligning user requirements with technical feasibility while optimizing computational resources.  



### A.4 Disposition Specification

 **Collaboration**  
- The task follows the **Problem-Based Learning (PBL) methodology**, requiring continuous team interaction.  
- Essential for developing solutions collaboratively through **PBL whiteboard sessions**, maintaining the **logbook**, and **documenting each project phase**.  
- Encourages **knowledge-sharing** and iterative improvements.  

 **Responsibility**  
- Ensures adherence to **project deadlines**, accurate **documentation**, and a **functional automaton design**.  
- Requires individual accountability for contributions, ensuring that the **final deliverable meets user expectations** and project standards.  

**Creativity**  
- Necessary for adapting automata **functionalities to specific user requirements**.  
- Encourages exploring **alternative implementations**, such as incorporating **randomized elements** in automata behavior.  
- Enhances **technical documentation**, making system operations visually and conceptually engaging.  


### A.5 Knowledge-Skill Pairing and Bloom’s Taxonomy Alignment

This step maps **knowledge areas to the corresponding skills (Bloom Cognitive Level)** required to successfully demonstrate competency in this task.  

**A.5.1 Mapping Knowledge to Skills**  
To achieve this competency, students must demonstrate the ability to:  

**Compreender** Language theory para ...
**Aplicar** operações sobre Regular Expressions para ...
**Apply** Analytical and Critical Thinking para...



**A.5.3 Verb Annotation**  
To provide clarity on competency expectations, the following verb annotations define the required actions:  

- **Apply** → Analytical and Critical Thinking → 
- **Aplicar** operações sobre Regular Expressions -> (Compare, Compose, Differentiate)




### A.6 Summary Table for Competency A

| **Competency** | **Dispositions** | **Knowledge** | **Skill** |
|------------|-----------|------------|----|
|  |   | Regular Expressions | **Apply (Compare, Compose, Differentiate)** |
| **Apply operations on formal languages** | Collaborative, Responsible, Creative | Language theory | **Understand**
| | | Analytical and Critical Thinking (FPK) | **Apply** |





## Table of Competencies for Task: *The Vending Machine for Sodas and Snacks*

| **Competency** | **Dispositions** | **Knowledge** | **Skill** |
|----------------|------------------|---------------|-----------|
| **Develop problem solutions using Automata** | Collaborative, Responsible, Proactive, Creative | Automata over Infinite Objects | Create (Construct, Develop, Design) |
|  |  | Requirements Analysis | Apply (Interpret, Implement, Organize) |
|  |  | Analytical and Critical Thinking (FPK) | Apply |
|  |  |                                        |       |       
| **Determine when to use a DFA or NFA** | Investigative, Collaborative, Responsible, Proactive, Creative | Automata over Infinite Objects | Understand (Compare) |
|  |  | Analytical and Critical Thinking (FPK) | Apply (Evaluate, Decide) |
|  |  |                                        |       | 
| **Testing Automata Using Simulators** | Collaborative, Responsible, Proactive, Creative | Automata over Infinite Objects | Apply (Experiment, Relate, Simulate) |
|  |  | Problem Solving and Troubleshooting (FPK) | Apply (Diagnose, Debug, Refine) |
|  |  |                                        |       | 
| **Determining Regular Expressions that Represent Automata** | Investigative, Collaborative, Responsible, Proactive, Creative | Automata over Infinite Objects | Understand |
|  |  | Regular Languages | Apply |
|  |  | Problem Solving and Troubleshooting (FPK) | Apply |
|  |  |                                        |       | 
| **Relating Regular Expressions to Finite Automata** | Collaborative, Responsible, Proactive | Automata over Infinite Objects | Understand |
|  |  | Regular Languages | Understand |
|  |  |                                        |       | 
| **Collaborative Technical Report Writing** | Collaborative, Meticulous, Responsible | Written Communication (FPK) | Apply (Write, Structure, Revise, Refine) |
