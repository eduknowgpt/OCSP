# **Introdução a Linguagens Formais e Teoria da Computação**

## Visão Geral da Disciplina

Instituto de Computação – UFBA
Bacharelado em Ciência da Computação
4º semestre – 2º ano

A disciplina **Introdução a Linguagens Formais e Teoria da Computação** foi oferecida de forma remota, adotando uma abordagem moderna e interativa de aprendizagem, com a metodologia **PBL (Problem-Based Learning)**. O objetivo central foi estimular o pensamento crítico e a resolução de problemas por meio de situações práticas que aproximam teoria e aplicações do mundo real.

Diversas ferramentas foram utilizadas para compor uma experiência rica e colaborativa:

* **Google Colab**: disponibilização de materiais e exercícios práticos.
* **Meet, Discord e WhatsApp**: tutorias em tempo real e fóruns de perguntas e respostas.
* **Moodle**: plataforma para distribuição de conteúdo, envio de atividades e discussões assíncronas.
* **E-mail**: canal adicional de comunicação para suporte individual.

A integração dessas ferramentas garantiu flexibilidade e acessibilidade, favorecendo um ambiente propício ao desenvolvimento de competências essenciais em Teoria da Computação.

## Ementa da Disciplina

A disciplina oferece uma introdução abrangente à teoria de linguagens formais e da computação. Explora conceitos fundamentais de linguagens formais, iniciando pela hierarquia de Chomsky e avançando por linguagens regulares e livres de contexto. São examinados modelos-chave de computação, incluindo expressões regulares, autômatos finitos determinísticos e não determinísticos, e autômatos com pilha.

Os estudantes também estudam gramáticas livres de contexto, além de técnicas fundamentais de análise léxica e sintática relevantes ao processamento de linguagens de programação. A disciplina introduz as máquinas de Turing como modelo formal de computação e discute linguagens recursivamente enumeráveis e recursivas, decidibilidade e indecidibilidade.

Por meio de exemplos práticos e discussão teórica, os estudantes examinam o **Problema da Parada** e a **Tese de Church**, entendendo suas implicações sobre o que pode ou não ser computado. A disciplina conclui com uma visão geral de conceitos básicos em complexidade computacional, incluindo classes de problemas decidíveis e indecidíveis no âmbito da hierarquia de Chomsky.

## Objetivos da Disciplina

### Objetivo Geral

Proporcionar aos estudantes o conhecimento das linguagens definidas na **hierarquia de Chomsky** e suas relações com os modelos formais da **Teoria da Computação**.

### Objetivos Específicos

Desenvolver as seguintes habilidades e competências:

* Reconhecer os conceitos de alfabeto, palavra e linguagem.
* Manipular linguagens, reconhecedores e gramáticas.
* Desenvolver autômatos finitos, autômatos com pilha e máquinas de Turing.
* Relacionar autômatos aos módulos de análise de um compilador de linguagens de programação.
* Compreender os limites da Computação.
* Reconhecer a aplicação da Tese de Church.
* Compreender as classes de problemas **P**, **NP** e **NP-Completo**.

### Competências Adicionais com a Metodologia PBL

Com a adoção do **Problem-Based Learning (PBL)**, a disciplina também visa:

* Conceituar situações-problema usando ferramentas da Teoria da Computação.
* Propor representações e soluções computacionais formais para problemas do mundo real.
* Avaliar a aplicação de formalismos com diferentes poderes de expressão para representar e resolver os problemas apresentados.

## Conteúdos da Disciplina

1. Motivação para o Estudo de Linguagens Formais

   * Hierarquia de Chomsky
   * Especificação de linguagens de programação e compiladores

2. Conceito de Linguagem Formal

   * Alfabeto, palavra, fecho de Kleene, linguagem

3. Linguagens Regulares

   * Expressões regulares
   * Autômato finito determinístico (DFA)
   * Autômato finito não determinístico (NFA)
   * AFN com transições \$\lambda\$
   * Análise léxica de linguagens de programação

