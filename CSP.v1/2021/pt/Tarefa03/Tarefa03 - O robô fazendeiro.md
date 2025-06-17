# Problema 3 (Tarefa): **Robô Fazendeiro**
 
Autores: Luiz Gavaza &nbsp; Lais Salvador &nbsp;  Roberta Oliveira  &nbsp; Daniel Cason
 
Colaboradores: Edeyson Gomes &nbsp;  Jéssica Santana

19 de Outubro 2020
## **Tarefa: O robô fazendeiro**

### **1. Introdução**
A empresa Robô Fazendeiro está desenvolvendo um protótipo de robô para realizar a identificação de rebanhos em fazendas pecuaristas, onde estes animais vivem soltos (pecuária extensiva). Este robô foi concebido com um módulo de visualização bastante avançado que consegue classificar se um animal é bovino, caprino ou suíno. Para melhorar a gestão da fazenda, como por exemplo, selecionar os alimentos que devem ser enviados para cada rebanho, faz-se necessário identificar quais rebanhos estão presentes nos lotes. Com o objetivo de economizar com viagens de transportes da alimentação, o robô deve enviar mensagens com solicitação de alimentação quando identificar uma quantidade mínima de indivíduos de um dado rebanho. Essas quantidades mínimas são definidas com o dono da fazenda. Entretanto, a empresa Robô Fazendeiro ainda não desenvolveu o módulo responsável por realizar a identificação mencionada. 

Um dos técnicos da empresa Robô Fazendeiro, que coincidentemente é estudante de um dos cursos de Computação da UFBA, trouxe o problema para que seus colegas de turma pudessem, em equipe, trabalhar para apresentar o protótipo do módulo de identificação do robô. Por questões econômicas, a empresa Robô Fazendeiro está em busca de uma solução menos custosa possível nesse primeiro protótipo.

Nas pesquisas iniciais os estudantes perceberam que uma simples máquina de estados finitos é capaz de resolver este problema. Como eles chegaram a essa conclusão é uma boa questão. Outro achado na pesquisa foi a descoberta de uma expressão matemática muito usada em protocolos, de fácil compreensão, que pode ser parte da documentação da solução. Essa expressão pode ser construída a partir do momento em que a solução for implementada com uma máquina de estados finitos. Os estudantes comentaram sobre essa possibilidade numa reunião e a empresa se interessou em saber mais sobre este detalhamento. 

A empresa também tem interesse em averiguar se existe alguma regra que permita determinar a quantidade mínima de estados e de transições a partir das quantidades mínimas de cada rebanho que se deseja identificar, assim, será possível realizar orçamentos mais assertivos.

A ferramenta sugerida para simular o processo do módulo de identificação do robô é o JFLAP.

### **2. Processo** 

Durante o processo de construção da solução será utilizada a metodologia de ensino e aprendizagem Problem Based Learning (PBL) que se caracteriza pela utilização de problemas do mundo real para estimular o desenvolvimento do pensamento crítico, do trabalho em equipe e de habilidades para a resolução de problemas, além de contribuir para a construção de conhecimentos acerca de um tema específico. O processo deve ser documentado através do quadro-branco PBL que é composto pelas colunas QUESTÕES, FATOS, IDEIAS/HIPÓTESES e AÇÕES. Em cada reunião da equipe deve ser construída uma versão do quadro-branco e assim teremos a documentação dos passos para construção da solução. A descrição desse processo fará parte da avaliação do grupo. Além disso, será disponibilizado um documento compartilhado para o preenchimento do Diário de Bordo, conforme demonstrado em um encontro síncrono.

### **3. Produto** 

Um integrante da equipe deverá postar no AVA UFBA até as 20:20 do dia 31/03/2021, no espaço apropriado para tal, um arquivo para o simulador JFLAP com módulo de identificação do robô, bem como, um relatório no modelo de artigos da SBC (Sociedade Brasileira de Computação) que descreva com o máximo de detalhes a idealização de funcionamento do módulo de identificação do robô. O relatório deverá conter as operações executadas para funcionamento do sistema e, ao menos, 2 (dois) exemplos de funcionamento. Lembrando que esse relatório também deve contemplar os interesses/questionamentos da empresa com relação à documentação e orçamentos.

### **4. Conhecimentos/Conceitos Envolvidos** 

1. Máquina de estados  (Finite state machines)
2. Linguagens Regulares (Regular languages)
&nbsp; Formal languages and automata theory
3. Expressões Regulares 

### **5. Objetivos de Aprendizagem** 

#### **5.1 Objetivo Geral** 

Desenvolver um módulo de identificação de rebanhos para um protótipo de robô fazendeiro, utilizando conhecimentos em máquinas de estados finitos e expressões regulares.

#### **5.2 Objetivos Específicos** 
1. Identificar as funcionalidades do módulo de identificação do robô fazendeiro.
2. Aplicar o conceito de máquinas de estados finitos para resolver o problema de identificação dos rebanhos.
3. Pesquisar e utilizar expressões regulares como parte da documentação e solução do problema.
4. Investigar a relação entre as quantidades mínimas de rebanhos a serem identificados e a quantidade mínima de estados e transições necessárias na máquina de estados finitos.
5. Utilizar a ferramenta JFLAP para simular o processo de identificação do robô.
6. Elaborar um relatório detalhado, no modelo de artigos da SBC, descrevendo o funcionamento do módulo de identificação do robô, incluindo as operações executadas e exemplos de funcionamento.



### </a> Referências 
RAMOS, M. V. M.; JOSE NETO, J.; VEGA, I. S. **Linguagens Formais: Teoria, Modelagem e Implementação**. Editora Bookman, 2009.

MENEZES, Paulo Blauth. **Linguagens formais e autômatos**. 6. ed. Bookman, 2011.
