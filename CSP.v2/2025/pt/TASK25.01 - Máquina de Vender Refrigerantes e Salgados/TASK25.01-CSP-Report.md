
# CSP-Report — TASK25.01 - *A Máquina de Vender Refrigerantes e Salgados*

## 1. Introdução

Este relatório aplica o **Competency Specification Process (CSP)** à **TASK25.01 — Máquina de Vender Refrigerantes e Salgados**, uma atividade cujo objetivo é **modelar, analisar e justificar o comportamento de um sistema discreto** por meio de **Linguagens Formais, Autômatos Finitos e Expressões Regulares**.

A TASK25.01 constitui uma **reengenharia conceitual da Tarefa01**, que preserva o problema original — a modelagem de uma máquina de venda automática —, mas o reorganiza sob um **arcabouço formal mais rigoroso**. As principais mudanças concentram-se no **aumento da complexidade estrutural do sistema**, decorrente da atualização dos valores monetários e do impacto sobre o espaço de estados do autômato, e na **substituição de elementos processuais do PBL** (como quadros reflexivos e diários) por **artefatos formais de evidência**, em especial o **autômato no JFLAP**, a **expressão regular (ou sua justificativa formal)** e um **relatório técnico rigoroso**.

Além disso, a TASK25.01 reforça explicitamente o **vínculo teórico entre autômatos e expressões regulares**, exigindo o método de construção ou a justificativa de impossibilidade, e integra o **bônus aleatório** como um elemento estrutural do modelo, conectando-o à discussão sobre **não-determinismo**. Essas mudanças, aliadas à atualização curricular e institucional, transformam a Tarefa01 em uma atividade **mais formal, mais exigente e plenamente compatível com a avaliação por competências**.





## 2. Análise da Entidade Instrucional

### 2.1 Identificação

- **Título:** Máquina de Vender Refrigerantes e Salgados  
- **Tipo:** Caso problema-baseado (PBL) com ênfase em artefatos formais  
- **Domínio:** Linguagens Formais, Autômatos Finitos e Expressões Regulares  

### 2.2 Descrição Sintética

A tarefa requer que os estudantes **abstraiam e modelem formalmente** o funcionamento de uma máquina de venda automática que:

- aceita um conjunto finito e previamente definido de **moedas e notas**;  
- disponibiliza **produtos com preços fixos**;  
- mantém e atualiza um **saldo acumulado**, calculando **troco** quando necessário;  
- pode conceder um **bônus aleatório**, introduzindo bifurcações no comportamento do sistema.

Esse comportamento deve ser representado por um **autômato finito** capaz de reconhecer exatamente as **sequências válidas de inserção de dinheiro e seleção de produtos**, distinguindo-as de sequências inválidas. Sempre que possível, a linguagem reconhecida pelo autômato deve ser também descrita por uma **expressão regular**, ou, alternativamente, deve ser fornecida uma **justificativa formal** para a impossibilidade dessa descrição.

A tarefa exige, portanto, não apenas a construção de um artefato operacional (o autômato), mas a **análise teórica do modelo**, incluindo a validação de seu comportamento, a avaliação de suas propriedades formais e a **justificação matemática** das decisões de modelagem, com o apoio de **simuladores** para observação e verificação dos resultados.




## 3. Resultados Esperados

Ao final da tarefa, espera-se que os estudantes produzam um **conjunto coerente de evidências formais** que demonstre a compreensão e a aplicação dos conceitos de Linguagens Formais e Autômatos Finitos no contexto do problema proposto. Em particular, os aprendizes devem apresentar:

