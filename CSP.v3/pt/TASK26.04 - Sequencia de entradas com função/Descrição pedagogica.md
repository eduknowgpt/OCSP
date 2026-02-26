## **Título da Atividade**
Cálculo de Fatorial para uma Sequência de Entradas com Função

## **Contexto Instrucional**
Atividade individual em disciplina introdutória de programação, realizada em ambiente de laboratório (com compilação/execução) ou como avaliação prática. O estudante entrega um programa/algoritmo funcional, acompanhado de registros de teste e justificativa breve sobre as decisões adotadas.

## **Objetivo da Atividade**
Desenvolver uma solução que controle a leitura de múltiplos valores a partir de uma contagem informada e calcule o fatorial de cada valor por meio de uma função, produzindo resultados verificáveis.

## **Descrição da Tarefa**
1. Ler um número de entrada **n**, que representa a quantidade de valores a serem inseridos em seguida.  
2. Ler **n** valores numéricos e, para **cada** valor lido, calcular o respectivo **fatorial**.  
3. O cálculo do fatorial deve ser realizado **obrigatoriamente por uma função**, invocada a partir do fluxo principal.  
4. Apresentar, para cada valor de entrada, o resultado do fatorial de forma que seja possível conferir a correspondência entre entrada e saída.  
5. Fornecer uma justificativa breve descrevendo o papel da função e como o programa garante que exatamente **n** valores são processados.

## **Condições de Execução**
- A solução deve conter uma **função dedicada** ao cálculo do fatorial (não apenas um bloco repetido no corpo principal).
- Como o enunciado não explicita o domínio dos “n números”, adotar uma hipótese técnica mínima e comum ao conceito de fatorial: **tratar as entradas como inteiros não negativos**; se o estudante optar por outro tratamento, deve **registrar explicitamente** a decisão e suas implicações.
- Garantir consistência para casos de borda plausíveis, como **n = 0** (não solicitar valores adicionais e finalizar de forma coerente).
- Considerar que o fatorial cresce rapidamente: utilizar representação numérica compatível com a linguagem adotada e, se houver limite prático de entrada para evitar estouro numérico, **documentar** esse limite de forma objetiva.

## **Evidências Esperadas**
- Código-fonte (ou pseudocódigo formal).
- Registros de teste (entradas e saídas) cobrindo, no mínimo:
  - um caso com valor **0** ou **1**;
  - um caso com valor **maior que 1**;
  - um caso com **mais de um** valor (n > 1).
- Justificativa breve (3–6 linhas) descrevendo a organização da solução e as decisões sobre domínio/limites numéricos (quando aplicável).

## **Critérios de Avaliação**
- **Correção do comportamento:** lê **n**, processa exatamente **n** valores e apresenta o fatorial correspondente a cada entrada.
- **Uso adequado de função:** o cálculo do fatorial está encapsulado em função e é invocado de maneira coerente no fluxo do programa.
- **Completude e consistência:** tratamento consistente de casos como **n = 0** e coerência com o domínio assumido para o fatorial.
- **Verificabilidade:** saídas e registros de teste permitem conferência objetiva dos resultados.
- **Clareza técnica:** justificativa breve, direta e compatível com o artefato entregue (sem contradições).