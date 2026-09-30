# 1 - Introdução

Este relatório apresenta a especificação de competências (Competency Specification Protocol – CSP) para uma tarefa de programação em linguagem C cujo foco central é o rastreamento de variáveis, a interpretação de atribuições e de expressões aritméticas, bem como a análise de um trecho de código já fornecido.  

A entidade instrucional de referência é uma questão de múltipla escolha na qual o estudante recebe um programa em C que:

- declara quatro variáveis numéricas (`a`, `b`, `c`, `d`);
- lê valores fornecidos pelo usuário;
- realiza uma sequência de atribuições que “propaga” valores entre as variáveis;
- aplica operações aritméticas encadeadas;
- e, ao final, produz um estado final para as variáveis que deve ser inferido pelo estudante.

O estudante deve determinar, com base na simulação mental ou manual da execução do programa, quais são os valores finais das variáveis após a execução de todas as instruções, escolhendo a alternativa correta.  

---

# 2 - Análise da Entidade Instrucional

## 2.1 Problema

O desafio proposto consiste em analisar um trecho de código em C que realiza leitura e manipulação de quatro variáveis numéricas, aplicando uma série de atribuições e operações aritméticas. A partir de valores iniciais fornecidos para as variáveis (`A`, `B`, `C`, `D`), o estudante deve determinar quais serão os valores finais de `a`, `b`, `c` e `d` após a execução de todas as linhas de código.

- **Entradas:** quatro valores numéricos fornecidos pelo usuário (por exemplo, 10, 15, 20 e 25), associados às variáveis `a`, `b`, `c` e `d`.
- **Processamento:**  
  - leitura dos valores por meio de `scanf`;  
  - sequência de atribuições que copia e sobrescreve valores entre as variáveis (`a = b; b = c; c = d; d = a;`);  
  - aplicação de operações aritméticas com soma, divisão e multiplicação (`b = a + b/2; c = c + b; d = d + (b*2) - a;`), respeitando a precedência de operadores.
- **Saída (conceitual):** estado final das variáveis `a`, `b`, `c` e `d`, que não é impresso no código, mas deve ser inferido pelo estudante para escolher a alternativa correta na questão de múltipla escolha.

A condição central do problema é a capacidade de acompanhar o fluxo de execução linha a linha, atualizando mentalmente ou em uma tabela o valor de cada variável. Não há, na entidade original, impressão explícita dos resultados; a “saída” é conceitual e se materializa na escolha correta da alternativa e na justificativa do raciocínio.

## 2.2 Processo esperado

Em alto nível, o processo de solução esperado por parte do estudante envolve:

1. **Compreensão do código fornecido:**  
   Identificar as declarações de variáveis, o comando de leitura (`scanf`) e a sequência de atribuições e operações aritméticas.

2. **Mapeamento das entradas:**  
   Associar corretamente os valores iniciais fornecidos (por exemplo, 10, 15, 20, 25) às variáveis `a`, `b`, `c`, `d`, considerando a ordem de leitura.

3. **Rastreamento sequencial do programa:**  
   Executar mentalmente o programa linha a linha, atualizando os valores das variáveis após cada instrução relevante:
   - após cada atribuição simples (`a = b; b = c; c = d; d = a;`);
   - após cada expressão aritmética com múltiplos operadores (`b = a + b/2; c = c + b; d = d + (b*2) - a;`).

4. **Respeito à precedência de operadores:**  
   Avaliar corretamente as expressões, considerando a ordem adequada (multiplicação e divisão antes de soma e subtração, uso de parênteses etc.).

5. **Registro do estado das variáveis:**  
   Manter uma tabela ou anotação intermediária com o estado de `a`, `b`, `c`, `d` a cada passo, garantindo clareza no raciocínio.

6. **Determinação da alternativa correta:**  
   Comparar o estado final obtido para as variáveis com as alternativas apresentadas na questão de múltipla escolha e selecionar a opção coerente com o rastreamento realizado.

7. **(Opcional, mas desejável) Validação da solução:**  
   Quando possível, executar o código em um ambiente de desenvolvimento (ajustando, se necessário, especificadores de formato) para confrontar o resultado empírico com o previsto, fortalecendo o raciocínio de testagem e depuração.

---

# 3 - Enumeração dos Conhecimentos

**K1. Tipos de dados numéricos e especificadores de formato em C**  
O estudante precisa compreender como declarar variáveis numéricas (`float`, `int`) e como utilizar especificadores de formato em `scanf` e `printf` (`%f`, `%d` etc.), reconhecendo a importância da consistência entre tipo e formato.

