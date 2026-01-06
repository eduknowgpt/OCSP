# Competency Lifecycle — C19 - *Apply homomorphisms in formal languages*



## 1. Definição Original — *CSP-Report (Ciclo 1)*

### Competency Title

    Apply homomorphisms in formal languages



### Textual Description

Esta competência envolve a capacidade do aprendiz de **definir e aplicar homomorfismos sobre símbolos, cadeias e linguagens**, utilizando **codificações formais** para relacionar diferentes representações simbólicas de um mesmo domínio ou de domínios distintos.

Os aprendizes devem demonstrar a capacidade de:
- aplicar homomorfismos de forma consistente a alfabetos, cadeias e linguagens;
- **analisar quais propriedades estruturais são preservadas, modificadas ou perdidas** sob tais transformações;
- **justificar formalmente os limites da equivalência** entre representações, distinguindo claramente **correspondência estrutural** de **equivalência semântica**.

Essa competência opera em **nível conceitual**, sem exigir implementação computacional de funções de codificação, e assume os homomorfismos como **instrumentos teóricos de análise e justificação**, não como mecanismos operacionais.

- **Alinhamento CS2023**:  
  TC.FLR — Formal Languages and Recognizers

- **Learning Objectives atendidos**:  
  LO8.1, LO8.2, LO8.3



### Activation

- **ActivationRole**: `supporting`  
  A competência tem papel **de apoio**, sendo mobilizada para sustentar análises de equivalência e limites de codificação dentro da tarefa.

- **ActivationMode**: `interpretative`  
  O desempenho esperado envolve **interpretação e análise conceitual** das transformações formais e de seus efeitos estruturais.

- **ActivationConstraint**: `mandatory`  
  A competência é necessária sempre que a tarefa exige justificar relações entre diferentes representações simbólicas.



### Knowledge Specification

Os seguintes componentes de conhecimento são essenciais para a demonstração desta competência:

#### Computing Knowledge (CS2023)

- **Formal Languages**
  - Alfabetos, cadeias e linguagens.
  - Propriedades estruturais de linguagens independentes de semântica.

- **Homomorphisms**
  - Definição formal de homomorfismos sobre alfabetos e cadeias.
  - Extensão de homomorfismos para linguagens.
  - Preservação e transformação de propriedades linguísticas sob homomorfismos.

- **Codifications**
  - Codificações formais entre representações simbólicas.
  - Condições formais de equivalência e não equivalência entre representações.

#### Professional Knowledge (FPK — CC2020)

- **Analytical and Critical Thinking**
  - Avaliação das consequências estruturais de mapeamentos formais.
  - Identificação de propriedades preservadas e não preservadas.
  - Justificação rigorosa de afirmações sobre equivalência.



### Disposition Specification

As seguintes disposições apoiam a demonstração efetiva desta competência:

- **Epistemic Rigor**
  - Compromisso com definições precisas de mapeamentos e funções.
  - Rejeição de noções intuitivas ou informais de equivalência.

- **Intellectual Responsibility**
  - Justificação cuidadosa de afirmações sobre preservação e transformação.
  - Consciência explícita dos limites formais das codificações.

- **Reflectiveness**
  - Capacidade de distinguir correspondência estrutural de significado semântico.
  - Reconhecimento de que equivalência formal não implica equivalência interpretativa.



### Knowledge–Skill Pairing and Bloom’s Taxonomy Alignment

- **Formal Languages** → **Understand**  
  *(interpretar a estrutura de linguagens e suas propriedades relevantes)*

- **Homomorphisms** → **Apply**  
  *(definir e aplicar homomorfismos a símbolos, cadeias e linguagens)*

- **Codifications** → **Apply**  
  *(mapear e traduzir representações por meio de transformações formais)*

- **Analytical and Critical Thinking (FPK)** → **Analyze**  
  *(analisar propriedades preservadas, justificar limites e avaliar equivalência formal)*



### Verb Annotation (Bloom-Aligned)

- **Understand** → *interpret, explain, identify, describe*  
- **Apply** → *define, apply, map, transform*  
- **Analyze** → *analyze, justify, differentiate, evaluate*



### Summary Table for Competency C19

| **Competency** | **Dispositions** | **Knowledge** | **Skill (Bloom + Verb Annotation)** |
|---------------|-----------------|---------------|-------------------------------------|
| **Apply homomorphisms in formal languages** | Epistemic rigor; Intellectual responsibility; Reflectiveness | Formal Languages | **Understand** *(interpret, explain, identify, describe)* |
|  |  | Homomorphisms | **Apply** *(define, apply, map, transform)* |
|  |  | Codifications | **Apply** *(encode, translate, represent)* |
|  |  | Analytical and Critical Thinking (FPK) | **Analyze** *(analyze, justify, differentiate, evaluate)* |




### Intenção Original

A competência **C19** foi inicialmente definida para tornar explícita a capacidade do aprendiz de **relacionar diferentes representações simbólicas por meio de homomorfismos formais**, no contexto da Teoria das Linguagens Formais.

Em sua formulação original, a competência buscava:

- permitir a **definição e aplicação de homomorfismos** sobre símbolos, cadeias e linguagens;
- apoiar a análise de **codificações formais** entre representações distintas de um mesmo domínio;
- sustentar a discussão sobre **preservação, modificação ou perda de propriedades estruturais**;
- evitar interpretações equivocadas de equivalência baseadas apenas em intuição semântica.

Desde sua concepção, a C19 foi pensada como uma competência **de apoio**, acionada quando a tarefa exige justificar relações entre diferentes representações formais.



### Características Identificadas (Ciclo 1)

