# RELATÓRIO CSP — Autoria de Competências (Competency Authoring)

## Introdução
Este relatório situa-se na fase de **Autoria de Competências** do Competency Specification Process (CSP) e especifica, com **alta rastreabilidade**, **sem redundância** e com **reuso planejado**, os **Conhecimentos (K)**, **Objetivos de Aprendizagem (LO)** e **Competências (CT)** elicitos pela **TASK26.3**, no modelo **Conhecimento–Habilidade–Disposição (K–S–D)**, com foco exclusivo em Computação.

A tarefa solicita que o estudante desenvolva, em linguagem C, um programa que **lê um valor numérico**, aplica uma **regra de decisão baseada em limite** e apresenta **resultados numéricos** ao final, garantindo valores definidos para cenários alternativos. As evidências são observáveis porque a atividade requer **código-fonte executável**, **saída verificável** (resultados impressos) e **justificativa breve** conectando condição, cálculo e comportamento observado.

O modelo **K–S–D** é adequado porque: (i) os **Conhecimentos (K)** são estritamente selecionados do **Catálogo da Disciplina** (limite superior, sem criação de K novo); (ii) as **Habilidades (S)** emergem na modelagem, implementação e explicação do comportamento; e (iii) as **Disposições (D)** capturam rigor e verificabilidade na entrega, sem transformar atitudes em conteúdo técnico.

---

# 1. Análise da Entidade Instrucional

## Título
**TASK26.3 — Cálculo de Excesso de Peso e Multa (Linguagem C)**

## Descrição
Atividade individual de programação introdutória em C, com foco em: leitura de entrada numérica, uso de variáveis/constantes e tipos primitivos, expressões aritméticas e lógicas, **estruturas de seleção** para tratar cenários alternativos, e impressão de resultados como evidência verificável, acompanhada de justificativa breve.

## Processo de Desenvolvimento da Solução (em etapas)
1. Interpretar o enunciado e explicitar entrada, saídas e regra de decisão.
2. Selecionar variáveis/constantes e tipos primitivos coerentes com os dados.
3. Construir expressões aritméticas e condição lógica alinhadas à regra.
4. Implementar estrutura de seleção cobrindo explicitamente as alternativas.
5. Integrar entrada e saída básica para produzir evidência verificável.
6. Produzir justificativa breve conectando condição, cálculo e resultado observado.

## Resultados Esperados (lista de produtos e evidências)
- **Código-fonte em C** compilável e executável.
- **Saída do programa** com resultados apresentados de modo conferível.
- **Registros de execução** suficientes para verificar comportamento em cenários alternativos.
- **Justificativa breve** (2–5 linhas) descrevendo a condição e a lógica geral do cálculo (sem reescrever o código).

## Contexto de Aquisição (curso, organização, ambiente, avaliação)
- **Componente curricular:** Introdução à Programação (linguagem C).
- **Nível/Curso:** introdutório (perfil de entrada/1º período).
- **Organização:** individual.
- **Ambiente:** laboratório (compilação/execução) ou atividade escrita com entrega do código.
- **Avaliação:** correção do comportamento nos cenários previstos; consistência entre entrada–processamento–saída; clareza e verificabilidade da entrega e da justificativa.

## Perfil do Público-Alvo (nível, pré-requisitos, necessidades)
- **Perfil:** estudantes iniciantes em programação imperativa em C.
- **Pré-requisitos:** variáveis/constantes e tipos primitivos; expressões aritméticas e lógicas; estruturas de seleção; entrada/saída básica.
- **Necessidades recorrentes:** evitar lacunas de atribuição entre alternativas, manter coerência entre condição e cálculo e produzir saída conferível.

## Escala de Proficiência (critérios e dimensões)
Escala proposta em 4 níveis, em três dimensões (**Técnica**, **Cognitiva**, **Atitudinal**):

- **N1 — Inicial:** decisão/cálculo inconsistentes; valores não definidos em alguma alternativa; saída insuficiente; justificativa ausente/desconectada.
- **N2 — Básico:** solução funcional parcial; cobertura incompleta de alternativas ou inconsistências pontuais; justificativa parcial; evidências limitadas.
- **N3 — Proficiente:** comportamento correto nas alternativas relevantes; coerência entre tipos, variáveis, expressões e saída; justificativa breve coerente e verificável.
- **N4 — Avançado:** além da correção, demonstra rigor e estabilidade: cobertura consistente de cenários, artefato claro e justificativa tecnicamente precisa e concisa.

