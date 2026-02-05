# Competency Lifecycle — C18 - *Model real-world problems using formal language concepts*



## 1. Definição Original — *CSP-Report (Ciclo 1)*

### Competency Title

    Model real-world problems using formal language concepts

### Textual Description

Esta competência envolve a capacidade do aprendiz de **abstrair elementos de um domínio do mundo real** e **modelá-los como representações formais baseadas em linguagens**, por meio da definição explícita de **alfabetos, cadeias e linguagens** que capturem **aspectos estruturais relevantes** do problema.

Os aprendizes devem demonstrar a capacidade de:
- estabelecer **mapeamentos explícitos** entre entidades concretas e símbolos formais;
- **justificar decisões de modelagem**, incluindo escolhas e exclusões;
- analisar a **adequação estrutural** do modelo proposto;
- reconhecer e explicitar **limitações formais** da representação adotada.

Essa competência exige a **distinção clara entre propriedades estruturais e interpretações semânticas**, assumindo que a validade do modelo decorre de sua coerência formal, e não de sua correspondência intuitiva com o domínio original.

> Esta competência concentra-se na **fase de abstração e modelagem**, não envolvendo ainda a aplicação de operações formais (C17) nem a transformação entre representações por homomorfismos (C19).

- **Alinhamento CS2023**:  
  TC.FLR — Formal Languages and Recognizers

- **Learning Objectives atendidos**:  
  LO1.1, LO1.2, LO1.3,  
  LO5.3,  
  LO8.2



### Activation

- **ActivationRole**: `core`  
  A competência é **nuclear**, pois fundamenta toda a formalização do problema e antecede a aplicação de operações e análises estruturais.

- **ActivationMode**: `constructive`  
  O desempenho esperado envolve a **construção consciente de um modelo formal**, a partir de escolhas de abstração explicitamente justificadas.

- **ActivationConstraint**: `mandatory`  
  A Task25.00 não pode ser resolvida sem a modelagem formal inicial do domínio musical.



### Knowledge Specification

Os seguintes componentes de conhecimento são essenciais para a demonstração desta competência:

#### Computing Knowledge (CS2023)

- **Language Theory**
  - Alfabetos, cadeias e linguagens.
  - Fundamentos conceituais da abstração formal de domínios do mundo real.

- **Formal Languages**
  - Modelagem de coleções como conjuntos de cadeias.
  - Propriedades estruturais de linguagens independentes de semântica.

- **Homomorphisms and Codifications (nível conceitual)**
  - Noção de mapeamentos formais entre representações simbólicas.
  - Preservação e perda de informação sob codificação, como limite da modelagem.

#### Professional Knowledge (FPK — CC2020)

- **Analytical and Critical Thinking**
  - Identificação de características relevantes do domínio.
  - Avaliação crítica de escolhas de modelagem e de suas consequências formais.



### Disposition Specification

As seguintes disposições apoiam a demonstração efetiva desta competência:

- **Epistemic Rigor**
  - Compromisso com definições precisas e pressupostos explícitos.
  - Evitação de representações informais ou ambíguas.

- **Intellectual Responsibility**
  - Justificação consciente das decisões de abstração.
  - Reconhecimento do escopo e das limitações do modelo formal adotado.

- **Reflectiveness**
  - Capacidade de distinguir correção estrutural de adequação semântica.
  - Consciência de que todo modelo é uma aproximação formal do domínio.



### Knowledge–Skill Pairing and Bloom’s Taxonomy Alignment

- **Language Theory** → **Understand**  
  *(interpretar e explicar a relação entre domínios reais e representações formais)*

- **Formal Languages** → **Apply**  
  *(modelar domínios por meio de alfabetos, cadeias e linguagens)*

- **Homomorphisms and Codifications** → **Apply**  
  *(mapear entidades do domínio para símbolos formais, em nível conceitual)*

