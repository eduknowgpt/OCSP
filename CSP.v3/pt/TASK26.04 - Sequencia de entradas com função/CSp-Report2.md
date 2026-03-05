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

## 4. Definição de Competências

### 4.1 Competência Geral (BNCC – quando aplicável)
**Competência geral do domínio (Computação):**  
Mobilizar fundamentos de programação para implementar uma solução modular com funções, processar múltiplas entradas por repetição e produzir saídas verificáveis, sustentando correção e consistência por evidências de execução e justificativa técnica breve.

**BNCC (uso = sim):**  
Como a etapa (EF/EM) não está explicitada no contexto do curso, registra-se apenas alinhamento **em nível geral** com práticas de **pensamento computacional** e **programação/algoritmos** (formalização, decomposição, automação e validação), **sem uso de códigos**.

---

### 4.2 Especificações de Competências

### CT26.04.1
**Título da Competência**  
Modularizar um cálculo por função e integrá-lo ao processamento de múltiplas entradas.

**Descrição Textual (reutilizável; não específica do enunciado)**  
Definir e empregar uma **função** com responsabilidade clara (parâmetros e retorno) para realizar um cálculo, integrando-a ao fluxo principal que lê entradas, aciona o subprograma e apresenta resultados de forma conferível.

**Cobertura e rastreabilidade**
- LOs cobertos: (LO1, LO2)
- K mobilizados: (K10, K06, K02)

**Especificação de Conhecimentos**
- **K10 — Subprogramas: procedimentos e funções**  
  - Papel na competência: estrutura a decomposição da solução em uma função com responsabilidade bem definida.  
  - Evidência na tarefa: definição e uso consistente da função para realizar o cálculo solicitado.  
  - **Bloom associado:** Criar  
  - **Verbo taxonômico associado:** definir

- **K06 — Estrutura sequencial e E/S básica**  
  - Papel na competência: sustenta a integração entre leitura de entradas, chamada da função e apresentação dos resultados.  
  - Evidência na tarefa: o programa recebe os dados e apresenta saídas verificáveis para cada valor processado.  
  - **Bloom associado:** Aplicar  
  - **Verbo taxonômico associado:** ler

- **K02 — Fundamentos práticos da linguagem C (C11) para programação introdutória**  
  - Papel na competência: viabiliza a implementação concreta da solução no ambiente da disciplina.  
  - Evidência na tarefa: produção de um artefato executável/compilável com estrutura mínima adequada.  
  - **Bloom associado:** Aplicar  
  - **Verbo taxonômico associado:** implementar

**Alinhamento com a Taxonomia de Bloom (revisada)**  
Predomínio de **Criar**, pois a competência exige implementação e integração funcional de uma solução modular.

**Pareamento Conhecimento–Habilidade**
- **K10 / Criar / definir** → estruturar a solução em função com parâmetros e retorno coerentes.
- **K06 / Aplicar / ler** → articular entrada, processamento e saída de forma verificável.
- **K02 / Aplicar / implementar** → materializar a solução em linguagem de programação no padrão da disciplina.

**Anotação de Verbos (lista)**
definir, ler, implementar.

**Especificação de Disposições (2–4)**
- Rigor na definição da função e de sua responsabilidade.
- Consistência na integração entre fluxo principal e subprograma.
- Clareza na apresentação dos resultados para conferência.

**Competências Alinhadas à BNCC (quando aplicável)**  
Alinhamento geral com decomposição e formalização de soluções algorítmicas, sem códigos.

**Tabela-Resumo**

| Código | Competência | Disposições | Conhecimento | Bloom | Verbo | Habilidade |
|---|---|---|---|---|---|---|
| CT26.04.1 | Modularizar por função e integrar ao fluxo | rigor, consistência, clareza | K10 | Criar | definir | estruturar cálculo em função |
| CT26.04.1 | Modularizar por função e integrar ao fluxo | rigor, consistência, clareza | K06 | Aplicar | ler | integrar E/S ao processamento |
| CT26.04.1 | Modularizar por função e integrar ao fluxo | rigor, consistência, clareza | K02 | Aplicar | implementar | materializar a solução em C |