---

# 2. Seleção e Enumeração de Conhecimentos


### KDisc-02 — Fundamentos práticos da linguagem C (C11) para programação introdutória
- **Descrição (ensinável/observável):**
  - Estrutura mínima de um programa em C e organização básica.
  - Compilação/execução como condição operacional do artefato.
  - Uso introdutório de E/S para observar resultados.
- **Justificativa de mobilização na tarefa:** a evidência central é um programa executável em C com leitura e impressão de resultados.

### KDisc-03 — Variáveis, constantes e tipos primitivos
- **Descrição (ensinável/observável):**
  - Representação de dados por variáveis/constantes e atribuição.
  - Uso coerente de tipos primitivos em operações e resultados.
  - Consistência de valores definidos ao longo do fluxo.
- **Justificativa de mobilização na tarefa:** a tarefa depende de representar entrada e resultados derivados com valores definidos em cenários alternativos.

### KDisc-04 — Expressões aritméticas e avaliação
- **Descrição (ensinável/observável):**
  - Construção e avaliação de expressões aritméticas.
  - Dependência entre valores (resultado derivado de outro valor).
  - Coerência entre cálculo e valor apresentado.
- **Justificativa de mobilização na tarefa:** a solução exige calcular resultados numéricos derivados a partir da entrada.

### KDisc-05 — Expressões lógicas e condições
- **Descrição (ensinável/observável):**
  - Comparações e composição de condições booleanas.
  - Critério de decisão como expressão de verdade/falsidade.
  - Aderência entre regra do enunciado e condição construída.
- **Justificativa de mobilização na tarefa:** o comportamento do programa muda conforme a condição (aplica ou não aplica a regra).

### KDisc-06 — Estrutura sequencial e E/S básica
- **Descrição (ensinável/observável):**
  - Organização do programa em fluxo entrada → processamento → saída.
  - Leitura e impressão como evidência observável do comportamento.
  - Ordem de execução coerente para produzir resultados.
- **Justificativa de mobilização na tarefa:** leitura e apresentação de resultados são parte explícita da evidência requerida.

### KDisc-07 — Estruturas de seleção
- **Descrição (ensinável/observável):**
  - Seleção entre alternativas (if/else) baseada em condição.
  - Cobertura explícita de caso verdadeiro e caso falso.
  - Garantia de resultados definidos em todas as alternativas.
- **Justificativa de mobilização na tarefa:** a tarefa exige tratar explicitamente dois cenários e assegurar valores definidos.

### Nota Analítica
A seleção privilegia conhecimentos **centrais e reutilizáveis** para tarefas introdutórias do tipo “regra + decisão + cálculo + saída”, evitando granularidade excessiva. Não foram selecionados itens do catálogo relacionados a repetição, tipos estruturados, subprogramas, recursão e arquivos por não serem necessários para esta tarefa.

---

# 3. Identificação de Objetivos de Aprendizagem

### LO1. Interpretar enunciados e especificar entrada, saída e regra de decisão para um programa.
- **K associados:** (KDisc-03, KDisc-05, KDisc-06, KDisc-07)

### LO2. Representar dados e resultados usando variáveis/constantes e tipos primitivos coerentes, assegurando valores definidos nos cenários previstos.
- **K associados:** (KDisc-03, KDisc-07)

### LO3. Construir e aplicar expressões aritméticas para calcular resultados derivados a partir de uma entrada.
- **K associados:** (KDisc-03, KDisc-04, KDisc-06)

### LO4. Formular condições lógicas e empregar estruturas de seleção para controlar o fluxo de execução em cenários alternativos.
- **K associados:** (KDisc-05, KDisc-07)

### LO5. Implementar em C uma solução estruturada com E/S básica, produzindo saída verificável e justificativa breve sobre a lógica aplicada.
- **K associados:** (KDisc-02, KDisc-06, KDisc-07)

### Nota Analítica
Os LOs foram formulados para **reuso** em outras tarefas da disciplina (não dependem do tema do enunciado) e são avaliáveis por evidências típicas: código executável, saída conferível e justificativa breve. Em Bloom revisada, LO1/LO4 combinam **Analisar/Aplicar**; LO2/LO3 enfatizam **Aplicar**; LO5 envolve **Criar** apenas porque exige implementação do programa.

---

# 4. Definição de Competências

## 4.1 Competência Geral (BNCC – quando aplicável)
**Competência geral do domínio (Computação):**  
Mobilizar fundamentos de programação imperativa para modelar problemas como transformação entrada–processamento–saída, implementar soluções com **estruturas de seleção** e produzir evidências verificáveis do comportamento do programa.

