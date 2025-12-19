# CSP-Report — TASK25.05  - Juízes Online na Logistic Solutions


## 1. Introdução

Este relatório apresenta a aplicação do **Competency Specification Process (CSP)** à  
**TASK25.05 — Juízes Online na Logistic Solutions**, uma tarefa baseada em
**Aprendizagem Baseada em Problemas (PBL)** que explora os **limites teóricos e
práticos de sistemas automatizados de avaliação (Online Judges – OJ)**.

A TASK25.05 constitui uma **evolução direta da TASK204**, ampliando o escopo do
problema, aprofundando o rigor conceitual e fortalecendo a integração entre
**modelagem formal, complexidade computacional e teoria da computação**.


## 2. Análise da Entidade Instrucional

### 2.1 Identificação

- **Título:** Juízes Online na Logistic Solutions  
- **Tipo:** Tarefa PBL  
- **Domínio:** Teoria da Computação  

### 2.2 Descrição Sintética

Os estudantes devem analisar o funcionamento de um **Juiz Online (OJ)** a partir de
submissões de soluções para problemas computacionalmente difíceis, como o
**Problema do Caixeiro Viajante (TSP)** e o **Problema de Alocação de Horários (PT)**.

A tarefa envolve:

- análise de resultados **TLE**;
- estudo de **complexidade computacional**;
- discussão de **limitações teóricas** (Problema da Parada);
- modelagem do OJ por meio de uma **Máquina de Estados Finitos (MEF)**;
- argumentação formal sobre o que um OJ pode ou não detectar.



## 3. Resultados Esperados

Os aprendizes devem produzir:

- uma análise fundamentada sobre **TSP e PT** em OJs;
- justificativas teóricas para ocorrências de **TLE**;
- uma **MEF** representando o comportamento geral de um OJ;
- simulações da MEF (ex.: JFLAP);
- respostas conceituais para gestores não técnicos;
- um **artigo técnico no formato da SBC**, com rigor científico.



## 4. Enumeração de Conhecimentos

### 4.1 Conhecimentos de Computação (CS2023)

- Máquinas de Estados Finitos
- Máquinas de Turing
- Problema da Parada
- Linguagens Recursivamente Enumeráveis
- Problemas P, NP e NP-Completos
- Hierarquia de Chomsky
- Complexidade Computacional
- Modelagem e Simulação de Autômatos


### 4.2 Conhecimentos Profissionais (FPK — CC2020)

- Pensamento analítico e crítico  
- Comunicação técnica escrita  



## 5. Objetivos de Aprendizagem

### Objetivo Geral

Aplicar conceitos da **Teoria da Computação** para modelar, analisar e justificar
o funcionamento e as limitações de **Juízes Online**, relacionando problemas
reais de alta complexidade a fundamentos teóricos da computação.

### Objetivos Específicos

- LO1: analisar **TSP** e **PT** sob a ótica da complexidade;
- LO2: explicar a ocorrência de **TLE** em OJs;
- LO3: compreender e aplicar o **Problema da Parada**;
- LO4: modelar o OJ por meio de uma **MEF**;
- LO5: justificar limites teóricos de sistemas automáticos;
- LO6: comunicar resultados a públicos técnicos e não técnicos.



## 6. Competências Reutilizadas

Com base no **TASK204-CSP-Report**, as seguintes competências são **integralmente
reutilizadas**, pois continuam **necessárias e suficientes** para a TASK25.05.


- **C15 — Understand the Halting Problem and its Implications**  
  Essencial para justificar a impossibilidade de detecção geral de loops infinitos.

- **C16 — Apply Turing Machine Concepts to Analyze Computational System Capabilities**  
  Fundamenta a análise de capacidades e limites dos OJs.

- **C06 — Develop Problem-Solving Solutions Using Finite State Machines**  
  Necessária para modelar o comportamento do OJ por meio de uma MEF.

- **C02 — Justify the Use of Deterministic Finite Automata (DFAs)**  
  Sustenta a adequação (e limites) do uso de modelos finitos para representar OJs.

- **C03 — Test Automata Using Simulators**  
  Utilizada para validar e ilustrar o modelo por meio de simulação.

- **C14 — Differentiate Classifications of Formal Grammars**  
  Apoia a contextualização do OJ na Hierarquia de Chomsky.

- **C05 — Write a Technical Report**  
  Necessária para produção do artigo no formato SBC, com clareza e rigor.



## 7. Avaliação sobre Novas Competências

Apesar da ampliação do escopo (inclusão do PT e aprofundamento da análise),
**não se identificou a necessidade de novas competências**.

A TASK25.05:
- intensifica o uso das competências existentes;
- eleva o nível cognitivo de aplicação e análise;
- integra competências já definidas de forma mais profunda.

Portanto, o **reuso é suficiente e metodologicamente adequado**.

---

## 8. Estrutura Semântica Resultante

````
TASK25.05
├── C15 (Problema da Parada)
├── C16 (Máquinas de Turing e capacidades computacionais)
├── C06 (MEF)
├── C02 (Justificação de DFA)
├── C03 (Simulação)
├── C14 (Hierarquia de Chomsky)
└── C05 (Comunicação técnica)
````


## 9. Conclusão

A TASK25.05 representa uma **evolução conceitual consistente** da TASK204,
ampliando o domínio do problema e aprofundando a análise teórica, sem exigir
novas competências.

O **reuso integral** das competências previamente especificadas demonstra a
**robustez do modelo CSP**, sua capacidade de adaptação a tarefas evolutivas e
sua aderência aos princípios de **modularidade, coerência e reutilização** que
orientam a OntoKSD.
