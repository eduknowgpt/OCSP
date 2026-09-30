
# CSP-Report — TASK25.01 - *A Máquina de Vender Refrigerantes e Salgados*

## 1. Introdução

Este relatório aplica o **Competency Specification Process (CSP)** à **TASK25.01 — Máquina de Vender Refrigerantes e Salgados**, uma atividade cujo objetivo é **modelar, analisar e justificar o comportamento de um sistema discreto** por meio de **Linguagens Formais, Autômatos Finitos e Expressões Regulares**.

A TASK25.01 constitui uma **reengenharia conceitual da Tarefa01**, que preserva o problema original — a modelagem de uma máquina de venda automática —, mas o reorganiza sob um **arcabouço formal mais rigoroso**. Ela não é mera repetição;
é um caso de reuso com reconfiguração de evidências e ativações que ajuda a validar a flexibilidade do CSP e da OntoKSD.

As principais mudanças concentram-se no **aumento da complexidade estrutural do sistema**, decorrente da atualização dos valores monetários e do impacto sobre o espaço de estados do autômato, e na **substituição de elementos processuais do PBL** (como quadros reflexivos e diários) por **artefatos formais de evidência**, em especial o **autômato no JFLAP**, a **expressão regular (ou sua justificativa formal)** e um **relatório técnico rigoroso**.

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

As competências a seguir constituem o perfil de desempenho esperado para a **TASK25.01 — Máquina de Vender Refrigerantes e Salgados**. Cada competência é explicitada em termos de papel de ativação, modo de ativação e condição de ativação, de forma alinhada ao catálogo atual da OntoKSD e às exigências conceituais e evidenciais da tarefa. O conjunto foi ajustado para preservar coerência com o catálogo consolidado, evitando o reuso de competências cujo escopo semântico passou a ser específico de outras tarefas.



### C18 — Model real-world problems using formal language concepts

**ActivationRole:** `core`  
**ActivationMode:** `constructive`  
**ActivationConstraint:** `mandatory`

**Particularização na TASK25.01:**  
Mapear moedas, notas, produtos, saldo, troco e bônus em símbolos, cadeias e linguagens, definindo o modelo formal base da máquina de venda automática. Essa competência sustenta a abstração do domínio e a construção da representação simbólica do sistema.



### C17 — Apply operations on formal languages

**ActivationRole:** `core`  
**ActivationMode:** `analytical`  
**ActivationConstraint:** `mandatory`

**Particularização na TASK25.01:**  
Operar cadeias por concatenação, prefixos e sequências parciais para caracterizar cadeias válidas e inválidas de uso da máquina. Nesta tarefa, C17 é mobilizada no nível necessário para a análise estrutural da linguagem reconhecida, sem tomar propriedades de fechamento como foco principal.



### C23 — Interpret and apply algebraic notation for strings and languages

ActivationRole: transversal
ActivationMode: analytical
ActivationConstraint: mandatory

Particularização na TASK25.01:
Usar ε, concatenação, Σ*, notação de cadeias e notação de linguagens para especificar cadeias, estados, condições de aceitação e descrições formais do comportamento da máquina. Essa competência substitui o uso anterior de C13.01, por tratar especificamente de notação algébrica de strings e linguagens, e não de regras gramaticais formais. O report da tarefa exige explicitamente uma definição simbólica do alfabeto e das cadeias válidas, o que justifica essa ativação transversal.



### C05.01 — Write mathematically rigorous answers

**ActivationRole:** `transversal`  
**ActivationMode:** `justificatory`  
**ActivationConstraint:** `mandatory`

**Particularização na TASK25.01:**  
Justificar a correção do autômato, a validade das cadeias, o papel do não-determinismo e os limites da descrição por expressões regulares, usando definições, exemplos e contraexemplos. A tarefa exige não apenas um relatório técnico, mas também justificativas formais sobre o comportamento do modelo.



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
Usar o JFLAP para validar empiricamente o comportamento do autômato frente a sequências de moedas, notas e seleção de produtos. A competência é condicional porque a simulação constitui evidência importante da correção operacional, mas sua ativação depende da efetiva exploração do simulador como instrumento de validação.



