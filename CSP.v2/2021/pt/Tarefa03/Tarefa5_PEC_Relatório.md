# Relatório de Especificação de Competências: Tarefa03 – O Robô Fazendeiro

## Introdução

Este relatório aplica o **Processo de Especificação de Competências (PEC)** ao cenário de Aprendizagem Baseada em Problemas (ABP) intitulado **"O Robô Fazendeiro"**, que envolve estudantes no desenvolvimento de um sistema protótipo para **identificação de rebanhos** em ambientes de pecuária extensiva. O cenário é baseado em um desafio do mundo real proposto pela empresa *Farmer Robot*, que busca uma solução de baixo custo para automatizar a classificação de animais — bovinos, caprinos e suínos — utilizando um sistema robótico equipado com um módulo de identificação visual.

Os estudantes devem modelar e simular o processo de tomada de decisão do robô utilizando **Máquinas de Estados Finitos (FSMs)** e **Expressões Regulares**, produzindo um protótipo funcional no ambiente **JFLAP**. A tarefa promove a integração de linguagens formais, modelagem computacional e raciocínio analítico em um ambiente de desenvolvimento colaborativo.

Por meio da metodologia PEC, as competências são **derivadas e estruturadas** a partir da análise da descrição da tarefa, dos domínios de conhecimento requeridos, dos objetivos de aprendizagem específicos e das disposições comportamentais. O objetivo é definir uma estrutura de competências reutilizável e sensível ao contexto, que apoie tanto o **desenvolvimento técnico** quanto a **relevância educacional**.

## 1. Análise da Descrição da Tarefa

A tarefa *Farmer Robot* desafia os estudantes a prototiparem um módulo de tomada de decisão capaz de identificar a presença e a quantidade de rebanhos específicos (bovinos, caprinos e suínos) dentro de cercas de fazendas. Essa capacidade é crucial para automatizar a logística de pedidos de ração e otimizar práticas de gestão agropecuária.

Para atender às necessidades operacionais e às restrições orçamentárias da empresa, os estudantes devem projetar uma **máquina de estados finitos** capaz de:

* **Classificar animais** em categorias distintas de rebanhos com base em entrada visual;
* **Detectar limiares mínimos de rebanho**, que acionam pedidos de entrega de ração;
* **Representar o comportamento do módulo** por meio de uma simulação no JFLAP;
* **Produzir expressões regulares** que formalizam a lógica do sistema;
* **Investigar correlações** entre limiares de rebanho e o número mínimo de estados e transições exigidos.

Além da solução técnica, os estudantes devem elaborar um **relatório técnico** no formato de artigo da SBC. Este relatório deve explicar o projeto do sistema, apresentar exemplos de uso e responder a perguntas da empresa relacionadas à **clareza da documentação** e à **estimativa de custo** com base na complexidade da máquina.

Essa tarefa exige que os aprendizes:

* **Apliquem conhecimento teórico** sobre FSMs e expressões regulares para projetar uma solução eficiente e expressiva computacionalmente;
* **Traduza os requisitos das partes interessadas** em especificações formais e representações lógicas;
* **Analise padrões e estruturas** dentro das FSMs para otimizar o projeto;
* **Simule e valide** a solução utilizando ferramentas apropriadas (JFLAP);
* **Colabore efetivamente**, documentando o processo de projeto por meio de artefatos estruturados da ABP, como diários de bordo e quadros-brancos.

Por meio deste cenário baseado em problemas, espera-se que os estudantes integrem **teoria da computação**, **modelagem formal** e **raciocínio prático** em um protótipo funcional alinhado às necessidades de uma parte interessada do mundo real.

## 2. Enumeração de Conhecimentos

Para concluir com sucesso a tarefa *Farmer Robot*, os estudantes devem recorrer a uma combinação de domínios de conhecimento teórico e profissional. Essas áreas de conhecimento estão alinhadas ao **Sistema de Classificação da Computação da ACM (2012)** para conhecimento fundamental em computação e ao framework **ACM/IEEE CC2020** para competências profissionais fundamentais (FPK).

Essa base interdisciplinar de conhecimento apoia o desenvolvimento de um sistema eficaz e otimizado de tomada de decisão para classificação de animais e gestão de alimentação.

