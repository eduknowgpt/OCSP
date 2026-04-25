## **Competency Lifecycle – C13 – *Interpret rule-based notation***


## **1. Definição Original — *CSP-Report (Ciclo 1)***

A competência C13 emerge da necessidade de compreender e interpretar notações formais baseadas em regras, utilizadas para descrever comportamentos simbólicos, sequências válidas e estruturas hierárquicas em sistemas computacionais.

No contexto das tarefas do CSP, identificou-se que a construção de modelos formais (ex.: PDAs) exige, previamente, a capacidade de interpretar corretamente gramáticas, regras de produção e notações simbólicas. Essa competência não se confunde com a criação de modelos, mas com a leitura semântica e estrutural de descrições formais que orientam ou explicam o comportamento do sistema.

Assim, C13 surge como uma competência pré-operacional e interpretativa, necessária para sustentar atividades de modelagem formal.


### **Primeira Especificação (CSP Phase 1B: Competency Authoring)**

Na primeira especificação, a competência **C13 – Interpret rule-based notation** foi definida com o objetivo de captar a capacidade do estudante de **compreender e interpretar notações formais baseadas em regras**, utilizadas para descrever comportamentos simbólicos e sequências válidas em sistemas computacionais.

A competência foi inicialmente concebida como **suporte conceitual** às atividades de modelagem formal, contemplando a leitura e interpretação de:

* regras de produção;
* gramáticas formais;
* descrições simbólicas de comportamento.

Nessa versão inicial, a especificação apresentava as seguintes características:

* **Escopo conceitual amplo**, incluindo referências genéricas a *rule-based notation*;
* **Conhecimentos associados** envolvendo linguagens formais e modelos de reconhecimento;
* **Nível cognitivo predominante** situado em **Understand**, com verbos como *interpret*, *recognize* e *explain*;
* Papel implícito como competência **pré-operacional**, necessária para apoiar competências de modelagem e solução de problemas.

Embora conceitualmente válida, a especificação inicial ainda apresentava **imprecisões quanto ao modelo computacional de referência** e ao **nível exato de abstração da notação interpretada**.



Durante a **Competency Authoring Phase**, C13 foi formalizada com a seguinte estrutura:


### Competency C13 Specification

#### Competency Title

  Interpret rule-based notation

#### Textual Description

Understand and interpret formal notations based on production rules, such as context-free grammars, to represent system behavior and enable navigation control through symbol sequences.

#### Knowledge Specification

The following knowledge areas are essential for mastering this competency:

* Context-Free Grammars and Regular Languages
  * Understand how these formal languages define structured symbol sequences and how to construct grammars for recognizing or generating specific behavior patterns.

* Pushdown Automata 
  * Understand the correspondence between rule-based languages and automata capable of recognizing them, particularly the role of memory in parsing nested structures.

* Analytical and Critical Thinking (FPK)
  * Apply reasoning skills to interpret rule sets, validate symbolic behavior representations, and refine grammars for clarity, completeness, and correctness.

#### Disposition Specification

The development of formal, rule-based models requires the following behavioral dispositions:


* Collaborative – Co-develop and review rule-based models with peers.

* Responsible – Ensure accuracy and consistency in symbolic representations.

* Proactive – Anticipate rule interactions and model ambiguities.



#### Knowledge-Skill Pairing

#### Mapping Knowledge to Skills
To demonstrate this competency, students must be able to:

* Understand knowledge of Context-Free Grammars and Regular Languages to define symbolic representations of system behavior through production rules.

* Apply knowledge of Automata (PDA and FA) to simulate and validate rule-based control logic in accordance with language constraints.

* Employ Analytical and Critical Thinking to evaluate rule sets, identify ambiguities or redundancies, and improve grammar structures for better alignment with system requirements.


#### Bloom’s Taxonomy Alignment

This competency engages learners at the following cognitive levels:

* **Understand** – To recognize, interpret, and describe the structure and purpose of rule-based models.

* **Apply** – To construct grammars and use symbolic rules to represent and control system behavior.



#### Verb Annotation
Interpret, Apply, Recognize, Analyze

#### Summary Table for Competency C13

| **Competency**                | **Dispositions**                                               | **Knowledge**                          | **Skill**                  |
| ----------------------------- | -------------------------------------------------------------- | -------------------------------------- | -------------------------- |
| Interpret rule-based notation |  Collaborative, Responsible, Proactive| Finite Automata                      | **Understand**             |
|                               |                                                                | Regular Languages                      | **Apply (Utilize, Solve)** |
|                               |                                                                | Analytical and Critical Thinking  | **Apply**                  |





## **2. Revisões — *CSRP-Report (Ciclo 1 — Revisão por Especialistas)***

