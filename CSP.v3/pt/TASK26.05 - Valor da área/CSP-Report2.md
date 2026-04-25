# RELATÓRIO CSP — Autoria de Competências

## Introdução

Este relatório situa-se na fase de **Autoria de Competências** do Competency Specification Process (CSP) e tem por finalidade especificar, com rastreabilidade, controle de granularidade e possibilidade de reuso, os **Conhecimentos (K)**, **Objetivos de Aprendizagem (LO)** e **Competências (CT)** mobilizados por uma tarefa introdutória de programação.

A tarefa analisada solicita a construção, em linguagem C, de um programa que leia um valor de entrada associado ao peso informado pelo usuário, verifique se há excedente em relação a um limite definido no enunciado e, quando aplicável, calcule o excesso e a multa correspondente, exibindo os resultados de forma verificável. A atividade elicita evidências observáveis porque exige um **artefato executável**, um **fluxo explícito de entrada–processamento–saída** e uma **justificativa breve** sobre a lógica adotada.

O modelo **Conhecimento–Habilidade–Disposição (K–S–D)** é adequado a esta tarefa porque os conhecimentos podem ser delimitados pelo catálogo da disciplina, as habilidades emergem da modelagem e implementação da solução computacional, e as disposições dizem respeito à precisão, à completude e à verificabilidade do comportamento do programa.

---

# 1. Análise da Entidade Instrucional

## Título
- **Código da Task:** TASKXX.YY *(não informado explicitamente na entrada)*
- **Título:** Cálculo de Excesso de Peso e Multa (Linguagem C)
- **Nível/Curso:** nível introdutório de programação
- **Componente Curricular:** Introdução à Programação
- **Contexto:** atividade individual de programação em C, com produção de solução executável e resultados verificáveis
- **Escala de proficiência:** Inicial, Básico, Proficiente e Avançado

## Descrição
A tarefa requer que o estudante implemente um programa que lê número de lados e medida do lado (cm) e, com base no número de lados, imprima o rótulo do polígono solicitado e, quando exigido, um valor numérico associado ao caso (área). Também exige justificativa breve explicando a regra de decisão aplicada e o que foi impresso.



## Processo de Desenvolvimento da Solução (em etapas)
1. Interpretar a especificação de entradas e saídas (quais valores ler; quais mensagens/valores imprimir).
2. Representar adequadamente os dados de entrada (inteiro para lados; numérico para medida).
3. Estruturar seleção condicional para distinguir os casos previstos (3, 4, 5).
4. Implementar o cálculo numérico **apenas** nos casos em que a especificação exige valor de área.
5. Produzir saída textual e numérica de forma verificável.
6. Executar testes mínimos para os casos previstos e registrar evidências.

## Resultados Esperados (lista de produtos e evidências)
- Código-fonte em C, compilável e executável.
- Leitura correta do valor de entrada.
- Tratamento consistente dos dois cenários previstos pela tarefa.
- Saída com os valores produzidos pelo programa.
- Justificativa breve e tecnicamente coerente sobre a lógica de decisão e os cálculos adotados.

## Contexto de Aquisição (curso, organização, ambiente, avaliação)
- **Curso/nível:** disciplina introdutória de programação, compatível com formação técnica ou início da graduação em Computação.
- **Organização:** realização individual.
- **Ambiente:** laboratório de programação ou atividade avaliativa prática/escrita com entrega do código.
- **Avaliação:** centrada na correção do comportamento do programa, na completude do tratamento dos casos e na clareza da justificativa.

## Perfil do Público-Alvo (nível, pré-requisitos, necessidades)
- **Público-alvo:** estudantes iniciantes em programação.
- **Pré-requisitos mínimos:** noção básica de algoritmo, variáveis, atribuição, operadores aritméticos, operadores relacionais, leitura e impressão de dados.
- **Necessidades pedagógicas típicas:** interpretar corretamente o enunciado, distinguir entrada e saídas, construir a condição de decisão sem ambiguidades e garantir valores definidos em todos os caminhos de execução.

## Escala de Proficiência (critérios e dimensões)

### Nível 1 — Inicial
A solução apresenta falhas na interpretação do problema, na formulação da condição, nas atribuições ou nos cálculos, comprometendo a coerência entre entrada, processamento e saída.

### Nível 2 — Básico
A solução contempla a estrutura geral do problema, mas ainda apresenta fragilidades em um ou mais aspectos, como escolha de variáveis/tipos, tratamento incompleto dos casos ou inconsistências na saída.

### Nível 3 — Proficiente
A solução implementa corretamente a lógica do problema, trata os casos previstos com completude, produz saídas verificáveis e apresenta justificativa breve coerente com o comportamento do programa.

