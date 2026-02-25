# Relatório CSP — Autoria de Competências (Competency Authoring)

**Código da Task:** TASK25.20  
**Título:** Rastreamento de Estado de Variáveis em Atribuições Sequenciais (C)  
**Nível/Curso:** Curso Técnico em Informática (ou nível introdutório equivalente)  
**Componente Curricular:** Lógica de Programação / Programação Estruturada  
**Contexto:** resolução individual; registro escrito (trace/tabela); avaliação individual sem apresentação oral  
**Escala de proficiência:** 0–10 (incremento 0,1)  
**Alinhamento BNCC:** não aplicável (não solicitado nesta task)



## Introdução
Este relatório corresponde à fase de **Autoria de Competências** do CSP, na qual a tarefa instrucional é analisada para explicitar **conhecimentos (K)**, **objetivos de aprendizagem (LO)** e **competências (CT)** no formato **Conhecimento–Habilidade–Disposição (K–S–D)**.

A tarefa exige que o estudante acompanhe a execução sequencial de um trecho em C, produzindo um **trace do estado (A, B, C, D) após cada instrução**, selecionando a alternativa correta e apresentando **justificativa breve** baseada no registro. Esses produtos tornam a evidência observável porque permitem verificar: (i) correção do resultado final, (ii) consistência passo a passo e (iii) coerência entre raciocínio e resposta.

A tarefa suporta o modelo K–S–D porque mobiliza: (a) conhecimentos de domínio (atribuição, estado, execução sequencial, avaliação de expressões e números decimais), (b) habilidades de análise e representação (rastrear estado, calcular, comparar alternativas, justificar) e (c) disposições verificáveis na forma de trabalho (rigor, atenção a detalhes, compromisso com verificabilidade), sem misturar disposições como se fossem conhecimento.


# 1. Análise da Entidade Instrucional

## Título
Rastreamento de Estado de Variáveis em Atribuições Sequenciais (C)

## Descrição
A tarefa solicita determinar o estado final de quatro variáveis após executar, conceitualmente, um trecho em C com atribuições sucessivas e expressões aritméticas. A evidência principal é um **registro sequencial do estado** `(A, B, C, D)` após cada instrução, complementado por **seleção de alternativa** e **justificativa breve** ancorada no trace.

## Processo de Desenvolvimento da Solução (em etapas)
1. Registrar o estado inicial `(A, B, C, D)` conforme valores fornecidos no enunciado.
2. Executar as instruções em ordem, identificando a variável alterada em cada linha.
3. Quando houver expressões, calcular usando os **valores vigentes naquele ponto**.
4. Registrar o estado completo `(A, B, C, D)` após cada instrução, sem saltos.
5. Consolidar o estado final e comparar com as alternativas para selecionar a correspondente.
6. Revisar o trace para evitar inconsistências (uso indevido de valores antigos após sobrescrita).

## Resultados Esperados (lista de produtos e evidências)
- Alternativa marcada (resposta final).
- Trace/tabela com o estado completo `(A, B, C, D)` após cada instrução.
- Justificativa breve (1–3 linhas) baseada no trace.

## Contexto de Aquisição (curso, organização, ambiente, avaliação)
- **Curso/Nível:** técnico em Informática (ou introdutório equivalente).
- **Organização:** individual.
- **Ambiente:** registro escrito (papel ou meio digital equivalente).
- **Avaliação:** individual, escrita, sem apresentação oral; baseada no conjunto trace + alternativa + justificativa.

## Perfil do Público-Alvo (nível, pré-requisitos, necessidades)
- **Nível:** estudantes em fase inicial de programação estruturada.
- **Pré-requisitos:** variável e atribuição; execução sequencial; operações aritméticas e prioridade; interpretação de resultados decimais.
- **Necessidades típicas:** reduzir erros de rastreio (saltos, troca de variáveis, uso de valores não vigentes) e fortalecer a verificação por evidência.

## Escala de Proficiência (critérios e dimensões)
**Escala 0–10 (0,1), em três dimensões observáveis na própria entrega:**
- **Dimensão Técnica:** correção do estado final e consistência do trace com os cálculos.
- **Dimensão Cognitiva:** compreensão demonstrada por justificativa coerente (sobrescrita, valores vigentes, avaliação de expressões).
- **Dimensão Atitudinal:** legibilidade e auditabilidade do trace; compromisso com resposta baseada em evidência.

**Faixas sintéticas:**
- **0–2,9:** trace ausente/incoerente; resposta sem base verificável.
- **3–4,9:** trace parcial com lacunas; inconsistências relevantes.
- **5–6,9:** trace completo com pequenos deslizes; justificativa suficiente.
- **7–8,9:** trace consistente e claro; justificativa alinhada ao registro.
- **9–10:** alta precisão; trace altamente auditável; justificativa concisa e robusta.



