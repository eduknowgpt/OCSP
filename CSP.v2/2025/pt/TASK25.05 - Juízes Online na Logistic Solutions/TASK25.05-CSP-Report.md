# CSP-Report — TASK25.05  - Juízes Online na Logistic Solutions


## 1. Introdução

Este relatório apresenta a aplicação do **Competency Specification Process (CSP)** à *TASK25.05 — Juízes Online na Logistic Solutions*, uma tarefa baseada em Aprendizagem Baseada em Problemas (PBL) que investiga os limites teóricos e práticos de sistemas automatizados de avaliação, conhecidos como Online Judges (OJ).

A TASK25.05 representa uma evolução direta da TASK204, mantendo seu núcleo conceitual — a articulação entre Teoria da Computação, modelos formais e avaliação automática de programas — e ampliando o escopo analítico por meio da inclusão de problemas computacionalmente difíceis (como TSP e PT) e do aprofundamento da discussão sobre complexidade computacional, ocorrências de TLE e limitações fundamentais de sistemas automáticos.

Do ponto de vista metodológico, a tarefa foi concebida como um caso de reuso controlado de competências, fundamentado nos resultados consolidados do **ciclo CSP–CSRP–Adjustments da TASK204**. As competências previamente especificadas e avaliadas por especialistas mostraram-se suficientes, semanticamente estáveis e adequadas para sustentar a evolução da tarefa, dispensando a introdução de novas competências.


## 2. Análise da Entidade Instrucional

### 2.1 Identificação

- **Título:** *Juízes Online na Logistic Solutions*  
- **Tipo de Entidade Instrucional:** Tarefa baseada em **Aprendizagem Baseada em Problemas (Problem-Based Learning – PBL)**  
- **Domínio de Conhecimento:** **Teoria da Computação**, com foco em modelos formais, complexidade computacional e sistemas automáticos de avaliação  


### 2.2 Descrição Sintética

Os estudantes devem analisar o funcionamento de um **Juiz Online (OJ)** a partir da
avaliação automática de submissões para problemas **computacionalmente difíceis**,
como o **Problema do Caixeiro Viajante (TSP)** e o **Problema de Alocação de Horários (PT)**.

A tarefa requer a articulação entre **evidências empíricas de execução** (como resultados
**TLE**) e **fundamentação teórica**, promovendo a compreensão tanto de **limitações
práticas** quanto de **restrições teóricas** inerentes a sistemas automáticos de avaliação.

Em particular, a atividade envolve:

- a análise e interpretação de resultados **Time Limit Exceeded (TLE)**;
- o estudo da **complexidade computacional** associada a problemas de alta dificuldade;
- a discussão de **limitações teóricas fundamentais**, com ênfase no **Problema da Parada**;
- a **modelagem formal** do OJ por meio de uma **Máquina de Estados Finitos (MEF)**;
- a construção de **argumentação formal** sobre o que um OJ pode ou não detectar ou diagnosticar.

## 3. Resultados Esperados

Ao final da tarefa, os aprendizes devem produzir:

- uma **análise fundamentada** do comportamento de **TSP** e **PT** em Juízes Online;
- **justificativas teóricas consistentes** para a ocorrência de resultados **TLE**;
- uma **MEF** que represente o comportamento geral de um OJ;
- **simulações da MEF** utilizando ferramentas apropriadas (por exemplo, **JFLAP**);
- **respostas conceituais estruturadas** para gestores não técnicos;
- um **artigo técnico no formato da SBC**, com clareza, rigor científico e adequada fundamentação teórica.




## 4. Enumeração de Conhecimentos

### 4.1 Conhecimentos de Computação (CS2023)

- **Máquinas de Estados Finitos**  
  Modelos formais utilizados para representar o fluxo operacional de Juízes Online.

- **Máquinas de Turing (nível conceitual)**  
  Modelo de referência para fundamentar a expressividade computacional e os limites da análise automática de programas.

- **Problema da Parada**  
  Resultado central da Teoria da Computação que fundamenta a impossibilidade de detecção geral de loops infinitos.

- **Linguagens Recursivamente Enumeráveis (nível conceitual)**  
  Utilizadas para discutir problemas semi-decidíveis e limites de reconhecimento algorítmico.

- **Problemas P, NP e NP-Completos**  
  Base teórica para analisar a dificuldade computacional de problemas como TSP e PT e justificar ocorrências de TLE.

- **Hierarquia de Chomsky**  
  Estrutura de classificação utilizada para contextualizar o poder expressivo de diferentes modelos formais.

