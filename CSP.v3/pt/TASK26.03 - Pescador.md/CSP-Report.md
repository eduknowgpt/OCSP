# RELATÓRIO CSP — Autoria de Competências 

## Introdução
Este relatório situa-se na fase de **Autoria de Competências** do Competency Specification Process (CSP), com o propósito de especificar, com rastreabilidade e sem redundância, os **Conhecimentos (K)**, **Objetivos de Aprendizagem (LO)** e **Competências (CT)** elicitos por uma tarefa introdutória de programação.

A tarefa consiste em desenvolver, em linguagem C, um programa que **lê um peso P (kg)**, verifica se **P excede 50 kg**, e então calcula **E (excesso)** e **M (multa)** com taxa fixa de **R$ 4,00 por quilo excedente**; caso não haja excesso, **E e M devem ser zero**. As evidências são observáveis porque o estudante produz um **artefato executável (código-fonte)** e uma **saída verificável (valores de E e M)**, acompanhados de **justificativa breve** sobre a condição e os cálculos.

O modelo **K–S–D** é apropriado porque a tarefa mobiliza: (i) **conhecimentos de Computação** (tipos, variáveis, expressões, estruturas condicionais e entrada/saída), (ii) **habilidades** de modelar, implementar e testar a solução, e (iii) **disposições** de rigor e verificabilidade necessárias para uma entrega auditável, mantendo separação clara entre conteúdo técnico e postura acadêmica.


# 1. Análise da Entidade Instrucional

## Título
**TASK26.3 — Excesso de Peso de Peixes e Multa (Linguagem C)**

## Descrição
Tarefa de programação em C em que o estudante deve:
- ler **P** (peso em kg);
- verificar a condição **P > 50**;
- calcular **E = P − 50** e **M = E × 4,00** quando houver excesso;
- caso contrário, definir **E = 0** e **M = 0**;
- apresentar os valores de **E** e **M** como resultado.

> Observação técnica conservadora (derivada da descrição pedagógica): como o enunciado não explicita se P é inteiro ou real, a solução deve admitir **P como número real**, e a apresentação de **M** deve ser coerente com valor monetário (p.ex., duas casas decimais).

## Processo de Desenvolvimento da Solução (em etapas)
1. Identificar entrada (**P**), constantes (limite **50** e taxa **4,00**) e saídas (**E**, **M**).
2. Definir variáveis numéricas para **P**, **E** e **M**.
3. Implementar a **estrutura condicional** para distinguir **P > 50** e **P ≤ 50**.
4. Atribuir valores corretos em cada alternativa (cálculo vs. zeros).
5. Exibir **E** e **M** de forma verificável (consistência entre unidades e valores).

## Resultados Esperados (lista de produtos e evidências)
- **Código-fonte em C** (compilável e executável).
- **Saída do programa** com os valores de **E (kg)** e **M (R$)**.
- **Justificativa breve** (2–5 linhas) explicando a condição e as expressões usadas para E e M.

## Contexto de Aquisição (curso, organização, ambiente, avaliação)
- **Curso/Nível:** disciplina introdutória de programação (perfil típico de ensino técnico/superior inicial).
- **Organização:** execução individual.
- **Ambiente:** laboratório (compilação/execução) ou avaliação escrita com entrega do código/algoritmo.
- **Avaliação:** baseada na correção do comportamento nos dois casos (com e sem excesso) e na justificativa concisa.

## Perfil do Público-Alvo (nível, pré-requisitos, necessidades)
- **Público:** iniciantes em programação em C.
- **Pré-requisitos mínimos:** variáveis e atribuição; operadores aritméticos e relacionais; estruturas condicionais; noções de entrada/saída.
- **Necessidades típicas:** interpretar o enunciado com precisão, garantir atribuições em todas as alternativas e manter consistência de cálculo e saída.

## Escala de Proficiência (critérios e dimensões)
Escala proposta (4 níveis) aplicada às dimensões **Técnica**, **Cognitiva** e **Atitudinal**:

- **N1 — Inicial:** erros na estrutura condicional e/ou cálculos; atribuições incompletas (variáveis sem valor em alguma alternativa); evidências pouco verificáveis; justificativa ausente/incoerente.
- **N2 — Básico:** condição e cálculos principais presentes, porém com fragilidades (p.ex., tratamento incompleto de P ≤ 50 ou inconsistências na saída); justificativa parcial.
- **N3 — Proficiente:** comportamento correto para P > 50 e P ≤ 50; cálculos consistentes; saída conferível; justificativa breve e coerente.
- **N4 — Avançado:** além do correto, demonstra rigor na apresentação (consistência numérica e monetária), clareza de constantes e justificativa tecnicamente precisa e concisa.


# 2. Enumeração de Conhecimentos

