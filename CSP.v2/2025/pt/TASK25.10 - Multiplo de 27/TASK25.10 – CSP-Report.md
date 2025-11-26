# TASK25.10 – CSP – Verificação de Múltiplo de 27 em C

# 1. Introdução
Este relatório apresenta a especificação formal de competências (CSP – *Competency Specification Protocol*) para a tarefa **“Verificar se um número inteiro e positivo é múltiplo de 27, utilizando linguagem C”**.  
A tarefa situa-se no contexto de formação inicial em programação e tem como objetivo consolidar conhecimentos fundamentais sobre entrada de dados, operações aritméticas e estruturas condicionais, articulados com competências computacionais essenciais.

O CSP aqui definido identifica as competências demandadas pela tarefa, seus conhecimentos associados, disposições socioemocionais, alinhamento à BNCC e tabela de síntese técnica. O documento segue metodologia padronizada para garantir clareza, granularidade adequada e rastreabilidade pedagógica.

# 2. Análise da Entidade Instrucional
A tarefa constitui uma **entidade instrucional elementar**, de baixa complexidade algorítmica, porém de alta relevância conceitual para o desenvolvimento de raciocínio computacional inicial. Ela envolve:

- Extração e validação de entrada fornecida pelo usuário;  
- Compreensão da operação módulo como mecanismo de verificação de múltiplos;  
- Formulação de condições lógicas para tomada de decisão;  
- Comunicação correta de resultados;  
- Raciocínio sequencial e capacidade de teste.

A atividade configura etapa fundamental da formação introdutória de estudantes que iniciam estudos em linguagem C.

# 3. Enumeração dos Conhecimentos
1. Entrada e saída em C (`scanf`, `printf`)  
2. Tipos de dados inteiros e regras de uso  
3. Operador módulo (%) e propriedades aritméticas de múltiplos  
4. Estruturas condicionais (`if/else`)  
5. Validação de entrada e controle de fluxo simples  
6. Construção lógica de algoritmos sequenciais  

# 4. Objetivos de Aprendizagem
- Ler, validar e processar valores inteiros positivos em C;  
- Aplicar o operador módulo para verificar múltiplos;  
- Estruturar condições que determinem comportamentos distintos conforme a entrada;  
- Projetar e implementar algoritmos simples seguindo boas práticas;  
- Explicar, justificar e rastrear o funcionamento da solução implementada;  
- Adotar postura ética, organizada e responsável no desenvolvimento da tarefa.

# 5. Especificação das Competências (CSP)

# Competência 1 - 25.10.1
## Título
Aplicar operadores aritméticos para verificar múltiplos.

## Descrição Textual
A competência consiste em utilizar corretamente o operador módulo (%) na linguagem C para determinar se um número é múltiplo de outro. Essa habilidade envolve compreender o conceito matemático de resto da divisão inteira, traduzindo-o para o domínio computacional, e aplicar essa operação em condições lógicas capazes de produzir decisões corretas no programa.

## Conhecimentos Necessários

### Operador Módulo e Propriedades Aritméticas  
- Descrição: Compreensão de como o operador `%` determina o resto e como isso caracteriza múltiplos.  
- Bloom: Aplicar  
- Verbos: Calcular, Aplicar, Relacionar

### Aritmética Inteira  
- Descrição: Operações básicas e comportamento de números inteiros na linguagem C.  
- Bloom: Compreender  
- Verbos: Interpretar, Explicar, Identificar

## Disposições
- Precisão  
- Rigor lógico  
- Clareza no raciocínio  

## BNCC – Alinhamento
- EM13CO03  
- Competência Geral de Computação 3  

## Tabela Resumo
| Code        | Competency                                           | Dispositions                 | Conhecimento                        | Habilidade                          |
|-------------|-------------------------------------------------------|-------------------------------|----------------------------------|--------------------------------|
| 25.10.1 | Aplicar operadores aritméticos para verificar múltiplos | Precisão, Rigor lógico, Clareza | Operador Módulo e Propriedades | Aplicar (Calcular, Aplicar)   |
| . |  |  | Aritmética Inteira             | Compreender (Interpretar, Explicar) |

---

# Competência 2 - 25.10.2
## Título
Implementar estruturas condicionais para tomada de decisão.

## Descrição Textual
A competência refere-se à habilidade de construir decisões computacionais usando estruturas condicionais (`if/else`). Envolve analisar condições booleanas, organizar fluxos de execução e determinar respostas adequadas com base no estado da entrada.

