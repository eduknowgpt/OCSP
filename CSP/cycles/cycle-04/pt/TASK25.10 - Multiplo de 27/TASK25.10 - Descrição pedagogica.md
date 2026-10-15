# TASK25.10 – Verificação de Múltiplo de 27

**Área:** Lógica de Programação / Programação Estruturada  
**Linguagem:** C  
**Nível:** Iniciação  



## 1. Problema


### 1.1 Descrição do Desafio Computacional  
A tarefa consiste em desenvolver um programa em linguagem C que solicite ao usuário a entrada de um número inteiro e positivo e, em seguida, verifique se o valor informado é múltiplo de 27. Ao final, o programa deve exibir uma mensagem indicando claramente se o número digitado é ou não múltiplo de 27.


## 2. Processo

Espera-se que o programa:

- Leia um número inteiro fornecido pelo usuário;
- Faça a validação básica de que o número é positivo (não negativo);
- Utilize uma operação adequada para verificar a múltiplicidade em relação a 27;
- Apresente uma saída textual compreensível para o usuário final.

### 2.1 Entregaveis 

Nesta tarefa, o estudante deve entregar:

### 2.1 - Código-fonte em C

- Arquivo com extensão .c, contendo:

  - Declaração da função main;

  - Declaração de variável(is) inteira(s) para armazenar o número informado;

  - Uso de printf/scanf (ou funções equivalentes) para interação com o usuário;

  - Operação de verificação de múltiplo utilizando o operador módulo (%);

  - Estrutura condicional (if / else) para decidir a mensagem de saída;

  - Comentários mínimos explicando as principais partes da solução (opcional, mas desejável).

### 2.2 - Demonstração de execução (implícita ou registrada)

  - O estudante deve ser capaz de executar o programa com diferentes entradas, em especial:

  - Um número múltiplo de 27 (por exemplo, 27, 54, 81);

  - Um número não múltiplo de 27;

  - (Opcional) Um número zero ou negativo, caso o professor deseje discutir validação de entrada.

Essa demonstração pode ocorrer ao vivo, em laboratório, ou por meio de prints de tela / registros de execução, dependendo do contexto da disciplina.

O conjunto de entregáveis permite observar se o estudante domina o ciclo básico de desenvolvimento de um programa simples: análise do problema, implementação em C, compilação, execução e interpretação do resultado.


## 3. Conhecimentos Relacionados

- K1. Tipos de Dados Inteiros e Variáveis em C
Conhecimento sobre declaração e uso de variáveis do tipo inteiro `(int)`, bem como compreensão de que o valor lido deve representar um número inteiro positivo.
Envolvimento na tarefa: declaração da variável que armazena o número informado pelo usuário.

- K2. Entrada e Saída Padrão (I/O)
Uso de funções como `printf` e `scanf` para exibir mensagens e ler dados do usuário.
Envolvimento na tarefa: solicitar o número inteiro positivo e exibir o resultado da verificação.

- K3. Operador Módulo (`%`) e Conceito de Múltiplo
Compreensão de que `a % b == 0` indica que `a` é múltiplo de `b`.
Envolvimento na tarefa: uso do operador módulo para verificar se o número informado é múltiplo de 27.

- K4. Estruturas Condicionais (if / else)
Capacidade de tomar decisões com base em expressões lógicas, executando blocos de código distintos dependendo do resultado da condição.
Envolvimento na tarefa: decidir qual mensagem imprimir (múltiplo ou não múltiplo de 27).

- K5. Validação Simples de Entrada (noção inicial)
Reconhecimento da importância de garantir que o número seja positivo, seja por meio de mensagem ao usuário ou, ao menos, pela compreensão conceitual.
Envolvimento na tarefa: discussão sobre o que fazer se o usuário digitar um valor negativo ou zero (mesmo que a implementação seja mínima).

- K6. Compilação e Execução de Programas em C
Conhecimento operacional sobre como compilar (por exemplo, usando `gcc`) e executar o programa em um ambiente de desenvolvimento (IDE, terminal, etc.).
Envolvimento na tarefa: transformar o código-fonte em um programa executável, testar e observar o comportamento.

## 4. Objetivos de Aprendizagem