# 2. Enumeração de Conhecimentos

## Fundamentos de Estado e Execução
**K1 — Estado de variáveis em algoritmos imperativos**
- Compreender que variáveis mantêm valores que podem ser atualizados ao longo da execução.
- Entender que o conjunto de valores das variáveis caracteriza o “estado” do programa em um instante.
- Relacionar mudanças de estado às instruções executadas.

**K2 — Semântica da atribuição**
- Entender que a atribuição substitui o valor anterior da variável-alvo.
- Compreender que a expressão à direita é avaliada antes da atualização da variável.
- Reconhecer que o valor sobrescrito deixa de ser o valor vigente.

**K3 — Execução sequencial de instruções**
- Compreender que instruções são executadas na ordem em que aparecem.
- Entender que cada instrução altera o estado que servirá de base para a próxima.
- Reconhecer dependências temporais entre leituras e escritas de variáveis.

## Expressões e Dependências
**K4 — Avaliação de expressões aritméticas**
- Conhecer regras de precedência e associatividade de operadores aritméticos.
- Entender que subexpressões são avaliadas antes da atribuição do resultado.
- Reconhecer que expressões utilizam valores vigentes no momento da avaliação.

**K5 — Dependência entre variáveis**
- Compreender que o valor de uma variável pode depender do valor atual de outra.
- Reconhecer efeitos de reatribuições encadeadas ao longo das instruções.
- Identificar propagação de valores em sequências de atribuição.

## Representação Numérica
**K6 — Tipos numéricos e representação em ponto flutuante**
- Entender que variáveis em ponto flutuante podem produzir resultados decimais.
- Reconhecer implicações de operações (como divisão) na geração de valores não inteiros.

### Nota Analítica
Os conhecimentos K1–K6 são diretamente mobilizados pela tarefa e aparecem como requisitos de raciocínio no trace, no cálculo de expressões e na validação da alternativa. Elementos como “construir o trace” e “justificar” são tratados como **habilidades** nas competências; organização/legibilidade e compromisso com evidência permanecem como **disposições**, preservando a separação K–S–D.

---

# 3. Identificação de Objetivos de Aprendizagem

**LO1 — Rastrear o estado das variáveis em execução sequencial**  
Rastrear, com precisão, o estado `(A, B, C, D)` após cada instrução, mantendo coerência temporal e respeitando sobrescrita.

**LO2 — Avaliar expressões aritméticas com regras formais**  
Aplicar regras de precedência/associatividade e usar valores vigentes para calcular corretamente as expressões do trecho, registrando resultados (inclusive decimais quando pertinentes).

**LO3 — Determinar e validar o estado final por comparação com alternativas**  
Consolidar o estado final obtido no trace e validar por comparação direta com as alternativas fornecidas.

**LO4 — Justificar a alternativa selecionada com base no trace**  
Produzir justificativa breve que sustente a escolha da alternativa por evidências explícitas do registro.

### Nota Analítica
Os LOs preservam observabilidade e coerência com evidências da tarefa (trace, alternativa, justificativa), evitando objetivos atitudinais disfarçados. Em Bloom revisada, LO1/LO2 priorizam **Aplicar** e **Analisar**; LO3/LO4 enfatizam **Avaliar** (validar por comparação e sustentar por evidências).

---

# 4. Definição de Competências

## 4.1 Competência Geral (BNCC – quando aplicável)
**Competência geral do domínio (Computação):**  
Analisar a execução de algoritmos expressos em uma linguagem de programação, modelando o **estado de variáveis** ao longo do tempo, avaliando **expressões** de forma formal e **verificando** a correção do comportamento observado por meio de rastreamento (trace) e explicação baseada em evidências.

**Referência BNCC Computação (nível de alinhamento):**  
Esta tarefa se correlaciona principalmente ao **Eixo Pensamento Computacional**, em especial aos objetos de conhecimento **Algoritmos** e **Organização e representação da informação**, pois envolve simular execução passo a passo e representar estados de maneira estruturada. Quando for necessário registrar códigos, o alinhamento mais defensável ocorre com **EF15CO01** (representação estruturada) e **EF15CO02** (construir/simular algoritmos), entendidos aqui como referência conceitual (a tarefa está em um curso técnico introdutório).

---

## 4.2 Especificações de Competências

### CT25.20.1 — Modelar estado e execução sequencial em programas imperativos
**Descrição Textual**  
Capacidade de construir e manter um modelo mental coerente do **estado** de um programa imperativo (valores vigentes das variáveis) durante a execução **sequencial**, reconhecendo efeitos de **atribuições** e de dependência temporal entre instruções.