- **Complexidade Computacional**  
  Conceitos relacionados a custo temporal, escalabilidade e viabilidade prática de soluções algorítmicas.

- **Modelagem e Simulação de Autômatos**  
  Técnicas para construção, validação e análise de modelos formais, incluindo o uso de ferramentas como JFLAP.

### 4.2 Conhecimentos Profissionais (FPK — CC2020)

- **Pensamento analítico e crítico**  
  Necessário para interpretar resultados, estabelecer relações teóricas e construir justificativas consistentes.

- **Comunicação técnica escrita**  
  Competência essencial para a produção de um artigo técnico no formato da SBC, com clareza e rigor científico.




## 5. Objetivos de Aprendizagem

### Objetivo Geral

Aplicar conceitos da **Teoria da Computação** para **modelar, analisar e justificar**
o funcionamento e as limitações de **Juízes Online (OJ)**, relacionando problemas
reais de alta complexidade a fundamentos teóricos da computação.

### Objetivos Específicos

- **LO1:** analisar os problemas **TSP** e **PT** sob a perspectiva da **complexidade computacional**;
- **LO2:** explicar a ocorrência de resultados **Time Limit Exceeded (TLE)** em Juízes Online;
- **LO3:** compreender e **utilizar o Problema da Parada como base conceitual**
  para justificar limitações de análise automática de programas;
- **LO4:** modelar o comportamento de um Juiz Online por meio de uma
  **Máquina de Estados Finitos (MEF)**;
- **LO5:** justificar **limites teóricos fundamentais** de sistemas automáticos de avaliação;
- **LO6:** comunicar resultados e justificativas de forma clara a **públicos técnicos
  e não técnicos**, por meio de documentação formal.




## 6. Competências Reutilizadas

Com base no ciclo **CSP–CSRP–Adjustments** da **TASK204**, as competências abaixo são
reutilizadas na **TASK25.05**, pois permanecem alinhadas aos objetivos de:
(i) **modelagem formal do comportamento do OJ (MEF)**, (ii) **análise de limites teóricos
de automação**, e (iii) **produção de evidência técnico-científica**.

Entretanto, como a TASK25.05 intensifica explicitamente a análise de **TSP** e **PT**
sob a ótica da **complexidade computacional** e a justificativa de **TLE**, torna-se
necessário complementar o conjunto com **uma competência adicional** voltada a
complexidade/NP e estratégias algorítmicas, de forma a evitar que esse eixo central
da tarefa permaneça apenas como “conhecimento” sem correspondente competência avaliável.

### 6.1 Competências reutilizadas (mantidas)

- **C15 — Understand the Halting Problem and its Implications**  
  Fundamenta a justificativa de que sistemas automáticos (como OJs) não podem, em geral,
  detectar não-terminação ou diagnosticar completamente suas causas.
  - **ActivationConstraint:** `mandatory`
  - **ActivationMode:** `analytical`, `justificatory`
  - **ActivationRole:** `core`

- **C06 — Develop Problem-Solving Solutions Using Finite State Machines**  
  Sustenta a construção do modelo formal (MEF) que representa o fluxo operacional do OJ.
  - **ActivationConstraint:** `mandatory`
  - **ActivationMode:** `constructive`
  - **ActivationRole:** `supporting`

- **C03 — Test Automata Using Simulators**  
  Viabiliza validação/ilustração do modelo por simulação (ex.: JFLAP), quando requerido.
  - **ActivationConstraint:** `conditional`
  - **ActivationMode:** `artifact-oriented`
  - **ActivationRole:** `supporting`

- **C05 — Write a Technical Report**  
  Competência transversal associada ao principal artefato de evidência (artigo SBC).
  - **ActivationConstraint:** `mandatory`
  - **ActivationMode:** `artifact-oriented`
  - **ActivationRole:** `transversal`

- **C02 — Justify the Use of Deterministic Finite Automata (DFAs)**  
  Enriquecimento teórico para discutir adequação e limites do uso de modelos finitos na
  representação do OJ.
  - **ActivationConstraint:** `optional`
  - **ActivationMode:** `justificatory`
  - **ActivationRole:** `extension`

- **C14 — Differentiate Classifications of Formal Grammars**  
  Competência de extensão para contextualização na Hierarquia de Chomsky, sem impacto
  direto na conclusão da tarefa.
  - **ActivationConstraint:** `optional`
  - **ActivationMode:** `analytical`
  - **ActivationRole:** `extension`

