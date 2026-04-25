# CSP-Report — TASK25.05 — *Juízes Online na Logistic Solutions* (versão corrigida)

## 1. Introdução

Este relatório aplica o **Competency Specification Process (CSP)** à **TASK25.05 — Juízes Online na Logistic Solutions**, uma tarefa cujo objetivo é **modelar, analisar e justificar teoricamente o comportamento de sistemas de avaliação automática de programas** (*Online Judges*), articulando conceitos de **Máquinas de Estados Finitos**, **complexidade computacional**, **computabilidade** e **limitações fundamentais da análise automática de programas**.

A tarefa parte de um cenário em que estudantes e profissionais investigam por que implementações para o **Problema do Caixeiro Viajante (TSP)** e para o **Problema de Alocação de Horários (PT – Timetabling)** continuam produzindo **TLE (Time Limit Exceeded)** em um OJ, mesmo após a correção de erros de compilação, execução e resposta. Além disso, a tarefa exige que os estudantes analisem até que ponto um OJ pode avaliar diferentes tipos de problemas e **diagnosticar razões para TLE**, tanto em códigos de programadores experientes quanto iniciantes. 

Em relação à **Task204**, a **Task25.05** preserva o núcleo relativo à modelagem do OJ por meio de uma **Máquina de Estados Finitos (MEF)** e à análise de suas limitações teóricas, mas introduz uma mudança importante de escopo. Enquanto Task204 concentrava-se mais diretamente no **TSP** e na impossibilidade de detectar **laços infinitos** como desdobramento do **Problema da Parada**, a Task25.05 amplia a discussão para:

- múltiplos problemas difíceis (**TSP** e **PT**);
- relações entre **TLE**, **complexidade temporal** e **estratégias algorítmicas**;
- limites do OJ para explicar ou prever completamente certas causas de comportamento;
- distinção entre **limitações práticas** e **limitações teóricas** dos sistemas automáticos de avaliação. 


Assim, a versão 25.05 desloca o centro da tarefa para uma integração entre:

- **análise de complexidade e NP-completude**;
- **modelagem formal do fluxo do OJ por FSM**;
- **discussão de computabilidade e indecidibilidade**;
- **comunicação técnica rigorosa**.

Essa mudança justifica uma atualização do perfil de competências em relação à Task204, preservando competências estáveis quando seu escopo permanece adequado e introduzindo nova centralidade para a competência de **complexidade computacional**.






## 2. Análise da Entidade Instrucional

### 2.1 Identificação

- **Título:** Juízes Online na Logistic Solutions 2025 
- **Tipo:** Caso PBL com ênfase em modelagem formal, análise de complexidade e limitações computacionais  
- **Domínio:** Teoria da Computação — Autômatos Finitos, Computabilidade e Complexidade Computacional. 

### 2.2 Descrição Sintética

A tarefa requer que os estudantes analisem o funcionamento de um **Online Judge (OJ)**, expliquem por que instâncias de **TSP** e **PT** tendem a gerar **TLE**, investiguem as capacidades e limitações desses sistemas para avaliar programas e diagnosticar seus comportamentos, e construam uma **Máquina de Estados Finitos (MEF)** que represente o fluxo geral de avaliação do OJ.

Os estudantes devem articular:

- o comportamento observável do OJ (AC, WA, CE, RE, TLE);
- a dificuldade prática de resolver problemas como **TSP** e **PT** dentro de limites de tempo;
- a base teórica que explica por que certos aspectos da análise automática de programas são intrinsecamente limitados;
- a comunicação dessas conclusões em um **artigo técnico no formato SBC**. 




### 2.3 Mudanças principais em relação à Task204

A Task25.05 altera a Task204 em quatro aspectos principais:

1. **Ampliação do conjunto de problemas analisados**: além do **TSP**, a nova versão inclui explicitamente o **PT (Timetabling)**, reforçando a discussão sobre problemas difíceis e estratégias para evitar TLE. 

2. **Ampliação da análise do OJ**: a questão deixa de ser apenas se o OJ detecta laços infinitos e passa a incluir se ele consegue **avaliar diferentes classes de problemas** e **identificar razões para TLE**.
  
3. **Maior centralidade da complexidade computacional**: a nova formulação enfatiza explicitamente **P, NP, NP-completude, complexidade temporal** e estratégias algorítmicas. 

4. **Preservação, mas recontextualização, da discussão teórica sobre limites**: o **Problema da Parada** permanece relevante, mas agora integrado a uma análise mais ampla das limitações dos OJs. 







