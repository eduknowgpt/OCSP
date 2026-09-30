# CSP-Report — TASK25.04 — *Movimentação de Robô* 

## 1. Introdução

Este relatório aplica o **Competency Specification Process (CSP)** à **TASK25.04 — Movimentação de Robô**, uma tarefa cujo objetivo é **especificar, validar e interpretar formalmente sequências simbólicas** que descrevem a navegação de um robô em **ambientes aninhados**, integrando **estrutura sintática**, **correção semântica** e **processamento de resultados**. 

O problema propõe uma linguagem artificial composta por **portas de entrada e saída** (`OPEN`, `CLOSE`), **marcas de energia** (inteiros) e **conectores de fluxo** (operadores aritméticos). Para que a navegação do robô seja considerada válida, a sequência deve satisfazer simultaneamente dois critérios fundamentais:

1. **correção estrutural**, garantindo o balanceamento e o aninhamento adequado das salas;  
2. **correção operacional**, assegurando que marcas de energia e conectores formem expressões bem definidas e avaliáveis. 

Do ponto de vista da Teoria da Computação, a tarefa exige a **especificação de uma linguagem formal**, a **definição de seus tokens**, a **construção de uma gramática** capaz de capturar tanto o aninhamento das salas quanto a estrutura das expressões aritméticas, e a **implementação de mecanismos de reconhecimento, validação e interpretação**. O processamento correto culmina não apenas na aceitação ou rejeição da sequência, mas também na **avaliação semântica da expressão**, produzindo o saldo final de energia. 

Com base no **catálogo atual de competências**, esta tarefa **não pode ser descrita adequadamente apenas com competências já existentes voltadas a autômatos, gramáticas ou Máquinas de Turing**. Embora algumas competências do catálogo sejam reutilizáveis, a tarefa introduz demandas específicas de **análise léxica**, **análise sintática** e **validação semântica**, que justificam a introdução de novas competências especializadas. Assim, esta versão corrigida do CSP-Report preserva o reuso onde ele é semanticamente adequado e introduz novas competências apenas onde o catálogo atual ainda não cobre explicitamente o domínio de **scanner / parser / semantic validation**. 





## 2. Análise da Entidade Instrucional

### 2.1 Identificação

- **Título:** Movimentação de Robô  
- **Tipo:** Caso PBL com ênfase em especificação e validação formal de linguagens  
- **Domínio:** Linguagens Formais, Autômatos e Fundamentos de Compiladores. 




### 2.2 Descrição 

A tarefa requer que os estudantes **especifiquem e implementem um validador automático** para uma linguagem simbólica que descreve a movimentação de um robô em **ambientes hierarquicamente aninhados**. Essa linguagem combina **estruturas de delimitação** (portas `OPEN` e `CLOSE`) com **expressões aritméticas**, formadas por marcas de energia (inteiros) e conectores de fluxo (operadores). 

Os estudantes devem, inicialmente, **definir e reconhecer os tokens da linguagem**, construindo um **analisador léxico** capaz de identificar portas, números, operadores e símbolos inválidos. Em seguida, devem projetar um **analisador sintático** que verifique simultaneamente o **balanceamento e o aninhamento correto das salas** e a **ordem válida entre operandos e operadores**, rejeitando sequências estrutural ou operacionalmente incorretas. 

A tarefa também exige que a validação vá além da aceitação sintática, incorporando uma **interpretação semântica da expressão**, de modo que, quando a sequência for válida, o sistema produza o **resultado final da combinação das energias**. Em caso de erro, o sistema deve gerar um **relatório detalhado**, indicando o tipo de falha, sua localização e a justificativa formal para a rejeição. 

No âmbito do CSP, a TASK25.04 caracteriza-se como uma atividade de **integração entre análise léxica, sintática e semântica**, na qual o desempenho do estudante é evidenciado por **artefatos formais verificáveis** (scanner, parser, avaliador e relatório técnico), e não por descrições narrativas do processo.





