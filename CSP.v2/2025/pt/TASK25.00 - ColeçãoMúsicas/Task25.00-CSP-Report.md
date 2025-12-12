# Competency Specification Report: Task25.00 - Coleção de Músicas


## Introduction

Este relatório aplica a metodologia do **Competency Specification Process (CSP)** à **Task25.00 – Coleção de Músicas**, uma atividade da disciplina **MATC94 – Introdução às Linguagens Formais e Teoria da Computação**. A tarefa propõe a modelagem do domínio musical por meio de **linguagens formais**, tratando **notas como símbolos**, **músicas como cadeias** e **coleções de músicas como linguagens**, permitindo o uso rigoroso de operações clássicas como concatenação, fecho, reversão, união, interseção e complemento.

O problema exige respostas **formalmente justificadas**, mobilizando definições precisas, propriedades de fecho, exemplos mínimos e contraexemplos, quando apropriado. No contexto do CSP, a atividade favorece a especificação de competências relacionadas à **abstração de domínios reais**, **análise estrutural de linguagens** e **argumentação matemática rigorosa**, integrando conhecimento teórico, habilidades formais e postura analítica própria da Teoria da Computação.



## 1. Instructional Entity Analysis

### Title

- Coleção de Músicas

### Description
- Os aprendizes devem **modelar partituras musicais como objetos formais**, representando notas como símbolos, músicas como cadeias (strings) e coleções de músicas como linguagens, a fim de analisar propriedades estruturais e **aplicar operações clássicas sobre linguagens formais**. 

- A tarefa enfatiza a produção de **respostas matematicamente justificadas**, evitando interpretações intuitivas não formalizadas.



### Solution Development Process

**Abordagem esperada do aprendiz:**

- **Analisar as restrições do problema**, considerando que:
  - partituras podem envolver **um ou múltiplos instrumentos**, resultando em símbolos simples ou compostos;
  - cada música corresponde a uma **cadeia finita de comprimento arbitrário**;
  - músicas podem pertencer a **gêneros definidos extensionais** (conjuntos finitos) ou **intensionais** (por propriedades formais, como padrão rítmico).

- **Definir formalmente o modelo**, identificando:
  - o **alfabeto** de símbolos musicais;
  - a noção de **música** como string sobre esse alfabeto;
  - coleções de músicas como **linguagens** (subconjuntos de Σ\*).

- **Aplicar operações formais sobre linguagens**, tais como:
  - concatenação, prefixo, sufixo e subcadeias;
  - reversão;
  - união, interseção, complemento;
  - fecho de Kleene e linguagem vazia.

- **Analisar propriedades estruturais e de fecho**, utilizando:
  - definições formais;
  - exemplos mínimos;
  - demonstrações (incluindo raciocínio indutivo, quando pertinente);
  - contraexemplos para refutar afirmações incorretas.

- **Explorar equivalências e codificações**, discutindo:
  - homomorfismos entre diferentes representações (partitura ↔ gravação);
  - limites formais da intercambialidade entre codificações simbólicas.

- **Documentar rigorosamente** todas as escolhas de modelagem e conclusões, empregando notação matemática precisa e linguagem técnica adequada.





### Expected Outcomes
Os aprendizes devem produzir:

- Definições formais de **alfabeto, string, linguagem, linguagem vazia e fecho**;
- Interpretação e aplicação correta de **operações algébricas sobre cadeias e linguagens**;
- Análise da **finitude ou infinitude** de linguagens definidas no problema;
- Identificação de padrões estruturais e **argumentação sobre propriedades de linguagens**;
- Uso consistente de **homomorfismos e codificações** entre representações simbólicas;
- Modelagem de um problema do mundo real por meio de **conceitos de linguagens formais**;
- Elaboração de um **relatório técnico** com explicações claras, coerentes e matematicamente rigorosas, contendo:
  - definições formais;
  - exemplos mínimos;
  - demonstrações (incluindo indução e propriedades de fecho);
  - contraexemplos, quando apropriado.


### Acquisition Context

