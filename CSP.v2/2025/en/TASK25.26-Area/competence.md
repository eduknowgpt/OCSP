# RELATÓRIO DE ESPECIFICAÇÃO DE COMPETÊNCIAS (CSP REPORT)

## TASK 12.4 --- Classificação e Cálculo de Área de Polígonos Regulares (3--5 lados)

------------------------------------------------------------------------

## 0. Inferências Realizadas

**Inferência 1 -- Público-alvo:** estudantes de Introdução à Programação
no 1º semestre.\
**Justificativa:** exige condicionais simples e fórmulas geométricas
básicas.

**Inferência 2 -- Linguagem:** linguagem imperativa comum.\
**Justificativa:** I/O e condicionais são universais.

**Inferência 3 -- Validação:** entradas devem ser positivas e
adequadas.\
**Justificativa:** "validar adequação ao contexto".

**Inferência 4 -- Reentrada em caso de erro:** o programa solicita
novamente entradas inválidas.\
**Justificativa:** prática pedagógica padrão.

**Inferência 5 -- Fórmulas geométricas utilizadas:**\
- Triângulo equilátero: A = (l\^2 \* sqrt(3)) / 4\
- Quadrado: A = l\^2

**Inferência 6 -- Triângulo é sempre equilátero.**

**Inferência 7 -- Saída padronizada.**

**Inferência 8 -- Número de lados determina classificação.**

**Inferência 9 -- Cálculo somente para 3 e 4 lados.**

**Inferência 10 -- Tratamento de tipos numéricos:** inteiro e real.

**Inferência 11 -- Apenas um polígono por execução.**

**Inferência 12 -- Escala 0--100 para proficiência.**

**Inferência 13 -- Uso obrigatório da BNCC + CC2020 + CC2023.**

**Inferência 14 -- Conjunto final de competências:**\
- validação de dados\
- condicionais\
- classificação\
- cálculo geométrico

------------------------------------------------------------------------

## 1. Análise de Entidades Instrucionais

### 1.1 Título da Tarefa

TASK 12.4 --- Classificação e Cálculo de Área de Polígonos Regulares
(3--5 lados)

### 1.2 Descrição Completa da Tarefa

O programa deve ler a quantidade de lados (3--5) e o valor do lado,
validar ambas as entradas, classificar o polígono e calcular a área
quando aplicável. Triângulos equiláteros e quadrados têm área calculada;
pentágonos apenas são identificados.

### 1.3 Processo de Desenvolvimento Esperado

1.  Ler número de lados.\
2.  Validar intervalo.\
3.  Ler medida do lado.\
4.  Validar positividade.\
5.  Classificar o polígono.\
6.  Calcular área (se aplicável).\
7.  Exibir saída padronizada.

### 1.4 Resultados Esperados

-   Classificação correta do polígono.\
-   Aplicação das fórmulas geométricas.\
-   Erros tratados adequadamente.\
-   Saída clara e consistente.

### 1.5 Contexto de Aquisição

Aula de Introdução à Programação.

### 1.6 Perfil do Público-Alvo

Estudantes iniciantes em computação.

### 1.7 Escala de Proficiência

0--100.

------------------------------------------------------------------------

## 2. Enumeração de Conhecimento

### Fundamentos Computacionais

-   Condicionais (if, elif, else)\
-   Tipos numéricos\
-   Entrada e saída\
-   Validação de dados

### Fundamentos Matemáticos

-   Polígonos regulares\
-   Fórmulas geométricas de área

### Pensamento Computacional (BNCC)

-   Decomposição\
-   Modelagem algorítmica

### CC2020

-   Algorithmic Thinking\
-   Control Flow Structures

### CC2023

-   Mathematical & Analytical Foundations\
-   Data Validation and Representation

------------------------------------------------------------------------

## 3. Objetivos de Aprendizagem

### Objetivo Geral

Construir um programa que classifique polígonos e calcule áreas usando
condicionais e validação.

### Objetivos Específicos

-   Aplicar estruturas condicionais\
-   Analisar entradas numéricas\
-   Criar soluções integrando matemática e programação\
-   Implementar fórmulas geométricas\
-   Padronizar saídas computacionais