**K2. Entrada de dados com `scanf`**  
É necessário entender como a função `scanf` realiza a leitura de múltiplos valores, a ordem em que eles são lidos e como são atribuídos às variáveis do programa.

**K3. Atribuições e atualização de variáveis**  
O estudante deve dominar a semântica da atribuição em C, compreendendo que o valor à direita do operador `=` é avaliado e então armazenado na variável à esquerda, sobrescrevendo o valor anterior.

**K4. Operadores aritméticos e precedência**  
É essencial saber interpretar expressões com soma, subtração, multiplicação e divisão, respeitando a precedência de operadores e o uso de parênteses, para calcular corretamente o valor resultante.

**K5. Fluxo de execução sequencial**  
O estudante precisa entender que, na ausência de estruturas de controle complexas, o programa é executado linha a linha, na ordem em que as instruções aparecem, o que é crucial para o rastreamento adequado.

**K6. Rastreio (tracing) e simulação manual de código**  
É necessário saber simular a execução do programa manualmente, registrando, em cada etapa, o valor atualizado das variáveis, a fim de prever o comportamento sem depender apenas da execução em máquina.

**K7. Leitura e interpretação de código fornecido**  
O estudante deve ser capaz de compreender um trecho de código escrito por outrem (professor ou autor), mesmo com pequenos problemas de estilo, identificando sua funcionalidade e possíveis pontos de confusão.

**K8. Boas práticas de programação e clareza de código**  
É desejável reconhecer aspectos de clareza, legibilidade e robustez, tais como a consistência entre tipos e especificadores de formato, e a inclusão de saídas auxiliares (por exemplo, `printf`) para apoiar a depuração.

---

# 4 - Objetivos de Aprendizagem

**LO1.** Rastrear, passo a passo, a execução de um programa sequencial em C, identificando os valores assumidos pelas variáveis após cada instrução.  

**LO2.** Interpretar corretamente expressões aritméticas em C, explicando como a precedência de operadores e o uso de parênteses influenciam o resultado final.  

**LO3.** Utilizar adequadamente a função `scanf` para leitura de múltiplos valores, reconhecendo a importância da correspondência entre tipos de dados e especificadores de formato.  

**LO4.** Resolver questões de múltipla escolha sobre o comportamento de algoritmos simples, justificando a alternativa escolhida com base em um rastreamento sistemático do código.  

**LO5.** Analisar criticamente um trecho de código legado, identificando possíveis melhorias em termos de clareza, consistência de tipos e apoio à depuração.

---

# 5 - Especificação das Competências (CSP)

## 5.1 Competência CT-RASTREIO.1

**Competência CT-RASTREIO.1**  
### Título

Rastrear a execução sequencial de programas em C, acompanhando a atualização de variáveis.

### Descrição Textual

Trata-se da capacidade de seguir, de forma sistemática, a execução de um programa sequencial em C, linha a linha, atualizando mentalmente ou em registros escritos o valor de cada variável após cada instrução. No contexto da tarefa, essa competência se manifesta quando o estudante consegue, a partir dos valores de entrada, acompanhar as atribuições e operações aritméticas, construindo uma tabela ou raciocínio estruturado que o leva a determinar o estado final de `a`, `b`, `c` e `d`. Essa competência é fundamental para compreender o funcionamento de programas imperativos, identificar erros lógicos e construir uma base sólida para o estudo de estruturas de controle mais complexas.

### Conhecimentos Necessários

**Rastreio e simulação manual de código (K6)**  
- Descrição  
Capacidade de simular, manualmente, a execução de cada instrução, atualizando os valores das variáveis em uma tabela ou registro intermediário.  
- Bloom: Analisar  
- Verbos: Rastrear, Simular, Verificar, Conferir

**Atribuições e atualização de variáveis (K3)**  
- Descrição  
Entendimento de como o operador de atribuição sobrescreve valores anteriores e de como a ordem das atribuições afeta o estado final das variáveis.  
- Bloom: Compreender  
- Verbos: Explicar, Identificar, Descrever, Reconhecer

**Fluxo de execução sequencial (K5)**  
- Descrição  
Compreensão de que as instruções são executadas na ordem em que aparecem, o que permite prever o efeito de cada linha sobre o conjunto de variáveis.  
- Bloom: Compreender  
- Verbos: Descrever, Relacionar, Ordenar, Interpretar

### Disposições

Organizado, Persistente, Cuidadoso, Rigoroso, Reflexivo.

### BNCC – Alinhamento

