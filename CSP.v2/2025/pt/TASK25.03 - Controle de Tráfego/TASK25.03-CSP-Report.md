# CSP-Report — TASK25.03 — *Controle de Tráfego* (versão 2025)

## 1. Introdução

Este relatório aplica o **Competency Specification Process (CSP)** à **TASK25.03 — Controle de Tráfego**, uma tarefa cujo objetivo é **modelar, analisar e justificar computacionalmente um sistema de monitoramento de veículos pesados**, utilizando **Máquinas de Turing** e seus conceitos associados para processar dados provenientes de sensores em uma rodovia real.  

A tarefa descreve um cenário no qual sensores instalados na estrada de Aratu, em Salvador, categorizam veículos noturnos em **leves, pesados e muito pesados**, com base em seu peso, e demandam um sistema capaz de **contabilizar a quantidade de veículos por categoria** e **identificar a categoria predominante** da noite anterior, de modo a subsidiar políticas de preservação do asfaltamento. 

A **TASK25.03** constitui uma reformulação curricularmente atualizada da **Tarefa02**, preservando o núcleo do problema — a modelagem computacional de um sistema de controle de tráfego baseado em sensores —, mas alterando de forma significativa sua **organização pedagógica e epistemológica**. Enquanto a versão original estava fortemente ancorada em práticas de **PBL processual**, exigindo quadros de fatos, ideias, ações e diários de bordo como parte da avaliação, a TASK25.03 desloca o foco para **evidências formais e tecnicamente verificáveis**, consistindo essencialmente em **artefatos computacionais** (máquinas em JFLAP) e em um **relatório técnico rigoroso**. Além disso, a versão atualizada enfatiza explicitamente a **fundamentação teórica da solução**, posicionando o uso de Máquinas de Turing e da **tese de Church–Turing** não apenas como instrumentos de implementação, mas como **meios de análise e validação conceitual** do sistema proposto. 

Essa mudança transforma a tarefa de uma atividade predominantemente processual e narrativa em uma **atividade orientada a competências formais**, permitindo que o desempenho do estudante seja avaliado pela **qualidade do modelo computacional e de sua justificação teórica**, e não pela documentação de seu percurso colaborativo.



## 2. Análise da Entidade Instrucional

### 2.1 Identificação

- **Título:** Controle de Tráfego  
- **Tipo:** Caso PBL com ênfase em modelagem formal e análise computacional  
- **Domínio:** Teoria da Computação — Máquinas de Turing e Computabilidade. 



### 2.2 Descrição

A tarefa requer que os estudantes **modelem formalmente um sistema de monitoramento de tráfego rodoviário**, no qual dados provenientes de sensores classificam veículos em diferentes categorias de peso ao longo de uma noite. Essas leituras devem ser representadas como **cadeias sobre um alfabeto simbólico**, e o comportamento do sistema deve ser descrito por uma **Máquina de Turing (MT)** capaz de **contabilizar ocorrências, comparar quantidades e decidir qual categoria de veículo foi predominante**.

Os estudantes devem projetar uma MT que **leia a fita de entrada**, **processe os símbolos correspondentes aos veículos**, **mantenha contadores ou marcas auxiliares** e **produza uma saída computada** correspondente à categoria predominante — ou a uma codificação equivalente dessa decisão. A tarefa exige que esse modelo seja **formalmente especificado**, **executável em simulador (JFLAP)** e **teoricamente justificado** à luz da **tese de Church–Turing**, explicitando por que o problema é computável e adequadamente modelado por uma MT.

Diferentemente de versões anteriores, a TASK25.03 concentra-se na **qualidade formal do modelo computacional e de sua justificativa**, e não na documentação do processo colaborativo, alinhando a atividade ao paradigma de **avaliação por competências** em Teoria da Computação. 




## 3. Resultados Esperados

Ao final da tarefa, espera-se que os estudantes produzam **artefatos formais e justificativas teóricas** que evidenciem sua capacidade de **modelar e analisar um sistema computacional baseado em dados de sensores**. Em particular, os estudantes deverão apresentar:

- uma **Máquina de Turing funcional**, implementada e testada em simulador, capaz de **processar a sequência de veículos registrada**, **contabilizar adequadamente as categorias** e **decidir corretamente qual categoria de peso foi predominante**;
- **simulações documentadas** que demonstrem o comportamento da máquina para diferentes entradas;
- um **relatório técnico matematicamente rigoroso** contendo:
  - a **especificação formal da máquina**;
  - a **interpretação de seus estados, transições e símbolos auxiliares**;
  - a **descrição da forma de saída produzida**;
  - a **justificação teórica de sua correção e computabilidade**, fundamentada na **tese de Church–Turing** e nos princípios da Teoria da Computação. 
  




## 4. Enumeração de Conhecimentos

A realização adequada da **TASK25.03 — Controle de Tráfego** requer a mobilização integrada de conhecimentos disciplinares em **Teoria da Computação** e de conhecimentos profissionais fundamentais, conforme os referenciais do **CS2023** e do **CC2020**. Esses conhecimentos sustentam tanto a **modelagem formal do problema** quanto a **análise de computabilidade e correção do sistema**. 