### Conhecimento em Computação

* **Máquinas de Estados Finitos (Autômatos Finitos)**  
  Fundamentais para modelar a lógica de classificação do robô. As FSMs permitem aos estudantes projetar e simular o processo de decisão para detecção de rebanhos utilizando estados e transições bem definidos.

* **Expressões Regulares (Linguagens Regulares)**  
  Utilizadas para representar o comportamento da FSM e validar se os padrões de entrada do robô correspondem aos formatos esperados de classificação animal.

* **Engenharia de Requisitos**  
  Permite a interpretação e tradução das demandas funcionais da empresa (ex.: baixo custo, limiares mínimos, interpretabilidade) em especificações de sistema e restrições de modelagem.

* **Modelagem e Simulação**  
  Apoia a criação, execução e refinamento das FSMs em ferramentas como o **JFLAP**, permitindo que os estudantes testem o comportamento do sistema e validem os resultados em cenários esperados.

### Conhecimento Profissional (FPK)

* **Raciocínio Analítico e Crítico**  
  Essencial para decompor o problema em partes solucionáveis, identificar oportunidades de otimização (ex.: minimização de estados) e interpretar o comportamento do sistema por meio do raciocínio lógico.

* **Resolução de Problemas e Solução de Falhas**  
  Necessário para resolver desafios de projeto e implementação, como padrões ambíguos, explosão de estados ou inconsistências nas expressões regulares.

* **Comunicação Escrita**  
  Necessária para entregar um relatório técnico claro e bem estruturado, justificando as escolhas de projeto e comunicando soluções para partes interessadas com diferentes níveis de conhecimento técnico.

## 3. Identificação de Objetivos de Aprendizagem

### Objetivo Geral

Aplicar métodos formais — especificamente **Máquinas de Estados Finitos** e **Expressões Regulares** — para projetar e simular um sistema de tomada de decisão para classificação de rebanhos em um contexto agrícola robótico.

### Objetivos de Aprendizagem Específicos

1. **Modelar** o comportamento de um sistema de classificação de rebanhos utilizando Máquinas de Estados Finitos.
2. **Gerar** Expressões Regulares que representem ou validem padrões aceitos pela FSM.
3. **Identificar** o número mínimo de estados e transições necessários para um comportamento eficiente do sistema.
4. **Analisar** correlações entre a complexidade da FSM e restrições do mundo real, como limiares de classificação e custo.
5. **Traduzir** requisitos funcionais em especificações formais utilizando técnicas de Engenharia de Requisitos.
6. **Testar e simular** FSMs utilizando ferramentas como o JFLAP para validar correção e efetividade.
7. **Documentar** o comportamento do sistema, a lógica e as decisões de implementação utilizando escrita técnica estruturada.

### Importância Desses Objetivos

Esses objetivos servem como um **caminho estruturado para o desenvolvimento de competências**, permitindo que os estudantes:

* Conectem **modelos formais abstratos** com **aplicações concretas do mundo real**;
* Reforcem habilidades de **especificação formal**, **reconhecimento de padrões** e **raciocínio computacional**;
* Desenvolvam autonomia na **avaliação de trade-offs** entre expressividade, complexidade e desempenho;
* Aprimorem práticas **colaborativas e reflexivas**, como articular justificativas e compartilhar decisões de modelagem;
* Reforcem competências essenciais alinhadas com **práticas profissionais de computação**, especialmente no contexto de sistemas embarcados e automação.

## 4. Definições de Competências

As competências são especificadas com base nos **Objetivos de Aprendizagem (OAs)** identificados na análise da tarefa.

### Reutilização de Competências

Para atender ao Objetivo 6, "Testar e simular MFEs usando ferramentas como o JFLAP para validar correção e eficácia", reutilizamos a competência previamente definida na Tarefa 01 – A Máquina de Refrigerantes e Lanches:

> Testar Autômatos Usando Simuladores

