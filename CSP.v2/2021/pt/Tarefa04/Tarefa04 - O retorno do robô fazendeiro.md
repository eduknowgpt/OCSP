# Problema 4 (Tarefa): O retorno do Robô fazendeiro
 
 Autores: Luiz Gavaza &nbsp; Lais Salvador &nbsp; Roberta Oliveira &nbsp; Jessica Santana &nbsp; Otávio Neto
 
 Colaborador: Edeyson Gomes

 12 de Abril 2021
## Tarefa: O retorno do robô fazendeiro

### **1. Introdução**

A empresa Robô Fazendeiro ficou bastante satisfeita com a resolução proposta para o problema de sinalização para envio de alimentos e está animada com a implementação de uma nova funcionalidade: o robô, além de percorrer o rebanho e emitir o aviso de enviar alimentos, deve ser capaz de retornar ao ponto de partida e assim realizar outra tarefa. A empresa já possui kits de “sensores externos” que direcionam o caminho do robô aos rebanhos, o problema é como fazer o robô voltar ao ponto de partida. Como sabemos, já foi previamente acordado com o fazendeiro a quantidade mínima necessária de indivíduos do rebanho para emitir o aviso de enviar alimentos.

A equipe de estudantes da UFBA responsável pelo desenvolvimento do protótipo inicial, ao estudar este problema de navegação, percebeu que uma simples máquina de estados finitos não resolve o problema: como chegaram nessa conclusão é uma boa questão. Ao detalhar um pouco mais o estudo em relação ao problema do retorno ao ponto de partida, os alunos perceberam que, com o acoplamento de um dispositivo de memória auxiliar na máquina de estados, é possível modelar uma solução para apoio à navegação do robô fazendeiro.

Os alunos também perceberam que o módulo de Envio de Alimento do Problema do Robô Fazendeiro pode ser estendido com o módulo de navegação proposto neste novo problema ou os dois módulos podem ser soluções separadas que funcionam em paralelo, mas que podem se comunicar de alguma forma. A empresa também tem interesse em uma notação que especifique regras de geração de sequências de localização, para fins de documentação e aperfeiçoamento do módulo de navegação do robô.

A ferramenta sugerida para simular o processo do módulo de navegação do robô e a geração de sequências de localização  é o JFLAP1

### **2. Processo**
Durante o processo de construção da soluçã̃o será utilizada a metodologia de ensino e aprendizagem Problem Based Learning (PBL) que se caracteriza pela utilização de problemas do mundo real para estimular o desenvolvimento do pensamento crítico, do trabalho em equipe e de habilidades para a resolução de problemas, além de contribuir para a constru̧cão de conhecimentos acerca de um tema específico.

O processo deve ser documentado através do quadro-branco PBL que é composto pelas colunas QUESTÕES, FATOS, IDEIAS/HIPÓTESES e AÇÕES. Em cada reunião da equipe deve ser construída uma versão do quadro-branco e assim teremos a documentação dos passos para construção da solução. Além disso, será disponibilizado um documento compartilhado para o preenchimento do Diário de Bordo que deve conter as atas das reuniões com nomes dos participantes, pontos discutidos e desafios encontrados. A descrição desse processo fará parte da avaliaç̃ao do grupo. Nesse processo a participaç̃ao/contribuição de cada componente da equipe  é fundamental, assim cada estudante também será avaliado individualmente com base na observação dos tutores e no feedback dos colegas.

### **3. Produto**
Um integrante da equipe deverá postar no AVA UFBA até as 20:20 do dia 28/04/2021, no espaço apropriado para tal, um arquivo para o simulador JFLAP com módulo de navegação do robô, bem como, um relatório no modelo de artigos da SBC (Sociedade Brasileira de Computação) que descreva com o máximo de detalhes a idealização de funcionamento do módulo de navegaç̃ao do robô. O relatório deverá conter as operações executadas para funcionamento do sistema e, ao menos, 2 (dois) exemplos de funcionamento. Caso tenha sido desenvolvida uma notação baseada em regras, neste relatório também deve conter exemplos de geração de sequências de localização. Caso não tenha sido desenvolvida, apresentar no relatório as principais dificuldades.


### **4. Conhecimentos/Conceitos Envolvidos**
1. Autômato de pilha
2. Gramáticas livre de contexto
   
### **5. Objetivos de Aprendizagem** 

#### **5.1 Objetivo Geral**

Desenvolver um módulo de navegação para o robô fazendeiro, que permita o retorno ao ponto de partida após a emissão do aviso de enviar alimento.

#### **5.2 Objetivos Específicos**

1. Compreender as funcionalidades e desafios do problema de navegação do robô fazendeiro.
2. Investigar o uso de dispositivos de memória auxiliar em uma máquina de estados finitos para modelar uma solução para o problema de retorno ao ponto de partida.
3. Analisar a possibilidade de estender o módulo de envio de alimentos com o módulo de navegação proposto ou desenvolver soluções separadas que funcionem em paralelo e possam se comunicar.
4. Pesquisar e propor uma notação que especifique regras de geração de sequências de localização para documentação e aperfeiçoamento do módulo de navegação.
5. Utilizar a ferramenta JFLAP para simular o processo de navegação do robô e a geração de sequências de localização.

### </a> Referências 
RAMOS, M. V. M.; JOSE NETO, J.; VEGA, I. S. **Linguagens Formais: Teoria, Modelagem e Implementação**. Editora Bookman, 2009.

MENEZES, Paulo Blauth. **Linguagens formais e autômatos**. 6. ed. Bookman, 2011.

