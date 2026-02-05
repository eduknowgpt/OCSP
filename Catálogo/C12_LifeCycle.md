## Competency Lifecycle - C12 - *Develop problem-solving solutions using Pushdown Automata*


## 1. Definição Original — *CSP-Report (Ciclo 1)*

A competência C12 emerge da **limitação identificada no uso de Autômatos Finitos** para resolver o problema de navegação reversa do *Farmer Robot*. A necessidade de **memória auxiliar para registrar e reproduzir trajetos** motivou a adoção de **Pushdown Automata (PDA)** como modelo computacional mínimo adequado para o problema.

Essa transição conceitual — de FSM para PDA — constitui o **evento gerador** da competência, ancorado diretamente no desafio central da tarefa: permitir que o robô **retorne ao ponto inicial após a execução de uma sequência arbitrária de movimentos**.

Na Fase 1A do CSP, o escopo da competência foi delimitado para evitar generalizações indevidas. A análise dos requisitos do problema levou às seguintes decisões estruturais:

* O foco da competência é **modelagem e solução de problemas**, não apenas compreensão teórica.
* O modelo computacional central é o **Pushdown Automaton**, devido ao uso explícito de **pilha para memória de percurso**.
* A competência exige **integração entre requisitos do domínio (navegação robótica)** e **formalismo computacional**.

Essa etapa estabelece que C12 opera no **nível de criação/aplicação**, e não apenas no nível conceitual.



### Primeira Especificação (CSP Phase 1B: Competency Authoring)

Durante a **Competency Authoring Phase**, C12 foi formalizada com a seguinte estrutura:

### Competency C12 Specification

#### Competency Title

  Develop problem-solving solutions using Pushdown Automata

#### Textual Description

Design and implement a Pushdown Automaton (PDA) capable of representing a navigation strategy for a robotic system, focusing on the return path after food delivery. The solution must simulate how memory structures enable backtracking and route inference.

### Knowledge Specification

The following knowledge areas are essential for mastering this competency:

* **Pushdown Automata and Finite Automata**
  *Understand the principles of state-based computation with memory, focusing on stack operations, transition functions, and language recognition. Apply this knowledge to simulate navigation behavior that requires remembering and reversing sequences.*

* **Requirements Analysis**
  *Identify, structure, and formalize behavioral requirements derived from task analysis. Translate real-world navigation goals into functional and non-functional requirements relevant to PDA design.*

* **Analytical and Critical Thinking**
  *Use systematic reasoning and problem decomposition to model navigation logic. Evaluate design alternatives and justify modeling choices based on behavioral constraints and system goals.*


### Disposition Specification

Effective engagement with this task requires the following behavioral dispositions:

* **Inventive** – Propose novel approaches to modeling navigation logic using PDAs.
* **Collaborative** – Work effectively in teams to refine shared solutions.
* **Responsible** – Demonstrate accountability in modeling decisions and validation.
* **Proactive** – Anticipate challenges in model behavior and adjust accordingly.
* **Creative** – Construct innovative solutions that go beyond straightforward implementations.



### Knowledge–Skill Pairing

#### Mapping Knowledge to Skills

To demonstrate this competency, students must be able to:

* Apply knowledge of **Pushdown Automata** to **develop** navigation strategies that require memory and backtracking, simulating return paths using stack-based logic.

* **Apply** knowledge of **Requirements Analysis** to extract, structure, and prioritize behavioral specifications aligned with the robot’s goals.

* **Employ** **Analytical and Critical Thinking** to deconstruct complex task requirements, evaluate the adequacy of models, and refine solutions through iterative reasoning.



#### Bloom’s Taxonomy Alignment

The primary cognitive processes involved in this competency are aligned with the following Bloom’s levels:

* **Create** – For using PDA concepts in system modeling developing a solution to the Return of the Farm Robot problem.


#### Verb Annotation

To provide clarity on competency expectations, the following verb annotations define the required actions:

* **Create** → Pushdown Automata → *Design, Develop, Construct*
* **Apply** → Requirements Analysis → *Interpret, Specify, Translate*



#### Summary Table for Competency C12

| **Competency**                                            | **Dispositions**                                               | **Knowledge**                          | **Skill**                  |
| --------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------- | -------------------------- |
| Develop problem-solving solutions using Pushdown Automata | Inventive, Collaborative, Responsible, Proactive, Creative | Finite Automata                      | **Create (Design, Develop, Construct)** |
|                                                           |                                                                | Requirements Analysis               | **Apply (Interpret, Specify, Translate)**             |
|                                                           |                                                                | Analytical and Critical Thinking (FPK) | **Apply**                  |