### 4.1 Conhecimentos de Computação (CS2023)

- **Teoria da Computabilidade**
  - noção de função computável;
  - tese de Church–Turing;
  - limites e alcance dos modelos de computação efetiva.

- **Máquinas de Turing**
  - definição formal de MT;
  - estados, símbolos, transições e fita;
  - variantes e extensões conceituais.

- **Linguagens e Decisão**
  - linguagens reconhecíveis e decidíveis;
  - problemas de decisão sobre cadeias.

- **Modelagem de Processamento de Dados**
  - interpretação de entradas simbólicas provenientes de sensores;
  - contagem, comparação e decisão sobre quantidades.

- **Simulação de Modelos Computacionais**
  - uso de ferramentas como o **JFLAP** para execução e teste de Máquinas de Turing. 



### 4.2 Conhecimentos Profissionais Fundamentais (FPK — CC2020)

- **Pensamento Analítico e Crítico**  
  Capacidade de decompor o comportamento do sistema, avaliar a correção do modelo e justificar formalmente as decisões de projeto.

- **Comunicação Técnica Escrita**  
  Capacidade de produzir um **relatório claro, estruturado e matematicamente preciso**, expressando definições, argumentos e conclusões de forma coerente. 






## 5. Objetivos de Aprendizagem

### Objetivo Geral

Capacitar o estudante a **modelar, implementar e justificar formalmente sistemas computacionais de processamento de dados**, utilizando **Máquinas de Turing** para representar, executar e analisar **procedimentos de decisão e contagem** sobre sequências simbólicas. 


### Objetivos Específicos

Ao concluir a tarefa, o estudante deverá ser capaz de:

- **LO1 — Abstrair dados do mundo real em representações simbólicas**  
  Representar leituras de sensores e categorias de veículos por meio de **símbolos de um alfabeto formal** e **cadeias de entrada**.

- **LO2 — Definir formalmente o problema computacional**  
  Especificar o problema de **contabilização e decisão** como uma **função computável ou problema de decisão** sobre cadeias.

- **LO3 — Construir uma Máquina de Turing**  
  Projetar uma **MT funcional** capaz de processar a entrada simbólica e produzir a decisão correta sobre a categoria predominante.

- **LO4 — Simular e validar o modelo computacional**  
  Utilizar um **simulador de MT (JFLAP)** para testar o comportamento da máquina em diferentes entradas.

- **LO5 — Justificar computabilidade e correção**  
  Demonstrar formalmente que o problema é **computável** e que a MT construída **resolve corretamente** o problema proposto, com base na **tese de Church–Turing**.

- **LO6 — Comunicar resultados tecnicamente**  
  Produzir um **relatório técnico rigoroso**, apresentando o modelo, as simulações e as justificativas de forma clara e matematicamente precisa. 






## 6. Competências da TASK25.03 (com Ativações OntoKSD)  

As competências a seguir constituem o **perfil de desempenho esperado** para a **TASK25.03 — Controle de Tráfego**. O conjunto foi elaborado com base no **catálogo atual da OntoKSD**, usando competências compatíveis com o domínio de **Máquinas de Turing, computabilidade, notação simbólica e validação por simuladores**.



### **C18 — Model real-world problems using formal language concepts**

**Tipo:** Competência atômica

**ActivationRole:** `core`  
**ActivationMode:** `constructive`  
**ActivationConstraint:** `mandatory`

**Particularização na TASK25.03:**  
Codificar leituras de sensores e categorias de veículos em **símbolos, cadeias e linguagens**, definindo a entrada formal do sistema. Essa competência sustenta a abstração inicial do domínio e a representação simbólica do problema computacional. 



### **C17 — Apply operations on formal languages**

**Tipo:** Competência atômica

**ActivationRole:** `core`  
**ActivationMode:** `analytical`  
**ActivationConstraint:** `mandatory`

**Particularização na TASK25.03:**  
Analisar e reorganizar cadeias simbólicas por meio de **varredura, marcação, segmentação e comparação estrutural**, de modo a apoiar a lógica de contagem e decisão implementada pela Máquina de Turing. Nesta tarefa, C17 não representa a execução do algoritmo em si, mas a competência de tratar formalmente a estrutura da entrada simbólica que será processada pela máquina.




### **C07 — Develop problem-solving solutions using Turing Machines**

**Tipo:** Competência atômica

**ActivationRole:** `core`  
**ActivationMode:** `constructive`  
**ActivationConstraint:** `mandatory`

**Particularização na TASK25.03:**  
Projetar e implementar uma **Máquina de Turing funcional** capaz de **contar ocorrências, comparar quantidades e decidir** qual categoria de veículo é predominante. Essa competência responde diretamente à exigência de construção da solução computacional no domínio das Máquinas de Turing.




### **C16 — Interpret Turing Machine concepts to analyze computational system capabilities**

**Tipo:** Competência atômica

**ActivationRole:** `supporting`  
**ActivationMode:** `analytical`  
**ActivationConstraint:** `mandatory`

