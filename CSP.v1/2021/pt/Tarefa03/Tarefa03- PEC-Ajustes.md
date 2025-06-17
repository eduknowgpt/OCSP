# Relatório de Revisão e Ajustes na Especificação de Competências: Tarefa03 - Robô Agrícola

## Introdução  

O processo de revisão, baseado no feedback dos especialistas **P1 e P2**, identificou **áreas-chave para melhoria** no framework de especificação de competências. Esses insights foram categorizados em **cinco temas principais**:  
- **Granularidade do Conhecimento** → Garantir nível adequado de detalhamento  
- **Adequação do Conhecimento** → Alinhar competências com conhecimentos relevantes  
- **Vocabulário Controlado** → Padronizar terminologia para consistência  
- **Verbos da Taxonomia de Bloom** → Melhorar clareza nas descrições de habilidades  
- **Clareza Textual** → Refinar descrições para evitar ambiguidades  

Com base nessas recomendações, **diversos refinamentos foram implementados** para melhorar a especificidade, clareza e reusabilidade das competências.

## **Resultados da Revisão e Ajustes Implementados**  

### **Refinamento da Granularidade do Conhecimento**  
Seguindo as sugestões dos revisores, **o sistema de classificação de conhecimento foi atualizado de CC2012 para CS2013**, que oferece uma taxonomia mais **detalhada** e **hierárquica**. Essa mudança garante **maior especificidade**, tornando as competências **mais reutilizáveis** e **melhor alinhadas** com tarefas educacionais.  
  - **"Análise de Requisitos"** foi **redefinida** como **"Engenharia de Requisitos"**  
  - **"Autômatos Finitos"** foi **redefinido** como **"Máquinas de Estados Finitos"**  

## Especificação Revisada de Competências para Tarefa 03

### Reúso de Competências

    > Testagem de Autômatos Usando Simuladores 

    > Redação Técnica Colaborativa de Relatórios

### Especificação da Competência A  

### A.1 Título da Competência

    Desenvolver Soluções de Resolução de Problemas Usando Máquinas de Estados Finitos

### A.2 Descrição Textual

Projete e implemente soluções computacionais usando **Máquinas de Estados Finitos (MEFs)** para modelar sistemas caracterizados por estados e transições, em contextos reais e instrucionais. Esta competência enfatiza a capacidade de traduzir requisitos do sistema em modelos formais que sejam logicamente consistentes, verificáveis e alinhados com os princípios da teoria de autômatos.

Espera-se que os estudantes demonstrem proficiência em:
- Analisar e interpretar especificações de sistemas;
- Aplicar conhecimento teórico de MEFs para construir modelos comportamentais precisos;
- Garantir que os modelos resultantes sejam funcionalmente corretos, logicamente sólidos e adequados ao propósito.

Esta competência promove a integração de métodos formais e habilidades de resolução de problemas, preparando os estudantes para abordar tarefas de modelagem de sistemas com rigor e insight prático.

### A.3 Especificação de Conhecimento

As seguintes áreas de conhecimento são críticas para esta competência:

* **Máquinas de Estados Finitos**
  Compreender e aplicar a estrutura, comportamento e aplicações de autômatos determinísticos e não-determinísticos para modelar sistemas sequenciais.

* **Engenharia de Requisitos**
  Identificar, interpretar e traduzir requisitos do sistema em especificações formais para projeto de MEFs.

* **Pensamento Analítico e Crítico**
  Decompor o problema, avaliar restrições e objetivos, e selecionar estratégias de modelagem apropriadas para guiar o processo de projeto.

### A.4 Pareamento Conhecimento-Habilidade

* **Aplicar** conhecimento de **Máquinas de Estados Finitos** para projetar modelos que reflitam comportamentos do mundo real através de transições de estado estruturadas.

* **Aplicar** **Engenharia de Requisitos** para entender as expectativas do usuário e traduzi-las em especificações formais claras que orientem o projeto de MEFs.

* **Aplicar** **Pensamento Analítico e Crítico (FPK)** para interpretar o problema, analisar possíveis caminhos de projeto e justificar decisões de modelagem baseadas em lógica e viabilidade.

### A.5 Tabela Resumo para Competência A

| **Competência** | **Disposições** | **Conhecimento** | **Habilidade** |
|-----------------|-----------------|------------------|----------------|
| **Desenvolver Soluções de Resolução de Problemas Usando Máquinas de Estados Finitos** | Inventivo, Colaborativo, Responsável, Proativo, Criativo | Máquinas de Estados Finitos | **Aplicar (Usar, Implementar, Criar)** |
| | | Engenharia de Requisitos | **Aplicar (Interpretar, Especificar, Traduzir)** |
| | | Pensamento Analítico e Crítico (FPK) | **Aplicar** |



