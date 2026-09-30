# TASK25.10 – Verificação de Múltiplo de 27  
## Relatório CSP (Competency Specification Protocol)

---

## 1. Introdução

Este relatório aplica o *Competency Specification Protocol (CSP)* à tarefa **TASK25.10 – Verificação de Múltiplo de 27**, cuja entidade instrucional consiste em desenvolver, em linguagem C, um programa que:

- leia um número inteiro e positivo informado pelo usuário;  
- verifique se esse número é múltiplo de 27;  
- apresente uma mensagem clara indicando o resultado da verificação.

O objetivo central é explicitar conhecimentos, objetivos de aprendizagem e competências computacionais associadas à tarefa, de modo a apoiar o planejamento didático, a avaliação formativa e a posterior integração em sistemas baseados em competências. As competências descritas são focadas exclusivamente em Computação e organizadas em torno de operadores aritméticos, estruturas condicionais, validação de entrada, construção de algoritmos sequenciais e testagem/depuração de programas simples em C.

---

## 2. Análise da Entidade Instrucional

### 2.1 Problema

A entidade instrucional é uma tarefa de programação introdutória em C que propõe o seguinte desafio computacional:

- Desenvolver um programa em C que leia um número inteiro e positivo informado pelo usuário;  
- Verificar se o número digitado é múltiplo de 27, utilizando uma operação aritmética adequada (operador módulo `%`);  
- Exibir uma mensagem textual clara indicando se o número é ou não múltiplo de 27.

### 2.2 Processo esperado

O processo esperado para a resolução do problema envolve:

- Leitura do número inteiro fornecido pelo usuário por meio da entrada padrão;  
- Validação básica de que o valor informado é um número não negativo (preferencialmente positivo);  
- Cálculo do resto da divisão do número por 27 utilizando o operador módulo (`%`);  
- Uso de estrutura condicional (`if` / `else`) para decidir a mensagem de saída com base no resultado do cálculo;  
- Apresentação de uma saída textual clara, indicando explicitamente se o número digitado é múltiplo de 27 ou não.

---

## 3. Enumeração dos Conhecimentos

- **K1 – Tipos de Dados Inteiros e Variáveis em C**  
  Compreender e declarar variáveis inteiras (`int`) para armazenar valores fornecidos pelo usuário.

- **K2 – Entrada e Saída Padrão em C (I/O)**  
  Utilizar `printf` e `scanf` (ou funções equivalentes) para interagir com o usuário, solicitando dados e exibindo resultados.

- **K3 – Operador Módulo (`%`) e Conceito de Múltiplo**  
  Entender que `a % b == 0` implica que `a` é múltiplo de `b`, articulando esse conceito matemático na implementação em C.

- **K4 – Estruturas Condicionais (`if` / `else`)**  
  Empregar decisões lógicas para executar caminhos distintos de código a partir de condições booleanas.

- **K5 – Validação Simples de Entrada**  
  Reconhecer a importância de garantir que os dados atendam aos requisitos (por exemplo, número positivo), ainda que com lógica elementar.

- **K6 – Compilação e Execução de Programas em C**  
  Compilar o código (por exemplo, com `gcc`) e executar o programa em um ambiente de desenvolvimento, interpretando mensagens do compilador e resultados.

- **K7 – Testes e Casos de Borda em Programas Simples**  
  Planejar e executar testes com diferentes entradas (múltiplos, não múltiplos, zero, negativos, valores extremos), identificando falhas e ajustando o código.

---

## 4. Objetivos de Aprendizagem

- **LO1.** Declarar e utilizar variáveis inteiras em C para armazenar valores fornecidos pelo usuário em um programa simples.  
- **LO2.** Implementar a leitura de dados via teclado utilizando funções de entrada e saída padrão em C (`scanf`, `printf`).  
- **LO3.** Aplicar o operador módulo (`%`) para verificar se um número inteiro é múltiplo de outro, interpretando corretamente o resultado.  
- **LO4.** Utilizar estruturas condicionais (`if` / `else`) para controlar o fluxo de execução do programa com base em uma condição lógica.  
- **LO5.** Produzir uma saída textual clara e coerente, informando ao usuário se o número digitado é ou não múltiplo de 27.  
- **LO6.** Executar e testar o programa com diferentes entradas, reconhecendo a importância de verificar correção para valores múltiplos, não múltiplos e casos de borda.