- um **autômato finito funcional**, que modele corretamente o comportamento da máquina de venda e reconheça as sequências válidas de inserção de dinheiro e seleção de produtos;  
- uma **definição simbólica explícita** do alfabeto de entrada e das **cadeias válidas**, incluindo as condições sob as quais um produto é liberado, há devolução de troco ou ocorre a concessão de bônus;  
- **simulações no JFLAP (ou ferramenta equivalente)** que confirmem empiricamente o comportamento do autômato para diferentes sequências de entrada;  
- uma **análise formal** sobre a linguagem reconhecida, incluindo sua **regularidade** e, quando aplicável, sua **descrição por expressões regulares** ou a justificativa de sua impossibilidade;  
- um **relatório técnico matematicamente rigoroso**, no qual definições, exemplos, justificativas e conclusões sejam apresentados de forma clara, precisa e logicamente estruturada.




## 4. Enumeração de Conhecimentos

A realização adequada da TASK25.01 requer a mobilização integrada de conhecimentos disciplinares em Teoria da Computação e de conhecimentos profissionais fundamentais, conforme os referenciais do **CS2023** e do **CC2020**.

### 4.1 Conhecimentos de Computação (CS2023)

- **Language Theory**  
  - definição de **alfabetos, cadeias e linguagens**;  
  - distinção entre **cadeias válidas e inválidas** em um sistema formal.

- **Formal Languages**  
  - **concatenação** e formação de sequências admissíveis;  
  - noção de **prefixos, sufixos e cadeias parciais**;  
  - caracterização da **linguagem reconhecida** por um modelo formal.

- **Finite Automata**  
  - **autômatos finitos determinísticos** como modelos de sistemas discretos;  
  - **estados, transições e estados de aceitação**;  
  - **reconhecimento de linguagens** por meio de autômatos.

- **Regular Expressions**  
  - **representação algébrica** de linguagens regulares;  
  - **equivalência teórica** entre autômatos finitos e expressões regulares;  
  - limites e possibilidades da descrição de uma linguagem por ER.



### 4.2 Conhecimentos Profissionais Fundamentais (FPK — CC2020)

- **Pensamento analítico e crítico**  
  Capacidade de decompor o comportamento do sistema, avaliar a correção do modelo e justificar formalmente as decisões de projeto.

- **Comunicação técnica escrita**  
  Capacidade de produzir um **relatório claro, estruturado e matematicamente preciso**, expressando definições, argumentos e conclusões de forma coerente.



## 5. Objetivos de Aprendizagem

### Objetivo Geral

Capacitar o estudante a **modelar, analisar e validar o comportamento de uma máquina de venda automática como uma linguagem formal reconhecida por um autômato finito**, articulando **modelagem simbólica, simulação e argumentação matemática rigorosa** para justificar propriedades, limites e correção do modelo.

### Objetivos Específicos

Ao concluir a tarefa, o estudante deverá ser capaz de:

- **LO1 — Abstração simbólica do domínio**  
  Abstrair os elementos relevantes do problema (produtos, moedas, troco, bônus e ações da máquina) e **associá-los a símbolos de um alfabeto formal**, explicitando hipóteses e convenções de modelagem.

- **LO2 — Representação formal de sequências**  
  Representar **sequências válidas e inválidas** de uso da máquina como **cadeias sobre o alfabeto definido**, caracterizando formalmente quando uma cadeia corresponde a uma operação aceitável do sistema.

- **LO3 — Construção do modelo reconhecedor**  
  **Construir um autômato finito** (determinístico ou não determinístico, quando apropriado) que **reconheça exatamente** as cadeias válidas definidas pelo modelo, refletindo corretamente o saldo, o troco e o bônus.

- **LO4 — Validação por simulação**  
  **Simular o comportamento do autômato** em uma ferramenta apropriada (por exemplo, JFLAP), analisando diferentes sequências de entrada para **verificar a correção e a completude** do modelo.

- **LO5 — Análise formal e limites expressivos**  
  **Justificar formalmente** o reconhecimento e a validade das cadeias, bem como os **limites expressivos do modelo**, incluindo:
  - a **possibilidade ou impossibilidade de descrevê-lo por expressões regulares**;  
  - o **papel do não-determinismo** introduzido por mecanismos como o bônus aleatório.