### Especificação da Competência B

### B.1 Título da Competência

  Projetar Expressões Regulares que Representam Autômatos Finitos

### B.2 Descrição Textual

Esta competência aborda a capacidade de entender e manipular a relação entre **representações de linguagem formal** e **modelos computacionais**. Espera-se que os aprendizes interpretem o comportamento de sistemas baseados em estados e os representem usando expressões simbólicas equivalentes, como expressões regulares.

Envolve aplicar **análise sistemática** para identificar padrões comportamentais e requisitos, e construir ou validar representações formais que descrevam com precisão o comportamento pretendido do sistema. Os aprendizes devem demonstrar tanto compreensão conceitual de linguagens formais quanto competência prática no desenvolvimento de modelos corretos, expressivos e verificáveis.

### B.3 Especificação de Conhecimento

As seguintes áreas de conhecimento são essenciais para esta competência:

* **Expressões Regulares**
    * Compreender a sintaxe e semântica de expressões regulares, bem como seu papel na definição de linguagens formais. Os aprendizes devem reconhecer o poder expressivo e as limitações das expressões regulares e demonstrar capacidade de construí-las, transformá-las e validá-las em alinhamento com o comportamento do sistema.

* **Máquinas de Estados Finitos (MEFs)**
    * Compreender a estrutura e lógica operacional de MEFs, incluindo estados, transições e linguagens aceitas. Os aprendizes devem ser capazes de traduzir requisitos comportamentais em representações de MEFs e estabelecer equivalência formal entre MEFs e expressões regulares.

* **Pensamento Analítico e Crítico**
    * Empregar raciocínio analítico para interpretar restrições do sistema, avaliar corretude e otimizar modelos formais. Os aprendizes devem avaliar criticamente a adequação de expressões regulares e MEFs na representação de comportamentos pretendidos, identificando falhas, redundâncias ou ineficiências em sua estrutura.

### B.4 Pareamento Conhecimento-Habilidade

#### Mapeamento de Conhecimento para Habilidades

Para demonstrar efetivamente esta competência, os estudantes devem ser capazes de:

* **Interpretar** conhecimento de **Expressões Regulares** para analisar o comportamento de autômatos e construir representações simbólicas equivalentes que capturem a mesma linguagem aceita.

* **Aplicar** conhecimento de **Máquinas de Estados Finitos (MEFs)** para decompor requisitos de sistema ou tarefa e traduzi-los em modelos formais expressos através de expressões regulares.

* **Empregar** **Pensamento Analítico e Crítico** para avaliar sistematicamente, refinar e validar expressões regulares quanto à corretude, eficiência e alinhamento com o comportamento pretendido.

#### Anotação de Verbos

As seguintes associações de verbos ilustram como cada área de conhecimento apoia o desenvolvimento de habilidades cognitivas relevantes, baseadas na Taxonomia de Bloom:

* **Compreender** → Expressões Regulares → Interpretar, Relacionar, Representar

* **Aplicar** → Máquinas de Estados Finitos → Decompor, Traduzir, Construir

* **Aplicar** → Pensamento Analítico e Crítico → Analisar, Testar, Refinar

### B.5 Tabela Resumo para Competência B

| **Competência** | **Disposições** | **Conhecimento** | **Habilidade** |
|-----------------|-----------------|------------------|----------------|
| **Projetar Expressões Regulares que Representam Autômatos Finitos** | Inventivo, Colaborativo, Responsável, Proativo, Criativo | Máquinas de Estados Finitos | **Compreender (Interpretar, Relacionar, Representar)** |
| | | Expressões Regulares | **Aplicar (Decompor, Traduzir, Construir)** |
| | | Pensamento Analítico e Crítico (FPK) | **Aplicar (Analisar, Testar, Refinar)** |



### B.4 Tabela Resumo da Competência B

| **Competência**                                            | **Disposições**                                             | **Conhecimento**                              | **Habilidade**                                  |
| ---------------------------------------------------------- | ----------------------------------------------------------- | --------------------------------------------- | ------------------------------------------------ |
| **Determinar Expressões Regulares que Representam Autômatos** | Inventivo, Colaborativo, Responsável, Proativo, Criativo | Máquinas de Estados Finitos                   | **Compreender (Interpretar, Relacionar, Representar)** |
|                                                            |                                                             | Expressões Regulares                          | **Aplicar (Decompor, Traduzir, Construir)**     |
|                                                            |                                                             | Pensamento Analítico e Crítico                | **Aplicar (Analisar, Testar, Refinar)**          |


### **C.1 Título da Competência**

    Identificar Padrões em Máquinas de Estados Finitos


### **C.2 Descrição Textual**