---

## 5. Especificação das Competências (CSP)

### 5.1 Competência CT-MULT27.1

**Competência CT-MULT27.1**  
**Título**  

Construir algoritmos sequenciais simples com clareza e correção.

**Descrição Textual**

Trata-se da capacidade de elaborar algoritmos sequenciais simples que representem, de forma clara e ordenada, o processo de leitura de um valor, aplicação de uma operação aritmética e apresentação de um resultado.

No contexto da tarefa, o estudante deve ser capaz de organizar a solução em passos bem definidos (ler o número, calcular o resto da divisão por 27, decidir a mensagem), mantendo a coerência entre o enunciado do problema, o algoritmo planejado e o código em C.

Essa competência envolve a articulação entre o entendimento conceitual de algoritmo e sua tradução para uma sequência de instruções executáveis, respeitando a sintaxe básica da linguagem C.

**Conhecimentos Necessários**

**Algoritmo Sequencial**  
Descrição  
Capacidade de descrever uma solução como uma sequência finita de passos, sem desvios complexos, garantindo início, processamento e término bem definidos.  
Bloom: Aplicar  
Verbos: Descrever, Organizar, Sequenciar  

**Sintaxe Básica de Programas em C**  
Descrição  
Conhecimento da estrutura mínima de um programa em C (função `main`, blocos delimitados por chaves, ponto-e-vírgula, comentários).  
Bloom: Aplicar  
Verbos: Escrever, Estruturar, Implementar  

**Declaração de Variáveis Inteiras**  
Descrição  
Utilizar corretamente variáveis inteiras (`int`) para armazenar entradas do usuário e intermediários de cálculo.  
Bloom: Aplicar  
Verbos: Declarar, Atribuir, Manipular  

**Disposições**

- Organizado  
- Cuidadoso  
- Persistente  

**BNCC – Alinhamento**

- **Eixo:** Pensamento Computacional (PC).  
- **Habilidades Específicas:**  
  - **EM13CO01 (PC)** – Explorar e construir a solução de problemas por meio da reutilização de partes de soluções existentes.  
  - **EM13CO02 (PC)** – Explorar e construir a solução de problemas por meio de refinamentos, utilizando diversos níveis de abstração desde a especificação até a implementação.  
- **Competência Geral de Computação:**  
  - Competência Geral 5 de Computação – desenvolver projetos que envolvam a investigação de desafios e a construção de soluções computacionais.

**Tabela Resumo – CT-MULT27.1**

| Código       | Competência                                               | Disposição                      | Conhecimento                       | Habilidade                                         |
|-------------|-----------------------------------------------------------|----------------------------------|------------------------------------|----------------------------------------------------|
| CT-MULT27.1 | Construir algoritmos sequenciais simples com clareza e correção. | Organizado, Cuidadoso, Persistente | Algoritmo Sequencial              | Aplicar (Descrever, Organizar, Sequenciar)         |
| CT-MULT27.1 | Construir algoritmos sequenciais simples com clareza e correção. | Organizado, Cuidadoso, Persistente | Sintaxe Básica de Programas em C  | Aplicar (Escrever, Estruturar, Implementar)        |
| CT-MULT27.1 | Construir algoritmos sequenciais simples com clareza e correção. | Organizado, Cuidadoso, Persistente | Declaração de Variáveis Inteiras  | Aplicar (Declarar, Atribuir, Manipular)            |

---

### 5.2 Competência CT-MULT27.2

**Competência CT-MULT27.2**  
**Título**  

Aplicar operadores aritméticos para verificar múltiplos.

**Descrição Textual**

Essa competência envolve o uso adequado de operadores aritméticos, em especial o operador módulo (`%`), para verificar relações de múltiplo e divisor entre inteiros.

