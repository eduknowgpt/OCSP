# Relatório de Especificação de Competências: Tarefa 02 - Controle de Tráfego

## Introdução

Este relatório aplica o **Processo de Especificação de Competências (PEC)** ao cenário de Aprendizagem Baseada em Problemas (ABP) intitulado **"Controle de Tráfego"**, que envolve os alunos no desenvolvimento de uma solução computacional utilizando **Máquinas de Turing** para monitoramento e classificação de veículos em rodovias. A tarefa integra métodos formais e pensamento sistêmico para modelar um problema real identificado pelo Departamento de Infraestrutura de Transportes da Bahia (DERBA).

Através da metodologia PEC, as competências são extraídas e estruturadas com base na análise da descrição da tarefa, domínios de conhecimento relevantes, objetivos de aprendizagem e disposições comportamentais. O objetivo é definir um framework robusto de competências alinhado tanto com o **desenvolvimento de habilidades técnicas** quanto com a **resolução colaborativa de problemas**.

## 1. Análise da Descrição da Tarefa

A tarefa *Controle de Tráfego* desafia os alunos a desenvolver uma solução computacional formal que aborda um problema real identificado pelo **Departamento de Infraestrutura de Transportes da Bahia (DERBA)**: a deterioração de rodovias devido à pressão excessiva do tráfego noturno de veículos pesados.

Para apoiar os esforços de prevenção de desgaste do pavimento, os alunos devem projetar um sistema capaz de:

* **Processar dados de sensores** coletados nas entradas e saídas de veículos na rodovia Aratu;
* **Classificar veículos** em três categorias de peso (leve, pesado e muito pesado);
* **Contar ocorrências** para cada categoria durante a noite anterior; e
* **Identificar a categoria mais frequente**, permitindo que o DERBA priorize intervenções.

O sistema deve ser modelado usando **Máquinas de Turing**, refletindo um modelo teórico porém expressivo de computação. Os entregáveis incluem um ou mais **arquivos de Máquina de Turing baseados no JFLAP** e um **relatório técnico** em conformidade com os padrões de formatação da SBC, explicando claramente a lógica de classificação, racional de design e processo de simulação.

Esta tarefa requer que os alunos:

* **Traduzam objetivos definidos pelo usuário** em especificações formais de sistema baseadas na teoria da computabilidade;
* **Modelem restrições do mundo real** (ex: estrutura de entrada dos sensores, lógica de classificação por peso) usando Máquinas de Turing;
* **Avaliem o uso de variantes de Máquinas de Turing** (ex: multifita, não-determinísticas) quando modelos padrão forem insuficientes;
* **Simulem e testem** o modelo usando ferramentas apropriadas para garantir correção funcional;
* **Colaborem efetivamente** durante o processo de resolução de problemas, documentando todas as etapas e decisões de forma estruturada e reflexiva.

Através deste cenário de aprendizagem baseada em problemas, espera-se que os alunos integrem **conhecimento teórico de computação** com **modelagem prática e simulação**, produzindo uma solução que seja tanto academicamente rigorosa quanto socialmente relevante.

## 2. Enumeração de Conhecimentos

Para completar com sucesso a tarefa *Controle de Tráfego*, os alunos devem mobilizar um conjunto inter-relacionado de domínios de conhecimento teórico e profissional. Estes domínios estão alinhados com taxonomias reconhecidas: o **ACM Computing Classification System (2012)** para conhecimentos de computação e o **ACM/IEEE CC2020** para competências profissionais.

Esta base de conhecimento garante que o problema seja abordado não apenas de uma perspectiva técnica, mas também através de raciocínio analítico, especificação formal e comunicação efetiva.

### Conhecimentos de Computação

* **Máquinas de Turing**
  * Fundamentais para representar o processo computacional necessário para classificar veículos e calcular estatísticas de frequência. Os alunos devem entender a estrutura, comportamento e poder expressivo das Máquinas de Turing para codificar operações do mundo real em um modelo formal.

* **Variantes de Máquinas de Turing**
  * O conhecimento de Máquinas de Turing multifita ou não-determinísticas é essencial quando modelos padrão são insuficientes para desempenho ou expressividade. Variantes permitem manipulação mais eficiente de dados e simulação do sistema sob restrições complexas.

