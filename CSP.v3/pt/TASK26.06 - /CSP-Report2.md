# RELATÓRIO CSP — Autoria de Competências  
## TASK26.06 — Verificação de Simetria em Matriz de Ordem 3

## Introdução
Este relatório situa-se na fase de **Autoria de Competências** do **Competency Specification Process (CSP)** e tem como finalidade explicitar, com rastreabilidade e sem redundância, os **Conhecimentos (K)**, **Objetivos de Aprendizagem (LO)** e **Competências (CT)** mobilizados pela **TASK26.06**, com foco exclusivo em Computação.

A tarefa solicita que o estudante elabore um algoritmo capaz de **verificar se uma matriz de ordem 3 é simétrica**, produzindo um resultado final inequívoco e uma justificativa breve sobre o critério adotado. A atividade elicita evidências observáveis porque exige representação de uma estrutura bidimensional, comparação entre posições relacionadas, controle do fluxo de execução e explicitação de uma decisão verificável.

A tarefa sustenta o modelo **K–S–D** porque articula: **conhecimentos** sobre matrizes, expressões lógicas, repetição, seleção e organização sequencial; **habilidades** de representar, percorrer, comparar, decidir e justificar; e **disposições** como rigor lógico, precisão e clareza técnica. O relatório utiliza exclusivamente o catálogo da disciplina como limite superior para a seleção dos conhecimentos.

---

# 1. Análise da Entidade Instrucional

## Título
**Verificação de Simetria em Matriz de Ordem 3**

## Descrição
A atividade consiste em desenvolver um algoritmo que determine se uma matriz 3x3 satisfaz a propriedade de simetria. Para isso, o estudante deve representar a matriz, acessar seus elementos por posição, comparar entradas correspondentes em relação à diagonal principal e emitir uma classificação final tecnicamente coerente.

A tarefa não exige, pelo enunciado, uma linguagem de programação específica. Assim, a análise privilegia o comportamento computacional da solução, e não detalhes sintáticos de implementação.

## Processo de Desenvolvimento da Solução (em etapas)
1. Representar a matriz como uma estrutura bidimensional de ordem 3.
2. Identificar quais posições devem ser relacionadas para verificar a propriedade solicitada.
3. Percorrer ou acessar as posições relevantes da estrutura.
4. Formular e aplicar as comparações necessárias.
5. Consolidar uma decisão final sobre a matriz.
6. Explicitar, de forma breve, o critério computacional utilizado.

## Resultados Esperados
- Algoritmo escrito na forma adotada pela disciplina.
- Representação explícita da matriz 3x3.
- Resultado final indicando se a matriz é simétrica ou não simétrica.
- Evidência verificável do comportamento da solução.
- Justificativa breve, coerente com o critério computacional empregado.

## Contexto de Aquisição
- **Código da Task:** TASK26.06
- **Nível/Curso:** programação introdutória, compatível com ensino técnico ou graduação inicial.
- **Componente Curricular:** Introdução à Programação.
- **Organização:** atividade individual.
- **Ambiente:** laboratório de programação ou avaliação prática/escrita com foco algorítmico.
- **Avaliação:** centrada na correção da verificação, na consistência do processamento e na clareza da justificativa.

## Perfil do Público-Alvo
- Estudantes iniciantes em programação.
- Com domínio prévio de variáveis, estruturas condicionais, estruturas de repetição e noções básicas de matrizes.
- Com necessidade de consolidar acesso por índices, relações posicionais em matrizes e coerência entre processamento e classificação final.

## Escala de Proficiência
A proficiência pode ser observada em três dimensões: **correção computacional**, **controle do fluxo** e **verificabilidade da solução**.

- **Nível 1 — Inicial:** representa parcialmente a matriz ou não estabelece corretamente o critério de simetria; a solução apresenta inconsistências lógicas relevantes.
- **Nível 2 — Básico:** reconhece a estrutura matricial e realiza parte do processamento necessário, mas com lacunas de cobertura, decisão ou justificativa.
- **Nível 3 — Proficiente:** representa a matriz adequadamente, realiza as comparações necessárias, produz classificação coerente e apresenta justificativa verificável.
- **Nível 4 — Avançado:** além de correta, a solução é precisa, bem estruturada, logicamente consistente e explicitamente justificável.

