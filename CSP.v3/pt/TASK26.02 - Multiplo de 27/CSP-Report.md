# Introdução

Este Relatório CSP documenta a fase de **Autoria de Competências (Competency Authoring)** aplicada à atividade **TASK25.21 – Verificação de Múltiplo de 27 com Entrada Validada em Linguagem C** (código adotado para rastreabilidade, a partir da descrição pedagógica desta conversa). A tarefa situa-se em um contexto introdutório de **Lógica de Programação / Programação em C** em curso técnico, com ênfase na construção de um programa simples, correto e comunicável.

A atividade elicita **evidências observáveis** porque exige a produção de um artefato executável (programa em C), com comportamento verificável por testes (casos múltiplos e não múltiplos de 27, além de entradas inválidas quanto à positividade), e porque solicita justificativas explícitas (descrição escrita e/ou explicação oral) sobre validação de entrada e regra usada para determinar multiplicidade.

O cenário suporta o modelo **Conhecimento–Habilidade–Disposição (K–S–D)** ao combinar: (i) **conhecimentos ensináveis** (tipos inteiros, entrada/saída, operador de resto, divisibilidade, estruturas condicionais); (ii) **habilidades demonstráveis** (implementar validação, computar condição de múltiplo, produzir saída clara, testar e depurar); e (iii) **disposições** mobilizadas no processo avaliativo e de produção (responsabilidade, rigor, ética/autoria, clareza comunicacional), conforme o desenho previsto (entrega do código, demonstração de execução e justificativa).

---

# 1. Análise da Entidade Instrucional

## Título
**Verificação de Múltiplo de 27 com Entrada Validada em Linguagem C**

## Descrição
O estudante desenvolve um programa em linguagem C que solicita um **número inteiro positivo**, valida o atendimento ao requisito de positividade e determina se o valor informado é **múltiplo de 27**, exibindo mensagem final inequívoca. A atividade valoriza correção lógica, clareza de interação com o usuário e robustez básica frente a entradas fora do requisito.

## Processo de Desenvolvimento da Solução (em etapas)
1. **Leitura e extração de requisitos**: identificar restrições (inteiro; positivo; verificação de múltiplo de 27) e resultados esperados (mensagens claras).
2. **Planejamento do fluxo**: definir sequência mínima (entrada → validação → verificação → saída), incluindo o tratamento para casos inválidos de positividade.
3. **Implementação em C**: realizar leitura do inteiro, aplicar validação de positividade e computar a condição de múltiplo de 27, com decisão e impressão do resultado.
4. **Testes dirigidos**: executar com valores representativos (múltiplo e não múltiplo) e com valores inválidos quanto à positividade.
5. **Revisão final**: verificar legibilidade (indentação/nomeação) e consistência das mensagens antes da entrega.

## Resultados Esperados (lista de produtos e evidências)
- **Código-fonte** completo em C.
- **Execução demonstrada** do programa com entradas válidas e ao menos um teste adicional (múltiplo e não múltiplo), além de evidência de tratamento de entrada inválida quanto à positividade.
- **Descrição escrita breve** (ou texto equivalente) explicitando: (i) como a entrada é validada; (ii) qual regra é usada para verificar se é múltiplo de 27.
- **Explicação oral curta (opcional)** sobre o raciocínio e decisões de implementação.

## Contexto de Aquisição (curso, organização, ambiente, avaliação)
- **Curso/Nível**: curso técnico na área de Informática, em unidade introdutória.
- **Componente curricular**: Lógica de Programação / Programação em C.
- **Ambiente**: laboratório de informática ou ambiente local com compilador C (ex.: GCC) e execução em terminal/console.
- **Organização**: preferencialmente individual; quando em dupla (programação em pares), preserva-se a responsabilização individual pela explicação do que foi implementado.
- **Avaliação**: individual, baseada no funcionamento do programa e na justificativa (escrita e/ou oral).

## Perfil do Público-Alvo (nível, pré-requisitos, necessidades)
- **Nível**: iniciantes em programação estruturada na linguagem C.
- **Pré-requisitos**: noções de variáveis e tipos inteiros; entrada/saída; estruturas condicionais; noção de divisibilidade; noções básicas de teste.
- **Necessidades típicas**: apoio para transformar requisitos em condição computável, organizar fluxo mínimo do programa e comunicar resultados com clareza.

## Escala de Proficiência (critérios e dimensões)
Escala **0,0–10,0** com incrementos de **0,1**, baseada em três dimensões coerentes com a avaliação prevista:

- **Dimensão Técnica (0–10)**: compila/executa; valida positividade; determina corretamente múltiplo de 27; mensagens finais corretas e inequívocas.
- **Dimensão Cognitiva (0–10)**: explica a regra usada (divisibilidade via condição computacional), justifica a validação de positividade e interpreta casos testados.
- **Dimensão Atitudinal (0–10)**: responsabilidade e autonomia; postura ética/autoria; comunicação respeitosa e colaborativa quando houver trabalho em pares.

---

# 2. Enumeração de Conhecimentos

## 2.1 Fundamentos de Programação em C
**K1 – Tipos inteiros e variáveis**
- Declaração e uso de variáveis inteiras para armazenar o valor informado.
- Relação entre tipo de dado e validade da leitura/armazenamento do número.
- Noção de valor positivo (maior que zero) aplicada ao domínio do problema.

**K2 – Entrada e saída em programas C (interação em console)**
- Solicitação de dado ao usuário e leitura do valor informado.
- Emissão de mensagens claras para orientar entrada e comunicar resultado.
- Consistência entre o que é solicitado e o que é processado/exibido.

## 2.2 Aritmética Computacional e Divisibilidade
**K3 – Operações aritméticas e operador de resto**
- Uso de uma operação computacional para identificar divisibilidade.
- Interpretação do resto como indicador de múltiplo (resto igual a zero).
- Relação entre cálculo e decisão final do programa.

**K4 – Conceito de múltiplo e critério de divisibilidade**
- Definição operacional: um número é múltiplo de 27 quando é divisível por 27.
- Conexão entre conceito matemático e condição verificável no programa.
- Reconhecimento de casos típicos (múltiplo vs. não múltiplo) para teste.

## 2.3 Controle de Fluxo e Validação
**K5 – Estruturas condicionais**
- Tomada de decisão baseada em comparação/condição (válido vs. inválido; múltiplo vs. não múltiplo).
- Encadeamento mínimo de decisões para garantir comportamento coerente.
- Clareza de ramificações e suas saídas.

**K6 – Validação de entrada (positividade) e tratamento de caso inválido**
- Critério de validação: aceitar somente valores inteiros positivos.
- Estratégia de resposta a entradas fora do requisito (recusar/orientar).
- Impacto da validação na confiabilidade do resultado final.

## 2.4 Testes, Qualidade e Comunicação
**K7 – Testes com casos representativos**
- Seleção de entradas para cobrir resultados possíveis (múltiplo e não múltiplo).
- Inclusão de caso inválido quanto à positividade para verificar tratamento.
- Relação entre teste e confirmação do comportamento esperado.

**K8 – Legibilidade e organização básica do código**
- Indentação e organização do fluxo para facilitar leitura e manutenção.
- Nomeação coerente e consistência textual nas mensagens.
- Clareza estrutural como suporte à explicação do programa.

**K9 – Comunicação técnica e autoria**
- Descrição breve e objetiva da regra adotada e da validação realizada.
- Explicação oral curta, quando solicitada, com vocabulário adequado.
- Evidência de autoria por meio da justificativa do raciocínio e decisões.

**Nota Analítica (curadoria dos conhecimentos):**  
Os conhecimentos foram selecionados por serem **diretamente mobilizados** pela tarefa (entrada/saída, inteiros, validação, divisibilidade via condição computacional e decisão condicional), e por sustentarem **evidências observáveis** previstas (código executável, testes demonstrados e explicação do critério). Elementos não exigidos explicitamente (p.ex., modularização avançada) foram evitados para manter aderência estrita ao escopo descrito.

---

# 3. Identificação de Objetivos de Aprendizagem

**LO1 – Identificar** os requisitos do problema (inteiro, positividade e múltiplo de 27) e **organizar** o fluxo mínimo da solução (entrada → validação → verificação → saída).  
**LO2 – Implementar** a leitura de um número inteiro e **apresentar** mensagens de interação e resultado de forma clara e inequívoca.  
**LO3 – Validar** a entrada quanto à positividade e **tratar** o caso inválido de modo coerente com o requisito da tarefa.  
**LO4 – Determinar** se o valor informado é múltiplo de 27 por meio de uma condição computacional derivada do conceito de divisibilidade.  
**LO5 – Testar** o programa com casos representativos (múltiplo, não múltiplo e inválido quanto à positividade) e **corrigir** inconsistências identificadas.  
**LO6 – Explicar** (por escrito e/ou oralmente) a regra utilizada para a verificação de múltiplo e a justificativa da validação de entrada.