- **Analytical and Critical Thinking (FPK)** → **Analyze**  
  *(avaliar adequação, identificar limitações e justificar escolhas de modelagem)*



### Verb Annotation (Bloom-Aligned)

- **Understand** → *interpret, explain, identify, describe*  
- **Apply** → *model, represent, encode, construct*  
- **Analyze** → *analyze, justify, differentiate, evaluate*



### Summary Table for Competency C18

| **Competency** | **Dispositions** | **Knowledge** | **Skill (Bloom + Verb Annotation)** |
|---------------|-----------------|---------------|-------------------------------------|
| **Model real-world problems using formal language concepts** | Epistemic rigor; Intellectual responsibility; Reflectiveness | Language Theory | **Understand** *(interpret, explain, identify, describe)* |
|  |  | Formal Languages | **Apply** *(model, represent, construct)* |
|  |  | Homomorphisms and Codifications | **Apply** *(map, encode, represent)* |
|  |  | Analytical and Critical Thinking (FPK) | **Analyze** *(analyze, justify, differentiate, evaluate)* |



### Intenção Original

A competência **C18** foi inicialmente definida para explicitar a capacidade do aprendiz de **abstrair um domínio do mundo real** e **construir uma representação formal baseada em linguagens**, por meio da definição de **alfabetos, cadeias e linguagens**.

Na formulação original, a competência tinha como objetivos centrais:

- tornar explícita a **fase de abstração e modelagem**, frequentemente implícita em tarefas de Teoria da Computação;
- separar conceitualmente a **modelagem do domínio** da aplicação de operações formais e da análise de propriedades;
- permitir que decisões de abstração fossem **observáveis e justificáveis** como evidência de aprendizagem.

Desde sua concepção, a C18 foi pensada como uma competência **nuclear** em tarefas que envolvem a transposição de fenômenos do mundo real para estruturas formais.



### Características Identificadas (Ciclo 1)

- Ênfase clara em **abstração e modelagem formal**;
- Uso de verbos como *model*, *represent* e *construct*, indicando atividade de construção conceitual;
- Dependência explícita de **justificativa das escolhas de modelagem**;
- Risco inicial de sobreposição com:
  - competências de operações formais (posteriormente C17);
  - competências de transformação/codificação (posteriormente C19);
- Necessidade de distinguir **estrutura formal** de **interpretação semântica**.



## 2. Revisão por Especialistas — *CSRP-Report (Ciclo 1)*

### Principais Achados da Revisão

Durante a **Fase 2 (Expert Review)**, a competência C18 foi analisada à luz das evidências exigidas pela **TASK25.00 — Coleção de Músicas** e de tarefas conceitualmente similares.

Os principais pontos registrados foram:

- **Alta adequação epistemológica**  
  A competência corresponde diretamente à primeira etapa necessária para a resolução da tarefa, antecedendo qualquer análise algébrica.

- **Necessidade de delimitação de escopo**  
  Observou-se a necessidade de explicitar que C18 **não inclui**:
  - aplicação de operações formais (C17);
  - transformação entre representações por homomorfismos (C19).

- **Centralidade conceitual**  
  A ausência de uma competência como C18 levaria à diluição da fase de modelagem em outras competências, reduzindo clareza e rastreabilidade.

- **Evidência observável**  
  As decisões de abstração (definição de alfabeto, cadeia, linguagem e exclusões) aparecem explicitamente nas respostas esperadas.



### Recomendações dos Especialistas

Com base na revisão, foi recomendado que a competência C18:

- fosse **mantida como competência central (core)**;
- tivesse seu **escopo explicitamente restrito à fase de modelagem**;
- enfatizasse a **justificação das escolhas de abstração**;
- incorporasse explicitamente a análise das **limitações formais do modelo**;
- distinguisse claramente **correção estrutural** de **adequação semântica**.



### Limite de Decisão

📌 **Resultado do CSRP (Ciclo 1):**  
**Aprovada com Refinamento de Escopo e Clarificação Conceitual**



