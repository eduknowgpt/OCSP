# Relatório de Especificação de Competência: Tarefa01 - A Máquina de Venda Automática de Refrigerantes e Lanches

## Introdução

Com base na estrutura geral definida na metodologia CSP, este relatório apresenta a aplicação do **Processo de Especificação de Competência** para a **Tarefa 1 – A Máquina de Venda Automática de Refrigerantes e Lanches**, um cenário de Aprendizagem Baseada em Problemas (ABP) que explora o uso de **autômatos finitos e expressões regulares** no desenvolvimento de soluções de software e hardware para máquinas de venda automática.

## 1. Análise da Descrição da Tarefa

A tarefa ABP intitulada **"A Máquina de Venda Automática de Refrigerantes e Lanches"** apresenta um problema relacionado ao **cálculo de troco em transações de máquinas automáticas**, onde os pagamentos são efetuados usando moedas e cédulas. A tarefa exige que os estudantes projetem uma solução que permita à máquina aceitar pagamentos, fornecer o troco corretamente e operar conforme requisitos funcionais pré-definidos.

Para resolver esse problema com sucesso, os estudantes devem demonstrar sua capacidade de:
- **Aplicar conceitos de autômatos finitos** para modelar o comportamento da máquina de venda.
- **Simular e validar** a funcionalidade do autômato usando ferramentas computacionais.
- **Documentar o processo de desenvolvimento** de forma estruturada e técnica.

Esta tarefa não apenas avalia a compreensão dos estudantes sobre **teoria dos autômatos**, mas também sua capacidade de:
1. **Analisar restrições do mundo real** e traduzi-las em um modelo computacional formal.
2. **Projetar e implementar** um autômato que atenda aos requisitos funcionais.
3. **Justificar e explicar** decisões de projeto por meio de um relatório técnico bem estruturado.

Além disso, a tarefa introduz um desafio opcional: implementar uma **funcionalidade de troco bônus aleatório**, onde a máquina ocasionalmente fornece um valor extra de R$1,00 quando o preço exato do produto é pago. Isso adiciona um **elemento estocástico** ao sistema, incentivando os estudantes a considerar **comportamentos probabilísticos** no design do autômato.

Por meio deste cenário estruturado de **Aprendizagem Baseada em Problemas (ABP)**, os estudantes se envolvem com um **problema do mundo real**, conectando conhecimento teórico com **modelagem computacional prática**, simulação e documentação técnica.

## 2. Enumeração do Conhecimento

Para enumerar sistematicamente o conhecimento em computação necessário para esta tarefa, foi utilizado o **Sistema de Classificação em Computação da ACM (2012)** como vocabulário controlado. Este sistema é amplamente reconhecido e adotado globalmente, garantindo padronização e consistência na categorização do conhecimento em computação.

Para o **conhecimento profissional (FPK)**, foi referenciado o **Currículo de Computação da ACM (CC) 2020**, que fornece uma estrutura organizada para competências profissionais essenciais.

Com base na **descrição da tarefa**, foi identificado o seguinte conjunto de componentes de conhecimento necessários:

### **Conhecimento em Computação**  
- **Autômatos sobre Objetos Infinitos**  
  - Envolve o estudo e aplicação de modelos matemáticos que descrevem sistemas computacionais usando **estados e transições**.  
  - Essencial para o projeto da **lógica baseada em estados da máquina de venda**.  

- **Autômatos Finitos Não Determinísticos (AFN)**  
  - Representa uma classe de autômatos que permite múltiplas transições possíveis para uma dada entrada a partir de um estado.  
  - Importante para entender o poder expressivo e a flexibilidade no projeto de reconhecedores de linguagens regulares.  
  - Fornece conhecimento fundamental para modelar máquinas de estados compactas e versáteis, que podem ser posteriormente convertidas para formas determinísticas para implementação.