Essa competência continua totalmente relevante na tarefa atual, onde se espera que os estudantes validem seus modelos de autômatos por meio de ferramentas de simulação formal como o JFLAP. Os resultados de aprendizagem incluem a capacidade de executar, observar e analisar o comportamento dos autômatos em um ambiente simulado, garantindo a correção funcional e o alinhamento com as especificações do sistema.

Além disso, como um dos entregáveis desta tarefa é um **relatório técnico** formatado segundo os padrões acadêmicos da **Sociedade Brasileira de Computação (SBC)**, também **reutilizamos a competência previamente definida na Tarefa 01**:

> Escrita Colaborativa de Relatório Técnico

Essa competência envolve o planejamento, estruturação e redação de um documento abrangente que comunique claramente o processo de resolução do problema, as decisões tomadas e as justificativas para o modelo implementado. Reforça habilidades essenciais em redação técnica, colaboração em equipe e documentação.

A reutilização dessas competências apoia os seguintes princípios:

* **Consistência pedagógica** no desenvolvimento de competências ao longo de diferentes tarefas de aprendizagem.
* **Reconhecimento e reforço de habilidades transversais**, como documentação e validação baseada em ferramentas.
* **Evitar redundâncias** por meio da rastreabilidade estruturada de competências.
* **Alinhamento com a educação baseada em competências**, onde um resultado de aprendizagem bem definido pode ser demonstrado em múltiplos contextos instrucionais.

Ao **reutilizar competências validadas**, garantimos que os estudantes construam sobre habilidades previamente adquiridas, promovendo a aprendizagem cumulativa e facilitando práticas de avaliação com base em indicadores de desempenho observáveis e transferíveis.

### 4.1 Especificação da Competência A

### A.1 Título da Competência

Desenvolver Soluções de Resolução de Problemas Usando Máquinas de Estados Finitos

### A.2 Descrição Textual

Projetar e implementar soluções computacionais usando **Máquinas de Estados Finitos (MFEs)** para abordar problemas do mundo real ou instrucionais que envolvem modelagem de sistemas por meio de estados e transições. Esta competência reflete a capacidade do estudante de aplicar o conhecimento teórico de autômatos na construção de modelos confiáveis e verificáveis que atendam aos requisitos definidos do sistema.

Espera-se que os estudantes demonstrem não apenas domínio das MFEs, mas também a capacidade de analisar os requisitos do sistema e aplicar raciocínio lógico para modelar comportamentos, assegurando que a solução seja teoricamente sólida e praticamente relevante.

### A.3 Especificação de Conhecimentos

As seguintes áreas de conhecimento são fundamentais para esta competência:

* **Autômatos Finitos (Máquinas de Estados Finitos)**
  Compreender e aplicar a estrutura, o comportamento e as aplicações de autômatos determinísticos e não determinísticos para modelar sistemas sequenciais.

* **Análise de Requisitos**
  Identificar, interpretar e traduzir os requisitos do sistema em especificações formais para o projeto da MFE.

* **Raciocínio Analítico e Crítico (FPK)**
  Decompor o problema, avaliar restrições e objetivos e selecionar estratégias adequadas de modelagem para orientar o processo de projeto.

### A.4 Especificação de Disposições

Dada a natureza colaborativa da tarefa e a necessidade de desenvolvimento criativo de modelos, as seguintes disposições comportamentais são essenciais:

* **Inventivo**
  Propor estratégias de modelagem inovadoras e explorar diferentes maneiras de estruturar MFEs para refletir o comportamento do sistema.

* **Colaborativo**
  Cooperar com os colegas na discussão dos requisitos, no projeto da máquina e na validação de seu comportamento.

* **Responsável**
  Assumir a responsabilidade pela qualidade da solução, garantindo consistência com as expectativas e prazos da tarefa.

* **Proativo**
  Antecipar desafios de implementação e adaptar o projeto para melhorar a precisão e a funcionalidade.

* **Criativo**
  Transformar requisitos do sistema em modelos intuitivos e inovadores, tornando comportamentos abstratos operacionais por meio de estados e transições.

### A.5 Associação Conhecimento-Habilidade

Este passo mapeia as **áreas de conhecimento com as habilidades correspondentes** necessárias para demonstrar com sucesso a competência nesta tarefa.

**A.5.1 Mapeamento de Conhecimento para Habilidades**

