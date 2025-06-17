# Relatório de Resultados da Revisão e Ajustes na Especificação de Competências: Tarefa 04 – O Retorno do Robô Agricultor

## Introdução

O processo de revisão, fundamentado no feedback dos especialistas **P1 e P2**, identificou **áreas-chave para melhoria** na estrutura de especificação de competências. Essas percepções foram categorizadas em **cinco temas principais**:  
- **Granularidade do Conhecimento** → Garantir um nível adequado de detalhamento.  
- **Adequação do Conhecimento** → Alinhar competências com conhecimentos relevantes e aplicáveis.  
- **Vocabulário Controlado** → Padronizar a terminologia para aumentar a consistência.  
- **Verbos da Taxonomia de Bloom** → Melhorar a clareza nas descrições das habilidades.  
- **Clareza Textual** → Refinar as descrições para evitar ambiguidades.  

Com base nessas recomendações, **vários aprimoramentos foram implementados** para melhorar a especificidade, clareza e reutilização das competências.

## Especificação Revisada da Competência para a Tarefa 04

### Reutilização de Competências

> Testar Autômatos Usando Simuladores

> Escrever um Relatório Técnico

### Especificação da Competência A

#### A.1 Título da Competência

Desenvolver soluções para resolução de problemas usando Autômatos com Pilha

#### A.2 Descrição Textual

Esta competência envolve a habilidade de projetar e implementar modelos computacionais usando Autômatos com Pilha (Pushdown Automata – PDA) para representar comportamentos que requerem decisões baseadas em memória. Espera-se que os alunos modelem e simulem sistemas nos quais a memória baseada em pilha seja essencial para tarefas como retrocesso, reconhecimento de estruturas aninhadas ou navegação sequencial.

A aplicação dos PDAs pode abranger domínios como controle robótico, análise sintática de linguagens ou computação simbólica, e requer compreensão de como transições, entradas e operações na pilha interagem para produzir respostas sensíveis ao contexto. Os estudantes devem demonstrar capacidade de aplicar conceitos formais para construir modelos que sejam tanto teoricamente sólidos quanto eficazes na prática para resolver problemas envolvendo processos estruturados ou hierárquicos.

#### A.2 Tabela para a Competência A

| **Competência**                                             | **Disposições**                                                | **Conhecimento**                 | **Habilidade**                   |
| ----------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------- | ------------------------------- |
| Desenvolver soluções para resolução de problemas usando Autômatos com Pilha | Inventivo, Colaborativo, Responsável, Proativo, Criativo      | Autômatos com Pilha             | **Aplicar (Desenvolver, Modelar)** |
|                                                             |                                                               | Engenharia de Requisitos        | **Aplicar**                     |
|                                                             |                                                               | Pensamento Analítico e Crítico | **Aplicar**                     |

### Especificação da Competência B

#### B.1 Título da Competência

Interpretar notação baseada em regras

#### B.2 Descrição Textual

Esta competência envolve a habilidade de compreender e interpretar notações formais baseadas em regras, tais como gramáticas livres de contexto, usadas para definir e controlar o comportamento de sistemas por meio de sequências estruturadas de símbolos. Espera-se que os alunos analisem como regras de produção regem sequências válidas de operações, permitindo a representação de lógica decisória, fluxos procedurais ou protocolos de comunicação.

Esta competência é aplicável a domínios que exigem modelagem simbólica, como processamento de linguagens, controle robótico e especificação formal. Enfatiza a compreensão da sintaxe e hierarquias de regras, bem como a capacidade de interpretar como tais notações definem restrições e orientam a execução em sistemas computacionais.

#### B.3 Especificação do Conhecimento

As seguintes áreas de conhecimento são essenciais para o domínio desta competência:

* Gramáticas Livres de Contexto e Linguagens Regulares (Linguagens Livres de Contexto)
  * Compreender como essas linguagens formais definem sequências estruturadas de símbolos e como construir gramáticas para reconhecer ou gerar padrões específicos de comportamento.

* Autômatos com Pilha
  * Compreender a correspondência entre linguagens baseadas em regras e autômatos capazes de reconhecê-las, particularmente o papel da memória na análise de estruturas aninhadas.