- **Linguagens Regulares (Expressões Regulares)**  
  - Requer compreensão e aplicação de **técnicas formais** para representar e manipular conjuntos de strings.  
  - Usado principalmente em **processamento de texto, análise léxica e reconhecimento de padrões** dentro da lógica operacional da máquina de venda.

- **Análise de Requisitos (Engenharia de Requisitos de Software)**  
  - Processo sistemático para **coletar, analisar e especificar requisitos do sistema**.  
  - Garante que **necessidades do usuário e expectativas do sistema** sejam claramente compreendidas e documentadas.

- **Ferramentas de Simulação**  
  - Uso de **ferramentas de simulação de autômatos** (como JFLAP) para validar e analisar **soluções propostas**.  
  - Permite **testar, depurar e refinar** o autômato da máquina de venda antes da implementação.

### **Conhecimento Profissional (FPK)**  
- **Pensamento Analítico e Crítico**  
  - Capacidade de **decompor problemas complexos em componentes fundamentais**, avaliar resultados e tomar decisões bem fundamentadas baseadas em análises rigorosas.

- **Resolução de Problemas e Diagnóstico**  
  - Requer identificar, analisar e resolver **desafios específicos da tarefa** utilizando **estratégias eficazes e métodos computacionais** para desenvolver soluções ótimas.

- **Comunicação Escrita**  
  - Habilidade para **produzir relatórios técnicos claros e estruturados** detalhando os processos de projeto, implementação e validação.  
  - Garante que descobertas e decisões sejam comunicadas efetivamente aos interessados.

Esta **enumeração de conhecimento** serve como base para a especificação de competências, garantindo que os estudantes adquiram tanto **expertise teórica quanto prática** necessária para completar a tarefa com sucesso.

## 3. Identificação dos Objetivos de Aprendizagem

O **objetivo geral** desta tarefa é desenvolver **autômatos finitos e expressões regulares** para resolver **problemas do mundo real** modelando um sistema de máquina de venda automática. Este objetivo enfatiza a aplicação prática da **teoria dos autômatos** na resolução computacional de problemas.

### **Objetivos Específicos de Aprendizagem**  
Para alcançar este objetivo geral, os estudantes devem demonstrar a capacidade de:

1. **Identificar funcionalidades do sistema**  
   - Analisar o modelo conceitual do usuário da máquina de venda e definir seus comportamentos esperados.

2. **Alinhar requisitos do usuário com funcionalidades do autômato**  
   - Conciliar as funcionalidades desejadas da máquina de venda com as restrições e capacidades do autômato em desenvolvimento.

3. **Avaliar o papel do não determinismo em autômatos finitos**  
   - Analisar quando e como **autômatos finitos não determinísticos (AFN)** podem ser usados efetivamente no projeto do sistema.

4. **Compreender equivalências entre autômatos determinísticos e não determinísticos**  
   - Demonstrar entendimento da equivalência entre **Autômatos Finitos Determinísticos (AFD)** e **Autômatos Finitos Não Determinísticos (AFN)**, destacando cenários em que um pode ser preferível ao outro.

5. **Entender a equivalência entre Autômatos Finitos (AF) e Expressões Regulares (ER)**  
   - Estabelecer conexões entre as **representações por autômatos finitos** e as **expressões regulares**, reforçando sua intercambialidade teórica e prática.

6. **Aplicar a equivalência AF-ER no desenvolvimento de expressões regulares**  
   - Utilizar autômatos finitos existentes para derivar **expressões regulares correspondentes**, aplicando métodos formais para converter autômatos em padrões regex equivalentes.

7. **Associar opções da máquina, moedas e cédulas a símbolos do alfabeto**  
   - Mapear elementos reais da máquina de venda (como seleções de produtos e formas de pagamento) ao **alfabeto formal** usado no design do autômato.

8. **Desenvolver relatórios técnicos**  
   - Documentar o **projeto, implementação e validação** do autômato, garantindo clareza e precisão na redação técnica.

