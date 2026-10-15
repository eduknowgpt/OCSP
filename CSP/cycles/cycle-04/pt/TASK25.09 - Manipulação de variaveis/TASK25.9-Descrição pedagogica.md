# TASK25.9 – Manipulação de Variáveis  
> Criador: Prof. MS. Marcos Bião, Univasf – Campus Salgueiro

## 1. Problema

A tarefa apresenta um trecho de código em linguagem C que realiza leitura, atribuição e atualização de variáveis numéricas, seguido de uma questão de múltipla escolha sobre o resultado final das variáveis após a execução do algoritmo. O estudante recebe o código abaixo:

```c
int main(){
    float a,b,c,d;
    scanf("%d%d%d%d",&a,&b,&c,&d);
    a = b;
    b = c;
    c = d;
    d = a;
    b = a + b/2;
    c = c+b;
    d = d + (b*2) - a;
}
```

Supondo que os valores inicialmente fornecidos para as variáveis A, B, C e D sejam, respectivamente, 10, 15, 20 e 25, o estudante deve determinar quais serão os valores finais de a, b, c e d após a execução completa do algoritmo, escolhendo a alternativa correta dentre:

(a) 15 – 17,5 – 42,5 – 35

(b) 15 – 17,5 – 42,5 – 50

(c) 15 – 25 – 50 – 45

(d) 15 – 25 – 50 – 50

(e) 15 – 30 – 55 – 60

O foco desta tarefa não está apenas em “acertar a alternativa”, mas em compreender com precisão o fluxo de execução, a ordem das atribuições, a atualização sucessiva de valores nas variáveis e as consequências de possíveis inconsistências entre tipos de dados e especificadores de formato na leitura (por exemplo, uso de `%d` com variáveis declaradas como `float`). Do ponto de vista pedagógico, trata-se de um exercício que busca desenvolver a habilidade de rastrear estados de variáveis, depurar raciocínios equivocados e interpretar o comportamento de um programa linha a linha.


## 2. Processo

Espera-se que o programa:

- Leia quatro valores numéricos fornecidos pelo usuário, associados às variáveis `a`, `b`, `c` e `d`.

- Armazene esses valores nas variáveis, considerando a interação entre tipo declarado (`float`) e especificador de leitura (`%d`).

- Execute, em ordem, uma sequência de atribuições que “propaga” o valor de uma variável para outra (`a = b; b = c; c = d; d = a`;).

- Realize operações aritméticas adicionais sobre as variáveis, envolvendo soma, divisão e multiplicação (`b = a + b/2; c = c + b; d = d + (b*2) - a`;).

- Atualize o valor de cada variável, de modo que o estudante possa rastrear o estado final de `a`, `b`, `c` e `d` após todas as instruções.

- Permita que o estudante, por meio de simulação manual ou mental, determine a alternativa correta na questão de múltipla escolha, identificando o resultado numérico correspondente.

Do ponto de vista do processo computacional, a tarefa exige que o estudante acompanhe a execução sequencial do programa, identifique dependências entre variáveis (por exemplo, quando um valor é sobrescrito e deixa de ser acessível), compreenda a diferença entre valor inicial e valor atualizado, e reconheça como operações aritméticas encadeadas impactam o estado final do programa.

### 2.1. Entregaveis

Para fins pedagógicos, os entregáveis associados a essa tarefa podem ser organizados da seguinte forma:

- Resolução da questão de múltipla escolha (alternativa marcada):
O estudante deve indicar explicitamente qual alternativa considera correta (a, b, c, d ou e). Esse entregável permite avaliar, de forma objetiva, se o estudante foi capaz de acompanhar corretamente o fluxo de execução e chegar ao resultado numérico esperado.

- Rastreamento passo a passo das variáveis (tabela ou descrição textual):
Recomenda-se solicitar que o estudante produza uma tabela ou descrição organizada contendo os valores de a, b, c e d após cada linha relevante de código. Por exemplo, após a leitura inicial, após cada atribuição simples e após cada operação aritmética.
Esse artefato torna explícito o raciocínio subjacente, permitindo ao professor verificar se eventuais erros decorrem de:

   - má compreensão da ordem de execução;

   - confusão na propagação de valores entre variáveis;

   - dificuldade com operações aritméticas ou com o uso de divisão e multiplicação;

   - desatenção ao fato de que as variáveis têm seus valores atualizados e não “mantêm” versões antigas.