### Nível 4 — Avançado
Além da correção funcional, a solução apresenta rigor técnico, clareza estrutural, boa legibilidade da saída e justificativa precisa sobre a relação entre condição, cálculos e resultados.

---

# 2. Seleção e Enumeração de Conhecimentos (Catálogo K)

## Seleção do subconjunto

### **K02 — Fundamentos práticos da linguagem C (C11) para programação introdutória**
- Estrutura básica de um programa em C para leitura, processamento e impressão.
- Declarações simples, comandos básicos e coerência sintática elementar.
- Relação entre intenção algorítmica e materialização da solução em C.

**Justificativa de mobilização na tarefa:** a atividade exige que a solução seja implementada em linguagem C, no padrão introdutório da disciplina.

### **K03 — Variáveis, constantes e tipos primitivos**
- Representação de valores simples por identificadores.
- Atribuição e atualização de valores ao longo da execução.
- Escolha de tipos coerentes para dados de entrada e resultados numéricos.

**Justificativa de mobilização na tarefa:** o problema exige representar a entrada, o excesso e a multa, com atribuições consistentes em todos os caminhos de execução.

### **K04 — Expressões aritméticas e avaliação**
- Construção de expressões aritméticas com operadores básicos.
- Avaliação de cálculos a partir de valores de entrada e constantes.
- Coerência entre expressão computacional e resultado produzido.

**Justificativa de mobilização na tarefa:** a solução depende de cálculos derivados da entrada para produzir as saídas exigidas.

### **K05 — Expressões lógicas e condições**
- Formulação de sentenças condicionais com operadores relacionais e lógicos.
- Interpretação de verdade/falsidade no controle do fluxo.
- Correspondência entre regra do problema e condição computacional.

**Justificativa de mobilização na tarefa:** o núcleo lógico da atividade está em decidir se o valor informado ultrapassa o limite definido no enunciado.

### **K06 — Estrutura sequencial e E/S básica**
- Organização do programa no fluxo entrada → processamento → saída.
- Leitura de dados e impressão de resultados.
- Coerência entre o que é recebido, processado e exibido.

**Justificativa de mobilização na tarefa:** a solução deve ler um valor, processá-lo e produzir saídas verificáveis de modo ordenado.

### **K07 — Estruturas de seleção**
- Tratamento de caminhos alternativos de execução com base em uma condição.
- Cobertura explícita dos casos verdadeiro e falso.
- Implementação de regras simples de decisão.

**Justificativa de mobilização na tarefa:** a atividade requer tratamento distinto para os cenários “com excesso” e “sem excesso”.

### Nota Analítica
A seleção foi mantida em **seis conhecimentos**, todos pertencentes ao catálogo da disciplina e diretamente relacionados ao comportamento computacional exigido pela tarefa. Foram excluídos conhecimentos relativos a repetição, subprogramas, recursão, tipos estruturados e arquivos, pois não há evidência suficiente de sua mobilização no enunciado analisado.

---

# 3. Identificação de Objetivos de Aprendizagem

**LO1.** Interpretar um problema de programação introdutória, identificando entrada, saídas e regra de decisão computacional.  
**K associados:** (K03, K05, K06)

**LO2.** Selecionar variáveis, constantes e tipos primitivos adequados para representar dados e resultados em uma solução em C.  
**K associados:** (K02, K03)

**LO3.** Construir expressões aritméticas e condições lógicas coerentes com a especificação do problema.  
**K associados:** (K04, K05)

**LO4.** Implementar, em linguagem C, um fluxo de entrada, processamento e saída articulado por estrutura de seleção.  
**K associados:** (K02, K06, K07)

**LO5.** Produzir uma solução completa, com valores definidos em todos os caminhos de execução e resultados verificáveis.  
**K associados:** (K03, K04, K06, K07)

### Nota Analítica
Os LOs foram formulados de modo reutilizável, evitando aderência excessiva ao enunciado específico. Em termos de observabilidade, eles podem ser evidenciados pelo código, pela saída produzida e pela justificativa breve. Em Bloom revisada, predominam **Aplicar** e **Criar**, com presença de **Analisar** na interpretação do problema e na coerência entre condição, cálculo e comportamento observado.

---

# 4. Definição de Competências

## 4.1 Competência Geral (BNCC – quando aplicável)

**Competência geral do domínio:**  
Mobilizar fundamentos de programação imperativa para representar dados, formalizar regras de decisão, implementar processamento numérico e produzir saídas verificáveis em linguagem C.

