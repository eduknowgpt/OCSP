# Competency Lifecycle — C17 - *Apply operations on formal languages*


## 1. Definição Original — *CSP-Report (Ciclo 1)*

### Competency Title

    Apply operations on formal languages


### Textual Description  

Esta competência envolve a capacidade do aprendiz de **aplicar, analisar e justificar operações formais sobre linguagens**, tais como **concatenação, união, interseção, complemento, fecho de Kleene e reversão**, com foco explícito nos **efeitos estruturais** dessas operações e em suas **propriedades teóricas**.

Os aprendizes devem demonstrar a capacidade de:
- avaliar a **pertinência estrutural** dos resultados obtidos;
- determinar se as linguagens resultantes **preservam propriedades relevantes** (por exemplo, pertencimento a uma classe, finitude ou infinitude);
- **justificar formalmente** suas conclusões por meio de definições precisas, exemplos mínimos, contraexemplos e propriedades conhecidas (como propriedades de fechamento).

Esta competência é exercida **exclusivamente em nível conceitual e algébrico**, **não envolvendo construção, simulação ou implementação de autômatos**.

- **Alinhamento CS2023**:  
  TC.FLR — Formal Languages and Recognizers

- **Learning Objectives atendidos**:  
  LO2.1, LO2.2,  
  LO3.1, LO3.2, LO3.3, LO3.4,  
  LO4.1, LO4.2, LO4.3,  
  LO5.1, LO5.2,  
  LO9.4



### Activation

- **ActivationRole**: `core`  
  A competência é **nuclear** para a tarefa, pois sustenta a análise estrutural das coleções musicais modeladas como linguagens.

- **ActivationMode**: `analytical`  
  O desempenho esperado envolve **análise formal**, comparação de resultados e justificação conceitual das operações aplicadas.

- **ActivationConstraint**: `mandatory`  
  A Task25.00 não pode ser resolvida adequadamente sem o domínio desta competência.



### Knowledge Specification

Os seguintes componentes de conhecimento são essenciais para a demonstração desta competência:

#### Computing Knowledge (CS2023)

- **Language Theory**
  - Alfabetos, cadeias e linguagens.
  - Linguagens finitas e infinitas.
  - Fundamentos conceituais dos modelos formais de linguagem.

- **Operations on Formal Languages**
  - União, interseção, diferença e complemento (com universo explicitamente definido).
  - Concatenação de cadeias e linguagens.
  - Fecho de Kleene.
  - Reversão de cadeias e linguagens.
  - Propriedades de fechamento de classes de linguagens, em nível conceitual.

- **Regular Expressions**
  - Expressões regulares como notação algébrica para descrever linguagens.
  - Relação conceitual entre expressões regulares e operações sobre linguagens.

#### Professional Knowledge (FPK — CC2020)

- **Analytical and Critical Thinking**
  - Decomposição de problemas formais.
  - Avaliação das consequências estruturais de construções formais.
  - Justificação de afirmações com base em raciocínio matemático preciso.



### Disposition Specification

As seguintes disposições apoiam a demonstração efetiva desta competência:

- **Epistemic Rigor**
  - Compromisso com justificativas formais em detrimento de intuições informais.
  - Distinção clara entre definições, exemplos e propriedades gerais.

- **Intellectual Responsibility**
  - Precisão na aplicação de definições e operações.
  - Coerência e consistência nos argumentos formais.

- **Persistence**
  - Disposição para revisar definições e raciocínios diante de inconsistências ou ambiguidades.



### Knowledge–Skill Pairing and Bloom’s Taxonomy Alignment

- **Language Theory** → **Understand**  
  *(interpretar e explicar definições formais e propriedades fundamentais das linguagens)*

- **Operations on Formal Languages** → **Apply / Analyze**  
  *(aplicar operações formais e analisar seus efeitos estruturais e consequências teóricas)*

- **Regular Expressions** → **Apply**  
  *(utilizar notação algébrica para descrever e relacionar linguagens)*

- **Analytical and Critical Thinking (FPK)** → **Analyze**  
  *(examinar argumentos formais, identificar inconsistências e avaliar a validade de conclusões)*