Esta competência foca na habilidade de **analisar a estrutura e o comportamento das Máquinas de Estados Finitos (MEFs)** para identificar padrões recorrentes, regularidades ou redundâncias que influenciem a complexidade, eficiência e expressividade do modelo. Envolve reconhecer como categorias de entrada, lógica de transição e configurações de estados impactam o design e o desempenho de modelos computacionais.

Espera-se que os estudantes demonstrem proficiência na análise de MEFs, identificação de padrões estruturais e aplicação do **pensamento analítico e crítico** para interpretar o comportamento do sistema, otimizar modelos e justificar decisões de projeto fundamentadas em raciocínio formal.


### **C.3 Especificação do Conhecimento**

As seguintes áreas de conhecimento são essenciais para esta competência:

* **Máquinas de Estados Finitos (MEFs)**  
  *Compreender as características estruturais das MEFs — incluindo estados, transições, determinismo e minimização — e como esses elementos impactam a representação e otimização de comportamentos computacionais.*

* **Pensamento Analítico e Crítico**  
  *Aplicar raciocínio lógico e reconhecimento de padrões para detectar estruturas subjacentes, formular inferências baseadas em evidências e tomar decisões informadas sobre o design e aprimoramento de MEFs.*


### **C.5.1 Mapeamento do Conhecimento para Habilidades**

Para demonstrar esta competência, os estudantes devem ser capazes de:

* **Analisar** o conhecimento sobre **Máquinas de Estados Finitos** para examinar arquiteturas de estados, identificar padrões emergentes e avaliar como classificações de entrada influenciam transições e a complexidade do modelo.

* **Aplicar** o conhecimento de **Pensamento Analítico e Crítico** para detectar regularidades estruturais, formular inferências fundamentadas e refinar representações de MEFs com base em requisitos específicos da tarefa e coerência lógica.


### **C.5.3 Anotação de Verbos**

Os seguintes verbos de ação, alinhados à Taxonomia de Bloom, ilustram como cada área de conhecimento apoia o desenvolvimento das habilidades relevantes:

* **Analisar** → *Máquinas de Estados Finitos*  
  → *Examinar*, *Avaliar*, *Comparar*

* **Aplicar** → *Pensamento Analítico e Crítico*  
  → *Inferir*, *Justificar*, *Interpretar*


### C.6 Tabela Resumo da Competência C

| **Competência**                                 | **Disposições**                | **Conhecimento**                        | **Habilidade**                                  |
| ---------------------------------------------- | ------------------------------ | --------------------------------------- | ------------------------------------------------ |
| **Identificar Padrões em Máquinas de Estados Finitos** | Inventivo, Criativo, Meticuloso | Máquinas de Estados Finitos             | **Analisar (Examinar, Avaliar, Comparar)**       |
|                                                |                                | Pensamento Analítico e Crítico (FPK)   | **Aplicar (Inferir, Justificar, Interpretar)**   |



### **Tabela Resumo Unificada das Competências A, B e C**

| **Competência**                                                    | **Disposições**                                             | **Conhecimento**                             | **Habilidade**                                     |
| ------------------------------------------------------------------ | ----------------------------------------------------------- | -------------------------------------------- | -------------------------------------------------- |
| **Desenvolver Soluções de Problemas Usando Máquinas de Estados Finitos** | Inventivo, Colaborativo, Responsável, Proativo, Criativo   | Máquinas de Estados Finitos                  | **Aplicar (Usar, Implementar, Criar)**             |
|                                                                    |                                                             | Engenharia de Requisitos                     | **Aplicar (Interpretar, Especificar, Traduzir)**   |
|                                                                    |                                                             | Pensamento Analítico e Crítico (FPK)        | **Aplicar (Analisar, Justificar, Avaliar)**        |
|                                                                    |                                                               |                                              |                                                    |
| **Determinar Expressões Regulares que Representam Autômatos**      | Inventivo, Colaborativo, Responsável, Proativo, Criativo   | Máquinas de Estados Finitos                  | **Compreender (Interpretar, Relacionar, Representar)** |
|                                                                    |                                                             | Expressões Regulares                         | **Aplicar (Decompor, Traduzir, Construir)**        |
|                                                                    |                                                             | Pensamento Analítico e Crítico (FPK)        | **Aplicar (Analisar, Testar, Refinar)**            |
|                                                                    |                                                               |                                              |                                                    |
| **Identificar Padrões em Máquinas de Estados Finitos**             | Inventivo, Criativo, Meticuloso                             | Máquinas de Estados Finitos                  | **Analisar (Examinar, Avaliar, Comparar)**         |
|                                                                    |                                                             | Pensamento Analítico e Crítico (FPK)        | **Aplicar (Inferir, Justificar, Interpretar)**     |