**Definição de Ativação**
- Restrição de ativação: **obrigatória**
- Modo de ativação: **construtiva**
- Função de ativação: **núcleo**
- Justificativa: a tarefa exige explicitamente que o cálculo seja encapsulado em função e integrado ao fluxo de leitura e saída do programa, constituindo evidência central da solução implementada.

---

### CT26.04.2
**Título da Competência**  
Aplicar repetição e atualização aritmética para computação iterativa baseada em entradas.

**Descrição Textual (reutilizável; não específica do enunciado)**  
Empregar **estruturas de repetição** e **expressões aritméticas** para realizar computações iterativas com atualização controlada de variáveis, garantindo consistência do processamento ao longo das iterações.

**Cobertura e rastreabilidade**
- LOs cobertos: (LO3, LO4)
- K mobilizados: (K08, K04, K03)

**Especificação de Conhecimentos**
- **K08 — Estruturas de repetição**  
  - Papel na competência: organiza o processamento iterativo de múltiplas entradas e/ou etapas sucessivas do cálculo.  
  - Evidência na tarefa: uso de laços para controlar a repetição necessária ao processamento.  
  - **Bloom associado:** Aplicar  
  - **Verbo taxonômico associado:** iterar

- **K04 — Expressões aritméticas e avaliação**  
  - Papel na competência: sustenta a atualização consistente dos valores intermediários e do resultado final.  
  - Evidência na tarefa: operações aritméticas coerentes ao longo do cálculo.  
  - **Bloom associado:** Aplicar  
  - **Verbo taxonômico associado:** calcular

- **K03 — Variáveis, constantes e tipos primitivos**  
  - Papel na competência: assegura controle coerente de acumuladores, contadores e dados de entrada.  
  - Evidência na tarefa: uso consistente de variáveis durante o processamento iterativo.  
  - **Bloom associado:** Aplicar  
  - **Verbo taxonômico associado:** atualizar

**Alinhamento com a Taxonomia de Bloom (revisada)**  
Predomínio de **Aplicar**, pois a competência requer uso correto de laços, variáveis e expressões aritméticas em uma solução já delimitada.

**Pareamento Conhecimento–Habilidade**
- **K08 / Aplicar / iterar** → controlar a repetição necessária ao processamento.
- **K04 / Aplicar / calcular** → produzir atualizações aritméticas coerentes.
- **K03 / Aplicar / atualizar** → manter o estado computacional consistente ao longo das iterações.

**Anotação de Verbos (lista)**
iterar, calcular, atualizar.

**Especificação de Disposições (2–4)**
- Atenção à consistência do laço e da contagem.
- Rigor no controle das atualizações sucessivas.
- Persistência na conferência do comportamento iterativo.

**Competências Alinhadas à BNCC (quando aplicável)**  
Alinhamento geral com automação de procedimentos e tratamento sistemático de dados, sem códigos.

**Tabela-Resumo**

| Código | Competência | Disposições | Conhecimento | Bloom | Verbo | Habilidade |
|---|---|---|---|---|---|---|
| CT26.04.2 | Repetição e atualização aritmética | atenção, rigor, persistência | K08 | Aplicar | iterar | controlar processamento repetido |
| CT26.04.2 | Repetição e atualização aritmética | atenção, rigor, persistência | K04 | Aplicar | calcular | executar atualização aritmética coerente |
| CT26.04.2 | Repetição e atualização aritmética | atenção, rigor, persistência | K03 | Aplicar | atualizar | manter variáveis consistentes |