## 3. Ajustes Implementados — *CSP_Adjustments*

### Alterações Declaradas

Em resposta às recomendações da revisão, os seguintes ajustes foram aplicados à competência C18:

- **Delimitação explícita do escopo**
  - Inclusão textual clara de que a competência se restringe à **abstração e modelagem**, excluindo operações e transformações.

- **Reforço da justificativa de modelagem**
  - Ênfase na explicitação de escolhas, exclusões e simplificações adotadas no modelo formal.

- **Inclusão das limitações formais**
  - Reconhecimento explícito de que todo modelo possui limites estruturais.

- **Consolidação do papel funcional**
  - Confirmação da competência como **core**, antecedendo C17 e C19 no fluxo cognitivo da tarefa.



### Ativação Final (Ajustada)

- **ActivationRole**: `core`
- **ActivationMode**: `constructive`
- **ActivationConstraint**: `mandatory`



## 4. Versão Final — *Ciclo 2*

### Competency Title

    Model real-world problems using formal language concepts



### Descrição Textual Refinada

Esta competência refere-se à capacidade de **abstrair elementos de um domínio do mundo real** e **modelá-los como representações formais baseadas em linguagens**, por meio da definição explícita de **alfabetos, cadeias e linguagens** que capturem **aspectos estruturais relevantes** do problema.

Espera-se que os aprendizes sejam capazes de:

- estabelecer **mapeamentos explícitos** entre entidades do domínio e símbolos formais;
- **justificar decisões de modelagem**, incluindo escolhas e exclusões;
- analisar a **adequação estrutural** do modelo proposto;
- reconhecer e explicitar **limitações formais** da representação adotada.

A competência concentra-se exclusivamente na **fase de abstração e modelagem**, não envolvendo ainda a aplicação de operações formais (C17) nem transformações entre representações por homomorfismos (C19).



### Knowledge Specification (Final)

- **Language Theory**
  - Alfabetos, cadeias e linguagens.
  - Fundamentos da abstração formal de domínios reais.

- **Formal Languages**
  - Modelagem de coleções como conjuntos de cadeias.
  - Propriedades estruturais independentes de semântica.

- **Homomorphisms and Codifications (nível conceitual)**
  - Noção de mapeamentos formais.
  - Preservação e perda de informação como limite da modelagem.

- **Analytical and Critical Thinking (FPK)**



### Disposition Specification (Final)

- Epistemic Rigor  
- Intellectual Responsibility  
- Reflectiveness  



## 5. Knowledge–Skill Pairing (Final)

- **Language Theory — Understand**
  → interpretar e explicar a relação entre domínios reais e representações formais.

- **Formal Languages — Apply**
  → modelar domínios por meio de alfabetos, cadeias e linguagens.

- **Homomorphisms and Codifications — Apply (conceitual)**
  → mapear entidades do domínio para símbolos formais.

- **Analytical and Critical Thinking (FPK) — Analyze**
  → avaliar adequação estrutural, justificar escolhas e identificar limitações.



### Bloom’s Taxonomy Alignment (Final)

- **Language Theory — Understand**
- **Formal Languages — Apply**
- **Homomorphisms and Codifications — Apply**
- **Analytical and Critical Thinking — Analyze**



### Summary Table — Competency C18 (Final)

| **ID** | **Competency** | **Dispositions** | **Knowledge** | **Skill (Bloom)** |
|------|----------------|------------------|---------------|-------------------|
| C18 | **Model real-world problems using formal language concepts** | Epistemic rigor; Intellectual responsibility; Reflectiveness | Language Theory | **Understand (Interpret, Explain)** |
|     |                |                  | Formal Languages | **Apply (Model, Represent, Construct)** |
|     |                |                  | Homomorphisms & Codifications (conceptual) | **Apply (Map, Encode)** |
|     |                |                  | Analytical & Critical Thinking (FPK) | **Analyze (Evaluate, Justify)** |