- **C16 — Interpret Turing Machine Concepts to Analyze Computational System Capabilities**  
  Permanece teoricamente relevante, mas, como na TASK204, tende a apresentar sobreposição
  evidencial com C15 se não houver artefato específico para avaliá-la isoladamente.
  Mantém-se como competência de apoio/enriquecimento.
  - **ActivationConstraint:** `optional` ou `conditional`
  - **ActivationMode:** `interpretative`
  - **ActivationRole:** `supporting` ou `extension`



### 6.2 Competência adicional requerida pela evolução da TASK25.05 (nova)

### C21.1 Título da Competência

    Analisar a Complexidade Computacional e as Implicações da NP-Dificuldade


### C21.2 Descrição Textual

Esta competência refere-se à capacidade de **analisar a complexidade computacional**
e **interpretar as implicações da NP-dificuldade** no comportamento e na viabilidade
de soluções algorítmicas.

Os aprendizes devem ser capazes de compreender como **o tamanho da entrada, a estratégia
algorítmica e a classe de complexidade do problema** influenciam o custo computacional,
a escalabilidade e a possibilidade prática de execução de algoritmos sob **restrições
de tempo e recursos**.

A competência enfatiza a habilidade de **justificar limites de desempenho e viabilidade**
a partir da articulação entre **resultados teóricos da complexidade computacional** e
**restrições práticas de execução**, distinguindo limitações decorrentes de
**ineficiência algorítmica** daquelas associadas à **dificuldade computacional inerente
ao problema**.



### C21.3 Especificação de Conhecimentos

Os seguintes conhecimentos são essenciais para o desenvolvimento desta competência:

* **Complexidade Computacional**

  * Fundamenta a análise do custo algorítmico em termos de tempo e escalabilidade.
  * Permite raciocinar sobre limites de desempenho sob recursos computacionais finitos.

* **Problemas P, NP e NP-Difíceis / NP-Completos**

  * Estabelecem a base teórica para compreender dificuldades computacionais inerentes.
  * Sustentam a justificativa de inviabilidade de soluções eficientes em certos problemas.

* **Escalabilidade Algorítmica (nível conceitual)**

  * Relaciona o crescimento do tamanho da entrada ao comportamento do tempo de execução.
  * Apoia a interpretação de limites práticos de execução.

* **Pensamento Analítico e Crítico (FPK)**

  * Necessário para avaliar desempenho e construir justificativas coerentes.
  * Sustenta a articulação entre teoria da complexidade e observações empíricas.


### C21.4 Especificação de Disposições

**Colaboração**

* A competência pode ser desenvolvida em contextos colaborativos que favoreçam a
  comparação de interpretações sobre viabilidade e desempenho algorítmico.

**Responsabilidade**

* Os estudantes devem zelar pela **correção conceitual** e pela **coerência teórica**
  de suas análises, evitando generalizações indevidas.

**Proatividade**

* Os aprendizes buscam ativamente compreender implicações da complexidade computacional
  em diferentes cenários de aplicação.

**Criatividade**

* A criatividade apoia o uso de **exemplos, analogias e abstrações** para explicar
  fenômenos relacionados à complexidade.


### C21.5 Pareamento Conhecimento–Habilidade

#### C21.5.1 Mapeamento de Conhecimentos para Habilidades

* **Analisar** a **complexidade computacional** para interpretar limites de desempenho.
* **Compreender** a **NP-dificuldade** para justificar inviabilidade prática.
* **Compreender** efeitos de **escalabilidade** na execução de algoritmos.
* **Aplicar** pensamento analítico e crítico para estruturar justificativas.


#### C21.5.2 Alinhamento com a Taxonomia de Bloom

* **Complexidade Computacional – Analisar**
* **NP-Dificuldade – Compreender**
* **Escalabilidade – Compreender**
* **Pensamento Analítico e Crítico – Aplicar**


#### C21.5.3 Anotação de Verbos

* **Analisar** → Complexidade Computacional → *Decompor, Relacionar, Interpretar*
* **Compreender** → NP-Dificuldade → *Explicar, Justificar, Distinguir*
* **Compreender** → Escalabilidade → *Relacionar, Interpretar, Explicar*
* **Aplicar** → Pensamento Analítico e Crítico → *Avaliar, Estruturar, Argumentar*


### C21.6 Tabela-Resumo da Competência C21

