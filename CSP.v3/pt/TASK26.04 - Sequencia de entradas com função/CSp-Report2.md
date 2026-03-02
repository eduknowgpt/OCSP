# RELATÓRIO CSP — Autoria de Competências (TASK26.04)

## Introdução
Este relatório situa-se na fase de **Autoria de Competências** do *Competency Specification Process (CSP)* e tem por objetivo especificar, com **alta rastreabilidade** e **sem redundância**, os **Conhecimentos (K)**, **Objetivos de Aprendizagem (LO)** e **Competências (CT)** elicitos por uma tarefa introdutória de programação.

A tarefa **TASK26.04** solicita a construção de um algoritmo/programa que **lê um número n**, recebe **n valores** e calcula, para cada valor, o **fatorial**, com a exigência explícita de que esse cálculo seja realizado por **uma função**. A tarefa produz evidências observáveis porque o estudante entrega um **artefato executável (código/pseudocódigo)**, gera **saídas verificáveis** e apresenta uma **justificativa breve** sobre a organização da solução (especialmente o uso de função).

O modelo **K–S–D** é apropriado porque: (i) a tarefa mobiliza **conhecimentos de Computação** previstos no catálogo da disciplina (entrada/saída, tipos, expressões, repetição e funções), (ii) exige **habilidades** de implementar, modularizar e verificar o comportamento do programa, e (iii) requer **disposições** ligadas a rigor, consistência e verificabilidade para sustentar uma entrega auditável.

---

# 1. Análise da Entidade Instrucional

## Título
**Cálculo de Fatoriais de Múltiplas Entradas com Função (TASK26.04)**

## Descrição
Atividade prática de programação em que o estudante deve processar uma quantidade definida de entradas (n valores) e, para cada uma, produzir o fatorial correspondente, **obrigatoriamente** encapsulando o cálculo em **uma função** e apresentando resultados de forma verificável.

## Processo de Desenvolvimento da Solução (em etapas)
1. **Leitura do parâmetro n** (quantidade de valores a processar).
2. **Leitura repetida** dos valores (n entradas).
3. **Chamada da função de fatorial** para cada valor lido, obtendo o resultado associado.
4. **Emissão de saída** para cada processamento, de modo que seja possível relacionar entrada e resultado.
5. **Verificação mínima** por execução com casos distintos (incluindo um caso com n > 1), registrando evidências de funcionamento.

## Resultados Esperados (produtos e evidências)
- Artefato de solução (programa em C ou pseudocódigo equivalente) contendo:
  - leitura de n;
  - laço para leitura/processamento de n valores;
  - definição e uso de função para fatorial;
  - impressão/registro dos resultados.
- Registros de execução (saídas) demonstrando:
  - processamento de múltiplas entradas;
  - consistência entre valores informados e resultados apresentados.
- Justificativa breve descrevendo o papel da função e a organização do fluxo principal.

## Contexto de Aquisição (curso, organização, ambiente, avaliação)
- **Curso/nível:** disciplina introdutória de programação (nível técnico ou equivalente).
- **Organização:** individual.
- **Ambiente:** laboratório de programação ou atividade prática com execução local.
- **Avaliação:** correção funcional do programa + verificabilidade das saídas + justificativa breve.

## Perfil do Público-Alvo (nível, pré-requisitos, necessidades)
- Estudantes em estágio inicial, com conhecimentos básicos de:
  - leitura/impressão,
  - variáveis e tipos simples,
  - estruturas de repetição,
  - noção inicial de funções.
- Necessidade típica: consolidar **modularização** (função) e **processamento repetido** (n entradas) com resultados conferíveis.

## Escala de Proficiência (critérios e dimensões)
Dimensões observadas: **correção**, **completude**, **modularização por função**, **verificabilidade (testes/saídas)**.

