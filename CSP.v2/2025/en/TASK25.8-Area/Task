# Inferências Realizadas (preenchimento automático de lacunas)

Para produzir uma descrição didática completa, equivalente em profundidade ao arquivo *TASK25.7-Factorial.md*, algumas lacunas presentes no enunciado original foram preenchidas por inferência pedagógica:

1. **Suposição de faixa de domínio dos valores**  
   Admitiu-se que o número de lados deve ser um inteiro positivo ≥ 3, pois polígonos regulares não existem abaixo desse limite.

2. **Cálculo da área de triângulo e quadrado**  
   O enunciado não detalhava as fórmulas de área. Inferiu-se que:
   - Para **triângulo equilátero**: \( A = \frac{l^2\sqrt{3}}{4} \)  
   - Para **quadrado**: \( A = l^2 \)

3. **Tratamento padronizado para o pentágono**  
   A atividade solicita apenas “escrever PENTÁGONO”, sem área. Foi inferido que:
   - A tarefa pretende trabalhar *classificação condicional*, não cálculos geométricos avançados.
   - Portanto, o programa apenas identifica o pentágono, sem calcular área.

4. **Uso de condicionais estruturadas**  
   O enunciado não explicita a estrutura de controle. Inferiu-se que o propósito pedagógico envolve prática com estruturas condicionais (if/elif/else).

5. **Validação de entradas inválidas**  
   Embora não mencionada, foi inferida a necessidade de rejeitar valores abaixo de 3, como ocorre em atividades padrão do 1º semestre.

6. **Unidade de medida**  
   A área deve ser expressa em cm², inferência direta da unidade fornecida no lado.

7. **Nível cognitivo dos estudantes**  
   Assumi que se trata de alunos iniciantes, portanto a tarefa deve trabalhar:
   - Leitura de dados,
   - Seleção (condicional),
   - Aplicação de fórmulas básicas,
   - Impressão formatada.

---

# Título da Tarefa

Classificação e Cálculo de Áreas de Polígonos Regulares a partir do Número de Lados e Medida do Lado

---

# Descrição da Situação-Problema

Na disciplina **Introdução à Programação**, estudantes iniciantes são apresentados a problemas que combinam raciocínio geométrico elementar com implementação de estruturas condicionais. Para fortalecer a habilidade de interpretar entradas e produzir diferentes comportamentos conforme o tipo de dado recebido, os alunos devem implementar um programa que **classifica um polígono regular** a partir do número de lados informado e, quando aplicável, calcula sua área utilizando a medida do lado fornecida.

O programa deve:

1. Ler o **número de lados** de um polígono regular (inteiro ≥ 3).  
2. Ler a **medida do lado**, em centímetros.  
3. Aplicar lógica condicional para:
   - Identificar **TRIÂNGULO** quando lados = 3 e calcular sua área utilizando a fórmula do triângulo equilátero.  
   - Identificar **QUADRADO** quando lados = 4 e calcular sua área.  
   - Identificar **PENTÁGONO** quando lados = 5, sem necessidade de cálculo de área.  
4. Exibir o nome do polígono e, quando aplicável, sua área total em **cm²**.

Entradas inválidas (como número de lados menor que 3) devem ser rejeitadas com mensagem apropriada, solicitando nova entrada.

---

# Requisitos Funcionais da Tarefa

* **RF1** — Ler o número de lados (*n*) e validar que *n ≥ 3*.  
* **RF2** — Ler a medida do lado (*l*), assumindo valores positivos em centímetros.  
* **RF3** — Classificar o polígono com base no número de lados.  
* **RF4** — Se *n = 3*, calcular a área de um triângulo equilátero:  
  \[
  A = \frac{l^2\sqrt{3}}{4}
  \]
* **RF5** — Se *n = 4*, calcular a área de um quadrado:  
  \[
  A = l^2
  \]