* **Tese de Church-Turing**
  * Fornece a base teórica para a tarefa, reforçando a equivalência entre raciocínio algorítmico e funções Turing-computáveis. Espera-se que os alunos fundamentem suas soluções neste conceito fundamental.

* **Engenharia de Requisitos**
  * Permite a identificação, análise e formalização das necessidades do usuário (ex: demanda do DERBA por classificação de tráfego noturno) em requisitos computacionais que guiam o design do sistema.

* **Modelagem e Simulação**
  * Envolve abstrair comportamentos do sistema em representações formais e validá-los através de ferramentas como o **JFLAP**. Esta área de conhecimento suporta refinamento iterativo e verificação da solução proposta.

### Conhecimentos Profissionais (FPK)

* **Pensamento Analítico e Crítico**
  * Necessário para desconstruir o contexto do problema (ex: monitoramento e classificação de tráfego) em componentes acionáveis, e para formular modelos lógicos que atendam às expectativas das partes interessadas.

* **Resolução de Problemas e Solução de Problemas**
  * Essencial para abordar questões de implementação, como lidar com formatos de entrada não padronizados, otimizar o uso de fitas ou depurar simulações de Máquinas de Turing.

* **Comunicação Escrita**
  * Necessária para produzir um relatório bem estruturado e tecnicamente sólido que documente o racional de design, decisões de implementação e estratégias de validação. Isso garante que os resultados sejam comunicados efetivamente para públicos técnicos e não técnicos, como o DERBA.

## 3. Identificação de Objetivos de Aprendizagem

### Objetivo Geral

Desenvolver e validar soluções computacionais formais para problemas do mundo real aplicando conhecimento de **Máquinas de Turing**, com foco em modelagem, classificação e análise de dados de tráfego baseados em entrada de sensores.

Este objetivo destaca a aplicação prática de conceitos teóricos da ciência da computação, reforçando a capacidade de projetar soluções algorítmicas fundamentadas em modelos formais.

### Objetivos Específicos

Para alcançar o objetivo geral, espera-se que os alunos:

1. **Identifiquem** requisitos e restrições do sistema com base no input das partes interessadas, particularmente as necessidades expressas pelo DERBA para análise e classificação de dados de tráfego.
2. **Traduzam e alinhem** estes requisitos com as capacidades e limitações computacionais das Máquinas de Turing, garantindo um design de sistema fiel e executável.
3. **Avaliem** a adequação das Máquinas de Turing padrão e determinem quando o uso de **variantes de máquina** (ex: multifita, não-determinísticas) é necessário para melhorar expressividade ou desempenho.
4. **Apliquem** a **Tese de Church-Turing** para justificar a viabilidade do sistema proposto, conectando modelos formais de computação com o conceito intuitivo de resolução algorítmica de problemas.
5. **Forneçam** simulações de **Máquina de Turing** em formato JFLAP que demonstrem uma solução funcional para o problema.

### Importância Destes Objetivos

Estes objetivos de aprendizagem estabelecem um **caminho estruturado e progressivo** para o desenvolvimento de competências ao integrar:

* **Compreensão teórica** de modelos formais de computação;
* **Análise contextual** de problemas do mundo real;
* **Habilidades de modelagem e simulação** para implementação e validação de sistemas;
* **Reflexão crítica** sobre adequação computacional e decisões de design.

Juntos, eles garantem que os aprendizes estejam equipados para preencher a lacuna entre **conceitos teóricos abstratos** e **resolução prática de problemas**, promovendo uma experiência de aprendizagem baseada em competências que é tanto rigorosa quanto relevante para contextos profissionais em computação.

## 4. Definições de Competências

As competências são especificadas com base nos **Objetivos de Aprendizagem (OAs)** identificados na análise da tarefa.

### Reúso de Competências

Para cumprir o objetivo de "fornecer simulações de **Máquina de Turing** em formato JFLAP que demonstrem uma solução funcional para o problema", reutilizamos a competência:

> **Testar Autômatos Usando Simuladores**

definida anteriormente na *Tarefa01 – A Máquina de Vendas de Refrigerantes e Lanches*:

Esta competência permanece totalmente relevante na tarefa atual, onde espera-se que os alunos validem seus modelos de autômatos através de ferramentas formais de simulação como o JFLAP. Os resultados de aprendizagem incluem a capacidade de executar, observar e analisar o comportamento de autômatos em um ambiente simulado, garantindo correção funcional e alinhamento com as especificações do sistema.

Além disso, como um dos entregáveis desta tarefa é um **relatório técnico** formatado de acordo com os padrões acadêmicos da **Sociedade Brasileira de Computação (SBC)**, também reutilizamos a competência definida anteriormente na *Tarefa01*:

> **Escreva, em grupo, um Relatório Técnico**

Esta competência envolve planejar, estruturar e compor um documento abrangente que comunique claramente o processo de resolução de problemas, decisões tomadas e justificativas para o modelo implementado. Ela reforça habilidades essenciais em redação técnica, colaboração em equipe e documentação.

O reúso destas competências apoia os seguintes princípios:

* **Consistência pedagógica** no desenvolvimento de competências através de diferentes tarefas de aprendizagem.
* **Reconhecimento e reforço de habilidades transversais**, como documentação e validação baseada em ferramentas.
* **Evitação de redundância** através de rastreabilidade estruturada de competências.
* **Alinhamento com educação baseada em competências**, onde um resultado de aprendizagem bem definido pode ser demonstrado em múltiplos contextos instrucionais.

Ao **reutilizar competências validadas**, garantimos que os alunos construam sobre habilidades previamente adquiridas, promovemos aprendizagem cumulativa e facilitamos práticas de avaliação baseadas em indicadores de desempenho observáveis e transferíveis.


### 4.1 Especificação da Competência A  

### A.1 Título da Competência  
    Desenvolver Soluções de Resolução de Problemas Usando Máquinas de Turing  

### A.2 Descrição Textual  
Projete e implemente uma Máquina de Turing que processe e classifique dados de veículos, transformando requisitos do usuário em um modelo funcional. Valide o modelo por meio de simulação e garanta alinhamento com restrições práticas.  

### A.3 Especificação de Conhecimento  
As seguintes áreas de conhecimento são críticas para esta competência:  

- **Máquinas de Turing (nmT):**  
    - Essencial para alcançar o objetivo geral, este conhecimento envolve compreender e aplicar os princípios das Máquinas de Turing para modelar a solução de categorização e análise de tráfego.  

- **Análise de Requisitos:**  
    - Necessária para identificar e formalizar com precisão as necessidades dos técnicos da DERBA, garantindo que os requisitos do sistema sejam bem compreendidos e corretamente implementados.  

- **Pensamento Analítico e Crítico (FPK):**  
    - Fundamental para planejar e desenvolver a solução, permitindo que os alunos analisem informações disponíveis, avaliem estratégias alternativas e proponham abordagens que equilibrem precisão e eficiência.  

### A.4 Especificação de Disposição  

A análise da tarefa **Controle de Tráfego na Rodovia Aratu** destaca as disposições comportamentais-chave necessárias para resolver o problema e entregar uma solução eficaz. As principais disposições incluem:  

**Colaborativo**  
- Trabalhar em estreita colaboração com os membros da equipe para projetar e integrar todas as partes do sistema, compartilhar insights e garantir uma solução coesa.  

**Responsável**  
- Demonstrar comprometimento com a qualidade da solução, cumprir prazos e garantir que os requisitos técnicos da DERBA sejam totalmente atendidos.  

**Proativo**  
- Antecipar possíveis desafios de implementação, propor melhorias e adaptar o modelo computacional para aumentar a precisão da classificação de veículos.  

**Inventivo**  
- Explorar diferentes variantes de Máquinas de Turing e sua aplicabilidade ao controle de tráfego, analisando as formas mais eficazes de processar dados de sensores da rodovia.  

**Criativo**  
- Desenvolver soluções inovadoras para melhorar a análise de dados de tráfego noturno, permitindo que o sistema se torne mais eficiente e responsivo às necessidades de gestão de infraestrutura.  

### A.5 Pareamento Conhecimento-Habilidade  

Esta etapa mapeia **áreas de conhecimento para as habilidades correspondentes** necessárias para demonstrar com sucesso a competência nesta tarefa.  

**A.5.1 Mapeamento de Conhecimento para Habilidades**  

