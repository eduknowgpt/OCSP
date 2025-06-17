# Problema 5 (Tarefa): **O robô fazendeiro e o robô alimentador**
 
Autores: Luiz Gavaza &nbsp; Lais Salvador &nbsp; Roberta Oliveira &nbsp; Jessica Santana &nbsp; Otávio Neto

Colaborador: Edeyson Gomes

 05 de Maio 2021
## Tarefa: O robô fazendeiro e o robô alimentador

### **1.Introdução**
A empresa Robô Fazendeiro ficou bastante satisfeita com as soluções propostas para os problemas de sinalizaç̃ao para envio de alimentos e de retorno do robô ao ponto de partida. Agora o departamento de inovação está animado com a implementação de uma nova funcionalidade e de um novo robô: o robô fazendeiro, ao percorrer os rebanhos e emitir o aviso de enviar alimentos, deverá também comunicar o caminho que deverá ser seguido pelo robô alimentador para que este chegue até o rebanho com o suprimento adequado. Este novo robô, o alimentador, está em fase de protótipo, e a demanda inicial é a implementação do seu módulo de navegação.

Por outro lado, a equipe de estudantes da UFBA responsável pelo desenvolvimento dos módulos iniciais do robô fazendeiro, ao estudar as novas demandas, encontrou na literatura uma máquina abstrata com acesso sequencial de leitura e gravação a um dispositivo de memória ilimitada, que pode incorporar os módulos do robô fazendeiro como também o módulo de navegação do robô alimentador. Esse achado foi compartilhado com a equipe de inovação da empresa que propôs, então, evoluções nos módulos do robô fazendeiro. Por exemplo, ao revisar a solução proposta para o problema de sinalização para envio de alimentos, os estudantes perceberam que poderiam melhorar a solução ao permitir que o fazendeiro especifique as quantidades mínimas de indivíduos de cada rebanho como entradas para a máquina. Além disso, após algumas reuniões com a equipe de inovação, a fim de uniformizar documentação e treinamento da equipe de manutenção, decidiu-se que o mesmo modelo de máquina abstrata deve ser usado para implementar o módulo de navegação (com sua nova funcionalidade) do robô fazendeiro, como também o módulo de navegação do robô alimentador.

A ferramenta sugerida para simular o processo dos módulos dos robôs  é a JFLAP[^1].

[^1]: www.jflap.com

### **2. Processo**
Durante o processo de construção da solução será utilizada a metodologia de ensino e aprendizagem Problem Based Learning (PBL) que se caracteriza pela utilização de problemas do mundo real para estimular o desenvolvimento do pensamento crítico, do trabalho em equipe e de habilidades para a resolução de problemas, além de contribuir para a construção de conhecimentos acerca de um tema específico.

O processo deve ser documentado através do quadro-branco PBL que é composto pelas colunas QUESTÕES, FATOS,  IDEIAS/HIPÓTESES e AÇÕES. Em cada  reunião da equipe deve ser construída e compartilhada com os tutores uma versão do quadro-branco, evidenciando o processo evolutivo de construção da solução. Além disso, será disponibilizado um documento compartilhado por equipe, chamado Diário de Bordo, que deve conter: as atas das reuniões com nomes dos participantes, pontos discutidos e desafios encontrados. A descrição deste processo fará parte da avaliação do grupo. Em PBL a participa̧cao/contribuição ao de cada componente da equipe é fundamental, assim cada estudante também será avaliado individualmente com base na observação dos tutores e no feedback dos colegas.

### **3. Produto**
Um integrante da equipe deverá postar no AVA UFBA até as 20:20 do dia 24/05/2021, no espaço apropriado para tal, um arquivo para o simulador JFLAP com módulo de identificação, navegação do robô fazendeiro e o do robô alimentador, bem como, um relatório no modelo de artigos da SBC (Sociedade Brasileira de Computação) que descreva com o máximo de detalhes a idealização de funcionamento dos módulos desenvolvidos para os robôs. O relatório deveŕa conter as operações executadas para funcionamento do sistema e, ao menos, 2 (dois) exemplos detalhando o funcionamento de cada um dos módulos desenvolvidos. 

### **4. Conhecimentos/Conceitos Envolvidos**
1. Máquina de Turing
2. Variações de Máquina de Turing

### **5. Objetivos de Aprendizagem** 

#### **5.1 Objetivos Gerais**
Desenvolver módulos de identificação e navegação para o robô fazendeiro e o robô alimentador, utilizando conhecimentos em máquina de Turing.

**5.2 Objetivos Específicos**

1. Compreender as novas demandas e funcionalidades relacionadas ao robô fazendeiro e ao robô alimentador.
2. Investigar a máquina abstrata com acesso sequencial de leitura e gravação a um dispositivo de memória ilimitada e sua aplicação nos módulos dos robôs.
3. Revisar a solução proposta para o problema de sinalização para envio de alimentos, permitindo que o fazendeiro especifique as quantidades mínimas de indivíduos de cada rebanho como entradas para a máquina.

### </a> Referências 
RAMOS, M. V. M.; JOSE NETO, J.; VEGA, I. S. **Linguagens Formais: Teoria, Modelagem e Implementação**. Editora Bookman, 2009.

MENEZES, Paulo Blauth. **Linguagens formais e autômatos**. 6. ed. Bookman, 2011.