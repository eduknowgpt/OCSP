# CSP-Report — TASK25.02 — *Labirinto do Minotauro*

## 1. Introdução

Este relatório aplica o **Competency Specification Process (CSP)** à **TASK25.02 — Labirinto do Minotauro**, uma tarefa cujo objetivo é **modelar formalmente a navegação em um labirinto com retorno ao ponto de origem**, analisando os **limites expressivos de autômatos finitos** e a necessidade de **memória estruturada**. 

O problema toma como metáfora o fio de Ariadne, utilizado por Teseu para marcar o caminho de ida e permitir o retorno, e o reinterpreta como um **mecanismo formal de memória**. Em termos de Teoria da Computação, essa exigência corresponde à distinção entre **autômatos finitos**, que não possuem memória suficiente para registrar percursos arbitrários, e **autômatos com pilha (PDA)**, capazes de armazenar e recuperar símbolos de forma estruturada.  

A TASK25.02 exige que os estudantes:

* demonstrem por que **autômatos finitos são insuficientes** para resolver o problema do retorno;
* construam um **autômato de pilha** que reconheça sequências de movimentos de ida e volta no labirinto;
* especifiquem formalmente essas sequências por meio de uma **gramática livre de contexto**;
* validem os modelos construídos por meio de **simulações no JFLAP**. 

No contexto do CSP, a tarefa mobiliza competências relacionadas à **análise de poder expressivo**, **modelagem formal com memória**, **equivalência entre dispositivos reconhecedores e gramáticas**, e **argumentação teórica rigorosa**, integrando conhecimento computacional, habilidade formal e disposições epistêmicas próprias da Teoria da Computação. 




## 2. Análise da Entidade Instrucional

### 2.1 Identificação

* **Título:** Labirinto do Minotauro
* **Tipo:** Caso PBL com ênfase em modelagem formal
* **Domínio:** Linguagens Formais, Autômatos de Pilha e Gramáticas Livres de Contexto. 

### 2.2 Descrição 

A tarefa requer que os estudantes **modelem formalmente um sistema de navegação em um labirinto** no qual um agente deve **alcançar um destino e retornar ao ponto de origem**, utilizando uma **estrutura de memória simbólica** para registrar o percurso realizado. 

Os movimentos do agente, como esquerda, direita, avanço e retorno, devem ser representados como **símbolos de um alfabeto**, e os caminhos percorridos devem ser modelados como **cadeias sobre esse alfabeto**. O desafio central consiste em demonstrar que **autômatos finitos são insuficientes** para reconhecer corretamente as sequências válidas de ida e volta, exigindo a construção de um **autômato de pilha (PDA)** que utilize sua pilha como análogo formal do “fio de Ariadne”. 

A tarefa também requer a **especificação de uma gramática livre de contexto (GLC)** equivalente ao PDA construído, evidenciando a relação formal entre **modelos reconhecedores e sistemas geradores**. A correção dos modelos deve ser validada por meio de **simulações no JFLAP** e por **justificativas teóricas** que explicitem propriedades de memória, reconhecimento e equivalência. 



## 3. Resultados Esperados

Ao final da tarefa, espera-se que os estudantes produzam:

* um **autômato de pilha funcional** que reconheça corretamente sequências de navegação com ida e retorno;
* uma **gramática livre de contexto equivalente** que gere a mesma linguagem;
* **simulações no JFLAP** que evidenciem o comportamento correto do PDA;
* uma **análise formal** demonstrando a **insuficiência de autômatos finitos** para o problema;
* um **relatório técnico matematicamente rigoroso**, contendo definições, modelos, justificativas e argumentos formais sobre poder expressivo e equivalência de modelos. 





## 4. Enumeração de Conhecimentos

A realização adequada da **TASK25.02 — Labirinto do Minotauro** requer a mobilização integrada de conhecimentos disciplinares em **Teoria da Computação** e de conhecimentos profissionais fundamentais, conforme os referenciais do **CS2023** e do **CC2020**. Esses conhecimentos sustentam tanto a **modelagem formal do problema** quanto a **análise de poder expressivo e equivalência de modelos** exigida pela tarefa. 

### 4.1 Conhecimentos de Computação (CS2023)

* **Linguagens Formais**

  * alfabetos, cadeias e linguagens;
  * definição de linguagens por propriedades estruturais;
  * distinção entre reconhecimento e geração de linguagens.

* **Autômatos Finitos**

  * limitações de memória dos AF;
  * incapacidade de reconhecer padrões de ida e retorno arbitrários.