**Nota Analítica:**  
Os LOs usam verbos **observáveis e avaliáveis** e se conectam diretamente às evidências previstas: funcionamento do programa (Aplicar), validação e decisão (Aplicar/Analisar), testes (Avaliar em nível introdutório por checagem de comportamento), e explicação do raciocínio (Compreender/Analisar). Essa formulação favorece rastreabilidade entre requisitos, execução demonstrada e justificativa do estudante.

---

# 4. Definição de Competências

## 4.1 Competência Geral (BNCC – quando aplicável)
**(BNCC não utilizada nesta task)**  
Competência geral do domínio: **analisar um enunciado, implementar uma solução computacional simples e justificá-la**, articulando validação de dados, decisão condicional e comunicação clara do resultado.

---

## 4.2 Especificações de Competências

### CT25.21.1 — Interpretar requisitos e explicitar critérios de validação e decisão

#### Título da Competência
Interpretar requisitos do problema e explicitar critérios de validação e decisão.

#### Descrição Textual
O estudante analisa o enunciado para identificar restrições (inteiro; positivo) e o objetivo lógico (verificar múltiplo de 27), transformando-os em critérios operacionais que orientam o fluxo do programa e a comunicação do resultado ao usuário.

#### Especificação de Conhecimentos
- **K4 (múltiplo/divisibilidade)**: traduz o conceito de múltiplo em condição verificável.
  - **Bloom (revisada):** Analisar → Aplicar  
  - **Pareamento Conhecimento–Habilidade:** Divisibilidade → formular critério de decisão computável  
  - **Anotação de Verbos:** identificar, interpretar, traduzir, definir
- **K6 (validação de entrada)**: explicita o critério “positivo” como condição obrigatória antes da verificação.
  - **Bloom (revisada):** Analisar → Aplicar  
  - **Pareamento Conhecimento–Habilidade:** Validação → definir regra de aceitação/recusa  
  - **Anotação de Verbos:** delimitar, justificar, estabelecer, orientar

#### Especificação de Disposições
- **Rigor** na interpretação do enunciado e completude de requisitos.
- **Responsabilidade** ao definir critérios que garantam resultado confiável.
- **Clareza comunicacional** ao explicitar regras e resultados.

#### Competências Alinhadas à BNCC (quando aplicável)
Não aplicável (BNCC não utilizada nesta task).

#### Tabela-Resumo
| Código | Competência | Disposições | Conhecimento | Habilidade |
|---|---|---|---|---|
| CT25.21.1 | Interpretar requisitos e explicitar critérios de validação e decisão | Rigor; Responsabilidade; Clareza comunicacional | K4; K6 | Identificar e traduzir requisitos em critérios operacionais |

#### Definição de Ativação (Activation Definition)
- **ActivationConstraint:** obrigatória  
- **ActivationMode:** analítica  
- **ActivationRole:** apoio  
Justificativa: a tarefa depende de interpretar corretamente “inteiro e positivo” e “múltiplo de 27” para orientar validação e decisão; isso sustenta, mas não substitui, a construção do artefato executável.

---

### CT25.21.2 — Implementar interação por entrada/saída com mensagens claras

#### Título da Competência
Implementar interação por entrada/saída com mensagens claras e consistentes.

#### Descrição Textual
O estudante implementa a solicitação do número e apresenta mensagens que orientam o usuário e comunicam o resultado de forma inequívoca, assegurando alinhamento entre dado lido, processamento e saída exibida.

#### Especificação de Conhecimentos
- **K2 (entrada/saída)**: realiza leitura do inteiro e impressão de mensagens.
  - **Bloom (revisada):** Aplicar  
  - **Pareamento Conhecimento–Habilidade:** E/S → implementar interação em console  
  - **Anotação de Verbos:** solicitar, ler, exibir, comunicar
- **K1 (tipos inteiros/variáveis)**: usa variável inteira apropriada ao dado.
  - **Bloom (revisada):** Aplicar  
  - **Pareamento Conhecimento–Habilidade:** Tipos → armazenar e usar valor corretamente  
  - **Anotação de Verbos:** declarar, armazenar, utilizar

#### Especificação de Disposições
- **Atenção a detalhes** na consistência das mensagens.
- **Empatia técnica** (orientar o usuário sem ambiguidade).
- **Organização** na apresentação do resultado.

#### Competências Alinhadas à BNCC (quando aplicável)
Não aplicável (BNCC não utilizada nesta task).

#### Tabela-Resumo
| Código | Competência | Disposições | Conhecimento | Habilidade |
|---|---|---|---|---|
| CT25.21.2 | Implementar interação por entrada/saída com mensagens claras | Atenção a detalhes; Empatia técnica; Organização | K1; K2 | Ler dados e comunicar resultados com clareza |

