# CSP-Report — TASK25.03 — *Controle de Tráfego*

## 1. Introdução

Este relatório aplica o **Competency Specification Process (CSP)** à **TASK25.03 — Controle de Tráfego**, uma tarefa cujo objetivo é **modelar, analisar e justificar computacionalmente um sistema de monitoramento de veículos pesados**, utilizando **Máquinas de Turing e seus modelos estendidos** para processar dados provenientes de sensores em uma rodovia real.

A tarefa descreve um cenário no qual sensores instalados na estrada de Aratu, em Salvador, categorizam veículos noturnos em **leves, pesados e muito pesados**, com base em seu peso, e demandam um sistema capaz de **contabilizar a quantidade de veículos por categoria** e **identificar a categoria predominante** da noite anterior, de modo a subsidiar políticas de preservação do asfaltamento.

A **TASK25.03** constitui uma **reformulação curricularmente atualizada da Tarefa02**, preservando o núcleo do problema — a modelagem computacional de um sistema de controle de tráfego baseado em sensores — mas alterando de forma significativa sua **organização pedagógica e epistemológica**. Enquanto a versão original estava fortemente ancorada em práticas de **PBL processual**, exigindo quadros de fatos, ideias, ações e diários de bordo como parte da avaliação, a TASK25.03 desloca o foco para **evidências formais e tecnicamente verificáveis**, consistindo essencialmente em **artefatos computacionais (máquinas em JFLAP)** e em um **relatório técnico rigoroso**. Além disso, a versão atualizada enfatiza explicitamente a **fundamentação teórica da solução**, posicionando o uso de Máquinas de Turing e da **tese de Church–Turing** não apenas como instrumentos de implementação, mas como **meios de análise e validação conceitual** do sistema proposto. Essa mudança transforma a tarefa de uma atividade predominantemente processual e narrativa em uma **atividade orientada a competências formais**, permitindo que o desempenho do estudante seja avaliado pela **qualidade do modelo computacional e de sua justificação teórica**, e não pela documentação de seu percurso colaborativo.




## 2. Análise da Entidade Instrucional

### 2.1 Identificação

- **Título:** Controle de Tráfego  
- **Tipo:** Caso PBL com ênfase em modelagem formal e análise computacional  
- **Domínio:** Teoria da Computação — Máquinas de Turing e Computabilidade  



### 2.2 Descrição Sintética

A tarefa requer que os estudantes **modelem formalmente um sistema de monitoramento de tráfego rodoviário**, no qual dados provenientes de sensores classificam veículos em diferentes categorias de peso ao longo de uma noite. Essas leituras devem ser representadas como **cadeias sobre um alfabeto simbólico**, e o comportamento do sistema deve ser descrito por uma **Máquina de Turing (MT)** capaz de **contabilizar ocorrências, comparar quantidades e decidir qual categoria de veículo foi predominante**.

Os estudantes devem projetar uma MT que **leia a fita de entrada**, **processa os símbolos correspondentes aos veículos**, **mantenha contadores ou marcas auxiliares** e **produza uma decisão final** sobre o tipo de veículo que mais impactou a rodovia. A tarefa exige que esse modelo seja **formalmente especificado, executável em simulador (JFLAP)** e **teoricamente justificado** à luz da **tese de Church–Turing**, explicitando por que o problema é computável e adequadamente modelado por uma MT.

Diferentemente de versões anteriores, a TASK25.03 concentra-se na **qualidade formal do modelo computacional e de sua justificativa**, e não na documentação do processo colaborativo, alinhando a atividade ao paradigma de **avaliação por competências** em Teoria da Computação.




## 3. Resultados Esperados

Ao final da tarefa, espera-se que os estudantes produzam **artefatos formais e justificativas teóricas** que evidenciem sua capacidade de **modelar e analisar um sistema computacional baseado em dados de sensores**. Em particular, os estudantes deverão apresentar **uma Máquina de Turing funcional**, implementada e testada em simulador, capaz de **processar a sequência de veículos registrada** e **decidir corretamente qual categoria de peso foi predominante**.

Além do modelo computacional, espera-se a entrega de **simulações documentadas** que demonstrem o comportamento da máquina para diferentes entradas, bem como de um **relatório técnico matematicamente rigoroso** contendo a **especificação formal da máquina**, a **interpretação de seus estados e transições** e a **justificação teórica de sua correção e computabilidade**, fundamentada na **tese de Church–Turing** e nos princípios da Teoria da Computação.





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

As competências a seguir constituem o **perfil de desempenho esperado** para a **TASK25.03 — Controle de Tráfego**. Todas as competências utilizadas pertencem ao **Catálogo da OntoKSD**; aqui elas são apenas **ativadas e particularizadas** para o contexto da tarefa.



### **C20 — Modelar e analisar sistemas do mundo real como linguagens formais**  
**Tipo:** Competência composta (nível de tarefa)

**ActivationRole:** `core`  
**ActivationMode:** `integrative`  
**ActivationConstraint:** `mandatory`

**Particularização na TASK25.03:**  
Integra a abstração dos dados de tráfego, a construção da Máquina de Turing, a análise do processo de contagem e decisão e a justificação formal da computabilidade, constituindo o **resultado cognitivo global da tarefa**.