- Eixo: Pensamento Computacional (PC).  
- Código: EM13CO02 (Pensamento Computacional) – formular e resolver problemas utilizando conceitos fundamentais de Computação.  
- Competência Geral de Computação: Competência Geral 1 – Desenvolver e aplicar o pensamento computacional na análise e resolução de problemas.

### Tabela Resumo da Competência CT-RASTREIO.1

Código | Competência | Disposição | Conhecimento | Habilidade
---|---|---|---|---
CT-RASTREIO.1 | Rastrear a execução sequencial de programas em C, acompanhando a atualização de variáveis. | Organizado, Persistente, Cuidadoso, Rigoroso, Reflexivo | Rastreio e simulação manual de código (K6) | Analisar (Rastrear, Simular, Verificar, Conferir)
CT-RASTREIO.1 | Rastrear a execução sequencial de programas em C, acompanhando a atualização de variáveis. | Organizado, Persistente, Cuidadoso, Rigoroso, Reflexivo | Atribuições e atualização de variáveis (K3) | Compreender (Explicar, Identificar, Descrever, Reconhecer)
CT-RASTREIO.1 | Rastrear a execução sequencial de programas em C, acompanhando a atualização de variáveis. | Organizado, Persistente, Cuidadoso, Rigoroso, Reflexivo | Fluxo de execução sequencial (K5) | Compreender (Descrever, Relacionar, Ordenar, Interpretar)

---

## 5.2 Competência CT-EXPRESSOES.2

**Competência CT-EXPRESSOES.2**  
### Título

Interpretar e avaliar expressões aritméticas em C respeitando a precedência de operadores.

### Descrição Textual

Esta competência refere-se à habilidade de analisar e calcular corretamente expressões aritméticas em linguagem C, levando em conta a precedência de operadores e o uso de parênteses. No contexto da tarefa, ela se manifesta quando o estudante interpreta corretamente expressões como `b = a + b/2;` e `d = d + (b*2) - a;`, determinando com precisão os valores resultantes. Essa competência é essencial para evitar erros de cálculo e para compreender o efeito real das instruções sobre o estado das variáveis, contribuindo para o desenvolvimento de um raciocínio matemático e computacional integrado.

### Conhecimentos Necessários

**Operadores aritméticos e precedência (K4)**  
- Descrição  
Domínio das regras de precedência de operadores (multiplicação e divisão antes de soma e subtração, uso de parênteses) e sua aplicação em expressões em C.  
- Bloom: Aplicar  
- Verbos: Calcular, Aplicar, Determinar, Resolver

**Tipos de dados numéricos em C (K1)**  
- Descrição  
Compreensão dos tipos numéricos (`int`, `float` etc.) e de como eles se comportam em operações aritméticas, inclusive quanto a possíveis efeitos de conversão.  
- Bloom: Compreender  
- Verbos: Explicar, Reconhecer, Diferenciar, Descrever

### Disposições

Lógico, Cuidadoso, Detalhista, Rigoroso.

### BNCC – Alinhamento

- Eixo: Pensamento Computacional (PC).  
- Código: EM13CO01 (Pensamento Computacional) – analisar problemas e desenvolver representações e procedimentos para sua resolução.  
- Competência Geral de Computação: Competência Geral 2 – Utilizar modelos e representações para descrever e analisar situações e processos.

### Tabela Resumo da Competência CT-EXPRESSOES.2

Código | Competência | Disposição | Conhecimento | Habilidade
---|---|---|---|---
CT-EXPRESSOES.2 | Interpretar e avaliar expressões aritméticas em C respeitando a precedência de operadores. | Lógico, Cuidadoso, Detalhista, Rigoroso | Operadores aritméticos e precedência (K4) | Aplicar (Calcular, Aplicar, Determinar, Resolver)
CT-EXPRESSOES.2 | Interpretar e avaliar expressões aritméticas em C respeitando a precedência de operadores. | Lógico, Cuidadoso, Detalhista, Rigoroso | Tipos de dados numéricos em C (K1) | Compreender (Explicar, Reconhecer, Diferenciar, Descrever)

---

## 5.3 Competência CT-ENTRADA.3

**Competência CT-ENTRADA.3**  
### Título

Operar corretamente a entrada de dados em C, relacionando tipos de variáveis e especificadores de formato.

### Descrição Textual

Esta competência diz respeito à capacidade de configurar corretamente a leitura de dados em C, compreendendo a relação entre tipos de variáveis e especificadores de formato utilizados em funções como `scanf`. No contexto da tarefa, embora o foco principal seja o rastreamento, o estudante é convidado a refletir sobre a consistência (ou inconsistência) entre declarar variáveis como `float` e utilizar especificadores `%d`, bem como sobre as implicações dessa escolha para a clareza e robustez do programa. Essa competência é fundamental para evitar erros sutis de entrada, garantir previsibilidade na execução do código e favorecer boas práticas de programação.

