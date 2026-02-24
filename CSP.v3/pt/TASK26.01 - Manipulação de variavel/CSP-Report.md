# Relatório CSP — Autoria de Competências (Competency Authoring)

**Código da Task:** TASK25.20  
**Título:** Rastreamento de Variáveis em Sequência de Atribuições na Linguagem C  
**Nível/Curso:** Curso Técnico em Informática (aplicável também a disciplinas introdutórias no ensino superior)  
**Componente Curricular:** Lógica de Programação / Programação Estruturada  
**Contexto:** Atividade individual; rastreamento escrito (tabela/registro sequencial); avaliação sem apresentação oral; possibilidade de validação opcional em ambiente C, a critério do docente  
**Escala de proficiência:** 0–10 (passo 0,1)

---

## Introdução
Este relatório se insere na fase de **Autoria de Competências** do Competency Specification Process (CSP), na qual a tarefa instrucional é analisada para explicitar **conhecimentos mobilizados**, **objetivos de aprendizagem observáveis** e **competências** formuladas no modelo **Conhecimento–Habilidade–Disposição (K–S–D)**.

A tarefa consiste em analisar um trecho de programa em C no qual variáveis recebem valores iniciais e, em seguida, passam por uma sequência de atribuições e expressões aritméticas. Esse desenho instrucional elicita evidências observáveis porque requer que o estudante produza: (i) um **rastreio passo a passo** do estado das variáveis após cada instrução, (ii) uma **resposta final selecionando a alternativa correta**, e (iii) uma **justificativa breve** coerente com o rastreamento. Esses produtos permitem verificar correção, consistência interna e clareza da explicação.

O modelo K–S–D é suportado de forma direta: a atividade demanda **conhecimentos declarativos e procedimentais** (por exemplo, atribuição e avaliação de expressões), **habilidades de análise e representação** (rastrear estados e explicar mudanças) e **disposições acadêmicas** (organização, atenção a detalhes, responsabilidade/autoria).

---

# 1. Análise da Entidade Instrucional

## Título
Rastreamento de Variáveis em Sequência de Atribuições na Linguagem C

## Descrição
A tarefa solicita que o estudante determine os valores finais de quatro variáveis após a execução completa de um algoritmo em C, partindo de valores iniciais definidos. O estudante deve produzir um registro sistemático do estado das variáveis após cada comando, incluindo cálculos intermediários quando houver expressões, e selecionar a alternativa correspondente ao resultado final.

## Processo de Desenvolvimento da Solução (em etapas)
1. **Registrar estado inicial** das variáveis (valores fornecidos).
2. **Executar mentalmente** cada linha do algoritmo em sequência.
3. **Atualizar e registrar** o estado (A, B, C, D) após cada atribuição.
4. **Calcular explicitamente** expressões aritméticas antes de atualizar a variável-alvo.
5. **Consolidar valores finais** e **comparar** com as alternativas.
6. **Selecionar a alternativa correta** e **redigir justificativa breve** ancorada no rastreamento.

## Resultados Esperados (lista de produtos e evidências)
- Alternativa marcada (resposta final).
- Rastreio/tabela de execução com valores de A, B, C e D após cada comando.
- Justificativa breve (parágrafo curto ou anotações na tabela) explicando pontos críticos (sobrescrita, dependência entre variáveis, uso de valores atualizados em expressões).

## Contexto de Aquisição (curso, organização, ambiente, avaliação)
- **Curso/Nível:** técnico em Informática (e adaptável ao superior introdutório).
- **Organização:** individual (com discussão pontual opcional, mantendo entrega individual).
- **Ambiente:** papel e caneta, quadro ou planilha; ambiente C opcional para validação, a critério do docente.
- **Avaliação:** sem apresentação oral; baseada na resposta selecionada e na qualidade do rastreamento/justificativa.

## Perfil do Público-Alvo (nível, pré-requisitos, necessidades)
- **Nível:** iniciantes em programação estruturada.
- **Pré-requisitos:** noções de variável e atribuição; execução sequencial; expressões aritméticas e prioridade de operadores; interpretação de resultados com decimais (coerente com variáveis de ponto flutuante).
- **Necessidades típicas:** apoio na construção de representações de estado (tabelas), redução de erros por “pulos” de etapas e fortalecimento da verificação de consistência.