- **N1 — Inicial:** lê parcialmente as entradas e/ou a função não está integrada de forma consistente; saídas não permitem conferência.
- **N2 — Básico:** processa n entradas e usa função, mas com inconsistências (ex.: integração frágil, resultados não confiáveis para alguns casos).
- **N3 — Proficiente:** lê n e processa todos os valores; função de fatorial com responsabilidade clara; resultados consistentes e saídas verificáveis.
- **N4 — Avançado:** além do N3, apresenta evidências de teste mais completas e justificativa técnica concisa e bem fundamentada.

---

# 2. Seleção e Enumeração de Conhecimentos (Catálogo K)

> **Fonte do catálogo:** *Catálogo de Conhecimentos da Disciplina — Introdução à Programação (Univasf)* (anexo).  
> **Regra aplicada:** seleção de subconjunto **sem criação de K novo**.

## Conhecimentos selecionados (subconjunto do catálogo)

**K02 — Fundamentos práticos da linguagem C (C11) para programação introdutória**
- Descrição (ensinável/observável):
  - Expressar soluções introdutórias em C com sintaxe mínima adequada.
  - Organizar o programa conforme convenções essenciais da linguagem.
  - Produzir um artefato compilável/executável no contexto da disciplina.
- Justificativa de mobilização na tarefa: a tarefa demanda implementação em ambiente típico de IP; a evidência principal é um programa funcional.

**K03 — Variáveis, constantes e tipos primitivos**
- Descrição (ensinável/observável):
  - Representar dados de entrada e resultados com tipos primitivos apropriados.
  - Declarar e atualizar variáveis de forma consistente ao longo do processamento.
  - Sustentar coerência entre tipo, operação e saída.
- Justificativa de mobilização na tarefa: o cálculo de fatorial exige manipulação de valores inteiros e controle consistente de variáveis acumuladoras e de entrada.

**K04 — Expressões aritméticas e avaliação**
- Descrição (ensinável/observável):
  - Construir expressões aritméticas coerentes com a intenção do algoritmo.
  - Compreender efeitos da ordem de avaliação em operações e atribuições.
  - Aplicar operações de forma consistente na produção do resultado.
- Justificativa de mobilização na tarefa: o fatorial envolve operações multiplicativas sucessivas e atualização de acumuladores.

**K06 — Estrutura sequencial e E/S básica**
- Descrição (ensinável/observável):
  - Ler dados de entrada e produzir saídas de modo conferível.
  - Organizar o fluxo sequencial de leitura → processamento → escrita.
  - Garantir que a saída corresponda ao processamento realizado.
- Justificativa de mobilização na tarefa: a tarefa depende de leitura de n e de n valores, além de apresentação verificável dos resultados.

**K08 — Estruturas de repetição**
- Descrição (ensinável/observável):
  - Implementar repetição controlada por contagem/condição.
  - Processar coleções de entradas em laços bem definidos.
  - Evitar inconsistências como laços incompletos ou contagens incorretas.
- Justificativa de mobilização na tarefa: é necessário iterar n vezes para ler/processar os valores e produzir resultados correspondentes.

**K10 — Subprogramas: procedimentos e funções**
- Descrição (ensinável/observável):
  - Decompor o problema em subprogramas coesos com parâmetros/retorno.
  - Definir e invocar funções com responsabilidade clara.
  - Promover reuso e facilitar verificação por unidade de comportamento.
- Justificativa de mobilização na tarefa: há exigência explícita de que o cálculo do fatorial seja feito por uma função.

### Nota Analítica (seleção)
A seleção prioriza conhecimentos diretamente exigidos pela tarefa: **entrada/saída**, **controle por repetição**, **expressões aritméticas**, **tipos/variáveis** e **modularização por função**, mantendo o conjunto enxuto (6 itens) e com granularidade compatível com reuso ao longo da disciplina.

---

# 3. Identificação de Objetivos de Aprendizagem

**LO1 — Implementar leitura de n e processamento de n entradas com saída verificável.**  
K associados: (K06, K02)

