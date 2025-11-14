# **Competency Specification Report: TASK25.2 – Tic-Tac-Toe Implementation**

## **Introduction**

Building on the foundational CSP methodology, this report presents the application of the **Competency Authoring phase** in **TASK25.2 – Tic-Tac-Toe Implementation**, a learning task that explores **structured programming, data representation, control flow, and modular decomposition** in the design of a fully functional 3×3 TIC-TAC-TOE game.


## 1. Instructional Entity Analysis

### Title

* Tic-Tac-Toe Implementation (3×3)

### Description

* Learners face the problem of designing a Tic-Tac-Toe game that allows two human players to alternate valid moves, handles game rules robustly, detects victory or draw conditions, and clearly communicates the game state, while applying core concepts of structured programming.


### Solution Development Process

Describe the expected learner approach:

* Analyze the game constraints ( turn alternation, valid moves, board boundaries, winning conditions, draw scenarios ).

* Model the solution as a structured program ( using lists/matrices, conditionals, loops, and well-defined functions ).

* Simulate & validate  executing the program iteratively to test scenarios such as row/column/diagonal wins and invalid inputs .

* Document and report design choices and formal representation  through explanatory comments, modular code structure, and an individual oral explanation demonstrating conceptual and procedural understanding .


### Expected Outcomes  
Learners should produce:

- A fully functional and robust implementation of the 3×3 Tic-Tac-Toe game.  
- A modular program structured into coherent functions (e.g., board initialization, move validation, victory checking, game loop).  
- A clear and well-documented source code file or repository demonstrating correct use of lists/matrices, conditionals, loops, and parameters.  
- A practical demonstration showing the game executing correctly under different scenarios (valid moves, invalid moves, victories, draws).  
- An individual oral explanation that justifies design decisions, demonstrates authorship, and communicates the logic of the program using appropriate technical vocabulary.  
- Evidence of collaborative work during the development process, with equitable task distribution and respectful interaction.  


### Acquisition Context

This learning task is developed within the  Programming Logic  course of the  Integrated Technical Program in Informatics (1st year, IFBA – Valença Campus) . 

It is carried out in a hands-on  computer lab environment , supported by introductory instruction on structured programming (lists, matrices, loops, conditionals, functions).  

Students work in  pairs or trios  to develop the solution, but must individually defend and justify their program in an oral assessment.  

The context emphasizes the integration of conceptual knowledge, practical coding skills, ethical authorship, and communication abilities.  


### Target Audience Profile

- **Educational Level:** 1st-year students of an Integrated Technical Program in Informatics.  
- **Prior Knowledge:** Basic understanding of algorithms, variables, assignment, and simple input/output.  
- **Programming Experience:** Beginner level; early exposure to structured programming concepts.  
- **Learning Needs:** Clear examples, step-by-step guidance, practice with debugging, and opportunities to articulate reasoning.  
- **Expected Dispositions:** Willingness to collaborate, attention to detail, openness to feedback, and ethical engagement with shared work.  


### Proficiency Scale

Scores range from **0.0 to 10.0**, in increments of **0.1**, based on:

- **Technical correctness** (program runs, validates moves, detects outcomes).  
- **Conceptual understanding** (explanation of flow, structures, functions).  
- **Code quality and organization** (clarity, modularization, naming, structure).  
- **Problem-solving process** (debugging, testing, scenario analysis).  
- **Communication and authorship** (clarity, vocabulary, ethical justification).  
- **Collaboration** (evidence of equitable participation and responsibility).  



## 2. Knowledge Enumeration

### 2.1. Fundamentals of Programming

* **K1 – Concept of algorithm**

  * Notion of a finite sequence of instructions to solve a problem.

* **K2 – Basic data types and variables**

  * Integers, characters/strings; declaration, assignment, simple scope.

* **K3 – Input and output of data**

  * Reading user input; displaying messages and results.

### 2.2. Simple Data Structures

* **K4 – Lists and matrices (vectors and two-dimensional arrays)**

  * Index-based access; initialization and updating of positions.

* **K5 – State representation using data structures**

  * Modeling the game board as a data structure (matrix/list of lists).

### 2.3. Control Structures

* **K6 – Conditional structures (if/elif/else or equivalents)**

  * Use in validating moves; checking win/draw conditions.

* **K7 – Repetition structures (while/for)**

  * Control of the main game loop; repetition until the stopping condition.

### 2.4. Decomposition and Modularization