No âmbito da tarefa, o estudante deve ser capaz de traduzir o conceito matemático de múltiplo para uma expressão lógica em C, como `numero % 27 == 0`, compreendendo o significado do resto da divisão e sua relação com a propriedade de múltiplo.

A competência inclui tanto a dimensão conceitual (o que significa ser múltiplo) quanto a dimensão procedimental (como operacionalizar essa verificação em código).

**Conhecimentos Necessários**

**Operador Módulo e Aritmética de Inteiros em C**  
Descrição  
Utilização de operações aritméticas com inteiros, em particular o operador `%`, para obter o resto da divisão e avaliar múltiplos.  
Bloom: Aplicar  
Verbos: Calcular, Verificar, Implementar  

**Conceito Matemático de Múltiplo e Divisão Exata**  
Descrição  
Compreensão de que um número é múltiplo de outro quando a divisão resulta em resto zero, articulando essa ideia entre Matemática e Computação.  
Bloom: Compreender  
Verbos: Explicar, Relacionar, Interpretar  

**Disposições**

- Rigoroso  
- Atento a detalhes  
- Lógico  

**BNCC – Alinhamento**

- **Eixo:** Pensamento Computacional (PC).  
- **Habilidades Específicas:**  
  - **EM13CO01 (PC)** – Explorar e construir a solução de problemas por meio da reutilização de partes de soluções existentes (por exemplo, padrões de verificação de múltiplos).  
  - **EM13CO02 (PC)** – Explorar e construir a solução de problemas por meio de refinamentos, desde a especificação até a implementação.  
- **Competência Geral de Computação:**  
  - Competência Geral 5 de Computação – desenvolvimento de soluções computacionais com base em raciocínio lógico e fundamentos da Computação.

**Tabela Resumo – CT-MULT27.2**

| Código       | Competência                                         | Disposição                           | Conhecimento                                   | Habilidade                                              |
|-------------|-----------------------------------------------------|--------------------------------------|-----------------------------------------------|---------------------------------------------------------|
| CT-MULT27.2 | Aplicar operadores aritméticos para verificar múltiplos. | Rigoroso, Atento a detalhes, Lógico | Operador Módulo e Aritmética de Inteiros em C | Aplicar (Calcular, Verificar, Implementar)              |
| CT-MULT27.2 | Aplicar operadores aritméticos para verificar múltiplos. | Rigoroso, Atento a detalhes, Lógico | Conceito Matemático de Múltiplo e Divisão Exata | Compreender (Explicar, Relacionar, Interpretar)       |

---

### 5.3 Competência CT-MULT27.3

**Competência CT-MULT27.3**  
**Título**  

Implementar estruturas condicionais para tomada de decisão.

**Descrição Textual**

Esta competência diz respeito à habilidade de traduzir condições lógicas em estruturas condicionais (`if` / `else`) na linguagem C, controlando o fluxo de execução do programa.

Na tarefa em questão, o estudante precisa formular a condição “é múltiplo de 27?” em termos de uma expressão booleana (`numero % 27 == 0`) e, a partir dela, selecionar o bloco de código adequado para imprimir a mensagem correspondente (“é múltiplo” ou “não é múltiplo”).

A competência envolve tanto o domínio das construções sintáticas quanto a coerência semântica entre o enunciado do problema, a expressão lógica e o comportamento do programa.

**Conhecimentos Necessários**

**Expressões Lógicas e Relacionais em C**  
Descrição  
Construção de expressões booleanas a partir de operadores relacionais e lógicos, expressando condições como igualdade, diferença e comparações.  
Bloom: Aplicar  
Verbos: Formular, Avaliar, Comparar  

**Estrutura `if` / `else` em C**  
Descrição  
Uso de comandos condicionais para selecionar blocos de instruções a serem executados de acordo com o valor de uma expressão lógica.  
Bloom: Aplicar  
Verbos: Implementar, Selecionar, Controlar  

**Derivação de Condições a partir de Requisitos**  
Descrição  
Capacidade de ler o enunciado do problema e extrair, de forma explícita, as condições que devem ser verificadas pelo programa.  
Bloom: Analisar  
Verbos: Identificar, Decompor, Justificar  

**Disposições**