### Verb Annotation (Bloom-Aligned)

- **Understand** → *interpret, explain, identify, describe*  
- **Apply** → *apply, compute, derive, determine*  
- **Analyze** → *analyze, justify, differentiate, evaluate*



### Summary Table for Competency C17

| **Competency** | **Dispositions** | **Knowledge** | **Skill (Bloom + Verb Annotation)** |
|---------------|-----------------|---------------|-------------------------------------|
| **Apply operations on formal languages** | Epistemic rigor; Intellectual responsibility; Persistence | Language Theory | **Understand** *(interpret, explain, identify, describe)* |
|  |  | Operations on Formal Languages | **Apply / Analyze** *(apply, compute, derive, analyze)* |
|  |  | Regular Expressions | **Apply** *(use, specify, relate)* |
|  |  | Analytical and Critical Thinking (FPK) | **Analyze** *(analyze, justify, differentiate, evaluate)* |




### Intenção Original

A definição original da competência **C17** foi introduzida para explicitar a capacidade do estudante de **empregar operações formais sobre linguagens** como instrumento central de análise em tarefas de Teoria das Linguagens Formais.

Nesta formulação inicial, a competência buscava:

- permitir que os estudantes **aplicassem operações algébricas** sobre linguagens formais;
- sustentar a análise de **propriedades estruturais**, como pertencimento, finitude e fechamento;
- servir como eixo conceitual para tarefas que envolvem **manipulação simbólica rigorosa**, sem recorrer a implementações algorítmicas.

A competência foi concebida como **nuclear** em tarefas de modelagem e análise formal de linguagens, especialmente em contextos introdutórios de Teoria da Computação.



### Características Identificadas (Ciclo 1)

- Forte alinhamento com **Teoria das Linguagens Formais**;
- Uso do verbo **Apply**, sugerindo ação direta sobre objetos formais;
- Ênfase em **operações clássicas** (concatenação, fecho de Kleene, complemento, reversão);
- Possível ambiguidade inicial quanto ao **nível de aplicação** (conceitual vs. operacional);
- Dependência implícita de **justificação matemática rigorosa** como evidência.



## 2. Revisão por Especialistas — *CSRP-Report (Ciclo 1)*

### Principais Achados da Revisão

Durante a Fase 2 (Expert Review), os especialistas analisaram a competência C17 à luz das evidências efetivamente produzidas na **TASK25.00** e em tarefas conceitualmente similares.

Os principais pontos observados foram:

- **Adequação conceitual elevada**  
  A competência corresponde diretamente às ações exigidas pela tarefa, sendo indispensável para sua resolução adequada.

- **Risco de interpretação operacional**  
  O uso do verbo *Apply* poderia ser interpretado, fora de contexto, como exigência de construção ou simulação de modelos reconhecedores.

- **Centralidade cognitiva**  
  Diferentemente de competências como C16, a C17 não atua como suporte conceitual, mas como **núcleo da atividade analítica**.

- **Evidência claramente observável**  
  As operações aplicadas e suas justificativas aparecem explicitamente nas respostas esperadas, permitindo avaliação independente.



### Recomendações dos Especialistas

Os especialistas recomendaram que a competência C17:

- **fosse mantida como competência central (core)**;
- tivesse seu **escopo explicitamente delimitado ao nível conceitual e algébrico**;
- evitasse qualquer interpretação que implicasse **implementação, simulação ou construção de autômatos**;
- incorporasse explicitamente a **análise de consequências estruturais** das operações, e não apenas sua aplicação mecânica.



### Limite de Decisão

**Resultado do CSRP (Ciclo 1):**  
**Aprovada com Refinamento de Escopo e Clarificação Semântica**



## 3. Ajustes Implementados — *CSP-Adjustments*

### Alterações Declaradas

Com base nas recomendações do CSRP, os seguintes ajustes foram aplicados à competência C17:

- **Clarificação do nível de atuação**
  - Inclusão explícita de que a competência é exercida **exclusivamente em nível conceitual e algébrico**.

- **Expansão controlada do escopo**
  - Ênfase não apenas na aplicação das operações, mas também na **análise de seus efeitos estruturais** e propriedades teóricas.