## 3. Resultados Esperados

Ao final da tarefa, espera-se que os estudantes produzam:

- um **artigo técnico em formato SBC** contendo a análise do **TSP** e do **PT** no contexto de OJs;
- respostas fundamentadas às perguntas dos gestores sobre as **capacidades e limitações** dos OJs;
- uma **Máquina de Estados Finitos (MEF)** representando o comportamento geral do OJ, com estados como **AC, WA, CE, RE e TLE**;
- exemplos e argumentos que expliquem por que determinados problemas tendem a gerar **TLE**;
- justificativas teóricas que distingam entre **limitações práticas** de desempenho e **limitações teóricas** de análise automática. 


Como evidência adicional, pode haver **simulação da MEF em JFLAP**, quando essa exploração fizer parte da solução proposta. 




## 4. Enumeração de Conhecimentos

A realização adequada da **TASK25.05 — Juízes Online na Logistic Solutions** requer a mobilização integrada de conhecimentos disciplinares em **Teoria da Computação** e de conhecimentos profissionais fundamentais, conforme os referenciais do **CS2023** e do **CC2020**.

### 4.1 Conhecimentos de Computação

- **Máquinas de Estados Finitos**
  - estados e transições;
  - modelagem de fluxos de avaliação;
  - representação de comportamentos observáveis de sistemas automáticos.

- **Complexidade Computacional**
  - classes **P**, **NP** e **NP-complete**;
  - relação entre dificuldade computacional e crescimento do tempo de execução;
  - implicações práticas da NP-hardness para problemas como **TSP** e **PT**.

- **Computabilidade**
  - problema da parada;
  - limites da análise automática de programas;
  - distinção entre o que pode ser automatizado em geral e o que não pode.

- **Máquinas de Turing e Linguagens Recursivamente Enumeráveis**
  - uso conceitual como modelo de referência para discutir computação geral;
  - relação com capacidades e limites de sistemas automáticos de avaliação.

- **Avaliação Automática de Programas**
  - interpretação de resultados como **AC, WA, CE, RE e TLE**;
  - relação entre características do algoritmo e respostas do OJ. 


  
### 4.2 Conhecimentos Profissionais Fundamentais (FPK — CC2020)

- **Pensamento Analítico e Crítico**  
  Capacidade de relacionar observações empíricas (como TLE) a explicações teóricas rigorosas, distinguindo causas algorítmicas, limitações práticas e limitações fundamentais.

- **Comunicação Técnica Escrita**  
  Capacidade de produzir um **relatório claro, estruturado e teoricamente fundamentado**, articulando modelagem, explicações conceituais e exemplos. 




## 5. Objetivos de Aprendizagem

### Objetivo Geral

Aplicar conceitos fundamentais da **Teoria da Computação** para modelar, analisar e explicar problemas práticos relacionados a **Juízes Online (OJ)**, articulando **modelagem por FSM**, **complexidade computacional**, **problemas NP-completos** e **limitações teóricas da análise automática de programas**. 


### Objetivos Específicos

Ao concluir a tarefa, o estudante deverá ser capaz de:

- **LO1 — Explicar o fluxo de avaliação de um OJ por meio de FSMs**  
  Representar estados e transições associados a resultados como AC, WA, CE, RE e TLE.

- **LO2 — Analisar por que TSP e PT tendem a produzir TLE**  
  Relacionar o comportamento observado às características de complexidade computacional dos problemas.

- **LO3 — Discutir estratégias para alcançar AC em problemas difíceis**  
  Identificar implicações práticas da escolha algorítmica frente aos limites do OJ.

- **LO4 — Explicar limitações teóricas do OJ**  
  Justificar por que certos comportamentos de programas não podem ser analisados ou previstos completamente em geral.

- **LO5 — Interpretar o papel de Máquinas de Turing e computabilidade**  
  Relacionar modelos gerais de computação às capacidades e limites dos OJs.

- **LO6 — Comunicar tecnicamente as análises e conclusões**  
  Elaborar um artigo técnico rigoroso com exemplos, explicações e justificativas teóricas.

- **LO7 — Simular e validar a MEF do OJ, quando aplicável**  
  Utilizar ferramentas como o JFLAP para testar e ilustrar o modelo proposto. 





## 6. Competências da TASK25.05 (com Ativações OntoKSD) 