**Definição de Ativação**
- Restrição de ativação: **obrigatória**
- Modo de ativação: **construtiva**
- Função de ativação: **núcleo**
- Justificativa: o processamento de múltiplas entradas e a produção do resultado dependem diretamente do uso correto de repetição, variáveis e operações aritméticas, todos evidenciados no comportamento do programa.

---

### CT26.04.3
**Título da Competência**  
Garantir consistência de dados e saídas ao longo do processamento.

**Descrição Textual (reutilizável; não específica do enunciado)**  
Gerenciar **variáveis, tipos, entrada e saída** de forma coerente em programas com processamento repetido, assegurando que os valores manipulados e apresentados correspondam ao comportamento esperado.

**Cobertura e rastreabilidade**
- LOs cobertos: (LO1, LO4)
- K mobilizados: (K03, K06, K04)

**Especificação de Conhecimentos**
- **K03 — Variáveis, constantes e tipos primitivos**  
  - Papel na competência: sustenta a consistência entre dados lidos, valores processados e resultados produzidos.  
  - Evidência na tarefa: declarações e atualizações coerentes das variáveis usadas na solução.  
  - **Bloom associado:** Aplicar  
  - **Verbo taxonômico associado:** declarar

- **K06 — Estrutura sequencial e E/S básica**  
  - Papel na competência: garante que a entrada e a saída sejam organizadas de forma conferível.  
  - Evidência na tarefa: cada valor informado pode ser relacionado ao resultado apresentado.  
  - **Bloom associado:** Aplicar  
  - **Verbo taxonômico associado:** apresentar

- **K04 — Expressões aritméticas e avaliação**  
  - Papel na competência: assegura coerência entre operações realizadas e resultado obtido.  
  - Evidência na tarefa: o valor final decorre de operações consistentes com o processamento proposto.  
  - **Bloom associado:** Analisar  
  - **Verbo taxonômico associado:** verificar

**Alinhamento com a Taxonomia de Bloom (revisada)**  
Predominam **Aplicar** e **Analisar**, pois além de usar adequadamente os recursos da linguagem, o estudante precisa conferir coerência entre dados, processamento e saída.

**Pareamento Conhecimento–Habilidade**
- **K03 / Aplicar / declarar** → estabelecer e manter variáveis/tipos coerentes.
- **K06 / Aplicar / apresentar** → organizar saídas rastreáveis e conferíveis.
- **K04 / Analisar / verificar** → checar a coerência das operações e dos resultados.

**Anotação de Verbos (lista)**
declarar, apresentar, verificar.

**Especificação de Disposições (2–4)**
- Cuidado com a rastreabilidade entre entrada e saída.
- Rigor na manutenção do estado do programa.
- Clareza na apresentação dos resultados.

**Competências Alinhadas à BNCC (quando aplicável)**  
Alinhamento geral com precisão e validação de resultados em práticas computacionais, sem códigos.

**Tabela-Resumo**

| Código | Competência | Disposições | Conhecimento | Bloom | Verbo | Habilidade |
|---|---|---|---|---|---|---|
| CT26.04.3 | Consistência de dados e saídas | cuidado, rigor, clareza | K03 | Aplicar | declarar | manter variáveis e tipos coerentes |
| CT26.04.3 | Consistência de dados e saídas | cuidado, rigor, clareza | K06 | Aplicar | apresentar | produzir saídas conferíveis |
| CT26.04.3 | Consistência de dados e saídas | cuidado, rigor, clareza | K04 | Analisar | verificar | conferir coerência aritmética |

**Definição de Ativação**
- Restrição de ativação: **obrigatória**
- Modo de ativação: **analítica + construtiva**
- Função de ativação: **núcleo**
- Justificativa: a tarefa só se torna verificável quando leitura, processamento e saída permanecem consistentes; por isso, a competência envolve tanto construção da solução quanto análise do comportamento produzido.

---

### CT26.04.4
**Título da Competência**  
Verificar o comportamento do programa por evidências de execução e justificativa técnica breve.