#### Definição de Ativação (Activation Definition)
- **ActivationConstraint:** obrigatória  
- **ActivationMode:** construtiva  
- **ActivationRole:** núcleo  
Justificativa: há exigência explícita de solicitar entrada e exibir resultado; a evidência principal (programa executável) depende diretamente da implementação de E/S e mensagens claras.

---

### CT25.21.3 — Validar a positividade da entrada e tratar casos inválidos

#### Título da Competência
Validar a positividade da entrada e tratar casos inválidos de forma coerente.

#### Descrição Textual
O estudante verifica se o valor informado atende ao requisito de ser positivo e define o comportamento do programa para o caso inválido, recusando-o e orientando o usuário, conforme o nível de robustez previsto na tarefa.

#### Especificação de Conhecimentos
- **K6 (validação e tratamento de inválidos)**: implementa critério de aceitação/recusa para positividade.
  - **Bloom (revisada):** Aplicar  
  - **Pareamento Conhecimento–Habilidade:** Validação → implementar checagem e resposta  
  - **Anotação de Verbos:** validar, recusar, orientar, assegurar
- **K5 (condicionais)**: estrutura a ramificação para caso válido vs. inválido.
  - **Bloom (revisada):** Aplicar  
  - **Pareamento Conhecimento–Habilidade:** Condicionais → controlar fluxo por condição  
  - **Anotação de Verbos:** decidir, selecionar, direcionar

#### Especificação de Disposições
- **Responsabilidade** com requisitos do enunciado.
- **Rigor** ao evitar resultados indevidos em caso inválido.
- **Cuidado com qualidade** (robustez básica).

#### Competências Alinhadas à BNCC (quando aplicável)
Não aplicável (BNCC não utilizada nesta task).

#### Tabela-Resumo
| Código | Competência | Disposições | Conhecimento | Habilidade |
|---|---|---|---|---|
| CT25.21.3 | Validar a positividade da entrada e tratar casos inválidos | Responsabilidade; Rigor; Cuidado com qualidade | K5; K6 | Implementar validação e ramificação coerente |

#### Definição de Ativação (Activation Definition)
- **ActivationConstraint:** obrigatória  
- **ActivationMode:** construtiva  
- **ActivationRole:** núcleo  
Justificativa: a tarefa exige explicitamente número inteiro **positivo** e prevê tratamento para entrada fora do requisito; a validação é parte central do comportamento esperado.

---

### CT25.21.4 — Determinar multiplicidade de 27 por condição computacional

#### Título da Competência
Determinar se um inteiro é múltiplo de 27 por condição computacional.

#### Descrição Textual
O estudante aplica o conceito de divisibilidade para construir uma verificação computacional de múltiplo de 27, garantindo decisão correta e mensagem final compatível com o resultado calculado.

#### Especificação de Conhecimentos
- **K3 (operador de resto/aritmética computacional)**: usa a condição de resto para identificar divisibilidade.
  - **Bloom (revisada):** Aplicar  
  - **Pareamento Conhecimento–Habilidade:** Resto/divisão → computar condição de múltiplo  
  - **Anotação de Verbos:** calcular, verificar, comparar, determinar
- **K4 (divisibilidade/múltiplos)**: justifica a regra adotada como critério matemático.
  - **Bloom (revisada):** Compreender → Aplicar  
  - **Pareamento Conhecimento–Habilidade:** Divisibilidade → explicar e aplicar o critério  
  - **Anotação de Verbos:** explicar, relacionar, aplicar

#### Especificação de Disposições
- **Precisão** no raciocínio lógico-matemático.
- **Atenção a detalhes** para evitar decisões incorretas.
- **Confiança epistêmica** (basear a decisão em regra justificável).

#### Competências Alinhadas à BNCC (quando aplicável)
Não aplicável (BNCC não utilizada nesta task).

#### Tabela-Resumo
| Código | Competência | Disposições | Conhecimento | Habilidade |
|---|---|---|---|---|
| CT25.21.4 | Determinar multiplicidade de 27 por condição computacional | Precisão; Atenção a detalhes; Confiança epistêmica | K3; K4 | Calcular e decidir sobre divisibilidade (múltiplo vs. não múltiplo) |

#### Definição de Ativação (Activation Definition)
- **ActivationConstraint:** obrigatória  
- **ActivationMode:** construtiva  
- **ActivationRole:** núcleo  
Justificativa: o objetivo principal da tarefa é verificar se o número é múltiplo de 27; a competência corresponde diretamente ao núcleo funcional do programa e às evidências de teste.

