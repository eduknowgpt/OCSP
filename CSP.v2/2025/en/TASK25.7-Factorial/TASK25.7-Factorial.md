# ✅ **Tarefa Aprimorada (versão pronta para CSP)**

## **Título da Tarefa**

Cálculo de Fatoriais com Funções e Estruturas de Repetição

## **Descrição da Situação-Problema**

Em um sistema de apoio ao laboratório de matemática da escola, é necessário desenvolver um módulo que calcule o **fatorial de uma série de valores** informados pelo usuário. O laboratório costuma testar algoritmos com diferentes conjuntos de dados, então o sistema deve permitir que o usuário informe **quantos valores serão avaliados** e, em seguida, solicitar cada valor individualmente.

Para garantir a clareza e modularidade do código, o cálculo do fatorial **deve obrigatoriamente ser implementado como uma função** separada, que receba o número como parâmetro e retorne o resultado.

O programa deve:

1. Ler um número inteiro **n**, indicando quantos valores serão inseridos;
2. Ler **n valores inteiros** (um por vez);
3. Para cada valor, calcular e exibir o **fatorial** correspondente utilizando a função implementada.

O sistema deve validar entradas negativas, exibindo mensagem de erro e solicitando nova entrada quando necessário.

## **Requisitos Funcionais da Tarefa**

* RF1: Receber um inteiro n que representa a quantidade de valores.
* RF2: Ler cada valor individualmente.
* RF3: Implementar uma função `fatorial(x)` que calcule o fatorial de x.
* RF4: Validar que x ≥ 0 (rejeitar negativos).
* RF5: Exibir o fatorial de cada valor no formato: `n! = resultado`.

## **Variações e Extensões (progressão de complexidade)**

* V1 (básica): Apenas calcular fatoriais sem validação.
* V2 (intermediária): Adicionar validação de entradas negativas.
* V3 (avançada): Tratar casos de números grandes (usar tipo adequado ou mensagem de limite).
* V4 (avançada): Armazenar todos os resultados em uma lista e exibir um resumo final.

Isso permite **progressão cognitiva** e **reuso de competências**, atendendo ao CSP.

---

# 🎯 **Conhecimentos relacionados (OntoKSD — Knowledge)**

## **Fundamentos de Programação**

* Tipos de dados numéricos (inteiros).
* Entrada e saída padrão (I/O).
* Estruturas de repetição (laço contado).
* Estruturas condicionais (validação de dados).
* Procedimentos e funções (definição, parâmetros, retorno).
* Escopo de variáveis.

## **Matemática Computacional**

* Conceito de fatorial (n!).
* Relação recursiva multiplicativa.
* Operações aritméticas.

## **Boas Práticas de Programação**

* Modularização.
* Tratamento de erros e entradas inválidas.
* Organização lógica de programas.

---

# 🎯 **Objetivos de Aprendizagem (LOs)**

A seguir, alinhados à BNCC Computação e à Taxonomia de Bloom (níveis de *Aplicar*, *Analisar*, *Criar*):

## **LO1 – Aplicar**

* **Aplicar** estruturas de repetição para percorrer coleções de dados.
* **Aplicar** funções para organizar soluções algorítmicas modulares.

## **LO2 – Analisar**

* **Analisar** entradas numéricas e identificar valores inválidos (negativos).
* **Diferenciar** quando uma tarefa deve ser resolvida por função ou rotina simples.

## **LO3 – Criar**

* **Criar** uma função que calcule o fatorial de um número utilizando raciocínio lógico estruturado.
* **Construir** um programa modular que coordena entrada de dados, processamento e saída.

---

# 🧠 **Operações Cognitivas (Bloom – verbos da Computação)**

* **Identificar** (valores inválidos, fluxo de repetição).
* **Implementar** (função de fatorial).
* **Modularizar** (separar lógica do cálculo).
* **Executar** (laços e chamadas de função).
* **Testar** (valores variados).
* **Depurar** (erros de entrada e cálculo).

---

# 📦 **Competências Potenciais (modelo KSD — prévias para CSP)**

### **Exemplo de Competência Derivada (rascunho)**

> **Implementar algoritmos modulares que realizam cálculos matemáticos recorrentes**, utilizando funções, estruturas de repetição e validação de dados para resolver problemas sistemáticos de forma clara e eficiente.

### **Conhecimento (K)**

* Estruturas de repetição.
* Funções e modularização.
* Operações matemáticas básicas.
* I/O e validação.

### **Habilidade (S)**

* Implementar e testar funções computacionais.
* Organizar lógica algorítmica de forma modular.
* Controlar fluxo e validação de entradas.

### **Disposições (D)**

* Rigor no teste de entradas incorretas.
* Clareza na organização do código.
* Persistência para depurar e validar.