## 3. Resultados Esperados

Ao final da tarefa, espera-se que os estudantes produzam um **conjunto integrado de artefatos formais** que evidenciem sua capacidade de **especificar, validar e interpretar uma linguagem formal completa**. Em particular, os estudantes deverão apresentar:

- um **analisador léxico funcional**, capaz de identificar corretamente portas, marcas de energia, conectores e símbolos inválidos;
- um **analisador sintático** que reconheça o balanceamento das salas e a estrutura correta das expressões;
- um **módulo de análise semântica**, responsável por **avaliar corretamente as expressões aritméticas** quando a sequência for válida;
- um **relatório automático de validação**, indicando de forma precisa se a sequência é aceita ou rejeitada e, em caso de erro, **o local, o tipo e a justificativa formal da falha**;
- um **relatório técnico matematicamente rigoroso**, documentando a especificação da linguagem, as decisões de projeto do analisador léxico-sintático, os critérios de validação semântica e os resultados obtidos. 





## 4. Enumeração de Conhecimentos

A realização adequada da **TASK25.04 — Movimentação de Robô** requer a mobilização integrada de conhecimentos disciplinares em **Teoria da Computação e Compiladores** e de conhecimentos profissionais fundamentais, conforme os referenciais do **CS2023** e do **CC2020**. Esses conhecimentos sustentam a **especificação da linguagem**, a **validação estrutural e operacional** das sequências e a **avaliação semântica** das expressões. 

### 4.1 Conhecimentos de Computação (CS2023)

- **Teoria das Linguagens Formais**
  - alfabetos, cadeias e linguagens;
  - definição de linguagens por regras sintáticas;
  - distinção entre correção estrutural e correção operacional.

- **Linguagens Livres de Contexto**
  - gramáticas livres de contexto;
  - aninhamento e balanceamento de símbolos;
  - reconhecimento de estruturas hierárquicas.

- **Análise Léxica**
  - definição de tokens;
  - reconhecimento de padrões regulares;
  - tratamento de símbolos inválidos e separadores.

- **Análise Sintática**
  - verificação de ordem e estrutura dos tokens;
  - detecção de erros sintáticos;
  - construção de analisadores baseados em gramáticas.

- **Análise Semântica**
  - avaliação de expressões aritméticas;
  - coerência entre operandos e operadores;
  - distinção entre erros sintáticos e semânticos.

- **Modelos de Computação com Memória Estruturada**
  - uso implícito de pilha para verificação de aninhamento;
  - relação entre gramáticas livres de contexto e mecanismos de reconhecimento. 




### 4.2 Conhecimentos Profissionais Fundamentais (FPK — CC2020)

- **Pensamento Analítico e Crítico**  
  Capacidade de decompor o comportamento do sistema, avaliar a correção da linguagem definida, identificar inconsistências e justificar formalmente as decisões de projeto.

- **Comunicação Técnica Escrita**  
  Capacidade de produzir um **relatório claro, estruturado e matematicamente preciso**, expressando definições, especificações, argumentos e conclusões de forma coerente e verificável. 





## 5. Objetivos de Aprendizagem

### Objetivo Geral

Capacitar o estudante a aplicar os **fundamentos teóricos de Linguagens Formais e Autômatos** na concepção e implementação de um **analisador léxico-sintático completo**, estendendo essa análise à **validação semântica** e à geração de relatórios de erro formalmente justificados. 

### Objetivos Específicos

Ao concluir a tarefa, o estudante deverá ser capaz de:

- **LO1 — Especificar simbolicamente a linguagem do robô**  
  Definir o alfabeto, os tokens e as categorias léxicas da linguagem, distinguindo portas, inteiros, operadores, espaços e símbolos inválidos.

- **LO2 — Construir um analisador léxico (scanner)**  
  Implementar um mecanismo capaz de identificar e classificar corretamente os tokens da linguagem.