**Descrição Textual (reutilizável; não específica do enunciado)**  
Planejar e registrar **evidências mínimas de verificação** por meio de execuções com casos distintos e apresentar justificativa técnica concisa que sustente a correção do comportamento observado em programas com repetição e funções.

**Cobertura e rastreabilidade**
- LOs cobertos: (LO5)
- K mobilizados: (K06, K08, K10)

**Especificação de Conhecimentos**
- **K06 — Estrutura sequencial e E/S básica**  
  - Papel na competência: fornece a base observável para registro e interpretação das execuções.  
  - Evidência na tarefa: saídas registradas e comparáveis aos dados informados.  
  - **Bloom associado:** Avaliar  
  - **Verbo taxonômico associado:** registrar

- **K08 — Estruturas de repetição**  
  - Papel na competência: permite verificar se o processamento repetido ocorre conforme previsto.  
  - Evidência na tarefa: testes com múltiplas entradas evidenciam o funcionamento iterativo.  
  - **Bloom associado:** Analisar  
  - **Verbo taxonômico associado:** examinar

- **K10 — Subprogramas: procedimentos e funções**  
  - Papel na competência: permite justificar que o cálculo foi corretamente encapsulado e utilizado.  
  - Evidência na tarefa: relação entre chamadas da função e resultados apresentados.  
  - **Bloom associado:** Avaliar  
  - **Verbo taxonômico associado:** justificar

**Alinhamento com a Taxonomia de Bloom (revisada)**  
Predominam **Analisar** e **Avaliar**, pois a competência se concentra na inspeção do comportamento produzido e na sustentação argumentativa da correção da solução.

**Pareamento Conhecimento–Habilidade**
- **K06 / Avaliar / registrar** → documentar execuções de forma verificável.
- **K08 / Analisar / examinar** → inspecionar o comportamento iterativo em casos distintos.
- **K10 / Avaliar / justificar** → sustentar tecnicamente o uso da função no programa.

**Anotação de Verbos (lista)**
registrar, examinar, justificar.

**Especificação de Disposições (2–4)**
- Compromisso com verificabilidade.
- Postura crítica diante dos resultados observados.
- Objetividade na justificativa técnica.

**Competências Alinhadas à BNCC (quando aplicável)**  
Alinhamento geral com validação e comunicação de resultados em programação, sem códigos.

**Tabela-Resumo**

| Código | Competência | Disposições | Conhecimento | Bloom | Verbo | Habilidade |
|---|---|---|---|---|---|---|
| CT26.04.4 | Verificação por evidências | compromisso, criticidade, objetividade | K06 | Avaliar | registrar | documentar saídas conferíveis |
| CT26.04.4 | Verificação por evidências | compromisso, criticidade, objetividade | K08 | Analisar | examinar | inspecionar repetição em execução |
| CT26.04.4 | Verificação por evidências | compromisso, criticidade, objetividade | K10 | Avaliar | justificar | sustentar uso correto da função |

**Definição de Ativação**
- Restrição de ativação: **obrigatória**
- Modo de ativação: **justificatória + analítica**
- Função de ativação: **núcleo**
- Justificativa: a tarefa exige evidências observáveis de execução e uma justificativa breve; assim, a competência é ativada diretamente pela análise dos testes e pela explicação técnica do comportamento do programa.

---

## Checagem Final
- Todos os K são do catálogo (nenhum K novo criado).
- Todo LO referencia K e é coberto por pelo menos uma CT.
- Toda CT referencia K e cobre LO(s).
- Cada conhecimento mobilizado em cada CT possui:
  - um **nível de Bloom associado**;
  - um **verbo taxonômico associado ao par conhecimento/Bloom**.
- CTs são exclusivas de Computação, reutilizáveis e não hipergranulares (4 CTs).
- Bloom não está inflado.
- BNCC aparece apenas quando defensável e sem códigos inventados.
- O relatório analisa e especifica a tarefa sem copiar integralmente a descrição pedagógica.