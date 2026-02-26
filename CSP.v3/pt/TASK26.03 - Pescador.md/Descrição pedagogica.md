## Título da Atividade
Cálculo de Excesso de Peso e Multa (Linguagem C)

## Contexto Instrucional
Atividade individual em disciplina introdutória de programação em C (nível técnico ou equivalente), voltada ao uso de **entrada/saída**, **variáveis**, **expressões aritméticas** e **estruturas condicionais**, com entrega de solução executável e resultados verificáveis.

## Objetivo da Atividade
Desenvolver um programa que aplique uma regra de decisão para identificar **excesso** em relação a um limite estabelecido e calcular a **multa proporcional** ao excedente, produzindo saída consistente e conferível.

## Descrição da Tarefa
A partir do peso total de peixes informado pelo usuário (**P**, em quilogramas), o estudante deve construir um programa em C que:
- determine se o peso ultrapassa o limite definido no enunciado;
- quando houver ultrapassagem, **registre o excedente** na variável **E** e **calcule a multa** correspondente na variável **M**, conforme a taxa por quilograma excedente descrita no enunciado;
- ao final, exiba os valores de **E** e **M** de forma verificável.

## Condições de Execução
- Utilizar **estrutura condicional** para tratar explicitamente os cenários “com excesso” e “sem excesso”.
- Garantir que **E** e **M** recebam valores definidos em qualquer caminho de execução.
- Adotar tipos numéricos compatíveis com a leitura do peso e com o cálculo do valor monetário, assegurando consistência entre cálculo e saída.
- Recomenda-se validar a solução com entradas que cubram os dois cenários (abaixo/igual ao limite e acima do limite).

## Evidências Esperadas
- Código-fonte em C que realiza: leitura de **P**, decisão por **estrutura condicional**, atribuição de **E** e **M**, e impressão dos resultados.
- Registros de execução (saídas) que permitam verificar o comportamento do programa nos cenários “sem excesso” e “com excesso”.
- Justificativa breve (2–5 linhas) descrevendo a condição utilizada e a lógica geral do cálculo (sem reescrever o código).

## Critérios de Avaliação
- **Correção:** identifica corretamente quando há/não há excesso e produz valores de **E** e **M** compatíveis com a regra do enunciado.
- **Completude e consistência:** atribuições de **E** e **M** em todos os caminhos; coerência entre entrada, processamento e saída.
- **Verificabilidade e clareza:** saída legível e suficiente para conferência; justificativa breve, objetiva e tecnicamente coerente.