---

# 2. Seleção e Enumeração de Conhecimentos (Catálogo K)

## Conhecimentos selecionados

### **K01 — Modelo de execução e noção de estado (paradigma imperativo)**
- Compreensão de que a solução evolui por mudanças de estado ao longo da execução.
- Uso de variáveis e estados lógicos para sustentar o processamento.
- Relação entre execução parcial e conclusão final.
**Justificativa de mobilização na tarefa:** a verificação da simetria depende de acompanhar o estado lógico da análise à medida que os elementos da matriz são confrontados.

### **K03 — Variáveis, constantes e tipos primitivos**
- Uso de identificadores para índices, valores e estado da solução.
- Representação consistente de dados simples envolvidos no processamento.
- Apoio operacional ao acesso e à comparação de elementos.
**Justificativa de mobilização na tarefa:** o algoritmo requer variáveis para controle de índices, apoio ao percurso e registro da decisão final.

### **K05 — Expressões lógicas e condições**
- Formulação de condições booleanas a partir de relações entre elementos.
- Interpretação de igualdade e desigualdade como base para decisão.
- Composição de critérios de verificação.
**Justificativa de mobilização na tarefa:** a propriedade de simetria é decidida por relações lógicas entre posições correspondentes da matriz.

### **K06 — Estrutura sequencial e E/S básica**
- Organização do fluxo entrada/processamento/saída.
- Encadeamento operacional coerente da solução.
- Emissão de resultado verificável.
**Justificativa de mobilização na tarefa:** a atividade exige uma sequência consistente entre representação da matriz, processamento da verificação e apresentação do resultado.

### **K07 — Estruturas de seleção**
- Escolha de caminhos alternativos de execução com base em condições.
- Consolidação de uma decisão final de classificação.
- Tratamento explícito de resultados possíveis.
**Justificativa de mobilização na tarefa:** ao final da análise, a solução deve decidir se a matriz satisfaz ou não a propriedade investigada.

### **K08 — Estruturas de repetição**
- Uso de laços para percorrer dados estruturados.
- Controle de iteração por índice e condição de parada.
- Cobertura sistemática de elementos relevantes.
**Justificativa de mobilização na tarefa:** a verificação pode demandar varredura organizada da matriz para confrontar posições relacionadas.

### **K09 — Tipos de dados estruturados em C (vetores, matrizes, strings, enum, union)**
- Representação de dados em matrizes.
- Acesso por índice de linha e coluna.
- Manipulação de estrutura bidimensional como objeto central do problema.
**Justificativa de mobilização na tarefa:** a matriz é o núcleo estrutural da atividade, tanto na representação quanto no processamento.

### Nota Analítica
Foram selecionados **sete conhecimentos** do catálogo, todos diretamente relacionados à evidência principal da tarefa. O subconjunto preserva boa granularidade: é suficiente para descrever a atividade com precisão, sem dispersão excessiva. Não foram incluídos conhecimentos sobre subprogramas, recursão ou arquivos, pois não são exigidos pelo enunciado nem pela descrição pedagógica da task.

---

# 3. Identificação de Objetivos de Aprendizagem

### **LO1.**
Representar e acessar dados organizados em matrizes para fins de processamento algorítmico.  
**K associados:** (K09, K03)

### **LO2.**
Formular condições computacionais a partir de relações entre elementos de uma estrutura bidimensional.  
**K associados:** (K05, K09, K01)

### **LO3.**
Organizar o fluxo de uma solução que receba, processe e devolva uma classificação verificável sobre uma matriz.  
**K associados:** (K06, K03, K09)

### **LO4.**
Empregar estruturas de repetição para percorrer, de modo controlado, posições relevantes de uma matriz.  
**K associados:** (K08, K09, K03)