As competências a seguir constituem o **perfil de desempenho esperado** para a **TASK25.05 — Juízes Online na Logistic Solutions**. O conjunto foi definido com base no **catálogo atual**, preservando competências já estabilizadas em **Task204** quando seu escopo continua adequado, mas documentando as mudanças exigidas pela nova versão da tarefa.


### 6.1 Competências centrais

#### **C21 — Analyze Computational Complexity and the Implications of NP-Hardness**

**Tipo:** Competência atômica

**ActivationRole:** `core`  
**ActivationMode:** `analytical`  
**ActivationConstraint:** `mandatory`

**Particularização na TASK25.05:**  
Analisar por que instâncias de **TSP** e **PT** tendem a gerar **TLE**, relacionando esse comportamento à **complexidade computacional**, à dificuldade de obtenção de soluções exatas eficientes e às implicações práticas da **NP-hardness** em ambientes de avaliação automática.

**Mudança em relação à Task204:**  
Na Task204, o foco estava mais concentrado no **TSP** e na explicação de limitações do OJ com base no **Halting Problem**. Na Task25.05, a inclusão explícita de **TSP + PT**, bem como a exigência de discutir estratégias para alcançar **AC**, torna a análise de **complexidade e NP-completude** uma competência central da tarefa.




#### **C15 — Understand the Halting Problem and its Implications**

**Tipo:** Competência atômica

**ActivationRole:** `core`  
**ActivationMode:** `analytical`, `justificatory`  
**ActivationConstraint:** `mandatory`

**Particularização na TASK25.05:**  
Explicar por que existem limites fundamentais para a análise automática de programas em OJs, especialmente quando se pergunta se o sistema consegue **diagnosticar integralmente causas de TLE** ou prever certos comportamentos de execução. A competência continua relevante porque a Task25.05 mantém a discussão sobre limites teóricos da avaliação automática, ainda que de forma mais ampla que em Task204.


**Mudança em relação à Task204:**  
Na Task204, C15 era a **principal nova competência nuclear** porque a questão sobre **laços infinitos** estava no centro da tarefa. Na Task25.05, C15 permanece central, mas divide protagonismo com **C21**, já que a análise do OJ passou a envolver também uma forte dimensão de **complexidade computacional**.



### 6.2 Competências de apoio

#### **C06 — Develop Problem-Solving Solutions Using Finite State Machines**

**Tipo:** Competência atômica

**ActivationRole:** `supporting`  
**ActivationMode:** `constructive`  
**ActivationConstraint:** `mandatory`

**Particularização na TASK25.05:**  
Construir uma **MEF** que represente o comportamento do OJ, incluindo estados como **AC, WA, CE, RE e TLE**, bem como transições coerentes com o fluxo geral de avaliação.

**Mudança em relação à Task204:**  
Mantém o mesmo papel de **apoio construtivo** já consolidado nos ajustes da Task204: a FSM não é o núcleo cognitivo da tarefa, mas um **mecanismo de externalização do raciocínio** sobre o OJ.




#### **C16 — Interpret Turing Machine Concepts to Analyze Computational System Capabilities**

**Tipo:** Competência atômica

**ActivationRole:** `supporting`  
**ActivationMode:** `interpretative`  
**ActivationConstraint:** `conditional`

**Particularização na TASK25.05:**  
Interpretar conceitos de **Máquinas de Turing**, **Máquina de Turing Universal** e **computabilidade** para analisar as capacidades e limitações dos OJs como sistemas automáticos de avaliação.

**Mudança em relação à Task204:**  
Preserva o papel interpretativo definido em Task204, mas agora aparece com utilidade um pouco mais clara, já que a Task25.05 menciona explicitamente **Máquina de Turing Universal**, **linguagens recursivamente enumeráveis** e análise de limites do OJ diante de problemas mais amplos.




#### **C03 — Test Automata Using Simulators**

**Tipo:** Competência atômica

**ActivationRole:** `supporting`  
**ActivationMode:** `artifact-oriented`  
**ActivationConstraint:** `conditional`

**Particularização na TASK25.05:**  
Utilizar o **JFLAP** para testar e ilustrar a **MEF do OJ**, quando essa simulação fizer parte efetiva da solução apresentada.

**Mudança em relação à Task204:**  
Mantém o mesmo estatuto de competência **condicional**, pois a profundidade da simulação pode variar sem alterar o núcleo teórico da tarefa.



### 6.3 Competências de extensão

#### **C02 — Justify the use of Deterministic Finite Automata (DFAs)**

**Tipo:** Competência atômica

**ActivationRole:** `extension`  
**ActivationMode:** `justificatory`  
**ActivationConstraint:** `optional`