* **K8 – Functions/procedures with parameters and return values**

  * Definition, invocation, argument passing, return values.

* **K9 – Problem decomposition into subproblems**

  * Separating the problem into: board display, move reading, end-of-game checking, main loop.

### 2.5. Logical Reasoning and Debugging

* **K10 – Logical and relational operators**

  * Equality, inequality, conjunction/disjunction; use in conditional expressions.

* **K11 – Basic notions of testing and debugging**

  * Testing win cases in rows, columns, diagonals, and draw scenarios.

### 2.6. Collaborative and Ethical Aspects

* **K12 – Teamwork in software development**

  * Task division, communication, shared responsibility.



## 3. Learning Objectives Identification

> **By the end of the task, the learner should be able to:**

1. **LO1 – Describe** in natural language the general functioning of the Tic-Tac-Toe game and the flow of the program that implements it.

2. **LO2 – Represent** the board state using lists or matrices, explaining how indexes correspond to game positions.

3. **LO3 – Implement** conditional and repetition structures to control the game flow, ensuring player alternation and the stopping condition (win or draw).

4. **LO4 – Modularize** the program into cohesive functions (e.g., board display, move reading, win checking, main loop), justifying the decomposition adopted.

5. **LO5 – Validate** user input, rejecting invalid moves and providing adequate feedback through messages.

6. **LO6 – Test and debug** the program using different scenarios (row, column, diagonal wins; draw), identifying and correcting logical errors.

7. **LO7 – Explain orally** the functioning of the code, including the interaction between functions and the execution flow of a complete match.

8. **LO8 – Collaborate** with the group in building the solution, assuming responsibilities and contributing equitably.





## 4. Competency Definition


## Competência Geral (BNCC – Computação na Educação Básica)

* **Compreender, analisar, projetar e implementar soluções computacionais** para problemas do cotidiano, mobilizando conceitos de algoritmos, representação de dados e estruturas de controle, de forma ética, colaborativa e reflexiva.



###  Competency CT25.2.1 Specification  

### Competency Title
    Definir os requisitos da solução analisando criticamente situações do mundo real.

### Textual Description  

Esta competência envolve a capacidade de **analisar um problema computacional concreto** — neste caso, o jogo da velha — para identificar, compreender e especificar seus **requisitos funcionais e não funcionais** antes da implementação. 

O estudante deve observar o funcionamento lógico do jogo, reconhecer suas regras e restrições, e traduzi-las em requisitos claros que orientem o desenvolvimento do programa.

O processo inclui a **colaboração** entre os integrantes da dupla, o **raciocínio analítico** para decompor o problema e a **documentação organizada** das observações, de forma a garantir uma base sólida para o código a ser produzido.


### Knowledge Specification
The following knowledge areas are critical for this competency:

- **Pensamento Analítico (FPK)**
    - O estudante deve ser capaz de **aplica** o **pensamento analítico** para decompor o funcionamento do jogo em componentes lógicos observáveis, como jogadas, condições de vitória e controle de fluxo. Esse raciocínio permite compreender as relações de causa e efeito no comportamento do jogo e antecipar as decisões de projeto que deverão ser implementadas.

    - **Bloom’s Taxonomy Alignment**: Apply
    - **Knowledge-Skill Pairing**: Pensamento Analítico / Apply
    - **Verb Annotation**: Use, Employ

- **Colaboração (FPK)**
    - O estudante deve ser capaz de aplicar **estratégias colaborativas** para discutir, comparar e validar interpretações sobre o problema com o colega de dupla. Essa cooperação contribui para a construção coletiva dos requisitos e para a resolução de ambiguidades, simulando práticas profissionais de coautoria em engenharia de software.

    - **Bloom’s Taxonomy Alignment**: Apply
    - **Knowledge-Skill Pairing**: Colaboração / Apply
    - **Verb Annotation**: Use, Employ, Demonstrate

- **Especificação de Requisitos**
    - O estudante deve ser capaz de **realizar** a especificação de requisitos para expressar, de forma organizada e compreensível, as funcionalidades esperadas (ex.: entrada de jogadas, detecção de vitória, mensagem de empate) e restrições (ex.: jogadas válidas, limite de turnos) da solução. O foco é transformar observações empíricas do jogo em descrições estruturadas que servirão de guia para a codificação.

    - **Bloom’s Taxonomy Alignment**: Apply
    - **Knowledge-Skill Pairing**: Especificação de Requisitos / Apply
    - **Verb Annotation**: Execute, Perform


