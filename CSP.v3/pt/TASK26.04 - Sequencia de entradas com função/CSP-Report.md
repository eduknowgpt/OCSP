# Relatório CSP — Autoria de Competências (Competency Authoring)

## Introdução
Este relatório se insere na fase de **Autoria de Competências** do **Competency Specification Process (CSP)**, com o objetivo de especificar, de forma rastreável, os **Conhecimentos (K)**, **Objetivos de Aprendizagem (LO)** e **Competências (CT)** elicitados por uma tarefa introdutória de programação, estruturados no modelo **K–S–D**.

A tarefa solicita que o estudante **leia um valor n**, em seguida **leia n números** e **calcule o fatorial de cada entrada**, com a exigência explícita de que o cálculo do fatorial seja realizado por **uma função**. As evidências são observáveis por meio do **artefato executável (código/pseudocódigo formal)**, das **saídas produzidas** e de **registros de teste**, além de uma **justificativa breve** sobre decisões técnicas e organização.

O modelo **K–S–D** é suportado porque: (i) há conhecimentos computacionais mobilizados (entrada/saída, controle de fluxo, funções, tipos e limites), (ii) há habilidades operacionais diretamente observáveis (construir solução, modularizar, tratar casos e verificar), e (iii) disposições necessárias à qualidade (precisão, verificação e rigor) sem confundi-las com conhecimento de domínio.



## 1. Análise da Entidade Instrucional

### Título
**TASK26.04 — Cálculo de Fatorial para uma Sequência de Entradas com Função**

### Descrição
A tarefa requer a construção de uma solução que:
- leia um inteiro **n** indicando quantas entradas serão processadas;
- leia **n** valores e calcule o **fatorial** de cada valor;
- realize o cálculo do fatorial **obrigatoriamente por uma função**;
- apresente resultados de forma verificável e com breve justificativa sobre decisões adotadas.

### Processo de Desenvolvimento da Solução
1. **Compreensão do enunciado** e identificação dos artefatos exigidos (função, processamento de n entradas, saída verificável).
2. **Planejamento da estrutura** do programa/algoritmo (fluxo principal + função para fatorial).
3. **Implementação do controle de processamento** de exatamente **n** entradas.
4. **Implementação da função** dedicada ao cálculo do fatorial e integração com o fluxo principal.
5. **Tratamento consistente de casos de borda plausíveis** e registro de decisões quando houver ambiguidade técnica.
6. **Testes** com cenários mínimos e **registro** das evidências (entradas/saídas).
7. **Justificativa breve** sobre organização (papel da função, domínio adotado e limites, se aplicável).

### Resultados Esperados (lista de produtos e evidências)
- **Código-fonte** (ou pseudocódigo formal) com:
  - leitura de `n`;
  - leitura de `n` valores;
  - chamada à função de fatorial para cada valor;
  - apresentação dos resultados.
- **Registros de teste** (entradas e saídas) cobrindo:
  - caso envolvendo `0` ou `1`;
  - caso com valor maior que `1`;
  - caso com `n > 1`.
- **Justificativa breve** (3–6 linhas) sobre estrutura e decisões técnicas (domínio/limites, quando aplicável).

### Contexto de Aquisição (curso, organização, ambiente, avaliação)
- **Curso/nível:** disciplina introdutória de programação (nível inicial).
- **Organização:** atividade **individual**.
- **Ambiente:** laboratório com execução/compilação ou avaliação prática equivalente.
- **Avaliação:** baseada em artefato executável e evidências de teste + justificativa curta.

### Perfil do Público-Alvo (nível, pré-requisitos, necessidades)
- **Nível:** iniciantes em programação.
- **Pré-requisitos plausíveis:** noções de variáveis, leitura de entrada, estruturas de repetição e conceito básico de funções (parâmetros/retorno).
- **Necessidades típicas:** reforço de modularização (separação função vs. fluxo principal), controle de iteração por contador e atenção a casos de borda e verificabilidade por testes.

### Escala de Proficiência (critérios e dimensões)
Escala proposta (4 níveis) — dimensões: **correção funcional**, **modularização com função**, **tratamento de casos**, **verificabilidade por testes** e **clareza da justificativa**.

- **Nível 1 — Inicial:** processa parcialmente as entradas, função ausente ou inadequada, evidências de teste insuficientes.
- **Nível 2 — Básico:** processa `n` entradas e usa função, mas com inconsistências em casos de borda e/ou testes pouco informativos.
- **Nível 3 — Proficiente:** processa exatamente `n` entradas, função correta e integrada, casos de borda plausíveis tratados de forma consistente, testes mínimos registrados e justificativa coerente.
- **Nível 4 — Avançado:** além do proficiente, demonstra maior robustez (p.ex., decisões explícitas sobre domínio/limites numéricos quando necessário) e evidências de teste mais abrangentes e rastreáveis.


