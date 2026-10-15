# RELATÓRIO CSP – TAREFA 25.12  
Excesso de Peso na Pesca: Cálculo Computacional em C

## 1. Introdução
Este relatório apresenta a especificação de competências (Competency Specification Protocol – CSP) referentes à Tarefa 25.12, cujo foco é a implementação de um programa em linguagem C para automatizar o cálculo de excesso de peso e multa na atividade de pesca, conforme as regras do regulamento estadual. A análise toma como referência a descrição pedagógica completa da tarefa, enfatizando aspectos instrucionais, cognitivos e computacionais.

O objetivo deste documento é identificar, organizar e formalizar as competências necessárias ao estudante para executar a tarefa com proficiência, assegurando alinhamento à BNCC e à estrutura de competências do currículo de Computação. As competências integram conhecimentos conceituais, procedimentais e disposicionais essenciais ao desenvolvimento do raciocínio computacional.

## 2. Análise da Entidade Instrucional
A Entidade Instrucional corresponde a um problema computacional contextualizado, destinado a estudantes do 1º semestre de cursos de nível superior na área de computação. A tarefa demanda o desenvolvimento de um programa em C que:

- Leia o peso total dos peixes (P);
- Verifique se o peso ultrapassa o limite de 50 kg;
- Compute o excesso (E) caso exista;
- Calcule a multa (M), fixada em R$ 4,00 por quilo excedente;
- Exiba os valores calculados, retornando zero para E e M quando não houver excesso.

Trata-se de uma entidade instrucional orientada à aplicação de conceitos fundamentais de programação: entrada/saída, variáveis, operações aritméticas, estruturas condicionais, lógica decisória e testes. A atividade promove a articulação entre abstração, modelagem computacional e validação do funcionamento do programa por meio de experimentação prática.

A tarefa exige ainda que o estudante demonstre capacidade de explicar o fluxo do algoritmo, justificar decisões técnicas e relacionar regras do mundo real com representações formais, reforçando habilidades analíticas e comunicativas.

## 3. Enumeração dos Conhecimentos
1. Declaração e manipulação de variáveis numéricas  
2. Estruturas condicionais (`if/else`)  
3. Operações aritméticas elementares  
4. Entrada e saída padrão (`scanf` e `printf`)  
5. Representação algorítmica de regras do mundo real  
6. Testagem, validação e análise de casos de uso  

## 4. Objetivos de Aprendizagem
Ao concluir a tarefa, o estudante deverá ser capaz de:

- Representar computacionalmente regras normativas utilizando estruturas condicionais.
- Manipular variáveis numéricas para armazenar e processar dados derivados.
- Implementar um algoritmo completo em C envolvendo entrada, processamento e saída.
- Realizar cálculos aritméticos a partir de parâmetros definidos no problema.
- Testar e validar o programa em diferentes cenários, interpretando os resultados obtidos.
- Explicar o fluxo do programa com clareza e justificar decisões computacionais tomadas durante o desenvolvimento.

## 5. Especificação das Competências (CSP)

### Competência 1 - 25.12.1  
#### Título  
Modelar computacionalmente regras do mundo real utilizando estruturas condicionais.

#### Descrição Textual
Consiste em traduzir regras do contexto da pesca — limite de peso, excesso e cálculo de multa — para representações formais por meio de estruturas condicionais. Envolve a capacidade de interpretar normas, abstraí-las e expressá-las computacionalmente, garantindo precisão lógica e correlação direta entre o problema físico e o algoritmo.

#### Conhecimentos Necessários
**Estruturas Condicionais em C**  
- Descrição: Aplicação correta de `if/else` para representar decisões baseadas em valores de entrada.  
- Bloom: Aplicar  
- Verbos: Implementar, Decidir, Executar  

**Modelagem de Regras do Mundo Real**  
- Descrição: Conversão de parâmetros normativos (limites, multa, excesso) em condições computacionais.  
- Bloom: Analisar  
- Verbos: Relacionar, Interpretar, Traduzir  

#### Disposições
- Analítico  
- Responsável  
- Preciso  

#### BNCC – Alinhamento
- EM13CO07  
- Competência Geral de Computação 3  

#### Tabela Resumo
Código | Competência | Disposição | Conhecimento | Habilidade  
---|---|---|---|---  
25.12.1 | Modelar computacionalmente regras do mundo real utilizando estruturas condicionais | Analítico, Responsável, Preciso | Estruturas Condicionais em C | Aplicar (Implementar, Decidir, Executar)  
. |  |  | Modelagem de Regras do Mundo Real | Analisar (Relacionar, Interpretar, Traduzir)  

---