## Escala de Proficiência (critérios e dimensões)
**Escala 0–10 (0,1):** baseada em três dimensões observáveis na tarefa.

- **Dimensão Técnica (0–10):** correção do rastreamento e dos valores finais; consistência entre passos e resultado.
- **Dimensão Cognitiva (0–10):** qualidade da explicação; compreensão de sobrescrita, dependências e uso de valores vigentes; explicitação de cálculos.
- **Dimensão Atitudinal (0–10):** organização, legibilidade, rastreabilidade do registro; responsabilidade acadêmica (autoria) e diligência.

**Descritores sintéticos por faixa:**
- **0–2,9:** registro ausente/incoerente; resposta sem rastreio verificável.
- **3–4,9:** rastreio parcial, com lacunas; justificativa fraca; possíveis inconsistências.
- **5–6,9:** rastreio majoritariamente correto; pequenas falhas de clareza; justificativa suficiente.
- **7–8,9:** rastreio completo e consistente; cálculos explicitados; justificativa clara.
- **9–10:** rastreio exemplar, altamente verificável; excelente precisão e comunicação concisa.

---

# 2. Enumeração de Conhecimentos

## Fundamentos de Programação (estado e atribuição)
**K1 — Semântica de atribuição e sobrescrita de valores**
- Compreender que uma atribuição substitui o valor anterior da variável.
- Reconhecer que o valor “antigo” não permanece disponível após ser sobrescrito.
- Identificar efeitos de cadeias de atribuições em sequência.

**K2 — Execução sequencial e dependência temporal**
- Entender que linhas são executadas em ordem e afetam o estado subsequente.
- Diferenciar valores iniciais de valores atualizados no decorrer do algoritmo.
- Reconhecer dependências entre variáveis por leitura/escrita ao longo do tempo.

## Expressões e Operações Aritméticas
**K3 — Avaliação de expressões aritméticas com prioridade de operadores**
- Aplicar ordem de operações ao calcular expressões.
- Realizar cálculos intermediários antes de atualizar variáveis-alvo.
- Interpretar a combinação de operações (ex.: divisão e soma) de forma consistente.

**K4 — Representação numérica com valores decimais**
- Interpretar resultados com casas decimais quando decorrentes das operações.
- Manter consistência de representação numérica no rastreamento.

## Representação e Rastreio (depuração conceitual)
**K5 — Técnicas de rastreamento (trace) do estado de variáveis**
- Construir tabela/registro sequencial do estado após cada instrução.
- Registrar somente variáveis modificadas mantendo o conjunto do estado visível.
- Garantir rastreabilidade do resultado final a partir das etapas.

## Argumentação e Verificabilidade
**K6 — Justificativa baseada em evidências do rastreamento**
- Relacionar resposta final às etapas registradas.
- Explicar mudanças críticas (sobrescrita e uso de valores vigentes) de forma verificável.
- Redigir justificativas concisas e alinhadas ao registro produzido.

## Postura Acadêmica e Qualidade do Registro
**K7 — Organização, legibilidade e responsabilidade acadêmica**
- Produzir registro claro, auditável e consistente.
- Demonstrar atenção a detalhes e evitar respostas por tentativa.
- Preservar autoria e coerência entre registro e resposta.

### Nota Analítica
Os conhecimentos foram curados por serem **diretamente mobilizados** pelos requisitos da tarefa: produzir rastreio após cada instrução, explicitar cálculos e justificar a alternativa escolhida. Itens foram formulados para serem ensináveis (podem ser explicados e praticados), observáveis (aparecem no registro e na justificativa) e avaliáveis (consistência interna e correção do resultado).

---

# 3. Identificação de Objetivos de Aprendizagem

**LO1** — Representar o estado inicial das variáveis conforme valores fornecidos.  
**LO2** — Rastrear, passo a passo, o estado das variáveis após cada comando de atribuição.  
**LO3** — Calcular corretamente expressões aritméticas envolvidas nas atribuições, explicitando contas intermediárias quando necessário.  
**LO4** — Diferenciar valores sobrescritos de valores vigentes ao longo da execução do algoritmo.  
**LO5** — Selecionar a alternativa correta com base nos valores finais obtidos por rastreamento verificável.  
**LO6** — Justificar a resposta final por meio de um registro organizado e coerente do rastreamento.  
**LO7** — Produzir um artefato escrito legível e auditável, com clareza e consistência.