**Especificação de Conhecimentos**
- **K1 (Estado):** compreender estado como o conjunto de valores vigentes das variáveis em um instante.
- **K2 (Atribuição):** compreender sobrescrita e avaliação da expressão antes da atualização da variável-alvo.
- **K3 (Execução sequencial):** compreender que a ordem das instruções determina o estado subsequente.
- **K5 (Dependência entre variáveis):** reconhecer propagação de valores por leituras/escritas entre variáveis.

**Alinhamento com a Taxonomia de Bloom (revisada)**
- **Analisar** (distinguir estados antes/depois e relações de dependência na execução).

**Pareamento Conhecimento–Habilidade**
- K1 → identificar e descrever o estado vigente após cada instrução.
- K2 → inferir efeitos de sobrescrita (o que deixa de ser vigente e o que passa a ser).
- K3 → manter coerência temporal no encadeamento de estados.
- K5 → reconhecer como valores se propagam entre variáveis em atribuições sucessivas.

**Anotação de Verbos**
- modelar, analisar, identificar, inferir, reconhecer

**Especificação de Disposições**
- Rigor ao seguir a ordem de execução.
- Atenção a detalhes (variável-alvo e valor vigente).
- Persistência para manter consistência do modelo de estado.

**Competências Alinhadas à BNCC (quando aplicável)**
- **EF15CO02 (Algoritmos):** a competência operacionaliza a simulação conceitual de algoritmos com foco em sequência e dependências.

**Tabela-Resumo**
| Código | Competência | Disposições | Conhecimento | Habilidade |
|---|---|---|---|---|
| CT25.20.1 | Modelar estado e execução sequencial | rigor; atenção; persistência | K1, K2, K3, K5 | modelar e analisar mudanças de estado |

**Definição de Ativação (Activation Definition)**
- **ActivationConstraint:** obrigatória  
- **ActivationMode:** analítica  
- **ActivationRole:** núcleo  
**Justificativa:** a tarefa depende de compreender como o estado muda a cada linha; sem esse modelo, o rastreamento e o resultado final não se sustentam.

---

### CT25.20.2 — Avaliar expressões aritméticas em contexto de execução (valores vigentes e ponto flutuante)
**Descrição Textual**  
Capacidade de avaliar formalmente expressões aritméticas presentes em atribuições, aplicando precedência/associatividade e utilizando os **valores vigentes** no momento da avaliação, interpretando resultados com **decimais** quando pertinentes.

**Especificação de Conhecimentos**
- **K4 (Expressões):** conhecer regras de precedência/associatividade e avaliação de subexpressões.
- **K3 (Execução sequencial):** compreender que operandos devem refletir o estado vigente do passo corrente.
- **K6 (Ponto flutuante):** compreender que operações podem produzir valores não inteiros e como representá-los.

**Alinhamento com a Taxonomia de Bloom (revisada)**
- **Aplicar** (executar regras formais de avaliação).
- **Analisar** (relacionar expressão ao estado vigente no passo).

**Pareamento Conhecimento–Habilidade**
- K4 → calcular corretamente o valor da expressão conforme regras formais.
- K3 → selecionar operandos corretos (valores vigentes no passo).
- K6 → registrar/interpretar resultados decimais de modo consistente.

**Anotação de Verbos**
- aplicar, calcular, avaliar, verificar, interpretar

**Especificação de Disposições**
- Precisão.
- Autochecagem de cálculos.
- Cuidado com diferenças numéricas sutis (incluindo decimais).

**Competências Alinhadas à BNCC (quando aplicável)**
- **EF15CO02 (Algoritmos):** a avaliação correta de expressões é condição para simular algoritmos e obter resultados coerentes.

**Tabela-Resumo**
| Código | Competência | Disposições | Conhecimento | Habilidade |
|---|---|---|---|---|
| CT25.20.2 | Avaliar expressões em contexto de execução | precisão; autochecagem; cuidado | K4, K3, K6 | calcular e interpretar expressões |

**Definição de Ativação (Activation Definition)**
- **ActivationConstraint:** obrigatória  
- **ActivationMode:** analítica  
- **ActivationRole:** núcleo  
**Justificativa:** o estado final é diretamente determinado por expressões; o erro em precedência, operandos vigentes ou decimais compromete toda a solução.

---

### CT25.20.3 — Simular execução por rastreamento (program tracing) e representar estados intermediários
**Descrição Textual**  
Capacidade de simular a execução passo a passo (program tracing), produzindo um **trace** que represente, após cada instrução, o estado completo `(A, B, C, D)` como evidência da execução concebida.