* Pensamento Analítico e Crítico
  * Aplicar habilidades de raciocínio para interpretar conjuntos de regras, validar representações simbólicas de comportamento e refinar gramáticas visando clareza, completude e correção.

#### B.5 Associação Conhecimento-Habilidade

**B.5.1 Mapeamento do Conhecimento para Habilidades**  
Para demonstrar essa competência, os estudantes devem ser capazes de:

* **Compreender** o conhecimento sobre Gramáticas Livres de Contexto e Linguagens Regulares para interpretar e construir representações baseadas em regras que definem sequências válidas de símbolos que governam o comportamento do sistema.  
  * Verbos: Interpretar, Construir, Relacionar

* **Compreender** o conhecimento sobre Autômatos com Pilha para reconhecer os mecanismos computacionais capazes de processar estruturas baseadas em regras — particularmente aquelas envolvendo hierarquia, recursão ou padrões aninhados — e relacionar esses modelos ao poder expressivo das gramáticas.  
  * Verbos: Reconhecer, Explicar, Comparar

* **Aplicar** Pensamento Analítico e Crítico para examinar conjuntos de regras, detectar inconsistências ou ambiguidades e refinar estruturas gramaticais para melhorar correção, clareza e aplicabilidade no domínio do sistema.  
  * Verbos: Analisar, Refinar, Validar

#### B.6 Tabela para a Competência B

| **Competência**                   | **Disposições**                                                | **Conhecimento**                 | **Habilidade**                                  |
| -------------------------------- | ------------------------------------------------------------- | ------------------------------- | ---------------------------------------------- |
| Interpretar notação baseada em regras | Inventivo, Colaborativo, Responsável, Proativo, Criativo      | Autômatos com Pilha             | **Compreender (Reconhecer, Explicar, Comparar)** |
|                                  |                                                               | Gramáticas Livres de Contexto   | **Compreender (Interpretar, Construir, Relacionar)** |
|                                  |                                                               | Linguagens Regulares            | **Compreender (Interpretar, Construir, Relacionar)** |
|                                  |                                                               | Pensamento Analítico e Crítico  | **Aplicar (Refinar, Validar)**                   |

### Especificação da Competência C

#### C.1 Título da Competência

Diferenciar classificações de gramáticas formais

#### C.2 Descrição Textual

Esta competência foca na habilidade de compreender e diferenciar classes de gramáticas formais, como gramáticas regulares e livres de contexto, juntamente com seus respectivos modelos computacionais (por exemplo, autômatos finitos e autômatos com pilha). Espera-se que os alunos analisem as características estruturais e o poder expressivo de cada tipo de gramática e avaliem sua adequação para modelar diferentes tipos de sistemas de controle simbólico ou comportamentos baseados em linguagem.

A competência apoia o entendimento crítico da hierarquia de Chomsky, permitindo aos estudantes classificar problemas segundo sua complexidade gramatical e tomar decisões informadas ao selecionar representações formais para projeto ou análise de sistemas.

#### C.3 Especificação do Conhecimento

As seguintes áreas de conhecimento são essenciais para o domínio desta competência:

* Linguagens Livres de Contexto  
  * Compreender os princípios das gramáticas livres de contexto, incluindo sua estrutura, regras de derivação e capacidade de descrever padrões hierárquicos. Reconhecer seus limites expressivos e os tipos de autômatos (por exemplo, autômatos com pilha) usados para reconhecê-las.

* Linguagens Regulares  
  * Compreender a definição e construção de gramáticas regulares e o uso correspondente de autômatos finitos para representar padrões planos ou repetitivos. Identificar as limitações das linguagens regulares em comparação com as livres de contexto.

* Pensamento Analítico e Crítico  
  * Aplicar raciocínio lógico para comparar classes gramaticais com base em estrutura, expressividade e requisitos computacionais. Avaliar qual tipo de gramática é mais apropriado para modelar comportamentos específicos e justificar a classificação com base em critérios formais.

#### C.4 Associação Conhecimento-Habilidade