## Conhecimentos Necessários

### Estruturas Condicionais (`if/else`)  
- Descrição: Sintaxe, semântica e uso estratégico de condições na linguagem C.  
- Bloom: Aplicar  
- Verbos: Decidir, Comparar, Implementar

### Expressões Booleanas  
- Descrição: Formulação de expressões lógicas que determinem caminhos de execução.  
- Bloom: Analisar  
- Verbos: Avaliar, Determinar, Relacionar

## Disposições
- Pensamento estruturado  
- Consistência lógica  
- Responsabilidade técnica  

## BNCC – Alinhamento
- EM13CO04  
- Competência Geral de Computação 4  

## Tabela Resumo
| Code         | Competency                                             | Dispositions                       | Conhecimento               | Habilidade                                    |
|--------------|---------------------------------------------------------|-------------------------------------|-------------------------|-------------------------------------------|
| 25.10.2 | Implementar estruturas condicionais para tomada de decisão | Pensamento estruturado, Consistência, Responsabilidade | Estruturas Condicionais | Aplicar (Decidir, Implementar)            |
| . |  |  | Expressões Booleanas   | Analisar (Avaliar, Determinar)            |

---

# Competência 3 - 25.10.3
## Título
Validar entradas numéricas conforme requisitos do programa.

## Descrição Textual
Esta competência refere-se à capacidade de analisar entradas fornecidas pelo usuário, verificando se atendem aos requisitos do problema (números inteiros positivos). Envolve identificar condições inválidas, aplicar estratégias de correção ou notificação e garantir robustez mínima da aplicação.

## Conhecimentos Necessários

### Validação de Entrada  
- Descrição: Estratégias de verificação e filtragem de valores incorretos.  
- Bloom: Avaliar  
- Verbos: Verificar, Avaliar, Detectar

### Controle de Fluxo Simples  
- Descrição: Caminhos alternativos diante de entradas inválidas.  
- Bloom: Aplicar  
- Verbos: Executar, Controlar, Selecionar

## Disposições
- Responsabilidade  
- Atenção aos detalhes  
- Perseverança na depuração  

## BNCC – Alinhamento
- EM13CO05  
- Competência Geral de Computação 5  

## Tabela Resumo
| Code           | Competency                                   | Dispositions                           | Knowledge            | Skill                                |
|----------------|-----------------------------------------------|-----------------------------------------|-----------------------|----------------------------------------|
| 25.10.3 | Validar entradas numéricas conforme requisitos | Responsabilidade, Atenção, Perseverança | Validação de Entrada | Avaliar (Verificar, Detectar)         |
| . |  |  | Controle de Fluxo    | Aplicar (Executar, Selecionar)        |

---

# Competência 4 - 25.10.4
## Título
Construir algoritmos sequenciais simples com clareza e correção.

## Descrição Textual
A competência consiste em projetar e implementar algoritmos lineares simples, articulando entrada, processamento e saída dentro de uma lógica coerente. Inclui formular pseudocódigo, estabelecer etapas mínimas de raciocínio e traduzir essas etapas para código C com precisão.

## Conhecimentos Necessários

### Estrutura Sequencial de Programas  
- Descrição: Compreensão do fluxo linear de execução.  
- Bloom: Compreender  
- Verbos: Descrever, Explicar, Organizar

### Modelagem Algorítmica Básica  
- Descrição: Representação lógica em pseudocódigo ou fluxograma.  
- Bloom: Criar  
- Verbos: Elaborar, Planejar, Estruturar

## Disposições
- Organização  
- Clareza comunicativa  
- Autonomia intelectual  

## BNCC – Alinhamento
- EM13CO02  
- Competência Geral de Computação 2  

## Tabela Resumo
| Code            | Competency                                          | Dispositions                         | Knowledge                       | Skill                                 |
|------------------|------------------------------------------------------|---------------------------------------|----------------------------------|-----------------------------------------|
| 25.10.4  | Construir algoritmos sequenciais simples             | Organização, Clareza, Autonomia       | Estrutura Sequencial            | Compreender (Descrever, Explicar)       |
| .   |              |        | Modelagem Algorítmica           | Criar (Elaborar, Planejar, Estruturar)  |



# 6. Conclusão
Este relatório CSP sistematiza as competências essenciais envolvidas na tarefa de verificar se um número é múltiplo de 27 utilizando linguagem C.
