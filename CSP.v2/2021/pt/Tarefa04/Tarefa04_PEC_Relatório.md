# Relatório de Especificação de Competência: Tarefa04 – O Retorno do Robô Fazendeiro

## Introdução

Este relatório aplica o **Processo de Especificação de Competência (PEC)** ao cenário de Aprendizagem Baseada em Problemas (ABP) intitulado **"O Retorno do Robô Fazendeiro"**. A tarefa desafia os alunos a projetar um módulo de navegação que permita ao robô retornar autonomamente ao seu local inicial após emitir alertas de entrega de alimentos. O módulo deve ser implementado usando modelos computacionais e validado por meio de simulação.

Esse cenário está fundamentado em um contexto agrícola real e enfatiza a aplicação de **métodos formais**, incluindo **teoria dos autômatos** e **gramáticas livres de contexto**, para resolver problemas de navegação autônoma. A solução proposta deve ser desenvolvida no **JFLAP**, com os resultados documentados em um relatório técnico formal conforme as normas da SBC (Sociedade Brasileira de Computação).

Por meio da aplicação do PEC, este relatório identifica e estrutura as competências necessárias para a realização da tarefa, com foco na integração do conhecimento teórico, raciocínio analítico e práticas colaborativas de resolução de problemas.


## 1. Análise da Descrição da Tarefa

A tarefa *Retorno do Robô Fazendeiro* foi proposta pela empresa **Farmer Robot**, após a implementação bem-sucedida de um módulo anterior de sinalização de entrega de alimentos. O novo desafio é permitir que o robô retorne autonomamente ao ponto de partida uma vez que o alerta tenha sido emitido.

A equipe de estudantes da UFBA identificou que uma **máquina de estados finita (FSM)** isoladamente não é suficiente para resolver o problema. Ao analisar os requisitos de navegação, concluíram que um **componente auxiliar de memória** — como uma **pilha** — seria necessário para que o robô pudesse registrar seu caminho e inverter a trajetória. Isso levou à adoção de **Autômatos com Pilha (PDA)** como solução de modelagem.

A solução deve simular a navegação do robô utilizando o **JFLAP**, e documentar as regras ou notações usadas para definição do percurso e lógica de retorno. Além disso, a tarefa incentiva as equipes a considerarem a extensão do Módulo de Entrega de Alimentos original ou o desenvolvimento de uma solução paralela capaz de comunicação entre módulos.

Para resolver esta tarefa, os alunos devem:

* Analisar o problema da navegação de retorno do robô e identificar os desafios computacionais associados;
* Utilizar teoria dos autômatos e máquinas com memória (ex.: PDA) para modelar o comportamento de retorno;
* Investigar **notações formais** para expressar regras baseadas em localização;
* Implementar e testar a lógica de navegação usando JFLAP;
* Produzir um relatório estruturado detalhando a solução e refletindo sobre as decisões de modelagem.


## 2. Enumeração de Conhecimentos

A tarefa requer uma combinação de domínios de conhecimento computacional e profissional. Alguns conhecimentos foram explicitamente declarados na tarefa; outros foram inferidos com base nas atividades esperadas.

### Conhecimentos Computacionais

* **Autômatos Finitos – Autômatos com Pilha (PDA)**  
  Utilizados para modelar a navegação do robô com memória, permitindo a lógica de retorno baseada em pilha.

* **Linguagens Regulares (Gramáticas Livres de Contexto)**  
  Suportam a definição de regras formais e a geração de padrões para sequências de locais.

* **Análise de Requisitos**  
  Essencial para identificar e formalizar os requisitos funcionais e não funcionais do sistema.

* **Modelagem e Simulação**  
  Aplicados por meio de ferramentas como o JFLAP para testar a correção e viabilidade do autômato proposto.

### Conhecimentos Profissionais

* **Pensamento Analítico e Crítico**  
  Permite decompor o problema de navegação e avaliar alternativas para o caminho de retorno.

* **Resolução de Problemas e Desenvolvimento de Soluções**  
  Necessário para identificar, estruturar e validar abordagens computacionais para a tarefa de navegação.

* **Comunicação Escrita**  
  Fundamental para documentar o design do sistema e os resultados da simulação em relatório técnico formal.


## 3. Identificação dos Objetivos de Aprendizagem

### Objetivo Geral

Aplicar modelos computacionais formais — especificamente autômatos baseados em memória e gramáticas formais — para desenvolver e validar um sistema de navegação robótica capaz de retornar ao ponto de origem.

### Objetivos Específicos de Aprendizagem