- Disciplina teórica de Teoria da Computação

- Tarefa avaliativa com foco em **argumentação formal e modelagem abstrata**



### Target Audience Profile

- **Nível acadêmico:** 2º–3º ano da graduação em Computação  
- **Experiência prévia:** fundamentos de estruturas de dados e introdução a autômatos  
- **Papéis esperados:** modelar linguagens formais; analisar propriedades; justificar formalmente decisões conceituais



### Proficiency Scale

- Escala com notas entre 0 e 100 (representando notas como 8.5 no modelo de avaliação da disciplina, por exemplo, que corresponde a 85 na escala).



## 2. Knowledge Enumeration

Para a enumeração sistemática dos conhecimentos de Computação requeridos nesta tarefa, foi adotado o **ACM CS2023** como **vocabulário controlado**, por se tratar do Body of Knowledge mais recente e amplamente aceito pela ACM, garantindo **padronização, rastreabilidade e consistência semântica** na categorização do conhecimento computacional.

Para o **Conhecimento Profissional Fundamental (FPK)**, utilizou-se como referência o **ACM Computing Curricula 2020 (CC2020)**, que oferece um arcabouço consolidado para competências profissionais transversais, tais como comunicação técnica, pensamento analítico e rigor conceitual.

Com base na **descrição da tarefa “Coleção de Músicas”**, que exige modelagem formal, argumentação matemática e aplicação de operações sobre linguagens, foram identificados os seguintes **componentes de conhecimento essenciais**.
 



### **Computing Knowledge**  
- **Linguagens Formais**
  - Alfabetos, cadeias, linguagens e linguagem vazia.
  - Linguagens finitas e infinitas.

- **Linguagens Regulares**
  - Expressões regulares e suas propriedades.
  - Relação entre expressões regulares, autômatos finitos e gramáticas regulares.

- **Máquinas de Estados Finitos**
  - DFA e NFA como reconhecedores de linguagens.
  - Noções de equivalência e poder expressivo.

- **Operações sobre Linguagens**
  - Concatenação, união, interseção e complemento.
  - Fecho de Kleene e propriedades de fechamento.
  - Reversão de cadeias.

- **Homomorfismos e Codificações**
  - Transformações formais entre representações simbólicas.
  - Discussão sobre equivalência e limites da intercambialidade entre codificações (ex.: partitura e gravação).

- **Raciocínio Formal**
  - Uso de definições matemáticas, exemplos mínimos, indução e contraexemplos para validação de afirmações.



### **Professional Knowledge (FPK)**  
Além do conhecimento técnico, a tarefa mobiliza competências profissionais fundamentais:

- **Pensamento Analítico e Crítico**
  - Capacidade de abstrair um domínio real (música) para um modelo formal.
  - Avaliação rigorosa da validade de afirmações e construções formais.

- **Comunicação Escrita Técnica**
  - Produção de textos claros, estruturados e semanticamente precisos.
  - Uso adequado de notação matemática e terminologia da Teoria da Computação.

- **Rigor Epistêmico**
  - Compromisso com justificativas formais, evitando respostas meramente intuitivas.
  - Clareza na distinção entre exemplos, definições, propriedades gerais e exceções.





## 3. Learning Objectives Identification

Com base no enunciado da tarefa **Coleção de Músicas**, os objetivos de aprendizagem foram definidos para refletir com precisão as **exigências conceituais**, o **nível de rigor matemático** e o **tipo de competência esperada** na disciplina **MATC94 – Introdução às Linguagens Formais e Teoria da Computação**.



### 3.1 General Learning Objective

O **objetivo geral** desta tarefa é capacitar o estudante a **modelar um domínio do mundo real (músicas e coleções musicais) como linguagens formais**, utilizando **conceitos fundamentais de linguagens, autômatos e expressões regulares**, e a **responder questões conceituais com rigor matemático**, por meio de definições formais, propriedades estruturais e argumentação lógica.



### 3.2 Specific Learning Objectives 

