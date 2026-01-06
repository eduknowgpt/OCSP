# Competency Specification Report: Task25.00 - Coleção de Músicas


## Introdução

Este relatório aplica a metodologia do **Competency Specification Process (CSP)** à *Task25.00 – Coleção de Músicas*, uma atividade da disciplina *MATC94 – Introdução às Linguagens Formais e Teoria da Computação*, cujo objetivo central é avaliar a capacidade do estudante de abstrair um domínio do mundo real e modelá-lo rigorosamente como um sistema formal.

Na tarefa, o domínio musical é utilizado como domínio de referência, no qual:

- notas musicais são abstraídas como símbolos de um alfabeto;

- músicas são modeladas como cadeias finitas;

- coleções de músicas são tratadas como linguagens formais.

Essa modelagem permite a aplicação sistemática de operações clássicas sobre linguagens, tais como concatenação, fecho de Kleene, reversão, união, interseção e complemento, bem como a análise de propriedades estruturais, incluindo pertencimento, finitude, infinitude e fechamento.

O enunciado da Task25.00 exige explicitamente que todas as respostas sejam formalmente justificadas, o que desloca o foco da atividade de interpretações intuitivas para o uso criterioso de:

- definições matemáticas precisas;

- exemplos mínimos e construções formais;

- propriedades teóricas e argumentos lógicos;

- contraexemplos, quando aplicável.



## 1. Instructional Entity Analysis

### Title

* **Coleção de Músicas**


### Description

Nesta tarefa, os aprendizes devem **abstrair e modelar partituras musicais como objetos formais**, estabelecendo uma correspondência explícita entre o domínio musical e os conceitos fundamentais da Teoria das Linguagens Formais. Nesse modelo:

* **notas musicais** são tratadas como **símbolos de um alfabeto**;
* **músicas** são representadas como **cadeias (strings) finitas**;
* **coleções de músicas** são formalizadas como **linguagens** (subconjuntos de Σ*).

A partir dessa modelagem, os estudantes devem **analisar propriedades estruturais** e **aplicar operações clássicas sobre linguagens formais**, tais como concatenação, fecho de Kleene, reversão, união, interseção e complemento.

A tarefa enfatiza fortemente a produção de **respostas matematicamente justificadas**, exigindo o uso explícito de definições formais, propriedades teóricas e argumentos lógicos. Interpretações intuitivas, analogias informais ou justificativas não formalizadas **não são consideradas suficientes**, reforçando o compromisso com o rigor epistêmico característico da Teoria da Computação.


### Solution Development Process

**Abordagem esperada do aprendiz:**

* **Analisar cuidadosamente as restrições e premissas do problema**, reconhecendo que:

  * partituras podem envolver **um ou múltiplos instrumentos**, o que implica símbolos simples (uma nota) ou **símbolos compostos** (conjuntos finitos de notas simultâneas);
  * cada música é modelada como uma **cadeia finita de comprimento arbitrário** (não limitada a um tamanho fixo);
  * coleções musicais podem ser definidas:

    * de forma **extensional**, como conjuntos finitos explicitamente listados; ou
    * de forma **intensional**, por meio de **propriedades formais** (por exemplo, padrões estruturais, restrições de forma ou critérios textuais como a ocorrência de uma palavra).

* **Estabelecer explicitamente a fronteira entre estrutura e significado**, assumindo que:

  * a correção das respostas depende da **estrutura formal** (símbolos, cadeias, linguagens e operações);
  * interpretações musicais ou semânticas (por exemplo, “soar bem”, “ser reconhecida como música”) **não substituem** justificativas matemáticas.

* **Definir formalmente o modelo de representação**, explicitando:

  * o **alfabeto (Σ)** de símbolos musicais adotado (incluindo, quando necessário, a noção de símbolo composto);
  * a noção de **música como cadeia** sobre Σ;
  * a caracterização de **coleções de músicas como linguagens** (L ⊆ Σ*);
  * o **universo de referência** quando necessário (por exemplo, para discutir complemento, definir claramente o conjunto em relação ao qual o complemento é tomado).