9. **Utilizar ferramentas de simulação de autômatos**  
   - Aplicar ferramentas como o **JFLAP** para simular, analisar e verificar a funcionalidade do autômato projetado.

### **Importância Destes Objetivos**  
Esses objetivos de aprendizagem fornecem um **caminho estruturado** para o desenvolvimento de competências, assegurando que os estudantes adquiram:  
- **Uma base teórica sólida** em autômatos e linguagens formais.  
- **A capacidade de conectar teoria e prática**, aplicando métodos formais para resolver problemas computacionais.  
- **Experiência prática com ferramentas de simulação**, reforçando habilidades concretas de resolução de problemas.  
- **Habilidades de comunicação técnica**, essenciais para transmitir soluções em contextos profissionais e acadêmicos.

Ao alcançar esses objetivos, os estudantes estarão capacitados com as **habilidades computacionais e analíticas** necessárias para modelar sistemas reais usando **autômatos finitos e expressões regulares**.

## 4. Definição da Competência

As competências são especificadas com base nos **Objetivos de Aprendizagem (OAs)** identificados na análise da tarefa.

### 4.1 Especificação da Competência A  

### A.1 Título da Competência  
Aplicar Autômatos Finitos para Modelagem de Sistemas Computacionais

### A.2 Descrição Textual  
Esta competência consiste na habilidade de **projetar e aplicar autômatos finitos**, incluindo versões determinísticas e não determinísticas, para modelar comportamentos de sistemas computacionais, como máquinas de venda automática. O aprendiz deve ser capaz de analisar requisitos do mundo real, traduzi-los em estados e transições, simular e validar o autômato usando ferramentas computacionais, e documentar claramente o processo.

A competência inclui a capacidade de iterar e refinar o modelo, adaptando-se a funcionalidades adicionais como a implementação do troco bônus aleatório.

### A.3 Especificação do Conhecimento  
- Autômatos Finitos Determinísticos (AFD) e Não Determinísticos (AFN)  
- Teoria de Linguagens Formais  
- Técnicas de Simulação de Autômatos (ferramentas como JFLAP)  
- Engenharia de Requisitos  
- Documentação Técnica  

### A.4 Especificação da Disposição  
- Atenção cuidadosa aos detalhes ao mapear requisitos para transições do autômato.  
- Persistência para iterar e refinar o modelo até atingir a conformidade desejada.  
- Proatividade em buscar e integrar feedback de simulações para melhorar a solução.  
- Flexibilidade para adaptar o modelo conforme necessidades adicionais, como o troco bônus aleatório.  

### 4.2 Especificação da Competência B  

### B.1 Título da Competência  
Aplicar Expressões Regulares para Reconhecimento de Padrões

### B.2 Descrição Textual  
Esta competência refere-se à habilidade de **utilizar expressões regulares** para reconhecer padrões dentro de sequências simbólicas, facilitando a análise e o processamento de dados estruturados. O aprendiz deve ser capaz de **criar, interpretar e manipular expressões regulares**, compreendendo sua equivalência com autômatos finitos e sua aplicação prática em sistemas computacionais.

Ela inclui a capacidade de associar símbolos do alfabeto a elementos do mundo real (como moedas, cédulas, opções de produtos) e utilizar essas associações para definir padrões que identificam sequências válidas de operações na máquina de venda.

Além disso, envolve a aplicação de **ferramentas computacionais para validar expressões regulares**, garantindo que os padrões correspondam corretamente às linguagens especificadas e suportem a funcionalidade esperada do sistema.

### B.3 Especificação do Conhecimento  
- **Expressões Regulares (ER)**  
  - Conhecimento formal para construir e interpretar padrões de linguagens regulares.  

- **Equivalência entre Autômatos Finitos e Expressões Regulares**  
  - Entendimento dos processos formais para conversão entre autômatos e ERs.  

- **Ferramentas de Simulação**  
  - Uso de software para validar e testar expressões regulares aplicadas.