### Disposition Specification

* **Meticuloso** — demonstra atenção à organização e clareza ao representar dados, requisitos e observações, cuidando para que nenhum aspecto essencial do problema seja negligenciado.

* **Colaborativo** — contribui ativamente nas discussões, respeitando e integrando as ideias do parceiro, buscando um entendimento comum sobre os requisitos e a forma de expressá-los.


#### Competências associadas - BNCC

**Competência geral 1 – Computação (Ensino Médio)**

> “Compreender as possibilidades e os limites da Computação para resolver problemas (...), propondo e analisando soluções computacionais para diversos domínios do conhecimento” – C1 envolve exatamente analisar o problema (jogo da velha), levantar requisitos e pensar a solução computacional adequada.

**Competência geral 5 – Computação (Ensino Médio)**

> “Desenvolver projetos para investigar desafios do mundo contemporâneo, construir soluções (...), preferencialmente de maneira colaborativa” – a definição de requisitos é a etapa inicial do projeto de software em dupla, articulando análise, discussão e documentação.

**Competências específicas:**

* **EM13CO01** – “Explorar e construir a solução de problemas por meio da reutilização de partes de soluções existentes” – ao analisar o jogo, os estudantes podem se apoiar em padrões de solução já conhecidos (ex.: exemplos de pseudocódigo para jogos de tabuleiro) e adaptá-los.
* **EM13CO02** – “Explorar e construir a solução de problemas por meio de refinamentos, utilizando diversos níveis de abstração desde a especificação até a implementação” – C1 está no nível de especificação de requisitos, que depois será refinado em algoritmos e código.



### Summary Table for Competency CT25.2.1

| **Code**  | **Competency** | **Dispositions** | **Knowledge** | **Skill** |
|-----------|----------------|------------------|---------------|-----------|
|           |                |                  | Pensamento Analítico (FPK) | **Apply (Use, Employ)** |
| CT25.1.1  | **Definir os requisitos da solução analisando criticamente situações do mundo real.** | Collaborative, Responsible, Creative | Colaboração (FPK) | **Apply (Use, Employ, Demonstrate)**
|          | | | Especificação de Requisitos | **Apply (Execute, Perform)** |





### Competency CT25.2.2 Specification

### Competency Title

Organize and represent information in structured formats, including matrices, records, and lists.

### Textual Description

This competency involves the ability to **translate conceptual elements of the Tic-Tac-Toe game into appropriate data structures**, representing the board, the moves made, and the intermediate states of the match.

The learner must apply analytical reasoning to **model domain information** (players, moves, winning conditions) in computationally adequate formats, using **simple lists or nested lists (matrices)**.

Precision in data representation is essential to ensure that the game rules are correctly implemented and understood, while also supporting **maintainability and clarity of code**. Collaborative work contributes to validating the data model, discussing implementation alternatives, and verifying coherence with previously defined requirements.



### Knowledge Specification

The following knowledge areas are critical for this competency:

- **Data Structures**

    - The learner must be able to **apply** **data structures** to store the current state of the game. This includes understanding how to **access, modify, and display** data efficiently and legibly, ensuring consistency throughout gameplay.

    * **Bloom’s Taxonomy Alignment:** Apply
    * **Knowledge-Skill Pairing:** Data Structures / Apply
    * **Verb Annotation:** Use, Manipulate, Modify, Implement


- **Analytical Thinking (FPK)**

    - The learner must be able to **apply analytical thinking** to determine what information must be represented, how these elements relate (e.g., move position, symbol “X” or “O”, winning condition), and how these relationships influence operations on the data. This analysis guides the selection of adequate structures and prevents redundancies or logical inconsistencies.

    * **Bloom’s Taxonomy Alignment:** Apply
    * **Knowledge-Skill Pairing:** Analytical Thinking / Apply
    * **Verb Annotation:** Analyze, Distinguish, Organize, Compare



- **Information Modeling**

    - The learner must be able to **carry out information modeling**, structuring domain elements (board, moves, game states) in a computational representation that supports clear manipulation and processing throughout the program.

    * **Bloom’s Taxonomy Alignment:** Apply 
    * **Knowledge-Skill Pairing:** Information Modeling / Apply
    * **Verb Annotation:** Construct, Represent, Structure, Arrange



### Disposition Specification

* **Meticulous** — demonstrates attention to detail when organizing and representing data, avoiding indexing errors, inconsistent values, or confusion between game states.