Durante a **Revisão por Especialistas (CSRP – Ciclo 1)**, a competência **C13** foi avaliada por meio de um **processo técnico-pedagógico de análise de artefatos educacionais**. A revisão concentrou-se exclusivamente na **avaliação conceitual, terminológica e cognitiva da especificação da competência**, sem envolver coleta, análise ou interpretação de dados pessoais, comportamentais ou identificáveis de participantes.

No âmbito dessa revisão, a competência foi considerada **pedagogicamente pertinente e adequadamente posicionada no conjunto de competências**. Contudo, os especialistas identificaram **necessidades de refinamento conceitual e terminológico**, especialmente no que se refere à **clareza do formalismo de referência mobilizado nas tarefas** e à **consistência interna da competência em relação às demais do conjunto**.

As principais recomendações formuladas pelos especialistas foram as seguintes:

* **Realinhamento contextual do formalismo computacional de referência**  
  Os especialistas observaram que, nos contextos analisados — particularmente em tarefas que exigiam o tratamento de **estruturas hierárquicas, aninhamento e dependências contextuais** —, referências implícitas ou genéricas a **Finite Automata** mostravam-se insuficientes. Recomendaram, portanto, o **alinhamento explícito com Pushdown Automata (PDA)** como modelo canônico para a interpretação de notações baseadas em regras nesses cenários específicos, dada sua maior capacidade expressiva.

* **Refinamento e precisão do conhecimento linguístico associado**  
  Foi recomendada a substituição de referências genéricas a **Regular Languages** por **Context-Free Grammars (CFGs)** e **Context-Free Languages (CFLs)**, de modo a alinhar explicitamente a notação interpretada ao **nível gramatical efetivamente requerido** pelas tarefas analisadas e à sua correspondência formal com modelos reconhecedores baseados em pilha.

* **Delimitação explícita do nível cognitivo mobilizado**  
  Os especialistas enfatizaram a necessidade de consolidar a competência predominantemente no nível **Understand** da Taxonomia de Bloom, evitando elevações indevidas para **Apply** ou **Create**. Tal recomendação baseou-se no entendimento de que o foco da C13 reside na **interpretação semântica, estrutural e relacional de notações formais**, e não na construção, execução ou otimização de modelos computacionais.

Essas recomendações tiveram como finalidade **preservar e explicitar o caráter interpretativo e conceitual da competência C13**, evitando sobreposição funcional com competências de **modelagem ou implementação** e assegurando sua posição como **fundamento cognitivo** para competências operacionais subsequentes (e.g., **C12**).

Importante destacar que tais recomendações foram **formuladas no contexto específico de tarefas que mobilizavam formalismos contexto-livres**. Nesse sentido, elas **informaram decisões posteriores de especialização controlada da competência** (e.g., a definição da **C13.01**), **sem implicar um estreitamento permanente do escopo geral da C13**, que foi posteriormente estabilizada como uma competência transversal e domain-independent.



## **3. Alterações Implementadas — *CSP-Adjustments***

Com base nas recomendações consolidadas no **CSRP-Report (Ciclo 1)**, foram implementados **ajustes procedimentais, semânticos e estruturais** na especificação da competência **C13**. Esses ajustes tiveram como objetivo **clarificar seu papel conceitual**, **eliminar ambiguidades identificadas durante a revisão especializada** e **preparar a competência para uma estabilização semanticamente robusta**, sem comprometer sua reutilização transversal.

As principais alterações implementadas foram as seguintes:

* **Clarificação terminológica orientada pelo contexto de uso**  
  A competência passou a distinguir explicitamente entre o **escopo geral de notações baseadas em regras** e os **formalismos específicos mobilizados em determinadas tarefas**. Nos contextos analisados, notações de natureza **contexto-livre** foram utilizadas como exemplos canônicos, permitindo eliminar ambiguidades observadas na interpretação inicial da competência, sem implicar restrição permanente de seu escopo geral.

* **Explícita diferenciação entre notação simbólica e modelo reconhecedor**  
  Foi reforçada a distinção conceitual entre a **interpretação de regras formais** e os **modelos computacionais que as reconhecem**. A correspondência com **Pushdown Automata (PDA)** passou a ser tratada como um **caso ilustrativo e teoricamente fundamentado**, evitando que a competência fosse confundida com atividades de construção, execução ou otimização de modelos baseados em pilha.

* **Reafirmação do papel funcional da competência no conjunto**  
  A C13 foi explicitamente caracterizada como uma competência de **leitura, análise e explicação de notações formais**, posicionando-se como **fundamento cognitivo** para competências operacionais de modelagem e solução de problemas (e.g., **C12**). Esse ajuste evitou sobreposição funcional e reforçou a separação entre competências interpretativas e construtivas.