### Competência 2 - 25.12.2
#### Título  
Implementar cálculos derivados a partir de parâmetros definidos.

#### Descrição Textual
Refere-se à capacidade de realizar operações numéricas para determinar o excesso de peso e o valor da multa a partir das variáveis fornecidas. A competência implica precisão matemática, compreensão do fluxo de dados e uso adequado de operadores aritméticos na linguagem C.

### Conhecimentos Necessários
**Operações Aritméticas em C**  
- Descrição: Utilização de operadores matemáticos para calcular excesso e multa.  
- Bloom: Aplicar  
- Verbos: Calcular, Executar, Operar  

**Manipulação de Variáveis Numéricas**  
- Descrição: Declaração, atribuição e atualização de variáveis relacionadas ao problema.  
- Bloom: Entender  
- Verbos: Identificar, Compreender, Utilizar  

#### Disposições
- Meticuloso  
- Organizado  
- Sistemático  

#### BNCC – Alinhamento
- EM13CO01  
- Competência Geral de Computação 1  

#### Tabela Resumo
Código | Competência | Disposição | Conhecimento | Habilidade  
---|---|---|---|---  
25.12.2 | Implementar cálculos derivados a partir de parâmetros definidos | Meticuloso, Organizado, Sistemático | Operações Aritméticas em C | Aplicar (Calcular, Executar, Operar)  
. |  |  | Manipulação de Variáveis Numéricas | Entender (Identificar, Compreender, Utilizar)  

---

### Competência 3 - 25.12.3
#### Título  
Estruturar programas em C com entrada, processamento e saída.

#### Descrição Textual
Envolve a habilidade de organizar um programa completo em C, compreendendo as etapas de leitura de dados, processamento interno e emissão de resultados. A competência inclui o uso correto de `scanf` e `printf`, bem como a organização lógica do fluxo computacional.

#### Conhecimentos Necessários
**Entrada e Saída em C**  
- Descrição: Utilização de funções de E/S para interação com o usuário.  
- Bloom: Aplicar  
- Verbos: Ler, Exibir, Implementar  

**Fluxo Algorítmico**  
- Descrição: Estruturação coerente do processo computacional (input → process → output).  
- Bloom: Compreender  
- Verbos: Explicar, Organizar, Relacionar  

#### Disposições
- Comunicativo  
- Clareza lógica  
- Atenção ao detalhe  

#### BNCC – Alinhamento
- EM13CO03  
- Competência Geral de Computação 4  

#### Tabela Resumo
Código | Competência | Disposição | Conhecimento | Habilidade  
---|---|---|---|---  
25.12.3 | Estruturar programas em C com entrada, processamento e saída | Comunicativo, Claro, Atento | Entrada e Saída em C | Aplicar (Ler, Exibir, Implementar)  
. |  |  | Fluxo Algorítmico | Compreender (Explicar, Organizar, Relacionar)  

---

### Competência 4 - 25.12.4
#### Título  
Validar o funcionamento da solução computacional por meio de testes.

#### Descrição Textual
Consiste em testar o programa utilizando diferentes cenários (abaixo, igual e acima do limite de 50 kg) para verificar a correção da lógica implementada. A competência envolve interpretação dos resultados, identificação de inconsistências e justificativa das decisões tomadas.

#### Conhecimentos Necessários
**Testes e Casos de Borda**  
- Descrição: Avaliação sistemática do programa em múltiplos cenários.  
- Bloom: Analisar  
- Verbos: Testar, Verificar, Avaliar  

**Interpretação de Saída Computacional**  
- Descrição: Compreensão e análise dos resultados gerados pelo programa.  
- Bloom: Avaliar  
- Verbos: Julgar, Comparar, Validar  

#### Disposições
- Reflexivo  
- Crítico  
- Perseverante  

#### BNCC – Alinhamento
- EM13CO05  
- Competência Geral de Computação 5  

#### Tabela Resumo
Código | Competência | Disposição | Conhecimento | Habilidade  
---|---|---|---|---  
25.12.4 | Validar o funcionamento da solução computacional por meio de testes | Reflexivo, Crítico, Perseverante | Testes e Casos de Borda | Analisar (Testar, Verificar, Avaliar)  
. |  |  | Interpretação de Saída Computacional | Avaliar (Julgar, Comparar, Validar)  

---

## Conclusão
Este relatório consolida as competências essenciais para o desenvolvimento da Tarefa 25.12, articulando saberes computacionais fundamentais para estudantes iniciantes em programação. A análise evidencia a necessidade de integrar compreensão conceitual, execução técnica e habilidades de validação e interpretação, assegurando uma formação alinhada às diretrizes da BNCC e às práticas contemporâneas do ensino de Computação.