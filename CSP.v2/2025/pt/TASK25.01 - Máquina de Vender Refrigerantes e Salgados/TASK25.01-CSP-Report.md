
# CSP-Report — TASK25.01 - A Máquina de Vender Refrigerantes e Salgados


## 1. Introdução

Este relatório apresenta a aplicação do **Competency Specification Process (CSP)** à  
**TASK25.01 — Máquina de Vender Refrigerantes e Salgados**, um caso PBL cujo objetivo é modelar, analisar e justificar o comportamento de um sistema discreto por meio de **Linguagens Formais e Autômatos Finitos**.

A TASK25.01 constitui uma **revisão conceitual da Tarefa01**, preservando o uso de
**autômatos e simuladores**, mas reorganizando-os sob um **arcabouço semântico mais
rigoroso**, alinhado ao modelo de competências adotado na **TASK25.00** e à
**OntoKSD**.



## 2. Análise da Entidade Instrucional

### 2.1 Identificação

- **Título:** Máquina de Vender Refrigerantes e Salgados  
- **Tipo:** Caso PBL  
- **Domínio:** Linguagens Formais e Autômatos Finitos  

### 2.2 Descrição Sintética

Os estudantes devem modelar formalmente o funcionamento de uma máquina de venda que:

- aceita moedas e notas específicas;
- vende produtos com preços definidos;
- calcula troco corretamente;
- pode oferecer um bônus eventual;
- pode ser representada por um **autômato finito**;
- pode ser analisada quanto à possibilidade de descrição por **expressões regulares**.

A tarefa exige **modelagem simbólica, validação do comportamento e justificativa
matemática**, com apoio de simuladores quando apropriado.



## 3. Resultados Esperados

Os aprendizes devem produzir:

- um **modelo formal** (autômato finito);
- uma **definição simbólica** de entradas e sequências válidas;
- **simulações** que validem o comportamento do modelo;
- uma **análise formal** sobre reconhecimento e regularidade;
- um **relatório técnico matematicamente rigoroso**.



## 4. Enumeração de Conhecimentos

### 4.1 Conhecimentos de Computação (CS2023)

- **Language Theory**
  - alfabetos, cadeias e linguagens;
  - cadeias válidas e inválidas.

- **Formal Languages**
  - concatenação e sequências admissíveis;
  - linguagens finitas;
  - prefixos e cadeias parciais.

- **Finite Automata**
  - autômatos finitos determinísticos;
  - reconhecimento de linguagens.

- **Regular Expressions**
  - representação algébrica de linguagens regulares;
  - relação entre AF e ER.

### 4.2 Conhecimentos Profissionais (FPK — CC2020)

- Pensamento analítico e crítico  
- Comunicação técnica escrita  


## 5. Objetivos de Aprendizagem

### Objetivo Geral

Modelar e analisar o comportamento de uma máquina de venda como uma
**linguagem formal reconhecida por um autômato finito**, validando esse modelo
por simulação e **justificando formalmente** suas propriedades.


### Objetivos Específicos

- LO1: associar produtos, moedas e ações a símbolos de um alfabeto;
- LO2: representar sequências válidas de uso da máquina;
- LO3: construir um autômato que reconheça essas sequências;
- LO4: simular o comportamento do modelo para validação;
- LO5: justificar formalmente reconhecimento, validade e limites;
- LO6: documentar o raciocínio de forma clara e rigorosa.



## 6. Competências 

As seguintes competências foram identificadas como necessárias.

- **C20 — Modelar e analisar sistemas do mundo real como linguagens formais**
    Competência **composta e de nível de tarefa**, formada por competências conceituais centrais.

- **C18 — Modelar problemas do mundo real como linguagens formais**  
  Abstração do domínio da máquina de venda em símbolos, cadeias e linguagens.

- **C17 — Aplicar operações sobre linguagens formais**  
  Uso de concatenação, sequências válidas e prefixos.

- **C13′ — Interpretar e aplicar notação algébrica de strings e linguagens**  
  Manipulação formal de ε, concatenação e linguagens.

- **C05′ — Produzir respostas matematicamente rigorosas**  
  Uso de definições formais, exemplos, justificativas e distinção entre intuição e prova.

- **C04 — Definir linguagens por meio de expressões regulares**  
  Quando aplicável, ou justificar formalmente a impossibilidade.

- **C02 — Justify the use of Deterministic Finite Automata (DFAs)**  
  Justificar formalmente que o comportamento da máquina pode ser modelado por um DFA,
  explicando estados, transições e condições de aceitação.

- **C03 — Test automata using simulators**  
  Utilizar simuladores (ex.: JFLAP) para **validar o comportamento do modelo**, não como
  fim em si, mas como **evidência empírica complementar** à justificativa formal.





## 8. Estrutura Semântica Resultante

`````
TASK25.01
 └── targetsCompetence
      └── C20 — Modelar e analisar sistemas como linguagens formais
        |   ├── C18 (Modelagem)
        |   ├── C17 (Operações)
        |   ├── C13′ (Notação algébrica)
        |   ├── C05′ (Rigor matemático)
        |   └── C04 (Expressões regulares)
        |
        ├── C02 (Justificação de DFA)
        └── C03 (Simulação de autômatos)
`````

## 9. Conclusão

O CSP-Report da TASK25.01 consolida um reuso controlado e semanticamente
justificado das competências da Tarefa01, integrando C02 e C03 como
competências de apoio, sem inflar o núcleo conceitual da tarefa.

A tarefa é adequadamente caracterizada por uma competência agregada de nível de
tarefa (C20), sustentada por competências que enfatizam modelagem formal,
manipulação simbólica e argumentação matemática rigorosa, mantendo alinhamento
com a OntoKSD e o CS2023.