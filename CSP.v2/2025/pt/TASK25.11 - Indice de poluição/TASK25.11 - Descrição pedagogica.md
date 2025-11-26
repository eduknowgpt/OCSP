# TASK – Sistema de Notificação de Poluição Industrial
> Criador: Prof. MS. Marcos Bião, Univasf – Campus Salgueiro

## 1. Problema

No contexto da **Lógica de Programação** em um curso introdutório de Computação, os estudantes devem elaborar um programa, em linguagem **C**, capaz de:

- **Ler um índice de poluição** medido pela Secretaria de Meio Ambiente;
- **Comparar** o valor lido com faixas predefinidas;
- **Determinar** quais grupos de indústrias (1º, 2º e 3º grupo) devem **suspender** suas atividades de acordo com o nível de poluição;
- **Emitir mensagens** adequadas ao usuário.

O índice considerado aceitável varia entre **0,05 e 0,25**. Acima disso:

| Índice de poluição | Grupos que devem ser notificados |
|--------------------|----------------------------------|
| ≥ 0,30             | 1º grupo                         |
| ≥ 0,40             | 1º e 2º grupos                   |
| ≥ 0,50             | Todos os grupos                  |

A tarefa exige compreensão das relações lógicas entre valores numéricos, uso de condicionais encadeadas e clareza na comunicação dos resultados, constituindo um problema clássico de tomada de decisão algorítmica.

## 2. Processo

1. **Identifique os requisitos** do problema (faixas, limites, mensagens).
2. **Represente a lógica em pseudocódigo**, fluxograma ou descrição passo a passo.
3. **Implemente** a estrutura condicional adequada em C.
4. **Teste** variados valores de entrada: abaixo da faixa, nas margens (0,30 – 0,40 – 0,50), acima do limite.
5. **Documente** brevemente seu raciocínio e as escolhas da implementação.

### Evidências coletadas

- Código-fonte em C, organizado e identado;
- Relatório ou explicação oral sobre:
  - Como o programa interpreta uma faixa numérica;
  - Por que a ordem dos testes condicionais importa;
  - Estratégia adotada para garantir clareza nas mensagens.

### Critérios de Avaliação

**1. Critério Técnico**
- Uso correto de `float` ou `double`;  
- Condicionais corretas e bem ordenadas;  
- Mensagens adequadas e alinhadas ao enunciado;  
- Compilação e execução sem erros.

**2. Critério Cognitivo**
- Clareza na explicação das condições;  
- Justificativa da estrutura escolhida;  
- Entendimento de limites (≥ vs >).

**3. Critério Atitudinal**
- Organização e cuidado na elaboração do código;  
- Demonstração de autonomia;  
- Atenção aos detalhes e responsabilidade na apresentação.

## 3. Contexto de Aquisição

A tarefa desenvolve competências essenciais para o início da formação em Computação:

- **Tomada de decisão com estruturas condicionais**;
- **Interpretação de dados reais** (índices ambientais);
- **Construção de modelos lógicos baseados em faixas e regras**;
- **Conexão entre computação e responsabilidade socioambiental**.

Pode ser utilizada como:

- Exercício individual em laboratório;
- Atividade avaliativa;
- Situação-problema introduzindo temas ambientais e computacionais.

## 4. Perfil do Público-Alvo

- **Nível educacional:** estudantes de 1º semestre de Computação.
- **Competências prévias esperadas:**  
  - Noções básicas de variáveis e tipos;  
  - Comparações;  
  - Entrada e saída básicas.
- **Perfil típico:** iniciantes que necessitam de exemplos concretos e contextualizados.
- **Postura desejada:** curiosidade, atenção às regras e engajamento.

## 5. Escala de Proficiência

### Básico
- Código parcial;  
- Erros de faixa;  
- Explicações frágeis.

### Proficiente
- Código correto e completo;  
- Lógica bem estruturada;  
- Explicação clara.

### Avançado
- Código robusto e comentado;  
- Tratamento de erros;  
- Justificativa das escolhas lógicas.

## 6. Resultados Esperados

O estudante deve ser capaz de:

- Implementar **estruturas condicionais múltiplas e encadeadas**;  
- Traduzir um problema real para regras algorítmicas;  
- Escolher adequadamente a ordem das verificações;  
- Documentar e justificar a solução;  
- Relacionar lógica computacional com problemas ambientais reais.