## 2. Enumeração de Conhecimentos

### Interação / Entrada–Saída e Rastreabilidade
**K1. Leitura controlada de entradas a partir de um contador (`n`)**
- Compreende a ideia de usar uma primeira entrada como parâmetro de quantidade.
- Mobiliza leitura sequencial e controle de quantas leituras ocorrerão.
- É observável pela coerência entre `n` informado e quantidade processada.

**K2. Apresentação de resultados com rastreabilidade entre entrada e saída**
- Conhece formas de tornar a saída verificável (correspondência clara entre valor lido e resultado).
- Sustenta a inspeção e conferência dos resultados gerados.
- Observável na estrutura da saída e nos registros de teste.

### Controle de Fluxo e Estado
**K3. Estruturas de repetição baseadas em contador**
- Entende repetição controlada por número de iterações conhecido.
- Mobiliza atualização de contador/condição de parada coerente.
- Observável pelo processamento de exatamente `n` valores.

**K4. Variáveis e estado de execução (acumulação e atualização)**
- Conhece o papel de variáveis para manter estado durante uma computação iterativa.
- Suporta padrões de inicialização e atualização em cálculos repetidos.
- Observável na consistência do cálculo e na ausência de dependência indevida entre entradas.

### Modularização
**K5. Funções: parâmetros, retorno e escopo**
- Entende encapsulamento de uma computação em função dedicada.
- Conhece passagem de valores por parâmetro e retorno de resultado.
- Observável pela existência de função específica de fatorial e seu uso no fluxo principal.

### Representações Numéricas e Casos de Borda
**K6. Tipos inteiros e limites de representação (crescimento rápido)**
- Reconhece que alguns resultados podem exceder limites do tipo numérico disponível.
- Sustenta decisões sobre tipos/limites e necessidade de documentá-los quando pertinente.
- Observável por escolhas registradas e comportamento consistente.

**K7. Casos de borda plausíveis e consistência de domínio**
- Conhece a necessidade de tratar entradas especiais (p.ex., `n = 0`, valores `0` e `1`) de modo coerente.
- Sustenta decisões quando o enunciado não explicita completamente o domínio das entradas.
- Observável no comportamento do programa e na justificativa breve.

### Depuração / Testes
**K8. Testes de caixa-preta e registro de evidências**
- Conhece o papel de escolher entradas representativas e registrar entradas/saídas.
- Sustenta verificabilidade sem depender de inspeção interna do código.
- Observável nos registros de teste solicitados e na coerência dos resultados.

**Nota Analítica:** Os conhecimentos foram curados para permanecerem **estritamente no domínio de Computação** (entrada/saída, controle de fluxo, funções, estado, tipos e testes). Elementos como “rigor”, “atenção” e “postura de verificação” foram alocados em **Disposições (D)**, evitando confundir K com S/D.


## 3. Identificação de Objetivos de Aprendizagem

**LO1.** Construir uma solução que processe uma quantidade variável de entradas controlada por um valor inicial (`n`).  
**LO2.** Encapsular uma computação repetida em uma função com parâmetros e retorno adequados.  
**LO3.** Integrar função e fluxo principal garantindo consistência do processamento para todas as entradas previstas.  
**LO4.** Identificar e tratar casos de borda plausíveis de forma consistente, registrando decisões técnicas quando necessário.  
**LO5.** Produzir e registrar testes de caixa-preta que permitam verificar o comportamento da solução.  


## 4. Definição de Competências

### 4.1 Competência Geral
**Competência Geral (Computação):** Desenvolver e validar soluções computacionais simples por meio de algoritmos e programas, com uso de abstrações básicas (funções e controle de fluxo) e verificação sistemática do comportamento por testes.

**Alinhamento BNCC (geral, sem códigos):** A tarefa se relaciona, de maneira defensável, a práticas de **pensamento computacional** e **programação** no componente de Computação, sobretudo na elaboração de algoritmos, implementação e verificação de soluções.



### 4.2 Especificações de Competências

> Convenção de códigos: **CT26.04.N** (N = 1..4)


#### CT26.04.1

##### Título da Competência
Implementar processamento iterativo de entradas controlado por contagem

##### Descrição Textual
Construir uma solução que leia um valor `n` e processe **exatamente `n` entradas subsequentes**, produzindo saídas verificáveis associadas às entradas.