### Nota Analítica
Os LOs foram formulados com verbos observáveis (representar, rastrear, calcular, diferenciar, selecionar, justificar, produzir) e possuem evidência direta nos artefatos esperados (tabela/registro, alternativa marcada, justificativa). Em termos de Bloom revisada, a tarefa concentra-se em **Aplicar** (executar cálculos e regras de atribuição), **Analisar** (rastrear dependências e estado), e **Avaliar** (conferir consistência e justificar a alternativa).

---

# 4. Definição de Competências

## 4.1 Competência Geral (BNCC – quando aplicável)
**Competência geral do domínio (sem códigos):** Analisar a execução de algoritmos e comunicar, de forma verificável, o comportamento de variáveis e expressões em programas estruturados, utilizando registros claros e justificativas baseadas em evidências.

> **Alinhamento BNCC:** não aplicado (não informado na entrada).

---

## 4.2 Especificações de Competências

### CT25.20.1 — Rastrear sobrescrita e dependências em atribuições sequenciais
**Descrição Textual**  
Capacidade de analisar uma sequência de atribuições e identificar, a cada passo, quais valores são sobrescritos e quais permanecem vigentes, mantendo coerência temporal entre linhas executadas.

**Especificação de Conhecimentos**
- **K1:** Semântica de atribuição e sobrescrita.
- **K2:** Execução sequencial e dependência temporal.

**Alinhamento com a Taxonomia de Bloom (revisada)**
- **Analisar** (distinguir estados antes/depois; identificar dependências).

**Pareamento Conhecimento–Habilidade**
- K1 → rastrear sobrescrita de valores.
- K2 → atualizar estado considerando ordem de execução.

**Anotação de Verbos**
- analisar, rastrear, identificar, diferenciar, atualizar

**Especificação de Disposições**
- Atenção a detalhes.
- Rigor na sequência de passos.
- Persistência para evitar “pulos” de estado.

**Competências Alinhadas à BNCC (quando aplicável)**
- Não aplicado (sem códigos; alinhamento apenas em nível geral ao raciocínio computacional e explicitação de processos).

**Tabela-Resumo**
| Código | Competência | Disposições | Conhecimento | Habilidade |
|---|---|---|---|---|
| CT25.20.1 | Rastrear sobrescrita e dependências | atenção; rigor; persistência | K1, K2 | rastrear estado e dependências |

**Definição de Ativação (Activation Definition)**
- **ActivationConstraint:** obrigatória  
- **ActivationMode:** analítica  
- **ActivationRole:** núcleo  
**Justificativa:** a tarefa exige rastreamento linha a linha e compreensão de sobrescrita/ordem de execução como base para qualquer resposta correta.

---

### CT25.20.2 — Construir registro rastreável do estado das variáveis (tabela/trace)
**Descrição Textual**  
Capacidade de produzir um registro sequencial auditável (tabela ou equivalente) que apresente o estado completo das variáveis após cada instrução, permitindo verificação independente do raciocínio.

**Especificação de Conhecimentos**
- **K5:** Técnicas de rastreamento do estado de variáveis.
- **K7:** Organização, legibilidade e responsabilidade acadêmica.

**Alinhamento com a Taxonomia de Bloom (revisada)**
- **Aplicar** (executar técnica de rastreio).
- **Criar** (produzir artefato representacional adequado).

**Pareamento Conhecimento–Habilidade**
- K5 → registrar estados após cada comando de forma sistemática.
- K7 → organizar e tornar o registro legível e verificável.

**Anotação de Verbos**
- registrar, organizar, representar, produzir, documentar

**Especificação de Disposições**
- Capricho e clareza na apresentação.
- Compromisso com rastreabilidade (facilitar checagem).
- Responsabilidade com autoria do registro.

**Competências Alinhadas à BNCC (quando aplicável)**
- Não aplicado (sem códigos; alinhamento geral à comunicação de processos e documentação).