* **Autômatos de Pilha (PDA)**

  * pilha como mecanismo de memória estruturada;
  * reconhecimento de linguagens livres de contexto;
  * relação entre operações de empilhar e desempilhar e o controle de percursos.

* **Gramáticas Livres de Contexto (GLC)**

  * definição e uso de regras de produção;
  * geração de linguagens livres de contexto;
  * correspondência entre PDA e GLC.

* **Equivalência entre Modelos**

  * equivalência formal entre **PDA e GLC**;
  * distinção entre classes de linguagens, em especial **regulares** e **livres de contexto**.

* **Simulação e Validação de Modelos**

  * uso de ferramentas como o **JFLAP** para testar PDAs e gramáticas;
  * interpretação formal dos resultados de simulação. 




### 4.2 Conhecimentos Profissionais Fundamentais (FPK — CC2020)

* **Pensamento Analítico e Crítico**
  Capacidade de decompor o comportamento do sistema, analisar limites expressivos dos modelos e avaliar a correção das soluções propostas.

* **Comunicação Técnica Escrita**
  Capacidade de produzir um **relatório claro, estruturado e matematicamente preciso**, expressando definições, modelos, argumentos e conclusões de forma coerente e verificável. 





## 5. Objetivos de Aprendizagem

### Objetivo Geral

Capacitar o estudante a **modelar, analisar e justificar formalmente sistemas de navegação com retorno**, utilizando **autômatos de pilha e gramáticas livres de contexto** para representar e reconhecer sequências de movimentos que requerem **memória estruturada**, distinguindo claramente os **limites dos autômatos finitos**. 

### Objetivos Específicos

Ao concluir a tarefa, o estudante deverá ser capaz de:

* **LO1 — Abstrair o domínio do labirinto**
  Representar posições, movimentos e percursos do labirinto por meio de **símbolos de um alfabeto formal** e **cadeias**.

* **LO2 — Caracterizar formalmente os percursos válidos**
  Definir quais sequências de movimentos correspondem a trajetos corretos de **ida e retorno** no labirinto, distinguindo-as de cadeias inválidas.

* **LO3 — Analisar os limites dos autômatos finitos**
  Justificar formalmente por que **AF não são suficientes** para reconhecer linguagens de navegação com retorno arbitrário.

* **LO4 — Construir um autômato de pilha (PDA)**
  Projetar um **PDA funcional** que reconheça corretamente as sequências válidas de navegação, utilizando a **pilha como memória do percurso**.

* **LO5 — Especificar uma gramática livre de contexto (GLC)**
  Construir uma **GLC equivalente ao PDA**, capaz de gerar a mesma linguagem de percursos.

* **LO6 — Analisar a equivalência entre modelos**
  Explicar formalmente a correspondência entre o **PDA e a GLC**, em termos de reconhecimento e geração da linguagem.

* **LO7 — Validar modelos por simulação**
  Utilizar o **JFLAP** para testar e confirmar o comportamento correto do PDA e da gramática.

* **LO8 — Justificar formalmente correção e limites**
  Produzir argumentos rigorosos sobre **correção, poder expressivo e limitações dos modelos** utilizados.

* **LO9 — Comunicar resultados tecnicamente**
  Elaborar um **relatório matematicamente rigoroso**, distinguindo definições, exemplos, simulações e provas formais. 





## 6. Competências da TASK25.02 (com Ativações OntoKSD)

As competências a seguir constituem o perfil de desempenho esperado para a **TASK25.02 — Labirinto do Minotauro**. Cada competência é explicitada em termos de papel de ativação, modo de ativação e condição de ativação, de forma alinhada ao catálogo atual da OntoKSD e às exigências conceituais e evidenciais da tarefa. O conjunto foi ajustado para preservar coerência com o catálogo consolidado, evitando tanto o reuso de competências cujo escopo atual se tornou específico de outras tarefas quanto o uso indevido de competências especializadas fora de seu significado original.


### **C18 — Model real-world problems using formal language concepts**

**Tipo:** Competência atômica

**ActivationRole:** `core`
**ActivationMode:** `constructive`
**ActivationConstraint:** `mandatory`

**Particularização na TASK25.02:**
Mapear posições, movimentos e percursos do labirinto em símbolos, cadeias e linguagens, estabelecendo a representação formal do problema de navegação. Essa competência sustenta a abstração inicial do domínio e a definição do espaço simbólico a ser modelado.



### **C17 — Apply operations on formal languages**

**Tipo:** Competência atômica

**ActivationRole:** `core`
**ActivationMode:** `analytical`
**ActivationConstraint:** `mandatory`