**LO2 — Definir e integrar uma função para cálculo de resultado por entrada, com parâmetros e retorno coerentes.**  
K associados: (K10, K02, K03)

**LO3 — Aplicar estruturas de repetição para processar múltiplas entradas e sustentar o processamento associado a cada valor.**  
K associados: (K08, K06, K03)

**LO4 — Empregar expressões aritméticas consistentes para atualização de valores intermediários e produção do resultado final.**  
K associados: (K04, K03)

**LO5 — Produzir evidências de verificação (execuções/testes e justificativa breve) que sustentem a correção e a consistência do programa.**  
K associados: (K06, K10, K08)

### Nota Analítica (observabilidade e Bloom)
Os LOs são formulados para reuso (não dependem do enunciado específico além do padrão “processar entradas → produzir saídas”) e são observáveis por: (i) código/pseudocódigo, (ii) saídas geradas, (iii) registros de teste e justificativa breve. Em Bloom revisada, predominam **Aplicar** (uso de repetição, E/S e expressões) e **Criar** quando há implementação/modularização (função integrada ao programa).

---

# 4. Definição de Competências

## 4.1 Competência Geral (BNCC – quando aplicável)
**Competência geral do domínio (Computação):**  
Mobilizar fundamentos de programação para implementar uma solução modular (com funções), processar múltiplas entradas por repetição e produzir saídas verificáveis, sustentando correção e consistência por evidências de execução e justificativa técnica breve.

**BNCC (uso = sim):**  
Como a etapa (EF/EM) não está explicitada no contexto do curso, registra-se apenas alinhamento **em nível geral** com práticas de **pensamento computacional** e **programação/algoritmos** (formalização, decomposição e validação), **sem uso de códigos**.

---

## 4.2 Especificações de Competências

### CT26.04.1
**Título da Competência**  
Modularizar um cálculo por função e integrá-lo ao processamento de múltiplas entradas.

**Descrição Textual (reutilizável; não específica do enunciado)**  
Definir e empregar uma **função** com responsabilidade clara (parâmetros/retorno) para realizar um cálculo, integrando-a ao fluxo principal que lê entradas, aciona o subprograma e apresenta resultados de forma conferível.

**Cobertura e rastreabilidade**
- LOs cobertos: (LO2, LO1)
- K mobilizados (Núcleo): (K10, K06, K02)
- K mobilizados (Apoio): (K03, K04)

**Especificação de Conhecimentos**
- **K10 (Núcleo):** função com parâmetros/retorno e responsabilidade clara; evidência: definição e chamadas coerentes no artefato entregue.
- **K06 (Núcleo):** leitura e emissão de saída compatíveis com o processamento; evidência: entradas processadas e resultados apresentados para conferência.
- **K02 (Núcleo):** expressão do artefato em C (ou equivalente no ambiente); evidência: programa compilável/executável no contexto da disciplina.
- **K03 (Apoio):** uso consistente de variáveis/tipos na passagem de dados e retorno; papel: sustentar integração correta entre função e fluxo.
- **K04 (Apoio):** coerência aritmética no cálculo encapsulado; papel: garantir que o valor retornado seja obtido por operações consistentes.

**Alinhamento com a Taxonomia de Bloom (revisada)**  
**Criar** (implementar e integrar função) + **Aplicar** (usar E/S e chamadas conforme especificação).

**Pareamento Conhecimento–Habilidade**
- (K10 → decompor em função e integrar por chamadas e retorno)
- (K06 → estruturar leitura/processamento/escrita com rastreabilidade)
- (K02 → implementar solução em C com estrutura mínima adequada)

**Anotação de Verbos (lista)**
definir, receber, retornar, chamar, ler, processar, imprimir, integrar.

**Especificação de Disposições (2–4)**
- Rigor na definição de responsabilidades da função (evitar ambiguidade de entradas/saídas).
- Consistência ao relacionar cada entrada ao resultado correspondente.
- Atenção a verificabilidade (saídas claras para conferência).