### Conhecimentos Necessários

**Entrada de dados com `scanf` (K2)**  
- Descrição  
Entendimento do funcionamento de `scanf` na leitura de múltiplos valores, incluindo a ordem de leitura, o uso de ponteiros (`&`) e a associação com variáveis.  
- Bloom: Aplicar  
- Verbos: Utilizar, Configurar, Executar, Implementar

**Tipos de dados e especificadores de formato (K1)**  
- Descrição  
Compreensão da correspondência correta entre tipos (`int`, `float` etc.) e especificadores (`%d`, `%f`), reconhecendo riscos de inconsistência e suas consequências.  
- Bloom: Analisar  
- Verbos: Analisar, Verificar, Avaliar, Diagnosticar

**Boas práticas de programação e clareza (K8)**  
- Descrição  
Reconhecimento da importância de escrever código legível e robusto, incluindo a escolha adequada de tipos e formatos, para reduzir erros de execução e facilitar a manutenção.  
- Bloom: Avaliar  
- Verbos: Julgar, Justificar, Recomendar, Criticar

### Disposições

Cuidadoso, Responsável, Rigoroso, Crítico.

### BNCC – Alinhamento

- Eixo: Pensamento Computacional (PC).  
- Código: EM13CO03 (Pensamento Computacional) – investigar problemas e manipular dados por meio de procedimentos computacionais.  
- Competência Geral de Computação: Competência Geral 3 – Produzir soluções computacionais com atenção à precisão e à confiabilidade dos dados.

### Tabela Resumo da Competência CT-ENTRADA.3

Código | Competência | Disposição | Conhecimento | Habilidade
---|---|---|---|---
CT-ENTRADA.3 | Operar corretamente a entrada de dados em C, relacionando tipos de variáveis e especificadores de formato. | Cuidadoso, Responsável, Rigoroso, Crítico | Entrada de dados com `scanf` (K2) | Aplicar (Utilizar, Configurar, Executar, Implementar)
CT-ENTRADA.3 | Operar corretamente a entrada de dados em C, relacionando tipos de variáveis e especificadores de formato. | Cuidadoso, Responsável, Rigoroso, Crítico | Tipos de dados e especificadores de formato (K1) | Analisar (Analisar, Verificar, Avaliar, Diagnosticar)
CT-ENTRADA.3 | Operar corretamente a entrada de dados em C, relacionando tipos de variáveis e especificadores de formato. | Cuidadoso, Responsável, Rigoroso, Crítico | Boas práticas de programação e clareza (K8) | Avaliar (Julgar, Justificar, Recomendar, Criticar)

---


# 6 - Conclusão

A entidade instrucional analisada, centrada na simulação de um programa em C para determinação do estado final de variáveis, constitui um recurso didático relevante para o desenvolvimento de competências fundamentais em Computação. Ao exigir que o estudante rastreie a execução linha a linha, interprete expressões aritméticas com precisão, reflita sobre a relação entre tipos e especificadores de formato e justifique a alternativa escolhida em uma questão de múltipla escolha, a tarefa favorece a construção de um entendimento profundo sobre o funcionamento de programas imperativos simples.

O relatório CSP aqui apresentado explicita, de forma estruturada, os conhecimentos mobilizados (K1–K8), os objetivos de aprendizagem (LO1–LO5) e um conjunto de competências de Computação (CT-RASTREIO.1, CT-EXPRESSOES.2, CT-ENTRADA.3) diretamente ancoradas na tarefa. Essa explicitação permite que o professor:

- utilize o CSP no **planejamento didático**, articulando a tarefa com outras atividades que aprofundem ou ampliem as mesmas competências;
- derive a partir do CSP **instrumentos de avaliação** mais precisos, como rubricas e critérios de correção que considerem não apenas o resultado final, mas também o processo de rastreamento, a clareza do raciocínio e a análise crítica do código;
- empregue o CSP como base para **sistemas de recomendação ou trilhas personalizadas**, em que a informação sobre o desempenho do estudante em cada competência possa orientar a indicação de novas tarefas, materiais de apoio ou atividades de remediação.

Dessa forma, o relatório CSP contribui para uma visão mais fina e orientada a competências do processo de ensino-aprendizagem em programação, favorecendo práticas pedagógicas que valorizam não apenas o acerto da resposta, mas a qualidade do raciocínio computacional desenvolvido pelos estudantes.
