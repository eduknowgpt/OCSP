### Tarefa: Programa para Explorar a Fórmula da Velocidade Média

	Tarefa adaptada da proposta do Prof. Margeylson Graça, do IFBA, Campus Valença

#### 1. Contexto Pedagógico

Você atua como professor(a) de Computação em uma escola de Ensino Médio.
O(a) professor(a) de Física da escola convidou você para desenvolver uma atividade interdisciplinar, em parceria, com o objetivo de **ajudar os estudantes a compreenderem o conceito de velocidade média**, focando no **raciocínio sobre a fórmula** e não nos cálculos manuais.

A ideia é criar um **programa interativo** que auxilie os alunos a explorar a relação entre **distância (Δs)**, **tempo (Δt)** e **velocidade média (Vₘ)**.

A fórmula de referência é: [ Vₘ = Δs / Δt ]

em que:

* **Vₘ** = velocidade média de um veículo em um percurso;
* **Δs** = deslocamento (distância total percorrida);
* **Δt** = intervalo de tempo gasto para percorrer essa distância.

---

#### 2. Objetivo da Tarefa

Desenvolver um programa que permita ao estudante **fornecer dois dos três valores** (Vₘ, Δs, Δt) e, a partir deles, o sistema deve **calcular automaticamente o terceiro valor**, reforçando:

* o entendimento da fórmula de velocidade média;
* a ideia de **rearranjo de fórmulas** (isolar uma variável);
* o uso de **condicionais** e **laços de repetição** na programação.

---

#### 3. Descrição do Problema

Você aceitou a parceria com a seguinte condição:

> *O programa deve permitir que o aluno informe apenas dois dos três valores (velocidade média, distância ou tempo), e o sistema deve calcular de forma correta o valor que ficou em branco.*

Exemplo:

* Se o aluno informar a **velocidade média** e o **tempo**, o programa deve calcular a **distância**.
* Se o aluno informar a **distância** e o **tempo**, o programa deve calcular a **velocidade média**.
* Se o aluno informar a **distância** e a **velocidade média**, o programa deve calcular o **tempo**.

---

#### 4. Requisitos da Atividade

**4.1. Estudo Conceitual**

Antes de implementar o programa, o(a) estudante deve:

1. **Estudar o cálculo de velocidade média**, interpretando o significado físico das grandezas envolvidas (Vₘ, Δs, Δt).
2. **Estudar o rearranjo da fórmula**, aprendendo a isolar:

   * Δs em função de Vₘ e Δt;
   * Δt em função de Δs e Vₘ;
   * Vₘ em função de Δs e Δt (forma original).

Esses rearranjos devem ser documentados (por escrito ou em comentários no código).

---

**4.2. Requisitos Funcionais do Programa**

O programa deve:

1. **Ler até três valores**, correspondentes a:

   * Velocidade média (Vₘ)
   * Distância (Δs)
   * Tempo (Δt)

2. **Permitir que exatamente um dos valores fique em branco** (ou seja, não seja informado diretamente pelo usuário).

   * Você deve definir e deixar claro no enunciado/código **como** o aluno sinaliza que um valor está “em branco” (por exemplo: digitando `0`, deixando uma entrada vazia, ou digitando um caractere especial).

3. **Identificar qual é o valor desconhecido** (o que ficou em branco) e **calcular o valor faltante** usando o rearranjo adequado da fórmula.

4. **Exibir o resultado** de forma clara, incluindo:

   * a grandeza calculada (Vₘ, Δs ou Δt);
   * o valor numérico calculado;
   * as unidades utilizadas (por exemplo: km/h, m/s, km, h, etc.) — podem ser assumidas unidades simples e fixas (ex.: km e h).

---

**4.3. Validação e Tratamento de Erros**

O programa deve utilizar **estruturas condicionais** para validar as entradas e proteger contra situações inválidas, tais como:

* Distância menor ou igual a zero (Δs ≤ 0);
* Tempo menor ou igual a zero (Δt ≤ 0);
* Velocidade média menor ou igual a zero (Vₘ ≤ 0);
* Caso o usuário informe:

  * menos de dois valores válidos, ou
  * todos os três valores (nenhum em branco),

o programa deve **exibir uma mensagem de erro ou orientação**, solicitando que o usuário informe exatamente **dois** valores válidos.

Você pode (opcionalmente) incluir mensagens educativas, explicando por que determinada combinação é inválida do ponto de vista físico (por exemplo, “tempo não pode ser zero”).

---

**4.4. Repetição da Tarefa**

O programa deve permitir que o aluno realize **vários experimentos** sem precisar ser executado novamente. Para isso:

1. Aplique um **laço de repetição** que:

   * leia os valores (ou a opção de saída);
   * execute as validações e o cálculo;
   * exiba o resultado;
   * volte a solicitar novos valores.

2. O laço deve ser encerrado quando o usuário digitar um valor especial em um dos campos (por exemplo, digitar `'f'` no primeiro valor para indicar **fim**).

   * Ao detectar essa condição, o programa deve exibir uma mensagem de despedida e encerrar a execução.

---

#### 5. Entregáveis Esperados

Para fins de avaliação (incluindo o CSP), o(a) estudante deve entregar:

1. **Código-fonte do programa**, com comentários explicando:

   * qual grandeza está sendo calculada;
   * como as fórmulas foram rearranjadas;
   * como são feitas as validações.

2. **Breve descrição textual** (pode ser em um arquivo `.md` ou comentário longo) contendo:

   * explicação da lógica usada para identificar o valor desconhecido;
   * os critérios de validação das entradas;
   * exemplos de uso (entrada → saída).

3. (Opcional, mas desejável) **Casos de teste** simples, com exemplos numéricos, mostrando:

   * entradas fornecidas (dois valores);
   * valor esperado para o terceiro;
   * comportamento do programa.