- **LO3 — Projetar um analisador sintático (parser)**  
  Verificar formalmente o balanceamento das salas, a ordem correta de abertura e fechamento e a sequência válida entre marcas de energia e conectores.

- **LO4 — Detectar e relatar falhas estruturais e sintáticas**  
  Identificar local, tipo e justificativa formal de erros léxicos ou sintáticos.

- **LO5 — Validar a coerência semântica da expressão**  
  Avaliar o saldo final de energia quando a sequência for válida e distinguir erros sintáticos de erros semânticos quando necessário.

- **LO6 — Comunicar tecnicamente a especificação e os resultados**  
  Produzir um relatório técnico rigoroso, explicitando a linguagem definida, os critérios de validação, os casos de erro e os resultados obtidos. 





## 6. Competências da TASK25.04 (com Ativações OntoKSD) 

As competências a seguir constituem o **perfil de desempenho esperado** para a **TASK25.04 — Movimentação de Robô**. O conjunto foi definido com base no **catálogo atual da OntoKSD**, reutilizando competências cujo escopo já cobre adequadamente partes da tarefa e introduzindo novas competências onde o catálogo ainda não explicita o domínio de **análise léxica, análise sintática e validação semântica**.

### 6.1 Competências Reutilizadas

#### **C18 — Model real-world problems using formal language concepts**

**Tipo:** Competência atômica

**ActivationRole:** `core`  
**ActivationMode:** `constructive`  
**ActivationConstraint:** `mandatory`

**Particularização na TASK25.04:**  
Mapear portas, marcas de energia, conectores e sequências de navegação em **símbolos, cadeias e linguagens**, estabelecendo a representação formal base do problema. Essa competência sustenta a abstração inicial da linguagem do robô e a definição do espaço simbólico a ser analisado.





#### **C13.01 — Interpret formal grammar-based rules**

**Tipo:** Competência transversal

**ActivationRole:** `transversal`  
**ActivationMode:** `analytical`  
**ActivationConstraint:** `mandatory`

**Particularização na TASK25.04:**  
Interpretar **regras gramaticais formais**, não terminais, produções e estruturas derivacionais que descrevem o balanceamento das salas e a organização válida das expressões internas. Nesta tarefa, C13.01 é mobilizada em seu sentido original, ligado à interpretação de **formal grammar-based rules**, apoiando a compreensão do parser e da gramática da linguagem do robô.





#### **C05.01 — Write mathematically rigorous answers**

**Tipo:** Competência transversal

**ActivationRole:** `transversal`  
**ActivationMode:** `justificatory`  
**ActivationConstraint:** `mandatory`

**Particularização na TASK25.04:**  
Justificar formalmente a correção do scanner, do parser, da validação semântica e dos relatórios de erro, usando definições, exemplos, contraexemplos e argumentos estruturados. A tarefa exige que a documentação técnica vá além da descrição operacional, tornando explícitos os fundamentos formais das decisões adotadas.





#### **C14 — Differentiate classifications of formal grammars**

**Tipo:** Competência atômica

**ActivationRole:** `supporting`  
**ActivationMode:** `analytical`  
**ActivationConstraint:** `conditional`

**Particularização na TASK25.04:**  
Distinguir, quando pertinente, entre estruturas **regulares** e **livres de contexto**, justificando por que o reconhecimento léxico pode ser tratado por padrões regulares, enquanto o balanceamento e o aninhamento exigem mecanismos gramaticais mais expressivos. Sua ativação é condicional porque essa análise aprofunda a fundamentação teórica, mas não é necessária para toda solução funcional.




### 6.2 Novas Competências Introduzidas em TASK25.04

#### **C25 — Develop lexical analyzers for symbolic languages**

**Tipo:** Competência atômica nova

**ActivationRole:** `core`  
**ActivationMode:** `constructive`  
**ActivationConstraint:** `mandatory`