**Particularização na TASK25.02:**
Analisar sequências de navegação por meio de concatenação, decomposição de cadeias, prefixos, sufixos e estrutura recursiva, distinguindo cadeias válidas e inválidas de ida e retorno. Nesta tarefa, C17 é mobilizada para a análise estrutural da linguagem de percursos, e não como competência de implementação do modelo com memória.



### **C02 — Justify the use of Deterministic Finite Automata (DFAs)**

**Tipo:** Competência atômica

**ActivationRole:** `supporting`
**ActivationMode:** `justificatory`
**ActivationConstraint:** `mandatory`

**Particularização na TASK25.02:**
Demonstrar formalmente a insuficiência dos autômatos finitos para o problema e justificar, por contraste, a necessidade de um modelo com memória estruturada. Nesta tarefa, C02 é usada para raciocinar sobre os limites expressivos dos AF diante da exigência de retorno arbitrário, conectando a análise do problema à necessidade de um PDA.




### **C14 — Differentiate classifications of formal grammars**

**Tipo:** Competência atômica

**ActivationRole:** `supporting`
**ActivationMode:** `analytical`
**ActivationConstraint:** `mandatory`

**Particularização na TASK25.02:**
Relacionar linguagens regulares e livres de contexto, justificando por que o problema exige uma gramática livre de contexto e um reconhecedor com memória estruturada. Essa competência sustenta a análise conceitual da classe de linguagem apropriada à tarefa e da mudança de formalismo reconhecedor.




### **C22 — Define Context-Free Grammars for Pushdown Automata**

**Tipo:** Competência atômica nova

**ActivationRole:** `supporting`
**ActivationMode:** `constructive`
**ActivationConstraint:** `mandatory`

**Particularização na TASK25.02:**
Construir uma gramática livre de contexto equivalente ao PDA, formalizando a geração da linguagem de percursos válidos e articulando a relação entre modelo reconhecedor e modelo gerador. Essa competência responde diretamente à exigência da tarefa de produzir uma GLC equivalente ao modelo com memória.


### **C13.01 — Interpret formal grammar-based rules**

**Tipo:** Competência transversal

**ActivationRole:** `transversal`
**ActivationMode:** `analytical`
**ActivationConstraint:** `mandatory`

**Particularização na TASK25.02:**
Interpretar gramáticas livres de contexto, não terminais, regras de produção e derivações formais como instrumentos para especificar a linguagem de navegação e explicar sua relação com o PDA. Nesta tarefa, C13.01 é mobilizada em seu sentido original, ligado a formal grammar-based rules, e não como competência geral de notação algébrica de cadeias e linguagens. Ela sustenta a interpretação das estruturas gramaticais usadas para documentar formalmente o sistema de navegação.



### **C05.01 — Write mathematically rigorous answers**

**Tipo:** Competência transversal

**ActivationRole:** `transversal`
**ActivationMode:** `justificatory`
**ActivationConstraint:** `mandatory`

**Particularização na TASK25.02:**
Justificar a correção do PDA, a equivalência com a GLC e os limites dos autômatos finitos, usando definições, exemplos, argumentos formais e contraexemplos. A tarefa exige que a explicação da solução seja formalmente sustentada, não apenas descrita de modo informal.



### **C03 — Test automata using simulators**

**Tipo:** Competência de apoio

**ActivationRole:** `supporting`
**ActivationMode:** `artifact-oriented`
**ActivationConstraint:** `mandatory`

**Particularização na TASK25.02:**
Utilizar o JFLAP para validar empiricamente o comportamento do PDA e apoiar a análise da GLC por meio de cadeias de teste e simulações. A simulação é parte explícita do produto da tarefa e constitui evidência observável da adequação do modelo.





### **C19 — Apply homomorphisms in formal languages**

**Tipo:** Competência atômica

**ActivationRole:** `supporting`
**ActivationMode:** `analytical`
**ActivationConstraint:** `conditional`

**Particularização na TASK25.02:**
Pode ser mobilizada quando for necessário explicitar formalmente a codificação entre percurso espacial e representação simbólica, mas não constitui o núcleo da tarefa. Sua ativação é condicional porque a modelagem do percurso não exige necessariamente uma análise explícita de homomorfismos em todas as soluções.




## 7. Nova Competência Introduzida na TASK25.02

### **Competency C22 Specification**

#### Competency Title

**Define Context-Free Grammars for Pushdown Automata**

#### Textual Description

This competency involves the ability to **define and apply context-free grammars that accurately represent the languages recognized by pushdown automata**. Learners must understand the formal correspondence between pushdown automata and context-free grammars and use this relationship to construct, interpret, and validate equivalent representations.

