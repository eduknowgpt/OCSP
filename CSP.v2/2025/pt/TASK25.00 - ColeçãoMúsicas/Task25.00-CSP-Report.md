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
Ao final desta atividade, os estudantes deverão ser capazes de:

> Definir formalmente e empregar corretamente os conceitos de alfabeto, cadeia, linguagem, linguagem vazia e fecho de linguagens, dentro de um arcabouço matemático preciso.

> Aplicar operações algébricas sobre cadeias e linguagens, incluindo concatenação, união, interseção, complemento, reversão e fecho de Kleene, interpretando seus efeitos em contextos concretos.

> Analisar e justificar propriedades de linguagens, tais como finitude ou infinitude, utilizando argumentos formais e contraexemplos quando apropriado.

> Identificar padrões estruturais em sequências simbólicas e argumentar sobre propriedades de linguagens induzidas por restrições do mundo real.

> Modelar artefatos musicais do mundo real (partituras, gravações, gêneros) como linguagens formais, por meio de codificações simbólicas e homomorfismos adequados.

> Construir e analisar autômatos finitos para reconhecer linguagens definidas por estruturas ou critérios musicais.

> Simular autômatos e operações sobre linguagens para validar resultados de reconhecimento e classificação.

> Elaborar um relatório técnico matematicamente rigoroso, apresentando definições, exemplos, demonstrações e raciocínios formais de forma clara, coerente e precisa.


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

Para garantir uma modelagem sistemática e semanticamente consistente dos conhecimentos envolvidos, esta enumeração adota o **ACM CS2023** como vocabulário controlado para o conhecimento computacional disciplinar e o **ACM Computing Curricula 2020 (CC2020)** como referência para o Conhecimento Profissional Fundamental (FPK).
Esses elementos constituem a dimensão Conhecimento (K) do modelo OntoKSD para a tarefa Coleção de Músicas.

A identificação dos componentes a seguir baseia-se nas exigências de modelagem formal, argumentação matemática e análise teórica de linguagens presentes na tarefa.


### Conhecimento em Computação (Alinhado ao CS2023)

- Linguagens Formais
  - Alfabetos, cadeias, linguagens e linguagem vazia.
  - Linguagens finitas e infinitas.
  - Subcadeias, prefixos e sufixos.

- Operações sobre Linguagens
  - União, interseção e complemento.
  - Concatenação e fecho de Kleene.
  - Reversão de cadeias e linguagens.
  - Propriedades de fechamento de classes de linguagens.

- Linguagens Regulares
  - Expressões regulares e sua semântica formal.
  - Equivalência entre expressões regulares e autômatos finitos.

- Autômatos Finitos
  - Autômatos finitos determinísticos e não determinísticos (DFA/NFA).
  - Reconhecimento de linguagens e equivalência entre autômatos.
  - Poder expressivo e limitações dos autômatos finitos.

- Homomorfismos e Codificações
  - Mapeamentos formais entre representações simbólicas.
  - Preservação de propriedades linguísticas sob homomorfismos.
  - Limites da equivalência representacional (ex.: partitura e gravação).

- Raciocínio Formal e Técnicas de Prova
  - Uso de definições precisas e exemplos mínimos.
  - Construção de argumentos formais e contraexemplos.
  - Justificação rigorosa de propriedades e operações sobre linguagens.


### Conhecimento Profissional Fundamental (FPK — CC2020)

- Pensamento Analítico e Crítico
  - Abstração de domínios do mundo real em modelos formais.
  - Avaliação rigorosa da validade de afirmações matemáticas.

- Comunicação Escrita Técnica
  - Produção de textos claros, estruturados e matematicamente precisos.
  - Uso adequado de notação formal e terminologia da Teoria da Computação.

- Rigor Epistêmico
  - Compromisso com justificativas formais em detrimento de intuições informais.
  - Clareza na distinção entre definições, exemplos, propriedades gerais e exceções.





## 3. Learning Objectives Identification

Com base no enunciado da tarefa **Coleção de Músicas**, os objetivos de aprendizagem foram definidos para refletir com precisão as **exigências conceituais**, o **nível de rigor matemático** e o **tipo de competência esperada** na disciplina **MATC94 – Introdução às Linguagens Formais e Teoria da Computação**.



### 3.1 General Learning Objective