**Alinhamento geral com BNCC:**  
A tarefa se alinha, em nível geral, às competências de Computação voltadas a **aplicar princípios e técnicas da Computação para identificar problemas e criar soluções computacionais** e a **avaliar soluções e processos envolvidos na resolução computacional de problemas**.

---

## 4.2 Especificações de Competências

### Competência CTXX.YY.1

**Título da Competência**  
Traduzir problemas simples em soluções algorítmicas claras.

**Descrição Textual**  
Interpretar problemas introdutórios de programação, identificando entradas, regras de processamento, condições e saídas, de modo a estruturar uma solução algorítmica coerente e implementável em diferentes contextos da disciplina.

**Cobertura e rastreabilidade**
- **LOs cobertos:** (LO1, LO3)
- **K mobilizados (Núcleo):** (K03, K05, K06)
- **K mobilizados (Apoio):** (K02)

**Especificação de Conhecimentos**
- **K03 — Variáveis, constantes e tipos primitivos:** sustenta a identificação e representação dos dados relevantes do problema; é diretamente evidenciado na definição das informações de entrada e saída.
- **K05 — Expressões lógicas e condições:** sustenta a explicitação computacional das regras de decisão; é diretamente evidenciado na formulação da condição que distingue os casos.
- **K06 — Estrutura sequencial e E/S básica:** sustenta a organização do encadeamento entre entrada, processamento e saída; é diretamente evidenciado na estrutura geral da solução.
- **K02 — Fundamentos práticos da linguagem C (C11) para programação introdutória:** oferece suporte para expressar a modelagem algorítmica no padrão operacional da disciplina.

==============================================================
**Alinhamento com a Taxonomia de Bloom (revisada)**  
**Analisar / Aplicar**
===============================================================

**Pareamento Conhecimento–Habilidade**

K03 / Aplicar / representar → representar os dados do problema por meio de variáveis e tipos coerentes.  
K05 / Analisar / formular → explicitar computacionalmente a regra de decisão que organiza os casos do problema.  
K06 / Aplicar / organizar → estruturar a relação entre entrada, processamento e saída de forma verificável.  
K02 / Aplicar / expressar → materializar a modelagem no padrão sintático-operacional da linguagem da disciplina.

**Anotação de Verbos (lista)**  
identificar, representar, formular, organizar, estruturar

**Especificação de Disposições (2–4)**
- Precisão conceitual
- Organização lógica
- Coerência

**Competências Alinhadas à BNCC (quando aplicável)**  
Alinhamento geral com competências de Computação relacionadas à formulação de problemas e à estruturação de soluções computacionais.

**Tabela-Resumo**

| Código | Competência | Disposições | Conhecimento | Habilidade |
|---|---|---|---|---|
| CTXX.YY.1 | Traduzir problemas simples em soluções algorítmicas claras | Precisão conceitual; Organização lógica; Coerência | K03 | Aplicar / representar |
| CTXX.YY.1 | Traduzir problemas simples em soluções algorítmicas claras | Precisão conceitual; Organização lógica; Coerência | K05 | Analisar / formular |
| CTXX.YY.1 | Traduzir problemas simples em soluções algorítmicas claras | Precisão conceitual; Organização lógica; Coerência | K06 | Aplicar / organizar |
| CTXX.YY.1 | Traduzir problemas simples em soluções algorítmicas claras | Precisão conceitual; Organização lógica; Coerência | K02 | Aplicar / expressar |

**Definição de Ativação**
- **Restrição de ativação:** obrigatória
- **Modo de ativação:** analítica
- **Função de ativação:** núcleo
- **Justificativa:** a tarefa exige que o estudante interprete o problema e estruture seus elementos computacionais antes de programar. A competência é ativada na identificação de entradas, condições, processamento e saídas como base da solução.

---

### Competência CTXX.YY.2

**Título da Competência**  
Manipular dados e expressões em problemas introdutórios de programação.

**Descrição Textual**  
Representar e manipular dados por meio de tipos primitivos, variáveis e constantes, construindo e avaliando expressões aritméticas e lógicas coerentes com a especificação de problemas computacionais simples.

**Cobertura e rastreabilidade**
- **LOs cobertos:** (LO2, LO3, LO5)
- **K mobilizados (Núcleo):** (K03, K04, K05)
- **K mobilizados (Apoio):** (K02)

**Especificação de Conhecimentos**
- **K03 — Variáveis, constantes e tipos primitivos:** sustenta a representação e atualização dos dados utilizados na solução; é diretamente evidenciado nas declarações e atribuições.
- **K04 — Expressões aritméticas e avaliação:** sustenta a produção de resultados derivados; é diretamente evidenciado nos cálculos implementados.
- **K05 — Expressões lógicas e condições:** sustenta a formulação de relações de comparação e decisão; é diretamente evidenciado nas expressões condicionais usadas no problema.
- **K02 — Fundamentos práticos da linguagem C (C11) para programação introdutória:** oferece suporte sintático para a materialização das variáveis e expressões na linguagem adotada.