| **Competência**                                             | **Disposições**                                       | **Conhecimentos**                 | **Habilidade**                                   |
| ------------------------------------------------------------ | ---------------------------------------------------- | --------------------------------- | ------------------------------------------------ |
| Analisar a Complexidade Computacional e as Implicações da NP-Dificuldade | Colaboração, Responsabilidade, Proatividade, Criatividade | Complexidade Computacional         | **Analisar (Decompor, Relacionar, Interpretar)** |
|                                                              |                                                      | P, NP, NP-Difíceis / NP-Completos | **Compreender (Explicar, Justificar, Distinguir)** |
|                                                              |                                                      | Escalabilidade Algorítmica        | **Compreender (Relacionar, Interpretar, Explicar)** |
|                                                              |                                                      | Pensamento Analítico e Crítico    | **Aplicar (Avaliar, Estruturar, Argumentar)**    |



### 6.3 Configuração Consolidada de Ativações (TASK25.05)

| Competência | Constraint | Mode | Role |
|---|---|---|---|
| **C15 — Understand the Halting Problem and its Implications** | mandatory | analytical, justificatory | core |
| **C21 — Analyze Computational Complexity and NP-Difficulty Implications** | mandatory | analytical, justificatory | core |
| **C06 — Develop Problem-Solving Solutions Using Finite State Machines** | mandatory | constructive | supporting |
| **C03 — Test Automata Using Simulators** | conditional | artifact-oriented | supporting |
| **C16 — Interpret Turing Machine Concepts** | optional / conditional | interpretative | supporting / extension |
| **C02 — Justify the Use of Deterministic Finite Automata (DFAs)** | optional | justificatory | extension |
| **C14 — Differentiate Classifications of Formal Grammars** | optional | analytical | extension |
| **C05 — Write a Technical Report** | mandatory | artifact-oriented | transversal |





## 7. Avaliação sobre Novas Competências

A ampliação do escopo da TASK25.05 — com a inclusão explícita de problemas
computacionalmente difíceis e o aprofundamento da análise de **complexidade
computacional e escalabilidade** — **motivou a introdução de uma nova competência
nuclear**, a **C21**.

A competência **C21** não representa inflacionamento do conjunto competencial,
mas sim o **desacoplamento e a explicitação de um eixo cognitivo** que, na TASK204,
estava presente apenas de forma implícita no nível de conhecimento.

Com a introdução da C21, a TASK25.05:

- preserva o **reuso integral** das competências previamente especificadas;
- explicita o eixo de **análise de complexidade e viabilidade algorítmica**;
- eleva o nível cognitivo da tarefa sem comprometer a modularidade do modelo;
- mantém plena aderência aos princípios de **reusabilidade, coerência e rastreabilidade**
  que orientam o CSP e a OntoKSD.

Portanto, a evolução da tarefa é acompanhada por uma **extensão mínima e
metodologicamente justificada** do conjunto de competências, mantendo a
consistência do modelo e a clareza avaliativa.




## 8. Estrutura Semântica Resultante

````
TASK25.05
├── C15 (Problema da Parada)
├── C21 (Complexidade Computacional e NP-Dificuldade)
├── C06 (Modelagem por MEF)
├── C03 (Simulação de Autômatos)
├── C16 (Conceitos de Máquinas de Turing)
├── C02 (Justificação de DFA)
├── C14 (Hierarquia de Chomsky)
└── C05 (Comunicação Técnica)
````

## 9. Conclusão

A TASK25.05 representa uma **evolução conceitual consistente e controlada** da TASK204,
ampliando o domínio do problema e aprofundando a análise teórica por meio da
integração explícita de **complexidade computacional**, **escalabilidade** e
**viabilidade algorítmica**, sem descaracterizar o núcleo conceitual da tarefa original.

Essa evolução foi sustentada, em grande medida, pelo **reuso sistemático das
competências previamente especificadas**, cuja adequação e estabilidade semântica
foram confirmadas no ciclo **CSP–CSRP–Adjustments** da TASK204. A introdução da
competência **C21** constitui uma **extensão mínima, necessária e metodologicamente
justificada**, permitindo explicitar um eixo cognitivo que, na tarefa original,
estava presente apenas de forma implícita no nível de conhecimento.

O resultado é um conjunto competencial **coeso, não inflacionado e plenamente
rastreável**, que evidencia a **robustez do modelo CSP**, sua capacidade de apoiar
a evolução de tarefas instrucionais e sua aderência aos princípios de
**modularidade, coerência semântica e reusabilidade** que orientam a ontologia
**OntoKSD**.