O objetivo geral desta tarefa é capacitar o estudante a abstrair e modelar um domínio do mundo real (músicas e coleções musicais) como linguagens formais, empregando conceitos fundamentais de linguagens, autômatos e expressões regulares, bem como a analisar e justificar propriedades estruturais por meio de definições formais, operações sobre linguagens e argumentação matemática rigorosa, sem recorrer a intuições informais ou implementações algorítmicas ad hoc.



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
6.3 Diferenciar, em nível conceitual, gramáticas regulares e gramáticas livres de contexto, indicando seus limites expressivos, sem exigir construção formal de gramáticas livres de contexto. 

#### LO7 — Automata and Model Equivalence (Theoretical and Conceptual Level)
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
10.3 Distinguir explicitamente entre **intuição informal, exemplo ilustrativo e prova formal**.


### 3.3 Importance of These Objectives

Esses objetivos estabelecem um percurso estruturado de desenvolvimento de competências conceituais e analíticas, assegurando que o estudante:

- construa uma base teórica consistente em Linguagens Formais e Teoria da Computação, fundamentada em definições precisas e modelos formais;

- desenvolva a capacidade de abstrair e formalizar domínios do mundo real, traduzindo fenômenos concretos em representações matemáticas rigorosas;

- compreenda e analise propriedades estruturais, relações de equivalência e limites expressivos das linguagens formais;

- exercite pensamento analítico, argumentação lógica e rigor epistêmico, essenciais para a validação de afirmações em contextos teóricos;

- consolide habilidades de comunicação técnica, expressando raciocínios, modelos e justificativas de forma clara, coerente e matematicamente fundamentada.

Ao atingir esses objetivos, o estudante estará apto a articular teoria e prática de maneira consciente e crítica, utilizando conceitos de Linguagens Formais, Expressões Regulares e Autômatos Finitos para analisar, justificar e resolver problemas conceituais complexos, com clareza formal, precisão terminológica e consistência lógica.




## 4. Competency Definition

> Competências Reutilizadas e Especializadas do Conjunto de Referência

### C02 – Justify the use of Deterministic Finite Automata (DFAs)
- Relevância: Justificar propriedades de linguagens por meio de DFAs

- LO3.2, LO3.4, LO4.3, LO7.1

### C04 — Define Regular Expressions for Finite Automata

- Relevância: Definição formal de conjuntos de músicas (ex.: músicas com “amor”, música vazia, repetição de músicas).

- LO6.1, LO6.2, LO7.1


### C11 — Identify Patterns in Finite State Machines

- Relevância: Identificação de padrões como prefixos fixos (“20 primeiras notas”), repetições (Kleene) e substrings.

- LO3.2, LO4.1, LO6.1, LO7.2


### C14 — Differentiate classifications of formal grammars

- Relevância: Diferenciação entre linguagens regulares e possíveis limites expressivos.

- LO6.1, LO6.3


### C13′ — Interpret and apply algebraic notation for strings and languages

- Especialização de: C13 – Interpret rule-based notation

- Descrição : Interpretar, aplicar e justificar o uso de notações algébricas formais de strings (ε, Σ, |x|, concatenação, potência, reverso, subcadeias) e de linguagens (∪, ∩, complemento, concatenação, Lⁿ, L*, prefixos/sufixos, homomorfismos).

- Verbos observáveis: explain, apply, compute, derive, justify

- Disposições: meticulous, responsible

- LO1.1, LO1.2, LO1.3, LO2.1, LO2.2, LO3.1, LO3.3, LO4.2, LO5.1, LO6.2, LO8.1


### C05′ — Write mathematically rigorous answers

- Especialização de: C05 – Write a technical report

- Descrição: Produzir respostas matematicamente rigorosas, com definições formais, exemplos mínimos, demonstrações, uso explícito de propriedades (ex.: fecho) e contraexemplos, quando apropriado.

- Verbos observáveis: define, justify, prove, exemplify, refute

- Disposições: meticulous, responsible

- LO2.3, LO5.2, LO5.3, LO8.3, LO9.1, LO9.2, LO9.3, LO9.4, LO10.2, LO10.3




> Novas Competências

### Competency C17 Specification  


### Competency Title
    Apply operations on formal languages

### Textual Description  

This competency involves the learner’s ability to apply, analyze, and justify formal operations on languages, including concatenation, union, intersection, complement, Kleene closure, and reversal, and to reason about their structural effects and closure properties using precise mathematical definitions and arguments.