### **LO5.**
Utilizar seleção e controle de estado para consolidar uma decisão final baseada nas comparações realizadas.  
**K associados:** (K07, K05, K01)

### **LO6.**
Explicar, de forma tecnicamente coerente, o critério computacional utilizado e o resultado produzido pela solução.  
**K associados:** (K01, K05, K09)

### Nota Analítica
Os objetivos de aprendizagem foram formulados de modo **reutilizável**, evitando dependência excessiva do enunciado específico. Predominam os níveis **Aplicar** e **Analisar** da taxonomia revisada de Bloom, com apoio de **Criar** quando a tarefa é entendida como elaboração de uma solução algorítmica completa. A observabilidade decorre do artefato produzido, do comportamento verificável da solução e da justificativa breve exigida.

---

# 4. Definição de Competências

## 4.1 Competência Geral (BNCC – quando aplicável)
**Competência geral do domínio:** mobilizar fundamentos de programação para representar estruturas de dados, formular critérios de análise, controlar o fluxo de execução e produzir classificações computacionais verificáveis.

**Alinhamento geral com a BNCC:** a tarefa se relaciona, em nível amplo, com práticas de **pensamento computacional**, especialmente **abstração de estruturas**, **análise de padrões**, **formalização algorítmica** e **produção de soluções verificáveis**. Como a etapa específica não foi explicitada no contexto da task, o alinhamento é registrado sem códigos.

---

## 4.2 Especificações de Competências

### Competência CT26.06.1
**Título da Competência**  
Controlar o fluxo com estruturas de decisão, formulando expressões lógicas corretas para classificar propriedades em matrizes.

**Descrição Textual**  
Mobilizar estruturas de decisão e expressões lógicas para avaliar propriedades de dados organizados em matrizes, produzindo classificações computacionais coerentes, verificáveis e fundamentadas nas relações entre elementos da estrutura.

**Cobertura e rastreabilidade**
- **LOs cobertos:** (LO2, LO5, LO6)
- **K mobilizados (Núcleo):** (K05, K07)
- **K mobilizados (Apoio):** (K01, K09, K03)

**Especificação de Conhecimentos**
- **K05 — Expressões lógicas e condições**  
  Descrição curta: formulação de condições booleanas a partir de relações entre valores e posições.  
  Justificativa de evidência: a tarefa exige construir o critério lógico que permite decidir se a propriedade avaliada está presente na matriz.
- **K07 — Estruturas de seleção**  
  Descrição curta: uso de decisões para escolher caminhos de execução e consolidar classificações finais.  
  Justificativa de evidência: a solução precisa produzir uma decisão final inequívoca sobre a matriz analisada.
- **K01 — Modelo de execução e noção de estado (paradigma imperativo)**  
  Descrição curta: compreensão de que o resultado da solução decorre da evolução do estado do algoritmo ao longo do processamento.  
  Papel de suporte: sustenta o controle lógico da verificação e a coerência entre comparações parciais e decisão final.
- **K09 — Tipos de dados estruturados em C (vetores, matrizes, strings, enum, union)**  
  Descrição curta: organização de dados em estruturas matriciais com acesso por posição.  
  Papel de suporte: fornece o contexto estrutural no qual as condições e decisões são aplicadas.
- **K03 — Variáveis, constantes e tipos primitivos**  
  Descrição curta: uso de identificadores e valores para apoiar comparações e registrar resultados.  
  Papel de suporte: viabiliza o armazenamento do estado lógico e da classificação final.

**Alinhamento com a Taxonomia de Bloom (revisada)**  
**Aplicar** e **Analisar**

**Pareamento Conhecimento–Habilidade**
K05 / Aplicar / formular → formular expressões lógicas corretas para comparar elementos relacionados da matriz.  
K07 / Aplicar / decidir → controlar a decisão final da solução com base nas condições avaliadas.  
K01 / Analisar / verificar → verificar a coerência do estado lógico da solução ao longo da análise.  
K09 / Aplicar / relacionar → relacionar posições da matriz como base para a classificação computacional.  
K03 / Aplicar / registrar → registrar o resultado da verificação em variáveis adequadas.