**Competências Alinhadas à BNCC (quando aplicável)**  
Alinhamento geral com decomposição e formalização de solução algorítmica, sem códigos.

**Tabela-Resumo**

| Código | Competência | Disposições | Conhecimento | Habilidade |
|---|---|---|---|---|
| CT26.04.1 | Modularizar por função e integrar ao fluxo | rigor, consistência, verificabilidade | K10 | definir e integrar função com parâmetros/retorno |
| CT26.04.1 | Modularizar por função e integrar ao fluxo | rigor, consistência, verificabilidade | K06 | ler entradas e apresentar resultados conferíveis |
| CT26.04.1 | Modularizar por função e integrar ao fluxo | rigor, consistência, verificabilidade | K02 | implementar em C no padrão da disciplina |

**Definição de Ativação**
- Restrição de ativação: **obrigatória**
- Modo de ativação: **construtiva**
- Função de ativação: **núcleo**
- Justificativa: a tarefa exige explicitamente que o cálculo seja feito por função e que o programa processe entradas e produza saídas verificáveis; a evidência central é o artefato implementado com chamadas corretas e integração consistente.

---

### CT26.04.2
**Título da Competência**  
Aplicar repetição e atualização aritmética para computação iterativa baseada em entradas.

**Descrição Textual (reutilizável; não específica do enunciado)**  
Empregar **estruturas de repetição** e **expressões aritméticas** para realizar computações iterativas com atualização controlada de variáveis, garantindo consistência do processamento ao longo das iterações.

**Cobertura e rastreabilidade**
- LOs cobertos: (LO3, LO4)
- K mobilizados (Núcleo): (K08, K04, K03)
- K mobilizados (Apoio): (K02)

**Especificação de Conhecimentos**
- **K08 (Núcleo):** laços com contagem/condição coerentes; evidência: iteração correta para processar entradas e/ou etapas de cálculo.
- **K04 (Núcleo):** expressões aritméticas consistentes na atualização de valores; evidência: cálculo acumulativo coerente no resultado apresentado.
- **K03 (Núcleo):** controle de variáveis e tipos durante a repetição; evidência: variáveis inicializadas/atualizadas adequadamente ao longo das iterações.
- **K02 (Apoio):** materialização do laço e das expressões em C; papel: viabilizar a implementação no ambiente da disciplina.

**Alinhamento com a Taxonomia de Bloom (revisada)**  
**Aplicar** (usar laços e expressões) + **Analisar** (assegurar consistência de atualizações ao longo das iterações, quando justificado por testes/checagens).

**Pareamento Conhecimento–Habilidade**
- (K08 → construir repetição controlada e completa)
- (K04 → formular e aplicar atualizações aritméticas consistentes)
- (K03 → manter variáveis/tipos coerentes durante a iteração)

**Anotação de Verbos (lista)**
iterar, atualizar, acumular, calcular, controlar, repetir.

**Especificação de Disposições (2–4)**
- Atenção a consistência de contagem/condição (evitar iterações a mais ou a menos).
- Rigor no controle de atualizações (evitar resultados inconsistentes por erros de estado).
- Persistência na verificação com casos distintos.

**Competências Alinhadas à BNCC (quando aplicável)**  
Alinhamento geral com automatização de procedimentos e validação por casos, sem códigos.

**Tabela-Resumo**

| Código | Competência | Disposições | Conhecimento | Habilidade |
|---|---|---|---|---|
| CT26.04.2 | Repetição + atualização aritmética | atenção, rigor, persistência | K08 | implementar laços completos e corretos |
| CT26.04.2 | Repetição + atualização aritmética | atenção, rigor, persistência | K04 | aplicar expressões aritméticas consistentes |
| CT26.04.2 | Repetição + atualização aritmética | atenção, rigor, persistência | K03 | gerenciar variáveis/tipos durante iterações |