* **Collaborative** — works cooperatively with teammates to validate the data structure, integrate different implementation ideas, and reach shared technical understanding.



### BNCC-Aligned Competencies

> **General Competency 1 – Computing (High School)**
Representing the board (lists, matrices) is part of proposing and analyzing **viable computational solutions** aligned with the problem's structure.

> **General Competency 4 – Computing (High School)**
“Build knowledge using computational techniques and technologies…” — the data model of the game (board, moves, states) is itself a computational artifact.

**Specific Competencies:**

* **EF15CO01** – Identify structured ways to organize and represent information, including matrices, records, lists, and graphs.
* **EF04CO01** – Recognize real or digital objects represented by matrices with coordinate-based positions.
* **EF07CO03** – Build computational solutions by selecting adequate data structures, individually or collaboratively.
* **EF09CO02** – Select appropriate data types and structures (such as vectors and matrices) for proposed situations.
* **EM13CO02** – Refine computational solutions across levels of abstraction, from conceptual modeling to implementation.



### Summary Table for Competency CT25.2.2

| **Code** | **Competency**                                                                                            | **Dispositions**          | **Knowledge**             | **Skill**                                            |
| -------- | --------------------------------------------------------------------------------------------------------- | ------------------------- | ------------------------- | ---------------------------------------------------- |
| CT25.2.2 | **Organize and represent information in structured formats (matrices, records, lists).** | Meticulous, Collaborative | Data Structures     | **Apply (Use, Manipulate, Modify, Implement)**       |
|          |                                                                                                           |                           | Analytical Thinking (FPK) | **Apply (Analyze, Distinguish, Organize, Compare)**  |
|          |                                                                                                           |                           | Information Modeling      | **Apply (Construct, Represent, Structure, Arrange)** |





### Competency CT25.2.3 Specification

### Competency Title

Apply conditional structures and loops, in creative and inventive ways, to control program flow.

### Textual Description

This competency refers to the ability to **control the dynamic behavior of the Tic-Tac-Toe game** through the combined use of conditional structures and repetition constructs. The learner must understand and apply **decision and iteration commands** to manage turns, validate moves, and determine victory or draw conditions, ensuring that the game behaves consistently from beginning to end.

Beyond applying these concepts correctly, learners are expected to **explore creative and inventive solutions**, seeking to simplify code, reduce redundancy, and anticipate potential logical exceptions.
**Meticulousness** is essential to avoid logical errors and ensure correct gameplay flow, while **collaboration** enables collective refinement of control strategies and debugging practices.



### Knowledge Specification

The following knowledge areas are critical for this competency:


- **Conditional Structures (if, elif, else)**

    - The learner must be able to apply **conditional structures** to control decisions within the game, such as verifying whether a move is valid, identifying a winner, or detecting a draw. This requires translating the rules of the game into clear logical conditions that ensure each scenario is treated correctly in the program flow.

    * **Bloom’s Taxonomy Alignment:** Apply
    * **Knowledge-Skill Pairing:** Conditional Structures / Apply
    * **Verb Annotation:** Use, Implement, Determine, Evaluate, Select



- **Repetition Structures (while, for)**

    -   The learner must apply **loops** to construct the continuous cycle of the game, allowing moves to repeat until a termination condition (victory or draw) is met. This includes managing the number of turns, alternating players, and ensuring that the loop respects all defined rules.

    * **Bloom’s Taxonomy Alignment:** Apply
    * **Knowledge-Skill Pairing:** Repetition Structures / Apply
    * **Verb Annotation:** Execute, Iterate, Repeat, Cycle, Maintain


- **Relational and Logical Operators**

    - The learner must apply **relational and logical operators** to express decision and repetition conditions, composing Boolean expressions that evaluate game states (e.g., “all three positions are equal” or “there are empty spaces available”). These operators ensure **precision in decision making** and efficiency in program flow control.

    * **Bloom’s Taxonomy Alignment:** Apply
    * **Knowledge-Skill Pairing:** Logical Reasoning / Apply
    * **Verb Annotation:** Compare, Test, Validate, Combine, Construct (Boolean expressions)


### Disposition Specification

* **Creative (innovative)** — demonstrates initiative in exploring different ways to structure the code, proposing alternative solutions and improvements to program flow.
* **Inventive (exploratory)** — tests new approaches, experiments iteratively, and adjusts code based on observations and results.
* **Meticulous** — maintains constant attention to logical coherence, avoiding contradictions, unnecessary repetition, or control-flow failures that might compromise execution.
* **Collaborative** — works actively with teammates, discussing control strategies and jointly verifying the correct behavior of conditional and iterative structures.