**Anotação de Verbos (lista)**  
formular, comparar, decidir, classificar, verificar, controlar

**Especificação de Disposições**
- Rigor lógico
- Precisão analítica
- Clareza técnica
- Coerência

**Competências Alinhadas à BNCC (quando aplicável)**  
Alinhamento geral com formulação de regras, análise de padrões e tomada de decisão algorítmica.

**Tabela-Resumo**

| Código | Competência | Disposições | Conhecimento | Habilidade |
|---|---|---|---|---|
| CT26.06.1 | Controlar o fluxo com estruturas de decisão, formulando expressões lógicas corretas para classificar propriedades em matrizes | rigor lógico; precisão analítica; clareza técnica; coerência | K05 (Núcleo) | formular expressões lógicas corretas |
| CT26.06.1 | Controlar o fluxo com estruturas de decisão, formulando expressões lógicas corretas para classificar propriedades em matrizes | rigor lógico; precisão analítica; clareza técnica; coerência | K07 (Núcleo) | decidir e classificar |
| CT26.06.1 | Controlar o fluxo com estruturas de decisão, formulando expressões lógicas corretas para classificar propriedades em matrizes | rigor lógico; precisão analítica; clareza técnica; coerência | K01 (Apoio) | verificar a coerência do estado lógico |
| CT26.06.1 | Controlar o fluxo com estruturas de decisão, formulando expressões lógicas corretas para classificar propriedades em matrizes | rigor lógico; precisão analítica; clareza técnica; coerência | K09 (Apoio) | relacionar posições da matriz |
| CT26.06.1 | Controlar o fluxo com estruturas de decisão, formulando expressões lógicas corretas para classificar propriedades em matrizes | rigor lógico; precisão analítica; clareza técnica; coerência | K03 (Apoio) | registrar o resultado da decisão |

**Definição de Ativação**
- **Restrição de ativação:** obrigatória
- **Modo de ativação:** analítica
- **Função de ativação:** núcleo
- **Justificativa curta:** a task exige que o estudante formule corretamente o critério lógico da verificação e utilize estruturas de decisão para concluir se a matriz satisfaz ou não a propriedade solicitada.

---

### Competência CT26.06.2
**Título da Competência**  
Controlar o fluxo com repetição para percorrer matrizes por meio de índices e condições de parada coerentes.

**Descrição Textual**  
Empregar estruturas de repetição para percorrer matrizes de modo sistemático, utilizando índices e condições de parada coerentes, de forma a garantir cobertura adequada dos elementos relevantes ao processamento solicitado.

**Cobertura e rastreabilidade**
- **LOs cobertos:** (LO1, LO3, LO4)
- **K mobilizados (Núcleo):** (K08, K09)
- **K mobilizados (Apoio):** (K03, K06, K01)

**Especificação de Conhecimentos**
- **K08 — Estruturas de repetição**  
  Descrição curta: uso de laços para realizar percursos controlados e sistemáticos em estruturas de dados.  
  Justificativa de evidência: a tarefa demanda varredura organizada de posições da matriz para permitir a verificação da propriedade.
- **K09 — Tipos de dados estruturados em C (vetores, matrizes, strings, enum, union)**  
  Descrição curta: representação e acesso a matrizes por índices de linha e coluna.  
  Justificativa de evidência: a competência se manifesta no modo como o estudante percorre a estrutura bidimensional.
- **K03 — Variáveis, constantes e tipos primitivos**  
  Descrição curta: uso de variáveis de índice e apoio ao controle do percurso.  
  Papel de suporte: viabiliza a operacionalização dos laços e o acesso posicional aos elementos.
- **K06 — Estrutura sequencial e E/S básica**  
  Descrição curta: organização do fluxo operacional da solução do início ao fim.  
  Papel de suporte: apoia a integração entre representação da matriz, processamento repetitivo e saída final.