* **Aplicar operações formais sobre cadeias e linguagens**, incluindo:

  * concatenação de cadeias para representar composição de músicas;
  * identificação de prefixos, sufixos e subcadeias (trechos iniciais, finais e internos);
  * reversão de cadeias (música “ao contrário” no sentido formal);
  * união, interseção, diferença e complemento de linguagens (coleções);
  * fecho de Kleene e o papel da **cadeia vazia (ε)** e da **linguagem vazia (∅)**, distinguindo claramente esses dois conceitos.

* **Justificar cada conclusão com argumentação formal**, sustentando as respostas por meio de:

  * definições formais precisas (por exemplo, o que conta como cadeia, linguagem, trecho/prefixo, reverso, etc.);
  * exemplos mínimos cuidadosamente escolhidos para ilustrar propriedades;
  * demonstrações conceituais e raciocínios estruturados (incluindo raciocínio indutivo, quando apropriado);
  * **contraexemplos** para refutar generalizações indevidas ou afirmações falsas.

* **Recorrer a modelos reconhecedores apenas quando pertinente e no nível conceitual**, isto é:

  * usar autômatos, expressões regulares ou equivalências teóricas como **instrumentos de justificativa** (quando ajudarem a sustentar uma afirmação);
  * **sem exigir** construção operacional detalhada, implementação ou simulação, a menos que isso seja explicitamente necessário para fundamentar a resposta.

* **Explorar equivalências e codificações formais**, discutindo:

  * homomorfismos ou mapeamentos entre representações simbólicas (por exemplo, partitura ↔ gravação);
  * quais propriedades estruturais são preservadas ou perdidas na codificação;
  * os **limites formais da intercambialidade**, distinguindo “correspondência estrutural” de “equivalência semântica”.

* **Documentar rigorosamente** todas as escolhas de modelagem, raciocínios e conclusões, empregando:

  * notação matemática adequada e consistente;
  * terminologia precisa da Teoria das Linguagens Formais;
  * uma estrutura textual clara que diferencie explicitamente **definições**, **exemplos**, **argumentos/provas** e **conclusões**.












### Expected Outcomes

Ao final desta atividade, os estudantes deverão ser capazes de:

> Definir formalmente e empregar corretamente os conceitos de **alfabeto, cadeia, linguagem, linguagem vazia e fecho de linguagens**, utilizando notação matemática adequada e consistente.

> Aplicar e interpretar **operações algébricas sobre cadeias e linguagens**, incluindo concatenação, união, interseção, complemento, reversão e fecho de Kleene, analisando seus efeitos estruturais em contextos concretos.

> Analisar e **justificar propriedades estruturais de linguagens**, tais como pertencimento, finitude ou infinitude, recorrendo a definições formais, argumentos lógicos e contraexemplos quando apropriado.

> Identificar **padrões estruturais em sequências simbólicas** (prefixos, subcadeias, repetições) e argumentar sobre propriedades de linguagens induzidas por restrições formais derivadas de domínios do mundo real.

> Abstrair artefatos musicais do mundo real (partituras, gravações, gêneros) como **representações formais**, modelando-os como símbolos, cadeias e linguagens, e justificando explicitamente as escolhas de modelagem.

> Analisar, em nível conceitual, o uso de **autômatos finitos e expressões regulares** como instrumentos teóricos para justificar propriedades de linguagens, sem exigir construção ou simulação operacional detalhada.

> Avaliar **codificações simbólicas e homomorfismos** entre diferentes representações, distinguindo claramente **correspondência estrutural** de **interpretação semântica**, e identificando limites formais de equivalência.

> Produzir respostas e relatórios tecnicamente rigorosos, apresentando **definições formais, exemplos mínimos, argumentos estruturados e conclusões coerentes**, com clareza, precisão terminológica e consistência lógica.



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

Para assegurar uma modelagem sistemática, precisa e semanticamente consistente dos conhecimentos mobilizados na **Task25.00 – Coleção de Músicas**, esta enumeração adota o **ACM CS2023** como vocabulário controlado para o conhecimento computacional disciplinar e o **ACM Computing Curricula 2020 (CC2020)** como referência para o **Conhecimento Profissional Fundamental (FPK)**.