**BNCC (usar = sim; alinhamento geral, sem códigos):**  
Alinhamento geral com práticas de pensamento computacional e programação/algoritmos, especialmente na formalização de regras, uso de condições e implementação de seleção, com resultados observáveis. Sem códigos por ausência de base segura de etapa (EF/EM) para esta task.

---

## 4.2 Especificações de Competências

### CT26.3.1
**Título da Competência**  
Modelar regras de decisão e cálculo para soluções com cenários alternativos.

**Descrição Textual (reutilizável; não específica do enunciado)**  
Estruturar uma solução que explicite entradas e resultados, formule condição de decisão e defina cálculos associados, garantindo comportamento definido em cenários alternativos e coerência entre regra, cálculo e resultados esperados.

**Cobertura e rastreabilidade**
- **LOs cobertos:** (LO1, LO3, LO4)
- **K mobilizados (Núcleo):** (KDisc-04, KDisc-05, KDisc-07)
- **K mobilizados (Apoio):** (KDisc-03)

**Especificação de Conhecimentos**
- **KDisc-04 (Núcleo):** expressões aritméticas sustentam o cálculo de resultados derivados; evidência: valores resultantes coerentes com a regra.
- **KDisc-05 (Núcleo):** condições expressam o critério de decisão; evidência: discriminação correta de cenários.
- **KDisc-07 (Núcleo):** seleção garante cobertura de alternativas; evidência: resultados definidos em ambos os caminhos.
- **KDisc-03 (Apoio):** variáveis/tipos sustentam representação de entrada/resultados; papel: suporte de implementação e consistência.

**Alinhamento com a Taxonomia de Bloom (revisada)**  
Analisar (principal) + Aplicar (secundário)

**Pareamento Conhecimento–Habilidade**
- KDisc-05 → formular condição de decisão coerente com a regra.
- KDisc-04 → estabelecer cálculos para resultados derivados.
- KDisc-07 → estruturar alternativas completas (caso verdadeiro/falso).
- KDisc-03 → representar de modo consistente entrada e resultados.

**Anotação de Verbos (lista)**  
modelar, especificar, formular, discriminar, estabelecer, estruturar

**Especificação de Disposições (2–4)**  
rigor interpretativo; precisão; verificabilidade; responsabilidade acadêmica

**Competências Alinhadas à BNCC (quando aplicável)**  
Alinhamento geral com algoritmos e seleção condicional (sem códigos).

**Tabela-Resumo**
| Código | Competência | Disposições | Conhecimento | Habilidade |
|---|---|---|---|---|
| CT26.3.1 | Modelar regras de decisão e cálculo com cenários alternativos | rigor; precisão; verificabilidade; responsabilidade | Núcleo: KDisc-04,05,07; Apoio: KDisc-03 | formular condição; definir cálculos; estruturar cenários |

**Definição de Ativação**
- **Restrição de ativação:** obrigatória  
- **Modo de ativação:** analítica  
- **Função de ativação:** núcleo  
- **Justificativa:** a tarefa exige traduzir regra textual em condição e cálculos e prever comportamento em cenários alternativos; isso gera evidência direta de modelagem correta.

---

### CT26.3.2
**Título da Competência**  
Implementar, em C, programas estruturados com E/S, expressões e estruturas de seleção.

**Descrição Textual (reutilizável; não específica do enunciado)**  
Construir um programa em C que realize entrada de dados, processamento por expressões e decisão por estrutura de seleção, produzindo saída verificável e mantendo consistência de tipos e atribuições.

**Cobertura e rastreabilidade**
- **LOs cobertos:** (LO2, LO3, LO4, LO5)
- **K mobilizados (Núcleo):** (KDisc-02, KDisc-06, KDisc-07)
- **K mobilizados (Apoio):** (KDisc-03, KDisc-04, KDisc-05)

**Especificação de Conhecimentos**
- **KDisc-02 (Núcleo):** materializa a solução em C executável; evidência: código compila/executa e cumpre o comportamento.
- **KDisc-06 (Núcleo):** integra E/S e sequência para observabilidade; evidência: leitura e impressão coerentes com o processamento.
- **KDisc-07 (Núcleo):** implementa seleção com alternativas completas; evidência: resultados definidos em todos os caminhos.
- **KDisc-03 (Apoio):** variáveis/tipos sustentam armazenamento e coerência; papel: suporte de implementação.
- **KDisc-04 (Apoio):** expressões aritméticas implementam cálculos; papel: suporte do processamento.
- **KDisc-05 (Apoio):** expressões lógicas implementam o critério; papel: suporte da decisão.

