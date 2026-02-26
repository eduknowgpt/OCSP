# Relatório CSP — Autoria de Competências (Competency Authoring)

## Introdução
Este relatório documenta a fase de **Autoria de Competências** no contexto do CSP, especificando **Conhecimentos (K)**, **Objetivos de Aprendizagem (LO)** e **Competências (CT)** elicitas por uma tarefa introdutória de programação. A tarefa solicita a implementação de um programa que **lê entradas**, **decide a saída por condição** e **imprime resultados**, incluindo **cálculo numérico** em casos específicos.  
As evidências são observáveis porque o estudante produz um **artefato executável (código)**, **saídas de execução** e uma **justificativa breve** vinculada ao comportamento do programa.  
O modelo **K–S–D** é suportado porque: (i) há conhecimentos de computação mobilizados (representação de dados, controle de fluxo, E/S, expressões), (ii) há habilidades verificáveis no produto (construção do programa e verificação por testes) e (iii) disposições pertinentes (precisão, postura de verificação) aparecem como qualidades do processo e da entrega, sem se confundirem com conhecimento.

---

# 1. Análise da Entidade Instrucional

## Título
**TASK26.05 — Identificação de Polígono Regular e Saída Condicional**

## Descrição
A tarefa requer que o estudante implemente um programa que lê **número de lados** e **medida do lado (cm)** e, com base no número de lados, imprima o rótulo do polígono solicitado e, quando exigido, um **valor numérico** associado ao caso (área). Também exige **justificativa breve** explicando a regra de decisão aplicada e o que foi impresso.

## Processo de Desenvolvimento da Solução (em etapas)
1. Interpretar a especificação de entradas e saídas (quais valores ler; quais mensagens/valores imprimir).
2. Representar adequadamente os dados de entrada (inteiro para lados; numérico para medida).
3. Estruturar seleção condicional para distinguir os casos previstos (3, 4, 5).
4. Implementar o cálculo numérico **apenas** nos casos em que a especificação exige valor de área.
5. Produzir saída textual e numérica de forma verificável.
6. Executar testes mínimos para os casos previstos e registrar evidências.
7. Redigir justificativa breve baseada no comportamento observado (saídas/testes).

## Resultados Esperados (lista de produtos e evidências)
- Código-fonte do programa.
- Saídas de execução (registros) com ao menos um teste para: 3, 4 e 5 lados.
- Justificativa breve (2–5 linhas) conectando entrada → caso selecionado → saída produzida.

## Contexto de Aquisição (curso, organização, ambiente, avaliação)
- **Curso/Nível:** Introdução à Programação (nível introdutório; compatível com formação técnica ou inicial em computação).
- **Organização:** Individual.
- **Ambiente:** Laboratório de informática ou ambiente de desenvolvimento local/online.
- **Avaliação:** Baseada em artefato (código), evidências de execução (testes/saídas) e justificativa breve.

## Perfil do Público-Alvo (nível, pré-requisitos, necessidades)
- **Nível:** Iniciante em programação.
- **Pré-requisitos mínimos:** leitura de entrada, tipos numéricos básicos, expressões aritméticas, estruturas condicionais simples, impressão de saída.
- **Necessidades típicas:** apoio na interpretação de especificações e na verificação por testes (casos previstos e consistência de execução).

## Escala de Proficiência

**Dimensões avaliadas**
1. Correção do comportamento para casos previstos (3, 4, 5).
2. Consistência de tipos/expressões numéricas e impressão do resultado quando exigido.
3. Verificabilidade: presença e adequação de testes/saídas registradas.
4. Clareza mínima: justificativa breve coerente com evidências.

**Níveis**
- **N1 — Inicial:** Implementa parcialmente; falhas em distinguir casos e/ou ausência de evidências de teste.
- **N2 — Básico:** Distingue casos previstos; cálculo/saída com inconsistências pontuais; evidências mínimas incompletas.
- **N3 — Proficiente:** Casos previstos corretos; cálculo/saída consistentes; testes cobrindo 3, 4 e 5; justificativa coerente.
- **N4 — Avançado:** Além do N3, demonstra robustez (execução consistente) e justificativa especialmente precisa e aderente às evidências.

---

# 2. Enumeração de Conhecimentos