Esses elementos constituem a **dimensão Conhecimento (K)** do modelo **OntoKSD**, refletindo exclusivamente os conhecimentos **conceituais e teóricos** efetivamente requeridos pela tarefa, sem pressupor construção, simulação ou implementação de artefatos computacionais.

A identificação dos componentes a seguir baseia-se nas exigências de **modelagem formal**, **análise estrutural de linguagens** e **argumentação matemática rigorosa** explicitadas no enunciado da atividade.



### Conhecimento em Computação  
*(Alinhado ao CS2023 — TC.FLR: Formal Languages and Recognizers)*

- **Linguagens Formais**
  - Conceitos de **alfabeto, cadeia, linguagem, cadeia vazia (ε) e linguagem vazia (∅)**.
  - Distinção entre **linguagens finitas e infinitas**.
  - Noções estruturais de **prefixos, sufixos e subcadeias**.

- **Operações sobre Linguagens**
  - Operações algébricas: **união, interseção, diferença e complemento** (com universo explicitamente definido).
  - **Concatenação de cadeias e linguagens**.
  - **Fecho de Kleene** e suas implicações estruturais.
  - **Reversão** de cadeias e linguagens.
  - Propriedades de **fechamento de classes de linguagens**, em nível conceitual.

- **Linguagens Regulares**
  - **Expressões regulares** como notação algébrica para especificação de linguagens.
  - Noção de **regularidade** como classe expressiva, sem exigir construção operacional.

- **Autômatos Finitos (nível conceitual)**
  - Autômatos finitos como **modelos reconhecedores abstratos**.
  - Relação teórica entre **autômatos finitos, expressões regulares e linguagens regulares**.
  - Limites expressivos dos autômatos finitos, usados como suporte argumentativo.

- **Homomorfismos e Codificações**
  - Definição formal de **homomorfismos de cadeias e linguagens**.
  - Mapeamentos entre representações simbólicas distintas.
  - Análise de **propriedades preservadas e não preservadas** sob codificação.
  - Limites formais da equivalência representacional (por exemplo, partitura ↔ gravação).

- **Raciocínio Formal e Conhecimento sobre Prova**
  - Papel das **definições formais** como base de validade.
  - Uso de **exemplos mínimos** como instrumentos explicativos.
  - Construção e interpretação de **contraexemplos**.
  - Justificação lógica de propriedades estruturais de linguagens.



### Conhecimento Profissional Fundamental  
*(FPK — CC2020)*

- **Pensamento Analítico e Crítico**
  - Abstração de domínios do mundo real em **modelos formais precisos**.
  - Avaliação rigorosa da validade de afirmações à luz de definições e propriedades teóricas.

- **Comunicação Escrita Técnica**
  - Produção de textos matematicamente rigorosos, claros e bem estruturados.
  - Uso consistente de **notação formal**, terminologia técnica e encadeamento lógico.

- **Rigor Epistêmico**
  - Compromisso explícito com **justificativas formais** em detrimento de intuições informais.
  - Capacidade de distinguir claramente entre **definições**, **exemplos**, **argumentos** e **conclusões**.






## 3. Learning Objectives Identification

Com base no enunciado da tarefa **Coleção de Músicas**, os objetivos de aprendizagem foram definidos para refletir com precisão as **exigências conceituais**, o **nível de rigor matemático** e o **tipo de competência teórica e analítica esperada** na disciplina **MATC94 – Introdução às Linguagens Formais e Teoria da Computação**.



### 3.1 General Learning Objective

O objetivo geral desta tarefa é capacitar o estudante a **abstrair e modelar um domínio do mundo real** (músicas e coleções musicais) como **linguagens formais**, empregando conceitos fundamentais de linguagens, expressões regulares e modelos reconhecedores **em nível conceitual**, bem como a **analisar e justificar propriedades estruturais** por meio de definições formais, operações sobre linguagens e argumentação matemática rigorosa, **sem recorrer a intuições informais ou implementações algorítmicas ad hoc**.



### 3.2 Specific Learning Objectives 

#### LO1 — Formal Abstraction of the Domain
1.1 Definir formalmente um **alfabeto (Σ)** a partir do conjunto de símbolos musicais relevantes.  
1.2 Modelar uma **música como uma cadeia (string) sobre Σ**.  
1.3 Modelar uma **coleção de músicas como uma linguagem (L ⊆ Σ\*)**.  

