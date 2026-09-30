# RELATÓRIO CSP – Sistema de Notificação de Poluição Industrial

## Introdução

Este relatório apresenta a especificação completa de competências (Competency Specification Protocol — CSP) relacionadas à tarefa de programação na qual o estudante deve implementar, em linguagem C, um sistema capaz de interpretar um índice de poluição ambiental e emitir notificações para diferentes grupos industriais. Trata-se de uma tarefa centrada na aplicação de **estruturas condicionais**, **interpretação de faixas numéricas**, **lógica de decisão** e **comunicação algorítmica precisa**, constituindo um problema representativo para o desenvolvimento de competências fundamentais de Computação.

A análise segue rigorosamente o modelo metodológico adotado no projeto, estruturando os elementos da Entidade Instrucional, seus conhecimentos, objetivos de aprendizagem e competências computacionais formalizadas. Cada competência é apresentada com sua descrição textual, conhecimentos necessários (com Bloom, verbos e descrição), disposições e alinhamentos à BNCC, além de uma tabela resumo conforme especificado.



# 1. Análise da Entidade Instrucional

A tarefa consiste em desenvolver um programa em C que:

1. **Leia um índice de poluição** medido pela Secretaria de Meio Ambiente.
2. **Compare** esse valor a um conjunto de faixas regulatórias.
3. **Determine** quais grupos industriais (1º, 2º e 3º) devem suspender suas atividades.
4. **Emita mensagens adequadas** conforme o nível de poluição.

Esse problema exige dos estudantes:

- Interpretação de condições e limites numéricos;
- Construção de estruturas condicionais múltiplas e encadeadas;
- Organização lógica do fluxo de decisão;
- Clareza na formulação algorítmica;
- Rigor na escolha da ordem das comparações.

Do ponto de vista pedagógico, a tarefa mobiliza competências de **raciocínio lógico**, **estruturação de decisões**, **modelagem algorítmica** e **tratamento de entradas e saídas**, favorecendo o desenvolvimento de pensamento computacional e autonomia na resolução de problemas.



# 2. Enumeração dos Conhecimentos

K1 — Representação de dados numéricos em C  
K2 — Leitura de entrada padrão e comunicação textual  
K3 — Estruturas condicionais simples e compostas  
K4 — Comparações e operadores relacionais  
K5 — Modelagem de faixas numéricas (intervalos)  
K6 — Organização sequencial da lógica de decisão  
K7 — Construção e comunicação de algoritmos  
K8 — Validação e teste com múltiplas entradas  

---

# 3. Objetivos de Aprendizagem

1. Interpretar um problema real e convertê-lo em regras algorítmicas formais.  
2. Utilizar corretamente variáveis numéricas e instruções de entrada/saída.  
3. Empregar estruturas condicionais múltiplas para apoiar decisões computacionais.  
4. Identificar e ordenar adequadamente condições sobre intervalos.  
5. Construir algoritmos coerentes, organizados e comunicados com precisão.  
6. Testar e validar programas considerando casos típicos e limites.  
7. Relacionar decisões computacionais com cenários sociais e ambientais aplicados.  

---

# 4. Especificação das Competências (CSP)

## Competência 1 - 25.11.1

### Título
Interpretar requisitos e modelar regras de decisão baseadas em faixas numéricas.

### Descrição Textual
Esta competência envolve a capacidade de compreender requisitos de um problema contextualizado, identificar faixas numéricas relevantes e modelar regras de decisão algorítmica com base em limites. O estudante deve interpretar corretamente cenários reais e transformá-los em condições de decisão precisas, fundamentadas em operadores relacionais e na lógica das faixas de valores.

### Conhecimentos Necessários

**Modelagem de Faixas Numéricas**  
- Descrição: Compreender limites inferiores e superiores, sobreposições e intervalos críticos.  
- Bloom: Analisar  
- Verbos: Diferenciar, Classificar, Determinar  

**Operadores Relacionais**  
- Descrição: Aplicar operadores (`>=`, `<=`, `>`, `<`) para representar regras de decisão.  
- Bloom: Aplicar  
- Verbos: Aplicar, Utilizar, Executar  

**Interpretação de Requisitos Algorítmicos**  
- Descrição: Extrair regras formais a partir de um enunciado textual contextualizado.  
- Bloom: Compreender  
- Verbos: Explicar, Descrever, Identificar  

### Disposições
- Analítico  
- Responsável  
- Preciso  

### BNCC – Alinhamento
- EM13CO01  
- Competência Geral 1 de Computação  

### Tabela Resumo

