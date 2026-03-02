## Título da Atividade
Cálculo de Fatoriais de Múltiplas Entradas com Função (TASK26.04)

## Contexto Instrucional
Atividade individual em disciplina introdutória de programação (nível técnico ou equivalente), voltada à construção de um algoritmo/programa com leitura de dados, processamento repetido e decomposição em função. A entrega deve permitir verificação objetiva do comportamento por meio do artefato produzido e de saídas observáveis.

## Objetivo da Atividade
Desenvolver uma solução que processe uma quantidade definida de valores de entrada e, para cada um, obtenha o fatorial por meio de uma função dedicada, garantindo resultados verificáveis e consistentes.

## Descrição da Tarefa
O estudante deve elaborar um algoritmo que:
1. leia um número de entrada **n**, que representa a quantidade de valores a serem informados em seguida;
2. leia **n** valores numéricos;
3. para cada valor lido, calcule o seu fatorial utilizando obrigatoriamente uma função (isto é, o cálculo não deve estar “embutido” apenas no fluxo principal);
4. apresente, de forma verificável, o resultado do fatorial correspondente a cada valor informado.

Além do resultado final, deve ser incluída uma justificativa breve descrevendo como a função foi empregada para realizar o cálculo solicitado.

## Condições de Execução
- Como o fatorial é matematicamente definido para inteiros não negativos, a solução deve assumir esse domínio para os valores informados ou, caso o estudante opte por aceitar outros valores, deve explicitar e tratar de forma consistente a situação fora do domínio (por exemplo, sinalizando entrada inválida).
- A função de fatorial deve ter responsabilidade clara: receber um valor de entrada e retornar/produzir o fatorial correspondente, sendo chamada sempre que um novo valor for processado.
- Considerando o crescimento rápido do fatorial, o estudante deve manter coerência entre o tipo numérico adotado e a faixa de valores que pretende suportar, evitando resultados inconsistentes por limitações de representação numérica no ambiente utilizado.
- O algoritmo deve garantir que a leitura de **n** valores ocorra de forma controlada e que cada resultado possa ser associado ao respectivo valor de entrada.

## Evidências Esperadas
- Artefato de solução (algoritmo em pseudocódigo ou programa na linguagem adotada na disciplina) contendo:
  - leitura de **n**;
  - leitura repetida de **n** valores;
  - definição e uso de uma função para cálculo do fatorial;
  - apresentação dos resultados de forma conferível.
- Registros de execução/teste que incluam:
  - pelo menos um caso de contorno (ex.: valores mínimos do domínio do fatorial) e
  - um caso com múltiplas entradas (n > 1), evidenciando chamadas repetidas da função.
- Justificativa breve (2–5 linhas) explicando a organização da solução e o papel da função no cálculo.

## Critérios de Avaliação
- **Correção do comportamento:** calcula corretamente o fatorial para cada valor informado dentro do domínio assumido.
- **Completude e consistência:** lê exatamente **n** valores e produz resultados correspondentes para todos eles, sem omissões.
- **Uso adequado de função:** o cálculo do fatorial é realizado por função dedicada, devidamente integrada ao processamento dos **n** valores.
- **Verificabilidade:** resultados apresentados de maneira clara e rastreável (é possível conferir qual saída corresponde a qual entrada).
- **Coerência técnica:** escolhas sobre domínio de entrada e tipo numérico são consistentes e não geram resultados contraditórios no contexto do problema.