- **Comunicação Escrita (FPK)**  
  - Capacidade para documentar o processo e resultados de forma clara e técnica.  

### B.4 Especificação da Disposição  
- Curiosidade para explorar as possibilidades de expressões regulares em problemas computacionais.  
- Precisão ao mapear requisitos em padrões formais.  
- Capacidade de perseverar na validação e refinamento dos padrões.  
- Disposição para documentar e comunicar os resultados de forma clara.

## 5. Resumo da Especificação de Competências

| Código da Competência | Título da Competência                     | Conhecimentos Relacionados                           | Atitudes e Disposições                 |
|-----------------------|------------------------------------------|-----------------------------------------------------|--------------------------------------|
| A                     | Projetar Soluções Eficientes com Autômatos | Autômatos Finitos, Análise de Requisitos, Pensamento Analítico, Ferramentas de Simulação | Atenção, Persistência, Proatividade, Flexibilidade |
| B                     | Aplicar Expressões Regulares para Reconhecimento de Padrões | Expressões Regulares, Equivalência AF-ER, Ferramentas de Simulação, Comunicação Escrita | Curiosidade, Precisão, Perseverança, Comunicação Clara |



### A.6 Tabela Resumo da Competência A

| **Competência** | **Disposições**                     | **Conhecimentos**                     | **Habilidade**                             |
|-----------------|-----------------------------------|-------------------------------------|-------------------------------------------|
|                 |                                   | Autômatos sobre Objetos Infinitos   | **Aplicar (Construir, Desenvolver, Projetar)** |
| **Desenvolver soluções para problemas usando Autômatos** | **Colaborativo, Responsável, Proativo, Criativo** | Análise de Requisitos                    | **Aplicar (Interpretar, Implementar, Organizar)** |
|                 |                                   | Pensamento Analítico e Crítico (FPK) | **Aplicar**                              |

---

### 4.2 Especificação da Competência B

#### B.1 Título da Competência  
Determinar Quando Usar Autômatos Finitos Determinísticos (DFA)

#### B.2 Descrição da Competência  
Esta competência foca em **compreender o determinismo em autômatos finitos** e **determinar quando aplicar o não-determinismo**. Os estudantes devem analisar as restrições do sistema e **decidir se um autômato determinístico ou não-determinístico** é a melhor escolha para resolver um dado problema.

Esta competência requer a habilidade de:  
- **Diferenciar autômatos determinísticos e não-determinísticos** com base em suas propriedades e aplicações práticas.  
- **Avaliar os requisitos do problema** para determinar o modelo de autômato mais eficiente.  
- **Justificar a escolha** do tipo de autômato com raciocínio lógico e limitações computacionais.

#### B.3 Especificação de Conhecimento  
As seguintes áreas de conhecimento são essenciais para esta competência:  

- **Autômatos sobre Objetos Infinitos**  
  - Compreensão das características, limitações e aplicações dos modelos **determinísticos vs. não-determinísticos**.  
  - Identificação de cenários onde um modelo pode ser mais vantajoso que o outro.  

- **Pensamento Analítico e Crítico (FPK)**  
  - Necessário para **avaliar as restrições do sistema e tomar decisões informadas**.  
  - Permite que os estudantes desenvolvam **raciocínio estratégico** ao escolher entre modelos DFA e NFA.  

#### B.4 Especificação de Disposições  
Similar à **Competência A**, esta competência requer que os estudantes demonstrem atributos comportamentais fundamentais para facilitar a resolução de problemas e a tomada de decisões:  

- **Pensamento Investigativo** – Estimula a curiosidade e **análise crítica** das propriedades dos autômatos e suas aplicações.  
- **Colaboração** – Apoia o trabalho em equipe na discussão e justificativa das escolhas.


---

### B.5 Tabela Resumo da Competência B

