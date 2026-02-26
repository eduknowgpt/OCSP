# Catálogo de Conhecimentos da Disciplina — Introdução à Programação (Univasf)

**Objetivo:** estabelecer um *conjunto fixo e reutilizável* de conhecimentos (KDisc) para a disciplina **Introdução à Programação**, a ser usado como **limite superior** (escopo) na geração de relatórios CSP de tarefas da disciplina.  
**Regra de uso no CSP:** em cada tarefa, o relatório CSP **seleciona um subconjunto** deste catálogo (não cria novos conhecimentos fora dele). Extensões só são aceitas se a ementa/catálogo forem revisados.


## Fontes e âncoras

- **Ementa da disciplina (Univasf):** tópicos listados como pré-requisitos/conteúdos (inclui: von Neumann, C11, paradigma imperativo, variáveis/constantes, tipos simples, programação estruturada, sequência, expressões, seleção/repetição, tipos estruturados, subprogramas, recursão, arquivos e diretórios).  
- **CS2023 (ACM/IEEE):** Knowledge Unit **SDF-Fundamentals** (tópicos 1–8) e **SDF-Data-Structures** (tópico 4 para strings), usados aqui como **âncora externa**.

### Convenção de códigos CS2023 (coluna “Código CS2023 curto”)
- **SDF-n** = *SDF-Fundamentals*, tópico **n**  
- **SDFDS-n** = *SDF-Data-Structures*, tópico **n**  
- (Opcional/apoio) **ARASM-n** = *AR-Assembly*, tópico **n**; **ARMEM-n** = *AR-Memory*, tópico **n**



## Tabela-resumo do catálogo (KDisc)

| Código | Conhecimento (título reutilizável) | Rastreio na ementa (tópico) | Código CS2023 curto |
|---|---|---|---|
| K01 | Modelo de execução e noção de estado (paradigma imperativo) | Arquitetura de von Neumann; O paradigma imperativo; Programação estruturada; Estrutura sequencial | SDF-2 |
| K02 | Fundamentos práticos da linguagem C (C11) para programação introdutória | Introdução à linguagem C11 | SDF-1…SDF-6 *(genérico; CS2023 não fixa linguagem)* |
| K03 | Variáveis, constantes e tipos primitivos | Conceito de variáveis e constantes; Tipos de dados simples: inteiro, caracter, ponto flutuante | SDF-1 |
| K04 | Expressões aritméticas e avaliação | Expressões aritméticas | SDF-1 |
| K05 | Expressões lógicas e condições | Expressões lógicas | SDF-3 |
| K06 | Estrutura sequencial e E/S básica | Estrutura sequencial | SDF-3 |
| K07 | Estruturas de seleção | Estrutura de seleção | SDF-3 |
| K08 | Estruturas de repetição | Estrutura de repetição | SDF-3 |
| K09 | Tipos de dados estruturados em C (vetores, matrizes, strings, enum, union) | Tipos de dados estruturados: arranjos, cadeia de caracteres, matrizes, enumerações, uniões | SDF-6 + SDFDS-4 |
| K10 | Subprogramas: procedimentos e funções | Subprogramas: procedimentos e funções | SDF-4 |
| K11 | Recursão em subprogramas | Subprogramas recursivos | SDF-8 |
| K12 | Arquivos e diretórios (persistência e organização básica) | Arquivos e diretórios | SDF-5 |



## Definições detalhadas

### K01 — Modelo de execução e noção de estado (paradigma imperativo)
- **Descrição:** compreensão operacional de que um programa imperativo evolui por mudanças de estado durante a execução.
- **Escopo mínimo:** estado/atribuição como transição; sequência e fluxo de controle em nível introdutório.
- **Rastreio na ementa:** Arquitetura de von Neumann; O paradigma imperativo; Programação estruturada; Estrutura sequencial.
- **Código CS2023 curto:** SDF-2.
- **Evidências típicas (em tarefas):** rastrear execução, explicar atualizações de variáveis, justificar ordem de operações/efeitos.
- **Observações de reuso:** base transversal para praticamente qualquer tarefa de programação imperativa na disciplina.