Os aprendizes devem evidenciar a capacidade de empregar corretamente operações formais sobre linguagens, analisando pertinência, validade e consequências estruturais, e justificando formalmente suas conclusões por meio de exemplos, contraexemplos e propriedades teóricas.

- Alinhamento CS2023: TC.FLR — Formal Languages and Recognizers

- LO2.1, LO2.2, LO3.1, LO3.2, LO3.3, LO3.4, LO4.1, LO4.2, LO4.3, LO5.1, LO5.2, LO9.4


### Knowledge Specification

The following knowledge components are essential for demonstrating this competency:

### Computing Knowledge (CS2023)

- Language Theory
  - Alphabets, strings, and languages.
  - Finite and infinite languages.
  - Conceptual foundations of formal language models.

- Operations on Formal Languages
  - Union, intersection, and complement.
  - Concatenation and Kleene closure.
  - Reversal of strings and languages.
  - Closure properties of language classes.

- Regular Expressions
  - Algebraic representation of regular languages.
  - Correspondence between regular expressions and language operations.



### Professional Knowledge (FPK — CC2020)

- Analytical and Critical Thinking
  - Decomposition of formal problems.
  - Evaluation of the validity and consequences of formal constructions.
  - Justification of claims using precise mathematical reasoning.


### Disposition Specification

The following dispositions support the effective demonstration of this competency:

- Epistemic Rigor
  - Commitment to formal justification rather than intuitive reasoning.
  - Careful distinction between definitions, examples, and general properties.

- Responsibility
  - Accuracy in the application of definitions and operations.
  - Consistency and coherence in formal arguments.

- Persistence
  - Willingness to revisit definitions and reasoning steps to resolve inconsistencies.


### Knowledge-Skill Pairing and Bloom’s Taxonomy Alignment

This competency requires the following Knowledge–Skill (K–S) pairings:

- Language Theory → Understand
  - Interpret and explain formal definitions and foundational properties of languages.

- Operations on Formal Languages → Apply / Analyze
  - Execute formal operations on languages and determine their results within a defined universe.

- Regular Expressions → Apply
  - Use algebraic notation to specify, compose, and manipulate regular languages.

- Analytical and Critical Thinking (FPK) → Analyze
  - Examine formal arguments, identify inconsistencies, and assess the validity of claims.



**Verb Annotation**  
To clarify competency expectations, the following Bloom-aligned verb annotations are associated with each Knowledge–Skill pairing:

Understand (Language Theory)
→ interpret, explain, identify, describe

Apply (Operations on Formal Languages)
→ apply, execute, compute, derive

Apply (Regular Expressions)
→ use, compose, specify, manipulate

Analyze (Analytical and Critical Thinking – FPK)
→ analyze, justify, differentiate, examine



### Summary Table for Competency C17

| **Competency** | **Dispositions** | **Knowledge** | **Skill (Bloom + Verb Annotation)** |
|---------------|-----------------|---------------|-------------------------------------|
| **Apply operations on formal languages** | Epistemic rigor; Intellectual responsibility; Persistence | Language Theory | **Understand** *(interpret, explain, identify, describe)* |
|  |  | Operations on Formal Languages | **Apply** *(apply, execute, compute, derive)* |
|  |  | Regular Expressions | **Apply** *(use, compose, specify, manipulate)* |
|  |  | Analytical and Critical Thinking (FPK) | **Analyze** *(analyze, justify, differentiate, examine)* |









## Competency C18 Specification

### Competency Title
**Model real-world problems using formal language concepts**



### Textual Description

This competency involves the learner’s ability to **abstract elements of a real-world domain and model them as formal languages**, by defining **alphabets, strings, and languages** that represent relevant structural aspects of the problem.

Learners must demonstrate the capacity to **establish explicit mappings between concrete entities and formal symbols**, to **justify modeling decisions**, and to **analyze the adequacy and limitations** of the resulting formal representation, clearly distinguishing **structural properties** from **semantic interpretations**.



### Curricular Alignment

- **CS2023 Knowledge Area:**  
  **TC.FLR — Formal Languages and Recognizers**

- **Related Learning Objectives:**  
  LO1.1, LO1.2, LO1.3,  
  LO5.3,  
  LO8.2



### Knowledge Specification

#### Computing Knowledge (CS2023)

