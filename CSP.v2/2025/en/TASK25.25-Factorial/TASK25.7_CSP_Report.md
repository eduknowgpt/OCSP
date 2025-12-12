# **Competency Specification Report: Task25.7 – Cálculo de Fatoriais com Funções e Estruturas de Repetição**

## **Introdução**

Este relatório apresenta a aplicação da **fase de Autoria de Competências** do **Competency Specification Process (CSP)** à *Task25.7 – Cálculo de Fatoriais com Funções e Estruturas de Repetição*, uma atividade típica da disciplina **Introdução à Programação**, cujo foco é a implementação de funções, o uso de laços de repetição e a construção de soluções modulares.

A tarefa solicita que os aprendizes desenvolvam um programa capaz de receber uma quantidade *n* de valores, ler cada um deles individualmente e calcular o seu fatorial por meio de uma **função implementada pelos próprios estudantes**. O exercício envolve, portanto, conhecimentos fundamentais da Computação, incluindo definição de variáveis, controle de fluxo, repetição, modularização e validação de dados.

A seguir, apresenta-se o relatório estruturado conforme as fases do CSP.

---

# **1. Análise de Entidades Instrucionais**

### **1.1 Título da Tarefa**

Cálculo de Fatoriais com Funções e Estruturas de Repetição.

### **1.2 Descrição da Tarefa**

Os aprendizes devem implementar um programa que:

1. Leia um número inteiro *n*, indicando a quantidade de valores a serem processados.
2. Leia *n* valores inteiros (um por vez).
3. Para cada valor, calcule o fatorial utilizando uma função previamente implementada.
4. Valide entradas negativas, solicitando nova entrada sempre que necessário.
5. Exiba o resultado no formato "x! = resultado".

A solução deve obrigatoriamente empregar uma **função** para o cálculo de fatorial, reforçando o princípio de modularização.

### **1.3 Processo de Desenvolvimento Esperado**

O aprendiz deve ser capaz de:

* **Analisar as restrições do problema**: quantidade de números, domínio válido, necessidade de função.
* **Identificar entradas e saídas**: valores inteiros e resultados fatoriais.
* **Selecionar variáveis adequadas** e estruturar o fluxo do programa.
* **Aplicar estruturas de repetição** para percorrer os valores a serem processados.
* **Implementar a função de fatorial**, garantindo correção lógica.
* **Validar entradas negativas**, garantindo robustez do programa.
* **Testar, simular e depurar** a solução.

### **1.4 Resultados Esperados**

Os estudantes devem ser capazes de:

* Produzir um código limpo, modular, correto e legível.
* Modelar soluções simples com uso adequado de funções e laços.
* Testar entradas variadas e interpretar resultados.
* Corrigir erros decorrentes de validação ou lógica de repetição.

### **1.5 Contexto de Aquisição**

* **Disciplina**: Introdução à Programação.
* **Tipo de atividade**: Avaliação ou exercício estruturado.
* **Ambiente**: Laboratório de programação com feedback imediato.

### **1.6 Perfil do Público-Alvo**

* **Nível**: Estudantes do 1º semestre da graduação em Ciência da Computação.
* **Experiência prévia**: Noções iniciais de algoritmos, controle de fluxo e operações matemáticas simples.
* **Funções esperadas**: Projetar pequenas soluções computacionais que combinem repetição, seleção e modularização.

### **1.7 Escala de Proficiência**

Escala numérica de **0 a 100**, compatível com o sistema avaliativo da disciplina (por exemplo, nota 8,5 → 85).

---

# **2. Enumeração de Conhecimento**

A identificação do conhecimento necessário utiliza a **BNCC – Computação na Educação Básica** como vocabulário controlado, complementada pelos conhecimentos estruturantes da programação.

### **2.1 Conhecimento de Computação (BNCC)**

* **Reconhecimento e formulação de problemas**
  – analisar o problema e propor solução computacional;
  – identificar dados de entrada e saída.

* **Representação e manipulação de dados**
  – definir variáveis adequadas;
  – trabalhar com tipos inteiros e operações aritméticas.

* **Controle de Fluxo**
  – aplicar estruturas condicionais;
  – utilizar estruturas de repetição (laço contado).

* **Abstração e Modularização**
  – funções;
  – decomposição de problemas.

### **2.2 Conhecimento Profissional (FPK – CC2020)**