**Tabela-Resumo**
| Código | Competência | Disposições | Conhecimento | Habilidade |
|---|---|---|---|---|
| CT25.20.2 | Construir registro rastreável | clareza; rastreabilidade; responsabilidade | K5, K7 | produzir tabela/trace auditável |

**Definição de Ativação (Activation Definition)**
- **ActivationConstraint:** obrigatória  
- **ActivationMode:** construtiva  
- **ActivationRole:** núcleo  
**Justificativa:** a evidência central prevista para avaliação é o rastreio escrito; ele materializa o desempenho e sustenta a justificativa da resposta.

---

### CT25.20.3 — Avaliar expressões aritméticas e manter consistência numérica no rastreamento
**Descrição Textual**  
Capacidade de calcular expressões aritméticas presentes nas atribuições, explicitando contas intermediárias quando necessário, e registrar resultados coerentes com valores decimais.

**Especificação de Conhecimentos**
- **K3:** Prioridade de operadores e avaliação de expressões.
- **K4:** Representação numérica com valores decimais.

**Alinhamento com a Taxonomia de Bloom (revisada)**
- **Aplicar** (executar cálculos conforme regras).
- **Analisar** (integrar cálculo ao estado vigente das variáveis).

**Pareamento Conhecimento–Habilidade**
- K3 → calcular corretamente expressões antes de atualizar variáveis.
- K4 → registrar e interpretar resultados com casas decimais.

**Anotação de Verbos**
- calcular, aplicar, explicitar, verificar, registrar

**Especificação de Disposições**
- Precisão.
- Autochecagem de resultados.
- Paciência para explicitar intermediários.

**Competências Alinhadas à BNCC (quando aplicável)**
- Não aplicado (sem códigos; alinhamento geral à resolução de problemas e precisão representacional).

**Tabela-Resumo**
| Código | Competência | Disposições | Conhecimento | Habilidade |
|---|---|---|---|---|
| CT25.20.3 | Avaliar expressões e manter consistência numérica | precisão; autochecagem; paciência | K3, K4 | calcular e registrar valores coerentes |

**Definição de Ativação (Activation Definition)**
- **ActivationConstraint:** obrigatória  
- **ActivationMode:** analítica  
- **ActivationRole:** núcleo  
**Justificativa:** o resultado final depende diretamente de cálculos em expressões; erros de operação ou registro inviabilizam a alternativa correta.

---

### CT25.20.4 — Selecionar a alternativa correta com base em evidências do rastreamento
**Descrição Textual**  
Capacidade de consolidar valores finais obtidos no rastreamento e compará-los com as alternativas, selecionando a opção correspondente de forma consistente e justificável.

**Especificação de Conhecimentos**
- **K2:** Execução sequencial e dependência temporal.
- **K5:** Técnicas de rastreamento.
- **K6:** Justificativa baseada em evidências.

**Alinhamento com a Taxonomia de Bloom (revisada)**
- **Avaliar** (conferir correspondência entre rastreio e alternativas).
- **Analisar** (consolidar estados finais a partir do processo).

**Pareamento Conhecimento–Habilidade**
- K5 → consolidar estado final a partir do trace.
- K6 → fundamentar escolha pela evidência do registro.

**Anotação de Verbos**
- comparar, selecionar, validar, consolidar, justificar

**Especificação de Disposições**
- Rigor na conferência.
- Honestidade intelectual (não “chutar” sem rastreio).
- Responsividade a evidências (seguir o que o registro mostra).

**Competências Alinhadas à BNCC (quando aplicável)**
- Não aplicado (sem códigos; alinhamento geral à validação e tomada de decisão baseada em evidências).

**Tabela-Resumo**
| Código | Competência | Disposições | Conhecimento | Habilidade |
|---|---|---|---|---|
| CT25.20.4 | Selecionar alternativa baseada em evidência | rigor; honestidade; evidência | K2, K5, K6 | comparar e validar alternativa |

**Definição de Ativação (Activation Definition)**
- **ActivationConstraint:** obrigatória  
- **ActivationMode:** justificatória  
- **ActivationRole:** núcleo  
**Justificativa:** além do resultado, a tarefa requer sustentação do acerto por meio do rastreio e justificativa, tornando a escolha verificável.

---