## Representação e Estado (Variáveis/Tipos)
**K1. Variáveis e atribuição (estado do programa)**
- Variáveis como armazenamento de valores associados a identificadores.
- Atribuição como atualização do estado antes da saída.
- Necessidade de atribuir valores em todas as alternativas da estrutura condicional.
- Mobilizado ao definir e atualizar **P**, **E** e **M**.

**K2. Tipos numéricos e representação de valores**
- Representação de números inteiros e reais em programas.
- Escolha de tipo numérico compatível com leitura de peso e cálculo monetário.
- Coerência de tipos em expressões aritméticas.
- Mobilizado ao representar **P**, **E** e **M**.

## Controle de Fluxo
**K3. Estruturas condicionais (seleção)**
- Avaliação de uma condição booleana e execução de uma entre alternativas de processamento.
- Tratamento explícito do caso verdadeiro e do caso falso.
- Relação entre regra do problema e seleção do caminho de execução.
- Mobilizado ao aplicar **P > 50** para decidir cálculo ou atribuição de zero.

**K4. Operadores relacionais e expressões booleanas**
- Construção de condições por comparação numérica.
- Interpretação operacional de “maior que” no contexto do programa.
- Papel da condição booleana na seleção do fluxo.
- Mobilizado na verificação **P > 50**.

## Expressões e Cálculo
**K5. Expressões aritméticas e uso de constantes**
- Construção de expressões com subtração e multiplicação.
- Uso consistente de constantes (limite 50; taxa 4,00).
- Dependência entre valores (M calculada a partir de E).
- Mobilizado em **E = P − 50** e **M = E × 4,00**.

## Interação (Entrada/Saída)
**K6. Entrada e saída padrão (conceito)**
- Leitura de um valor como entrada do programa.
- Impressão de resultados como evidência verificável.
- Coerência entre entrada, processamento e saída.
- Mobilizado ao ler **P** e exibir **E** e **M**.

**K7. Formatação de saída numérica (precisão)**
- Apresentação de números reais e controle de precisão na saída.
- Convenção de exibição de valores monetários com casas decimais.
- Separação entre valor computado e forma de apresentação.
- Mobilizado ao exibir **M** de modo conferível.

## Qualidade e Verificabilidade
**K8. Condições de contorno e comportamento esperado**
- Definição explícita do comportamento para **P ≤ 50** (sem excesso).
- Definição do comportamento para **P > 50** (com excesso).
- Importância de cobrir ambos os casos na validação.
- Mobilizado ao garantir **E=0 e M=0** quando aplicável.

### Nota Analítica
Os conhecimentos foram delimitados ao **domínio de Computação**, evitando registrar como K itens que são essencialmente **habilidades** (p.ex., “implementar”, “testar”) ou **disposições** (p.ex., “ser organizado”, “ser ético”). Essa separação sustenta rastreabilidade K→S→D nas competências.


# 3. Identificação de Objetivos de Aprendizagem (versão mais ampla e reutilizável)

**LO1.** Interpretar um enunciado e identificar informações relevantes para a solução computacional (dados de entrada, resultados esperados e regras de decisão).  
**LO2.** Selecionar e empregar tipos e variáveis adequados para representar dados e resultados em um programa.  
**LO3.** Aplicar operadores relacionais e expressões booleanas para formular condições de decisão em problemas computacionais.  
**LO4.** Utilizar estruturas condicionais para controlar o fluxo de execução e produzir resultados consistentes em cenários alternativos.  
**LO5.** Construir expressões aritméticas coerentes com a especificação do problema e manter consistência entre cálculo e resultado produzido.  
**LO6.** Produzir evidências verificáveis por meio de entrada/saída e justificar, de forma sucinta, a lógica adotada com base no comportamento esperado.


### Nota Analítica
Os LOs são observáveis e avaliáveis por meio do **código**, da **saída** e da **justificativa**. Em Bloom revisada, predominam **Aplicar** (uso de estruturas e expressões) e **Criar** quando se exige a construção do programa; **Analisar** aparece de forma moderada na justificativa e no confronto entre regra e comportamento.


# 4. Definição de Competências

## 4.1 Competência Geral 
**Competência geral do domínio:**  
Mobilizar fundamentos de programação para modelar uma regra de decisão, implementar uma solução com entrada/processamento/saída e verificar conformidade do resultado com a especificação, produzindo evidências verificáveis.

**BNCC:**  
Como a etapa (EF/EM) não está explicitada no contexto do curso, registra-se apenas correspondência em nível geral com práticas de **programação/algoritmos** e **pensamento computacional** (abstração, formalização e validação), sem uso de códigos.



## 4.2 Especificações de Competências

### CT26.3.1
#### Título da Competência
Modelar uma regra de decisão e cálculos associados em termos computacionais.