| **Competência**                                  | **Disposições**                                | **Conhecimentos**                          | **Habilidade**                                    |
|-------------------------------------------------|------------------------------------------------|--------------------------------------------|--------------------------------------------------|
|                                                 |                                                | Autômatos sobre Objetos Infinitos          | **Compreender (Diferenciar, Analisar)**          |
| **Determinar quando usar Autômatos Finitos Determinísticos (DFA)** | **Investigativo, Colaborativo, Responsável** | Pensamento Analítico e Crítico (FPK)       | **Aplicar (Avaliar, Decidir, Justificar)**       |

---

### 4.3 Especificação da Competência C

#### C.1 Título da Competência  
Projetar Autômatos Finitos para Reconhecimento de Linguagens

#### C.2 Descrição da Competência  
Esta competência envolve a capacidade de **projetar autômatos finitos** (determinísticos ou não-determinísticos) que reconheçam linguagens específicas, baseando-se em requisitos funcionais fornecidos.

O estudante deve ser capaz de:  
- Interpretar a descrição formal de uma linguagem.  
- Construir um autômato finito adequado para reconhecer essa linguagem.  
- Validar o autômato projetado, verificando se ele aceita ou rejeita corretamente cadeias de entrada.

#### C.3 Especificação de Conhecimento  
Os conhecimentos relevantes incluem:  

- **Autômatos sobre Objetos Infinitos**  
  - Estrutura e funcionamento dos autômatos finitos determinísticos e não-determinísticos.  
  - Técnicas de construção e equivalência entre autômatos.  

- **Análise de Requisitos**  
  - Entendimento dos requisitos da linguagem para construir o autômato correto.

- **Pensamento Analítico e Crítico (FPK)**  
  - Avaliação da precisão do autômato e suas limitações.

#### C.4 Especificação de Disposições  
São essenciais as seguintes disposições comportamentais:  

- **Proatividade** – Para assumir a liderança na construção do autômato.  
- **Criatividade** – Para desenvolver soluções inovadoras e eficientes.  
- **Precisão** – Para garantir que o autômato funcione conforme esperado.

---

### C.5 Tabela Resumo da Competência C

| **Competência**                               | **Disposições**                     | **Conhecimentos**                     | **Habilidade**                                |
|----------------------------------------------|-----------------------------------|-------------------------------------|----------------------------------------------|
|                                              |                                   | Autômatos sobre Objetos Infinitos   | **Aplicar (Projetar, Construir, Validar)**   |
| **Projetar Autômatos Finitos para Reconhecimento de Linguagens** | **Proativo, Criativo, Preciso**    | Análise de Requisitos                | **Compreender (Interpretar, Analisar)**      |
|                                              |                                   | Pensamento Analítico e Crítico (FPK) | **Aplicar (Avaliar)**                        |


---

### 4.4 Especificação da Competência D

#### D.1 Título da Competência  
Construir Expressões Regulares para Descrever Linguagens Formais

#### D.2 Descrição da Competência  
Esta competência envolve a capacidade de construir expressões regulares que descrevam linguagens formais específicas, incluindo operações como união, concatenação e fecho de Kleene.

O estudante deve ser capaz de:  
- Interpretar linguagens formais descritas por expressões regulares.  
- Construir expressões regulares que descrevam conjuntos de cadeias de caracteres.  
- Utilizar expressões regulares para modelar linguagens reconhecíveis por autômatos.

#### D.3 Especificação de Conhecimento  
Os conhecimentos necessários incluem:  

- **Expressões Regulares**  
  - Símbolos e operações básicas: união, concatenação e fecho de Kleene.  
  - Equivalência entre expressões regulares e autômatos finitos.

- **Teoria da Linguagem Formal**  
  - Definição e propriedades de linguagens regulares.

- **Pensamento Analítico e Crítico (FPK)**  
  - Capacidade de analisar e construir expressões regulares eficazes e corretas.

#### D.4 Especificação de Disposições  
São valorizadas as seguintes disposições:  

- **Rigor** – Para assegurar precisão na construção das expressões.  
- **Perseverança** – Para lidar com dificuldades na modelagem das linguagens.  
- **Curiosidade** – Para explorar diferentes maneiras de representar linguagens.