## Interação / Entrada–Saída
**K1. Entrada de dados e atribuição a variáveis**
- Leitura de valores de entrada e armazenamento em variáveis com tipos apropriados.
- Relação entre entrada recebida e estado interno do programa.
- Mobilizado para obter `número de lados` e `medida do lado` antes da decisão.
- Observável por meio do código e das execuções registradas.

**K2. Saída textual e numérica conforme especificação**
- Produção de mensagens e valores numéricos na saída do programa.
- Organização mínima da saída para permitir conferência (rótulo + valor quando exigido).
- Mobilizado nos três casos (3, 4, 5), com variação do conteúdo impresso.
- Observável pela saída capturada e coerência com o enunciado.

## Controle de Fluxo
**K3. Seleção condicional com múltiplos ramos**
- Estruturas de decisão para selecionar comportamentos distintos a partir de uma condição.
- Encadeamento/ramificação para tratar casos mutuamente exclusivos.
- Mobilizado para distinguir 3, 4 e 5 lados.
- Observável pela estrutura do controle de fluxo e pela correspondência com as saídas.

**K4. Tratamento de casos não especificados (consistência de execução)**
- Noções de fluxo padrão/alternativo quando a especificação não cobre determinadas entradas.
- Garantia de execução consistente (sem produzir resultados indevidos).
- Mobilizado porque o enunciado define comportamento apenas para 3, 4 e 5.
- Observável por ausência de efeitos inesperados e por escolhas coerentes no código.

## Expressões e Cálculo Computacional
**K5. Expressões aritméticas e precedência operacional**
- Construção e avaliação de expressões numéricas.
- Uso correto de operadores e agrupamentos para preservar a intenção do cálculo.
- Mobilizado no cálculo numérico exigido nos casos de 3 e 4 lados.
- Observável pela correção do valor impresso e pela forma da expressão implementada.

**K6. Funções matemáticas e tipos numéricos (precisão/representação)**
- Uso de tipos numéricos adequados (inteiro vs. real) em cálculos.
- Emprego de funções matemáticas quando necessárias ao cálculo (biblioteca padrão, quando aplicável).
- Mobilizado porque o resultado pode ser não inteiro.
- Observável por escolha de tipos e pela impressão de valores plausíveis.

## Verificação
**K7. Testes de casos e comparação com especificação**
- Seleção de entradas representativas para cobrir ramos de decisão.
- Comparação entre saída obtida e saída esperada pela especificação.
- Mobilizado pela exigência de registros de execução para 3, 4 e 5 lados.
- Observável nas evidências anexadas (saídas/testes) e na justificativa breve.



# 3. Identificação de Objetivos de Aprendizagem

**LO1.** Implementar leitura de múltiplas entradas e armazená-las em variáveis com tipos adequados.  
**LO2.** Aplicar seleção condicional para produzir saídas distintas a partir de uma especificação baseada em casos.  
**LO3.** Realizar cálculo numérico por meio de expressões computacionais e produzir saída numérica verificável quando requisitado.  
**LO4.** Planejar e executar testes que cubram ramos de decisão e registrar evidências de execução.  
**LO5.** Justificar brevemente decisões de controle de fluxo e resultados observados, com base em evidências (entradas/saídas).

### Nota Analítica
Os LOs foram formulados com verbos observáveis (implementar, aplicar, realizar, planejar/executar, justificar) e permanecem suficientemente amplos para reutilização em tarefas análogas de programação baseada em especificação. A progressão cognitiva é coerente: aplicação/implementação (LO1–LO3), verificação (LO4) e justificativa baseada em evidências (LO5), sem inflar níveis além do exigido.


# 4. Definição de Competências

## 4.1 Competência Geral 
**Competência Geral (Computação):** Desenvolver soluções computacionais simples que, a partir de entradas, executem decisões e cálculos e produzam saídas verificáveis, sustentando o processo com testes e justificativas baseadas em evidências.

**Alinhamento BNCC :** Relaciona-se de modo plausível a dimensões de **pensamento computacional** (estruturação de algoritmos, decomposição em casos, verificação) e **mundo digital** no que tange à programação e produção de artefatos executáveis. *A etapa (EF/EM) não está explicitada na entrada, portanto não se usam códigos.*

---

## 4.2 Especificações de Competências

### CT01.01.1 — Implementar decisão por casos com entrada e saída especificadas
**Descrição Textual**  
Capacidade de construir um programa que lê entradas, seleciona o comportamento correto para casos mutuamente exclusivos e imprime a saída textual exigida, de forma consistente com a especificação.