- LO1. Declarar e utilizar variáveis inteiras em C para armazenar valores fornecidos pelo usuário em um programa simples.

- LO2. Implementar a leitura de dados via teclado utilizando funções de entrada e saída padrão em C (como `scanf` e `printf`).

- LO3. Aplicar o operador módulo (`%`) para verificar se um número inteiro é múltiplo de outro, interpretando corretamente o resultado da operação.

- LO4. Utilizar estruturas condicionais (`if` / `else`) para controlar o fluxo de execução do programa com base em uma condição lógica.

- LO5. Produzir uma saída textual clara e coerente, informando ao usuário se o número digitado é ou não múltiplo de 27.

- LO6. Executar e testar o programa com diferentes entradas, reconhecendo a importância de verificar correção para valores múltiplos e não múltiplos.



## 5. Contexto de Aquisição

Esta tarefa é adequada para disciplinas introdutórias de programação, como:

- “Introdução à Programação”;

- “Algoritmos e Lógica de Programação”;

- componentes curriculares equivalentes em cursos de Computação e áreas afins. 



## 6. Perfil do Público-Alvo

- Nível de ensino:

  - Estudantes do Ensino Médio técnico (eixo de Informática/Computação);

  - ou graduandos do primeiro semestre em cursos de Computação, Engenharia, Sistemas de Informação e áreas correlatas.

- Conhecimentos prévios desejáveis:

  - Noção básica de número inteiro e múltiplo (oriunda da Matemática escolar);

  - Familiaridade inicial com a sintaxe básica de C (estrutura de um programa, função main, ponto e vírgula, chaves);

  - Ter visto, ao menos de forma introdutória:

    - declaração de variáveis;

    - uso de scanf e printf;

    - estrutura condicional if.



## 7. Escala de proficiencia 

### 7.1 Nível 1 – Inicial

- Tem dificuldade para montar a estrutura mínima de um programa em C (erros frequentes de sintaxe, ausência de `main`, problemas com chaves ou ponto e vírgula).

- Não consegue ler corretamente o número digitado pelo usuário ou não consegue compilar o programa.

- Demonstra pouca compreensão sobre o que significa “múltiplo de 27” e não utiliza o operador módulo de forma adequada.

- Depende de ajuda constante do professor ou de colegas para pequenos ajustes.

### 7.2 Nível 2 – Básico

- Consegue estruturar um programa em C com `main`, declaração de variável inteira e uso de `scanf`/`printf`, ainda que com pequenos erros pontuais.

- Utiliza o operador módulo (`%`) para verificar múltiplo de 27, mas pode cometer equívocos na condição (por exemplo, usar `== 27` em vez de `== 0`).

- Implementa uma estrutura `if` simples, porém a mensagem de saída pode ser pouco clara ou incompleta.

- Consegue compilar e executar o programa, com algum apoio, mas ainda testa poucos casos e não explora entradas variadas.

### 7.3 Nível 3 – Proficiente

- Estrutura corretamente o programa em C, com declaração adequada de variável, entrada e saída de dados.

- Usa corretamente o operador módulo (`numero % 27 == 0`) para verificar se o número digitado é múltiplo de 27.

- Implementa uma estrutura condicional `if / else` coerente, exibindo mensagens claras para os casos “múltiplo” e “não múltiplo”.

- Testa o programa com diferentes valores (incluindo múltiplos e não múltiplos de 27) e consegue interpretar os resultados.

- Mostra autonomia na correção de erros simples de sintaxe ou lógica.

### 7.4 Nível 4 – Avançado

- Além de atender plenamente aos critérios do nível Proficiente, introduz melhorias na solução, como:

  - checagem se o número é positivo e mensagem específica em caso de valor inválido;

  - organização do código com comentários explicativos;

  - mensagens de saída mais amigáveis e bem formatadas.

- Usa a tarefa como oportunidade para discutir generalização (por exemplo, adaptar o programa para verificar múltiplos de outros números) ou modularização futura (como extrair a verificação para uma função).

- Testa deliberadamente casos de borda (por exemplo, zero, números negativos, números grandes) e consegue justificar o comportamento do programa.

- Demonstra domínio conceitual do que é ser múltiplo e da relação entre divisão inteira, resto e condição lógica no código.