**Definição de Ativação**
- Restrição de ativação: **obrigatória**
- Modo de ativação: **construtiva**
- Função de ativação: **núcleo**
- Justificativa: a tarefa demanda processamento de **n** entradas e cálculo associado; isso exige repetição controlada e atualização aritmética consistente, evidenciada diretamente pelo comportamento do programa e pelas saídas produzidas.

---

### CT26.04.3
**Título da Competência**  
Garantir consistência de dados e saídas ao longo do processamento e das chamadas de função.

**Descrição Textual (reutilizável; não específica do enunciado)**  
Gerenciar **variáveis, tipos e entrada/saída** de forma consistente em um programa com processamento repetido e uso de subprogramas, assegurando que os valores manipulados e apresentados correspondam ao comportamento esperado.

**Cobertura e rastreabilidade**
- LOs cobertos: (LO1, LO4)
- K mobilizados (Núcleo): (K03, K06, K04)
- K mobilizados (Apoio): (K10, K02)

**Especificação de Conhecimentos**
- **K03 (Núcleo):** tipos/variáveis coerentes em leitura, processamento e saída; evidência: ausência de inconsistências observáveis entre entrada e resultado.
- **K06 (Núcleo):** estrutura sequencial e E/S que sustentam rastreabilidade; evidência: cada valor informado tem saída correspondente e compreensível.
- **K04 (Núcleo):** operações aritméticas coerentes com a intenção do cálculo; evidência: atualização consistente refletida no resultado final.
- **K10 (Apoio):** estruturação por função como organização do processamento; papel: sustentar separação de responsabilidades sem confundir fluxo de dados.
- **K02 (Apoio):** implementação em C; papel: garantir que decisões de tipos e E/S sejam expressas corretamente no ambiente adotado.

**Alinhamento com a Taxonomia de Bloom (revisada)**  
**Aplicar** (tipos, E/S, expressões) + **Analisar** (identificar e evitar inconsistências entre dados lidos, processados e exibidos).

**Pareamento Conhecimento–Habilidade**
- (K03 → escolher e manter tipos/variáveis consistentes)
- (K06 → produzir saídas rastreáveis para conferência)
- (K04 → aplicar operações coerentes ao longo do processamento)

**Anotação de Verbos (lista)**
declarar, inicializar, atualizar, ler, imprimir, conferir, manter.

**Especificação de Disposições (2–4)**
- Cuidado com consistência e rastreabilidade (não “perder” a relação entrada→saída).
- Rigor ao evitar estados indefinidos (valores não definidos/atualizações incoerentes).
- Clareza na apresentação de resultados para auditoria.

**Competências Alinhadas à BNCC (quando aplicável)**  
Alinhamento geral com precisão e validação de resultados em processos algorítmicos, sem códigos.

**Tabela-Resumo**

| Código | Competência | Disposições | Conhecimento | Habilidade |
|---|---|---|---|---|
| CT26.04.3 | Consistência de dados e saídas | cuidado, rigor, clareza | K03 | manter variáveis/tipos coerentes |
| CT26.04.3 | Consistência de dados e saídas | cuidado, rigor, clareza | K06 | produzir E/S rastreável e conferível |
| CT26.04.3 | Consistência de dados e saídas | cuidado, rigor, clareza | K04 | aplicar operações aritméticas coerentes |

**Definição de Ativação**
- Restrição de ativação: **obrigatória**
- Modo de ativação: **analítica + construtiva**
- Função de ativação: **núcleo**
- Justificativa: como a evidência é o comportamento do programa e suas saídas, a competência exige tanto construção (implementar) quanto análise (assegurar coerência entre leitura, atualização e impressão) para que os resultados sejam verificáveis.

---

### CT26.04.4
**Título da Competência**  
Verificar o comportamento do programa por evidências de execução e justificativa técnica breve.

