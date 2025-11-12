# Problema 3: Controle de Estacionamento

**Autores**: Lais Salvador, Edeyson A. Gomes, Luiz Gavaza
**Data**: 11 de maio de 2022

## 1. Problema

A empresa **EstaciONE**, proprietária de um grande estacionamento em Salvador, enfrenta desafios na gestão eficiente de suas vagas, que são divididas entre **usuários diários, assinantes mensais e clientes rotativos**. Cada vaga é exclusivamente reservada para uma dessas categorias, de modo que um cliente só pode estacionar se houver vaga disponível na categoria correspondente.

O problema surge devido à alta demanda e ao número limitado de vagas, resultando em:

* **Solicitações de estacionamento negadas** quando não há vagas disponíveis na categoria desejada.
* Necessidade de registrar e analisar **as solicitações negadas por categoria**, a fim de ajustar a capacidade ou planejar futuras expansões.

O comportamento do estacionamento é dinâmico ao longo do dia, com veículos **entrando e saindo continuamente**, ocupando e liberando vagas. Um requisito crítico é que, quando uma solicitação de estacionamento é negada por falta de espaço, o sistema deve garantir que esse evento **não interfira no atendimento de clientes subsequentes**.

Dessa forma, a **EstaciONE** precisa de um sistema automatizado capaz de:

1. Acompanhar a ocupação das vagas por categoria.
2. Monitorar e contabilizar as solicitações negadas por categoria.
3. Garantir que o processo de atendimento permaneça eficiente e justo.

Um dos sócios da empresa, estudante de Computação da UFBA, apresentou esse problema real para ser trabalhado com seus colegas na disciplina de **Linguagens Formais e Teoria da Computação**. O grupo tem como objetivo projetar uma **solução inicial** para o controle do estacionamento, baseada em modelos teóricos e máquinas estudadas em sala.

A análise e a apresentação da solução devem refletir não apenas sua implementação prática, mas também sua fundamentação teórica, conectando o problema real aos conceitos de **Linguagens Formais e Teoria da Computação**.

A ferramenta sugerida para simular o sistema de controle de estacionamento é o [JFLAP](http://www.jflap.org).

## 2. Entregáveis

Devem ser enviados, até **23h59 do dia 06/06/2022**, no Moodle da UFBA, os seguintes materiais:

1. Um arquivo contendo o modelo de máquina que resolve o problema.
2. Um **relatório no formato de artigo da SBC (Sociedade Brasileira de Computação)**, descrevendo em detalhe o projeto e o funcionamento do sistema de controle de estacionamento, incluindo o suporte para identificar o número de solicitações negadas por categoria a cada dia. O relatório também deve apresentar uma justificativa para a escolha do modelo de máquina utilizado.

## 3. Cronograma

| **Data** | **Sessão Tutorial**            |
| -------- | ------------------------------ |
| 11/05    | Sessão Tutorial 1 – Problema 3 |
| 18/05    | Sessão Tutorial 2 – Problema 3 |
| 25/05    | Sessão Tutorial 3 – Problema 3 |
| 01/06    | Sessão Tutorial 4 – Problema 3 |
| 06/06    | Entrega da Solução             |

## 4. Recursos de Aprendizagem

* **RAMOS, M. V. M.; JOSÉ NETO, J.; VEGA, I. S.**
  *Linguagens Formais: Teoria, Modelagem e Implementação*. Bookman, 2009.

* **MENEZES, Paulo Blauth.**
  *Linguagens Formais e Autômatos*, 6ª ed. Bookman, 2011.

* **VIEIRA, Newton José.**
  *Linguagens e Máquinas: Uma Introdução aos Fundamentos da Computação*, 2004.

## 5. Conceitos Envolvidos

1. Máquinas de Turing
2. Tese de Church-Turing
3. Variações da Máquina de Turing
4. Hierarquia de Chomsky

## 6. Objetivos de Aprendizagem

### 6.1 Objetivo Geral

Desenvolver habilidades para modelar, implementar e justificar sistemas de controle computacional utilizando conceitos de Máquinas de Turing e Linguagens Formais, estabelecendo conexões entre fundamentos teóricos e aplicações práticas.

### 6.2 Objetivos Específicos

1. Identificar e justificar problemas computacionais solucionáveis por Máquinas de Turing, relacionando sua estrutura e funcionamento à gestão de vagas de estacionamento.
2. Relacionar o problema de controle de estacionamento às linguagens e modelos da Hierarquia de Chomsky.
3. Projetar uma Máquina de Turing (ou variação adequada) para gerenciar a ocupação de vagas, considerando as categorias e restrições.
4. Implementar o modelo no JFLAP para simular o comportamento do sistema.
5. Justificar a escolha do modelo de máquina computacional (por exemplo, Máquina de Turing ou variação) com base nas características do problema.
6. Propor uma solução que contabilize e monitore o número de solicitações negadas por categoria, auxiliando em decisões gerenciais futuras.
7. Elaborar um relatório técnico no formato da SBC detalhando a solução proposta.
8. Incluir exemplos concretos e justificativas teóricas no relatório para demonstrar a eficácia do sistema.
9. Utilizar a metodologia de **Aprendizagem Baseada em Problemas (PBL)** para organizar o trabalho em equipe e documentar o progresso do projeto.
10. Conectar os fundamentos teóricos da Teoria da Computação a aplicações do mundo real.
11. Utilizar o JFLAP para validar e simular o comportamento do sistema, assegurando que ele atenda aos requisitos definidos pela empresa.