#### LO1 — Formal Abstraction of the Domain
1.1 Definir formalmente um **alfabeto (Σ)** a partir do conjunto de símbolos musicais relevantes.  
1.2 Modelar uma **música como uma cadeia (string) sobre Σ**.  
1.3 Modelar uma **coleção de músicas como uma linguagem (L ⊆ Σ\*)**.  

#### LO2 — Structural Analysis of Strings
2.1 Identificar e definir formalmente **prefixos, sufixos e subcadeias** de uma música.  
2.2 Determinar se um trecho de música pode ser formalmente considerado uma música válida.  
2.3 Justificar a validade (ou não) de trechos posicionados no início, meio ou fim de uma música.

#### LO3 — Operations over Languages
3.1 Aplicar a **concatenação** de cadeias para modelar a composição de músicas.  
3.2 Analisar se o resultado da concatenação pertence à mesma linguagem original.  
3.3 Aplicar **união, interseção e diferença** para combinar coleções musicais.  
3.4 Avaliar o **complemento** de uma linguagem em relação a um universo definido.  

#### LO4 — Kleene Closure and Language Cardinality
4.1 Aplicar o **fecho de Kleene (L\*)** a uma linguagem musical.  
4.2 Interpretar o papel da **cadeia vazia (ε)** em coleções musicais.  
4.3 Classificar linguagens como **finitas ou infinitas**, justificando formalmente.

#### LO5 — Reversal and String Transformations
5.1 Definir formalmente a **reversão de cadeias**.  
5.2 Aplicar a operação de reversão a uma música e analisar sua validade formal.  
5.3 Discutir implicações semânticas versus estruturais da reversão.

#### LO6 — Regular Languages and Formal Expressiveness
6.1 Reconhecer quando uma coleção de músicas pode ser descrita por uma **linguagem regular**.  
6.2 Especificar linguagens musicais por meio de **expressões regulares**.  
6.3 Diferenciar **gramáticas regulares** de **gramáticas livres de contexto**, indicando limites expressivos.  

#### LO7 — Automata and Model Equivalence (Conceptual Level)
7.1 Explicar a equivalência teórica entre **autômatos finitos, expressões regulares e gramáticas regulares**.  
7.2 Relacionar padrões estruturais de músicas a **estados e transições conceituais** de um autômato.  

#### LO8 — Homomorphisms and Codifications
8.1 Definir formalmente **homomorfismos de cadeias**.  
8.2 Analisar se duas representações (partitura e gravação) podem ser vistas como **codificações equivalentes**.  
8.3 Justificar limites formais da intercambialidade entre representações simbólicas.

#### LO9 — Formal Reasoning and Proof
9.1 Utilizar **definições formais** para sustentar respostas conceituais.  
9.2 Construir **exemplos mínimos** para ilustrar propriedades de linguagens.  
9.3 Empregar **contraexemplos** para refutar afirmações incorretas.  
9.4 Aplicar **raciocínio indutivo** quando apropriado (por exemplo, em propriedades de fecho).

#### LO10 — Technical Communication
10.1 Elaborar um **relatório técnico** com estrutura lógica e terminologia adequada.  
10.2 Apresentar justificativas claras, coerentes e matematicamente rigorosas.  
10.3 Distinguir explicitamente entre **intuição informal**, **exemplo** e **prova**.


### 3.3 Importance of These Objectives

Esses objetivos estabelecem um **caminho estruturado de desenvolvimento de competências**, assegurando que o estudante:

- construa uma **base teórica sólida** em linguagens formais e teoria da computação;
- desenvolva a capacidade de **abstrair domínios reais** para modelos matemáticos precisos;
- compreenda **propriedades estruturais e limites formais** das linguagens;
- exercite **pensamento analítico e rigor epistêmico**, fundamentais para a área;
- adquira habilidades de **comunicação técnica**, essenciais em contextos acadêmicos e profissionais.

Ao atingir esses objetivos, o estudante estará apto a **conectar teoria e prática**, utilizando conceitos de **Linguagens Formais e Autômatos** para analisar, justificar e resolver problemas conceituais complexos com clareza e rigor.




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