1. **Compreender** os desafios de navegação e as restrições de projeto do sistema do Robô Fazendeiro.  
2. **Investigar** o uso de memória baseada em pilha em autômatos para permitir o rastreamento e retorno do caminho.  
3. **Analisar** as vantagens e desvantagens entre integrar o novo módulo ao sistema existente ou implantar uma solução paralela.  
4. **Pesquisar e definir** regras formais usando notações ou gramáticas para especificar sequências de locais.  
5. **Simular e testar** a lógica de retorno usando o JFLAP, garantindo confiabilidade e precisão.


## 4. Especificação da Competência

### Reuso de Competência

Para cumprir o **Objetivo 4 — Usar ferramentas de simulação para autômatos finitos**, **reutilizamos a competência "Testar Autômatos Computacionais Usando Simuladores"** previamente definida na *Tarefa01 – Máquina de Venda de Refrigerantes e Snacks*:

> Testar Autômatos Usando Simuladores

Esta competência permanece totalmente relevante na tarefa atual, onde se espera que os alunos validem seus modelos de autômato por meio de ferramentas formais de simulação como o JFLAP. Os resultados esperados incluem a habilidade de executar, observar e analisar o comportamento dos autômatos em ambiente simulado, garantindo a correção funcional e o alinhamento com as especificações do sistema.

Adicionalmente, como um dos entregáveis da tarefa é um **relatório técnico** formatado conforme padrões acadêmicos da **Sociedade Brasileira de Computação (SBC)**, também **reutilizamos a competência previamente definida na Tarefa01**:

> Redação Colaborativa de Relatório Técnico

Esta competência envolve planejar, estruturar e redigir um documento abrangente que comunique claramente o processo de resolução do problema, decisões tomadas e justificativas para o modelo implementado. Ela reforça habilidades essenciais em redação técnica, colaboração em equipe e documentação.

O reuso dessas competências apoia os seguintes princípios:

* **Consistência pedagógica** no desenvolvimento de competências ao longo de diferentes tarefas de aprendizagem.  
* **Reconhecimento e reforço de habilidades transversais**, como documentação e validação baseada em ferramentas.  
* **Evitar redundância** por meio de rastreabilidade estruturada das competências.  
* **Alinhamento com a educação baseada em competências**, onde um resultado de aprendizagem bem definido pode ser demonstrado em múltiplos contextos instrucionais.

Ao **reutilizar competências validadas**, garantimos que os estudantes construam sobre habilidades previamente adquiridas, promovam a aprendizagem cumulativa e facilitem práticas de avaliação baseadas em indicadores de desempenho observáveis e transferíveis.


### 4.1 Especificação da Competência A

#### A.1 Título da Competência

Desenvolver soluções para resolução de problemas usando Autômatos com Pilha

#### A.2 Descrição Textual

Projetar e implementar um Autômato com Pilha (PDA) capaz de representar uma estratégia de navegação para um sistema robótico, com foco no caminho de retorno após a entrega de alimentos. A solução deve simular como estruturas de memória permitem o retrocesso e a inferência de rotas.

### **A.3 Especificação dos Conhecimentos**

As seguintes áreas de conhecimento são essenciais para dominar esta competência:

* **Autômatos com Pilha e Autômatos Finitos**  
  *Compreender os princípios da computação baseada em estados com memória, com foco em operações de pilha, funções de transição e reconhecimento de linguagens. Aplicar esse conhecimento para simular comportamentos de navegação que exigem lembrar e reverter sequências.*

* **Análise de Requisitos**  
  *Identificar, estruturar e formalizar requisitos comportamentais derivados da análise da tarefa. Traduzir metas de navegação do mundo real em requisitos funcionais e não funcionais relevantes para o design do PDA.*

* **Pensamento Analítico e Crítico**  
  *Utilizar raciocínio sistemático e decomposição de problemas para modelar a lógica de navegação. Avaliar alternativas de design e justificar escolhas de modelagem com base nas restrições comportamentais e objetivos do sistema.*


### **A.4 Especificação das Disposições**

O engajamento efetivo nesta tarefa requer as seguintes disposições comportamentais:

* **Inventivo** – Propor abordagens novas para modelar a lógica de navegação usando PDAs.  
* **Colaborativo** – Trabalhar eficazmente em equipes para aprimorar soluções compartilhadas.  
* **Responsável** – Demonstrar responsabilidade nas decisões de modelagem e validação.  
* **Proativo** – Antecipar desafios no comportamento do modelo e ajustar conforme necessário.  
* **Criativo** – Construir soluções inovadoras que ultrapassem implementações diretas.


### **A.5 Pareamento Conhecimento–Habilidade**

#### **A.5.1 Mapeamento do Conhecimento para Habilidades**

Para demonstrar esta competência, os estudantes devem ser capazes de:

* **Aplicar** o conhecimento sobre **Autômatos com Pilha** para modelar estratégias de navegação que exigem memória e retrocesso, simulando caminhos de retorno usando lógica baseada em pilha.