##### Especificação de Conhecimentos
- **K1:** Leitura controlada por `n` para determinar a quantidade de entradas processadas.
- **K3:** Repetição baseada em contador para garantir processamento de exatamente `n` valores.
- **K2:** Rastreabilidade na apresentação dos resultados.

##### Alinhamento com a Taxonomia de Bloom (revisada)
- **Nível predominante:** **Criar** (produzir um programa/algoritmo executável que realiza o processamento solicitado).
- **Níveis de suporte:** Aplicar (uso correto de repetição e entrada/saída).

##### Pareamento Conhecimento–Habilidade
- (K1, K3) → Controlar iteração e leitura de dados conforme `n`.
- (K2) → Tornar resultados verificáveis por correspondência entrada–saída.

##### Anotação de Verbos (lista)
- implementar, processar, ler, iterar, apresentar

##### Especificação de Disposições
- Precisão na contagem e no controle de iteração.
- Atenção a consistência entre quantidade informada e quantidade processada.
- Postura de verificação por conferência de entradas/saídas.

##### Competências Alinhadas à BNCC (quando aplicável)
- Alinhamento geral a práticas de programação e pensamento computacional: controle de fluxo, organização de entrada/saída e verificabilidade.

##### Tabela-Resumo
| Código     | Competência                                             | Disposições                                  | Conhecimento          | Habilidade                                  |
|-----------|----------------------------------------------------------|----------------------------------------------|-----------------------|---------------------------------------------|
| CT26.04.1 | Processar `n` entradas e produzir saída rastreável        | precisão; consistência; verificação           | K1, K2, K3            | controlar iteração; associar entrada–saída  |

##### Definição de Ativação
- **Restrição de ativação:** obrigatória  
- **Modo de ativação:** construtiva  
- **Função de ativação:** núcleo  
- **Justificativa:** A tarefa exige a construção do fluxo principal que lê `n` e processa `n` valores. Sem essa competência, não há atendimento ao requisito central de processamento controlado e evidência observável em execução.

---

#### CT26.04.2

##### Título da Competência
Modularizar o cálculo do fatorial em função dedicada e integrá-la ao programa

##### Descrição Textual
Definir e utilizar uma **função específica** para calcular o fatorial, invocando-a para cada entrada lida e integrando-a corretamente ao fluxo principal.

##### Especificação de Conhecimentos
- **K5:** Funções com parâmetros, retorno e escopo para encapsular o cálculo.
- **K4:** Gestão de estado interno do cálculo (inicialização e atualização coerentes).
- **K7:** Consistência para casos de borda plausíveis no cálculo.

##### Alinhamento com a Taxonomia de Bloom (revisada)
- **Nível predominante:** **Criar** (definir e integrar função como parte de uma solução funcional).
- **Níveis de suporte:** Aplicar (uso correto de parâmetros/retorno e fluxo de chamada).

##### Pareamento Conhecimento–Habilidade
- (K5) → Definir assinatura e uso de função coerentes com o problema.
- (K4) → Estruturar computação interna de forma consistente.
- (K7) → Garantir comportamento consistente em entradas especiais plausíveis.

##### Anotação de Verbos (lista)
- definir, encapsular, chamar, integrar, retornar

##### Especificação de Disposições
- Organização e disciplina de modularização (separar responsabilidades).
- Rigor na coerência entre função e fluxo principal.
- Cuidado com inicializações e dependências entre execuções.

##### Competências Alinhadas à BNCC (quando aplicável)
- Alinhamento geral: uso de abstrações (funções) para estruturar soluções e favorecer clareza/verificação (sem códigos).

##### Tabela-Resumo
| Código     | Competência                                              | Disposições                                  | Conhecimento          | Habilidade                                     |
|-----------|-----------------------------------------------------------|----------------------------------------------|-----------------------|-----------------------------------------------|
| CT26.04.2 | Implementar e integrar função para cálculo de fatorial     | organização; rigor; cuidado com consistência | K4, K5, K7            | modularizar; integrar chamadas; manter coerência |

##### Definição de Ativação
- **Restrição de ativação:** obrigatória  
- **Modo de ativação:** construtiva  
- **Função de ativação:** núcleo  
- **Justificativa:** O enunciado exige explicitamente que o cálculo do fatorial seja feito por **função**. A evidência é diretamente observável no código e no comportamento ao aplicar a função a cada entrada.

---

#### CT26.04.3

##### Título da Competência
Estabelecer e documentar decisões técnicas sobre domínio e limites numéricos