**Alinhamento com a Taxonomia de Bloom (revisada)**  
**Aplicar**

**Pareamento Conhecimento–Habilidade**

K03 / Aplicar / manipular → representar e atualizar dados por meio de variáveis, constantes e tipos primitivos coerentes.  
K04 / Aplicar / calcular → construir e avaliar expressões aritméticas compatíveis com os resultados exigidos.  
K05 / Aplicar / comparar → formular expressões lógicas simples para sustentar o comportamento da solução.  
K02 / Aplicar / implementar → materializar variáveis e expressões na linguagem de programação no padrão da disciplina.

**Anotação de Verbos (lista)**  
manipular, representar, calcular, comparar, avaliar, implementar

**Especificação de Disposições (2–4)**
- Precisão
- Rigor
- Consistência

**Competências Alinhadas à BNCC (quando aplicável)**  
Alinhamento geral com competências de Computação ligadas à representação de dados e ao processamento de informações em soluções computacionais.

**Tabela-Resumo**

| Código | Competência | Disposições | Conhecimento | Habilidade |
|---|---|---|---|---|
| CTXX.YY.2 | Manipular dados e expressões em problemas introdutórios de programação | Precisão; Rigor; Consistência | K03 | Aplicar / manipular |
| CTXX.YY.2 | Manipular dados e expressões em problemas introdutórios de programação | Precisão; Rigor; Consistência | K04 | Aplicar / calcular |
| CTXX.YY.2 | Manipular dados e expressões em problemas introdutórios de programação | Precisão; Rigor; Consistência | K05 | Aplicar / comparar |
| CTXX.YY.2 | Manipular dados e expressões em problemas introdutórios de programação | Precisão; Rigor; Consistência | K02 | Aplicar / implementar |

**Definição de Ativação**
- **Restrição de ativação:** obrigatória
- **Modo de ativação:** construtiva
- **Função de ativação:** núcleo
- **Justificativa:** a tarefa demanda manipulação consistente de dados e avaliação de expressões para produzir resultados corretos. A competência é ativada quando o estudante transforma valores de entrada em resultados computáveis e verificáveis.

---

### Competência CTXX.YY.3

**Título da Competência**  
Realizar entrada, processamento e saída de dados de forma consistente.

**Descrição Textual**  
Organizar o fluxo básico de programas introdutórios por meio da leitura de dados, do processamento das informações e da apresentação de resultados verificáveis e coerentes com a especificação do problema.

**Cobertura e rastreabilidade**
- **LOs cobertos:** (LO2, LO4, LO5)
- **K mobilizados (Núcleo):** (K02, K06, K03)
- **K mobilizados (Apoio):** (K04)

**Especificação de Conhecimentos**
- **K02 — Fundamentos práticos da linguagem C (C11) para programação introdutória:** sustenta a implementação executável da solução; é diretamente evidenciado no código produzido.
- **K06 — Estrutura sequencial e E/S básica:** sustenta a articulação entre leitura, processamento e apresentação dos resultados; é diretamente evidenciado no fluxo operacional do programa.
- **K03 — Variáveis, constantes e tipos primitivos:** sustenta o armazenamento e a passagem dos valores ao longo da execução; é diretamente evidenciado na consistência das atribuições e saídas.
- **K04 — Expressões aritméticas e avaliação:** oferece suporte ao processamento numérico necessário para a geração dos resultados exibidos.

**Alinhamento com a Taxonomia de Bloom (revisada)**  
**Aplicar / Criar**

**Pareamento Conhecimento–Habilidade**

K02 / Criar / implementar → materializar a solução em linguagem de programação no padrão da disciplina.  
K06 / Aplicar / articular → articular entrada, processamento e saída de forma verificável.  
K03 / Aplicar / manter → manter dados e resultados coerentes ao longo da execução.  
K04 / Aplicar / produzir → produzir resultados computacionais corretos a partir do processamento implementado.

**Anotação de Verbos (lista)**  
implementar, ler, articular, processar, manter, exibir

**Especificação de Disposições (2–4)**
- Clareza operacional
- Verificabilidade
- Responsabilidade técnica

**Competências Alinhadas à BNCC (quando aplicável)**  
Alinhamento geral com competências de Computação voltadas à implementação de soluções e à comunicação de resultados produzidos computacionalmente.