Para alcançar esta competência, os alunos devem demonstrar a capacidade de:  

- **Aplicar** *Pensamento Analítico e Crítico* juntamente com o conhecimento de *Máquinas de Turing* para desenvolver uma solução computacional que processe e classifique dados de tráfego. Isso inclui modelar o comportamento dos sensores e a categorização de veículos dentro da estrutura formal de uma Máquina de Turing.  

- **Usar** *Máquinas de Turing* para representar e simular a lógica de contagem e categorização de veículos, garantindo que o modelo processe corretamente os dados e entregue uma solução eficiente para o problema.  

- **Aplicar** *Análise de Requisitos* para identificar e especificar corretamente os requisitos essenciais do sistema. Os alunos devem elicitar as necessidades da DERBA, interpretar dados de sensores e definir critérios para análise de tráfego, garantindo que os requisitos do usuário sejam traduzidos em funcionalidades práticas na solução desenvolvida.  

**A.5.2 Alinhamento com a Taxonomia de Bloom**  

Para garantir uma abordagem de aprendizagem estruturada e progressiva, cada componente de conhecimento é alinhado com a Taxonomia Revisada de Bloom, fornecendo um quadro claro para avaliação da competência.  

- **Máquinas de Turing - Aplicar**  
- O nível *Aplicar* é usado para avaliar a capacidade dos alunos de empregar o conceito de Máquinas de Turing na modelagem e resolução do problema de controle de tráfego.  

- **Análise de Requisitos - Aplicar**  
- O nível *Aplicar* é usado para avaliar se os alunos conseguem interpretar e estruturar requisitos do sistema com base nas necessidades do problema.  

- **Pensamento Analítico e Crítico (FPK) - Aplicar**  
- O nível *Aplicar* é selecionado para avaliar a capacidade dos alunos de decompor o problema em componentes gerenciáveis e desenvolver estratégias eficazes para resolvê-lo.  

**A.5.3 Anotação de Verbos**  
Para fornecer clareza sobre as expectativas da competência, as seguintes anotações de verbos definem as ações necessárias:  

#### **Máquinas de Turing – Aplicar**  

* **Usar** um modelo de Máquina de Turing para representar o comportamento do sistema.  
* **Implementar** configurações e transições em um ambiente de simulação.  
* **Executar** processos definidos pela máquina para resolver problemas estruturados.  

 **Verbos**: *Usar*, *Implementar*, *Executar*  

#### **Análise de Requisitos – Aplicar**  

* **Interpretar** as necessidades funcionais e não-funcionais descritas no problema.  
* **Organizar** essas necessidades em especificações formais.  
* **Aplicar** princípios de modelagem de requisitos para orientar o projeto do sistema.  

 **Verbos**: *Interpretar*, *Organizar*, *Aplicar*  

#### **Pensamento Analítico e Crítico (FPK) – Aplicar**  

* **Decompor** o sistema em componentes lógicos gerenciáveis.  
* **Identificar** variáveis-chave e interações.  
* **Aplicar** raciocínio estruturado para mapear características do problema em modelos formais.  

 **Verbos**: *Decompor*, *Identificar*, *Aplicar*  

### A.6 Tabela Resumo para a Competência A  

| **Competência** | **Disposições** | **Conhecimento** | **Habilidade** |  
|------------|-----------|------------|----|  
|  |   | Máquinas de Turing  | **Aplicar (Usar, Implementar, Executar)** |  
| **Desenvolver Soluções de Resolução de Problemas Usando Máquinas de Turing** | **Colaborativo, Responsável, Proativo, Criativo, Inventivo** | Análise de Requisitos | **Aplicar (Interpretar, Organizar)** |  
| | | Pensamento Analítico e Crítico (FPK) | **Aplicar (Decompor, Identificar)** |  


### 4.2 Especificação da Competência B

### B.1 Título da Competência

    Identificar Variantes de Máquinas de Turing


### B.2 Descrição Textual

Compreender e identificar diferentes **variantes de Máquinas de Turing** — como máquinas de múltiplas fitas, não-determinísticas ou outras extensões — analisando suas capacidades e limitações computacionais. Espera-se que os estudantes avaliem se o uso de Máquinas de Turing padrão é suficiente ou se modelos estendidos são necessários para atender efetivamente aos requisitos do sistema.