4. Linguagens Livres de Contexto

   * Autômato com pilha
   * Gramáticas livres de contexto (GLCs)
   * Árvores de derivação
   * Ambiguidade em GLCs
   * Análise sintática de linguagens de programação

5. Linguagens Recursivas e Recursivamente Enumeráveis

   * Máquina de Turing
   * Tese de Church
   * Linguagem da parada

6. Problemas P, NP e NP-Completo

## Metodologia de Ensino e Aprendizagem

A disciplina seguirá uma metodologia ativa baseada em problemas, na qual cada unidade de aprendizagem é estruturada em torno da solução colaborativa de um problema. As atividades incluirão tutorias síncronas e discussões assíncronas via o **Ambiente Virtual de Aprendizagem (AVA)** adotado.

Especificamente, será utilizada uma abordagem híbrida, combinando atividades síncronas e assíncronas no AVA, composta por:

* Aulas dialogadas
* Videoaulas
* Atividades, exercícios e problemas
* Discussões em grupo sobre problemas, atividades e exercícios
* Tutorais síncronas com grupos de estudantes

## Competências-Alvo da Disciplina

As competências-alvo especificam as **habilidades observáveis** que os estudantes devem demonstrar à medida que progridem desde a compreensão até o **projeto, análise, validação e comunicação** de modelos computacionais. Alinhada aos conteúdos e à abordagem **PBL**, cada competência integra conhecimentos (linguagens e modelos formais), habilidades (modelagem, análise, implementação, teste) e disposições (rigor, colaboração, responsabilidade). As evidências são produzidas por meio de **simulações de autômatos/máquinas de Turing**, raciocínio formal sobre **expressividade e limites da computação** e um **relatório técnico** que documenta decisões de projeto, testes e justificativas.

Para maior clareza, as competências (C01–C16) estão organizadas em temas complementares; a numeração **não** implica sequência rígida:

* **Modelagem e Construção:** C01, C06 (FSMs), C12 (PDAs), C07 (TMs).
* **Expressividade e Mapeamentos:** C04 (regex ↔ FA), C13 (notação baseada em regras), C14 (classificações de gramáticas).
* **Variantes e Análise de Capacidades:** C08–C09 (variantes de MT), C16 (capacidades do sistema), C15 (Problema da Parada).
* **Determinismo e Padrões:** C02 (DFAs e justificativa), C11 (identificação de padrões em FSMs).
* **Verificação e Comunicação:** C03, C10 (testes com ferramentas), C05 (relatório técnico).

A avaliação enfatiza **correção, completude e aderência às especificações formais**, bem como a capacidade de **justificar escolhas**, comparar alternativas e **comunicar resultados** com clareza.

### Competências-Chave

* **C01 – Desenvolver soluções de problemas usando Autômatos**
  Capacidade de interpretar requisitos e projetar soluções baseadas em autômatos (FA, PDA, TM), validando modelos frente a especificações formais e casos de teste representativos.

* **C02 – Justificar o uso de Autômatos Finitos Determinísticos (DFAs)**
  Analisar restrições do problema para argumentar quando DFAs são apropriados, explicando os trade-offs do determinismo e seus impactos no projeto, na complexidade e na implementação.

* **C03 – Testar autômatos usando simuladores**
  Utilizar ferramentas (por exemplo, JFLAP) para simular autômatos, elaborando testes sistemáticos para verificar correção, completude e conformidade com a especificação.

* **C04 – Definir Expressões Regulares para Autômatos Finitos**
  Traduzir o comportamento de um autômato em expressões regulares equivalentes (e vice-versa) e validar a equivalência com casos de borda.

* **C05 – Escrever um relatório técnico**
  Produzir um relatório estruturado (por exemplo, formato SBC) documentando decisões de projeto, estratégias de implementação, experimentos/simulações, resultados e justificativas.

* **C06 – Desenvolver soluções de problemas usando Máquinas de Estados Finitos (FSMs)**
  Modelar o comportamento do sistema com FSMs para atender requisitos estabelecidos, assegurando verificabilidade e confiabilidade por meio de raciocínio formal e testes.