**Descrição Textual (reutilizável; não específica do enunciado)**  
Planejar e registrar **evidências mínimas de verificação** (execuções com casos distintos) e apresentar justificativa técnica concisa que sustente a correção do comportamento observado em um programa com repetição e funções.

**Cobertura e rastreabilidade**
- LOs cobertos: (LO5)
- K mobilizados (Núcleo): (K06, K08, K10)
- K mobilizados (Apoio): (K02, K03)

**Especificação de Conhecimentos**
- **K06 (Núcleo):** E/S como base de evidência; evidência: registros de execução que permitam conferência.
- **K08 (Núcleo):** repetição corretamente exercitada em testes (incluindo n > 1); evidência: saídas que demonstram processamento repetido.
- **K10 (Núcleo):** função exercitada por chamadas nos testes; evidência: resultados obtidos via uso efetivo da função.
- **K02 (Apoio):** execução em ambiente C; papel: viabilizar rodar e registrar evidências.
- **K03 (Apoio):** coerência de dados nas execuções; papel: sustentar confiabilidade dos resultados observados.

**Alinhamento com a Taxonomia de Bloom (revisada)**  
**Avaliar** (testar/verificar por evidências) + **Analisar** (justificar coerência do comportamento observado).

**Pareamento Conhecimento–Habilidade**
- (K06 → registrar saídas que sustentem verificação)
- (K08 → selecionar/usar casos que exercitem repetição)
- (K10 → demonstrar uso efetivo de função como unidade de cálculo)

**Anotação de Verbos (lista)**
testar, registrar, verificar, justificar, comparar, evidenciar.

**Especificação de Disposições (2–4)**
- Compromisso com verificabilidade (evidência acima de suposição).
- Postura crítica ao confrontar entrada, execução e resultado.
- Objetividade e clareza na justificativa breve.

**Competências Alinhadas à BNCC (quando aplicável)**  
Alinhamento geral com validação e comunicação de resultados em práticas de programação, sem códigos.

**Tabela-Resumo**

| Código | Competência | Disposições | Conhecimento | Habilidade |
|---|---|---|---|---|
| CT26.04.4 | Verificação por evidências | compromisso, criticidade, clareza | K06 | registrar E/S para conferência |
| CT26.04.4 | Verificação por evidências | compromisso, criticidade, clareza | K08 | exercitar repetição com casos distintos |
| CT26.04.4 | Verificação por evidências | compromisso, criticidade, clareza | K10 | evidenciar uso correto de função |

**Definição de Ativação**
- Restrição de ativação: **obrigatória**
- Modo de ativação: **justificatória + analítica**
- Função de ativação: **núcleo**
- Justificativa: a tarefa requer não apenas “ter um programa”, mas sustentar a correção com saídas e registros; a verificação é diretamente observável por execuções e pela justificativa breve que conecta evidências ao comportamento esperado.

---

## Fora do Escopo/Extensão (EXT) — se houver
- Suporte a **aritmética de precisão arbitrária** (fatorial de entradas muito grandes) e estratégias avançadas de prevenção de estouro numérico não são exigidas pela tarefa e não estão explicitadas no catálogo como conhecimento dedicado; quando desejado, deve ser tratado como extensão de escopo de disciplina/tarefa.
- Políticas formais de **tratamento de entradas fora do domínio** (mensagens de erro, recuperação de entrada) podem ser consideradas extensão, caso se pretenda padronizar validação além do necessário para a tarefa.

---

## Checagem Final (consistência K–LO–CT)
- Todos os K utilizados pertencem ao **catálogo** (K02, K03, K04, K06, K08, K10).
- Todo LO referencia K e é coberto por pelo menos uma CT.
- Toda CT referencia K (com distinção **Núcleo × Apoio**) e cobre LO(s).
- CTs são exclusivas de Computação, reutilizáveis e não hipergranulares (4 CTs).
- BNCC aparece apenas em alinhamento geral, **sem códigos**.