Para demonstrar esta competência, os estudantes devem demonstrar a habilidade de:

* **Aplicar** o conhecimento de **Autômatos Finitos** para projetar modelos que reflitam comportamentos reais por meio de transições de estado estruturadas.

* **Aplicar** a **Análise de Requisitos** para entender as expectativas do usuário e traduzi-las em especificações formais claras que orientem o projeto da MFE.

* **Aplicar** o **Raciocínio Analítico e Crítico (FPK)** para interpretar o problema, analisar possíveis caminhos de projeto e justificar as decisões de modelagem com base na lógica e na viabilidade.

**A.5.2 Alinhamento com a Taxonomia de Bloom**

* *Aplicar* é utilizado para todas as três áreas de conhecimento para avaliar a capacidade dos estudantes de transferir o conhecimento teórico para a prática.

**A.5.3 Anotação de Verbos**

Para proporcionar clareza nas expectativas da competência, as seguintes anotações de verbos definem as ações exigidas:

* **Aplicar** → Máquinas de Estados Finitos → *Usar, Implementar, Criar*
* **Aplicar** → Análise de Requisitos → *Interpretar, Especificar, Traduzir*

### A.6 Tabela Resumo da Competência A

| **Competência**                                                     | **Disposições**                                             | **Conhecimento**                         | **Habilidade**                              |
| ------------------------------------------------------------------- | ----------------------------------------------------------- | ---------------------------------------- | ------------------------------------------- |
| **Desenvolver Soluções de Resolução de Problemas Usando MFEs**      | Inventivo, Colaborativo, Responsável, Proativo, Criativo    | Autômatos Finitos                        | **Aplicar (Usar, Implementar, Criar)**       |
|                                                                     |                                                             | Análise de Requisitos                    | **Aplicar (Interpretar, Especificar, Traduzir)** |
|                                                                     |                                                             | Raciocínio Analítico e Crítico (FPK)    | **Aplicar**                                 |

### 4.3 Especificação da Competência B

### B.1 Título da Competência

Determinar Expressões Regulares que Representam Autômatos

### B.2 Descrição Textual

Esta competência foca na compreensão da relação entre **expressões regulares** e **autômatos finitos**, permitindo aos estudantes interpretar estruturas de autômatos e expressar seu comportamento usando representações formais equivalentes. Também envolve aplicar a **análise de requisitos** para identificar necessidades do sistema e traduzi-las em componentes válidos de linguagens regulares.

Os aprendizes devem demonstrar compreensão teórica das **linguagens regulares** e de seu poder expressivo, bem como a capacidade de aplicar análise sistemática para refinar ou validar as expressões regulares correspondentes a autômatos fornecidos.

### B.3 Especificação de Conhecimentos

As seguintes áreas de conhecimento são essenciais para esta competência:

* **Linguagens Regulares**
  * Compreender a sintaxe, a semântica e os limites expressivos das expressões regulares e sua equivalência formal com autômatos finitos.

* **Análise de Requisitos**
  * Aplicar métodos para identificar, interpretar e traduzir requisitos do sistema ou da tarefa em especificações formais adequadas ao projeto de MFEs.

* **Raciocínio Analítico e Crítico (FPK)**
  * Aplicar o pensamento analítico para testar e refinar expressões regulares quanto à correção, minimalidade e adequação funcional.

### B.4 Especificação de Disposições

As seguintes disposições comportamentais apoiam o desenvolvimento eficaz desta competência:

* **Inventivo**
  * Explorar expressões regulares alternativas que preservem a equivalência, otimizando para clareza ou minimalidade.

* **Colaborativo**
  * Analisar e validar cooperativamente a correspondência entre autômatos e expressões regulares.

* **Responsável**
  * Garantir que as expressões construídas estejam formalmente corretas e alinhadas com os requisitos da tarefa.

* **Proativo**
  * Tomar iniciativa em testar, iterar e aprimorar as expressões regulares produzidas.

* **Criativo**
  * Demonstrar criatividade em abordagens de modelagem que equilibrem simplicidade, precisão e expressividade.

### B.5 Associação Conhecimento-Habilidade