### **C04 — Definir linguagens por meio de expressões regulares**

**ActivationRole:** `extension`  
**ActivationMode:** `analytical`  
**ActivationConstraint:** `conditional`

**Particularização na TASK25.01:**  
Analisar se a linguagem reconhecida pelo autômato pode ser descrita por uma expressão regular, e, quando possível, apresentar um exemplo de ER correspondente a um trecho do modelo; caso contrário, justificar formalmente a impossibilidade ou a limitação dessa descrição. Trata-se de uma competência de extensão, pois a regularidade e sua descrição por ER enriquecem a análise formal da tarefa, mas não estruturam todas as respostas.



## Estrutura OntoKSD implícita (TASK25.01)

A estrutura abaixo explicita, de forma hierárquica e semanticamente alinhada à OntoKSD,  
como a competência de nível de tarefa (**C20**) agrega competências nucleares, transversais  
e de apoio mobilizadas na TASK25.01.

````
TASK25.01
├── coreCompetence
│   ├── C18 — Model real-world problems using formal language concepts
│   └── C17 — Apply operations on formal languages
│
├── transversalCompetence
│   ├── C23 — Interpret and apply algebraic notation for strings and languages
│   └── C05.01 — Write mathematically rigorous answers
│
├── supportingCompetence
│   ├── C02 — Justify the use of Deterministic Finite Automata (DFAs)
│   └── C03 — Test automata using simulators
│
└── extensionCompetence
    └── C04 — Define Regular Expressions for Finite Automata
````


### Observações ontológicas

- C18 e C17 formam o núcleo cognitivo da abstração e da análise estrutural da máquina.
- C23 e C05.01 atravessam toda a tarefa, garantindo precisão notacional e rigor justificativo.
- C02 e C03 fornecem suporte à validação formal e empírica do modelo.
- C04 permanece como extensão condicional voltada à análise de regularidade e descrição por expressões regulares.

Diferentemente da versão anterior, esta organização não reutiliza C20, já que no catálogo atual C20 passou a designar a competência específica da Task25.00 — musical collections. A tarefa continua coerente sem uma competência composta própria, podendo futuramente receber uma competência de nível de tarefa específica caso você queira manter esse padrão para todas as tasks.


## Mapeamento entre Objetivos de Aprendizagem (LOs) e Competências — TASK25.01

| **LO** | **Descrição do Objetivo de Aprendizagem** | **Competências Mobilizadas** |
|------|------------------------------------------|------------------------------|
| **LO1** | Abstrair o domínio da máquina em símbolos formais (produtos, moedas, bônus, ações) | C18, C23 |
| **LO2** | Representar sequências válidas e inválidas como cadeias sobre o alfabeto | C17, C23 |
| **LO3** | Construir um autômato finito que reconheça as sequências válidas | C18, C02, C23 |
| **LO4** | Simular o comportamento do autômato para validação | C0*, C02 |
| **LO5** | Justificar formalmente correção, reconhecimento, limites expressivos e não-determinismo | C05.01, C02, C04 |
| **LO6** | Documentar o raciocínio de forma clara, estruturada e rigorosa | C05.01, C23 |



## 7. Conclusão

O CSP-Report da TASK25.01, ajustado ao catálogo atual da OntoKSD, mantém um conjunto de competências semântica e pedagogicamente coerente para a modelagem formal de uma máquina de venda automática por meio de Linguagens Formais, Autômatos Finitos e Expressões Regulares. O núcleo da tarefa continua sustentado pela abstração do domínio e pela análise estrutural da linguagem (C18, C17), complementado por competências transversais de notação algébrica e rigor justificativo (C23, C05.01), além de competências de apoio voltadas à justificativa do modelo e à simulação (C02, C03) e da extensão condicional por ER (C04).
