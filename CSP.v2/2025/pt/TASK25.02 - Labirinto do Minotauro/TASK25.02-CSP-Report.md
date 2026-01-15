# CSP-Report — TASK25.02 — *Labirinto do Minotauro*

## 1. Introdução

Este relatório aplica o **Competency Specification Process (CSP)** à **TASK25.02 — Labirinto do Minotauro**, uma tarefa cujo objetivo é **modelar formalmente a navegação em um labirinto com retorno ao ponto de origem**, analisando os **limites expressivos de autômatos finitos** e a necessidade de **memória estruturada**.

O problema toma como metáfora o fio de Ariadne, utilizado por Teseu para marcar o caminho de ida e permitir o retorno, e o reinterpreta como um **mecanismo formal de memória**. Em termos de Teoria da Computação, essa exigência corresponde à distinção fundamental entre **autômatos finitos**, que não possuem memória suficiente para registrar percursos arbitrários, e **autômatos com pilha (PDA)**, capazes de armazenar e recuperar símbolos de forma estruturada.

A TASK25.02 exige que os estudantes:

- demonstrem por que **autômatos finitos são insuficientes** para resolver o problema do retorno;
- construam um **autômato de pilha** que reconheça sequências de movimentos de ida e volta no labirinto;
- especifiquem formalmente essas sequências por meio de uma **gramática livre de contexto**;
- e validem os modelos construídos por meio de **simulações no JFLAP**.

No contexto do CSP, a tarefa mobiliza competências relacionadas à **análise de poder expressivo**, **modelagem formal com memória**, **equivalência entre dispositivos reconhecedores e gramáticas**, e **argumentação teórica rigorosa**, integrando conhecimento computacional, habilidade formal e disposições epistêmicas próprias da Teoria da Computação.



## 2. Análise da Entidade Instrucional

### 2.1 Identificação

- **Título:** Labirinto do Minotauro  
- **Tipo:** Caso PBL com ênfase em modelagem formal  
- **Domínio:** Linguagens Formais, Autômatos de Pilha e Gramáticas Livres de Contexto  



### 2.2 Descrição Sintética

A tarefa requer que os estudantes **modelem formalmente um sistema de navegação em um labirinto** no qual um agente deve **alcançar um destino e retornar ao ponto de origem**, utilizando uma **estrutura de memória simbólica** para registrar o percurso realizado.

Os movimentos do agente (por exemplo, esquerda, direita, frente e retorno) devem ser representados como **símbolos de um alfabeto**, e os caminhos percorridos devem ser modelados como **cadeias sobre esse alfabeto**. O desafio central consiste em demonstrar que **autômatos finitos são insuficientes** para reconhecer corretamente as sequências válidas de ida e volta, exigindo a construção de um **autômato de pilha (PDA)** que utilize sua pilha como análogo formal do “fio de Ariadne”.

A tarefa também requer a **especificação de uma gramática livre de contexto (GLC)** equivalente ao PDA construído, evidenciando a relação formal entre **modelos reconhecedores e sistemas geradores**. A correção dos modelos deve ser validada por meio de **simulações no JFLAP** e por **justificativas teóricas** que explicitem propriedades de memória, reconhecimento e equivalência.



## 3. Resultados Esperados

Ao final da tarefa, espera-se que os estudantes produzam:

- um **autômato de pilha funcional** que reconheça corretamente sequências de navegação com ida e retorno;
- uma **gramática livre de contexto equivalente** que gere a mesma linguagem;
- **simulações no JFLAP** que evidenciem o comportamento correto do PDA;
- uma **análise formal** demonstrando a **insuficiência de autômatos finitos** para o problema;
- um **relatório técnico matematicamente rigoroso**, contendo definições, modelos, justificativas e argumentos formais sobre poder expressivo e equivalência de modelos.





## 4. Enumeração de Conhecimentos

A realização adequada da **TASK25.02 — Labirinto do Minotauro** requer a mobilização integrada de conhecimentos disciplinares em **Teoria da Computação** e de conhecimentos profissionais fundamentais, conforme os referenciais do **CS2023** e do **CC2020**. Esses conhecimentos sustentam tanto a **modelagem formal do problema** quanto a **análise de poder expressivo e equivalência de modelos** exigida pela tarefa.