#### Descrição Textual
Traduzir um enunciado com critério e cálculo proporcional em uma especificação operacional composta por: (i) **condição de decisão**, (ii) **variáveis derivadas**, e (iii) **expressões aritméticas**, incluindo tratamento explícito do caso alternativo (sem aplicação da regra).

#### Especificação de Conhecimentos
- **K4:** formular a condição que separa os casos relevantes do problema.
- **K5:** estabelecer expressões aritméticas coerentes com constantes/taxas fornecidas.
- **K8:** explicitar o comportamento esperado quando a condição não é satisfeita.

#### Alinhamento com a Taxonomia de Bloom (revisada)
- **Analisar** (principal) e **Aplicar** (secundário).

#### Pareamento Conhecimento–Habilidade
- **K4 → S:** construir a condição booleana que discrimina os casos.
- **K5 → S:** formular expressões corretas para as variáveis de saída.
- **K8 → S:** definir resultado/atribuições completas para o caso alternativo.

#### Anotação de Verbos (lista)
modelar, formalizar, discriminar, estabelecer, derivar, especificar

#### Especificação de Disposições
- Rigor na interpretação do enunciado.
- Precisão no uso de constantes e relações de cálculo.
- Postura de verificabilidade (casos e resultados explicitados).
- Responsabilidade acadêmica na justificativa sucinta.

#### Competências Alinhadas à BNCC (quando aplicável)
Alinhamento geral com abstração e formalização em pensamento computacional e programação/algoritmos, sem códigos.

#### Tabela-Resumo
| Código     | Competência                                                 | Disposições                                    | Conhecimento | Habilidade |
|-----------|--------------------------------------------------------------|-----------------------------------------------|--------------|-----------|
| CT26.3.1  | Modelar regra de decisão e cálculos em termos computacionais | rigor; precisão; verificabilidade; responsabilidade | K4, K5, K8   | formalizar condição e expressões; discriminar casos |

#### Definição de Ativação
- **Restrição de ativação:** obrigatória  
- **Modo de ativação:** analítica  
- **Função de ativação:** núcleo  
- **Justificativa:** a tarefa depende de traduzir o enunciado em condição e expressões; essa modelagem sustenta a implementação e a conferência de E e M.

---

### CT26.3.2
#### Título da Competência
Implementar em C a solução com variáveis, atribuições e estruturas condicionais.

#### Descrição Textual
Construir um programa em C que leia **P**, mantenha o estado por meio de variáveis **E** e **M**, aplique a **estrutura condicional** e atribua valores corretos em cada alternativa, produzindo um artefato executável.

#### Especificação de Conhecimentos
- **K1:** estruturar o estado do programa com P, E e M e garantir atribuição completa.
- **K2:** selecionar tipos numéricos compatíveis com o domínio do peso e do valor monetário.
- **K3:** implementar a estrutura condicional para executar cálculo ou atribuição de zero.
- **K6:** integrar leitura de P e apresentação de E e M ao fluxo do programa.

#### Alinhamento com a Taxonomia de Bloom (revisada)
- **Criar** (principal) e **Aplicar** (secundário).

#### Pareamento Conhecimento–Habilidade
- **K3 → S:** implementar a **estrutura condicional** com execução correta de cada alternativa.
- **K1 → S:** atribuir e manter valores de E e M de forma consistente.
- **K2 → S:** escolher representação numérica adequada para P, E e M.
- **K6 → S:** integrar entrada (P) e saída (E, M) ao fluxo do programa.

#### Anotação de Verbos (lista)
implementar, programar, construir, integrar, atribuir, inicializar, compilar

#### Especificação de Disposições
- Disciplina de conferir completude (variáveis definidas/atribuídas em todas as alternativas).
- Atenção à consistência entre leitura, cálculo e saída.
- Persistência diante de erros de compilação/execução (postura responsável de depuração).
- Clareza na estrutura do artefato entregue.

#### Competências Alinhadas à BNCC (quando aplicável)
Alinhamento geral com programação/algoritmos, sem códigos.

#### Tabela-Resumo
| Código     | Competência                                                      | Disposições                                           | Conhecimento       | Habilidade |
|-----------|-------------------------------------------------------------------|------------------------------------------------------|--------------------|-----------|
| CT26.3.2  | Implementar em C solução com variáveis e estruturas condicionais   | completude; consistência; persistência; clareza      | K1, K2, K3, K6     | programar solução; integrar I/O; garantir atribuições |

#### Definição de Ativação
- **Restrição de ativação:** obrigatória  
- **Modo de ativação:** construtiva  
- **Função de ativação:** núcleo  
- **Justificativa:** o produto central é o programa em C; a competência se evidencia diretamente na construção do artefato executável com leitura, decisão e atribuições corretas.

---

### CT26.3.3
#### Título da Competência
Realizar testes sistemáticos da solução para verificar conformidade com a especificação.