#### LO2 — Structural Analysis of Strings
2.1 Identificar e definir formalmente **prefixos, sufixos e subcadeias** de uma música.  
2.2 Determinar se um trecho de música pode ser formalmente considerado uma música válida.  
2.3 Justificar a validade (ou não) de trechos posicionados no início, meio ou fim de uma música, com base exclusivamente em critérios estruturais.

#### LO3 — Operations over Languages
3.1 Aplicar a **concatenação** de cadeias para modelar a composição de músicas.  
3.2 Analisar se o resultado da concatenação pertence à mesma linguagem original.  
3.3 Aplicar **união, interseção e diferença** para combinar coleções musicais.  
3.4 Avaliar o **complemento** de uma linguagem em relação a um universo explicitamente definido.  

#### LO4 — Kleene Closure and Language Cardinality
4.1 Aplicar o **fecho de Kleene (L\*)** a uma linguagem musical.  
4.2 Interpretar o papel da **cadeia vazia (ε)** e da **linguagem vazia (∅)** em coleções musicais.  
4.3 Classificar linguagens como **finitas ou infinitas**, justificando formalmente.

#### LO5 — Reversal and String Transformations
5.1 Definir formalmente a **reversão de cadeias**.  
5.2 Aplicar a operação de reversão a uma música e analisar sua validade estrutural.  
5.3 Distinguir explicitamente **validade estrutural** de **interpretação semântica** no contexto da reversão.

#### LO6 — Regular Languages and Formal Expressiveness
6.1 Reconhecer quando uma coleção de músicas pode ser descrita por uma **linguagem regular**.  
6.2 Especificar linguagens musicais por meio de **expressões regulares**.  
6.3 Diferenciar, em nível **conceitual**, linguagens regulares e linguagens livres de contexto, indicando limites expressivos, **sem exigir construção formal de gramáticas**.

#### LO7 — Automata and Model Equivalence (Conceptual Level)
7.1 Explicar a equivalência teórica entre **autômatos finitos, expressões regulares e gramáticas regulares**.  
7.2 Relacionar padrões estruturais de músicas a **estados e transições conceituais** de um autômato, **como instrumento teórico de justificação**.

#### LO8 — Homomorphisms and Codifications
8.1 Definir formalmente **homomorfismos de cadeias**.  
8.2 Analisar se duas representações (partitura e gravação) podem ser vistas como **codificações estruturalmente equivalentes**.  
8.3 Justificar limites formais da intercambialidade entre representações simbólicas.

#### LO9 — Formal Reasoning and Proof
9.1 Utilizar **definições formais** como base de validade de respostas conceituais.  
9.2 Construir **exemplos mínimos** para ilustrar propriedades de linguagens.  
9.3 Empregar **contraexemplos** para refutar afirmações incorretas.  
9.4 Aplicar **raciocínio indutivo** quando apropriado (por exemplo, em propriedades de fechamento).

#### LO10 — Technical and Epistemic Communication
10.1 Elaborar um **relatório técnico** com estrutura lógica, clareza argumentativa e terminologia adequada.  
10.2 Apresentar justificativas matematicamente rigorosas, coerentes e bem fundamentadas.  
10.3 Distinguir explicitamente entre **intuição informal**, **exemplo ilustrativo** e **prova ou argumento formal**.



### 3.3 Importance of These Objectives

Esses objetivos estabelecem um percurso estruturado de desenvolvimento de competências conceituais, analíticas e epistemológicas, assegurando que o estudante:

- construa uma base teórica sólida em Linguagens Formais e Teoria da Computação, fundamentada em definições precisas e modelos formais;
- desenvolva a capacidade de abstrair e formalizar domínios do mundo real em representações matemáticas rigorosas;
- compreenda e analise propriedades estruturais, relações de equivalência e limites expressivos das linguagens formais;
- exercite pensamento analítico, argumentação lógica e rigor epistêmico, essenciais para a validação de afirmações em contextos teóricos;
- consolide habilidades de comunicação técnica, expressando raciocínios, modelos e justificativas com clareza formal, precisão terminológica e consistência lógica.