**Especificação de Conhecimentos**
- **K1:** leitura e atribuição de entradas a variáveis.
- **K2:** impressão de saída textual/numerada conforme especificação.
- **K3:** seleção condicional multi-ramo para casos mutuamente exclusivos.

**Alinhamento com a Taxonomia de Bloom (revisada)**
- **Processo cognitivo:** **Criar** (construir o artefato/programa) com suporte de **Aplicar** (uso de estruturas condicionais).
- **Tipo de conhecimento:** Procedimental (estruturas e uso) e conceitual (noção de ramificação).

**Pareamento Conhecimento–Habilidade**
- (K1, K3) → selecionar o ramo correto a partir das entradas lidas.
- (K2, K3) → produzir saída coerente com o ramo selecionado.

**Anotação de Verbos (lista)**
- implementar; ler; decidir; selecionar; imprimir.

**Especificação de Disposições**
- Precisão ao seguir a especificação de saída.
- Rigor ao tratar casos como mutuamente exclusivos.
- Postura de verificação mínima (conferir se a saída corresponde ao caso).
- Cuidado com consistência de execução.

**Competências Alinhadas à BNCC (quando aplicável)**
- Alinhamento geral a pensamento computacional: definição de regras/casos e execução algorítmica baseada em condições.

**Tabela-Resumo**
| Código | Competência | Disposições | Conhecimento | Habilidade |
|---|---|---|---|---|
| CT01.01.1 | Implementar decisão por casos com E/S | precisão; rigor; verificação; consistência | K1, K2, K3 | ler entradas; selecionar ramo; imprimir saída |

**Definição de Ativação**
- **Restrição de ativação:** obrigatória  
- **Modo de ativação:** construtiva  
- **Função de ativação:** núcleo  
- **Justificativa:** A tarefa exige necessariamente a implementação do programa e a produção de saídas distintas por condição; isso é o núcleo observável do artefato entregue e estrutura toda a evidência.

---

### CT01.01.2 — Integrar cálculo numérico ao comportamento do programa quando requerido
**Descrição Textual**  
Capacidade de incorporar ao programa cálculos numéricos definidos pela especificação, garantindo tipos apropriados e impressão de resultado verificável nos casos em que o valor é exigido.

**Especificação de Conhecimentos**
- **K5:** construção/avaliação de expressões aritméticas com precedência adequada.
- **K6:** tipos numéricos e, quando aplicável, funções matemáticas para cálculo e precisão.
- **K2:** apresentação de saída numérica verificável.

**Alinhamento com a Taxonomia de Bloom (revisada)**
- **Processo cognitivo:** **Aplicar** (aplicar expressões e tipos corretamente) com componente de **Criar** (integrar o cálculo ao programa implementado).
- **Tipo de conhecimento:** Procedimental (operações/tipos) e conceitual (representação numérica).

**Pareamento Conhecimento–Habilidade**
- (K5, K6) → produzir cálculo numérico consistente com o caso selecionado.
- (K2) → apresentar resultado numérico de forma conferível.

**Anotação de Verbos (lista)**
- calcular; aplicar; integrar; representar; imprimir.

**Especificação de Disposições**
- Atenção à precisão e consistência numérica.
- Cautela ao lidar com valores não inteiros.
- Compromisso com verificabilidade do resultado (não “ocultar” cálculo).
- Rigor em calcular apenas quando a especificação exige.

**Competências Alinhadas à BNCC (quando aplicável)**
- Alinhamento geral: uso de abstração e representação numérica em soluções computacionais simples.

**Tabela-Resumo**
| Código | Competência | Disposições | Conhecimento | Habilidade |
|---|---|---|---|---|
| CT01.01.2 | Integrar cálculo numérico quando requerido | precisão; cautela; verificabilidade; rigor | K2, K5, K6 | calcular; usar tipos; imprimir resultado |

**Definição de Ativação**
- **Restrição de ativação:** obrigatória  
- **Modo de ativação:** construtiva  
- **Função de ativação:** núcleo  
- **Justificativa:** O enunciado exige valor numérico (área) para casos específicos; a competência é central porque o comportamento correto depende da integração entre cálculo, tipos e impressão.

---