- Comentário breve sobre o uso de tipos e especificadores de formato (opcional):
Pode-se solicitar um comentário curto sobre a combinação de float com %d em scanf. Ainda que, em muitos ambientes, o programa possa se comportar de forma aparentemente “aceitável” nos exemplos simples, essa discussão introduz noções de boas práticas de programação e de atenção à tipagem correta e à interface com o sistema de entrada.

Esses entregáveis, em conjunto, fornecem evidências mais ricas sobre o desenvolvimento de competências de rastreamento de código, interpretação de algoritmos e raciocínio sobre estados de variáveis.


## 3. Conhecimentos Relacionados

**K1. Tipos de dados numéricos e especificadores de formato**
[Compreensão de como variáveis float são declaradas e de como devem ser corretamente lidas usando funções de entrada como scanf, incluindo a relação entre tipo da variável e especificador (%f, %d etc.). A tarefa evidencia potenciais problemas de inconsistência entre tipo declarado e formato de leitura.]

**K2. Entrada de dados em linguagem C**
[Entendimento do uso de scanf para leitura de múltiplos valores, da ordem de leitura e da associação entre argumentos da função e variáveis do programa. O estudante precisa interpretar corretamente como os valores inicializados (10, 15, 20, 25) são associados às variáveis a, b, c e d.]

**K3. Atribuições e atualização de variáveis**
[Domínio da semântica de atribuição em C: o valor à direita do operador = é avaliado e, em seguida, armazenado na variável à esquerda. A tarefa explora o fato de que valores anteriores podem ser sobrescritos e não são mais acessíveis, exigindo rastreamento cuidadoso do estado.]

**K4. Operações aritméticas básicas e precedência de operadores**
[Capacidade de interpretar expressões como a + b/2, c + b e d + (b*2) - a, respeitando a precedência de operadores, a ordem de avaliação e o uso de parênteses. Envolve compreensão de divisão, multiplicação, soma e subtração em contexto de programação.]

**K5. Fluxo de execução sequencial**
[Compreensão de que, na ausência de estruturas de controle explícitas (como condicionais ou laços), as instruções são executadas linha a linha, na ordem em que aparecem. O estudante precisa acompanhar esse fluxo para determinar os valores finais das variáveis.]

**K6. Rastreio (tracing) e simulação de código**
[Habilidade de simular a execução do programa manualmente, registrando e atualizando o valor das variáveis a cada passo. Este conhecimento é central para a tarefa, pois o estudante não está, necessariamente, executando o código em um computador, mas raciocinando sobre ele.]

**K7. Leitura e interpretação de código legado ou dado pelo professor**
[Competência em compreender um trecho de código fornecido, ainda que apresente pequenos problemas de estilo ou de tipagem, e em extrair seu comportamento funcional, sem precisar reescrevê-lo integralmente.]

## 4. Objetivos de aprendizagem

**LO1**. Identificar e rastrear, passo a passo, os valores assumidos pelas variáveis a, b, c e d ao longo da execução sequencial do programa.

**LO2**. Interpretar corretamente instruções de atribuição e operações aritméticas em linguagem C, explicando como a precedência de operadores influencia o resultado final das expressões.

**LO3**. Simular manualmente a execução de um trecho de código em C, produzindo uma tabela ou registro organizado do estado das variáveis após cada instrução relevante.

**LO4**. Analisar criticamente o uso de tipos de dados e especificadores de formato na leitura de valores com scanf, reconhecendo possíveis inconsistências e seus impactos na clareza e na robustez do código.

**LO5**. Resolver uma questão de múltipla escolha sobre o resultado de um algoritmo, justificando a alternativa escolhida com base em um raciocínio sistemático sobre o fluxo de execução e a atualização de variáveis.

## 5. Contexto de aquisição

Esta tarefa é adequada a disciplinas introdutórias de programação, tais como Introdução à Programação, Algoritmos e Estruturas de Dados I ou componentes curriculares de Pensamento Computacional com foco em linguagens imperativas (como C).

O momento mais apropriado no curso é inicial ou intermediário, após os estudantes terem sido apresentados a:

- conceitos básicos de variáveis e tipos numéricos;

- sintaxe fundamental de C;

- operações aritméticas e precedência de operadores;

- uso elementar de scanf e printf.

## 6. Perfil do público alvo

O público-alvo típico são estudantes de:

- Ensino Superior em cursos de Computação, Engenharia ou áreas afins (semestre inicial); ou

- Ensino Médio Técnico em Informática/Computação, em componentes de programação introdutória.

Conhecimentos prévios desejáveis:

- noções básicas de algoritmos e de representação de variáveis;

- compreensão elementar de operações aritméticas e precedência (do ponto de vista matemático);

- familiaridade inicial com a sintaxe de C (declaração de variáveis, uso de main, funções de entrada/saída).

## 7. Escala de Proficiência
### 7.1 Nível Inicial – Reconhecimento Pontual e Erros Sistemáticos

O estudante nesse nível consegue identificar, de forma fragmentada, partes do código (por exemplo, reconhece que há atribuições e operações aritméticas), mas apresenta grande dificuldade em acompanhar a sequência de atualizações das variáveis.

- Frequentemente, mantém na cabeça os valores iniciais e ignora que as variáveis foram sobrescritas.

- Pode escolher uma alternativa na questão de múltipla escolha por tentativa ou por “intuição”, sem justificar adequadamente o raciocínio.

- Ao construir uma tabela de rastreamento (quando solicitado), comete erros em quase todas as etapas, trocando valores entre variáveis ou desrespeitando a ordem das instruções.

- Demonstra compreensão limitada dos conhecimentos K3, K4, K5 e K6, necessitando de forte intervenção docente e exemplos adicionais.

### 7.2 Nível Básico – Rastreamento Parcial com Inconsistências

O estudante em nível básico compreende a ideia de acompanhar o código linha a linha e consegue, com algum esforço, registrar corretamente parte das atualizações das variáveis.

- Em geral, acerta as primeiras atribuições (por exemplo, a = b; b = c; c = d; d = a;), mas se confunde quando surgem expressões aritméticas mais compostas (b = a + b/2; d = d + (b*2) - a;).

- Pode errar a alternativa na questão final por pequenos deslizes de cálculo ou por interpretação equivocada da precedência de operadores.

- Sua tabela de rastreamento contém alguns trechos corretos, mas apresenta inconsistências em etapas críticas.

- Demonstra domínio razoável de K1, K2 e K3, mas ainda vacila quanto a K4 e K6, precisando de prática guiada para consolidar esses conhecimentos.

### 7.3 Nível Proficiente – Rastreamento Correto e Justificação Coerente

No nível proficiente, o estudante deve ser capaz de:

- rastrear com precisão todos os passos da execução, registrando corretamente os valores de a, b, c e d após cada atribuição e operação aritmética;

- selecionar a alternativa correta na questão de múltipla escolha e justificar sua escolha com base em um raciocínio estruturado (por exemplo, apresentando a tabela de rastreamento ou descrevendo verbalmente o processo);

- interpretar a precedência de operadores em expressões como a + b/2 e d + (b*2) - a, explicando como cada parte contribui para o resultado final.

- Demonstra domínio consistente dos conhecimentos K2, K3, K4, K5 e K6, e começa a perceber questões de estilo e boas práticas ligadas a K1 (uso adequado de tipos e especificadores).

### 7.4 Nível Avançado – Análise Crítica e Generalização

No nível avançado, além de resolver corretamente a tarefa proposta, o estudante:

- questiona e analisa criticamente o código fornecido, sugerindo melhorias, como a correção dos especificadores de formato em scanf (%f em vez de %d) e a inclusão de saídas (printf) para verificar o estado das variáveis;

- é capaz de generalizar o raciocínio de rastreamento para outros trechos de código com estrutura semelhante, inclusive quando envolvem condicionais ou laços;

- discute implicações de clareza, legibilidade e manutenibilidade do código, articulando boas práticas de programação.

Esse estudante evidencia domínio abrangente dos conhecimentos K1 a K7 e alto grau de autonomia para testar, depurar e explicar soluções computacionais relacionadas a manipulação de variáveis e rastreamento de estado em programas imperativos.