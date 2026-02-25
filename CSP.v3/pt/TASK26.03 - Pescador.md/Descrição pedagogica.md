## Título da Atividade
Cálculo de Excesso de Peso de Peixes e Multa (Linguagem C)

## Contexto Instrucional
Atividade individual, típica de uma disciplina introdutória de programação em linguagem C, voltada à prática de leitura de dados, uso de variáveis e tomada de decisão com estrutura condicional. A tarefa pode ser realizada em laboratório (compilação e execução) ou como exercício escrito com entrega do algoritmo e do código-fonte.

## Objetivo da Atividade
Desenvolver um programa que, a partir do peso total de peixes informado, determine se há excesso em relação a um limite fixo (50 kg) e calcule, quando aplicável, o valor da multa proporcional ao peso excedente.

## Descrição da Tarefa
O estudante deve elaborar um programa em C que:
- Leia um valor **P** correspondente ao **peso de peixes** (em quilogramas).
- Verifique se **P > 50**.
  - Se houver excesso, registre em **E** o valor do **excesso** (isto é, *P − 50*) e em **M** o valor da **multa** correspondente, calculada como **4,00 reais por quilograma excedente** (*M = E × 4,00*).
  - Caso contrário, registre **E = 0** e **M = 0**.
- Apresente ao final os valores calculados de **E** e **M** (com zero quando não houver excesso).

> Observação técnica (para reduzir ambiguidade de correção): como o enunciado não explicita se **P** é inteiro ou real, o programa deve aceitar **P como número real** (em kg), mantendo coerência aritmética no cálculo de **E** e **M**. Para **M**, por se tratar de valor monetário, recomenda-se exibição com **duas casas decimais**.

## Processo de Desenvolvimento
1. Interpretar o enunciado e identificar entradas (**P**), processamento (comparação com 50; cálculo de **E** e **M**) e saídas (**E** e **M**).
2. Definir as variáveis necessárias (**P**, **E**, **M**) e inicializar **E** e **M** conforme o caso.
3. Implementar a decisão usando uma estrutura condicional:
   - Caso **P > 50**, calcular **E = P − 50** e **M = E × 4,00**.
   - Caso contrário, atribuir **E = 0** e **M = 0**.
4. Exibir os resultados de modo verificável (valores numéricos de **E** e **M**), garantindo consistência de unidades (kg) e moeda (R$).

## Evidências Esperadas
- Código-fonte em C que compila e executa sem erros.
- Saída do programa apresentando **E** (excesso em kg) e **M** (multa em R$), com **zero** quando **P ≤ 50**.
- Justificativa breve (2–5 linhas) explicando:
  - a condição usada para detectar excesso;
  - como foram obtidas as expressões de **E** e **M**.

## Critérios de Avaliação
**a) Dimensão Técnica (correção do raciocínio/solução)**
- Leitura correta de **P** e uso apropriado de variáveis.
- Condição de excesso corretamente aplicada (**P > 50**).
- Cálculo correto de **E = P − 50** quando houver excesso e **E = 0** caso contrário.
- Cálculo correto de **M = E × 4,00** e atribuição de **M = 0** quando não houver excesso.
- Apresentação de **E** e **M** coerente com o caso (excesso vs. não excesso).

**b) Dimensão Cognitiva (compreensão e explicação)**
- Explicação clara da relação entre limite, excesso e multa.
- Capacidade de justificar a estrutura condicional e as fórmulas utilizadas.
- Coerência entre a justificativa e o comportamento observado na execução.

**c) Dimensão Atitudinal (postura acadêmica na entrega)**
- Entrega organizada (código legível, nomes de variáveis coerentes e saída compreensível).
- Resultado verificável: valores exibidos de forma consistente, permitindo conferência objetiva.
- Responsabilidade na apresentação: ausência de omissões relevantes (por exemplo, não deixar variáveis sem atribuição em algum ramo da condição).