Esta competência reflete um entendimento conceitual da **Tese de Church-Turing** e requer que os alunos apliquem **Pensamento Analítico e Crítico (FPK)** para avaliar necessidades do sistema e propor abordagens de modelagem apropriadas com base nas características específicas das variantes de Máquinas de Turing.


### B.3 Especificação de Conhecimento

As seguintes áreas de conhecimento são críticas para esta competência:

* **Variantes de Máquinas de Turing**
  * Envolve reconhecer diferentes tipos de Máquinas de Turing (ex.: múltiplas fitas, não-determinísticas) e entender suas implicações operacionais para modelagem e resolução de problemas.

* **Tese de Church-Turing**
  * Fornece uma base teórica para avaliar o poder expressivo e a viabilidade dos modelos formais usados em problemas algorítmicos do mundo real.

* **Pensamento Analítico e Crítico (FPK)**
  * Auxilia na avaliação dos requisitos do sistema e na seleção dos modelos computacionais mais adequados para atingir os objetivos funcionais.
 
### 4.3 Especificação da Competência C

### C.1 Título da Competência

**Utilizar Variantes de Máquinas de Turing**

### C.2 Descrição Textual

Compreender e aplicar diferentes **variantes de Máquinas de Turing** - como modelos de múltiplas fitas e não-determinísticos - para desenvolver soluções otimizadas para problemas computacionais. Esta competência envolve analisar requisitos do sistema e determinar se Máquinas de Turing padrão são suficientes ou se capacidades estendidas são necessárias.

Espera-se que os estudantes demonstrem compreensão conceitual da **Tese de Church-Turing**, associando o modelo formal de computação com a noção intuitiva de algoritmo. Eles devem também aplicar raciocínio analítico para identificar o modelo computacional mais adequado para o problema em questão.

### C.3 Especificação de Conhecimento

As seguintes áreas de conhecimento são críticas para esta competência:

* **Variantes de Máquinas de Turing**
  Compreender modelos computacionais alternativos (ex.: múltiplas fitas, não-determinísticos) e suas diferenças expressivas e operacionais em comparação com Máquinas de Turing padrão.

* **Tese de Church-Turing**
  Compreender a base teórica que conecta modelos formais de computação com raciocínio algorítmico, e usar isso para justificar a viabilidade e completude de soluções propostas.

* **Pensamento Analítico e Crítico (FPK)**
  Essencial para avaliar requisitos do problema e selecionar a abordagem de modelagem mais apropriada com base em complexidade, eficiência e poder expressivo.

### C.4 Especificação de Disposição

A análise da tarefa *Controle de Tráfego na Rodovia Aratu* destaca atributos comportamentais que apoiam a avaliação crítica e adaptação de modelos computacionais para atender necessidades práticas. As principais disposições incluem:

* **Investigativo**
  Explorar modelos computacionais alternativos e avaliar sua relevância para o contexto do problema.

* **Responsável**
  Justificar decisões de modelagem com consistência teórica e prática, garantindo que soluções escolhidas atendam aos objetivos requeridos.

* **Proativo**
  Antecipar limitações potenciais em modelos padrão e propor alternativas melhoradas através de variantes.

* **Colaborativo**
  Discutir e validar escolhas de modelagem com colegas para aumentar a robustez da solução.

* **Criativo**
  Combinar conhecimento formal e insight contextual para construir modelos alternativos que sejam eficientes e inovadores.

### C.5 Pareamento Conhecimento-Habilidade

Esta etapa mapeia **áreas de conhecimento para as habilidades correspondentes** necessárias para demonstrar com sucesso esta competência.

**C.5.1 Mapeamento de Conhecimento para Habilidades**
Para demonstrar esta competência, os estudantes devem mostrar a capacidade de:

* **Aplicar** Pensamento Analítico e Crítico para examinar requisitos do sistema e determinar se Máquinas de Turing padrão ou variantes são mais apropriadas.

* **Usar** Variantes de Máquinas de Turing para modelar e otimizar soluções computacionais em cenários onde máquinas padrão são insuficientes.

* **Compreender** a Tese de Church-Turing para justificar conceitualmente o uso de modelos formais de computação na resolução de problemas do mundo real.