### CT01.01.3 — Verificar comportamento do programa por testes de casos previstos
**Descrição Textual**  
Capacidade de planejar e executar testes que cubram os ramos de decisão previstos (3, 4 e 5 lados), registrando evidências de execução e confrontando-as com a especificação.

**Especificação de Conhecimentos**
- **K7:** seleção de casos de teste e comparação com especificação.
- **K3:** compreensão do particionamento por ramos (para orientar cobertura).
- **K2:** leitura/interpretação das saídas produzidas.

**Alinhamento com a Taxonomia de Bloom (revisada)**
- **Processo cognitivo:** **Avaliar** (confrontar saídas com a especificação) e **Analisar** (relacionar entradas a ramos e resultados).
- **Tipo de conhecimento:** Procedimental (teste) e conceitual (cobertura por casos).

**Pareamento Conhecimento–Habilidade**
- (K3, K7) → escolher entradas que ativem cada ramo.
- (K2, K7) → comparar saída obtida com saída esperada e registrar evidências.

**Anotação de Verbos (lista)**
- testar; verificar; comparar; registrar; cobrir.

**Especificação de Disposições**
- Postura sistemática de verificação (não confiar apenas na implementação).
- Honestidade acadêmica ao registrar evidências reais de execução.
- Persistência ao ajustar até obter comportamento conforme especificação.
- Organização mínima na apresentação dos testes.

**Competências Alinhadas à BNCC (quando aplicável)**
- Alinhamento geral: verificação e depuração como prática de pensamento computacional.

**Tabela-Resumo**
| Código | Competência | Disposições | Conhecimento | Habilidade |
|---|---|---|---|---|
| CT01.01.3 | Verificar por testes e evidências | sistematicidade; honestidade; persistência; organização | K2, K3, K7 | testar ramos; comparar saídas; registrar evidências |

**Definição de Ativação**
- **Restrição de ativação:** obrigatória  
- **Modo de ativação:** analítica  
- **Função de ativação:** núcleo  
- **Justificativa:** A tarefa exige explicitamente registros de execução para casos previstos; a competência é núcleo porque torna o desempenho **observável e auditável**, sustentando a avaliação.

---

### CT01.01.4 — Justificar decisões e resultados com base em evidências de execução
**Descrição Textual**  
Capacidade de produzir uma justificativa breve que explique a regra de decisão aplicada e relacione entradas, ramo executado e saída observada, sem extrapolar além do que as evidências suportam.

**Especificação de Conhecimentos**
- **K3:** estrutura de decisão (para explicar seleção de ramos).
- **K2:** natureza da saída produzida (o que foi impresso e por quê).
- **K7:** vínculo entre teste, evidência e conclusão.

**Alinhamento com a Taxonomia de Bloom (revisada)**
- **Processo cognitivo:** **Analisar** (relacionar causa–efeito: entrada → ramo → saída) e **Explicar** em nível operacional.
- **Tipo de conhecimento:** Conceitual (ramos/saída) e procedimental (uso de evidências).

**Pareamento Conhecimento–Habilidade**
- (K3, K2) → descrever de forma concisa o comportamento selecionado e a saída correspondente.
- (K7) → sustentar a justificativa com evidências (saídas registradas), evitando afirmações não verificadas.

**Anotação de Verbos (lista)**
- justificar; explicar; relacionar; evidenciar; sustentar.

**Especificação de Disposições**
- Clareza e concisão técnica.
- Responsabilidade epistêmica (afirmar apenas o que as evidências sustentam).
- Rigor ao evitar “explicações soltas” sem vínculo com entradas/saídas.
- Atenção a detalhes relevantes (caso selecionado e resultado observado).

**Competências Alinhadas à BNCC (quando aplicável)**
- Alinhamento geral: comunicação de raciocínio computacional baseada em evidências e verificação.

**Tabela-Resumo**
| Código | Competência | Disposições | Conhecimento | Habilidade |
|---|---|---|---|---|
| CT01.01.4 | Justificar com evidências de execução | concisão; responsabilidade; rigor; atenção | K2, K3, K7 | relacionar entrada–ramo–saída; sustentar com evidências |

**Definição de Ativação**
- **Restrição de ativação:** obrigatória  
- **Modo de ativação:** justificatória  
- **Função de ativação:** apoio  
- **Justificativa:** A justificativa não substitui o artefato, mas apoia a avaliação ao tornar explícito o raciocínio do estudante e sua aderência às evidências registradas.