##### C.4.1 Mapeamento do Conhecimento para Habilidades

Para demonstrar efetivamente esta competência, os estudantes devem ser capazes de:

* **Compreender** o conhecimento sobre Linguagens Livres de Contexto  
  * Verbos associados: Reconhecer, Descrever, Diferenciar  
  * Os alunos devem ser capazes de reconhecer características estruturais das gramáticas livres de contexto, descrever seus padrões de derivação e diferenciar seu poder expressivo do das linguagens regulares.

* **Compreender** o conhecimento sobre Linguagens Regulares  
  * Verbos associados: Identificar, Classificar, Comparar  
  * Os alunos devem identificar características das gramáticas regulares e dos autômatos finitos, classificar construtos linguísticos conforme a complexidade gramatical e comparar linguagens regulares e livres de contexto em termos de expressividade e potencial de modelagem.

* **Aplicar** Pensamento Analítico e Crítico  
  * Os alunos devem analisar a adequação dos diferentes tipos de gramáticas para cenários específicos de modelagem, contrastar suas propriedades estruturais e computacionais e justificar a escolha de uma classe gramatical com base nos requisitos do sistema.

#### C.5.2 Alinhamento com a Taxonomia de Bloom

Esta competência envolve os seguintes níveis de processamento cognitivo:

* **Compreender** – Para identificar, descrever e classificar tipos de gramáticas e suas características estruturais.

* **Aplicar** – Para analisar necessidades de modelagem e selecionar classes gramaticais apropriadas com base em critérios formais e restrições do sistema.

#### C.6 Tabela Resumo para a Competência C

| **Competência**                            | **Disposições**                              | **Conhecimento**             | **Habilidade**                               |
| ----------------------------------------- | ------------------------------------------- | ---------------------------- | -------------------------------------------- |
| Diferenciar classificações de gramáticas formais | Inventivo, Colaborativo, Responsável, Proativo | Linguagens Regulares          | **Compreender (Identificar, Classificar, Comparar)** |
|                                           |                                             | Linguagens Livres de Contexto | **Compreender (Reconhecer, Descrever, Diferenciar)** |
|                                           |                                             | Pensamento Analítico e Crítico | **Aplicar**                                  |

### **Tabela Resumo Unificada das Competências A, B e C**

| **Competência**                                            | **Disposições**                                           | **Conhecimentos**               | **Habilidade**                                         |
| --------------------------------------------------------- | -------------------------------------------------------- | ------------------------------ | ----------------------------------------------------- |
| Desenvolver soluções para resolução de problemas usando Autômatos com Pilha | Inventivo, Colaborativo, Responsável, Proativo, Criativo | Autômatos com Pilha            | **Aplicar** (*Desenvolver, Modelar*)                   |
|                                                           |                                                          | Engenharia de Requisitos       | **Aplicar** (*Especificar, Estruturar*)                |
|                                                           |                                                          | Pensamento Analítico e Crítico | **Aplicar** (*Decompor, Avaliar*)                      |
|                                                           |                                                          |                              |                                                       |
| Interpretar notação baseada em regras                      | Inventivo, Colaborativo, Responsável, Proativo, Criativo | Autômatos com Pilha            | **Compreender** (*Reconhecer, Explicar, Comparar*)     |
|                                                           |                                                          | Gramáticas Livres de Contexto  | **Compreender** (*Interpretar, Construir, Relacionar*) |
|                                                           |                                                          | Linguagens Regulares           | **Compreender** (*Interpretar, Construir, Relacionar*) |
|                                                           |                                                          | Pensamento Analítico e Crítico | **Aplicar** (*Aprimorar, Validar*)                      |
|                                                           |                                                          |                              |                                                       |
| Diferenciar classificações de gramáticas formais           | Inventivo, Colaborativo, Responsável, Proativo           | Linguagens Regulares           | **Compreender** (*Identificar, Classificar, Comparar*) |
|                                                           |                                                          | Linguagens Livres de Contexto  | **Compreender** (*Reconhecer, Descrever, Diferenciar*) |
|                                                           |                                                          | Pensamento Analítico e Crítico | **Analisar**                                           |
