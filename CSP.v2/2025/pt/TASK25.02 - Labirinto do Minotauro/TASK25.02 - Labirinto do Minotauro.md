# Problema 25.02 : Labirinto do Minotauro

**Autores:** Laís Salvador  
**Colaboradores:** Edeyson Gomes e Marcos Bião  
**Data:** 15 de outubro de 2025  



## 1. Problema

![Labirinto do Minotauro](Labirinto.png)

Na antiga ilha de Creta, o rei Minos ordenou a construção de um labirinto tão intricado que até os ventos se perdiam em seus corredores. Dizia-se que ninguém — nem homem, nem deus — seria capaz de encontrar a saída depois de entrar. Nas sombras desse emaranhado de túneis habitava o temido **Minotauro**, criatura de corpo humano e cabeça de touro, guardião do mistério e do medo.

Mas a história, como todo bom mito, ganhou um novo herói: **Teseu**, que, guiado pelo engenho de **Ariadne**, levou consigo apenas um fio, uma espada e muita coragem. À medida que avançava, desenrolava o fio, deixando para trás o rastro de sua jornada — uma espécie de mapa invisível capaz de conduzi-lo de volta, caso sobrevivesse ao monstro.

Hoje, milênios depois, a **Fundação Ariadne** deseja recontar essa lenda em um novo formato: um **jogo educativo digital**, onde cada jogador se torna um Teseu moderno. O desafio é reconstruir o labirinto e criar uma forma de navegação que permita ao herói não apenas encontrar o Minotauro, mas também **retornar à entrada com segurança**.

No entanto, o módulo de navegação do jogo apresenta uma limitação: o personagem consegue chegar ao Minotauro, mas **não sabe retornar**. A equipe de desenvolvimento precisa modelar uma solução formal que permita que Teseu “lembre” o caminho percorrido e encontre a saída.

Vocês foram contratados como **equipe de engenheiros de linguagens formais** para investigar como representar computacionalmente essa navegação, respeitando as restrições da teoria de linguagens formais e de autômatos, com apoio do simulador **JFLAP**.

Além disso, a Fundação Ariadne tem interesse em uma **notação formal** que especifique regras de geração de sequências de localização, para fins de documentação e aperfeiçoamento do módulo de navegação de Teseu e de outros personagens a serem incluídos futuramente no jogo.

> **O enigma está lançado:** como transformar o fio de Ariadne em método formal?



## 2. Desafios

- Quais limitações um **autômato finito** apresenta ao tentar representar a memória do caminho percorrido?
- Que tipo de **dispositivo de memória auxiliar** poderia permitir que Teseu “lembrasse” os movimentos feitos?
- Como documentar o caminho de Teseu em uma **notação formal** de regras de localização?
- Que adaptações seriam necessárias se o labirinto tivesse **múltiplas saídas** ou **obstáculos dinâmicos**?



## 3. Etapas de Desenvolvimento

1. **Compreensão do problema:** discutir o desafio e identificar o que já se sabe e o que precisa ser aprendido.  
2. **Pesquisa e aprendizado autônomo:** investigar conceitos de autômatos, pilhas, gramáticas e modelagem formal.  
3. **Prototipagem e simulação:** usar o **JFLAP** para criar modelos candidatos e testar hipóteses.  
4. **Análise de falhas e refinamento:** justificar escolhas e avaliar limitações de cada abordagem.  
5. **Documentação científica:** redigir um artigo técnico no formato **SBC**, descrevendo o processo investigativo, resultados e contribuições.



## 4. Produto

Um integrante da equipe deverá enviar no **moodle.ufba.br**, até **23:59 do dia 03/11/2025**, os seguintes itens:

- Um **arquivo JFLAP** contendo o módulo de navegação do personagem Teseu, representando formalmente o processo de **ida e retorno** no labirinto.
- Um **relatório técnico** no formato da **Sociedade Brasileira de Computação (SBC)**, contendo:
  - descrição detalhada do funcionamento do módulo;
  - operações executadas para navegação;
  - ao menos **dois exemplos de simulação**;
  - geração de sequências de localização através de **notações formais**;
  - reflexões sobre desafios de investigação, limitações, principais dificuldades e soluções propostas.



## 5. Conhecimentos / Conceitos Envolvidos

- Autômato de Pilha  
- Gramáticas Livres de Contexto  
- Teoria dos Autômatos  
- Modelagem Formal com JFLAP  



## 6. Objetivos de Aprendizagem

### Objetivo Geral

Desenvolver um **módulo de navegação formal** para o personagem Teseu, capaz de representar computacionalmente o retorno ao ponto de partida, aplicando conceitos de **Linguagens Formais e Autômatos**.

### Objetivos Específicos

- Compreender os desafios do problema de navegação no contexto do **labirinto do Minotauro**.  
- Investigar o uso de **dispositivos de memória auxiliar** em máquinas de estados finitos.  
- Propor uma **notação formal** que especifique regras de geração de sequências de localização para documentação e melhoria do sistema.  
- Utilizar o **JFLAP** para simular o processo de navegação e validar a modelagem.



## Referências

RAMOS, M. V. M.; JOSE NETO, J.; VEGA, I. S.  
*Linguagens Formais: Teoria, Modelagem e Implementação.* Editora Bookman, 2009.

MENEZES, Paulo Blauth.  
*Linguagens formais e autômatos.* 6. ed. Bookman, 2011.
