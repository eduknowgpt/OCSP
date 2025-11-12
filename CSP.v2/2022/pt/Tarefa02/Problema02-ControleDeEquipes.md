# Problema 2: Controle de Equipes

**Autores**: Lais Salvador, Edeyson A. Gomes, Luiz Gavaza
**Data**: 12 de abril de 2022

## 1. Problema

A empresa *SOS Florestal* ficou satisfeita com os protótipos entregues para o problema do monitoramento por drones. Entretanto, uma nova regulamentação institucional exige adaptações no sistema de vigilância para atender às normas de segurança das equipes especializadas enviadas para lidar com os problemas detectados (como desmatamento, assoreamento de rios e incêndios).

De acordo com o regulamento, cada equipe deve ser composta por uma proporção fixa de voluntários (V) e não voluntários (NV), dependendo do tipo de evento. Essa proporção é expressa pela fórmula:
**Vi ≥ ni × NVi**, onde **ni > 0** é um fator definido para cada tipo de evento *i* (desmatamento, assoreamento ou incêndios).

Para cumprir o regulamento, o drone será equipado com um receptor capaz de capturar sinais emitidos pelos dispositivos individuais de cada membro da equipe, os quais transmitem:

* Localização geográfica
* Identificação única
* Status de voluntário (V) ou não voluntário (NV)

Devido à baixa potência de transmissão desses dispositivos, o drone deve sobrevoar a área para coletar os dados. Caso a proporção entre voluntários e não voluntários em uma determinada região não atenda ao requisito regulamentar, o drone deve emitir um alerta à base.

A equipe de estudantes da UFBA, responsável pelo desenvolvimento do protótipo, analisou o novo requisito e concluiu que **uma simples máquina de estados finitos não é suficiente para resolver o problema**. Surge então uma questão importante: quais fatores levaram a essa conclusão?

Para atender à regulamentação de composição das equipes, os estudantes perceberam que, no primeiro protótipo do módulo de controle de equipes, seria necessário **fixar o número de voluntários para cada não voluntário**, com base na proporção exigida para cada tipo de evento monitorado.

Após uma análise mais aprofundada, eles identificaram que **a inclusão de um dispositivo de memória auxiliar na máquina de estados** possibilitaria uma modelagem adequada da solução. Essa adição permite o registro e a validação em tempo real da proporção entre voluntários e não voluntários, garantindo conformidade com o regulamento.

Além disso, os estudantes observaram que o módulo de vigilância inicial desenvolvido no **Problema 1** poderia ser estendido para incluir a funcionalidade de controle de equipes. Alternativamente, os dois módulos poderiam ser implementados como **soluções independentes**, operando em paralelo, mas **comunicando-se entre si** para compartilhar dados relevantes.

Por fim, a *SOS Florestal* demonstrou interesse em uma **notação formal** que documente as regras de geração das equipes de forma clara e estruturada. Essa notação seria útil tanto para o controle operacional quanto para futuras melhorias.

A ferramenta sugerida para simular o módulo de controle de equipes é o [JFLAP](http://www.jflap.org).

## 2. Processo

Para desenvolver a solução, será adotada a metodologia de **Aprendizagem Baseada em Problemas (Problem-Based Learning – PBL)**. O PBL é reconhecido por utilizar problemas do mundo real como ponto de partida para estimular o desenvolvimento de habilidades essenciais, como pensamento crítico, trabalho em equipe e resolução de problemas. Essa abordagem contribui significativamente para a construção de conhecimento em torno de um tema específico.

A documentação do processo será realizada por meio de um quadro PBL (*PBL whiteboard*), estruturado em quatro colunas principais: **QUESTÕES**, **FATOS**, **IDEIAS/HIPÓTESES** e **AÇÕES**. Cada equipe deverá preencher e atualizar o quadro a cada reunião, garantindo o registro do processo de resolução do problema. Esse material será um componente importante da avaliação em grupo.

Além disso, será disponibilizado um documento compartilhado para que as equipes mantenham um **Diário de Bordo (Logbook)**, conforme orientado na reunião síncrona inicial. O diário servirá como registro complementar das atividades realizadas, decisões tomadas e desafios enfrentados durante o desenvolvimento.

Essa abordagem integrada assegura não apenas a organização e o acompanhamento do progresso, mas também promove a reflexão contínua e o aprendizado colaborativo entre os participantes.

## 3. Entregáveis

Um membro da equipe deverá submeter, por meio do Ambiente Virtual de Aprendizagem (AVA) da UFBA, até **18h do dia 02/05/2022**, os seguintes materiais:

* Um **arquivo JFLAP** contendo os **módulos de vigilância e controle de equipes do drone**.
* Um **relatório técnico no formato de artigo da SBC (Sociedade Brasileira de Computação)** descrevendo em detalhe o projeto e o funcionamento dos módulos.

O relatório deve incluir todas as operações do sistema e pelo menos dois exemplos de uso. Além disso, deve abordar as expectativas da empresa quanto à documentação e aos aspectos orçamentários.

## 4. Cronograma

| Data  | Sessão Tutorial                |
| ----- | ------------------------------ |
| 13/04 | Sessão Tutorial 1 – Problema 2 |
| 20/04 | Sessão Tutorial 2 – Problema 2 |
| 27/04 | Sessão Tutorial 3 – Problema 2 |
| 04/05 | Entrega da Solução             |

## 5. Recursos de Aprendizagem

* **RAMOS, M. V. M.; JOSÉ NETO, J.; VEGA, I. S.**
  *Linguagens Formais: Teoria, Modelagem e Implementação*. Bookman, 2009.

* **MENEZES, Paulo Blauth.**
  *Linguagens Formais e Autômatos*, 6ª ed. Bookman, 2011.

* **VIEIRA, Newton José.**
  *Linguagens e Máquinas: Uma Introdução aos Fundamentos da Computação*, 2004.

## 6. Conceitos Envolvidos

1. Máquinas de Estados Finitos
2. Linguagens Livres de Contexto
3. Gramáticas Livres de Contexto
4. Autômatos com Pilha
5. Hierarquia de Chomsky

## 7. Objetivos de Aprendizagem

### 7.1 Objetivos Gerais

1. Desenvolver habilidades para modelar, implementar e analisar sistemas computacionais utilizando conceitos de linguagens formais e autômatos.
2. Aplicar conhecimentos de Teoria da Computação para resolver problemas práticos relacionados ao monitoramento e controle operacional em cenários do mundo real.

### 7.2 Objetivos Específicos

1. Reconhecer problemas computacionais que exigem modelos baseados em memória, como os Autômatos com Pilha.
2. Projetar um sistema que combine Máquinas de Estados Finitos com dispositivos de memória para atender a requisitos específicos (por exemplo, proporções entre voluntários e não voluntários).
3. Modelar e simular o comportamento do sistema no JFLAP, garantindo conformidade com os regulamentos institucionais.
4. Relacionar o funcionamento da máquina com os conceitos de Linguagens e Gramáticas Livres de Contexto.
5. Determinar e justificar o número mínimo de estados, transições e regras necessários para uma implementação eficiente.
6. Elaborar um relatório técnico em formato SBC, detalhando as operações do sistema e apresentando exemplos concretos.
7. Simular e validar o comportamento do sistema no JFLAP, demonstrando conformidade com os requisitos operacionais.
8. Trabalhar colaborativamente para integrar conhecimentos e propor soluções criativas e fundamentadas.
9. Avaliar as limitações das Máquinas de Estados Finitos e discutir como o uso de memória amplia suas capacidades.