* **Estabilização cognitiva segundo a Taxonomia de Bloom**  
  A competência foi consolidada predominantemente no nível **Understand**, com controle explícito de verbos (*interpret*, *recognize*, *explain*, *relate*). Atividades de análise mais profunda foram tratadas como extensões cognitivas controladas, garantindo coerência entre o **desempenho esperado**, as **evidências observáveis** e os **critérios avaliativos**, sem deslocar a competência para níveis operacionais indevidos.

Esses ajustes não resultaram em um estreitamento definitivo da competência **C13**. Ao contrário, eles **informaram a posterior decisão de especialização controlada** (e.g., **C13.01**) para contextos que exigem interpretação de **formalismos gramaticais específicos**, permitindo que a C13 fosse estabilizada como uma **competência transversal, domain-independent e semanticamente consistente** dentro do CSP.




## **Resultado dos Ajustes (CSP)**

Como resultado dos ajustes informados pela revisão por especialistas e consolidados no CSP, a competência **C13** foi estabilizada como uma **competência interpretativa de base**, cujo papel central é **sustentar a compreensão formal de sistemas descritos por notações simbólicas baseadas em regras**.

A competência passou a ser explicitamente caracterizada como **pré-operacional**, não envolvendo atividades de construção, execução ou otimização de modelos computacionais. Seu escopo, nível cognitivo e conhecimentos associados foram claramente delimitados, evitando sobreposição funcional com competências de **modelagem**, **implementação** ou **solução de problemas** (e.g., **C12**).

Essa estabilização assegura que a C13 funcione como um **fundamento cognitivo transversal**, aplicável a diferentes domínios e contextos instrucionais, ao mesmo tempo em que permite **especializações controladas** (e.g., **C13.01**) quando tarefas exigem a interpretação de formalismos específicos.




## **Competency C13 Specification (Versão Estabilizada)**

### **Competency Title**

  Interpret rule-based notation



### **Textual Description**

This competency refers to the ability to **understand, interpret, and reason about rule-based notations** used to formally specify structured symbol sequences, constraints, or control logic in computational systems. Learners demonstrate this competency by analyzing how **rules, symbols, and hierarchical or sequential structures** define valid configurations, admissible behaviors, or execution flows.

The competency is **domain-independent** and applies to a wide range of contexts that rely on **symbolic modeling and formal specification**, including language processing, protocol definition, rule-based control systems, policy specification, and formal documentation. Emphasis is placed on the comprehension of **syntactic organization**, **rule dependencies**, and the relationship between notational elements and the behaviors they characterize or constrain, rather than on the construction of specific artifacts.


### **Knowledge Specification**

The following knowledge areas support the development of this competency:

* **Rule-Based Formalisms**  
  *Understand the general structure of rule-based systems, including production rules, constraints, and symbolic representations used to define valid sequences or configurations.*

* **Formal Grammars and Language Models**  
  *Understand how grammatical formalisms (e.g., regular or context-free grammars) organize symbols hierarchically or sequentially, serving as canonical examples of rule-based notation.*

* **Computational Models Corresponding to Rules**  
  *Recognize that different classes of rule-based specifications may correspond to different abstract computational models (e.g., finite automata, stack-based automata), without requiring detailed implementation or construction.*

* **Analytical and Critical Reasoning**  
  *Apply formal reasoning skills to interpret rule sets, analyze symbolic structures, identify ambiguities or inconsistencies, and assess whether a given notation adequately captures its intended constraints.*



### **Knowledge–Skill Pairing**

#### **Mapping Knowledge to Skills**

To demonstrate this competency, learners must be able to:

* **Understand** rule-based formalisms in order to interpret symbolic specifications that define valid sequences, structures, or constraints.  
  *Associated verbs:* *Interpret, Relate, Explain*

* **Understand** the relationship between rule-based notations and abstract computational models, recognizing how symbolic rules constrain or enable system behavior.  
  *Associated verbs:* *Recognize, Explain, Compare*

* **Analyze** symbolic rule systems using analytical and critical reasoning, identifying ambiguities or inconsistencies and evaluating the adequacy of notational representations.  
  *Associated verbs:* *Analyze, Evaluate, Validate*



### **Summary Table for Competency C13**

| **Competency**                | **Dispositions**                                           | **Knowledge**                         | **Skill (Bloom-aligned)**                          |
| ----------------------------- | ---------------------------------------------------------- | ------------------------------------- | -------------------------------------------------- |
| Interpret rule-based notation |  Collaborative, Responsible, Proactive | Rule-Based Formalisms                 | **Understand** (*Interpret, Explain*)              |
|                               |                                                            | Formal Grammars and Language Models   | **Understand** (*Relate, Compare*)                 |
|                               |                                                            | Analytical and Critical Reasoning     | **Analyze** (*Analyze, Evaluate, Validate*)        |