### **C18 — Modelar problemas do mundo real como linguagens formais**

**Tipo:** Competência atômica

**ActivationRole:** `core`  
**ActivationMode:** `constructive`  
**ActivationConstraint:** `mandatory`

**Particularização na TASK25.03:**  
Codificar leituras de sensores e categorias de veículos em **símbolos, cadeias e linguagens**, definindo a entrada formal do sistema.



### **C17 — Aplicar operações sobre linguagens formais**

**Tipo:** Competência atômica

**ActivationRole:** `core`  
**ActivationMode:** `analytical`  
**ActivationConstraint:** `mandatory`

**Particularização na TASK25.03:**  
Manipular cadeias simbólicas por meio de **varredura, marcação e decomposição**, preparando-as para processamento pela Máquina de Turing.



### **C16 — Desenvolver soluções utilizando Máquinas de Turing**

**Tipo:** Competência atômica

**ActivationRole:** `core`  
**ActivationMode:** `constructive`  
**ActivationConstraint:** `mandatory`

**Particularização na TASK25.03:**  
Projetar e implementar uma **Máquina de Turing funcional** capaz de **contar ocorrências e decidir** qual categoria de veículo é predominante.



### **C02 — Justificar o uso de modelos formais de computação**

**Tipo:** Competência atômica

**ActivationRole:** `supporting`  
**ActivationMode:** `justificatory`  
**ActivationConstraint:** `mandatory`

**Particularização na TASK25.03:**  
Justificar que a Máquina de Turing é o **modelo adequado** para resolver o problema, com base na **tese de Church–Turing** e nas características do processamento exigido.



### **C13′ — Interpretar e aplicar notação algébrica de strings e linguagens**

**Tipo:** Competência transversal

**ActivationRole:** `transversal`  
**ActivationMode:** `analytical`  
**ActivationConstraint:** `mandatory`

**Particularização na TASK25.03:**  
Utilizar notação formal para descrever **entradas, símbolos, configurações e linguagens** associadas à Máquina de Turing.



### **C05′ — Produzir respostas matematicamente rigorosas**

**Tipo:** Competência transversal

**ActivationRole:** `transversal`  
**ActivationMode:** `justificatory`  
**ActivationConstraint:** `mandatory`

**Particularização na TASK25.03:**  
Justificar formalmente a **correção, a computabilidade e o comportamento da Máquina de Turing**, usando definições, exemplos e argumentos teóricos.



### **C03 — Testar modelos computacionais por simulação**

**Tipo:** Competência de apoio

**ActivationRole:** `supporting`  
**ActivationMode:** `artifact-oriented`  
**ActivationConstraint:** `mandatory`

**Particularização na TASK25.03:**  
Utilizar o **JFLAP** para executar e validar empiricamente a **Máquina de Turing construída**.

 







## Mapeamento entre Objetivos de Aprendizagem (LOs) e Competências — TASK25.01

O mapeamento a seguir explicita a **rastreabilidade pedagógica** entre os Objetivos de Aprendizagem definidos para a TASK25.01 e as competências mobilizadas segundo a OntoKSD, evidenciando como cada LO contribui para o desempenho esperado na tarefa.

| **LO** | **Descrição do Objetivo de Aprendizagem** | **Competências Mobilizadas** |
|------|------------------------------------------|------------------------------|
| **LO1** | Abstrair o domínio do problema, associando produtos, moedas, bônus e ações a símbolos de um alfabeto formal | **C18**, C13′ |
| **LO2** | Representar sequências válidas e inválidas de uso da máquina como cadeias sobre o alfabeto definido | **C17**, C13′ |
| **LO3** | Construir um autômato finito que reconheça exatamente as sequências válidas do sistema | **C18**, **C20**, C02 |
| **LO4** | Simular o comportamento do autômato para validar seu funcionamento em diferentes cenários | **C03**, C20 |
| **LO5** | Justificar formalmente o reconhecimento, a correção e os limites expressivos do modelo | **C05′**, C02, C20 |
| **LO6** | Documentar o raciocínio de forma clara, estruturada e matematicamente rigorosa | **C05′**, C20 |

Esse mapeamento confirma que os LOs cobrem tanto a **construção do modelo formal** quanto sua **validação empírica** e **justificação teórica**, assegurando coerência entre objetivos, competências e evidências avaliáveis.



## 7. Conclusão

A TASK25.01 consolida uma **reengenharia conceitual e curricular** da Tarefa01, reposicionando-a como uma atividade plenamente alinhada à **educação baseada em competências**. A especificação resultante evidencia uma competência composta de nível de tarefa (**C20**), sustentada por competências nucleares de modelagem formal, operações simbólicas e justificação matemática, além de competências de apoio relacionadas à escolha do modelo computacional e à validação por simulação.

O conjunto de competências mobilizado é **adequado, completo e semanticamente controlado**, evitando inflacionar o núcleo conceitual da tarefa e preservando a coerência com a **OntoKSD**, o **CS2023** e o **CC2020**. O mapeamento explícito entre LOs e competências assegura rastreabilidade instrucional, clareza avaliativa e consistência epistemológica, justificando plenamente a elaboração de um CSP-Report específico para a TASK25.01.