* **Pensamento Analítico e Crítico**
  – decompor problemas;
  – avaliar resultados e tomar decisões fundamentadas.

Essa enumeração garante rastreabilidade semântica para a definição posterior da(s) competência(s).

---

# **3. Identificação dos Objetivos de Aprendizagem**

Os Objetivos de Aprendizagem foram derivados dos conhecimentos identificados e do comportamento esperado do aluno.

### **Objetivo Geral**

Desenvolver uma solução computacional modular que receba múltiplos valores e compute o fatorial de cada um utilizando uma função.

### **Objetivos Específicos**

1. Analisar o problema, identificando suas restrições e requisitos.
2. Identificar corretamente entradas e saídas.
3. Declarar variáveis necessárias à solução.
4. Utilizar estruturas condicionais para validação de dados.
5. Aplicar estruturas de repetição para processamento dos valores.
6. Implementar funções para modularizar a solução.
7. Descrever e automatizar a solução em uma linguagem de programação.

Esses objetivos guiam a especificação das competências na seção seguinte.

---


## **4. Competency Definition**

## **General Competency (BNCC – Computing in Basic Education)**

* **Understand, design, and implement modular computational solutions** for mathematical problems, mobilizing concepts of data representation, control structures, and functions in an ethical, rigorous, and reflective manner.

Nesta tarefa, isso se concretiza na capacidade de projetar e implementar um programa que calcula o **fatorial de múltiplos valores**, utilizando **funções** e **estruturas de repetição**, com validação de entradas e atenção à clareza do código.

---

### **Competency CT25.7.1 Specification**

### **Competency Title**

> Analyze the factorial problem and specify inputs, outputs, and constraints for the solution.

### **Textual Description**

This competency involves the ability to **analyze the concrete computational problem of calculating factorials for multiple values** in order to identify, interpret, and specify its **inputs, outputs, and operational constraints** before implementation.

The learner must understand the mathematical definition of the factorial function, recognize which data will be provided by the user (e.g., the number of values *n* and each individual integer), and determine the expected outputs (e.g., `x! = result`).

The process includes **interpreting the constraints** (e.g., non-negative integers only), **structuring the problem** as a relation between input and output, and **documenting** these requirements in a way that guides the subsequent design of loops and functions.

### **Knowledge Specification**

The following knowledge areas are critical for this competency:

---

* **Analytical Thinking (FPK)**

  * The learner must be able to **apply analytical thinking** to decompose the factorial problem into its fundamental components: identify the mathematical rule (n!), domain restrictions (n ≥ 0), and the need to process *n* different input values. This supports a clear understanding of what the program must do before any code is written.

  * **Bloom’s Taxonomy Alignment:** Apply

  * **Knowledge-Skill Pairing:** Analytical Thinking / Apply

  * **Verb Annotation:** Analyze, Distinguish, Interpret, Organize

---

* **Problem Analysis and Requirement Identification (BNCC – EF06CO05, EF06CO06)**

  * The learner must be able to **identify inputs and outputs** and **formulate the problem** as a computational task. This includes clarifying that the program must receive a quantity *n*, then *n* integers, and produce the factorial of each, respecting validity constraints (non-negative numbers).

  * **Bloom’s Taxonomy Alignment:** Understand → Apply

  * **Knowledge-Skill Pairing:** Problem Analysis / Apply

  * **Verb Annotation:** Identify, Determine, Specify, Describe

---

* **Mathematical Concept of Factorial**

  * The learner must understand the **mathematical definition of factorial** (n!) and its iterative nature (1 × 2 × … × n). This understanding is essential to map the abstract concept into a correct computational process.

  * **Bloom’s Taxonomy Alignment:** Understand

  * **Knowledge-Skill Pairing:** Mathematical Foundations / Understand

  * **Verb Annotation:** Explain, Interpret, Relate

---

### **Disposition Specification**

* **Meticulous** — pays attention to details when defining the domain of input values, constraints (non-negative integers), and expected outputs, avoiding ambiguous or incomplete specifications.
* **Responsible** — assumes responsibility for clearly stating what the program must do, understanding that imprecise requirements lead to incorrect implementations.

---

### **BNCC-Aligned Competencies**

> **General Competency 1 – Computing (High School)**
> “Understand the possibilities and limits of Computing to solve problems (...), proposing and analyzing computational solutions for various domains of knowledge.”
> Here, the student analyzes a **mathematical problem (factorial)** and specifies how it will be treated computationally.