- **Refinamento da evidência esperada**
  - Justificativas baseadas em **definições formais, exemplos mínimos, contraexemplos e propriedades de fechamento**.

- **Consolidação do papel funcional**
  - Confirmação de C17 como competência **core**, indispensável para a TASK25.00.



### Ativação Final (Ajustada)

- **ActivationRole**: `core`
- **ActivationMode**: `analytical`
- **ActivationConstraint**: `mandatory`



## 4. Versão Final — *Ciclo 2*

### Competency Title

    Apply operations on formal languages



### Descrição Textual Refinada

Esta competência refere-se à capacidade de **aplicar, analisar e justificar operações formais sobre linguagens**, tais como **concatenação, união, interseção, complemento, fecho de Kleene e reversão**, com foco explícito nos **efeitos estruturais dessas operações** e em suas **propriedades teóricas**.

Espera-se que os aprendizes sejam capazes de:

- aplicar operações formais a linguagens definidas sobre um alfabeto explícito;
- analisar se as linguagens resultantes **preservam propriedades relevantes**, como pertencimento a uma classe, finitude ou infinitude;
- **justificar formalmente** suas conclusões por meio de definições precisas, exemplos mínimos, contraexemplos e propriedades conhecidas (como propriedades de fechamento).

A competência é exercida **exclusivamente em nível conceitual e algébrico**, não envolvendo construção, simulação ou implementação de autômatos ou algoritmos.



### Knowledge Specification (Final)

- **Language Theory**
  - Alfabetos, cadeias e linguagens.
  - Linguagens finitas e infinitas.

- **Operations on Formal Languages**
  - Concatenação de cadeias e linguagens.
  - União, interseção, diferença e complemento (com universo explicitado).
  - Fecho de Kleene.
  - Reversão de cadeias e linguagens.
  - Propriedades de fechamento, em nível conceitual.

- **Regular Expressions (conceitual)**
  - Uso como notação algébrica para descrever linguagens.

- **Analytical and Critical Thinking (FPK)**



### Disposition Specification (Final)

- Epistemic Rigor  
- Intellectual Responsibility  
- Persistence  



## Knowledge–Skill Pairing (Final)

- **Language Theory — Understand**
  → interpretar e explicar definições formais e propriedades fundamentais.

- **Operations on Formal Languages — Apply / Analyze**
  → aplicar operações formais e analisar seus efeitos estruturais.

- **Regular Expressions — Apply**
  → utilizar notação algébrica para descrever e relacionar linguagens.

- **Analytical and Critical Thinking (FPK) — Analyze**
  → examinar argumentos formais, identificar inconsistências e justificar conclusões.



### Bloom’s Taxonomy Alignment (Final)

- **Language Theory — Understand**
- **Operations on Formal Languages — Apply / Analyze**
- **Regular Expressions — Apply**
- **Analytical and Critical Thinking — Analyze**



### Summary Table — Competency C17 (Final)

| **ID** | **Competency**                         | **Dispositions**                                   | **Knowledge**                          | **Skill (Bloom)**                           |
|------|----------------------------------------|--------------------------------------------------|----------------------------------------|---------------------------------------------|
| C17  | **Apply operations on formal languages** | Epistemic rigor, Intellectual responsibility, Persistence | Language Theory                        | **Understand (Explain, Interpret)**          |
|      |                                        |                                                  | Operations on Formal Languages          | **Apply / Analyze (Apply, Justify)**         |
|      |                                        |                                                  | Regular Expressions (conceptual)        | **Apply (Specify, Relate)**                  |
|      |                                        |                                                  | Analytical and Critical Thinking (FPK)  | **Analyze (Analyze, Evaluate, Justify)**     |



## 5. Estado do Ciclo de Vida

- **Status:** Aprovada (Ciclo 2)  
- **Papel:** Competência **core**  
- **Escopo:** Conceitual e algébrico  
- **Relação com outras competências:**  
  - Integra-se a **C18** (modelagem) e **C19** (transformações);
  - Sustenta a competência composta **C20**;
  - Complementa competências transversais **C13′** e **C05′**.