Learners demonstrate this competency by:

* analyzing pushdown automata to identify the structure of the language recognized;
* constructing context-free grammars that generate the same language;
* translating between pushdown automata and context-free grammars using standard formal notation;
* verifying representational equivalence through systematic testing or formal reasoning.



#### Knowledge Specification

* **Pushdown Automata**
* **Context-Free Grammars**
* **Analytical and Critical Thinking (FPK)**



#### Disposition Specification

* Investigative
* Meticulous
* Responsible
* Proactive


#### Knowledge–Skill Pairing

* **Pushdown Automata — Analyze**
  → identify, analyze, abstract stack-based language structure.

* **Context-Free Grammars — Apply (Construct, Translate)**
  → construct, express, translate equivalent grammars.

* **Analytical and Critical Thinking (FPK) — Apply (Reason, Validate)**
  → reason about equivalence, validate correctness, justify representations.






### Estrutura OntoKSD implícita (TASK25.02)

´´´´
TASK25.02
├── coreCompetence
│   ├── C18 — Model real-world problems using formal language concepts
│   └── C17 — Apply operations on formal languages
│
├── transversalCompetence
│   ├── C13.01 — Interpret formal grammar-based rules
│   └── C05.01 — Write mathematically rigorous answers
│
├── supportingCompetence
│   ├── C02 — Justify the use of Deterministic Finite Automata (DFAs)
│   ├── C14 — Differentiate classifications of formal grammars
│   ├── C22 — Define Context-Free Grammars for Pushdown Automata
│   ├── C03 — Test automata using simulators
│   └── C19 — Apply homomorphisms in formal languages (conditional)

´´´´


### Observações ontológicas

- C18 e C17 formam o núcleo cognitivo da abstração do domínio e da análise estrutural dos percursos.
- C13.01 e C05.01 atravessam toda a tarefa, garantindo interpretação formal de regras gramaticais e rigor justificativo.
- C02, C14, C22 e C03 sustentam a análise do poder expressivo, a construção da GLC, a simulação do PDA e a justificação da adequação do modelo.
- C19 permanece como competência de apoio condicional, útil apenas quando a solução explicita formalmente a codificação entre representação espacial e simbólica.



## 8. Mapeamento entre Objetivos de Aprendizagem (LOs) e Competências — TASK25.02

A tabela a seguir explicita a **rastreabilidade pedagógica e ontológica** entre os **Objetivos de Aprendizagem** definidos para a TASK25.02 e as **competências da OntoKSD** mobilizadas para seu atendimento.

| **LO**  | **Descrição do Objetivo de Aprendizagem**                                                         | **Competências Mobilizadas**          |
| ------- | ------------------------------------------------------------------------------------------------- | ------------------------------------- |
| **LO1** | Abstrair posições, movimentos e percursos do labirinto como símbolos e cadeias                    | C18, C13.01                       |
| **LO2** | Caracterizar formalmente sequências válidas e inválidas de ida e retorno                          | C17, C18, C13.01              |
| **LO3** | Justificar a insuficiência dos autômatos finitos para reconhecer o retorno arbitrário             | C02, C14, C05.01              |
| **LO4** | Construir um PDA que use memória estruturada para reconhecer percursos válidos                    | C18, C17, C02, C13.01     |
| **LO5** | Especificar uma GLC equivalente ao PDA                                                            | C22, C14, C13.01              |
| **LO6** | Explicar formalmente a equivalência entre PDA e GLC                                               | C22, C14, C05.01              |
| **LO7** | Validar o comportamento dos modelos por simulação no JFLAP                                        | C03, C05.01                       |
| **LO8** | Justificar formalmente correção, poder expressivo e limites dos modelos                           | C05.01, C02, C14, C17 |
| **LO9** | Comunicar os resultados em relatório técnico rigoroso                                             | C05.01, C13.01                    |




## Conclusão

CSP-Report da TASK25.02, ajustado ao catálogo atual da OntoKSD, mantém um conjunto de competências semântica e pedagogicamente coerente para a modelagem formal de sistemas de navegação com retorno que exigem memória estruturada. O núcleo da tarefa continua sustentado pela abstração do domínio e pela análise estrutural das sequências de navegação (C18, C17), complementado por competências transversais de interpretação de regras gramaticais formais e rigor justificativo (C13.01, C05.01), além de competências de apoio voltadas à análise do poder expressivo, à construção de uma GLC equivalente, à simulação e à justificativa da adequação do modelo (C02, C14, C22, C03, com C19 como apoio condicional).  


