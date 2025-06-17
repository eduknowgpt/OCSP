
# Relatório de Especificação de Competências: Tarefa05 - O Robô Fazendeiro e o Robô Alimentador

## Introdução

Este relatório aplica o **Processo de Especificação de Competências (PEC)** ao cenário de Aprendizagem Baseada em Problemas (ABP) intitulado **"O Robô Fazendeiro e o Robô Alimentador"**, que expande desafios anteriores ao integrar novas funcionalidades e um segundo agente robótico. Neste cenário, os estudantes devem projetar soluções computacionais utilizando **Máquinas de Turing** para modelar o comportamento tanto do Robô Fazendeiro quanto do novo Robô Alimentador.

O desafio central é garantir que, durante a travessia do rebanho e o sinal de entrega de alimento, o Robô Fazendeiro também comunique o caminho que o Robô Alimentador deve seguir. Além disso, uma máquina abstrata unificada — capaz de operações sequenciais de leitura e escrita sobre uma memória ilimitada — deve ser empregada para implementar os módulos de navegação de ambos os robôs. Essa decisão visa apoiar a padronização da documentação do sistema e simplificar o treinamento para manutenção.

Por meio da metodologia PEC, as competências são extraídas e estruturadas a partir da descrição da tarefa, dos domínios de conhecimento relevantes, dos objetivos de aprendizagem e das disposições comportamentais. O resultado é uma estrutura organizada para o aprendizado baseado em competências que integra modelagem computacional, aplicação de ferramentas e resolução colaborativa de problemas em cenários inspirados no mundo real.

## 1. Análise da Descrição da Tarefa

A tarefa *Robô Fazendeiro e Robô Alimentador* aborda os esforços contínuos de inovação da empresa Robô Fazendeiro. Após o sucesso na implantação dos módulos anteriores de sinalização e navegação, a empresa pretende introduzir um novo robô, o **Robô Alimentador**, que trabalhará em coordenação com o **Robô Fazendeiro** para entregar suprimentos ao rebanho de forma eficiente.

O objetivo principal é integrar a lógica de identificação e navegação de ambos os robôs utilizando um modelo computacional unificado — uma **Máquina de Turing** com acesso sequencial de leitura/escrita a uma memória ilimitada. O Robô Fazendeiro deve não apenas alertar a localização do rebanho, mas também codificar e transmitir o caminho que o Robô Alimentador deverá seguir. Adicionalmente, o módulo anterior de sinalização do Robô Fazendeiro deve ser revisado para permitir a entrada de um limiar mínimo para a contagem de membros do rebanho.

Os entregáveis esperados são:

* Um **arquivo JFLAP** implementando os módulos de navegação de ambos os robôs utilizando o modelo de máquina abstrata compartilhado.
* Um **relatório técnico** seguindo o formato de artigo da SBC, documentando a lógica, decisões de projeto e execução dos módulos desenvolvidos, com exemplos.

Esta tarefa requer que os estudantes:

* Compreendam a interação e coordenação entre múltiplos módulos robóticos.
* Reavaliem e aprimorem soluções computacionais existentes.
* Investiguem modelos computacionais abstratos e os apliquem em novos cenários de projeto.
* Utilizem o **JFLAP** para simular e validar o comportamento do sistema.
* Colaborem de forma eficaz e mantenham documentação estruturada por meio de ferramentas ABP como o Quadro Branco e o Diário de Bordo.

## 2. Enumeração dos Conhecimentos

A execução bem-sucedida desta tarefa exige mobilização de conhecimentos tanto da computação teórica quanto de habilidades profissionais. Os domínios do conhecimento são categorizados de acordo com o **Sistema de Classificação da Computação da ACM (2012)** e as diretrizes do **ACM/IEEE CC2020**.

### Conhecimentos em Computação

* **Máquinas de Turing**  
  Essenciais para modelar os módulos do Robô Fazendeiro e do Robô Alimentador, as Máquinas de Turing fornecem uma base universal para representar lógica envolvendo memória, fluxo de controle e tomada de decisões.

* **Máquina de Turing (Variações)**  
  Conhecimento sobre variações, como Máquinas de Turing multitarefa ou não-determinísticas, pode ser necessário para otimizar a coordenação entre os dois robôs ou melhorar a eficiência na lógica de navegação.

* **Tese de Church-Turing**  
  Fornece a base teórica da tarefa, reforçando a equivalência entre raciocínio algorítmico e funções computáveis por Turing. Espera-se que os alunos fundamentem suas soluções neste conceito.

* **Engenharia de Requisitos**  
  Permite a identificação, análise e formalização das necessidades do usuário (por exemplo, a exigência da DERBA de classificação de tráfego noturno) em requisitos computacionais que orientem o projeto do sistema.

* **Modelagem e Simulação**  
  Necessários para representar formalmente os comportamentos dos robôs e testá-los em ambientes de simulação como o JFLAP.

### Conhecimentos Profissionais (FPK)

* **Pensamento Analítico e Crítico**  
  Apoia a análise das dependências funcionais entre os robôs, a exploração das capacidades das máquinas abstratas e a avaliação de alternativas de projeto.

* **Resolução de Problemas e Projeto de Soluções**  
  Fundamental para adaptar a lógica existente, resolver limitações nos módulos atuais e propor estratégias integradas de navegação multiagente.

* **Comunicação Escrita**  
  Os estudantes devem produzir um relatório técnico estruturado que documente os módulos desenvolvidos, justifique decisões de projeto e comunique os resultados de forma clara para públicos técnicos e não técnicos.

## 3. Identificação dos Objetivos de Aprendizagem

### Objetivo Geral

Aplicar conhecimentos sobre Máquinas de Turing para desenvolver e integrar os módulos de identificação e navegação do Robô Fazendeiro e do Robô Alimentador.

### Objetivos Específicos

1. **Compreender** as funcionalidades e novas demandas relacionadas aos dois robôs.
2. **Investigar** o modelo de máquina abstrata capaz de leitura e escrita sequencial em dispositivo de memória ilimitado e aplicá-lo à navegação robótica.
3. **Revisar** a solução de sinalização de entrega de alimentos, incorporando a especificação do tamanho mínimo do rebanho como entrada.
4. **Desenvolver** sistemas de navegação modulares e reutilizáveis para ambos os robôs usando um modelo computacional unificado.
5. **Simular** o comportamento dos robôs utilizando a ferramenta JFLAP para validar os módulos.

Esses objetivos garantem que os estudantes combinem conhecimento teórico e aplicado, reforcem o raciocínio algorítmico e utilizem ferramentas de simulação para prototipar sistemas robóticos funcionais alinhados a modelos formais de computação.

## 4. Especificação de Competências

Para apoiar os objetivos de aprendizagem da Tarefa 05, o **conjunto de competências definido para**