### 4.1 Conhecimentos de Computação (CS2023)

- **Linguagens Formais**
  - alfabetos, cadeias e linguagens;
  - definição de linguagens por propriedades estruturais;
  - distinção entre reconhecimento e geração de linguagens.

- **Autômatos Finitos**
  - limitações de memória dos AF;
  - incapacidade de reconhecer padrões de ida e retorno arbitrários.

- **Autômatos de Pilha (PDA)**
  - pilha como mecanismo de memória estruturada;
  - reconhecimento de linguagens livres de contexto;
  - relação entre operações de empilhar e desempilhar e o controle de percursos.

- **Gramáticas Livres de Contexto (GLC)**
  - definição e uso de regras de produção;
  - geração de linguagens livres de contexto;
  - correspondência entre PDA e GLC.

- **Equivalência entre Modelos**
  - equivalência formal entre **PDA e GLC**;
  - distinção entre classes de linguagens (regulares vs. livres de contexto).

- **Simulação e Validação de Modelos**
  - uso de ferramentas como o **JFLAP** para testar autômatos de pilha e gramáticas;
  - interpretação formal dos resultados de simulação.



### 4.2 Conhecimentos Profissionais Fundamentais (FPK — CC2020)

- **Pensamento Analítico e Crítico**  
  Capacidade de decompor o comportamento do sistema, analisar limites expressivos dos modelos e avaliar a correção das soluções propostas.

- **Comunicação Técnica Escrita**  
  Capacidade de produzir um **relatório claro, estruturado e matematicamente preciso**, expressando definições, modelos, argumentos e conclusões de forma coerente e verificável.



## 5. Objetivos de Aprendizagem

### Objetivo Geral

Capacitar o estudante a **modelar, analisar e justificar formalmente sistemas de navegação com retorno**, utilizando **autômatos de pilha e gramáticas livres de contexto** para representar e reconhecer sequências de movimentos que requerem **memória estruturada**, distinguindo claramente os **limites dos autômatos finitos**.



### Objetivos Específicos

Ao concluir a tarefa, o estudante deverá ser capaz de:

- **LO1 — Abstrair o domínio do labirinto**  
  Representar posições, movimentos e percursos do labirinto por meio de **símbolos de um alfabeto formal** e **cadeias**.

- **LO2 — Caracterizar formalmente os percursos válidos**  
  Definir quais sequências de movimentos correspondem a trajetos corretos de **ida e retorno** no labirinto, distinguindo-as de cadeias inválidas.

- **LO3 — Analisar os limites dos autômatos finitos**  
  Justificar formalmente por que **AF não são suficientes** para reconhecer linguagens de navegação com retorno arbitrário.

- **LO4 — Construir um autômato de pilha (PDA)**  
  Projetar um **PDA funcional** que reconheça corretamente as sequências válidas de navegação, utilizando a **pilha como memória do percurso**.

- **LO5 — Especificar uma gramática livre de contexto (GLC)**  
  Construir uma **GLC equivalente ao PDA**, capaz de gerar a mesma linguagem de percursos.

- **LO6 — Analisar a equivalência entre modelos**  
  Explicar formalmente a correspondência entre o **PDA e a GLC**, em termos de reconhecimento e geração da linguagem.

- **LO7 — Validar modelos por simulação**  
  Utilizar o **JFLAP** para testar e confirmar o comportamento correto do PDA e da gramática.

- **LO8 — Justificar formalmente correção e limites**  
  Produzir argumentos rigorosos sobre **correção, poder expressivo e limitações dos modelos** utilizados.

- **LO9 — Comunicar resultados tecnicamente**  
  Elaborar um **relatório matematicamente rigoroso**, distinguindo definições, exemplos, simulações e provas formais.







## 6. Competências da TASK25.02 (com Ativações OntoKSD)