* **Aplicar** o conhecimento de **Análise de Requisitos** para extrair, estruturar e priorizar especificações comportamentais alinhadas aos objetivos do robô.

* **Empregar** **Pensamento Analítico e Crítico** para desconstruir requisitos complexos da tarefa, avaliar a adequação dos modelos e refinar soluções por meio de raciocínio iterativo.


#### **A.5.2 Alinhamento com a Taxonomia de Bloom**

Os principais processos cognitivos envolvidos nesta competência estão alinhados com os seguintes níveis de Bloom:

* **Aplicar** – Para usar conceitos de PDA na modelagem do sistema e no design guiado por requisitos.


#### **A.5.3 Anotação de Verbos**

Verbos representativos associados a esta competência incluem:

* *Desenvolver*, *Aplicar*, *Modelar*, *Simular*, *Interpretar*, *Construir*, *Aprimorar*, *Justificar*



#### A.6 Tabela Resumo da Competência A

| **Competência**                                            | **Disposições**                                               | **Conhecimentos**                    | **Habilidade**                  |
| --------------------------------------------------------- | ------------------------------------------------------------- | ---------------------------------- | ------------------------------ |
| Desenvolver soluções para resolução de problemas usando Autômatos com Pilha | Inventivo, Colaborativo, Responsável, Proativo, Criativo      | Autômatos com Pilha                | **Aplicar (Desenvolver, Modelar)** |
|                                                           |                                                               | Análise de Requisitos              | **Aplicar**                    |
|                                                           |                                                               | Pensamento Analítico e Crítico    | **Aplicar**                    |



## 4.2 Especificação da Competência B

### B.1 Título da Competência  
Interpretar notação baseada em regras

### B.2 Descrição Textual  
Compreender e interpretar notações formais baseadas em regras de produção, como gramáticas livres de contexto, para representar o comportamento do sistema e possibilitar o controle de navegação por meio de sequências simbólicas.

### B.3 Especificação do Conhecimento  
As seguintes áreas de conhecimento são essenciais para o domínio desta competência:

- **Gramáticas Livres de Contexto e Linguagens Regulares**  
  Compreender como essas linguagens formais definem sequências estruturadas de símbolos e como construir gramáticas para reconhecer ou gerar padrões de comportamento específicos.

- **Autômatos com Pilha e Autômatos Finitos**  
  Entender a correspondência entre linguagens baseadas em regras e autômatos capazes de reconhecê-las, particularmente o papel da memória na análise de estruturas aninhadas.

- **Pensamento Analítico e Crítico (FPK)**  
  Aplicar habilidades de raciocínio para interpretar conjuntos de regras, validar representações simbólicas de comportamento e refinar gramáticas para clareza, completude e correção.

### B.4 Especificação das Disposições  
O desenvolvimento de modelos formais baseados em regras exige as seguintes disposições comportamentais:

- Inventivo – Propor construções gramaticais criativas para capturar comportamentos complexos.  
- Colaborativo – Co-desenvolver e revisar modelos baseados em regras com colegas.  
- Responsável – Garantir a precisão e consistência nas representações simbólicas.  
- Proativo – Antecipar interações entre regras e ambiguidades no modelo.  
- Criativo – Explorar múltiplas estruturas gramaticais para representar o mesmo comportamento de forma elegante.

### B.5 Pareamento Conhecimento-Habilidade

#### B.5.1 Mapeamento do Conhecimento para Habilidades  
Para demonstrar essa competência, o aluno deve ser capaz de:

- Compreender as **Gramáticas Livres de Contexto e Linguagens Regulares** para definir representações simbólicas do comportamento do sistema por meio de regras de produção.  
- Aplicar o conhecimento sobre **Autômatos (com Pilha e Finitos)** para simular e validar a lógica de controle baseada em regras conforme as restrições da linguagem.  
- Empregar **Pensamento Analítico e Crítico** para avaliar conjuntos de regras, identificar ambiguidades ou redundâncias, e melhorar estruturas gramaticais para melhor alinhamento com os requisitos do sistema.

#### B.5.2 Alinhamento com a Taxonomia de Bloom  
Esta competência envolve os seguintes níveis cognitivos:

- **Compreender** – Reconhecer, interpretar e descrever a estrutura e o propósito dos modelos baseados em regras.  
- **Aplicar** – Construir gramáticas e usar regras simbólicas para representar e controlar o comportamento do sistema.

#### B.5.3 Anotação de Verbos  
Interpretar, Aplicar, Reconhecer, Analisar

### B.6 Tabela Resumo da Competência B  

