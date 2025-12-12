# Problema 25.05: Juízes Online na Logistic Solutions

**Autores:** Laís Salvador, Edeyson A. Gomes e Luiz Gavaza  
**Data:** 8 de junho de 2022  



## 1. Problema

Estudantes do Instituto de Computação da **UFBA** estão se preparando para a **Maratona de Programação da SBC**  
(http://maratona.sbc.org.br), onde equipes submetem soluções para problemas desafiadores por meio de sistemas automatizados de avaliação — os **Juízes Online (OJ – Online Judges)**.

Esses sistemas executam o código submetido em múltiplos casos de teste e retornam resultados como:

- **AC – Accepted:** solução correta em todos os casos;  
- **WA – Wrong Answer:** saída incorreta em pelo menos um caso;  
- **TLE – Time Limit Exceeded:** a execução ultrapassou o tempo limite;  
- **CE – Compilation Error:** falha de compilação;  
- **RE – Runtime Error:** erro em tempo de execução (ex.: acesso inválido à memória, divisão por zero).

Durante os treinos, o estudante **Carlos** se deparou com um problema clássico de logística: o **Problema do Caixeiro Viajante**  
(**TSP – Traveling Salesman Problem**). Ele levou o desafio para sua equipe na startup **Logistic Solutions**, que começou a submeter implementações a um OJ.  

Embora tenham resolvido falhas de compilação e execução (**CE**, **RE**) e eliminado respostas incorretas (**WA**), todas as soluções continuavam retornando **TLE**.

Diante disso, surgiram dúvidas importantes:

- O problema estaria na **lógica das soluções** ou nas **configurações do OJ**?  
- Que **estratégias** seriam necessárias para alcançar um resultado **AC** ao resolver instâncias do TSP dentro dos limites do OJ?

Paralelamente, gestores da startup demonstraram interesse em saber mais sobre o funcionamento desses sistemas. Carlos recebeu, então, duas tarefas adicionais:

- Avaliar se o **OJ** seria capaz de lidar também com outros problemas complexos, como o **Problema de Alocação de Horários**  
  (**PT – Timetabling**), relatado por uma universidade cliente;  
- Investigar se o OJ consegue **identificar razões para resultados TLE** em diversas situações, tanto quando o código é escrito por programadores experientes quanto por aprendizes de programação.

Ao levar essas questões para discussão na disciplina de **Teoria da Computação**, seus colegas perceberam que o comportamento do OJ poderia ser **abstraído e explicado por meio de uma Máquina de Estados Finitos (MEF)**, capaz de representar:

- transições entre situações típicas de avaliação (**AC, WA, TLE, CE, RE**);  
- o **fluxo operacional** do OJ.

### Desafio Central

Os estudantes devem:

- Investigar por que soluções de **TSP** e **PT** tendem a gerar **TLE**, relacionando esses resultados à **complexidade computacional**;  
- Modelar o funcionamento do **OJ** por meio de uma **MEF**, ilustrando de forma clara e didática o ciclo de avaliação e suas restrições;  
- Investigar as **limitações teóricas** de sistemas de Juízes Online, decorrentes de propriedades fundamentais das linguagens, autômatos e modelos computacionais.



## 2. Entregáveis

A submissão dos entregáveis deve ser feita via **Moodle da UFBA**, até **23h59 do dia 06/01/2025**.

A equipe deverá:

### Artigo Técnico (formato SBC)

Submeter um artigo no formato da **SBC**, contendo todas as análises e resultados. O relatório deve incluir:

- Discussões da equipe sobre o **TSP** e o **PT** em OJs;  
- Hipóteses fundamentadas sobre os resultados das submissões de instâncias do TSP e do PT;  
- Caracterização dos problemas **TSP** e **PT**, destacando:
  - desafios computacionais;
  - dificuldade de obter soluções exatas eficientes;
  - razões pelas quais soluções podem provocar **TLE**;
  - estratégias para contornar esse tipo de problema.

#### Desafio Extra

- Avaliar códigos para **TSP** e **PT** em um OJ e apresentar resultados para **diferentes tamanhos de entrada**.

### Respostas aos Gestores da Startup

- Explicação **conceitual e prática** sobre os limites de um OJ;  
- Indicação da **capacidade do OJ** para avaliar diferentes classes de problemas;  
- Fundamentação teórica para justificar:
  - por que certos comportamentos de programas são difíceis (ou impossíveis) de analisar totalmente;
  - até onde um OJ consegue **prever ou diagnosticar** causas para TLE.

### Modelagem do OJ

Apresentar uma **Máquina de Estados Finitos (MEF)** representando o comportamento do OJ, contendo:

- diagrama de estados com transições entre **AC, WA, CE, RE, TLE**, etc.;  
- justificativa de como a MEF captura o comportamento geral do sistema;  
- destaque para **limitações intrínsecas** do modelo e do próprio processo de avaliação.

O texto deve ser claro, bem estruturado, com rigor científico, conectando questões práticas aos conceitos teóricos da disciplina, e utilizando corretamente as **referências bibliográficas**.



## 3. Recursos de Aprendizagem

HOPCROFT, J. E.; ULLMAN, J. D.; MOTWANI, R.  
*Introduction to Automata Theory, Languages, and Computation.* Campus, 2002.

SIPSER, M.  
*Introduction to the Theory of Computation.* Thomson Learning, 2007.

VIEIRA, Newton José.  
*Linguagens e Máquinas: Uma Introdução aos Fundamentos da Computação.* 2004.

ZIVIANI, Nivio.  
*Projeto de algoritmos: com implementações em Pascal e C.* Thomson, 2004.  
Disponível em: https://www2.dcc.ufmg.br/livros/algoritmos/



## 4. Conceitos Envolvidos

- Linguagens Recursivamente Enumeráveis  
- Problemas Indecidíveis  
- Máquina de Turing Universal  
- Problemas **P**, **NP** e **NP-Completos**  
- Máquinas de Estados Finitos  
- Problema do Caixeiro Viajante (**TSP**)  
- Problema de Alocação de Horários (**PT – Timetabling**)  
- Limitações de sistemas automáticos de avaliação  
- Complexidade temporal e comportamentos não analisáveis em geral  
- Modelos abstratos para análise de sistemas computacionais  



## 5. Objetivos de Aprendizagem

### 5.1 Objetivo Geral

Aplicar conceitos fundamentais da **Teoria da Computação** para modelar, analisar e resolver problemas práticos relacionados a **Juízes Online (OJ)** e à **complexidade computacional** de desafios do mundo real, como o **Problema do Caixeiro Viajante (TSP)**.

### 5.2 Objetivos Específicos

- Explicar os princípios das **Máquinas de Estados Finitos (MEFs)** e sua aplicação em OJs;  
- Interpretar os problemas **TSP** e **PT** e reconhecer sua relação com **NP-Completude**;  
- Compreender o **Problema da Parada** e suas implicações;  
- Aplicar MEFs para representar o fluxo de avaliação do OJ;  
- Empregar conceitos de **Máquinas de Turing** e **Linguagens Recursivamente Enumeráveis** para analisar capacidades e limitações dos OJs;  
- Utilizar ferramentas como o **JFLAP** para simular e testar a MEF proposta;  
- Analisar razões para **TLE** relacionando complexidade, limites de tempo e estratégias algorítmicas;  
- Diferenciar **limitações práticas** e **limitações teóricas** dos OJs;  
- Projetar uma **MEF** representando o comportamento de um OJ;  
- Elaborar um relatório técnico no padrão **SBC**;  
- Construir exemplos ilustrativos que demonstrem os desafios de problemas de alta complexidade.



## Referências

KIOTHEKA, F.; ALMEIDA, R.  
*Introdução à maratona de programação.* v. 1.7, 2022.  
Disponível em: https://www.inf.ufpr.br/maratona/livreto

BARBOSA, F.; JEOVANE, J.; AVELINO, G.; MAGALHÃES, A.  
Estudo de coloração de grafos aplicado ao problema de alocação de horários.  
In: **ERCEMAPI**, 12., 2024. Anais […]. SBC, 2024. p. 139–148.  
DOI: https://doi.org/10.5753/ercemapi.2024.243698

CARDOSO, A. C.; FAGUNDES, F.  
Escalonamento de grade de horários de disciplinas com coloração de grafos.  
In: **Jornada de Iniciação Científica do CEULP/ULBRA**, 19., 2019.  
Disponível em: https://ulbra-to.br/jornada/trabalho/escalonamento-de-grade-de-horarios-de-disciplinas-com-coloracao-de-grafos



*Problema reformulado por Laís Salvador, Edeyson Gomes e Marcos Bião em dezembro de 2025.*