As competências a seguir constituem o **perfil de desempenho esperado** para a **TASK25.02 — Labirinto do Minotauro**. Cada competência é especificada não apenas por seu conteúdo, mas também por **como, por que e em que grau** ela é mobilizada na tarefa, em consonância com a OntoKSD.


### **C20 — Modelar e analisar sistemas do mundo real como linguagens formais**  
**Tipo:** Competência composta (nível de tarefa)

**ActivationRole:** `core`  
**ActivationMode:** `integrative`  
**ActivationConstraint:** `mandatory`

**Particularização na TASK25.02:**  
Integra a abstração do domínio de navegação, a construção de modelos formais com memória, a análise do poder expressivo e a justificação teórica da solução, constituindo o **resultado cognitivo global da tarefa**.



### **C18 — Modelar problemas do mundo real como linguagens formais**

**Tipo:** Competência atômica

**ActivationRole:** `core`  
**ActivationMode:** `constructive`  
**ActivationConstraint:** `mandatory`

**Particularização na TASK25.02:**  
Mapear posições, movimentos e percursos em **símbolos, cadeias e linguagens**, estabelecendo a representação formal do problema de navegação.



### **C19 — Aplicar homomorfismos e codificações formais**

**Tipo:** Competência atômica

**ActivationRole:** `core`  
**ActivationMode:** `analytical`  
**ActivationConstraint:** `mandatory`

**Particularização na TASK25.02:**  
Codificar movimentos físicos e percursos espaciais como **sequências simbólicas**, analisando como as propriedades estruturais são preservadas sob essa representação.



### **C17 — Aplicar operações sobre linguagens formais**

**Tipo:** Competência atômica

**ActivationRole:** `core`  
**ActivationMode:** `analytical`  
**ActivationConstraint:** `mandatory`

**Particularização na TASK25.02:**  
Analisar sequências de navegação por meio de **concatenação, prefixos e estrutura recursiva**, caracterizando cadeias válidas e inválidas de ida e retorno.



### **C02 — Justificar o uso de Autômatos Finitos Determinísticos**

**Tipo:** Competência atômica

**ActivationRole:** `supporting`  
**ActivationMode:** `justificatory`  
**ActivationConstraint:** `mandatory`

**Particularização na TASK25.02:**  
Demonstrar formalmente a **insuficiência dos autômatos finitos** para o problema e justificar a **necessidade de um autômato de pilha**, explicando o papel da pilha como memória do percurso.




### **C14 — Diferenciar classes de gramáticas formais**

**Tipo:** Competência atômica

**ActivationRole:** `supporting`  
**ActivationMode:** `analytical`  
**ActivationConstraint:** `mandatory`

**Particularização na TASK25.02:**  
Relacionar **linguagens regulares e livres de contexto**, justificando por que o problema exige uma **gramática livre de contexto**.



### **C04 — Definir linguagens por meio de expressões e gramáticas formais**

**Tipo:** Competência atômica

**ActivationRole:** `extension`  
**ActivationMode:** `constructive`  
**ActivationConstraint:** `mandatory`

**Particularização na TASK25.02:**  
Construir uma **gramática livre de contexto** equivalente ao PDA, formalizando a geração da linguagem de percursos.



### **C13′ — Interpretar e aplicar notação algébrica de strings e linguagens**

**Tipo:** Competência transversal

**ActivationRole:** `transversal`  
**ActivationMode:** `analytical`  
**ActivationConstraint:** `mandatory`

**Particularização na TASK25.02:**  
Utilizar ε, concatenação, Σ\*, não terminais e regras de produção para **especificar cadeias, estados e linguagens**.



### **C05′ — Produzir respostas matematicamente rigorosas**

**Tipo:** Competência transversal

**ActivationRole:** `transversal`  
**ActivationMode:** `justificatory`  
**ActivationConstraint:** `mandatory`

**Particularização na TASK25.02:**  
Justificar a **correção do PDA**, a **equivalência com a GLC** e os **limites dos AF**, usando definições, exemplos e contraexemplos.


### **C03 — Testar autômatos por simulação**

**Tipo:** Competência de apoio