## **2. Revisões — *CSRP-Report (Ciclo 1 — Revisão por Especialistas)***

Durante a **Revisão por Especialistas (CSRP – Ciclo 1)**, a competência **C12** foi avaliada como **teoricamente consistente e alinhada ao escopo da tarefa**, porém foram identificados **ajustes necessários para aumentar sua precisão conceitual e coerência cognitiva**. As principais recomendações foram:

* **Realinhamento do modelo computacional**
  Substituição explícita e definitiva de **Finite Automata** por **Pushdown Automata (PDA)**, assegurando correspondência entre o **poder expressivo do modelo** e os **requisitos de memória** impostos pelo problema de retorno de navegação.

* **Fortalecimento da vinculação conhecimento–contexto**
  Tornar explícita a relação entre **operações de pilha** e o mecanismo de **registro e reversão de trajetos**, elemento central para a resolução do problema proposto.

* **Refinamento cognitivo e operacional**
  Ajustar os **verbos de ação** e os **pares conhecimento–habilidade** para refletir adequadamente níveis superiores da Taxonomia de Bloom — **Apply** e **Create** — evitando caracterizações restritas ao nível **Understand**, incompatíveis com as exigências de modelagem e construção efetiva da solução.

A incorporação dessas recomendações resultou na **estabilização conceitual da competência C12**, eliminando ambiguidades quanto ao **modelo computacional adotado**, ao **papel funcional do conhecimento declarado** e ao **nível cognitivo efetivamente mobilizado** no desempenho esperado dos estudantes.



## **3. Alterações Implementadas — *CSP-Adjustments***

Com base nas recomendações consolidadas no **CSRP-Report (Ciclo 1)**, foram realizadas **alterações pontuais e estruturantes** na especificação da competência **C12**, com o objetivo de assegurar **alinhamento conceitual**, **coerência cognitiva** e **adequação pedagógica** ao contexto da tarefa *Task 04 – The Return of the Farmer Robot*. As principais alterações implementadas são descritas a seguir.

### **3.1 Realinhamento do Modelo Computacional**

Todas as referências a **Finite Automata** foram **removidas ou substituídas** por **Pushdown Automata (PDA)** na especificação da competência C12. Esse ajuste garante:

* Correspondência direta entre o **modelo computacional declarado** e o **comportamento requerido** pelo problema;
* Adequação do formalismo à necessidade de **memória auxiliar baseada em pilha**;
* Eliminação de inconsistências conceituais previamente identificadas pelos especialistas.

Esse realinhamento estabelece o **PDA como o núcleo teórico-operacional** da competência.



### **3.2 Refinamento dos Componentes de Conhecimento**

Os componentes de conhecimento associados à C12 foram **revisados e refinados** para aumentar sua **granularidade funcional** e **relevância instrucional**. Em particular:

* O conhecimento de **Pushdown Automata** passou a enfatizar explicitamente:

  * operações de pilha (push, pop, símbolo de base);
  * transições dependentes de estado, entrada e pilha;
  * relação entre percurso de ida e retorno.

* **Análise de Requisitos** foi mantida e explicitamente conectada à:

  * identificação de restrições de navegação;
  * tradução de objetivos do domínio em especificações formais.

* **Pensamento Analítico e Crítico** foi reposicionado como conhecimento transversal de suporte à:

  * decomposição do problema;
  * avaliação de alternativas de modelagem;
  * refinamento iterativo da solução.



### **3.3 Ajuste dos Pares Conhecimento–Habilidade**

Os pares conhecimento–habilidade foram **reformulados** para refletir de forma mais fiel o **desempenho esperado do estudante**. As principais alterações incluem:

* Associação explícita de **Pushdown Automata** ao nível **Create**, com verbos como:

  * *Design*, *Develop*, *Construct*;
* Associação de **Análise de Requisitos** ao nível **Apply**, com verbos como:

  * *Interpret*, *Specify*, *Translate*;
* Remoção de associações implícitas ou ambíguas com o nível **Understand**, consideradas insuficientes para caracterizar atividades de **modelagem e construção efetiva**.

Esse ajuste reforça o caráter **operacional e produtivo** da competência C12.



### **3.4 Consolidação do Alinhamento com a Taxonomia de Bloom**

A competência C12 foi consolidada como uma competência de **nível cognitivo elevado**, predominantemente situada nos níveis:

* **Apply** — na interpretação e formalização de requisitos;
* **Create** — na concepção e implementação de soluções baseadas em PDA.

Esse posicionamento elimina ambiguidades cognitivas e assegura **coerência entre objetivos, atividades, evidências e avaliação**.





### **3.5 Resultado dos Ajustes**

### Competency C12 Specification

