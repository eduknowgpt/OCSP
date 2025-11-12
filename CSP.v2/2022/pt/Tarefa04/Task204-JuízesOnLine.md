# Problema 4: Juízes Online na Logistic Solutions

**Autores**: Lais Salvador, Edeyson A. Gomes, Luiz Gavaza
**Data**: 8 de junho de 2022

## 1. Problema

Vários estudantes do **Instituto de Computação da UFBA** estão se preparando para participar da **Maratona de Programação da SBC** ([http://maratona.sbc.org.br](http://maratona.sbc.org.br)). Nessa competição, as equipes submetem códigos-fonte para resolver problemas, utilizando sistemas de avaliação conhecidos como **Juízes Online (OJ – Online Judges)**.

Um OJ avalia o código executando múltiplos casos de teste e retornando um dos seguintes resultados:

1. **AC – Accepted**: passou em todos os casos de teste.
2. **WA – Wrong Answer**: resposta incorreta em pelo menos um caso de teste.
3. **TLE – Time Limit Exceeded**: o programa excedeu o tempo limite.
4. **CE – Compilation Error**: o programa falhou na compilação (avisos não são erros).
5. **RE – Runtime Error**: o programa apresentou falha de execução, como acesso inválido à memória ou divisão por zero.

Durante o treinamento para a maratona, o estudante Carlos se deparou com um problema de OJ relacionado à logística — o **Problema do Caixeiro Viajante (TSP – Traveling Salesman Problem)**. Ele compartilhou o desafio com sua equipe da startup **Logistic Solutions**, que começou a submeter códigos para resolvê-lo. Após corrigirem erros de compilação e execução (CE e RE) e eliminarem respostas incorretas (WA), todas as submissões ainda retornavam o mesmo resultado: **TLE**.

Apesar da experiência da equipe, surgiram dúvidas:

* Seria uma falha lógica ou uma abordagem inadequada?
* Que estratégias poderiam levar a um resultado **AC** para o TSP?

Além disso, os gestores da startup se interessaram pelo funcionamento do OJ e pediram a Carlos que investigasse:

* Se o OJ pode avaliar outros tipos de problemas.
* Se o OJ é capaz de detectar quando um programa entra em um **loop infinito**.

Carlos levou essas questões para seus colegas da disciplina de **Teoria da Computação**, que perceberam que o comportamento do OJ poderia ser modelado usando uma **Máquina de Estados Finitos (MEF)** para:

* Representar as transições entre diferentes resultados de avaliação (AC, WA, TLE, etc.).
* Ilustrar o funcionamento do OJ e explicar sua lógica tanto para programadores quanto para gestores.

O principal desafio é:

1. Analisar por que os códigos do TSP retornam **TLE** e como alcançar **AC**.
2. Projetar uma **Máquina de Estados Finitos** que represente a lógica do OJ e explique suas limitações — especialmente a impossibilidade teórica de detectar loops infinitos.

## 2. Entregáveis

A equipe deverá submeter um **relatório no formato de artigo da SBC** contendo todas as análises e resultados. A submissão deve ser feita via **Moodle da UFBA**, até **23h59 do dia 27/06/2022**. O relatório deve incluir:

1. **Discussões da equipe sobre o TSP no OJ**:

   * Hipóteses sobre os resultados das submissões.
   * Caracterização do TSP: sua definição, desafios computacionais e possíveis causas para os resultados TLE.

2. **Respostas aos gestores da startup**:

   * Respostas detalhadas às perguntas propostas, com explicações e demonstrações.
   * Discussão sobre as capacidades e limitações do OJ, especialmente quanto à detecção de loops infinitos.

3. **MEF representando o comportamento do OJ**:

   * Um modelo do OJ usando uma **Máquina de Estados Finitos**, incluindo estados, transições e condições que representem saídas como AC, WA, TLE, etc.
   * Explicação de como a MEF esclarece o funcionamento e as restrições do sistema.

O relatório deve ser claro, bem estruturado e conectar questões práticas aos conceitos teóricos abordados na disciplina.

## 3. Cronograma

| **Data** | **Sessão Tutorial**            |
| -------- | ------------------------------ |
| 08/06    | Sessão Tutorial 1 – Problema 4 |
| 15/06    | Sessão Tutorial 2 – Problema 4 |
| 20/06    | Sessão Tutorial 3 – Problema 4 |
| 27/06    | Sessão Tutorial 4 – Problema 4 |
| 27/06    | Entrega Final                  |

## 4. Recursos de Aprendizagem

* **HOPCROFT, J. E.; ULLMAN, J. D.; MOTWANI, R.**
  *Introduction to Automata Theory, Languages, and Computation*. Campus, 2002.

* **SIPSER, M.**
  *Introduction to the Theory of Computation*. Thomson Learning, 2007.

* **VIEIRA, Newton José.**
  *Linguagens e Máquinas: Uma Introdução aos Fundamentos da Computação*, 2004.

## 5. Conceitos Envolvidos

1. Linguagens Recursivamente Enumeráveis
2. Hierarquia de Chomsky
3. Problema da Parada (*Halting Problem*)
4. Máquina de Turing Universal
5. Problemas P, NP e NP-Completos
6. Máquinas de Estados Finitos

## 6. Objetivos de Aprendizagem

### 6.1 Objetivo Geral

Aplicar conceitos fundamentais da Teoria da Computação para modelar, analisar e resolver problemas práticos relacionados a sistemas de Juízes Online (OJ) e à complexidade computacional de desafios do mundo real, como o Problema do Caixeiro Viajante (TSP).

### 6.2 Objetivos Específicos

1. Compreender Máquinas de Estados Finitos e sua aplicação em sistemas automatizados de avaliação (OJ).
2. Relacionar o Problema do Caixeiro Viajante (TSP) com os problemas NP-Completos e suas implicações práticas.
3. Conectar as validações e saídas do OJ à Hierarquia de Chomsky.
4. Identificar limitações teóricas e práticas na avaliação de programas, incluindo a detecção de loops infinitos.
5. Modelar o comportamento do OJ por meio de uma **Máquina de Estados Finitos (MEF)** com estados como AC, WA, TLE, etc.
6. Utilizar MEFs para explicar o comportamento e as restrições do sistema de avaliação.
7. Compreender o **Problema da Parada (Halting Problem)** e suas implicações na detecção de loops infinitos.
8. Explicar como a teoria da computação justifica as limitações dos OJs.
9. Analisar as causas dos resultados **TLE** nas submissões do TSP.
10. Utilizar conceitos de **Máquina de Turing** e **Linguagens Recursivamente Enumeráveis** para discutir as capacidades dos OJs.
11. Produzir um relatório técnico no formato da SBC, com análise detalhada e fundamentação teórica.
12. Incluir exemplos concretos para demonstrar o comportamento do OJ e os desafios do TSP.
13. Trabalhar colaborativamente utilizando a metodologia de **Aprendizagem Baseada em Problemas (PBL)** para estruturar a resolução.
14. Documentar o progresso da equipe por meio de quadros e diagramas.
15. Implementar e simular a MEF no JFLAP para validar o modelo.

## Referências

**KIOTHEKA, Fernando; ALMEIDA, Raul.** *Introdução à Maratona de Programação*. v. 1.7, 2022.
Disponível em: [https://www.inf.ufpr.br/maratona/livreto](https://www.inf.ufpr.br/maratona/livreto)