---

### D.5 Tabela Resumo da Competência D

| **Competência**                                  | **Disposições**                        | **Conhecimentos**                      | **Habilidade**                                  |
|-------------------------------------------------|--------------------------------------|--------------------------------------|------------------------------------------------|
|                                                 |                                      | Expressões Regulares                  | **Aplicar (Construir, Modelar, Interpretar)**  |
| **Construir Expressões Regulares para Descrever Linguagens Formais** | **Rigor, Perseverança, Curiosidade** | Teoria da Linguagem Formal            | **Compreender (Analisar, Avaliar)**             |
|                                                 |                                      | Pensamento Analítico e Crítico (FPK) | **Aplicar (Avaliar, Justificar)**               |

---

### 4.5 Especificação da Competência E

#### E.1 Título da Competência  
Analisar e Validar Modelos Computacionais para Reconhecimento de Linguagens

#### E.2 Descrição da Competência  
Esta competência envolve a habilidade de analisar e validar modelos computacionais, como autômatos finitos e expressões regulares, garantindo que eles reconheçam corretamente as linguagens para as quais foram projetados.

O estudante deve ser capaz de:  
- Verificar a correção e completude dos modelos.  
- Testar os modelos com conjuntos de cadeias representativas.  
- Comparar diferentes modelos para a mesma linguagem e justificar a escolha.

#### E.3 Especificação de Conhecimento  
Conhecimentos necessários incluem:  

- **Modelos Computacionais**  
  - Autômatos finitos determinísticos e não determinísticos.  
  - Expressões regulares e suas propriedades.

- **Técnicas de Validação**  
  - Métodos para testar e validar modelos.

- **Pensamento Analítico e Crítico (FPK)**  
  - Capacidade de avaliar e justificar decisões sobre modelos.

#### E.4 Especificação de Disposições  
As seguintes disposições são importantes:  

- **Cuidado** – Para garantir a qualidade da validação.  
- **Persistência** – Para iterar testes e ajustes.  
- **Comunicação** – Para apresentar justificativas claras.

---

### E.5 Tabela Resumo da Competência E

| **Competência**                              | **Disposições**                   | **Conhecimentos**                 | **Habilidade**                                |
|---------------------------------------------|---------------------------------|---------------------------------|----------------------------------------------|
|                                             |                                 | Modelos Computacionais           | **Aplicar (Analisar, Validar, Comparar)**    |
| **Analisar e Validar Modelos Computacionais para Reconhecimento de Linguagens** | **Cuidado, Persistência, Comunicação** | Técnicas de Validação            | **Compreender (Avaliar, Justificar)**         |
|                                             |                                 | Pensamento Analítico e Crítico (FPK) | **Aplicar (Testar, Argumentar)**            |


---

### 4.6 Especificação da Competência F

#### F.1 Título da Competência  
Projetar Autômatos Finitos para Reconhecimento de Linguagens Regulares

#### F.2 Descrição da Competência  
Esta competência envolve a habilidade de projetar autômatos finitos, tanto determinísticos quanto não determinísticos, capazes de reconhecer linguagens regulares específicas.

O estudante deve ser capaz de:  
- Construir autômatos a partir de expressões regulares e descrições formais.  
- Identificar estados, transições e estados finais corretamente.  
- Otimizar autômatos para eficiência e simplicidade.

#### F.3 Especificação de Conhecimento  
Conhecimentos fundamentais incluem:  

- **Autômatos Finitos**  
  - Conceitos de estados, transições, estado inicial e final.  
  - Autômatos determinísticos (AFD) e não determinísticos (AFN).

- **Expressões Regulares e Linguagens Regulares**  
  - Equivalência e conversão entre autômatos e expressões regulares.

- **Princípios de Otimização**  
  - Minimização de estados.

#### F.4 Especificação de Disposições  
As seguintes disposições são essenciais:  