Código | Competência | Disposição | Conhecimento | Habilidade  
-----|------------|--------------|-----------|-------  
25.11.1 | Interpretar requisitos e modelar regras de decisão | Analítico, Responsável, Preciso | Modelagem de Faixas Numéricas | Analisar (Diferenciar, Classificar, Determinar)  
. |  |  | Operadores Relacionais | Aplicar (Aplicar, Utilizar, Executar)  
. |  |  | Interpretação de Requisitos | Compreender (Explicar, Descrever, Identificar)  

---

## Competência 2 - 25.11.2

### Título
Construir estruturas condicionais corretas e ordenadas para tomada de decisão.

### Descrição Textual
Esta competência concentra-se na habilidade de estruturar decisões condicionais múltiplas, garantindo coerência e ordem lógica entre os testes. O estudante deve compreender a dependência entre condições, evitar conflitos e assegurar que o programa execute a resposta correta para cada intervalo de valores.

### Conhecimentos Necessários

**Estruturas Condicionais Encadeadas**  
- Descrição: Aplicação de `if`, `else if`, `else` em cenários com múltiplas decisões.  
- Bloom: Aplicar  
- Verbos: Implementar, Utilizar, Operacionalizar  

**Ordem Lógica das Condições**  
- Descrição: Identificar a importância da ordenação dos testes e seus impactos no resultado.  
- Bloom: Analisar  
- Verbos: Avaliar, Comparar, Justificar  

**Coerência Lógica**  
- Descrição: Garantir que as condições sejam mutuamente consistentes e exaustivas.  
- Bloom: Avaliar  
- Verbos: Verificar, Validar, Revisar  

### Disposições
- Rigoroso  
- Atento  
- Metódico  

### BNCC – Alinhamento
- EM13CO03  
- Competência Geral 3 de Computação  

### Tabela Resumo

Código | Competência | Disposição | Conhecimento | Habilidade  
-----|------------|--------------|-----------|-------  
25.11.2 | Construir estruturas condicionais | Rigoroso, Atento, Metódico | Estruturas Condicionais Encadeadas | Aplicar (Implementar, Utilizar, Operacionalizar)  
. |  |  | Ordem Lógica das Condições | Analisar (Avaliar, Comparar, Justificar)  
. |  |  | Coerência Lógica | Avaliar (Verificar, Validar, Revisar)  

---

## Competência 3 - 25.11.3

### Título
Validar e testar programas empregando casos típicos e limites críticos.

### Descrição Textual
Esta competência abrange a capacidade de avaliar o comportamento do programa mediante entradas variadas, especialmente aquelas nos limites das faixas de decisão. O estudante deve identificar casos de borda, validar a lógica implementada e justificar os resultados obtidos, assegurando que as respostas estejam alinhadas ao comportamento esperado.

### Conhecimentos Necessários

**Testes e Casos de Borda**  
- Descrição: Reconhecer valores críticos (0,29; 0,30; 0,40; 0,50) e compreender sua relevância.  
- Bloom: Analisar  
- Verbos: Testar, Identificar, Diagnosticar  

**Validação de Saída**  
- Descrição: Verificar se as mensagens emitidas correspondem às regras definidas.  
- Bloom: Avaliar  
- Verbos: Verificar, Confirmar, Validar  

**Rastreio e Justificação da Lógica**  
- Descrição: Explicar o caminho de execução e justificar decisões computacionais.  
- Bloom: Criar  
- Verbos: Explicar, Argumentar, Justificar  

### Disposições
- Reflexivo  
- Crítico  
- Responsável  

### BNCC – Alinhamento
- EM13CO05  
- Competência Geral 5 de Computação  

### Tabela Resumo

Código | Competência | Disposição | Conhecimento | Habilidade  
-----|------------|--------------|-----------|-------  
25.11.3 | Validar e testar programas | Reflexivo, Crítico, Responsável | Testes e Casos de Borda | Analisar (Testar, Identificar, Diagnosticar)  
. |  |  | Validação de Saída | Avaliar (Verificar, Confirmar, Validar)  
. |  |  | Rastreio e Justificação da Lógica | Criar (Explicar, Argumentar, Justificar)  

---

# 5. Conclusão

A tarefa analisada promove o desenvolvimento de competências essenciais à formação em Computação, articulando raciocínio lógico, interpretação de dados reais, domínio de estruturas condicionais e rigor analítico. O relatório CSP sistematiza essas competências de forma alinhada à BNCC e ao modelo utilizado nos documentos anteriores do projeto.

O conjunto de competências aqui especificado fundamenta práticas pedagógicas voltadas à autonomia, precisão e responsabilidade no desenvolvimento de soluções computacionais, consolidando a aprendizagem tanto técnica quanto formativa.