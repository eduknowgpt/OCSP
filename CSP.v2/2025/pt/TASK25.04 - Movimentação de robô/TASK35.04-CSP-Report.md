# CSP-Report — TASK25.04 — *Movimentação de Robô*

## 1. Introdução

Este relatório aplica o **Competency Specification Process (CSP)** à **TASK25.04 — Movimentação de Robô**, uma tarefa cujo objetivo é **modelar, validar e interpretar formalmente sequências simbólicas** que descrevem a navegação de um robô em **ambientes aninhados**, integrando **estrutura sintática**, **correção semântica** e **processamento de resultados**.

O problema propõe uma linguagem artificial composta por **portas de entrada e saída** (`OPEN`, `CLOSE`), **marcas de energia** (inteiros) e **conectores de fluxo** (operadores aritméticos). Para que a navegação do robô seja considerada válida, a sequência deve satisfazer simultaneamente dois critérios fundamentais:  
(i) **correção estrutural**, garantindo o balanceamento e o aninhamento adequado das salas, e  
(ii) **correção operacional**, assegurando que marcas de energia e conectores formem expressões bem definidas e avaliáveis.

Do ponto de vista da Teoria da Computação, a tarefa exige a **especificação de uma linguagem formal**, a **definição de seus tokens**, a **construção de uma gramática** capaz de capturar tanto o aninhamento das salas quanto a estrutura das expressões aritméticas, e a **implementação de mecanismos de reconhecimento e validação**. O processamento correto culmina não apenas na aceitação ou rejeição da sequência, mas também na **avaliação semântica da expressão**, produzindo o saldo final de energia.

No contexto do CSP, a TASK25.04 mobiliza competências relacionadas à **análise léxica**, **análise sintática**, **uso de memória estruturada para balanceamento**, **verificação de propriedades semânticas** e **argumentação técnica rigorosa**. A tarefa desloca o foco de uma simples validação estrutural para a **integração entre sintaxe e significado**, aproximando-se de problemas clássicos de **compiladores e interpretadores**, e permitindo uma avaliação baseada em **artefatos formais verificáveis** (scanner, parser, relatórios de erro e avaliação da expressão), alinhada aos referenciais do **CS2023**, do **CC2020** e à ontologia **OntoKSD**.


## 2. Análise da Entidade Instrucional

### 2.1 Identificação

- **Título:** Movimentação de Robô  
- **Tipo:** Caso PBL com ênfase em especificação e validação formal de linguagens  
- **Domínio:** Linguagens Formais, Autômatos e Fundamentos de Compiladores  



### 2.2 Descrição Sintética

A tarefa requer que os estudantes **especifiquem e implementem um validador automático** para uma linguagem simbólica que descreve a movimentação de um robô em **ambientes hierarquicamente aninhados**. Essa linguagem combina **estruturas de delimitação** (portas `OPEN` e `CLOSE`) com **expressões aritméticas**, formadas por marcas de energia (inteiros) e conectores de fluxo (operadores).

Os estudantes devem, inicialmente, **definir e reconhecer os tokens da linguagem**, construindo um **analisador léxico** capaz de identificar portas, números, operadores e símbolos inválidos. Em seguida, devem projetar um **analisador sintático** que verifique simultaneamente o **balanceamento e o aninhamento correto das salas** e a **ordem válida entre operandos e operadores**, rejeitando sequências estrutural ou operacionalmente incorretas.

A tarefa também exige que a validação vá além da aceitação sintática, incorporando uma **interpretação semântica da expressão**, de modo que, quando a sequência for válida, o sistema produza o **resultado final da combinação das energias**. Em caso de erro, o sistema deve gerar um **relatório detalhado**, indicando o tipo de falha, sua localização e a justificativa formal para a rejeição.

No âmbito do CSP, a TASK25.04 caracteriza-se como uma atividade de **integração entre análise léxica, sintática e semântica**, na qual o desempenho do estudante é evidenciado por **artefatos formais verificáveis** (scanner, parser, avaliador e relatório técnico), e não por descrições narrativas do processo, alinhando-se ao paradigma de **avaliação por competências**.


## 3. Resultados Esperados

Ao final da tarefa, espera-se que os estudantes produzam um **conjunto integrado de artefatos formais** que evidenciem sua capacidade de **especificar, validar e interpretar uma linguagem formal completa**. Em particular, os estudantes deverão apresentar um **analisador léxico funcional**, capaz de identificar corretamente portas, marcas de energia, conectores e símbolos inválidos, bem como um **analisador sintático** que reconheça o balanceamento das salas e a estrutura correta das expressões.

Além da validação estrutural e sintática, espera-se a implementação de um **módulo de análise semântica**, responsável por **avaliar corretamente as expressões aritméticas** quando a sequência for válida. O sistema deve ainda gerar um **relatório automático de validação**, indicando de forma precisa se a sequência é aceita ou rejeitada e, em caso de erro, **o local, o tipo e a justificativa formal da falha**.

Como evidência final, os estudantes devem produzir um **relatório técnico matematicamente rigoroso**, documentando a especificação da linguagem, as decisões de projeto do analisador léxico-sintático, os critérios de validação semântica e os resultados obtidos, permitindo a verificação objetiva do desempenho demonstrado.


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