**Particularização na TASK25.03:**  
Interpretar conceitos de **Máquinas de Turing**, computabilidade e capacidade de processamento para analisar por que esse formalismo é adequado ao problema de controle de tráfego. Essa competência apoia a reflexão conceitual sobre o alcance do modelo, distinguindo a mera construção da máquina de sua justificação teórica.





### **C23 — Interpret and apply algebraic notation for strings and languages**

**Tipo:** Competência transversal

**ActivationRole:** `transversal`  
**ActivationMode:** `analytical`  
**ActivationConstraint:** `mandatory`

**Particularização na TASK25.03:**  
Utilizar notação formal para descrever **entradas, símbolos, fitas, configurações e linguagens** associadas à Máquina de Turing. Essa competência substitui o uso anterior de C13′/C13.01, pois a tarefa requer **notação simbólica geral de cadeias e linguagens**, e não interpretação de regras gramaticais formais.





### **C05.01 — Write mathematically rigorous answers**

**Tipo:** Competência transversal

**ActivationRole:** `transversal`  
**ActivationMode:** `justificatory`  
**ActivationConstraint:** `mandatory`

**Particularização na TASK25.03:**  
Justificar formalmente a **correção, a computabilidade e o comportamento da Máquina de Turing**, usando definições, exemplos, argumentos teóricos e organização explícita entre afirmações, justificativas e conclusões.




### **C10 — Test Turing Machines Using Simulators**

**Tipo:** Competência de apoio

**ActivationRole:** `supporting`  
**ActivationMode:** `artifact-oriented`  
**ActivationConstraint:** `mandatory`

**Particularização na TASK25.03:**  
Utilizar o **JFLAP** para executar e validar empiricamente a **Máquina de Turing construída**, observando diferentes entradas, o comportamento da fita e a decisão final produzida.




### **C09 — Apply Turing Machine Variants**

**Tipo:** Competência atômica

**ActivationRole:** `extension`  
**ActivationMode:** `analytical`  
**ActivationConstraint:** `conditional`

**Particularização na TASK25.03:**  
Analisar, quando pertinente, a necessidade ou a conveniência de recorrer a **variantes ou extensões de Máquinas de Turing** para representar de forma mais clara ou eficiente o processamento requerido. Sua ativação é condicional porque o problema pode ser resolvido com MT padrão, mas o próprio enunciado menciona a avaliação de extensões como objetivo de aprendizagem. 



## Estrutura OntoKSD implícita (TASK25.03) 

```
TASK25.03
├── coreCompetence
│   ├── C18 — Model real-world problems using formal language concepts
│   ├── C17 — Apply operations on formal languages
│   └── C07 — Develop problem-solving solutions using Turing Machines
│
├── transversalCompetence
│   ├── C23 — Interpret and apply algebraic notation for strings and languages
│   └── C05.01 — Write mathematically rigorous answers
│
├── supportingCompetence
│   ├── C16 — Interpret Turing Machine concepts to analyze computational system capabilities
│   └── C10 — Test Turing Machines Using Simulators
│
└── extensionCompetence
    └── C09 — Apply Turing Machine Variants
    
```


### Observações ontológicas
- C18, C17 e C07 formam o núcleo cognitivo da abstração do domínio, do tratamento estrutural das cadeias e da construção da solução em Máquina de Turing.
- C23 e C05.01 atravessam toda a tarefa, garantindo precisão notacional e rigor justificativo.
- C16 fornece suporte conceitual para a análise da adequação do formalismo de Máquina de Turing ao problema.
- C10 fornece suporte empírico por meio da simulação da máquina em JFLAP.
- C09 permanece como competência de extensão condicional, acionada quando a solução discute explicitamente variantes ou extensões de MT.





## 7. Mapeamento entre Objetivos de Aprendizagem (LOs) e Competências — TASK25.03 

O mapeamento a seguir explicita a **rastreabilidade pedagógica** entre os **Objetivos de Aprendizagem** definidos para a **TASK25.03** e as competências mobilizadas segundo a OntoKSD, evidenciando como cada objetivo contribui para o desempenho esperado na tarefa.

| **LO** | **Descrição do Objetivo de Aprendizagem** | **Competências Mobilizadas** |
|---|---|---|
| **LO1** | Abstrair leituras de sensores e categorias de veículos como símbolos e cadeias de entrada | **C18**, **C23** |
| **LO2** | Definir formalmente o problema de contagem e decisão sobre a categoria predominante | **C18**, **C17**, **C05.01** |
| **LO3** | Construir uma Máquina de Turing capaz de processar a entrada e produzir a decisão correta | **C07**, **C18**, **C17** |
| **LO4** | Simular e validar o comportamento da MT em diferentes entradas | **C10**, **C07**, **C05.01** |
| **LO5** | Justificar computabilidade, adequação do modelo e correção da solução | **C16**, **C05.01**, **C07** |
| **LO6** | Comunicar o modelo, as simulações e as justificativas em relatório técnico rigoroso | **C05.01**, **C23** |
| **LO7** | Avaliar a necessidade de usar extensões ou variantes da Máquina de Turing | **C09**, **C16** |