Ao atingir esses objetivos, o estudante estará apto a articular teoria e prática de maneira crítica e consciente, utilizando conceitos de Linguagens Formais, Expressões Regulares e Autômatos Finitos **como instrumentos teóricos** para analisar, justificar e resolver problemas conceituais complexos, com rigor matemático e solidez argumentativa.





## 4. Competency Definition  
### Competências Reutilizadas e Especializadas do Conjunto de Referência

As competências a seguir foram reutilizadas por apresentarem **aderência direta às exigências conceituais, epistêmicas e avaliativas da Task25.00 – Coleção de Músicas**.  
Para cada competência reutilizada, são explicitados o **papel de ativação (ActivationRole)**, o **modo de ativação (ActivationMode)** e a **condição de ativação (ActivationConstraint)**, conforme o modelo de ativação adotado no **CSP/OntoKSD**.  
Essa explicitação visa assegurar transparência metodológica, alinhamento com os objetivos de aprendizagem e coerência entre competência, evidência e avaliação.



### **C04 — Define Regular Expressions for Finite Automata**

- **Relevância**  
  Permite a **especificação formal de conjuntos de músicas** por meio de expressões regulares, contemplando casos como:
  - músicas que satisfazem uma propriedade textual (por exemplo, contêm uma palavra específica);
  - a música vazia;
  - a repetição indefinida de músicas (fecho de Kleene).

- **Learning Objectives atendidos**  
  LO6.1, LO6.2, LO7.1

- **ActivationRole**: `core`  
  A competência é **nuclear**, pois viabiliza a definição formal de linguagens musicais exigida pela tarefa.

- **ActivationMode**: `artifact-oriented`  
  O desempenho esperado consiste na **produção de artefatos formais**, especificamente expressões regulares que caracterizam linguagens.

- **ActivationConstraint**: `mandatory`  
  A tarefa não pode ser resolvida de forma adequada sem o domínio dessa competência.



### **C14 — Differentiate classifications of formal grammars**

- **Relevância**  
  Possibilita a **diferenciação conceitual** entre linguagens regulares e linguagens de maior poder expressivo, permitindo:
  - delimitar o escopo das construções formais utilizadas;
  - justificar limites expressivos, sem exigir construção de gramáticas.

- **Learning Objectives atendidos**  
  LO6.1, LO6.3

- **ActivationRole**: `extension`  
  A competência atua como **ampliação conceitual**, enriquecendo a análise sem ser central para todas as respostas.

- **ActivationMode**: `analytical`  
  O foco está na **análise comparativa e conceitual** de classes de linguagens.

- **ActivationConstraint**: `optional`  
  É mobilizada quando o estudante discute limites expressivos ou generalizações conceituais.



### **C13′ — Interpret and apply algebraic notation for strings and languages**

- **Especialização de**: C13 — *Interpret rule-based notation*

- **Descrição**  
  Interpretar, aplicar e justificar o uso de **notações algébricas formais** de:
  - **cadeias** (ε, Σ, |x|, concatenação, potência, reversão, subcadeias);
  - **linguagens** (∪, ∩, complemento, concatenação, Lⁿ, L\*, prefixos/sufixos, homomorfismos).

- **Verbos observáveis**  
  explain, apply, compute, derive, justify

- **Disposições**  
  meticulous, responsible

- **Learning Objectives atendidos**  
  LO1.1, LO1.2, LO1.3,  
  LO2.1, LO2.2,  
  LO3.1, LO3.3,  
  LO4.2,  
  LO5.1,  
  LO6.2,  
  LO8.1

- **ActivationRole**: `core`  
  Trata-se da **competência estrutural central** da tarefa, sustentando praticamente todas as respostas.

- **ActivationMode**: `analytical`  
  O desempenho envolve **manipulação simbólica, análise algébrica e justificação formal**.

- **ActivationConstraint**: `mandatory`  
  Sem essa competência, não é possível atender às exigências formais da tarefa.



### **C05′ — Write mathematically rigorous answers**

- **Especialização de**: C05 — *Write a technical report*