- Ênfase em **transformações formais** entre representações simbólicas;
- Uso de verbos como *define*, *apply*, *map* e *transform*;
- Dependência direta de **análise conceitual**, não operacional;
- Risco inicial de:
  - sobreposição com a fase de modelagem (C18);
  - interpretação como implementação de funções computacionais;
- Necessidade de distinção explícita entre:
  - **correspondência estrutural**;
  - **equivalência semântica**.



## 2. Revisão por Especialistas — *CSRP-Report (Ciclo 1)*

### Principais Achados da Revisão

Durante a **Fase 2 (Expert Review)**, a competência C19 foi analisada à luz das evidências exigidas pela **TASK25.00 — Coleção de Músicas** e de tarefas conceitualmente relacionadas.

Os principais pontos registrados foram:

- **Adequação conceitual clara**  
  A competência corresponde às situações em que a tarefa exige discutir **codificações entre representações**, como partitura e gravação.

- **Necessidade de controle de escopo**  
  Foi identificado o risco de a competência ser interpretada como exigência de **implementação computacional de funções**, o que não é requerido pela tarefa.

- **Papel cognitivo secundário**  
  Diferentemente de C17 e C18, a C19 não estrutura a tarefa como um todo, mas **sustenta argumentos específicos**.

- **Evidência observável**  
  A aplicação de homomorfismos e a análise de propriedades preservadas aparecem explicitamente em justificativas conceituais esperadas.



### Recomendações dos Especialistas

Com base na revisão, foi recomendado que a competência C19:

- fosse mantida como **competência de suporte (supporting)**;
- tivesse seu **escopo explicitamente restrito ao nível conceitual**;
- enfatizasse a análise de **preservação e perda de propriedades estruturais**;
- reforçasse a distinção entre **equivalência formal** e **equivalência semântica**;
- evitasse qualquer expectativa de **implementação algorítmica**.



### Limite de Decisão

📌 **Resultado do CSRP (Ciclo 1):**  
**Aprovada com Refinamento de Escopo e Reforço Interpretativo**



## 3. Ajustes Implementados — *CSP_Adjustments*

### Alterações Declaradas

Em resposta às recomendações da revisão, os seguintes ajustes foram aplicados à competência C19:

- **Restrição explícita ao nível conceitual**
  - Inclusão textual clara de que a competência **não envolve implementação computacional**.

- **Reforço do caráter analítico**
  - Ênfase na análise de propriedades preservadas, modificadas ou perdidas.

- **Clarificação do papel funcional**
  - Consolidação da competência como **supporting**, acionada sob condições específicas da tarefa.

- **Separação semântica**
  - Delimitação clara em relação:
    - à modelagem (C18);
    - às operações algébricas (C17).



### Ativação Final (Ajustada)

- **ActivationRole**: `supporting`
- **ActivationMode**: `interpretative`
- **ActivationConstraint**: `mandatory`



## 4. Versão Final — *Ciclo 2*

### Competency Title

    Apply homomorphisms in formal languages



### Descrição Textual Refinada

Esta competência refere-se à capacidade de **definir e aplicar homomorfismos sobre símbolos, cadeias e linguagens**, utilizando **codificações formais** para relacionar diferentes representações simbólicas de um mesmo domínio ou de domínios distintos.

Espera-se que os aprendizes sejam capazes de:

- aplicar homomorfismos de forma consistente a alfabetos, cadeias e linguagens;
- analisar **quais propriedades estruturais são preservadas, modificadas ou perdidas** sob tais transformações;
- **justificar formalmente os limites da equivalência** entre representações, distinguindo claramente **correspondência estrutural** de **equivalência semântica**.

A competência é exercida **exclusivamente em nível conceitual**, não envolvendo implementação computacional de funções de codificação, e assume os homomorfismos como **instrumentos teóricos de análise e justificação**.



### Knowledge Specification (Final)

- **Formal Languages**
  - Alfabetos, cadeias e linguagens.
  - Propriedades estruturais independentes de semântica.

- **Homomorphisms**
  - Definição formal sobre alfabetos, cadeias e linguagens.
  - Extensão de homomorfismos para linguagens.
  - Preservação e transformação de propriedades.

- **Codifications**
  - Codificações formais entre representações simbólicas.
  - Condições formais de equivalência e não equivalência.

- **Analytical and Critical Thinking (FPK)**



### Disposition Specification (Final)

- Epistemic Rigor  
- Intellectual Responsibility  
- Reflectiveness  



## 5. Knowledge–Skill Pairing (Final)

- **Formal Languages — Understand**
  → interpretar a estrutura de linguagens e suas propriedades.

- **Homomorphisms — Apply**
  → definir e aplicar homomorfismos a símbolos, cadeias e linguagens.

- **Codifications — Apply**
  → mapear e traduzir representações por meio de transformações formais.

- **Analytical and Critical Thinking (FPK) — Analyze**
  → analisar propriedades preservadas e justificar limites de equivalência.



### Bloom’s Taxonomy Alignment (Final)

- **Formal Languages — Understand**
- **Homomorphisms — Apply**
- **Codifications — Apply**
- **Analytical and Critical Thinking — Analyze**



### Summary Table — Competency C19 (Final)

| **ID** | **Competency** | **Dispositions** | **Knowledge** | **Skill (Bloom)** |
|------|----------------|------------------|---------------|-------------------|
| C19 | **Apply homomorphisms in formal languages** | Epistemic rigor; Intellectual responsibility; Reflectiveness | Formal Languages | **Understand (Interpret, Explain)** |
|     |                |                  | Homomorphisms | **Apply (Define, Map, Transform)** |
|     |                |                  | Codifications | **Apply (Encode, Translate)** |
|     |                |                  | Analytical & Critical Thinking (FPK) | **Analyze (Justify, Differentiate)** |