- Raciocínio lógico  
- Cuidadoso  
- Sistemático  

**BNCC – Alinhamento**

- **Eixo:** Pensamento Computacional (PC).  
- **Habilidades Específicas:**  
  - **EM13CO02 (PC)** – Explorar e construir a solução de problemas por meio de refinamentos, utilizando diversos níveis de abstração desde a especificação até a implementação.  
- **Competência Geral de Computação:**  
  - Competência Geral 5 de Computação – planejar e implementar soluções computacionais com base em raciocínio lógico e estruturas de controle.

**Tabela Resumo – CT-MULT27.3**

| Código       | Competência                                             | Disposição                               | Conhecimento                                   | Habilidade                                            |
|-------------|---------------------------------------------------------|------------------------------------------|-----------------------------------------------|-------------------------------------------------------|
| CT-MULT27.3 | Implementar estruturas condicionais para tomada de decisão. | Raciocínio lógico, Cuidadoso, Sistemático | Expressões Lógicas e Relacionais em C        | Aplicar (Formular, Avaliar, Comparar)                 |
| CT-MULT27.3 | Implementar estruturas condicionais para tomada de decisão. | Raciocínio lógico, Cuidadoso, Sistemático | Estrutura `if` / `else` em C                 | Aplicar (Implementar, Selecionar, Controlar)          |
| CT-MULT27.3 | Implementar estruturas condicionais para tomada de decisão. | Raciocínio lógico, Cuidadoso, Sistemático | Derivação de Condições a partir de Requisitos | Analisar (Identificar, Decompor, Justificar)         |

---

### 5.4 Competência CT-MULT27.4

**Competência CT-MULT27.4**  
**Título**  

Validar entradas numéricas conforme requisitos do programa.

**Descrição Textual**

Trata-se da capacidade de verificar se os dados fornecidos pelo usuário atendem aos requisitos da tarefa, identificando situações inválidas (por exemplo, número negativo ou zero, quando o problema exige número positivo) e tratando-as de forma apropriada.

Na tarefa de múltiplo de 27, a competência se manifesta quando o estudante:

- reconhece que o enunciado exige um número inteiro e positivo;  
- incorpora essa restrição na lógica do programa (por exemplo, verificando `numero <= 0`);  
- decide se o programa deve rejeitar o valor, solicitar nova entrada ou, no mínimo, informar o usuário sobre a inconsistência.

Essa competência aproxima o estudante de uma visão mais robusta de programação, em que pré-condições e validação de dados são elementos essenciais de qualidade de software.

**Conhecimentos Necessários**

**Requisitos de Entrada e Pré-condições**  
Descrição  
Noção de que certos programas assumem condições mínimas sobre os dados de entrada, e que essas condições devem ser explicitadas e verificadas.  
Bloom: Analisar  
Verbos: Identificar, Delimitar, Justificar  

**Validação Básica de Dados Numéricos**  
Descrição  
Aplicação de verificações simples (por exemplo, `> 0`) para confirmar se os dados estão dentro de faixas aceitáveis antes de proceder ao cálculo.  
Bloom: Aplicar  
Verbos: Verificar, Filtrar, Garantir  

**Mensagens de Erro e Comunicação com o Usuário**  
Descrição  
Formulação de mensagens textuais claras para informar ao usuário sobre entradas inválidas e orientar sobre o uso correto do programa.  
Bloom: Aplicar  
Verbos: Comunicar, Informar, Orientar  

**Disposições**

- Responsável  
- Cuidadoso  
- Ético  

**BNCC – Alinhamento**

- **Eixo:** Pensamento Computacional (PC).  
- **Habilidades Específicas:**  
  - **EM13CO02 (PC)** – Explorar e construir a solução de problemas por meio de refinamentos, desde a especificação (incluindo restrições de entrada) até a implementação.  
- **Competência Geral de Computação:**  
  - Competência Geral 5 de Computação – desenvolver soluções computacionais considerando requisitos, restrições e correção de resultados.

**Tabela Resumo – CT-MULT27.4**

| Código       | Competência                                                  | Disposição                     | Conhecimento                            | Habilidade