- **K01 — Modelo de execução e noção de estado (paradigma imperativo)**  
  Descrição curta: compreensão da progressão do processamento ao longo das iterações.  
  Papel de suporte: favorece o entendimento da atualização dos índices e da evolução da verificação.

**Alinhamento com a Taxonomia de Bloom (revisada)**  
**Aplicar** e **Criar**

**Pareamento Conhecimento–Habilidade**
K08 / Aplicar / percorrer → percorrer a matriz com repetição controlada e cobertura adequada dos elementos relevantes.  
K09 / Aplicar / acessar → acessar elementos da matriz por índices de linha e coluna.  
K03 / Aplicar / controlar → controlar índices e variáveis auxiliares durante o percurso da estrutura.  
K06 / Aplicar / organizar → organizar o fluxo entre representação da matriz, processamento iterativo e saída verificável.  
K01 / Analisar / acompanhar → acompanhar a progressão do processamento durante as iterações.

**Anotação de Verbos (lista)**  
percorrer, iterar, acessar, controlar, organizar, processar

**Especificação de Disposições**
- Sistematização
- Organização procedimental
- Atenção operacional
- Consistência

**Competências Alinhadas à BNCC (quando aplicável)**  
Alinhamento geral com elaboração de procedimentos computacionais, decomposição operacional e tratamento sistemático de dados estruturados.

**Tabela-Resumo**

| Código | Competência | Disposições | Conhecimento | Habilidade |
|---|---|---|---|---|
| CT26.06.2 | Controlar o fluxo com repetição para percorrer matrizes por meio de índices e condições de parada coerentes | sistematização; organização procedimental; atenção operacional; consistência | K08 (Núcleo) | percorrer com repetição controlada |
| CT26.06.2 | Controlar o fluxo com repetição para percorrer matrizes por meio de índices e condições de parada coerentes | sistematização; organização procedimental; atenção operacional; consistência | K09 (Núcleo) | acessar elementos por posição |
| CT26.06.2 | Controlar o fluxo com repetição para percorrer matrizes por meio de índices e condições de parada coerentes | sistematização; organização procedimental; atenção operacional; consistência | K03 (Apoio) | utilizar índices de controle |
| CT26.06.2 | Controlar o fluxo com repetição para percorrer matrizes por meio de índices e condições de parada coerentes | sistematização; organização procedimental; atenção operacional; consistência | K06 (Apoio) | organizar o fluxo da solução |
| CT26.06.2 | Controlar o fluxo com repetição para percorrer matrizes por meio de índices e condições de parada coerentes | sistematização; organização procedimental; atenção operacional; consistência | K01 (Apoio) | acompanhar a evolução da execução |

**Definição de Ativação**
- **Restrição de ativação:** obrigatória
- **Modo de ativação:** construtiva
- **Função de ativação:** núcleo
- **Justificativa curta:** a verificação da propriedade na matriz depende de um percurso computacional controlado, no qual índices e iterações precisam ser usados com coerência para acessar os elementos relevantes.

---

### Competência CT26.06.3
**Título da Competência**  
Representar e processar coleções homogêneas em matrizes, acessando e relacionando elementos por posição.

**Descrição Textual**  
Representar dados homogêneos em matrizes e processá-los por meio de acesso posicional, estabelecendo relações entre elementos da estrutura para apoiar análises, verificações e classificações computacionais.

**Cobertura e rastreabilidade**
- **LOs cobertos:** (LO1, LO2, LO3, LO6)
- **K mobilizados (Núcleo):** (K09, K06)
- **K mobilizados (Apoio):** (K05, K03, K08)

**Especificação de Conhecimentos**
- **K09 — Tipos de dados estruturados em C (vetores, matrizes, strings, enum, union)**  
  Descrição curta: organização de dados em matrizes e acesso indexado a seus elementos.  
  Justificativa de evidência: a tarefa é centrada na representação e análise de uma matriz de ordem 3.
- **K06 — Estrutura sequencial e E/S básica**  
  Descrição curta: encadeamento do processamento computacional desde a entrada até a saída.  
  Justificativa de evidência: o estudante precisa estruturar a solução de forma que a matriz seja tratada e o resultado final seja apresentado de modo verificável.