- **Language Theory**
  - Alphabets, strings, and languages.
  - Conceptual foundations for formal abstraction of real-world domains.

- **Formal Languages**
  - Modeling collections as sets of strings.
  - Structural properties of languages independent of semantics.

- **Homomorphisms and Codifications**
  - Formal mappings between symbolic representations.
  - Preservation and loss of information under encoding.

#### Professional Knowledge (FPK — CC2020)

- **Analytical and Critical Thinking**
  - Identification of relevant domain features.
  - Evaluation of modeling choices and their formal consequences.



### Disposition Specification

- **Epistemic Rigor**
  - Commitment to precise definitions and explicit assumptions.
  - Avoidance of informal or ambiguous representations.

- **Intellectual Responsibility**
  - Careful justification of modeling decisions.
  - Awareness of the scope and limits of formal models.

- **Reflectiveness**
  - Ability to distinguish structural correctness from semantic interpretation.



### Knowledge–Skill Pairing and Bloom’s Taxonomy Alignment

- **Language Theory** → **Understand**  
  *(interpret and explain relationships between real-world domains and formal representations)*

- **Formal Languages** → **Apply**  
  *(model domains using alphabets, strings, and languages)*

- **Homomorphisms and Codifications** → **Apply**  
  *(map and encode domain entities into symbolic representations)*

- **Analytical and Critical Thinking (FPK)** → **Analyze**  
  *(evaluate adequacy, identify limitations, and justify modeling choices)*



### Verb Annotation (Bloom-Aligned)

- **Understand** → *interpret, explain, identify, describe*  
- **Apply** → *model, encode, represent, construct*  
- **Analyze** → *analyze, justify, differentiate, evaluate*



### Summary Table for Competency C18

| **Competency** | **Dispositions** | **Knowledge** | **Skill (Bloom + Verb Annotation)** |
|---------------|-----------------|---------------|-------------------------------------|
| **Model real-world problems using formal language concepts** | Epistemic rigor; Intellectual responsibility; Reflectiveness | Language Theory | **Understand** *(interpret, explain, identify, describe)* |
|  |  | Formal Languages | **Apply** *(model, encode, represent, construct)* |
|  |  | Homomorphisms and Codifications | **Apply** *(map, encode, transform, represent)* |
|  |  | Analytical and Critical Thinking (FPK) | **Analyze** *(analyze, justify, differentiate, evaluate)* |






## Competency C19 Specification

### Competency Title
**Apply homomorphisms in formal languages**



### Textual Description

This competency involves the learner’s ability to **define and apply homomorphisms over strings and languages**, using **formal codifications to translate symbolic representations** between different domains.

Learners must demonstrate the capacity to **apply homomorphisms to symbols, strings, and languages**, to **analyze which structural properties are preserved or altered**, and to **justify the limits of formal equivalence** between different representations, clearly distinguishing **formal correspondence** from **semantic interpretation**.



### Curricular Alignment

- **CS2023 Knowledge Area:**  
  **TC.FLR — Formal Languages and Recognizers**

- **Related Learning Objectives:**  
  LO8.1, LO8.2, LO8.3



### Knowledge Specification

#### Computing Knowledge (CS2023)

- **Formal Languages**
  - Alphabets, strings, and languages.
  - Structural properties of languages.

- **Homomorphisms**
  - Definition of homomorphisms over alphabets and strings.
  - Extension of homomorphisms to languages.
  - Preservation and transformation of language properties.

- **Codifications**
  - Formal encodings between symbolic representations.
  - Conditions for equivalence and non-equivalence between representations.

#### Professional Knowledge (FPK — CC2020)

- **Analytical and Critical Thinking**
  - Evaluation of formal mappings and their consequences.
  - Identification of preserved and non-preserved properties.



### Disposition Specification

- **Epistemic Rigor**
  - Commitment to precise definitions of mappings and functions.
  - Avoidance of informal or intuitive notions of equivalence.

- **Intellectual Responsibility**
  - Careful justification of claims about equivalence and transformation.
  - Awareness of formal limitations of codifications.

- **Reflectiveness**
  - Ability to distinguish structural correspondence from semantic meaning.



### Knowledge–Skill Pairing and Bloom’s Taxonomy Alignment

- **Formal Languages** → **Understand**  
  *(interpret the structure of languages and their properties)*