---

### K02 — Fundamentos práticos da linguagem C (C11) para programação introdutória
- **Descrição:** elementos de sintaxe e convenções mínimas em C (C11) para expressar soluções de programação introdutória.
- **Escopo mínimo:** estrutura de um programa, declarações simples, comandos básicos, compilação/execução no nível exigido pela disciplina.
- **Rastreio na ementa:** Introdução à linguagem C11.
- **Código CS2023 curto:** SDF-1…SDF-6 *(genérico; CS2023 não fixa linguagem, mas estes tópicos pressupõem uma linguagem escolhida)*.
- **Evidências típicas:** código que compila/executa; uso adequado de tipos/declarações; consistência entre intenção e sintaxe.
- **Observações de reuso:** não deve virar competência “de sintaxe”; serve como base operacional para evidenciar os demais KDisc.

---

### K03 — Variáveis, constantes e tipos primitivos
- **Descrição:** representação de dados simples e uso de identificadores para armazenar/manipular valores.
- **Escopo mínimo:** inteiros, caracteres, ponto flutuante; constantes; atribuição; coerência de tipos em operações básicas.
- **Rastreio na ementa:** Conceito de variáveis e constantes; Tipos de dados simples: inteiro, caracter, ponto flutuante.
- **Código CS2023 curto:** SDF-1.
- **Evidências típicas:** declarar/atribuir corretamente; escolher tipo coerente; evitar conversões problemáticas em cálculos básicos.
- **Observações de reuso:** aplica-se a tarefas numéricas, condicionais, repetição e manipulação de estruturas.

---

### K04 — Expressões aritméticas e avaliação
- **Descrição:** construção e avaliação de expressões aritméticas com operadores e precedência.
- **Escopo mínimo:** operadores aritméticos; precedência/associatividade; composição de expressões; atualização por atribuição.
- **Rastreio na ementa:** Expressões aritméticas.
- **Código CS2023 curto:** SDF-1.
- **Evidências típicas:** cálculos corretos; uso explícito de parênteses quando necessário; resultados coerentes.
- **Observações de reuso:** essencial para problemas de cálculo, simulações simples e processamento de dados.

---

### K05 — Expressões lógicas e condições
- **Descrição:** construção de condições booleanas para tomada de decisão e controle de fluxo.
- **Escopo mínimo:** operadores relacionais e lógicos; composição de condições; interpretação de verdade/falsidade.
- **Rastreio na ementa:** Expressões lógicas.
- **Código CS2023 curto:** SDF-3.
- **Evidências típicas:** condições corretas em if/while; tratamento de casos; coerência entre regra do problema e condição.
- **Observações de reuso:** aparece em seleção, repetição, validação de entrada e checagens de invariantes simples.

---

### K06 — Estrutura sequencial e E/S básica
- **Descrição:** organização de programas como sequência de comandos com interação básica.
- **Escopo mínimo:** comandos sequenciais; atribuição; leitura/saída básica (no nível adotado pela disciplina).
- **Rastreio na ementa:** Estrutura sequencial.
- **Código CS2023 curto:** SDF-3.
- **Evidências típicas:** fluxo entrada→processamento→saída; saídas verificáveis; consistência do formato de saída.
- **Observações de reuso:** núcleo para qualquer tarefa com transformação de entrada em resultado.

---

### K07 — Estruturas de seleção
- **Descrição:** escolha de caminhos alternativos de execução com base em condições.
- **Escopo mínimo:** if/else (e, se aplicável, switch); aninhamento/encadeamento; cobertura de casos.
- **Rastreio na ementa:** Estrutura de seleção.
- **Código CS2023 curto:** SDF-3.
- **Evidências típicas:** implementação correta de regras; ausência de lacunas; explicação do porquê de cada ramo.
- **Observações de reuso:** frequente em tarefas de decisão, classificação, regras de negócio simples.

---