**Tabela-Resumo**

| Código | Competência | Disposições | Conhecimento | Habilidade |
|---|---|---|---|---|
| CTXX.YY.3 | Realizar entrada, processamento e saída de dados de forma consistente | Clareza operacional; Verificabilidade; Responsabilidade técnica | K02 | Criar / implementar |
| CTXX.YY.3 | Realizar entrada, processamento e saída de dados de forma consistente | Clareza operacional; Verificabilidade; Responsabilidade técnica | K06 | Aplicar / articular |
| CTXX.YY.3 | Realizar entrada, processamento e saída de dados de forma consistente | Clareza operacional; Verificabilidade; Responsabilidade técnica | K03 | Aplicar / manter |
| CTXX.YY.3 | Realizar entrada, processamento e saída de dados de forma consistente | Clareza operacional; Verificabilidade; Responsabilidade técnica | K04 | Aplicar / produzir |

**Definição de Ativação**
- **Restrição de ativação:** obrigatória
- **Modo de ativação:** construtiva
- **Função de ativação:** núcleo
- **Justificativa:** a tarefa só se torna observável quando a solução lê dados, processa informações e apresenta resultados conferíveis. A competência é ativada diretamente no artefato executável e na qualidade verificável da saída.

---

### Competência CTXX.YY.4

**Título da Competência**  
Controlar o fluxo de execução com decisões condicionais.

**Descrição Textual**  
Construir soluções computacionais que utilizem estruturas de decisão e expressões lógicas corretas para tratar casos distintos e produzir comportamento consistente em diferentes cenários de execução.

**Cobertura e rastreabilidade**
- **LOs cobertos:** (LO1, LO3, LO4, LO5)
- **K mobilizados (Núcleo):** (K05, K07, K06)
- **K mobilizados (Apoio):** (K03)

**Especificação de Conhecimentos**
- **K05 — Expressões lógicas e condições:** sustenta a formulação da regra que controla a execução; é diretamente evidenciado na condição construída pelo estudante.
- **K07 — Estruturas de seleção:** sustenta o tratamento de caminhos alternativos; é diretamente evidenciado na implementação dos ramos condicionais.
- **K06 — Estrutura sequencial e E/S básica:** sustenta a inserção da decisão no fluxo global do programa; é diretamente evidenciado na coerência entre condição, processamento e saída.
- **K03 — Variáveis, constantes e tipos primitivos:** oferece suporte à manipulação dos valores que participam da decisão e das saídas associadas.

**Alinhamento com a Taxonomia de Bloom (revisada)**  
**Aplicar**

**Pareamento Conhecimento–Habilidade**

K05 / Aplicar / formular → formular expressões lógicas corretas para controlar o comportamento do programa.  
K07 / Aplicar / selecionar → tratar casos distintos por meio de estruturas de decisão coerentes com a regra do problema.  
K06 / Aplicar / integrar → integrar a decisão ao fluxo de entrada, processamento e saída de maneira verificável.  
K03 / Aplicar / associar → associar os dados manipulados aos diferentes caminhos de execução e aos resultados correspondentes.

**Anotação de Verbos (lista)**  
formular, decidir, selecionar, integrar, associar, controlar

**Especificação de Disposições (2–4)**
- Atenção aos casos
- Completude
- Coerência lógica

**Competências Alinhadas à BNCC (quando aplicável)**  
Alinhamento geral com competências de Computação relacionadas à criação de soluções baseadas em regras, condições e avaliação do comportamento computacional.

**Tabela-Resumo**

| Código | Competência | Disposições | Conhecimento | Habilidade |
|---|---|---|---|---|
| CTXX.YY.4 | Controlar o fluxo de execução com decisões condicionais | Atenção aos casos; Completude; Coerência lógica | K05 | Aplicar / formular |
| CTXX.YY.4 | Controlar o fluxo de execução com decisões condicionais | Atenção aos casos; Completude; Coerência lógica | K07 | Aplicar / selecionar |
| CTXX.YY.4 | Controlar o fluxo de execução com decisões condicionais | Atenção aos casos; Completude; Coerência lógica | K06 | Aplicar / integrar |
| CTXX.YY.4 | Controlar o fluxo de execução com decisões condicionais | Atenção aos casos; Completude; Coerência lógica | K03 | Aplicar / associar |

**Definição de Ativação**
- **Restrição de ativação:** obrigatória
- **Modo de ativação:** analítica/construtiva
- **Função de ativação:** núcleo
- **Justificativa:** a tarefa depende diretamente da distinção entre casos de execução. A competência é ativada tanto na formulação da condição quanto na construção dos ramos que determinam o comportamento final do programa.