> **Specific Competencies (examples):**
> **EF06CO05, EF06CO06** – Identify inputs and outputs, and formulate generalized solutions for classes de problemas.

---

### **Summary Table for Competency CT25.7.1**

| **Code** | **Competency**                                                                                   | **Dispositions**        | **Knowledge**                          | **Skill**                                             |
| -------- | ------------------------------------------------------------------------------------------------ | ----------------------- | -------------------------------------- | ----------------------------------------------------- |
| CT25.7.1 | **Analyze the factorial problem and specify inputs, outputs, and constraints for the solution.** | Meticulous, Responsible | Analytical Thinking (FPK)              | **Apply (Analyze, Distinguish, Interpret, Organize)** |
|          |                                                                                                  |                         | Problem Analysis & Requirements (BNCC) | **Apply (Identify, Determine, Specify, Describe)**    |
|          |                                                                                                  |                         | Mathematical Concept of Factorial      | **Understand (Explain, Interpret, Relate)**           |

---

### **Competency CT25.7.2 Specification**

### **Competency Title**

> Apply loops and conditional validation to process multiple numeric inputs for factorial computation.

### **Textual Description**

This competency involves the ability to **control the program flow** that processes *n* input values and computes the factorial of each, combining **repetition** and **decision structures**.

The learner must be able to **use loops** (e.g., `for`, `while`) to read multiple numeric inputs and iteratively compute the factorial, while simultaneously **applying conditional structures** to validate the values (e.g., rejecting negative numbers and requesting new input).

This includes composing **Boolean expressions** to check validity, ensuring that the program behaves reliably even when faced with incorrect or unexpected input.

Precise use of control flow and validation is essential to guarantee robustness, correctness, and user-friendly behavior.

### **Knowledge Specification**

The following knowledge areas are critical for this competency:

---

* **Repetition Structures (Loops)**

  * The learner must be able to **apply loops** to:

    * iterate over the *n* inputs;
    * perform the iterative multiplication that defines the factorial (1, 2, …, n).

  * **Bloom’s Taxonomy Alignment:** Apply

  * **Knowledge-Skill Pairing:** Repetition Structures / Apply

  * **Verb Annotation:** Execute, Iterate, Repeat, Cycle, Maintain

---

* **Conditional Structures and Data Validation**

  * The learner must be able to **use conditional structures** to validate inputs and handle exceptional cases (e.g., negative numbers). This includes deciding whether to accept a value, request another, or show an error message, ensuring that only valid numbers are processed.

  * **Bloom’s Taxonomy Alignment:** Apply

  * **Knowledge-Skill Pairing:** Conditional Structures & Validation / Apply

  * **Verb Annotation:** Use, Implement, Determine, Check, Validate

---

* **Relational and Logical Operators**

  * The learner must apply **relational and logical operators** (`<`, `>=`, `==`, `&&`, etc.) to express validation conditions (e.g., “x ≥ 0”), constructing accurate Boolean expressions that guide decision-making.

  * **Bloom’s Taxonomy Alignment:** Apply

  * **Knowledge-Skill Pairing:** Logical Reasoning / Apply

  * **Verb Annotation:** Compare, Test, Validate, Combine, Construct (conditions)

---

### **Disposition Specification**

* **Meticulous** — keeps careful attention to correctness in conditional and loop conditions, avoiding off-by-one errors, infinite loops, or missing validations.
* **Resilient** — perseveres through debugging typical control-flow errors (e.g., wrong loop limits, invalid conditions) until the program behaves correctly.
* **Responsible** — recognizes the importance of validating user input to ensure safe and reliable program execution.

---

### **BNCC-Aligned Competencies**

> **General Competency 1 – Computing**
> Application of algorithms and control structures to concrete problems, ensuring correct and safe behavior.

**Specific Competencies (examples):**

* **EF15CO02** – Develop algorithms involving sequences, selections, and repetitions.
* **EF06CO02** – Elaborate algorithms using repetition and selection.
* **EF69CO02** – Create algorithms using selection and repetition in different programming environments.

---

### **Summary Table for Competency CT25.7.2**