#### Descrição Textual
Planejar e executar testes da solução em **casos representativos e de contorno**, incluindo situações em que a condição de excesso não se aplica e em que se aplica, verificando a conformidade dos valores produzidos (E e M) com a regra definida e garantindo que a saída seja conferível.

#### Especificação de Conhecimentos
- **K8:** selecionar e distinguir casos sem aplicação da regra e com aplicação da regra.
- **K5:** conferir consistência aritmética dos cálculos.
- **K6:** observar e interpretar a saída como evidência do comportamento.
- **K7:** assegurar apresentação numérica que favoreça a conferência.

#### Alinhamento com a Taxonomia de Bloom (revisada)
- **Aplicar** (principal) e **Analisar** (secundário).

#### Pareamento Conhecimento–Habilidade
- **K8 → S:** selecionar casos de teste e verificar conformidade por caso.
- **K5 → S:** conferir cálculos e dependências entre variáveis de saída.
- **K6 → S:** coletar evidências na saída e interpretar resultados.
- **K7 → S:** validar a apresentação numérica para suportar auditoria.

#### Anotação de Verbos (lista)
testar, verificar, validar, comparar, conferir, evidenciar, interpretar

#### Especificação de Disposições
- Postura de verificação (não assumir correção sem testar casos relevantes).
- Precisão com detalhes numéricos e unidades.
- Transparência: evidências apresentadas de modo auditável.
- Responsabilidade ao relacionar resultado e especificação.

#### Competências Alinhadas à BNCC (quando aplicável)
Alinhamento geral com validação de algoritmos simples, sem códigos.

#### Tabela-Resumo
| Código     | Competência                                              | Disposições                                         | Conhecimento       | Habilidade |
|-----------|-----------------------------------------------------------|----------------------------------------------------|--------------------|-----------|
| CT26.3.3  | Realizar testes sistemáticos e verificar conformidade      | verificação; precisão; transparência; responsabilidade | K5, K6, K7, K8     | planejar/realizar testes; comparar esperado vs. observado |

#### Definição de Ativação
- **Restrição de ativação:** obrigatória  
- **Modo de ativação:** analítica  
- **Função de ativação:** apoio  
- **Justificativa:** a tarefa exige correção para casos distintos (P > 50 e P ≤ 50); testes sistemáticos sustentam evidência de conformidade e reforçam a confiabilidade da solução.

---

### CT26.3.4
#### Título da Competência
Justificar a solução com base em evidências do raciocínio (condição e cálculos).

#### Descrição Textual
Produzir justificativa breve e tecnicamente coerente que conecte a condição aplicada, as expressões de cálculo e os resultados apresentados, tornando explícita a compreensão do comportamento do programa.

#### Especificação de Conhecimentos
- **K3:** explicar como a estrutura condicional seleciona o caminho de execução.
- **K5:** explicar a origem e o papel das expressões aritméticas.
- **K1:** explicar a atribuição de zero no caso sem excesso.
- **K8:** explicar a distinção entre os casos do problema.

#### Alinhamento com a Taxonomia de Bloom (revisada)
- **Analisar** (principal) e **Aplicar** (secundário).

#### Pareamento Conhecimento–Habilidade
- **K3 → S:** descrever o critério de decisão e seu efeito no fluxo.
- **K5 → S:** justificar o cálculo de E e M a partir de constantes e operações.
- **K1 → S:** justificar atribuições em cada alternativa (incluindo zeros).
- **K8 → S:** articular os casos e os resultados esperados.

#### Anotação de Verbos (lista)
justificar, explicar, relacionar, evidenciar, descrever, fundamentar

#### Especificação de Disposições
- Honestidade acadêmica (explicação própria e coerente com o artefato).
- Clareza e concisão na argumentação técnica.
- Compromisso com verificabilidade (explicar de modo conferível).
- Rigor terminológico (uso correto de “condição”, “excesso”, “multa”, “atribuição”).

#### Competências Alinhadas à BNCC (quando aplicável)
Alinhamento geral com explicação de algoritmos simples e comunicação do raciocínio computacional, sem códigos.

#### Tabela-Resumo
| Código     | Competência                                           | Disposições                                      | Conhecimento     | Habilidade |
|-----------|--------------------------------------------------------|--------------------------------------------------|------------------|-----------|
| CT26.3.4  | Justificar solução com evidências (condição e cálculos) | honestidade; clareza; verificabilidade; rigor    | K1, K3, K5, K8   | explicar fluxo e fórmulas; fundamentar resultados |

#### Definição de Ativação 
- **Restrição de ativação:** obrigatória  
- **Modo de ativação:** justificatória  
- **Função de ativação:** apoio  
- **Justificativa:** a justificativa breve é uma evidência prevista na tarefa e complementa o código/saída ao tornar explícita a compreensão sobre condição, cálculos e casos.