### K08 — Estruturas de repetição
- **Descrição:** execução repetida de blocos de comandos controlada por condição ou contador.
- **Escopo mínimo:** while/for/do-while; condições de parada; laços por contagem e por condição.
- **Rastreio na ementa:** Estrutura de repetição.
- **Código CS2023 curto:** SDF-3.
- **Evidências típicas:** laços corretos; parada garantida; processamento acumulativo/iterativo coerente.
- **Observações de reuso:** central para varreduras de vetores, repetição de leituras e simulações.

---

### K09 — Tipos de dados estruturados em C (vetores, matrizes, strings, enum, union)
- **Descrição:** representação e manipulação de coleções e estruturas básicas em C.
- **Escopo mínimo:** vetores/arranjos; matrizes; strings (cadeias de caracteres); enumerações; uniões — com acesso por índice e percorrimento.
- **Rastreio na ementa:** Tipos de dados estruturados: arranjos, cadeia de caracteres, matrizes, enumerações, uniões.
- **Código CS2023 curto:** SDF-6 + SDFDS-4 (strings).
- **Evidências típicas:** indexação correta; percorrimento; atualização; manipulação de texto básica quando aplicável.
- **Observações de reuso:** habilita tarefas com coleções, tabelas, tabuleiros, listas de dados e processamento textual simples.

---

### K10 — Subprogramas: procedimentos e funções
- **Descrição:** decomposição de problemas em subprogramas coesos com parâmetros/retorno.
- **Escopo mínimo:** definição/invocação; passagem de parâmetros; retorno; noção de escopo; organização modular do programa.
- **Rastreio na ementa:** Subprogramas: procedimentos e funções.
- **Código CS2023 curto:** SDF-4.
- **Evidências típicas:** funções com responsabilidade clara; reuso; chamadas corretas; coerência entre dados de entrada/saída.
- **Observações de reuso:** favorece reuso entre tarefas e facilita avaliação por unidades de comportamento.

---

### K11 — Recursão em subprogramas
- **Descrição:** definição e uso de subprogramas recursivos como estratégia de resolução.
- **Escopo mínimo:** caso base e caso recursivo; progresso para término; rastreamento conceitual de chamadas.
- **Rastreio na ementa:** Subprogramas recursivos.
- **Código CS2023 curto:** SDF-8.
- **Evidências típicas:** funções recursivas corretas; término garantido; explicação do fluxo de chamadas e do caso base.
- **Observações de reuso:** usar apenas quando a tarefa realmente exigir/permitir; pode ser um eixo de atividades específicas da disciplina.

---

### K12 — Arquivos e diretórios (persistência e organização básica)
- **Descrição:** leitura/escrita de dados em arquivos e noções mínimas de organização por diretórios, no nível da disciplina.
- **Escopo mínimo:** abrir/ler/escrever/fechar arquivos; persistência simples entre execuções; caminhos/diretórios quando necessário.
- **Rastreio na ementa:** Arquivos e diretórios.
- **Código CS2023 curto:** SDF-5.
- **Evidências típicas:** persistir dados; ler entradas de arquivo; produzir saídas em arquivo; explicar a persistência.
- **Observações de reuso:** recomendado para tarefas de processamento de dados e miniaplicações com persistência.

---

## Itens explicitamente fora do escopo (por padrão)
Os tópicos abaixo aparecem no CS2023, mas **não estão explicitados na ementa** da disciplina (a menos que você decida incorporá-los formalmente):
- **SDF-9 (erros de execução) / SDF-10 (teste e depuração) / SDF-11 (documentação/comentários) / SDF-12 (mentalidade de segurança)**  
Se surgirem em uma tarefa, trate como **EXT (extensão)** e não crie novos KDisc sem atualizar este catálogo.

---

## Política de manutenção
- Alterações neste catálogo devem ocorrer **apenas** quando a ementa da disciplina mudar (ou quando a coordenação decidir incorporar extensões).
- Cada tarefa deve declarar explicitamente quais **KDisc** foram mobilizados (subconjunto), para garantir rastreabilidade e reuso.