- **Rigor** – Para construção precisa do autômato.  
- **Criatividade** – Para encontrar soluções eficientes.  
- **Detalhismo** – Para identificar e corrigir erros.

---

### F.5 Tabela Resumo da Competência F

| **Competência**                                 | **Disposições**                 | **Conhecimentos**                  | **Habilidade**                                    |
|------------------------------------------------|--------------------------------|----------------------------------|--------------------------------------------------|
|                                                |                                | Autômatos Finitos                | **Aplicar (Projetar, Construir, Otimizar)**      |
| **Projetar Autômatos Finitos para Reconhecimento de Linguagens Regulares** | **Rigor, Criatividade, Detalhismo** | Expressões Regulares e Linguagens Regulares | **Compreender (Converter, Relacionar)**          |
|                                                |                                | Princípios de Otimização         | **Aplicar (Minimizar, Analisar)**                 |

### F.6 Tabela Resumo para a Competência F

| **Competência**                    | **Disposições**                     | **Conhecimentos**                   | **Habilidade**                                |
|----------------------------------|-----------------------------------|-----------------------------------|----------------------------------------------|
| **Redação Colaborativa de Relatórios Técnicos** | Colaborativo, Meticuloso, Responsável | **Comunicação Escrita (FPK)**      | **Aplicar (Escrever, Estruturar, Revisar, Refinar)** |


## Tabela Resumo das Competências para a Tarefa: *A Máquina de Venda de Refrigerantes e Lanches*

| **Competência**                           | **Disposições**                             | **Conhecimentos**                         | **Habilidade**                                         |
|------------------------------------------|---------------------------------------------|-----------------------------------------|-------------------------------------------------------|
| **Desenvolver soluções para problemas usando Autômatos** | Colaborativo, Responsável, Proativo, Criativo | Autômatos sobre Objetos Infinitos       | Aplicar (Construir, Desenvolver, Projetar)             |
|                                          |                                             | Análise de Requisitos                    | Aplicar (Interpretar, Implementar, Organizar)          |
|                                          |                                             | Pensamento Analítico e Crítico (FPK)    | Aplicar                                                |
|                                          |                                             |                                         |                                                       |
| **Determinar quando usar um AFD ou AFN** | Investigativo, Colaborativo, Responsável, Proativo, Criativo | Autômatos sobre Objetos Infinitos       | Compreender (Comparar)                                 |
|                                          |                                             | Pensamento Analítico e Crítico (FPK)    | Aplicar (Avaliar, Decidir)                             |
|                                          |                                             |                                         |                                                       |
| **Testar Autômatos Usando Simuladores**  | Colaborativo, Responsável, Proativo, Criativo | Autômatos sobre Objetos Infinitos       | Aplicar (Experimentar, Relacionar, Simular)            |
|                                          |                                             | Resolução de Problemas e Depuração (FPK)| Aplicar (Diagnosticar, Depurar, Refinar)               |
|                                          |                                             |                                         |                                                       |
| **Determinar Expressões Regulares que Representam Autômatos** | Investigativo, Colaborativo, Responsável, Proativo, Criativo | Autômatos sobre Objetos Infinitos       | Compreender                                            |
|                                          |                                             | Linguagens Regulares                    | Aplicar                                                |
|                                          |                                             | Resolução de Problemas e Depuração (FPK)| Aplicar                                                |
|                                          |                                             |                                         |                                                       |
| **Relacionar Expressões Regulares a Autômatos Finitos** | Colaborativo, Responsável, Proativo         | Autômatos sobre Objetos Infinitos       | Compreender                                            |
|                                          |                                             | Linguagens Regulares                    | Compreender                                           |
|                                          |                                             |                                         |                                                       |
| **Redação Colaborativa de Relatórios Técnicos** | Colaborativo, Meticuloso, Responsável       | Comunicação Escrita (FPK)                | Aplicar (Escrever, Estruturar, Revisar, Refinar)       |