- **Homomorphisms** → **Apply**  
  *(define and apply homomorphisms to symbols, strings, and languages)*

- **Codifications** → **Apply**  
  *(encode and translate representations using formal mappings)*

- **Analytical and Critical Thinking (FPK)** → **Analyze**  
  *(analyze preserved properties and justify limits of equivalence)*



### Verb Annotation (Bloom-Aligned)

- **Understand** → *interpret, explain, identify, describe*  
- **Apply** → *define, apply, encode, transform*  
- **Analyze** → *analyze, justify, differentiate, evaluate*



### Summary Table for Competency C19

| **Competency** | **Dispositions** | **Knowledge** | **Skill (Bloom + Verb Annotation)** |
|---------------|-----------------|---------------|-------------------------------------|
| **Apply homomorphisms in formal languages** | Epistemic rigor; Intellectual responsibility; Reflectiveness | Formal Languages | **Understand** *(interpret, explain, identify, describe)* |
|  |  | Homomorphisms | **Apply** *(define, apply, encode, transform)* |
|  |  | Codifications | **Apply** *(encode, translate, map, represent)* |
|  |  | Analytical and Critical Thinking (FPK) | **Analyze** *(analyze, justify, differentiate, evaluate)* |





## Competency C20 Specification

### Competency Title

    Model and analyze musical collections as formal languages


### Textual Description

This task-level competency involves the learner’s ability to **integrate formal language concepts, operations, and representations** to **model musical collections as formal languages** and to **analyze their structural properties** through rigorous mathematical reasoning.

Learners must demonstrate the capacity to **abstract musical artifacts into symbols, strings, and languages**, to **apply algebraic operations and regular expressions**, and to **justify formal properties and limitations** using precise definitions, examples, and logical argumentation.  
This competency synthesizes multiple atomic competencies into a **coherent formal analysis of a real-world problem**.

 

### Competency Composition

This is a **composite competency** formed by the integration of the following competencies:

- **C18** — Model real-world problems using formal language concepts  
- **C17** — Apply operations on formal languages  
- **C19** — Apply homomorphisms in formal languages  
- **C04** — Specify languages using regular expressions  
- **C05′** — Produce mathematically rigorous technical documentation  
- **C13′** — Justify formal properties using logical and mathematical argumentation

 

### Curricular Alignment

- **CS2023 Knowledge Area:**  
  **TC.FLR — Formal Languages and Recognizers**

- **Task Association:**  
  Task25.00 — *Music Collection*

 

### Knowledge Specification

#### Computing Knowledge (CS2023)

- **Language Theory**
  - Foundations of formal modeling using languages.

- **Formal Languages**
  - Alphabets, strings, and languages.
  - Operations on languages and closure properties.

- **Regular Expressions**
  - Algebraic specification of regular languages.

- **Homomorphisms and Codifications**
  - Formal mappings between symbolic representations.

#### Professional Knowledge (FPK — CC2020)

- **Analytical and Critical Thinking**
  - Integration and evaluation of formal models.
  - Justification of properties and modeling decisions.

- **Technical Written Communication**
  - Formal documentation of definitions, reasoning, and conclusions.

 

### Disposition Specification

- **Epistemic Rigor**
  - Commitment to formal definitions and logical justification.

- **Intellectual Responsibility**
  - Accuracy and coherence in formal modeling and analysis.

- **Reflectiveness**
  - Awareness of modeling assumptions and limitations.

- **Persistence**
  - Willingness to refine models and arguments when inconsistencies arise.

 

### Knowledge–Skill Pairing and Bloom’s Taxonomy Alignment

- **Language Theory** → **Understand**  
  *(interpret foundational concepts of formal modeling)*

- **Formal Languages** → **Apply**  
  *(model musical collections and apply operations)*

- **Regular Expressions** → **Apply**  
  *(specify languages algebraically)*

- **Homomorphisms and Codifications** → **Apply**  
  *(map between symbolic representations)*

- **Analytical and Critical Thinking (FPK)** → **Analyze**  
  *(integrate, evaluate, and justify formal models)*

- **Technical Written Communication (FPK)** → **Create**  
  *(produce a coherent and rigorous technical report)*

 

### Verb Annotation (Bloom-Aligned)

- **Understand** → *interpret, explain, identify*  
- **Apply** → *model, apply, specify, encode*  
- **Analyze** → *analyze, integrate, justify, evaluate*  
- **Create** → *document, articulate, synthesize, present*

 

