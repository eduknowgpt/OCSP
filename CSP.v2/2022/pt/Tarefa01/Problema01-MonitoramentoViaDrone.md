# Problema 1: Monitoramento via Drone

**Autores**:  
Lais Salvador, Edeyson A. Gomes, Luiz Gavaza  
**Data**: 21 de março de 2022  



## Problema

A empresa *SOS Florestal* está desenvolvendo um protótipo de drone de vigilância destinado ao monitoramento florestal, com o objetivo de identificar eventos como desmatamento, assoreamento e incêndios florestais. Este drone será equipado com um módulo ótico de última geração, capaz de filmar e fotografar com zoom de até 60 vezes, além de utilizar sensores infravermelhos e de detecção de calor. Durante o monitoramento, ele transmite imagens e vídeos em tempo real para sua base, permitindo a análise dos dados e a identificação de áreas desmatadas, rios assoreados ou incêndios, incluindo focos iniciais.

Para cada transmissão (foto ou vídeo), o drone associa informações adicionais obtidas por seu sistema GPS avançado, como geolocalização, altura, velocidade (a ser calculada), além de dados barométricos e a temperatura estimada no solo. Planeja-se, futuramente, incluir novos sensores para ampliar as informações coletadas.

Ao receber os dados do drone, a base de controle pode emitir comandos para reposicionar o drone em uma nova coordenada e altura (respeitando a distância máxima de 5 km), solicitar novas fotos com diferentes níveis de zoom ou filmagens com duração e zoom especificados.

Quando um dos eventos monitorados é identificado, uma equipe especializada é designada para avaliar ou solucionar o problema. O tamanho da equipe depende da extensão do evento detectado, como o tamanho do incêndio, da área desmatada ou do trecho assoreado.

Um dos técnicos da *SOS Florestal*, que também é estudante de um curso de Computação na UFBA, trouxe este problema para ser trabalhado em equipe por seus colegas de turma, com o objetivo de desenvolver um protótipo funcional para o módulo de vigilância do drone.

Por restrições econômicas, a *SOS Florestal* busca uma solução de baixo custo para este primeiro protótipo. Durante as pesquisas iniciais, os estudantes identificaram que o problema pode ser modelado e resolvido utilizando uma máquina de estados finitos. Essa conclusão levanta uma questão interessante: como chegaram a essa solução?

Além disso, os estudantes descobriram uma expressão matemática frequentemente utilizada em protocolos e de fácil compreensão, que pode ser incorporada na documentação do projeto. Essa expressão, segundo os alunos, pode ser elaborada assim que o sistema for implementado com uma máquina de estados finitos. Após uma apresentação dessa possibilidade em uma reunião, a empresa demonstrou interesse em explorar mais detalhes.

A empresa também deseja investigar a viabilidade de estabelecer uma regra que permita determinar a quantidade mínima de estados e transições da máquina de estados, com base no número mínimo de eventos que se deseja monitorar. Esse conhecimento ajudaria a realizar orçamentos mais precisos e a otimizar o desenvolvimento do protótipo.

A ferramenta sugerida para simular o processo do módulo de vigilância do drone é o [JFLAP](http://www.jflap.org).



## Processo

Para a construção da solução, será adotada a metodologia de ensino e aprendizagem *Problem-Based Learning* (PBL), que se destaca por utilizar problemas do mundo real como ponto de partida para estimular o desenvolvimento de habilidades essenciais, como pensamento crítico, trabalho em equipe e resolução de problemas. Além disso, a abordagem contribui significativamente para a construção do conhecimento em torno de um tema específico.

A documentação do processo será realizada por meio do quadro-branco PBL, estruturado em quatro colunas principais: **QUESTÕES**, **FATOS**, **IDEIAS/HIPÓTESES** e **AÇÕES**. A cada reunião, cada equipe deverá preencher e atualizar o quadro-branco, garantindo o registro dos passos seguidos para a construção da solução. Esse material será um componente importante da avaliação do grupo, refletindo o progresso e o raciocínio coletivo durante o projeto.

Adicionalmente, será disponibilizado um documento compartilhado para que as equipes preencham o **Diário de Bordo**, conforme instruído durante o encontro síncrono inicial. O Diário de Bordo servirá como um registro complementar, detalhando as atividades realizadas, decisões tomadas e os desafios enfrentados ao longo do processo de desenvolvimento.

Essa abordagem integrada garante não apenas a organização e o acompanhamento do trabalho, mas também promove a reflexão contínua e o aprendizado colaborativo entre os participantes.



## Produto

Um integrante da equipe deverá postar no **AVA UFBA** até as **23:59 do dia 03/04/2022**, no espaço apropriado para tal:
- Um arquivo para o simulador **JFLAP** com o módulo de vigilância do drone.
- Um relatório no modelo de artigos da **SBC (Sociedade Brasileira de Computação)** que descreva com o máximo de detalhes a idealização de funcionamento de tal módulo.  

O relatório deverá conter as operações executadas para funcionamento do sistema e, ao menos, 2 (dois) exemplos de funcionamento. Lembrando que esse relatório também deve contemplar os interesses/questionamentos da empresa com relação à documentação e orçamentos.



## Cronograma

| **Data**  | **Sessão Tutorial**             |
|-----------|---------------------------------|
| 24/03     | Sessão Tutorial - Problema 1    |
| 31/03     | Sessão Tutorial - Problema 1    |
| 03/04     | Entrega da Solução              |



## Recursos para Aprendizagem

- RAMOS, M. V. M.; JOSÉ NETO, J.; VEGA, I. S. **Linguagens Formais: Teoria, Modelagem e Implementação**. Editora Bookman, 2009.  
- MENEZES, Paulo Blauth. **Linguagens formais e autômatos**. 6. ed. Bookman, 2011.



## Conhecimentos/Conceitos Envolvidos

1. Máquina de Estados  
2. Linguagens Regulares  
3. Expressões Regulares  
4. Hierarquia de Chomsky  



## Objetivos de Aprendizagem

### Objetivo Geral
Desenvolver as habilidades necessárias para modelar, implementar e documentar sistemas computacionais utilizando conceitos fundamentais de linguagens formais e teoria da computação, com foco na resolução de problemas reais.

### Objetivos Específicos

1. Entender os fundamentos de Máquinas de Estados e sua relação com linguagens regulares e expressões regulares.  
2. Identificar e caracterizar problemas computacionais que podem ser modelados por autômatos finitos e outras máquinas reconhecedoras.  
3. Modelar o funcionamento de um sistema de vigilância com base em uma Máquina de Estados para simulação no JFLAP.  
4. Determinar e justificar a quantidade mínima de estados e transições necessárias para atender os requisitos especificados.  
5. Integrar e aplicar expressões regulares para representar comportamentos específicos da máquina de estados.  
6. Descrever detalhadamente o funcionamento do sistema modelado, incluindo as operações realizadas e exemplos concretos de uso.  
7. Investigar e documentar as relações entre linguagens regulares, autômatos e expressões regulares, incluindo exemplos aplicáveis ao módulo de vigilância.  
8. Propor soluções para sistemas baseados em autômatos, atendendo restrições de recursos computacionais.  
9. Registrar e compartilhar o progresso das atividades por meio de ferramentas como o quadro-branco PBL e o Diário de Bordo.  
10. Trabalhar em equipe para integrar diferentes conhecimentos e propor soluções criativas e fundamentadas.  
11. Elaborar relatórios técnicos no formato SBC, descrevendo de forma clara e detalhada a solução proposta.  