- **Descrição**  
  Produzir respostas matematicamente rigorosas, empregando:
  - definições formais explícitas;
  - exemplos mínimos;
  - demonstrações conceituais;
  - uso consciente de propriedades teóricas (por exemplo, propriedades de fechamento);
  - contraexemplos, quando apropriado.

- **Verbos observáveis**  
  define, justify, prove, exemplify, refute

- **Disposições**  
  meticulous, responsible

- **Learning Objectives atendidos**  
  LO2.3,  
  LO5.2, LO5.3,  
  LO8.3,  
  LO9.1, LO9.2, LO9.3, LO9.4,  
  LO10.2, LO10.3

- **ActivationRole**: `transversal`  
  A competência é **transversal**, permeando todas as respostas e conteúdos da tarefa.

- **ActivationMode**: `justificatory`  
  O foco está na **sustentação formal das conclusões**, e não apenas na apresentação de resultados.

- **ActivationConstraint**: `mandatory`  
  Todas as respostas exigem rigor matemático explícito, tornando essa competência indispensável.




## Novas Competências da TASK25.00

### Competency C17 Specification

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









## Competency C18 Specification

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


## Competency C19 Specification

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



## Competency C20 Specification

### Competency Title
    Model and analyze musical collections as formal languages



### Textual Description

Esta competência de nível de tarefa envolve a capacidade do aprendiz de **integrar conceitos, operações e representações da Teoria das Linguagens Formais** para **modelar coleções musicais como linguagens formais** e **analisar rigorosamente suas propriedades estruturais**.

Os aprendizes devem demonstrar a capacidade de:
- abstrair artefatos musicais em **símbolos, cadeias e linguagens**;
- aplicar **operações algébricas** e **expressões regulares** para caracterizar coleções musicais;
- analisar **transformações formais e codificações** entre diferentes representações;
- justificar **propriedades, limites e consequências estruturais** por meio de definições precisas, exemplos mínimos, contraexemplos e argumentação lógica.

Esta competência **sintetiza competências atômicas previamente definidas** em uma **análise formal coerente de um problema do mundo real**, sem exigir implementação algorítmica ou construção operacional de modelos reconhecedores.



### Competency Composition

Competência **composta**, formada pela integração das seguintes competências:

- **C18** — Model real-world problems using formal language concepts  
- **C17** — Apply operations on formal languages  
- **C19** — Apply homomorphisms in formal languages  
- **C04** — Define Regular Expressions for Finite Automata  
- **C13′** — Interpret and apply algebraic notation for strings and languages  
- **C05′** — Write mathematically rigorous answers  



### Curricular Alignment

- **CS2023 Knowledge Area:**  
  TC.FLR — Formal Languages and Recognizers

- **Task Association:**  
  Task25.00 — *Coleção de Músicas*



### Activation

- **ActivationRole**: `core`  
  Trata-se da **competência central da tarefa**, responsável por integrar e dar sentido global às competências atômicas mobilizadas.

- **ActivationMode**: `integrative`  
  O desempenho esperado envolve **síntese, articulação e integração** de múltiplos conhecimentos e habilidades formais.

- **ActivationConstraint**: `mandatory`  
  Esta competência representa o **resultado esperado da tarefa** e é necessariamente ativada.



### Knowledge Specification

#### Computing Knowledge (CS2023)

- **Language Theory**
  - Fundamentos da modelagem formal por meio de linguagens.

- **Formal Languages**
  - Alfabetos, cadeias e linguagens.
  - Operações sobre linguagens e propriedades de fechamento.

- **Regular Expressions**
  - Especificação algébrica de linguagens regulares.

- **Homomorphisms and Codifications**
  - Mapeamentos formais entre representações simbólicas.
  - Limites estruturais da equivalência formal.

#### Professional Knowledge (FPK — CC2020)

- **Analytical and Critical Thinking**
  - Integração e avaliação de modelos formais.
  - Justificação de propriedades e decisões de modelagem.

- **Technical Written Communication**
  - Documentação rigorosa de definições, raciocínios e conclusões.



### Disposition Specification

- **Epistemic Rigor**
  - Compromisso com definições formais e argumentação lógica.