| **Competência**                 | **Disposições**                                          | **Conhecimento**                    | **Habilidade**                  |
|--------------------------------|---------------------------------------------------------|-----------------------------------|-------------------------------|
| Interpretar notação baseada em regras | Inventivo, Colaborativo, Responsável, Proativo, Criativo | Autômatos com Pilha, Autômatos Finitos | **Compreender**                |
|                                |                                                         | Linguagens Regulares               | **Aplicar (Utilizar, Resolver)** |
|                                |                                                         | Pensamento Analítico e Crítico    | **Aplicar**                   |

---

## 4.3 Especificação da Competência C

### C.1 Título da Competência  
Diferenciar classificações de gramáticas formais

### C.2 Descrição Textual  
Compreender e distinguir os tipos de gramáticas formais (por exemplo, regulares, livres de contexto) e seus autômatos correspondentes. Usar essas distinções para modelar e avaliar o comportamento de sistemas de controle baseados em linguagens.

### C.3 Especificação do Conhecimento  
As seguintes áreas de conhecimento são essenciais para essa competência:

- **Classificação de Gramáticas Formais** (Linguagens Regulares e Livres de Contexto)  
  Compreender a hierarquia de Chomsky, incluindo tipos de gramáticas, regras de produção e os autômatos capazes de reconhecer cada classe de linguagem.

- **Pensamento Analítico e Crítico**  
  Aplicar raciocínio lógico para diferenciar classes gramaticais, analisar suas capacidades de modelagem e associá-las a comportamentos ou restrições de sistemas adequados.

### C.4 Especificação das Disposições  
Realizar efetivamente essa tarefa de classificação requer as seguintes disposições:

- Inventivo – Explorar representações alternativas para sistemas baseados em gramáticas.  
- Colaborativo – Participar de discussões com pares para refinar a compreensão das distinções gramaticais.  
- Responsável – Manter rigor conceitual e consistência ao comparar modelos formais.  
- Proativo – Buscar insights profundos sobre hierarquias linguísticas e suas implicações práticas.

### C.5 Pareamento Conhecimento-Habilidade

#### C.5.1 Mapeamento do Conhecimento para Habilidades  
Para demonstrar essa competência, o aluno deve ser capaz de:

- Compreender a **Classificação de Gramáticas Formais** para reconhecer distinções estruturais e funcionais entre os tipos de gramáticas.  
- Aplicar **Pensamento Analítico e Crítico** para comparar propriedades gramaticais, relacioná-las a tarefas de modelagem de sistemas e determinar a classe de linguagem mais adequada para um dado comportamento.

#### C.5.2 Alinhamento com a Taxonomia de Bloom  
Essa competência envolve principalmente os seguintes níveis cognitivos:

- **Compreender** – Identificar, descrever e classificar tipos de gramáticas.  
- **Aplicar** – Associar tipos de gramáticas a exemplos práticos em modelagem de comportamento.

#### C.5.3 Anotação de Verbos  
Diferenciar, Classificar, Comparar, Contrastar, Identificar, Justificar

### C.6 Tabela Resumo da Competência C  

| **Competência**                              | **Disposições**                                   | **Conhecimento**                | **Habilidade**                                   |
|---------------------------------------------|--------------------------------------------------|-------------------------------|-------------------------------------------------|
| Diferenciar classificações de gramáticas formais | Inventivo, Colaborativo, Responsável, Proativo | Linguagens Regulares           | **Compreender (Diferenciar, Comparar, Contrastar)** |
|                                             |                                                  | Pensamento Analítico e Crítico | **Aplicar**                                     |

---

## Tabela Resumo das Competências A, B e C

| **Competência**                                             | **Disposições**                                           | **Conhecimento**                | **Habilidade**                                  |
|------------------------------------------------------------|----------------------------------------------------------|-------------------------------|------------------------------------------------|
| **Desenvolver soluções para resolução de problemas usando Autômatos com Pilha** | Inventivo, Colaborativo, Responsável, Proativo, Criativo | Autômatos com Pilha            | **Aplicar (Desenvolver, Modelar)**              |
|                                                            |                                                          | Análise de Requisitos          | **Aplicar**                                     |
|                                                            |                                                          | Pensamento Analítico e Crítico | **Aplicar**                                     |
| **Interpretar notação baseada em regras**                  | Inventivo, Colaborativo, Responsável, Proativo, Criativo | Autômatos com Pilha, Autômatos Finitos | **Compreender**                                |
|                                                            |                                                          | Linguagens Regulares           | **Aplicar (Utilizar, Resolver)**                 |
|                                                            |                                                          | Pensamento Analítico e Crítico | **Aplicar**                                     |
| **Diferenciar classificações de gramáticas formais**       | Inventivo, Colaborativo, Responsável, Proativo           | Linguagens Regulares           | **Compreender (Diferenciar, Comparar, Contrastar)** |
|                                                            |                                                          | Pensamento Analítico e Crítico | **Aplicar**                                     |