**Particularização na TASK25.05:**  
Pode ser mobilizada quando a equipe quiser justificar mais explicitamente por que uma **FSM/MEF** é um modelo adequado para representar o fluxo observável do OJ. Não constitui objetivo central nem gera evidência independente obrigatória.

**Mudança em relação à Task204:**  
Permanece como extensão opcional, em linha com os ajustes já consolidados.




#### **C14 — Differentiate classifications of formal grammars**

**Tipo:** Competência atômica

**ActivationRole:** `extension`  
**ActivationMode:** `analytical`  
**ActivationConstraint:** `optional`

**Particularização na TASK25.05:**  
Pode enriquecer a discussão quando os estudantes articularem a capacidade do OJ para avaliar problemas de diferentes naturezas com referências mais amplas à hierarquia de linguagens e modelos.

**Mudança em relação à Task204:**  
Mantém função de extensão, sem centralidade.



### 6.4 Competência transversal

#### **C05 — Write a Technical Report**

**Tipo:** Competência transversal

**ActivationRole:** `transversal`  
**ActivationMode:** `artifact-oriented`  
**ActivationConstraint:** `mandatory`

**Particularização na TASK25.05:**  
Produzir o artigo técnico em formato **SBC**, conectando a modelagem por FSM, a análise de **TSP** e **PT**, as limitações do OJ e as justificativas teóricas de forma clara, organizada e verificável.

**Mudança em relação à Task204:**  
Mantém exatamente o papel transversal e evidencial já definido nos ajustes da Task204.




## 7. Estrutura OntoKSD implícita (TASK25.05)

```text
TASK25.05
├── coreCompetence
│   ├── C21 — Analyze Computational Complexity and the Implications of NP-Hardness
│   └── C15 — Understand the Halting Problem and its Implications
│
├── supportingCompetence
│   ├── C06 — Develop Problem-Solving Solutions Using Finite State Machines
│   ├── C16 — Interpret Turing Machine Concepts to Analyze Computational System Capabilities
│   └── C03 — Test Automata Using Simulators (conditional)
│
├── extensionCompetence
│   ├── C02 — Justify the use of Deterministic Finite Automata (optional)
│   └── C14 — Differentiate classifications of formal grammars (optional)
│
└── transversalCompetence
    └── C05 — Write a Technical Report

```




## 8. Mapeamento entre Objetivos de Aprendizagem (LOs) e Competências — TASK25.05

O mapeamento a seguir explicita a **rastreabilidade pedagógica** entre os objetivos da tarefa e as competências mobilizadas, evidenciando como a **Task25.05** reorganiza o foco da antiga **Task204** ao tornar mais central a análise de **complexidade computacional**, sem abandonar a discussão sobre **limites teóricos da análise automática de programas**.

| **LO** | **Descrição do Objetivo de Aprendizagem** | **Competências Mobilizadas** |
|---|---|---|
| **LO1** | Explicar o fluxo de avaliação de um OJ por meio de FSMs | **C06**, **C02** |
| **LO2** | Analisar por que TSP e PT tendem a produzir TLE | **C21** |
| **LO3** | Discutir estratégias para alcançar AC em problemas difíceis | **C21**, **C05** |
| **LO4** | Explicar limitações teóricas do OJ | **C15**, **C16** |
| **LO5** | Interpretar o papel de Máquinas de Turing e computabilidade | **C16**, **C15** |
| **LO6** | Comunicar tecnicamente as análises e conclusões | **C05** |
| **LO7** | Simular e validar a MEF do OJ, quando aplicável | **C03**, **C06** |
| **LO8** | Relacionar a análise do OJ à complexidade e a problemas NP-completos | **C21**, **C14** |

Esse mapeamento mostra que a **Task25.05** desloca o centro da antiga **Task204**: a modelagem do OJ por **FSM/MEF** continua relevante, mas a nova versão torna explicitamente centrais a **análise de complexidade**, as implicações da **NP-hardness** e a distinção entre **limitações práticas** e **limitações teóricas** dos sistemas automáticos de avaliação.




## 9. Conclusão

A **TASK25.05** deve ser entendida como uma **evolução da Task204**, e não apenas como uma reformulação textual. A nova versão amplia o problema original ao incorporar explicitamente o **Problema de Alocação de Horários (PT)**, reforçar a discussão sobre **complexidade computacional** e ampliar o escopo da análise dos **Juízes Online** para além da questão da simples detecção de laços infinitos.