- **Intellectual Responsibility**
  - Coerência e precisão na integração de modelos e argumentos.

- **Reflectiveness**
  - Consciência explícita das suposições e limitações do modelo adotado.

- **Persistence**
  - Disposição para revisar modelos e argumentos diante de inconsistências.



### Knowledge–Skill Pairing and Bloom’s Taxonomy Alignment

- **Language Theory** → **Understand**  
  *(interpretar conceitos fundamentais de modelagem formal)*

- **Formal Languages** → **Apply**  
  *(modelar coleções musicais e aplicar operações)*

- **Regular Expressions** → **Apply**  
  *(especificar linguagens de forma algébrica)*

- **Homomorphisms and Codifications** → **Apply**  
  *(relacionar representações simbólicas distintas)*

- **Analytical and Critical Thinking (FPK)** → **Analyze**  
  *(integrar, avaliar e justificar modelos formais)*

- **Technical Written Communication (FPK)** → **Create**  
  *(produzir documentação técnica rigorosa e coerente)*



### Verb Annotation (Bloom-Aligned)

- **Understand** → *interpret, explain, identify*  
- **Apply** → *model, apply, specify, encode*  
- **Analyze** → *analyze, integrate, justify, evaluate*  
- **Create** → *document, articulate, synthesize, present*



### Tabela — Estrutura de Agregação da Competência C20

| **Competência Agregada** | **Título** | **Tipo** | **ActivationRole** | **ActivationMode** | **ActivationConstraint** | **Contribuição para C20** |
|-------------------------|-----------|----------|---------------------|---------------------|---------------------------|---------------------------|
| **C18** | Model real-world problems using formal language concepts | Atômica | core | constructive | mandatory | Responsável pela abstração inicial do domínio musical e pela definição formal de alfabetos, cadeias e linguagens que estruturam o problema. |
| **C17** | Apply operations on formal languages | Atômica | core | analytical | mandatory | Sustenta a aplicação e análise de operações formais sobre linguagens, permitindo a caracterização estrutural das coleções musicais modeladas. |
| **C19** | Apply homomorphisms in formal languages | Atômica | supporting | interpretative | mandatory | Apoia a análise de codificações e transformações formais entre diferentes representações simbólicas, esclarecendo limites de equivalência. |
| **C04** | Define Regular Expressions for Finite Automata | Reutilizada | core | artifact-oriented | mandatory | Permite a especificação algébrica das coleções musicais por meio de expressões regulares, complementando a análise formal. |
| **C13′** | Interpret and apply algebraic notation for strings and languages | Reutilizada | transversal | analytical | mandatory | Fornece a base notacional e algébrica necessária para expressar linguagens, operações e propriedades de forma rigorosa. |
| **C05′** | Write mathematically rigorous answers | Reutilizada | transversal | justificatory | mandatory | Garante a produção de evidências textuais rigorosas, com definições, exemplos, contraexemplos e justificações formais integradas. |






### Mapeamento LO × Competências (versão corrigida)

| LO | Competências atendidas |
|----|------------------------|
| LO1.1 | C18, C13′ |
| LO1.2 | C18, C13′ |
| LO1.3 | C18, C13′ |
| LO2.1 | C13′, C17 |
| LO2.2 | C13′, C17 |
| LO2.3 | C05′, C13′ |
| LO3.1 | C17, C13′ |
| LO3.2 | C17 |
| LO3.3 | C17, C13′ |
| LO3.4 | C17 |
| LO4.1 | C17 |
| LO4.2 | C13′, C17 |
| LO4.3 | C17 |
| LO5.1 | C13′, C17 |
| LO5.2 | C17, C05′ |
| LO5.3 | C05′, C18 |
| LO6.1 | C04, C14 |
| LO6.2 | C04, C13′ |
| LO6.3 | C14 |
| LO7.1 | C04 |
| LO8.1 | C19, C13′ |
| LO8.2 | C19, C18 |
| LO8.3 | C19, C05′ |
| LO9.1 | C05′ |
| LO9.2 | C05′ |
| LO9.3 | C05′ |
| LO9.4 | C05′, C17 |
| LO10.1 | C05 |
| LO10.2 | C05′ |
| LO10.3 | C05′ |