| **Code** | **Competency**                                                                                           | **Dispositions**                   | **Knowledge**                       | **Skill**                                               |
| -------- | -------------------------------------------------------------------------------------------------------- | ---------------------------------- | ----------------------------------- | ------------------------------------------------------- |
| CT25.7.2 | **Apply loops and conditional validation to process multiple numeric inputs for factorial computation.** | Meticulous, Resilient, Responsible | Repetition Structures               | **Apply (Execute, Iterate, Repeat, Cycle, Maintain)**   |
|          |                                                                                                          |                                    | Conditional Structures & Validation | **Apply (Use, Implement, Determine, Check, Validate)**  |
|          |                                                                                                          |                                    | Relational/Logical Operators        | **Apply (Compare, Test, Validate, Combine, Construct)** |

---

### **Competency CT25.7.3 Specification**

### **Competency Title**

> Design, implement, and test a modular factorial function to be reused in the program.

### **Textual Description**

This competency involves the ability to **structure the solution in a modular way**, encapsulating the factorial computation inside a **reusable function** that receives a parameter and returns the computed result.

The learner must be able to **design the function interface** (parameter type, return type), implement its internal logic (iterative or recursive), and **integrate** the function into the main program, calling it for each valid input.

Additionally, the learner is expected to **test and debug** the factorial function with different values (e.g., 0, 1, n > 1, bigger numbers), ensuring that the result is correct, that corner cases are handled, and that the function can be reused safely in other contexts.

### **Knowledge Specification**

The following knowledge areas are critical for this competency:

---

* **Functions, Parameters, and Return Values**

  * The learner must be able to **design and implement functions** that encapsulate the factorial logic, carefully choosing parameters (e.g., integer *x*) and return types (e.g., integer or long). This includes understanding how data flows into and out of the function.

  * **Bloom’s Taxonomy Alignment:** Create

  * **Knowledge-Skill Pairing:** Function Design / Create

  * **Verb Annotation:** Create, Construct, Design, Develop, Compose

---

* **Decomposition and Modularization**

  * The learner must be able to **decompose the problem** by separating the concerns: the main program is responsible for reading inputs and controlling the loop, while the factorial function is responsible only for the mathematical computation. This modularization favors reusability and clarity.

  * **Bloom’s Taxonomy Alignment:** Analyze → Create

  * **Knowledge-Skill Pairing:** Modularization / Create

  * **Verb Annotation:** Decompose, Structure, Organize, Integrate

---

* **Testing and Debugging**

  * The learner must be able to **test the factorial function** with different inputs and debug potential errors (off-by-one errors, incorrect initialization, etc.), verifying correctness and stability.

  * **Bloom’s Taxonomy Alignment:** Apply

  * **Knowledge-Skill Pairing:** Testing & Debugging / Apply

  * **Verb Annotation:** Test, Verify, Correct, Refine

---

### **Disposition Specification**

* **Meticulous** — carefully defines parameters, return types, and internal logic of the function, avoiding ambiguous behavior.
* **Persistent** — persists through debugging and refinement cycles until the function behaves correctly for all relevant test cases.
* **Collaborative** (if in pairs/groups) — discusses modularization choices and test cases with peers, integrating feedback to improve design.

---

### **BNCC-Aligned Competencies**

> **General Competency 4 – Computing (High School)**
> Building computational artifacts using appropriate techniques and technologies — here, the factorial function is a modular artifact.

> **General Competency 5 – Computing (High School)**
> Develop computational projects for real-world problems — modularization is essential to scalable and maintainable projects.

**Specific Competencies (examples):**

* **EF06CO02, EF06CO03** – Elaborate and describe algorithms and programs that implement solutions using selection and repetition.
* **EF06CO04** – Build solutions using decomposition and automate them via programming.
* **EM13CO02** – Refine computational solutions at multiple abstraction levels, including how to decompose into functions.

---

### **Summary Table for Competency CT25.7.3**

| **Code** | **Competency**                                                                            | **Dispositions**                      | **Knowledge**                        | **Skill**                                                |
| -------- | ----------------------------------------------------------------------------------------- | ------------------------------------- | ------------------------------------ | -------------------------------------------------------- |
| CT25.7.3 | **Design, implement, and test a modular factorial function to be reused in the program.** | Meticulous, Persistent, Collaborative | Functions, Parameters, Return Values | **Create (Create, Construct, Design, Develop, Compose)** |
|          |                                                                                           |                                       | Decomposition & Modularization       | **Create (Decompose, Structure, Organize, Integrate)**   |
|          |                                                                                           |                                       | Testing & Debugging                  | **Apply (Test, Verify, Correct, Refine)**                |