##### Descrição Textual
Adotar decisões técnicas coerentes quando houver ambiguidade (p.ex., domínio das entradas e limites de representação numérica) e registrá-las de forma breve, mantendo consistência no comportamento do programa.

##### Especificação de Conhecimentos
- **K7:** Casos de borda plausíveis e consistência do domínio adotado.
- **K6:** Limites de representação numérica e implicações do crescimento rápido do resultado.
- **K2:** Rastreabilidade para permitir conferência do comportamento frente a casos distintos.

##### Alinhamento com a Taxonomia de Bloom (revisada)
- **Nível predominante:** **Analisar** (identificar ambiguidades técnicas relevantes e suas implicações).
- **Nível de suporte:** Avaliar (julgar adequação da decisão e registrá-la de modo verificável).

##### Pareamento Conhecimento–Habilidade
- (K7, K6) → Identificar pontos críticos (domínio/limites) e escolher tratamento coerente.
- (K2) → Tornar a decisão auditável por justificativa e evidências.

##### Anotação de Verbos (lista)
- identificar, decidir, justificar, documentar, manter consistência

##### Especificação de Disposições
- Transparência técnica (explicitar suposições quando necessário).
- Responsabilidade quanto a limites de execução/representação.
- Postura de consistência e não-arbitrariedade.

##### Competências Alinhadas à BNCC (quando aplicável)
- Alinhamento geral: tomada de decisão em programação e avaliação de limitações de representação/execução (sem códigos).

##### Tabela-Resumo
| Código     | Competência                                              | Disposições                                   | Conhecimento     | Habilidade                                  |
|-----------|-----------------------------------------------------------|-----------------------------------------------|------------------|---------------------------------------------|
| CT26.04.3 | Decidir e registrar domínio/limites relevantes             | transparência; responsabilidade; consistência | K2, K6, K7       | analisar ambiguidades; justificar decisões   |

##### Definição de Ativação
- **Restrição de ativação:** opcional (dependente de surgirem ambiguidades na implementação)  
- **Modo de ativação:** analítica / justificatória  
- **Função de ativação:** apoio  
- **Justificativa:** A tarefa admite ambiguidades técnicas plausíveis (domínio e limites numéricos). Quando presentes, a competência é ativada para manter robustez e rastreabilidade, sem ser o núcleo do cálculo em si.

---

#### CT26.04.4

##### Título da Competência
Verificar a solução por testes e evidências registradas

##### Descrição Textual
Planejar e executar testes mínimos de caixa-preta, registrando entradas e saídas de modo a permitir verificação do comportamento, e fornecer justificativa breve coerente com as evidências.

##### Especificação de Conhecimentos
- **K8:** Seleção e registro de testes de caixa-preta.
- **K2:** Rastreabilidade de resultados para conferência.
- **K6:** Consideração de limites de representação quando afetarem verificabilidade.

##### Alinhamento com a Taxonomia de Bloom (revisada)
- **Nível predominante:** **Avaliar** (julgar se a solução se comporta como esperado a partir de evidências).
- **Nível de suporte:** Analisar (selecionar casos representativos).

##### Pareamento Conhecimento–Habilidade
- (K8) → Construir conjunto mínimo de testes e registrar evidências.
- (K2) → Organizar a saída/registro para inspeção objetiva.
- (K6) → Reconhecer quando limites numéricos impactam resultados e evidências.

##### Anotação de Verbos (lista)
- testar, verificar, registrar, evidenciar, justificar

##### Especificação de Disposições
- Postura de verificação (não assumir correção sem evidência).
- Cuidado com rastreabilidade (manter registros auditáveis).
- Rigor ao confrontar resultados com os casos testados.

##### Competências Alinhadas à BNCC (quando aplicável)
- Alinhamento geral: validação de soluções e uso de testes como prática de programação (sem códigos).

##### Tabela-Resumo
| Código     | Competência                                   | Disposições                                   | Conhecimento     | Habilidade                                |
|-----------|-----------------------------------------------|-----------------------------------------------|------------------|-------------------------------------------|
| CT26.04.4 | Testar e evidenciar comportamento do programa  | verificação; rigor; rastreabilidade           | K2, K6, K8       | planejar testes; registrar e justificar   |

##### Definição de Ativação
- **Restrição de ativação:** obrigatória  
- **Modo de ativação:** justificatória  
- **Função de ativação:** núcleo  
- **Justificativa:** A tarefa requer **registros de teste** e uma **justificativa breve**. A competência é central para garantir verificabilidade e avaliação objetiva, indo além da mera implementação.