- **LO6 — Comunicação técnica rigorosa**  
  **Documentar o raciocínio, o modelo e as justificativas** em um **relatório técnico claro, estruturado e matematicamente rigoroso**, distinguindo definições, exemplos, simulações e argumentos formais.





## 6. Competências da TASK25.01 (com Ativações OntoKSD)

As competências a seguir constituem o **perfil de desempenho esperado** para a TASK25.01. Cada competência é especificada não apenas por seu conteúdo, mas também por **como, por que e em que grau** ela é mobilizada na tarefa.


### **C20 — Modelar e analisar sistemas do mundo real como linguagens formais**
**Tipo:** Competência composta (nível de tarefa)

**ActivationRole:** `core`  
**ActivationMode:** `integrative`  
**ActivationConstraint:** `mandatory`

**Particularização na TASK25.01:**  
Integra a abstração do domínio da máquina de venda, a construção do autômato, a análise da linguagem reconhecida e a produção de justificativas formais, constituindo o **resultado cognitivo global da tarefa**.


### **C18 — Modelar problemas do mundo real como linguagens formais**

**ActivationRole:** `core`  
**ActivationMode:** `constructive`  
**ActivationConstraint:** `mandatory`

**Particularização na TASK25.01:**  
Mapear moedas, produtos, saldo, troco e bônus em **símbolos, cadeias e linguagens**, definindo o **modelo formal base** do sistema.



### **C17 — Aplicar operações sobre linguagens formais**

**ActivationRole:** `core`  
**ActivationMode:** `analytical`  
**ActivationConstraint:** `mandatory`

**Particularização na TASK25.01:**  
Operar cadeias por **concatenação, prefixos e sequências parciais** para caracterizar **cadeias válidas e inválidas** de uso da máquina. Não envolve propriedades de fechamento ou álgebra de classes.



### **C13′ — Interpretar e aplicar notação algébrica de strings e linguagens**

**ActivationRole:** `transversal`  
**ActivationMode:** `analytical`  
**ActivationConstraint:** `mandatory`

**Particularização na TASK25.01:**  
Usar ε, concatenação, Σ\* e notação de linguagens para **especificar cadeias, estados e condições de aceitação**.



### **C05′ — Produzir respostas matematicamente rigorosas**

**ActivationRole:** `transversal`  
**ActivationMode:** `justificatory`  
**ActivationConstraint:** `mandatory`

**Particularização na TASK25.01:**  
Justificar **correção do autômato, validade das cadeias, não-determinismo e limites de expressões regulares** usando definições, exemplos e contraexemplos.



### **C02 — Justify the use of Deterministic Finite Automata (DFAs)**

**ActivationRole:** `supporting`  
**ActivationMode:** `justificatory`  
**ActivationConstraint:** `mandatory`

**Particularização na TASK25.01:**  
Justificar formalmente que o comportamento da máquina de venda automática pode ser representado por um **autômato finito** — seja diretamente como **DFA** ou, quando apropriado, por meio de **NFA seguido de conversão** — explicando de forma explícita **como o espaço de estados é estruturado** para representar **saldos monetários, troco e o bônus aleatório**. Essa competência inclui a **análise do papel do não-determinismo** introduzido pelo bônus e a argumentação de que, apesar disso, o sistema permanece **finito, reconhecível e formalmente correto** sob o modelo de autômatos finitos.



### **C03 — Test automata using simulators**

**ActivationRole:** `supporting`  
**ActivationMode:** `artifact-oriented`  
**ActivationConstraint:** `conditional`

**Particularização na TASK25.01:**  
Usar o **JFLAP** para validar empiricamente o comportamento do autômato frente a **sequências reais de moedas e produtos**.



### **C04 — Definir linguagens por meio de expressões regulares**

**ActivationRole:** `extension`  
**ActivationMode:** `analytical`  
**ActivationConstraint:** `conditional`

**Particularização na TASK25.01:**  
Tentar obter uma **ER equivalente ao autômato** ou **justificar formalmente** por que isso não é possível.