#### B.5.1 Mapeamento de Conhecimento para Habilidades

Para demonstrar esta competência, os estudantes devem:

* **Compreender** o conhecimento de **Linguagens Regulares** para interpretar autômatos e expressar comportamentos equivalentes por meio de expressões regulares.
* **Aplicar** o conhecimento de **Análise de Requisitos** para decompor descrições de tarefas e derivar representações relevantes da linguagem regular.
* **Aplicar** o conhecimento de **Raciocínio Analítico e Crítico (FPK)** para refinar expressões regulares de forma iterativa.

#### B.5.2 Alinhamento com a Taxonomia de Bloom

* *Compreender* → Linguagens Regulares  
* *Aplicar* → Análise de Requisitos  
* *Aplicar* → Raciocínio Analítico e Crítico (FPK)

#### B.5.3 Anotação de Verbos

* **Compreender** → Linguagens Regulares → *Interpretar, Relacionar, Representar*
* **Aplicar** → Análise de Requisitos → *Decompor, Traduzir, Comparar*

### B.6 Tabela Resumo da Competência B

| **Competência**                                               | **Disposições**                                             | **Conhecimento**                          | **Habilidade**                                  |
| ------------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------- | ------------------------------------------------ |
| **Determinar Expressões Regulares que Representam Autômatos** | Inventivo, Colaborativo, Responsável, Proativo, Criativo    | Linguagens Regulares                      | **Compreender (Interpretar, Relacionar, Representar)** |
|                                                               |                                                             | Análise de Requisitos                     | **Aplicar (Decompor, Traduzir, Comparar)**         |
|                                                               |                                                             | Raciocínio Analítico e Crítico (FPK)     | **Aplicar**                                       |



### 4.3 Especificação da Competência C

### C.1 Título da Competência

Inferir e Identificar Padrões em Máquinas de Estados Finitos


### C.2 Descrição Textual

Analisar a estrutura e o comportamento de **Máquinas de Estados Finitos (FSMs)** para realizar inferências e identificar padrões emergentes que influenciam a complexidade e o desempenho do modelo. Esta competência envolve reconhecer relações entre classificações de entrada, transições de estado e a quantidade de estados necessários para uma modelagem eficaz.

Espera-se que os estudantes demonstrem a habilidade de **analisar FSMs**, detectar regularidades ou redundâncias de projeto e aplicar **Pensamento Analítico e Crítico (FPK)** para refinar e interpretar o comportamento do sistema.


### C.3 Especificação do Conhecimento

As seguintes áreas de conhecimento são críticas para esta competência:

* **Máquinas de Estados Finitos**
  * Compreender as propriedades estruturais das FSMs, incluindo estados, transições e princípios de minimização, e como esses elementos influenciam a modelagem computacional.

* **Pensamento Analítico e Crítico (FPK)**
  * Aplicar raciocínio lógico para identificar estruturas ocultas, tirar conclusões significativas e justificar decisões de projeto com base na identificação de padrões e na análise do modelo.



### C.4 Especificação de Atitudes

Dada a natureza abstrata da tarefa e as exigências cognitivas de reconhecimento de padrões e inferência, as seguintes atitudes comportamentais são essenciais:

* **Inventivo**
  * Abordar a análise de FSMs com originalidade, explorando interpretações não óbvias ou alternativas do comportamento estrutural.

* **Criativo**
  * Desenvolver métodos inovadores para visualizar, interpretar ou generalizar padrões baseados em estados.

* **Minucioso**
  * Atentar cuidadosamente aos detalhes ao identificar semelhanças, redundâncias ou ineficiências no design de estados e transições.


### **C.5 Pareamento Conhecimento-Habilidade**

Esta seção mapeia as **áreas de conhecimento** com as **habilidades** correspondentes exigidas para demonstrar com sucesso esta competência.

#### **C.5.1 Mapeamento do Conhecimento para Habilidades**

Para demonstrar esta competência, os estudantes devem:

* **Analisar** o conhecimento sobre **Autômatos Finitos** para examinar estruturas de estados, reconhecer padrões e determinar como as categorias de entrada influenciam o número de estados e transições necessários.
* **Aplicar** o conhecimento de **Pensamento Analítico e Crítico (FPK)** para realizar inferências fundamentadas, detectar regularidades comportamentais e refinar projetos de FSMs com base no raciocínio lógico e nas restrições da tarefa.



#### **C.5.2 Alinhamento com a Taxonomia de Bloom**

O nível **Analisar** da Taxonomia de Bloom é usado para avaliar a capacidade dos alunos de examinar os componentes das FSMs, explicar seu comportamento funcional e justificar melhorias estruturais ou comportamentais com base em evidências e raciocínio.



#### **C.5.3 Anotação de Verbos**

Para esclarecer as expectativas, os seguintes verbos estão alinhados às áreas de conhecimento no nível de Análise:

* **Analisar** → Autômatos Finitos → *Analisar, Avaliar, Comparar*



### C.6 Tabela Resumo da Competência C

| **Competência**                                           | **Atitudes**                  | **Conhecimento**                        | **Habilidade**                           |
| --------------------------------------------------------- | ----------------------------- | --------------------------------------- | ---------------------------------------- |
| **Inferir e Identificar Padrões em Máquinas de Estados Finitos** | Inventivo, Criativo, Minucioso | Autômatos Finitos                       | **Analisar (Avaliar, Comparar)**         |
|                                                           |                               | Pensamento Analítico e Crítico (FPK)   | **Aplicar (Inferir, Justificar, Interpretar)** |



---

### 4.4 Especificação da Competência D

### D.1 Título da Competência

Diferenciar as Classificações das Gramáticas Formais


### D.2 Descrição Textual

Compreender e diferenciar as diversas **classes de gramáticas formais** — conforme definidas pela hierarquia de Chomsky — com base em seu poder de geração e relação com autômatos. Esta competência envolve identificar características que distinguem gramáticas regulares, livres de contexto, sensíveis ao contexto e irrestritas, além de reconhecer sua aplicabilidade à resolução de problemas computacionais.

No contexto da tarefa *Fazendeiro Robótico*, essa competência reforça a base teórica necessária para selecionar e justificar o modelo computacional apropriado (por exemplo, Autômato Finito) com base nas restrições e requisitos do sistema.

Espera-se que os estudantes demonstrem **compreensão conceitual** da classificação das gramáticas e apliquem esse entendimento ao especificar comportamentos de sistemas, traduzindo requisitos em lógica executável por meio da **Engenharia de Requisitos** e do **Pensamento Analítico e Crítico (FPK).**


### D.3 Especificação do Conhecimento

As seguintes áreas de conhecimento são críticas para esta competência:

* **Linguagens Regulares**
  Compreender a organização hierárquica das gramáticas e sua relação com as classes de autômatos e reconhecimento de linguagens.

* **Engenharia de Requisitos**
  Traduzir necessidades dos usuários em especificações de sistemas que sejam compatíveis com o poder expressivo do modelo de linguagem formal selecionado.

* **Pensamento Analítico e Crítico (FPK)**
  Interpretar restrições de sistema, avaliar a aplicabilidade das gramáticas e raciocinar sobre qual classificação melhor se adequa a um determinado problema computacional.



### D.4 Especificação de Atitudes

Dada a profundidade analítica e as demandas colaborativas da tarefa, as seguintes atitudes comportamentais são essenciais:

* **Colaborativo**
  Participar ativamente de discussões em equipe para classificar gramáticas e alinhá-las com estratégias de solução.

* **Responsável**
  Garantir precisão na classificação teórica e manter o alinhamento entre as especificações do sistema e os modelos computacionais.

* **Proativo**
  Antecipar limitações nas escolhas de modelagem e explorar alternativas dentro da hierarquia de Chomsky.

* **Investigativo**
  Explorar as implicações teóricas da escolha da gramática e examinar casos extremos na equivalência entre gramáticas e autômatos.



### D.5 Pareamento Conhecimento-Habilidade

Esta etapa mapeia as **áreas de conhecimento com as habilidades** correspondentes necessárias para demonstrar a competência nesta tarefa.

#### **D.5.1 Mapeamento do Conhecimento para Habilidades**