### BNCC-Aligned Competencies

> **General Competency 1 (High School)**
Using conditionals and loops in the game implementation operationalizes the ability to **apply algorithms and control structures** to real problems.

> **General Competency 5 (High School)**
Developing computational projects that address real-world challenges — here represented by the need to **control interactive flow** in a robust manner.

**Specific Competencies:**

* **EF15CO02** – Develop and simulate algorithms involving sequences, selections, and repetitions.
* **EF03CO02** – Work with simple conditional repetitions in algorithms (e.g., “repeat while the game has no winner”).
* **EF04CO03** – Elaborate algorithms involving simple and nested repetitions.
* **EF69CO02** – Create algorithms using selection and repetition structures across different programming languages.



### Summary Table for Competency CT25.2.3

| **Code** | **Competency**                                                                                   | **Dispositions**                               | **Knowledge**                | **Skill**                                               |
| -------- | ------------------------------------------------------------------------------------------------ | ---------------------------------------------- | ---------------------------- | ------------------------------------------------------- |
| CT25.2.3 | **Apply conditional structures and loops, creatively and inventively, to control program flow.** | Creative, Inventive, Meticulous, Collaborative | Conditional Structures       | **Apply (Use, Implement, Determine, Evaluate, Select)** |
|          |                                                                                                  |                                                | Repetition Structures        | **Apply (Execute, Iterate, Repeat, Cycle, Maintain)**   |
|          |                                                                                                  |                                                | Logical/Relational Operators | **Apply (Compare, Test, Validate, Combine, Construct)** |





### Competency CT25.2.4 Specification

### Competency Title

Modularize the code, meticulously dividing responsibilities into independent functions.

### Textual Description

This competency involves the ability to **structure programs in a modular way**, decomposing the problem into specific and reusable functions, each responsible for a clearly defined part of the game.
The learner must be able to **create functions** with appropriate parameters and return values, understand the **scope of variables**, and organize program flow so that each component can be understood, tested, and modified in isolation.

Modularization reflects **maturity in computational reasoning**, enabling clarity, reusability, and maintainability of the code.
Meticulous behavior ensures precise and coherent implementation of functions, while collaboration enables the harmonious integration of the components produced by different team members.



### Knowledge Specification

- **Functions, Parameters, and Return Values**

    - The learner must be able to **create specific functions** that encapsulate distinct responsibilities within the program, such as initializing the board, checking winning conditions, or printing the current game state. This process requires defining **adequate parameters**, understanding data flow between functions, and planning consistent return values that support the logic of the program.

    * **Bloom’s Taxonomy Alignment:** Create
    * **Knowledge-Skill Pairing:** Function Design / Create
    * **Verb Annotation:** Create, Construct, Design, Develop, Compose



- **Variable Scope**

    - The learner must correctly apply the concept of **scope**, distinguishing between local and global variables to avoid naming conflicts and unexpected behavior. This demonstrates mastery over **visibility and lifetime** of variables within functional contexts, ensuring integrity and predictability of the code.

    * **Bloom’s Taxonomy Alignment:** Apply
    * **Knowledge-Skill Pairing:** Variable Scope / Apply
    * **Verb Annotation:** Apply, Utilize, Implement, Differentiate, Maintain


### Disposition Specification

* **Meticulous** — demonstrates careful attention to detail in defining functions, parameters, and return values, ensuring semantic consistency and minimizing errors or redundancy.

* **Collaborative** — actively participates in the division of responsibilities and integration of program functions, communicating clearly and constructively to guarantee coherence in the final code.


### BNCC-Aligned Competencies

> **General Competency 4 (High School)**
Build knowledge in Computing by applying techniques and technologies to produce artifacts — modularization is essential for scalable, organized projects.

> **General Competency 5 (High School)**
Develop computational projects addressing real-world challenges — larger projects require modular design to support teamwork and maintainability.

**Specific Competency:**

* **EM13CO02** – Refine computational solutions across multiple abstraction levels, including decisions about **how to decompose a program into functions** and how those components communicate.



### Summary Table for Competency CT25.2.4