## Estrutura OntoKSD implícita (TASK25.01)

A estrutura abaixo explicita, de forma hierárquica e semanticamente alinhada à OntoKSD,  
como a competência de nível de tarefa (**C20**) agrega competências nucleares, transversais  
e de apoio mobilizadas na TASK25.01.

````
TASK25.01
└── targetsCompetence
└── C20 — Modelar e analisar sistemas do mundo real como linguagens formais
│
├── coreCompetence
│  ├── C18 — Modelar problemas do mundo real como linguagens formais
│  └── C17 — Aplicar operações sobre linguagens formais
│
├── transversalCompetence
│  ├── C13′ — Interpretar e aplicar notação algébrica de strings e linguagens
│  └── C05′ — Produzir respostas matematicamente rigorosas
│
├── supportingCompetence
│  ├── C02 — Justificar o uso de Autômatos Finitos (DFA/NFA)
│  └── C03 — Testar autômatos por meio de simuladores
│
└── extensionCompetence
└── C04 — Definir linguagens por meio de expressões regulares
````


**Observações ontológicas**

- **C20** atua como **competência composta de nível de tarefa**, integrando todas as demais.
- **C18** e **C17** constituem o **núcleo cognitivo construtivo** da modelagem formal.
- **C13′** e **C05′** atravessam toda a atividade, garantindo **precisão simbólica e rigor epistêmico**.
- **C02** e **C03** fornecem **suporte formal e empírico** à validade do modelo.
- **C04** aparece como **extensão condicional**, acionada quando a regularidade da linguagem é analisada.

Essa estrutura permite rastrear, de forma explícita, **como cada competência contribui para o desempenho global** esperado na TASK25.01.


## Mapeamento entre Objetivos de Aprendizagem (LOs) e Competências — TASK25.01

| **LO** | **Descrição do Objetivo de Aprendizagem** | **Competências Mobilizadas** |
|------|------------------------------------------|------------------------------|
| **LO1** | Abstrair o domínio da máquina em símbolos formais (produtos, moedas, bônus, ações) | **C18**, C13′ |
| **LO2** | Representar sequências válidas e inválidas como cadeias sobre o alfabeto | **C17**, C13′ |
| **LO3** | Construir um autômato finito que reconheça as sequências válidas | **C18**, **C02**, C13′ |
| **LO4** | Simular o comportamento do autômato para validação | **C03**, C02 |
| **LO5** | Justificar formalmente correção, reconhecimento, limites expressivos e não-determinismo | **C05′**, **C02**, **C04** |
| **LO6** | Documentar o raciocínio de forma clara, estruturada e rigorosa | **C05′**, C13′ |
|    —    | Integrar modelagem, análise, validação e justificação no problema completo | **C20** |



## 7. Conclusão

O **CSP-Report da TASK25.01** consolida um **reuso controlado, explícito e semanticamente fundamentado** das competências originalmente mobilizadas na Tarefa01, incorporando **C02 (Justificação de Autômatos Finitos)** e **C03 (Simulação em JFLAP)** como **competências de apoio**, sem comprometer nem inflar o **núcleo conceitual** da atividade.

A tarefa é estruturada em torno de uma **competência composta de nível de tarefa (C20)**, que integra de forma coerente a **abstração do domínio**, a **construção do modelo formal**, a **análise das cadeias reconhecidas** e a **justificação matemática de sua correção e limites**. Essa agregação é sustentada por competências nucleares (C18, C17), transversais (C13′, C05′) e de apoio (C02, C03), com a extensão condicional de **C04** quando a análise de regularidade é pertinente.

Como resultado, a TASK25.01 alcança um **alto grau de rastreabilidade, precisão ontológica e alinhamento curricular** com o **CS2023** e com a **OntoKSD**, permitindo que o desempenho do estudante seja avaliado não apenas pelo artefato produzido, mas pelo **conjunto integrado de competências efetivamente mobilizadas** durante a resolução do problema.