---

### CT25.21.5 — Testar o programa com casos representativos e depurar inconsistências

#### Título da Competência
Testar o programa com casos representativos e depurar inconsistências.

#### Descrição Textual
O estudante seleciona entradas de teste que cubram resultados esperados (múltiplo, não múltiplo e inválido quanto à positividade), executa o programa e ajusta a solução quando identifica divergências entre comportamento obtido e comportamento esperado.

#### Especificação de Conhecimentos
- **K7 (testes representativos)**: planeja e executa testes coerentes com os critérios da atividade.
  - **Bloom (revisada):** Avaliar (nível introdutório: checar comportamento)  
  - **Pareamento Conhecimento–Habilidade:** Testes → verificar comportamento e consistência  
  - **Anotação de Verbos:** testar, verificar, comparar, corrigir
- **K8 (legibilidade/organização)**: melhora rastreabilidade ao revisar fluxo e mensagens.
  - **Bloom (revisada):** Aplicar  
  - **Pareamento Conhecimento–Habilidade:** Organização → ajustar clareza e reduzir erros  
  - **Anotação de Verbos:** revisar, ajustar, aprimorar

#### Especificação de Disposições
- **Persistência** na correção de falhas.
- **Autonomia** na verificação do próprio trabalho.
- **Postura crítica** ao confrontar resultados com critérios.

#### Competências Alinhadas à BNCC (quando aplicável)
Não aplicável (BNCC não utilizada nesta task).

#### Tabela-Resumo
| Código | Competência | Disposições | Conhecimento | Habilidade |
|---|---|---|---|---|
| CT25.21.5 | Testar o programa e depurar inconsistências | Persistência; Autonomia; Postura crítica | K7; K8 | Selecionar testes, executar, comparar resultados e corrigir |

#### Definição de Ativação (Activation Definition)
- **ActivationConstraint:** obrigatória  
- **ActivationMode:** analítica  
- **ActivationRole:** apoio  
Justificativa: a própria descrição prevê testes com entradas representativas e revisão final; essa competência sustenta a confiabilidade do artefato e a evidência de correção, embora o núcleo esteja na implementação.

---

### CT25.21.6 — Justificar a solução e demonstrar autoria com comunicação técnica adequada

#### Título da Competência
Justificar a solução e demonstrar autoria com comunicação técnica adequada.

#### Descrição Textual
O estudante descreve (e, quando solicitado, explica oralmente) como realizou a validação e qual regra usou para verificar múltiplo de 27, evidenciando compreensão e autoria por meio de argumentação concisa, vocabulário apropriado e alinhamento com o comportamento do programa.

#### Especificação de Conhecimentos
- **K9 (comunicação técnica e autoria)**: explicita raciocínio e decisões de implementação.
  - **Bloom (revisada):** Compreender → Analisar  
  - **Pareamento Conhecimento–Habilidade:** Comunicação → explicar e justificar decisões  
  - **Anotação de Verbos:** explicar, justificar, descrever, evidenciar
- **K4/K6 (divisibilidade e validação)**: sustenta a justificativa da regra e do critério de entrada.
  - **Bloom (revisada):** Compreender → Aplicar  
  - **Pareamento Conhecimento–Habilidade:** Conceitos → articular justificativa coerente  
  - **Anotação de Verbos:** relacionar, fundamentar, argumentar

#### Especificação de Disposições
- **Ética/autoria** (transparência sobre o que foi feito e por quê).
- **Clareza** na explicação do raciocínio.
- **Responsabilidade acadêmica** ao alinhar discurso e evidência (execução/código).

#### Competências Alinhadas à BNCC (quando aplicável)
Não aplicável (BNCC não utilizada nesta task).

#### Tabela-Resumo
| Código | Competência | Disposições | Conhecimento | Habilidade |
|---|---|---|---|---|
| CT25.21.6 | Justificar a solução e demonstrar autoria | Ética/autoria; Clareza; Responsabilidade acadêmica | K4; K6; K9 | Explicar e justificar regra e validação com base na evidência do programa |

#### Definição de Ativação (Activation Definition)
- **ActivationConstraint:** obrigatória  
- **ActivationMode:** justificatória  
- **ActivationRole:** núcleo  
Justificativa: a avaliação prevista inclui descrição escrita e pode incluir explicação oral; a competência é ativada diretamente quando o estudante justifica a validação e a regra de múltiplo, demonstrando compreensão e autoria.

---