**ActivationRole:** `supporting`  
**ActivationMode:** `artifact-oriented`  
**ActivationConstraint:** `mandatory`

**Particularização na TASK25.02:**  
Utilizar o **JFLAP** para validar empiricamente o comportamento do **PDA** e da **GLC** frente a cadeias de teste.




## Mapeamento entre Objetivos de Aprendizagem (LOs) e Competências — TASK25.01

A tabela a seguir explicita a **rastreabilidade pedagógica e ontológica** entre os **Objetivos de Aprendizagem (LOs)** definidos para a TASK25.01 e as **competências da OntoKSD** mobilizadas para seu atendimento. Cada linha mostra **como um objetivo específico é operacionalizado por competências atômicas e compostas**, garantindo alinhamento entre o que se espera que o estudante realize e as capacidades formalmente representadas no modelo ontológico.

| **LO** | **Descrição do Objetivo de Aprendizagem** | **Competências Mobilizadas** |
|------|------------------------------------------|------------------------------|
| **LO1** | Abstrair o domínio da máquina em símbolos formais (produtos, moedas, bônus e ações) | **C18**, C13′ |
| **LO2** | Representar sequências válidas e inválidas como cadeias sobre o alfabeto definido | **C17**, C13′ |
| **LO3** | Construir um autômato finito que reconheça as sequências válidas | **C18**, **C02**, C13′ |
| **LO4** | Simular o comportamento do autômato para validação | **C03**, C02 |
| **LO5** | Justificar formalmente correção, reconhecimento, limites expressivos e não-determinismo | **C05′**, **C02**, **C04** |
| **LO6** | Documentar o raciocínio de forma clara, estruturada e rigorosa | **C05′**, C13′ |
| — | Integrar modelagem, análise, validação e justificação no problema completo | **C20** |

### Leitura ontológica do mapeamento

- **C18** fornece a base de **abstração formal do domínio**, necessária para LO1 e LO3.  
- **C17** operacionaliza a análise de **cadeias e sequências**, sustentando LO2.  
- **C02** conecta o modelo simbólico ao **fundamento teórico dos autômatos**, sendo crítico para LO3–LO5.  
- **C03** fornece a **evidência empírica** por simulação (LO4).  
- **C04** é mobilizada de forma **condicional**, quando a equivalência com expressões regulares precisa ser analisada (LO5).  
- **C13′** e **C05′** garantem **precisão notacional e rigor epistêmico** ao longo de todos os LOs.  
- **C20** sintetiza o desempenho global da tarefa, integrando todas as competências mobilizadas.





## 7. Conclusão

O **CSP-Report da TASK25.01** estabelece uma **estrutura de competências clara, rastreável e ontologicamente consistente** para a modelagem e análise de uma máquina de venda automática como um sistema reconhecedor de linguagens formais. Ao articular **Objetivos de Aprendizagem específicos** com **competências genéricas da OntoKSD**, o modelo assegura que cada evidência exigida da tarefa — autômato, simulações, expressões formais e justificativas — corresponda a **capacidades cognitivas e técnicas bem definidas**.

A adoção de uma **competência composta de nível de tarefa (C20)** permite integrar, de forma coerente, a **abstração simbólica do domínio (C18)**, a **análise de cadeias (C17)**, a **justificação do modelo reconhecedor (C02)**, a **validação empírica (C03)** e o **rigor notacional e argumentativo (C13′, C05′)**, com a extensão condicional da **especificação por expressões regulares (C04)**. Essa organização evita tanto a **fragmentação excessiva** quanto a **diluição conceitual**, preservando a capacidade de **reuso e comparação entre tarefas**.

Como resultado, a TASK25.01 é posicionada não apenas como um exercício de construção de autômatos, mas como uma **atividade de educação por competências**, na qual o desempenho do estudante pode ser avaliado de forma **formal, transparente e semanticamente fundamentada**. Essa estrutura fortalece a rastreabilidade pedagógica, a validade das evidências produzidas e o alinhamento com os referenciais do **CS2023**, do **CC2020** e da **OntoKSD**.