- **K05 — Expressões lógicas e condições**  
  Descrição curta: relações lógicas entre elementos para sustentar verificações.  
  Papel de suporte: permite transformar relações posicionais da matriz em critério computacional de análise.
- **K03 — Variáveis, constantes e tipos primitivos**  
  Descrição curta: uso de identificadores para armazenar índices, valores e estado da solução.  
  Papel de suporte: apoia o acesso aos elementos e a materialização operacional da solução.
- **K08 — Estruturas de repetição**  
  Descrição curta: percursos sistemáticos sobre conjuntos estruturados de dados.  
  Papel de suporte: favorece o processamento ordenado da matriz quando a solução utiliza varredura iterativa.

**Alinhamento com a Taxonomia de Bloom (revisada)**  
**Aplicar** e **Analisar**

**Pareamento Conhecimento–Habilidade**
K09 / Aplicar / representar → representar e acessar coleções homogêneas em matrizes por posição.  
K06 / Aplicar / organizar → organizar o processamento computacional da matriz até a produção do resultado final.  
K05 / Analisar / relacionar → relacionar elementos da matriz segundo um critério lógico de verificação.  
K03 / Aplicar / manipular → manipular índices, valores e variáveis de apoio ao processamento.  
K08 / Aplicar / iterar → iterar sobre a estrutura quando o processamento exigir varredura sistemática.

**Anotação de Verbos (lista)**  
representar, acessar, relacionar, processar, organizar, verificar

**Especificação de Disposições**
- Precisão estrutural
- Atenção aos detalhes
- Clareza organizacional
- Rigor técnico

**Competências Alinhadas à BNCC (quando aplicável)**  
Alinhamento geral com representação de dados, abstração de estruturas e processamento organizado de informações em artefatos computacionais.

**Tabela-Resumo**

| Código | Competência | Disposições | Conhecimento | Habilidade |
|---|---|---|---|---|
| CT26.06.3 | Representar e processar coleções homogêneas em matrizes, acessando e relacionando elementos por posição | precisão estrutural; atenção aos detalhes; clareza organizacional; rigor técnico | K09 (Núcleo) | representar e acessar matrizes |
| CT26.06.3 | Representar e processar coleções homogêneas em matrizes, acessando e relacionando elementos por posição | precisão estrutural; atenção aos detalhes; clareza organizacional; rigor técnico | K06 (Núcleo) | organizar o processamento da solução |
| CT26.06.3 | Representar e processar coleções homogêneas em matrizes, acessando e relacionando elementos por posição | precisão estrutural; atenção aos detalhes; clareza organizacional; rigor técnico | K05 (Apoio) | relacionar elementos segundo critério lógico |
| CT26.06.3 | Representar e processar coleções homogêneas em matrizes, acessando e relacionando elementos por posição | precisão estrutural; atenção aos detalhes; clareza organizacional; rigor técnico | K03 (Apoio) | manipular índices, valores e variáveis de apoio |
| CT26.06.3 | Representar e processar coleções homogêneas em matrizes, acessando e relacionando elementos por posição | precisão estrutural; atenção aos detalhes; clareza organizacional; rigor técnico | K08 (Apoio) | percorrer a estrutura quando necessário |

**Definição de Ativação**
- **Restrição de ativação:** obrigatória
- **Modo de ativação:** construtiva
- **Função de ativação:** núcleo
- **Justificativa curta:** a atividade se apoia diretamente na capacidade de representar a matriz, acessar seus elementos por posição e estabelecer relações entre eles para produzir uma verificação computacional consistente.

---

# Fora do Escopo/Extensão (EXT)
- **Teste e depuração formais da solução:** a descrição pedagógica recomenda testar a solução com casos simétricos e não simétricos, mas o catálogo da disciplina explicita que teste e depuração não integram, por padrão, os conhecimentos K desta disciplina. Assim, esse aspecto permanece como extensão metodológica de avaliação, sem geração de K, LO ou CT específicos.