| **Code** | **Competency**                                                                   | **Dispositions**          | **Knowledge**                        | **Skill**                                                      |
| -------- | -------------------------------------------------------------------------------- | ------------------------- | ------------------------------------ | -------------------------------------------------------------- |
| CT25.2.4 | **Modularize the code by dividing responsibilities into independent functions.** | Meticulous, Collaborative | Functions, Parameters, Return Values | **Create (Create, Construct, Design, Develop, Compose)**       |
|          |                                                                                  |                           | Variable Scope                       | **Apply (Apply, Utilize, Implement, Differentiate, Maintain)** |



### Competency CT25.2.5 Specification

### Competency Title

Justify the authorship of computational solutions in an ethical, clear, and well-founded manner.

### Textual Description

This competency involves the ability to **explain and defend one’s own computational solution**, demonstrating conceptual mastery, clear communication, and ethical responsibility.
During the oral assessment, the learner must be able to **understand technical vocabulary**, **apply logical reasoning** to justify implementation decisions, and **communicate orally** in a structured and well-founded manner.

The competency reflects not only cognitive understanding but also the learner’s **ethical commitment to authorship** and respectful, collaborative communication in academic settings.



### Knowledge Specification


- **Programming Technical Vocabulary**

    - The learner must understand the meaning and use of **technical programming vocabulary**, recognizing essential terms and concepts such as function, loop, logical condition, and variable. This understanding allows learners to interpret and explain parts of the code and the decisions made during development.

    * **Bloom’s Taxonomy Alignment:** Understand
    * **Knowledge-Skill Pairing:** Technical Vocabulary / Understand
    * **Verb Annotation:** Explain, Interpret, Describe, Summarize, Clarify


- **Logical Reasoning**

    - The learner must apply **logical reasoning** to justify the sequence of operations in the code, demonstrating coherence between problem requirements and the implemented structure. This includes **making grounded arguments** that connect cause and effect between algorithmic decisions and resulting behaviors.

    * **Bloom’s Taxonomy Alignment:** Apply
    * **Knowledge-Skill Pairing:** Logical Reasoning / Apply
    * **Verb Annotation:** Apply, Demonstrate, Justify, Connect, Support



- **Oral Communication**

    - The learner must apply **oral communication skills** to describe the solution clearly, logically, and accessibly. This includes proper use of technical terminology, coherent sequencing of ideas, and the ability to respond to questions confidently and accurately.

    * **Bloom’s Taxonomy Alignment:** Apply
    * **Knowledge-Skill Pairing:** Oral Communication / Apply
    * **Verb Annotation:** Communicate, Present, Articulate, Respond, Elaborate



### Disposition Specification

* **Ethical** — acknowledges authorship, avoids plagiarism, and demonstrates intellectual honesty when presenting contributions and limitations.

* **Communicative** — expresses ideas clearly, objectively, and coherently, supporting mutual understanding and constructive dialogue.

* **Responsible** — commits to delivering accurate explanations and truthful representations of the solution, demonstrating maturity and professionalism.



### BNCC-Aligned Competencies

> **General Competency 4 (High School)**
Emphasizes producing computational artifacts considering **quality, communication, and critical reflection**.

> **General Competency 6 (High School)**
Express, represent, and communicate information and ideas clearly using computational objects and diverse languages — directly aligned with oral explanation of code.

> **General Competency 7 (High School)**
Act ethically, responsibly, and with commitment to the common good — foundational for the dispositions *Ethical* and *Responsible*.

**Specific Competencies:**

* **EM13CO19** – Present, argue, and negotiate computational solution proposals in collaborative contexts — mapped to **oral justification of code**.

* **EM13CO21** – Communicate complex ideas through computational artifacts, considering different audiences and languages — directly related to explaining a Tic-Tac-Toe program clearly and rigorously.



### Summary Table for Competency CT25.2.5

| **Code** | **Competency**                                                           | **Dispositions**                    | **Knowledge**        | **Skill**                                                         |
| -------- | ------------------------------------------------------------------------ | ----------------------------------- | -------------------- | ----------------------------------------------------------------- |
| CT25.2.5 | **Justify authorship of computational solutions ethically and clearly.** | Ethical, Communicative, Responsible | Technical Vocabulary | **Understand (Explain, Interpret, Describe, Summarize, Clarify)** |
|          |                                                                          |                                     | Logical Reasoning    | **Apply (Apply, Demonstrate, Justify, Connect, Support)**         |
|          |                                                                          |                                     | Oral Communication   | **Apply (Communicate, Present, Articulate, Respond, Elaborate)**  |