**C.5.2 Alinhamento com a Taxonomia de Bloom**

* Nível *Aplicar* é usado para avaliar a capacidade do estudante de analisar requisitos e escolher o modelo de Máquina de Turing apropriado.

* Nível *Compreender* é usado para avaliar o entendimento do estudante sobre a Tese de Church-Turing e sua capacidade de justificar viabilidade de soluções baseado nela.

**C.5.3 Anotação de Verbos**
Para fornecer clareza sobre expectativas da competência, as seguintes anotações de verbos definem as ações requeridas:

* **Aplicar** → Pensamento Analítico e Crítico → *Avaliar, Decidir, Selecionar*
* **Aplicar** → Máquina de Turing → *Usar, Adaptar, Implementar*
* **Compreender** → Tese de Church-Turing → *Explicar, Justificar, Interpretar*

### C.6 Tabela Resumo para Competência C

| **Competência**                          | **Disposições**                                               | **Conhecimento**                       | **Habilidade**                            |
|------------------------------------------|---------------------------------------------------------------|----------------------------------------|------------------------------------------|
| **Utilizar Variantes de Máquinas de Turing** | Inventivo, Responsável, Proativo, Colaborativo, Criativo | Máquinas de Turing                     | **Aplicar (Usar, Adaptar, Implementar)** |
|                                          |                                                                | Tese de Church-Turing                   | **Compreender (Explicar, Justificar)**   |
|                                          |                                                                | Pensamento Analítico e Crítico (FPK)    | **Aplicar (Avaliar, Decidir, Selecionar)** |

## Tabela Resumo de Todas as Competências - Tarefa: Controle de Tráfego

| **Competência**                                     | **Disposições**                                               | **Conhecimento**                       | **Habilidade**                                          |
|----------------------------------------------------|----------------------------------------------------------------|----------------------------------------|--------------------------------------------------------|
| **Desenvolver Soluções de Resolução de Problemas Usando Máquinas de Turing** | Colaborativo, Responsável, Proativo, Criativo, Inventivo | Máquinas de Turing                     | **Aplicar (Usar, Implementar, Executar)**              |
|                                                    |                                                                | Análise de Requisitos                   | **Aplicar (Interpretar, Organizar)**                   |
|                                                    |                                                                | Pensamento Analítico e Crítico (FPK)    | **Aplicar (Decompor, Identificar)**                   |
|                                                    |                                                                |                                        |                                                        |
| **Identificar Variantes de Máquinas de Turing**    | Investigativo, Colaborativo, Responsável, Proativo            | Máquinas de Turing                      | **Compreender (Diferenciar, Reconhecer, Explicar)**   |
|                                                    |                                                                | Tese de Church-Turing                   | **Compreender (Interpretar, Justificar)**             |
|                                                    |                                                                | Pensamento Analítico e Crítico (FPK)    | **Aplicar (Avaliar, Decidir, Justificar)**            |
|                                                    |                                                                |                                        |                                                        |
| **Utilizar Variantes de Máquinas de Turing**       | Inventivo, Responsável, Proativo, Colaborativo, Criativo      | Máquinas de Turing                      | **Aplicar (Usar, Adaptar, Implementar)**              |
|                                                    |                                                                | Tese de Church-Turing                   | **Compreender (Explicar, Justificar)**                |
|                                                    |                                                                | Pensamento Analítico e Crítico (FPK)    | **Aplicar (Avaliar, Decidir, Selecionar)**   


## Conclusão

A aplicação do Processo de Especificação de Competências (PEC) à Tarefa 2 demonstra como as competências podem ser sistematicamente derivadas, estruturadas e contextualizadas para preencher a lacuna entre conhecimento teórico e resolução prática de problemas na educação em computação. As competências definidas neste relatório fornecem uma base para um modelo de aprendizagem baseado em competências que promove não apenas a compreensão conceitual e a proficiência técnica, mas também o desenvolvimento de habilidades essenciais como simulação, modelagem, raciocínio analítico e elaboração colaborativa de relatórios.

Ao alinhar objetivos de aprendizagem com tarefas do mundo real, o PEC fomenta experiências de aprendizagem significativas e transferíveis, capacitando os estudantes com as competências necessárias para enfrentar desafios autênticos no campo da ciência da computação.