**Particularização na TASK25.04:**  
Construir um **analisador léxico** capaz de reconhecer e classificar corretamente **tokens** da linguagem do robô, incluindo `OPEN`, `CLOSE`, inteiros, operadores, espaços e símbolos inválidos.

**Textual Description:**  
This competency involves the ability to **design and implement lexical analyzers for symbolic languages**, correctly identifying and classifying input tokens according to formally specified categories.

Learners demonstrate this competency by:

- defining token classes and lexical categories;
- recognizing patterns associated with keywords, numbers, operators, separators, and invalid symbols;
- distinguishing relevant tokens from irrelevant or malformed input fragments;
- producing tokenization results that support later syntactic and semantic analysis.


#### **C26 — Develop syntactic analyzers for context-free symbolic languages**

**Tipo:** Competência atômica nova

**ActivationRole:** `core`  
**ActivationMode:** `constructive`  
**ActivationConstraint:** `mandatory`

**Particularização na TASK25.04:**  
Projetar e implementar um **analisador sintático** capaz de verificar o **balanceamento das salas**, o **aninhamento correto** de `OPEN` e `CLOSE` e a **ordem válida entre operandos e operadores**.

**Textual Description:**  
This competency involves the ability to **design and implement syntactic analyzers for symbolic languages governed by context-free structural constraints**, ensuring that input sequences conform to the grammar of the language.

Learners demonstrate this competency by:

- specifying grammatical rules for well-formed symbolic expressions;
- validating nested and balanced structures;
- detecting invalid token orderings and malformed derivations;
- using grammar-based mechanisms to accept or reject symbolic sequences.



#### **C27 — Validate semantic consistency of formal expressions**

**Tipo:** Competência atômica nova

**ActivationRole:** `supporting`  
**ActivationMode:** `analytical`  
**ActivationConstraint:** `mandatory`

**Particularização na TASK25.04:**  
Avaliar o **resultado final da combinação das energias** quando a sequência for válida e identificar inconsistências semânticas na interpretação da expressão, distinguindo-as de erros puramente léxicos ou sintáticos.

**Textual Description:**  
This competency involves the ability to **evaluate the semantic consistency of formally valid expressions**, producing computed results when appropriate and distinguishing semantic problems from lexical or syntactic invalidity.

Learners demonstrate this competency by:

- interpreting the meaning of syntactically valid symbolic expressions;
- computing the correct result of formally well-formed expressions;
- distinguishing structural validity from operational meaning;
- identifying when a sequence is syntactically acceptable but semantically problematic.



#### **C28 — Generate formal validation error reports**

**Tipo:** Competência atômica nova

**ActivationRole:** `supporting`  
**ActivationMode:** `artifact-oriented`  
**ActivationConstraint:** `mandatory`

**Particularização na TASK25.04:**  
Produzir **relatórios automáticos de validação**, informando se a sequência é válida e, em caso de erro, o **local**, o **tipo** e a **justificativa formal** da falha detectada.

**Textual Description:**  
This competency involves the ability to **generate formal validation reports** that communicate acceptance or rejection decisions, while explicitly identifying the location, type, and justification of lexical, syntactic, or semantic errors.

Learners demonstrate this competency by:

- reporting validation outcomes clearly and systematically;
- locating the point of failure in an input sequence;
- classifying error types precisely;
- providing formally grounded explanations for rejection.



## 7. Estrutura OntoKSD implícita (TASK25.04)

```text
TASK25.04
├── coreCompetence
│   ├── C18 — Model real-world problems using formal language concepts
│   ├── C25 — Develop lexical analyzers for symbolic languages
│   └── C26 — Develop syntactic analyzers for context-free symbolic languages
│
├── transversalCompetence
│   ├── C13.01 — Interpret formal grammar-based rules
│   └── C05.01 — Write mathematically rigorous answers
│
├── supportingCompetence
│   ├── C27 — Validate semantic consistency of formal expressions
│   └── C28 — Generate formal validation error reports
│
└── extensionCompetence
    └── C14 — Differentiate classifications of formal grammars