#### Competency Title

  Develop problem-solving solutions using Pushdown Automata

#### Textual Description

This competency addresses the ability to design, construct, and validate computational models based on Pushdown Automata (PDAs) to represent behaviors that require stack-based memory and context-sensitive control. Learners are expected to model systems in which memory is essential for tasks such as backtracking, recognition of nested structures, and sequential navigation.

Demonstrating this competency requires understanding how state transitions, input symbols, and stack operations interact to govern system behavior. Students must apply formal principles to construct PDA models that are logically correct, computationally adequate, and aligned with task-specific requirements.

Through this competency, learners develop the capacity to apply formal automata-based reasoning to practical problem scenarios—such as robotic navigation, language parsing, or symbolic processing—bridging theoretical foundations with effective computational solutions.


### **Knowledge Specification**

The following knowledge areas are essential for mastering this competency:

* **Pushdown Automata (PDA)**
  *Understand the formal principles of state-based computation with **stack-based memory**, including transition functions, stack operations (push, pop, stack alphabets, base symbols), and acceptance conditions. Apply this knowledge to model and validate computational behaviors that require **hierarchical memory**, **nested structure processing**, **backtracking**, or **sequence reversal**, ensuring adequacy for problems that exceed the expressive power of finite automata.*

* **Requirements Engineering**
  *Identify, structure, and formalize system requirements from problem descriptions and stakeholder needs. Translate real-world constraints and objectives into **functional and non-functional specifications** that inform the design of formal computational models, including Pushdown Automata.*

* **Analytical and Critical Thinking**
  *Apply systematic reasoning and problem decomposition to analyze problem structures, evaluate alternative modeling strategies, and justify design decisions based on formal properties, behavioral constraints, and system-level objectives.*




### **Disposition Specification**

Effective engagement with this competency requires the following behavioral dispositions:

* **Inventive** – Propose original modeling strategies and creative uses of stack-based mechanisms to address navigation and memory constraints.
* **Collaborative** – Work constructively in teams to discuss, refine, and validate PDA-based solutions.
* **Responsible** – Demonstrate rigor and accountability in formal modeling, simulation, and justification of design decisions.
* **Proactive** – Anticipate modeling challenges and iteratively refine solutions based on testing and analysis.
* **Creative** – Explore alternative representations and extensions of PDA models to enhance clarity, efficiency, or expressiveness.


### **Knowledge–Skill Pairing**

#### **Mapping Knowledge to Skills**

To demonstrate this competency, students must be able to:

* **Create** computational solutions using **Pushdown Automata**, designing and constructing formal models that employ **stack-based memory** to handle behaviors such as hierarchical processing, backtracking, nested structures, or sequence reversal.

* **Apply** knowledge of **Requirements Engineering** to elicit, structure, and prioritize system requirements, translating problem descriptions and constraints into **formal specifications** that guide the design of Pushdown Automata models.

* **Apply** **Analytical and Critical Thinking** to decompose complex problems, evaluate the adequacy and correctness of alternative modeling strategies, and iteratively refine solutions based on formal properties and system-level objectives.



### **Bloom’s Taxonomy Alignment**

The primary cognitive processes involved in this competency are aligned with the following levels of Bloom’s Revised Taxonomy:

* **Apply** — for interpreting and formalizing requirements, analyzing constraints, and evaluating modeling alternatives.
* **Create** — for designing, developing, and constructing Pushdown Automata–based solutions that address problems requiring memory and structured control.

This alignment reflects the **productive and generative nature** of the competency, which goes beyond conceptual understanding and emphasizes **formal model construction and validation**.



### **Verb Annotation**

To clarify competency expectations, the following verb annotations define the required learner actions:

* **Create** → *Pushdown Automata* → **Design, Develop, Construct**
* **Apply** → *Requirements Engineering* → **Interpret, Specify, Translate**
* **Apply** → *Analytical and Critical Thinking* → **Decompose, Evaluate, Refine**



### **Summary Table for Competency C12**

| **Competency**                                            | **Dispositions**                                           | **Knowledge**                    | **Skill (Bloom-aligned)**                   |
| --------------------------------------------------------- | ---------------------------------------------------------- | -------------------------------- | ------------------------------------------- |
| Develop problem-solving solutions using Pushdown Automata | Inventive, Collaborative, Responsible, Proactive, Creative | Pushdown Automata                | **Create** (*Design, Develop, Construct*)   |
|                                                           |                                                            | Requirements Engineering         | **Apply** (*Interpret, Specify, Translate*) |
|                                                           |                                                            | Analytical and Critical Thinking | **Apply** (*Decompose, Evaluate, Refine*)   |
