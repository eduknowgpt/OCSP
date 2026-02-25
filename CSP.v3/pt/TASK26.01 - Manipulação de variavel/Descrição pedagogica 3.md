## Título da Atividade  
**Rastreamento de Estado de Variáveis em Atribuições Sequenciais (C)**

---

## Contexto Instrucional  
Atividade aplicada em **Lógica de Programação / Programação Estruturada** (curso técnico em Informática ou nível introdutório), com foco em **execução sequencial**, **atribuição**, **dependência entre variáveis** e **avaliação de expressões aritméticas**.  
A resolução é **individual** e registrada por escrito, em formato compatível com correção objetiva.

---

## Objetivo da Atividade  
Ao final da atividade, o estudante deverá ser capaz de **analisar** a execução de um trecho de programa em C, **rastrear** as mudanças de estado de quatro variáveis após cada instrução e **justificar** a alternativa escolhida com base em um registro verificável do rastreamento.

---

## Descrição da Tarefa  
Considerando o trecho de programa em C fornecido no enunciado e assumindo que os valores iniciais atribuídos às variáveis `A`, `B`, `C` e `D` são, respectivamente, **10, 15, 20 e 25**, o estudante deve:

1. **Determinar os valores finais** de `A`, `B`, `C` e `D` após a execução completa do trecho.  
2. **Selecionar a alternativa** que corresponde ao conjunto final de valores.  
3. Produzir um **rastreio (trace)** do estado `(A, B, C, D)` **após cada instrução** do trecho, registrando cálculos intermediários quando houver expressões.

**Requisitos mínimos**
- O rastreio deve mostrar o estado completo `(A, B, C, D)` após cada linha relevante, sem “saltos”.
- Nas expressões aritméticas, o estudante deve indicar ao menos as operações que determinam o valor final (ex.: divisão e soma).
- Quando surgirem resultados não inteiros, o registro deve manter **coerência com valores decimais** (condizente com variáveis de ponto flutuante).

**Condição didática de análise**
- O foco é o **raciocínio sobre o estado das variáveis** durante a execução sequencial; portanto, considera-se como dado que as variáveis iniciam com (10, 15, 20, 25), conforme informado no enunciado.

---

## Processo de Desenvolvimento  
1. Registrar o estado inicial `(A, B, C, D)`.  
2. Avançar linha a linha, atualizando apenas a variável afetada e registrando o novo estado completo.  
3. Em linhas com expressões, calcular usando os **valores vigentes naquele ponto** e então registrar o estado atualizado.  
4. Ao final, comparar o conjunto obtido com as alternativas e marcar a correspondente.  
5. Revisar o rastreio para confirmar consistência (sem uso de valores “anteriores” após sobrescrita).

---

## Evidências Esperadas  
- **Alternativa marcada** (resposta final).  
- **Rastreio completo** do estado `(A, B, C, D)` após cada instrução, com cálculos intermediários quando aplicável.  
- **Justificativa breve** (1–3 linhas) explicando a escolha com base no rastreio.

---

## Critérios de Avaliação  

### Dimensão Técnica  
Observa-se se o estudante:
- Obtém o conjunto final correto de valores.  
- Mantém consistência entre cálculos intermediários e registros de estado.  

### Dimensão Cognitiva  
Observa-se se o estudante:
- Demonstra compreensão de **sobrescrita** (atribuições substituem valores anteriores).  
- Usa corretamente valores **vigentes** no momento de cada expressão e respeita a ordem das operações.  

### Dimensão Atitudinal  
Observa-se se o estudante:
- Apresenta rastreio **legível, organizado e auditável**.  
- Sustenta a resposta com evidência (rastreio), evitando respostas sem base verificável.