**Alinhamento com a Taxonomia de Bloom (revisada)**  
Criar (principal) + Aplicar (secundário)

**Pareamento Conhecimento–Habilidade**
- KDisc-02 → construir artefato executável em C.
- KDisc-06 → integrar leitura e impressão como evidência do comportamento.
- KDisc-07 → implementar seleção cobrindo alternativas.
- KDisc-03/04/05 → sustentar implementação por representação, cálculo e condição.

**Anotação de Verbos (lista)**  
implementar, construir, integrar, programar, aplicar, atribuir, executar

**Especificação de Disposições (2–4)**  
completude; consistência; rigor técnico; clareza para conferência

**Competências Alinhadas à BNCC (quando aplicável)**  
Alinhamento geral com programação/algoritmos (sem códigos).

**Tabela-Resumo**
| Código | Competência | Disposições | Conhecimento | Habilidade |
|---|---|---|---|---|
| CT26.3.2 | Implementar em C solução com E/S e seleção | completude; consistência; rigor; clareza | Núcleo: KDisc-02,06,07; Apoio: KDisc-03,04,05 | construir programa; integrar E/S; implementar seleção |

**Definição de Ativação**
- **Restrição de ativação:** obrigatória  
- **Modo de ativação:** construtiva  
- **Função de ativação:** núcleo  
- **Justificativa:** a principal evidência da tarefa é a implementação executável com leitura, decisão e saída verificável; portanto, a ativação ocorre pela construção do artefato.

---

### CT26.3.3
**Título da Competência**  
Analisar e justificar o comportamento de programas com seleção a partir de evidências observáveis.

**Descrição Textual (reutilizável; não específica do enunciado)**  
Interpretar resultados produzidos por programas com estruturas de seleção e justificar, de forma breve, a coerência entre condição, cálculo e saída, apoiando a análise em evidências observáveis.

**Cobertura e rastreabilidade**
- **LOs cobertos:** (LO1, LO5)
- **K mobilizados (Núcleo):** (KDisc-06, KDisc-07, KDisc-05)
- **K mobilizados (Apoio):** (KDisc-04, KDisc-02)

**Especificação de Conhecimentos**
- **KDisc-06 (Núcleo):** saída como evidência verificável; evidência: interpretação correta do que foi impresso.
- **KDisc-07 (Núcleo):** relação entre alternativa executada e resultado; evidência: explicação do caminho selecionado.
- **KDisc-05 (Núcleo):** condição como critério de seleção; evidência: justificativa do cenário ativado.
- **KDisc-04 (Apoio):** cálculo sustenta o valor exibido; papel: suporte à justificativa do resultado numérico.
- **KDisc-02 (Apoio):** contexto de execução em C; papel: suporte operacional para leitura de evidências.

**Alinhamento com a Taxonomia de Bloom (revisada)**  
Analisar (principal) + Aplicar (secundário)

**Pareamento Conhecimento–Habilidade**
- KDisc-06 → interpretar saída como evidência.
- KDisc-07 + KDisc-05 → justificar seleção do caminho executado.
- KDisc-04 → justificar valores exibidos com base no cálculo.

**Anotação de Verbos (lista)**  
analisar, interpretar, justificar, relacionar, evidenciar, conferir

**Especificação de Disposições (2–4)**  
verificabilidade; precisão; transparência; responsabilidade acadêmica

**Competências Alinhadas à BNCC (quando aplicável)**  
Alinhamento geral com análise/explicação de algoritmos simples com seleção (sem códigos).

**Tabela-Resumo**
| Código | Competência | Disposições | Conhecimento | Habilidade |
|---|---|---|---|---|
| CT26.3.3 | Analisar e justificar comportamento de seleção pela saída | verificabilidade; precisão; transparência; responsabilidade | Núcleo: KDisc-06,07,05; Apoio: KDisc-04,02 | interpretar evidências; justificar coerência condição–cálculo–saída |

**Definição de Ativação**
- **Restrição de ativação:** obrigatória  
- **Modo de ativação:** justificatória  
- **Função de ativação:** apoio  
- **Justificativa:** a tarefa prevê justificativa breve e resultados observáveis; a ativação ocorre ao explicar o comportamento com base na evidência de saída, complementando a implementação.