* **RF6** — Se *n = 5*, exibir apenas “PENTÁGONO”.  
* **RF7** — Exibir resultados no formato:  
  - `TRIÂNGULO — área = X cm²`  
  - `QUADRADO — área = Y cm²`  
  - `PENTÁGONO`

---

# Variações e Extensões (progressão de complexidade)

* **V1 (básica)** — Não realizar validação de limites; apenas classificar diretamente.  
* **V2 (intermediária)** — Adicionar validações de entrada e mensagens de erro.  
* **V3 (intermediária)** — Incluir cálculo da área do **pentágono** usando fórmula específica.  
* **V4 (avançada)** — Expandir para polígonos regulares de *n* lados utilizando fórmula geral:  
  \[
  A = \frac{n \cdot l^2}{4 \cdot \tan(\pi / n)}
  \]
* **V5 (avançada)** — Criar função modular para cálculo de áreas de polígonos arbitrários.  
* **V6 (avançada)** — Gerar representações textuais ou gráficas do polígono (ASCII art ou biblioteca gráfica).

Essas variações ampliam gradualmente o domínio conceitual e a autonomia algorítmica do estudante.

---

# Conhecimentos Relacionados (OntoKSD — Knowledge)

### Fundamentos de Programação
- Entrada e saída de dados (I/O).  
- Tipos numéricos e operações aritméticas.  
- Estruturas condicionais (if/elif/else).  
- Validação de dados.  
- Formatação de saída.  

### Geometria Computacional
- Classificação de polígonos regulares.  
- Conceito de área para figuras bidimensionais.  
- Fórmulas específicas: triângulo equilátero e quadrado.  

### Competências Computacionais Transversais
- Raciocínio lógico aplicado à seleção condicional.  
- Identificação de padrões estruturais em problemas clássicos.  
- Conversão de expressões matemáticas para código executável.

---

# Objetivos de Aprendizagem (BNCC Computação + Bloom)

### LO1 — Aplicar (nível: Aplicar – Bloom)
- Aplicar estruturas condicionais para classificar polígonos com base em propriedades numéricas.  
- Empregar fórmulas matemáticas simples na construção de algoritmos.

### LO2 — Analisar (nível: Analisar – Bloom)
- Analisar entradas e identificar valores inválidos, produzindo tratamento adequado.  
- Diferenciar casos em que cálculo de área é necessário e casos em que apenas classificação é suficiente.

### LO3 — Criar (nível: Criar – Bloom)
- Projetar uma solução que integra leitura, verificação, cálculos e apresentação final formatada.  
- Construir um programa completo que representa o raciocínio geométrico por meio de lógica computacional.

---

# Operações Cognitivas (Taxonomia de Bloom para Computação)

* **Identificar** — número de lados, unidade, tipo de polígono.  
* **Selecionar** — condição correta para cada tipo geométrico.  
* **Implementar** — regras condicionais e fórmulas de área.  
* **Calcular** — área conforme os casos previstos.  
* **Validar** — valores inválidos ou inconsistentes.  
* **Depurar** — erros de cálculo, lógica condicional ou formatação.  
* **Justificar** — escolha das fórmulas e da estrutura lógica utilizada.

---

# Competências Potenciais (modelo K—S—D)

### Conhecimentos (K)
- Conceitos de polígonos regulares.  
- Fórmulas geométricas básicas.  
- Estruturas de seleção e validação.  
- Operações matemáticas elementares.  

### Habilidades (S)
- Implementar condicionais para controlar fluxo decisório.  
- Traduzir fórmulas geométricas para expressões computacionais.  
- Tratar entradas e produzir saídas formatadas.  
- Articular conhecimento matemático e programação.

### Disposições (D)
- Rigor na associação entre definições matemáticas e seu uso em código.  
- Atenção aos detalhes na manipulação de unidades e formatos de saída.  
- Curiosidade para explorar extensões (polígonos com mais lados).  
- Persistência ao enfrentar erros lógicos ou geométricos.