### Summary Table for Competency CT25.00

| **Competency** | **Dispositions** | **Knowledge** | **Skill (Bloom + Verb Annotation)** |
|---------------|-----------------|---------------|-------------------------------------|
| **Model and analyze musical collections as formal languages** | Epistemic rigor; Intellectual responsibility; Reflectiveness; Persistence | Language Theory | **Understand** *(interpret, explain, identify)* |
|  |  | Formal Languages | **Apply** *(model, apply, compose, derive)* |
|  |  | Regular Expressions | **Apply** *(specify, compose, manipulate)* |
|  |  | Homomorphisms and Codifications | **Apply** *(encode, map, transform)* |
|  |  | Analytical and Critical Thinking (FPK) | **Analyze** *(analyze, integrate, justify, evaluate)* |
|  |  | Technical Written Communication (FPK) | **Create** *(document, synthesize, present)* |






### Mapeamento LO x Competências

Competencies are specified based on the **Learning Objectives (LOs)** identified in the task analysis.


| LO         | Descrição sintética do LO                                         | Competências atendidas |
| ---------- | ----------------------------------------------------------------- | ---------------------- |
| **LO1.1**  | Definir formalmente um alfabeto (Σ) a partir de símbolos musicais | **C18**, C13′          |
| **LO1.2**  | Modelar uma música como cadeia sobre Σ                            | **C18**, C13′          |
| **LO1.3**  | Modelar coleção de músicas como linguagem L ⊆ Σ*                  | **C18**, C13′          |
| **LO2.1**  | Identificar prefixos, sufixos e subcadeias                        | **C13′**, C17          |
| **LO2.2**  | Determinar se um trecho é música válida                           | **C13′**, C17          |
| **LO2.3**  | Justificar validade estrutural de trechos                         | **C05′**, C13′         |
| **LO3.1**  | Aplicar concatenação de cadeias                                   | **C17**, C13′          |
| **LO3.2**  | Avaliar se concatenação preserva linguagem                        | **C17**, **C02**, C11  |
| **LO3.3**  | Aplicar união, interseção e diferença                             | **C17**, C13′          |
| **LO3.4**  | Avaliar complemento de linguagem                                  | **C17**, **C02**       |
| **LO4.1**  | Aplicar fecho de Kleene (L*)                                      | **C17**, C11           |
| **LO4.2**  | Interpretar papel da cadeia vazia (ε)                             | **C13′**, C17          |
| **LO4.3**  | Classificar linguagem como finita ou infinita                     | **C17**, **C02**       |
| **LO5.1**  | Definir formalmente reversão de cadeias                           | **C13′**, C17          |
| **LO5.2**  | Aplicar reversão e analisar validade                              | **C17**, C05′          |
| **LO5.3**  | Distinguir validade estrutural vs. semântica                      | **C05′**, C18          |
| **LO6.1**  | Reconhecer linguagens regulares                                   | **C04**, **C14**, C11  |
| **LO6.2**  | Especificar linguagens por expressões regulares                   | **C04**, C13′          |
| **LO6.3**  | Distinguir gramáticas regulares e CF                              | **C14**                |
| **LO7.1**  | Explicar equivalência FA–RE–Gramáticas                            | **C04**, **C02**       |
| **LO7.2**  | Relacionar padrões a estados/transições                           | **C11**, C02           |
| **LO8.1**  | Definir homomorfismos de cadeias                                  | **C19**, C13′          |
| **LO8.2**  | Analisar partitura ↔ gravação como codificação                    | **C19**, **C18**       |
| **LO8.3**  | Justificar limites da intercambialidade                           | **C19**, **C05′**      |
| **LO9.1**  | Usar definições formais corretamente                              | **C05′**               |
| **LO9.2**  | Construir exemplos mínimos                                        | **C05′**               |
| **LO9.3**  | Construir contraexemplos                                          | **C05′**               |
| **LO9.4**  | Aplicar raciocínio indutivo                                       | **C05′**, C17          |
| **LO10.1** | Elaborar relatório técnico estruturado                            | **C05**                |
| **LO10.2** | Produzir justificativas claras e rigorosas                        | **C05′**               |
| **LO10.3** | Distinguir intuição, exemplo e prova                              | **C05′**               |