------------------------------------------------------------------------

## 4. Definição das Competências (com BNCC)

------------------------------------------------------------------------

### 4.1 Competência CT12.4.1 --- Validar Dados Numéricos para Processamento Geométrico

#### Descrição

Avaliar a integridade dos dados fornecidos pelo usuário, garantindo que
respeitam limites e coerência geométrica.

#### Habilidades BNCC Relacionadas

-   **EF06CO01 ---** Classificar informações e tipos de dados.\
-   **EF06CO05 ---** Identificar entradas, saídas e tipos de dados
    necessários.

#### Disposições

Rigor, precisão, atenção aos detalhes.

#### Tabela-Resumo

  Código     Conhecimento   Habilidade   Disposição   BNCC
  ---------- -------------- ------------ ------------ --------------------
  CT12.4.1   Validação      Analisar     Rigor        EF06CO01, EF06CO05

------------------------------------------------------------------------

### 4.2 Competência CT12.4.2 --- Aplicar Estruturas Condicionais para Controlar o Fluxo de Execução

#### Descrição

Traduzir regras geométricas e lógicas em estruturas condicionais que
organizam o fluxo do programa.

#### Habilidades BNCC Relacionadas

-   **EF06CO02 ---** Elaborar algoritmos com seleção (condicionais).\
-   **EF15CO02 ---** Construir e simular algoritmos com sequências e
    seleções condicionais.

#### Disposições

Consistência lógica, clareza, objetividade.

#### Tabela-Resumo

  Código     Conhecimento   Habilidade   Disposição   BNCC
  ---------- -------------- ------------ ------------ --------------------
  CT12.4.2   Condicionais   Aplicar      Clareza      EF06CO02, EF15CO02

------------------------------------------------------------------------

### 4.3 Competência CT12.4.3 --- Classificar Polígonos Regulares por Regras Determinísticas

#### Descrição

Mapear número de lados para categorias formais de polígonos.

#### Habilidades BNCC Relacionadas

-   **EF06CO01 ---** Classificação de dados.\
-   **EF06CO05 ---** Identificação de entradas/saídas relevantes.\
-   **EF15CO02 ---** Construção de algoritmos com condicionais.

#### Disposições

Sistematicidade, precisão, clareza categorial.

#### Tabela-Resumo

  ----------------------------------------------------------------------------
  Código     Conhecimento        Habilidade       Disposição       BNCC
  ---------- ------------------- ---------------- ---------------- -----------
  CT12.4.3   Geometria           Diferenciar      Precisão         EF06CO01,
                                                                   EF06CO05,
                                                                   EF15CO02

  ----------------------------------------------------------------------------

------------------------------------------------------------------------

### 4.4 Competência CT12.4.4 --- Implementar Cálculo Geométrico Computacional

#### Descrição

Converter fórmulas matemáticas em operações computacionais corretas e
eficientes.

#### Habilidades BNCC Relacionadas

-   **EF06CO03 ---** Descrever e implementar soluções computacionais.\
-   **EF06CO04 ---** Decompor e automatizar soluções computacionais.\
-   **EF15CO02 ---** Construção e simulação de algoritmos.

#### Disposições

Exatidão, meticulosidade, raciocínio matemático.

#### Tabela-Resumo

  ----------------------------------------------------------------------------
  Código     Conhecimento        Habilidade       Disposição       BNCC
  ---------- ------------------- ---------------- ---------------- -----------
  CT12.4.4   Geometria           Calcular         Exatidão         EF06CO03,
             Computacional                                         EF06CO04,
                                                                   EF15CO02

  ----------------------------------------------------------------------------

------------------------------------------------------------------------

## 5. Conclusão

A tarefa desenvolve competências fundamentais de programação iniciante:
validação, lógica condicional, classificação e cálculo geométrico. As
competências estão diretamente alinhadas às habilidades da BNCC
(EF06CO01--06 e EF15CO02) e integram conhecimentos de CC2020 e CC2023,
formando uma base sólida de raciocínio algorítmico e modelagem
computacional.