**Especificação de Conhecimentos**
- **K1 (Estado):** compreender o que constitui o estado a ser representado em cada passo.
- **K2 (Atribuição):** compreender quando e como o estado é atualizado.
- **K3 (Execução sequencial):** compreender a progressão temporal do trace (sem saltos).
- **K5 (Dependência):** reconhecer que registros intermediários devem refletir dependências entre variáveis.

**Alinhamento com a Taxonomia de Bloom (revisada)**
- **Aplicar** (executar o procedimento de rastrear passo a passo).
- **Analisar** (garantir coerência entre transições de estado e instruções).

**Pareamento Conhecimento–Habilidade**
- K3 → ordenar passos e registrar estado após cada instrução.
- K2 → atualizar corretamente o valor da variável-alvo após avaliar a expressão.
- K1 → manter o conjunto de valores como representação do estado vigente.
- K5 → registrar transições coerentes com propagação de valores entre variáveis.

**Anotação de Verbos**
- simular, rastrear, representar, registrar, organizar

**Especificação de Disposições**
- Sistematização (evitar saltos de passo).
- Compromisso com verificabilidade (trace como evidência).
- Consistência ao registrar o estado completo.

**Competências Alinhadas à BNCC (quando aplicável)**
- **EF15CO01 (Organização e representação da informação):** o trace materializa representação estruturada (registro) do estado.
- **EF15CO02 (Algoritmos):** o trace operacionaliza a simulação de algoritmo em execução sequencial.

**Tabela-Resumo**
| Código | Competência | Disposições | Conhecimento | Habilidade |
|---|---|---|---|---|
| CT25.20.3 | Simular execução com trace (tracing) | sistematização; verificabilidade; consistência | K1, K2, K3, K5 | rastrear e representar estados |

**Definição de Ativação (Activation Definition)**
- **ActivationConstraint:** obrigatória  
- **ActivationMode:** construtiva  
- **ActivationRole:** núcleo  
**Justificativa:** a tarefa exige explicitamente a produção do trace; ele é o artefato que torna a execução observável e sustenta a correção do resultado.

---

### CT25.20.4 — Verificar comportamento e explicar resultado com base em evidências do trace
**Descrição Textual**  
Capacidade de verificar a correção do resultado obtido (estado final) e explicar o comportamento do trecho de programa com base em evidências do trace, incluindo a comparação com alternativas e a justificativa breve de mudanças críticas (sobrescrita, dependências e expressões).

**Especificação de Conhecimentos**
- **K1 (Estado):** compreender estado final como consequência do encadeamento de estados intermediários.
- **K2 (Atribuição):** identificar pontos críticos de sobrescrita que justificam transições relevantes.
- **K4 (Expressões):** sustentar resultados de linhas com cálculo formal.
- **K5 (Dependência):** explicar propagação de valores entre variáveis.
- **K6 (Ponto flutuante):** manter consistência ao validar resultados com decimais.

**Alinhamento com a Taxonomia de Bloom (revisada)**
- **Avaliar** (validar correspondência entre estado final e alternativa; checar coerência do trace).
- **Compreender/Analisar** (explicar relações causa–efeito no comportamento do programa).

**Pareamento Conhecimento–Habilidade**
- K1 → consolidar o estado final a partir do trace.
- K6 → comparar valores finais com precisão numérica.
- K2/K5 → explicar transições críticas por sobrescrita e dependências.
- K4 → justificar valores oriundos de expressões com base em cálculos e estado vigente.

**Anotação de Verbos**
- verificar, validar, comparar, explicar, justificar

**Especificação de Disposições**
- Postura de verificação (não aceitar resultado sem evidência).
- Honestidade intelectual (justificar pelo trace, não por suposição).
- Rigor na conferência final.

**Competências Alinhadas à BNCC (quando aplicável)**
- **EF15CO02 (Algoritmos):** a competência incorpora a simulação e a validação do resultado do algoritmo, sustentada por evidência (trace).
- *(Quando se optar por alinhamento sem códigos adicionais:)* a explicação do comportamento é tratada como extensão natural da simulação/validação, sem forçar habilidades não explicitadas na BNCC.

**Tabela-Resumo**
| Código | Competência | Disposições | Conhecimento | Habilidade |
|---|---|---|---|---|
| CT25.20.4 | Verificar e explicar por evidência do trace | verificação; honestidade; rigor | K1, K2, K4, K5, K6 | validar resultado e explicar comportamento |

**Definição de Ativação (Activation Definition)**
- **ActivationConstraint:** obrigatória  
- **ActivationMode:** justificatória  
- **ActivationRole:** núcleo  
**Justificativa:** a tarefa exige seleção de alternativa e justificativa breve; validar e explicar o resultado por evidência do trace caracteriza prática computacional de verificação/compreensão de programa.

---