* **C07 – Desenvolver soluções de problemas usando Máquinas de Turing**
  Especificar e implementar modelos de Máquina de Turing que processem ou classifiquem entradas, mapeando requisitos para operações formais e demonstrando correção.

* **C08 – Identificar variantes de Máquinas de Turing**
  Reconhecer e caracterizar variantes (por exemplo, multi-fita, não determinística e outras extensões), comparando poder computacional e restrições.

* **C09 – Aplicar variantes de Máquinas de Turing**
  Selecionar e aplicar variantes de MT adequadas para resolver problemas de forma eficiente, justificando adequação e trade-offs em relação ao modelo padrão.

* **C10 – Testar Máquinas de Turing usando simuladores**
  Simular e avaliar MTs com ferramentas dedicadas, verificando correção, condições de terminação e aderência à especificação formal.

* **C11 – Identificar padrões em Máquinas de Estados Finitos**
  Analisar a estrutura e o comportamento de FSMs para detectar padrões, redundâncias e relações entre entradas, transições e configurações de estados que orientem ajustes de complexidade.

* **C12 – Desenvolver soluções de problemas usando Autômatos com Pilha**
  Projetar modelos baseados em AP para problemas livres de contexto, explicitando o comportamento da pilha e validando condições de aceitação.

* **C13 – Interpretar notação baseada em regras**
  Ler e raciocinar sobre formalismos baseados em regras (por exemplo, regras de produção, tabelas de transição), relacionando-os ao comportamento de autômatos/expressões regulares.

* **C14 – Diferenciar classificações de gramáticas formais**
  Classificar gramáticas na hierarquia de Chomsky e relacionar cada classe aos seus reconhecedores e ao seu poder de expressão.

* **C15 – Compreender o Problema da Parada e suas implicações**
  Explicar decidibilidade e indecidibilidade por meio do Problema da Parada, utilizando reduções para raciocinar sobre limites de problemas.

* **C16 – Aplicar conceitos de Máquina de Turing para analisar capacidades de sistemas computacionais**
  Utilizar a teoria de MT para classificar problemas como computáveis, semidecidíveis ou indecidíveis e para raciocinar sobre capacidades/limites de sistemas práticos.

## Avaliação da Aprendizagem

O desempenho discente será avaliado com base em:

* Participação ativa em atividades, fóruns e wikis

* Realização de exercícios e/ou quizzes

* Desenvolvimento de soluções para problemas

* Autoavaliação individual

* Avaliação pelos pares

* As avaliações utilizam escala de 0 a 10

## Referências

**Referências Básicas**
INTRODUÇÃO À TEORIA DA COMPUTAÇÃO. MICHAEL SIPSER. 2ª EDIÇÃO NORTE-AMERICANA. THOMSON.

Linguagens Formais: Teoria, Modelagem e Implementação. Marcus Vinícius Midena Ramos, João José Neto, Ítalo Santiago Vega. Editora Bookman. 2009.

Compiladores: princípios e práticas. LOUDEN, Kenneth C. São Paulo: Thomson Pioneira, 2004.

**Referências Complementares**
Introdução à Teoria de Autômatos, Linguagens e Computação. John E. Hopcroft, Jeffery D. Ullman; Rajeev Motwani. Tradução da segunda edição americana. Editora Campus. 2003.

Linguagens Formais e Autômatos. Paulo Blauth Menezes. Editora Sagra Luzzatto. Série Livros Didáticos – Instituto de Informática da UFRGS.

ELEMENTOS DE TEORIA DA COMPUTAÇÃO (ORIGINAL: ELEMENTS OF THE THEORY OF COMPUTATION. PRENTICE-HALL, INC., 1998). HARRY R. LEWIS, CHRISTOS H. PAPADIMITRIOU. EDITORA BOOKMAN.

Machines, Languages and Computation. Peter J. Denning; Jack B. Dennis; Joseph E. Qualitz. Prentice-Hall. 1978.

Compilers: Principles, Techniques, and Tools. Alfred V., Monica S. Lam, Ravi Sethi, Jeffrey D. Ullman. Addison Wesley; 2nd edition, 2008.