### CT25.20.5 — Explicar mudanças críticas do algoritmo de forma concisa e verificável
**Descrição Textual**  
Capacidade de elaborar uma justificativa breve e coerente que destaque pontos críticos (sobrescrita, dependência entre variáveis e uso de valores vigentes nas expressões), ancorando a explicação no registro produzido.

**Especificação de Conhecimentos**
- **K6:** Justificativa baseada em evidências.
- **K1:** Semântica de atribuição e sobrescrita.
- **K2:** Execução sequencial.

**Alinhamento com a Taxonomia de Bloom (revisada)**
- **Compreender** (explicar relações causa–efeito).
- **Analisar** (selecionar mudanças críticas e relacioná-las ao estado).
- **Avaliar** (apoiar afirmações em evidências do rastreio).

**Pareamento Conhecimento–Habilidade**
- K6 → redigir justificativa verificável.
- K1/K2 → explicar por que os valores mudam ao longo da sequência.

**Anotação de Verbos**
- explicar, justificar, descrever, relacionar, evidenciar

**Especificação de Disposições**
- Clareza comunicativa.
- Compromisso com verificabilidade.
- Postura acadêmica (argumentar com base no que foi registrado).

**Competências Alinhadas à BNCC (quando aplicável)**
- Não aplicado (sem códigos; alinhamento geral à comunicação e argumentação fundamentada).

**Tabela-Resumo**
| Código | Competência | Disposições | Conhecimento | Habilidade |
|---|---|---|---|---|
| CT25.20.5 | Explicar mudanças críticas de forma verificável | clareza; verificabilidade; postura acadêmica | K6, K1, K2 | justificar com base no rastreio |

**Definição de Ativação (Activation Definition)**
- **ActivationConstraint:** obrigatória  
- **ActivationMode:** justificatória  
- **ActivationRole:** apoio  
**Justificativa:** a justificativa não substitui o rastreio, mas fortalece a evidência cognitiva e permite avaliar compreensão para além do acerto numérico.

---

### CT25.20.6 — Manter qualidade acadêmica do artefato escrito (legibilidade e auditabilidade)
**Descrição Textual**  
Capacidade de produzir um artefato escrito claro e auditável, com organização, legibilidade e consistência interna entre rastreio, cálculos e resposta final.

**Especificação de Conhecimentos**
- **K7:** Organização, legibilidade e responsabilidade acadêmica.
- **K5:** Rastreio do estado (como estrutura do artefato).

**Alinhamento com a Taxonomia de Bloom (revisada)**
- **Aplicar** (empregar critérios de organização e registro).
- **Criar** (entregar artefato completo e verificável).

**Pareamento Conhecimento–Habilidade**
- K7 → apresentar o trabalho com qualidade documental.
- K5 → estruturar o rastreio de modo consistente e conferível.

**Anotação de Verbos**
- organizar, apresentar, documentar, revisar, garantir

**Especificação de Disposições**
- Diligência.
- Responsabilidade com a entrega.
- Respeito à verificabilidade (facilitar correção e auditoria).

**Competências Alinhadas à BNCC (quando aplicável)**
- Não aplicado (sem códigos; alinhamento geral à comunicação e responsabilidade).

**Tabela-Resumo**
| Código | Competência | Disposições | Conhecimento | Habilidade |
|---|---|---|---|---|
| CT25.20.6 | Qualidade acadêmica do artefato escrito | diligência; responsabilidade; verificabilidade | K7, K5 | organizar e revisar artefatos |

**Definição de Ativação (Activation Definition)**
- **ActivationConstraint:** obrigatória  
- **ActivationMode:** construtiva  
- **ActivationRole:** apoio  
**Justificativa:** a avaliação prevê legibilidade e rastreabilidade; um artefato desorganizado reduz a evidência mesmo quando o resultado final está correto.

---

## Checagem de Qualidade (síntese)
- Todas as competências possuem evidências observáveis (tabela/trace, alternativa marcada, justificativa).
- Há baixa redundância: competências distinguem análise de atribuição, construção do registro, cálculo, validação por alternativas, explicação e qualidade documental.
- Cada CT apresenta K–S–D completo e Definição de Ativação coerente com a natureza da tarefa.
- O relatório analisa a descrição pedagógica sem reproduzi-la integralmente; usa-a como base para especificação rastreável.