Para demonstrar esta competência, os estudantes devem demonstrar a capacidade de:

* **Compreender** as classes de **Linguagens Regulares** e relacioná-las com os autômatos correspondentes e propriedades computacionais.

* **Aplicar** a **Engenharia de Requisitos** para garantir que os modelos formais escolhidos atendam às necessidades das partes interessadas e às restrições do sistema.

* **Aplicar** o **Pensamento Analítico e Crítico (FPK)** para raciocinar sobre a seleção de gramáticas, justificar escolhas de modelagem e interpretar implicações teóricas em contextos práticos.



#### **D.5.2 Alinhamento com a Taxonomia de Bloom**

* O nível *Compreender* é utilizado para avaliar a capacidade conceitual do aluno de classificar gramáticas e associá-las ao tipo correto de autômato.

* O nível *Aplicar* é utilizado para avaliar a capacidade do aluno de traduzir requisitos de sistema e conhecimento teórico na seleção e implementação de modelos apropriados.



#### **D.5.3 Anotação de Verbos**

Para fornecer clareza sobre as expectativas da competência, as seguintes anotações de verbos definem as ações exigidas:

* **Compreender** → Linguagens Regulares → *Diferenciar, Comparar, Classificar*
* **Aplicar** → Engenharia de Requisitos → *Alinhar*
* **Aplicar** → Pensamento Analítico e Crítico (FPK)



### D.6 Tabela Resumo da Competência D

| **Competência**                                            | **Atitudes**                                         | **Conhecimento**                            | **Habilidade**                                          |
| ---------------------------------------------------------- | ---------------------------------------------------- | ------------------------------------------- | -------------------------------------------------------- |
| **Diferenciar as Classificações das Gramáticas Formais**   | Colaborativo, Responsável, Proativo, Investigativo   | Linguagens Regulares                         | **Compreender (Diferenciar, Comparar, Classificar)**     |
|                                                            |                                                      | Engenharia de Requisitos                     | **Aplicar (Alinhar)**                                   |
|                                                            |                                                      | Pensamento Analítico e Crítico (FPK)        | **Aplicar**                                              |



---

## Tabela Resumo de Todas as Competências

| **Competência**                                                       | **Atitudes**                                            | **Conhecimento**                          | **Habilidade**                                 |
| --------------------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------ | ---------------------------------------------- |
| **Desenvolver Soluções de Problemas Usando Máquinas de Estados Finitos** | Inventivo, Colaborativo, Responsável, Proativo, Criativo | Autômatos Finitos                        | **Aplicar (Usar, Implementar, Criar)**         |
|                                                                       |                                                         | Análise de Requisitos                    | **Aplicar (Interpretar, Especificar, Traduzir)**|
|                                                                       |                                                         | Pensamento Analítico e Crítico (FPK)     | **Aplicar (Analisar, Justificar, Avaliar)**    |
| **Determinar Expressões Regulares que Representam Autômatos**         | Inventivo, Colaborativo, Responsável, Proativo, Criativo | Linguagens Regulares                     | **Compreender (Interpretar, Relacionar, Representar)** |
|                                                                       |                                                         | Análise de Requisitos                    | **Aplicar (Decompor, Traduzir, Comparar)**     |
|                                                                       |                                                         | Pensamento Analítico e Crítico (FPK)     | **Aplicar (Analisar, Testar, Refinar)**        |
| **Inferir e Identificar Padrões em Máquinas de Estados Finitos**     | Inventivo, Criativo, Minucioso                         | Autômatos Finitos                        | **Analisar (Avaliar, Comparar)**               |
|                                                                       |                                                         | Pensamento Analítico e Crítico (FPK)     | **Aplicar (Inferir, Justificar, Interpretar)** |
| **Diferenciar as Classificações das Gramáticas Formais**             | Colaborativo, Responsável, Proativo, Investigativo      | Linguagens Regulares                     | **Compreender (Diferenciar, Comparar, Classificar)** |
|                                                                       |                                                         | Engenharia de Requisitos                 | **Aplicar (Alinhar)**                          |
|                                                                       |                                                         | Pensamento Analítico e Crítico (FPK)     | **Aplicar**                                     |

