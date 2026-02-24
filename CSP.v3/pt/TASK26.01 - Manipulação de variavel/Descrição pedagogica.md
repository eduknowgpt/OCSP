## Título da Atividade  
**Rastreamento de Variáveis em Sequência de Atribuições na Linguagem C**

---

## Contexto Instrucional  
Esta atividade é indicada para a disciplina de **Lógica de Programação / Programação Estruturada**, em cursos **técnicos em Informática** (ou disciplinas introdutórias de programação em nível superior). Seu objetivo formativo geral é consolidar a compreensão de **atribuição**, **dependência entre variáveis**, **ordem de execução** e **avaliação de expressões aritméticas** em um trecho de programa em C.

A organização recomendada é **individual**, pois a tarefa exige atenção ao estado interno do algoritmo e registro sistemático do raciocínio. A avaliação ocorre **sem apresentação oral**, com base na resposta selecionada e na justificativa escrita (rastreio), podendo ser aplicada como exercício avaliativo de curta duração ou atividade diagnóstica.

---

## Objetivo da Atividade  
Ao final da atividade, o estudante deverá ser capaz de **analisar** a execução de um trecho de programa em C, **rastrear** passo a passo as alterações sofridas por variáveis ao longo de uma sequência de comandos de atribuição e expressões aritméticas, e **justificar** a escolha da alternativa correta com base em um registro organizado dos valores assumidos por cada variável após cada instrução.

---

## Descrição da Tarefa  
O estudante receberá um trecho de algoritmo em C no qual quatro variáveis (A, B, C e D) são inicialmente preenchidas com os valores **10, 15, 20 e 25** (nessa ordem) e, em seguida, passam por uma sequência de atribuições e cálculos.

A tarefa consiste em:

1. **Determinar os valores finais** de A, B, C e D após a execução completa do algoritmo.  
2. **Selecionar a alternativa correta** dentre as opções fornecidas.  
3. **Apresentar um rastreamento escrito** (tabela ou registro sequencial) mostrando os valores de A, B, C e D **após cada linha de atribuição**, incluindo as contas intermediárias quando houver expressões.

### Requisitos mínimos da solução (obrigatórios)  
- Registrar os valores de **A, B, C e D após cada comando de atribuição**, evidenciando claramente quando um valor é sobrescrito.  
- Indicar, nas linhas com expressão aritmética, **como o valor foi calculado** (por exemplo, destacando a divisão e a soma).  
- Manter consistência na representação numérica, considerando que o algoritmo utiliza **variáveis de ponto flutuante** (valores podem assumir casas decimais).

### Condições a serem respeitadas  
- O rastreamento deve considerar que **cada linha é executada em sequência** e que as expressões utilizam os **valores atualizados** das variáveis no momento em que são avaliadas.  
- Não é esperado uso de código adicional: o foco é a **análise do comportamento do algoritmo** e a **interpretação correta das atribuições**.

### Comportamentos esperados da solução  
- **Correção** (valores finais compatíveis com o rastreio).  
- **Clareza** (registro legível e verificável por outra pessoa).  
- **Rastreabilidade** (capacidade de conferir a resposta a partir das etapas registradas).

---

## Processo de Desenvolvimento  

### Recursos disponíveis  
- Papel e caneta, quadro, ou planilha simples para montar a tabela de rastreamento.  
- Opcionalmente, um ambiente de desenvolvimento C (para validação), caso o docente decida permitir verificação prática.

### Conhecimentos prévios necessários  
- Conceito de **variável** e **atribuição** (entender que “recebe” sobrescreve o valor anterior).  
- **Ordem de execução** sequencial.  
- **Expressões aritméticas** e prioridade de operadores (especialmente divisão antes de soma).  
- Noções básicas de tipos numéricos (inteiro vs ponto flutuante), suficientes para interpretar resultados com decimais.

### Como conduzir o desenvolvimento (orientação ao estudante)  
1. Escreva os valores iniciais de A, B, C e D.  
2. Para cada linha de atribuição do algoritmo:  
   - Atualize somente a(s) variável(is) modificada(s).  
   - Registre novamente o conjunto (A, B, C, D) após a execução daquela linha.  
3. Nas linhas com cálculo, faça a conta explicitamente e só depois atualize o valor da variável.  
4. Ao final, compare seu resultado com as alternativas e selecione a que coincide com os valores finais obtidos.

### Trabalho colaborativo e responsabilidade individual  
Embora possa haver discussão breve para checagem de raciocínio, a entrega deve ser **individual**, assegurando autoria e consistência do registro do rastreamento.

---

## Evidências Esperadas  
- **Alternativa marcada** (resposta final).  
- **Rastreio/tabela de execução** com os valores de A, B, C e D após cada comando de atribuição.  
- **Justificativa breve** (1–2 parágrafos ou observações na tabela) explicando pontos críticos, como sobrescrita de valores e uso de valores atualizados nas expressões.

---

## Critérios de Avaliação  

### Dimensão Técnica  
Será observado se o estudante:  
- Determina corretamente os **valores finais** de A, B, C e D.  
- Mantém um rastreio coerente, sem “pulos” de estado ou atualizações indevidas.  
- Trata adequadamente resultados com **valores decimais**, quando surgirem das operações.

### Dimensão Cognitiva  
Será observado se o estudante:  
- Explica de forma consistente **por que** os valores mudam (sobrescrita, dependência entre variáveis e sequência de execução).  
- Demonstra compreensão de que expressões usam os **valores vigentes no momento** do cálculo.  
- Identifica trechos mais propensos a erro conceitual, como reatribuições encadeadas e expressões com múltiplas operações.

### Dimensão Atitudinal  
Será observado se o estudante:  
- Apresenta registro **organizado, legível e verificável**, permitindo auditoria do raciocínio.  
- Mantém postura de **responsabilidade acadêmica** (produção própria e justificativa compatível com o resultado).  
- Demonstra cuidado e atenção a detalhes, evitando respostas “por tentativa” sem rastreamento.
