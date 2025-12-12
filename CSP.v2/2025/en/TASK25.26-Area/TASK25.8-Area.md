# **TASK25.8: Classificação e Cálculo de Áreas de Polígonos Regulares**

## **1. Problema**

Os aprendizes devem desenvolver um **programa** que, a partir de duas entradas do usuário:
   1. O **número de lados** de um polígono regular;
   2. A **medida do lado** (em centímetros);

realize:

* A **classificação** do polígono entre três casos possíveis:

  * 3 lados → TRIÂNGULO
  * 4 lados → QUADRADO
  * 5 lados → PENTÁGONO

* E **calcule e imprima a área**, quando aplicável (triângulo ou quadrado).

O foco principal é a **formulação algorítmica**, o uso adequado de **estruturas condicionais**, a **seleção de fórmulas**, a **representação computacional de dados** e a **organização lógica da solução**.


## **2. Requisitos Funcionais da Tarefa**

### **RF1 — Ler entradas do usuário**

* Receber um inteiro representando o número de lados (*n*).
* Receber um valor real representando a medida do lado (*l*).

### **RF2 — Classificar o polígono**

* Identificar o tipo de polígono com base em *n* (3, 4 ou 5).
* Exibir a respectiva classificação.

### **RF3 — Calcular a área (quando aplicável)**

* Se *n = 3*: calcular área do triângulo equilátero.
* Se *n = 4*: calcular área do quadrado.
* Se *n = 5*: apenas informar “PENTÁGONO” (sem área).

### **RF4 — Validar o número de lados**

* Garantir que apenas valores **3, 4 ou 5** sejam aceitos.
* Para qualquer outro valor, exibir mensagem adequada e solicitar correção (opcional, dependendo da variação escolhida).

### **RF5 — Exibir a saída formatada**

* Exibir tipo de polígono.
* Exibir a área quando o cálculo for aplicável, com formatação adequada.



## **3. Variações e Extensões (Progressão Cognitiva e Reuso de Competências)**

### **V1 – Básica**

* Não realizar validação de dados; apenas classificar e/ou calcular área.

### **V2 – Intermediária**

* Validar que o número de lados pertence ao conjunto {3,4,5}.
* Tratar entradas inválidas com mensagens informativas.

### **V3 – Intermediária/Avançada**

* Encapsular o cálculo da área em **funções específicas** para cada polígono suportado.

### **V4 – Avançada**

* Estender para polígonos regulares de *n* lados usando a fórmula genérica.

### **V5 – Avançada**

* Criar um menu interativo; permitir múltiplas consultas.


# **4. Conhecimentos Relacionados (Foco em Computação)**

## **Fundamentos de Programação**

* Tipos de dados (inteiro e real).
* Entrada e saída padrão (leitura e impressão).
* Estruturas condicionais (`if/elif/else`).
* Operações aritméticas.
* Organização lógica do programa (sequência, seleção).

## **Abstração e Modelagem Computacional**

* Modelos de decisão baseados em condições.
* Mapeamento entre domínios reais (polígonos) e representações computacionais (inteiros e fórmulas).
* Seleção de caminhos de execução conforme classificações de entrada.

## **Boas Práticas de Programação**

* Clareza e organização do código.
* Nomes adequados para variáveis e intermediários.
* Modularização (nas variações avançadas).


# **5. Objetivos de Aprendizagem (LOs)**

Alinhados com a BNCC–Computação e com verbos da Taxonomia de Bloom revisada para Computação.

### **LO1 — Compreender**
* Interpretar a relação entre número de lados e tipo de polígono.
* Compreender como fórmulas matemáticas são traduzidas para operações computacionais.

### **LO2 — Aplicar**
* Aplicar estruturas condicionais para selecionar comportamentos diferentes do programa.
* Aplicar operações aritméticas para obter a área.

### **LO3 — Analisar**
* Identificar entradas inválidas e determinar o fluxo adequado para tratá-las.
* Comparar diferentes caminhos de execução conforme o número de lados.

### **LO4 — Criar**
* Construir uma solução algorítmica completa que lê dados, processa condições e apresenta saídas.
* Criar funções específicas para cálculos (nas variações avançadas).


# **6. Processo de Desenvolvimento Esperado (para análise pelo CSP)**

O aprendiz deverá:

1. **Analisar o enunciado** para identificar entradas, restrições e saídas.
2. **Representar computacionalmente** os casos (3,4,5 lados).
3. **Selecionar** as estruturas de decisão necessárias para discriminar corretamente cada caso.
4. **Aplicar** fórmulas matemáticas dentro da lógica computacional.
5. **Validar** entradas inválidas (de acordo com a variação usada).
6. **Testar** o programa com diferentes conjuntos de valores.
7. **Refinar** a solução para melhorar clareza, modularização ou robustez.


# **7. Perfil do Público-Alvo**

* Estudantes iniciantes (1º semestre).
* Conhecimento prévio básico em algoritmos e estruturas condicionais.
* Aprendidos em contexto de disciplina de programação introdutória.

# **8. Resultados Esperados**

Os aprendizes devem ser capazes de:

* Implementar código **correto, claro e modular**.
* Formular soluções computacionais baseadas em **decisão** e **seleção**.
* Integrar **operações aritméticas** simples no fluxo do programa.
* Demonstrar domínio das competências essenciais de **lógica, abstração e controle de fluxo**.



# **9. Fórmulas Gerais e Cálculos**

A área de um polígono regular com `n` lados e lado `l` é:

```
A = n * l^2 / (4 * tan(pi / n))
```

## Triângulo equilátero (n = 3)

```
A = (sqrt(3) / 4) * l^2
```



## Quadrado (n = 4)

**Fórmula final (quadrado):**
```
A = l^2
```

