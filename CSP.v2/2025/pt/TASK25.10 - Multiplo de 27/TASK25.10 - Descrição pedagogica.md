# TASK25.10 – Verificação de Múltiplo de 27

**Área:** Lógica de Programação / Programação Estruturada  
**Linguagem:** C  
**Nível:** Iniciação  



## 1. Problema


### 1.1 Descrição do Desafio Computacional  
O estudante deve elaborar um programa em linguagem C que:

- Solicite ao usuário a digitação de um número inteiro positivo;  
- Verifique se o valor informado é múltiplo de 27;  
- Informe ao usuário, por meio de mensagem apropriada, se o número é ou não múltiplo de 27;  
- Inclua verificação para garantir que o número seja positivo; opcionalmente, trate entradas inválidas.  

Este problema demanda da aluna ou do aluno a utilização de operações aritméticas (módulo), estruturas de decisão (`if/else`) e controle de fluxo de leitura e validação — aspectos centrais no aprendizado inicial de programação.  

### 1.2 Produto Final Esperado  
- Um **programa em C**, com código fonte claro e comentado, que:  
  - Leia um valor inteiro positivo por meio de entrada padrão;  
  - Aplique a operação `n % 27`;  
  - Compare o resultado com zero para determinar múltiplo;  
  - Exiba mensagem de saída adequada (“É múltiplo de 27” ou “Não é múltiplo de 27”);  
  - Implemente checagem da positividade da entrada (ou tratamento de erro ou repetição de leitura).  



## 2. Processo

1. **Compreensão do enunciado** — identificação dos requisitos: entrada positiva, múltiplo de 27, mensagens adequadas.  
2. **Pseudocódigo ou esboço lógico** — antes de codificar: definir variáveis, leitura, verificação, saída.  
3. **Implementação em C** — declaração de variáveis, leitura com `scanf`, verificação de positividade, cálculo de módulo, estrutura condicional, mensagens ao usuário.  
4. **Testes** — com valores múltiplos e não múltiplos de 27; valores negativos ou zero; valores maiores.  
5. **Tratamento de erros / validações adicionais** — opcionalmente: repetição de leitura em caso de entrada inválida.  
6. **Documentação / comentários** — clareza no código; explicação de decisões; boas práticas.  

### 2.1 Evidências de Realização  
- Código-fonte (.c) com comentários e boa indentação;  
- Registro de execução — captura de tela, gravação ou demonstração;  
- Registro de testes com diversos casos;  
- (Opcional) Relatório ou documentação breve — explicando a lógica, escolhas e testes;  
- (Opcional) Defesa oral ou explicação ao professor/classe sobre o funcionamento do programa.  



### 2.2. Critérios de Avaliação

A avaliação considera três dimensões principais:

### Critério Técnico  
- Correção do código: compila e executa sem erros;  
- Funcionalidade conforme especificação: leitura de inteiro positivo, verificação correta de múltiplo, mensagens adequadas;  
- Tratamento de entradas inválidas ou não conformes (quando requerido);  
- Qualidade do código: indentação, clareza, comentários, convenções mínimas.  

### Critério Cognitivo  
- Demonstração de compreensão da lógica de múltiplo e do operador módulo;  
- Capacidade de justificar decisões de implementação (por que validação de positividade, por que usar `%`, fluxo lógico);  
- Clareza na explicação da estrutura do programa (fluxo de dados, condições, saídas).  

### Critério Atitudinal / Procedimental  
- Cumprimento dos prazos;  
- Autonomia e organização no desenvolvimento;  
- Responsabilidade e honestidade intelectual (autorias, colaborações justas);  
- Esforço por testar e depurar o programa;  
- Atenção a detalhes de sintaxe e boas práticas.  



## 3. Contexto de Aquisição

A tarefa apoia a formação inicial em programação ao desenvolver habilidades fundamentais como:

- Execução mental de algoritmos simples, compreendendo entradas, verificações e saídas.
- Entendimento do fluxo sequencial do programa, prevenindo erros lógicos futuros.
- Interpretação de expressões condicionais, essencial para debugging e leitura de código.

Pode ser aplicada como atividade individual em sala, exercício avaliativo ou tarefa para casa.

## 4. Perfil do Público-Alvo

- **Nível educacional:** aluno de 1 semestre em curso superior na área de computação;  
- **Pré-requisitos esperados:** noções básicas de representações de dados, variáveis, operadores aritméticos, lógica de programação;  
- **Experiência com programação:** mínima / iniciante, ideal para primeira ou segunda tarefa prática;  
- **Disposições desejáveis:** paciência para testes e depuração; atenção aos detalhes; interesse em lógica e algoritmos; responsabilidade acadêmica; curiosidade para entender o funcionamento interno.  



## 5. Escala de Proficiência

Adota-se escala qualitativa com **níveis: Básico – Proficiente – Avançado**.

- **Básico:** Programa compila e executa para casos simples; pode faltar tratamento de entrada inválida ou falhas em casos extremos; explicação mínima e superficial da lógica.  
- **Proficiente:** Programa atende todos os requisitos: leitura, verificação, mensagens corretas; código claro e documentado; testes razoáveis; explicação coerente da lógica e decisões.  
- **Avançado:** Além dos requisitos, implementa tratamento robusto de entradas (validação, repetição), cobre casos extremos, código bem estruturado e comentado; demonstra compreensão conceitual profunda; justifica escolhas e demonstra clareza algorítmica e rigor.  

Essa escala pode ser desdobrada com pontuação (ex: 0 – 10) em cada eixo (Técnico, Cognitivo, Atitudinal), conforme critério do professor.  



## 6. Resultados Esperados (Aprendizagens / Competências)

- Código C funcional e robusto, satisfazendo a especificação;  
- Compreensão do uso de operador módulo para verificação de múltiplos;  
- Capacidade de estruturar fluxos simples de programa (entrada → processamento → saída);  
- Habilidade para validar entrada de dados e tratar casos não triviais;  
- Desenvolvimento de boas práticas de programação (legibilidade, documentação, clareza).  
- Competências metacognitivas: pensar logicamente, testar, depurar, justificar decisões de design.  



## 7. Observações e Possíveis Variações  

- A tarefa pode ser estendida: permitir que o usuário informe um divisor arbitrário (não apenas 27) e verificar múltiplos;  
- Pode-se exigir tratamento de entrada não numérica como desafio adicional;  
- Em contexto de sala sem computador, realizar a lógica em pseudocódigo ou fluxograma;  
- Incentivar reflexões sobre robustez, limites de tipo `int`, casos de overflow ou entradas muito grandes.  
