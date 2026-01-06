# CSP_Adjustments — Ajustes de Especificação de Competências  
## TASK25.00 — Coleção de Músicas


## 1. Contextualização dos Ajustes

Este documento registra os **ajustes realizados no CSP da TASK25.00 — Coleção de Músicas** após a conclusão da **Fase 2 (Expert Review)** e a consolidação do **CSRP-Report**, conforme previsto no **Competency Specification Process (CSP)**.

Os ajustes aqui descritos resultam de uma **análise técnica do artefato de especificação de competências**, considerando:

- comentários agregados de revisores especialistas;
- coerência epistemológica entre tarefa, objetivos de aprendizagem e competências;
- observabilidade das evidências exigidas;
- necessidade de reduzir ambiguidades semânticas e sobreposição de escopo.

Em conformidade com o **TCLE adotado**, os ajustes não se baseiam em dados pessoais, avaliações de desempenho ou análises individualizadas, mas exclusivamente em **refinamentos conceituais do modelo de competências**.




## 2. Ajustes em Competências Reutilizadas

### 2.1 C04 — *Define Regular Expressions for Finite Automata*

- **Ajuste aplicado:**  
  - Restrição explícita do escopo ao **nível conceitual e algébrico**.
  - Exclusão de qualquer expectativa de construção de autômatos.
- **Resultado:**  
  Competência mantida como **core**, em modo *artifact-oriented*.



### 2.2 C14 — *Differentiate classifications of formal grammars*

- **Ajuste aplicado:**  
  - Reclassificação explícita como competência de **extensão**.
  - Definição de ativação **opcional**, em modo analítico.
- **Resultado:**  
  Uso controlado, sem gerar exigências construtivas.



### 2.3 C13′ — *Interpret and apply algebraic notation for strings and languages*

- **Ajuste aplicado:**  
  - Consolidação como competência **core transversal**.
  - Explicitação de que cobre notações algébricas de cadeias e linguagens, excluindo gramáticas.
- **Resultado:**  
  Competência estabilizada, sem alterações estruturais adicionais.



### 2.4 C05′ — *Write mathematically rigorous answers*

- **Ajuste aplicado:**  
  - Reforço do papel como competência **transversal de evidência**.
  - Ênfase na distinção entre definição, exemplo e justificativa formal.
- **Resultado:**  
  Competência mantida, sem ajustes adicionais.



## 3. Introdução e Refinamento de Novas Competências

### 3.1 C17 — *Apply operations on formal languages*

- **Motivação do ajuste:**  
  Necessidade de centralizar a aplicação e análise de operações formais.
- **Ajustes realizados:**  
  - Delimitação explícita do escopo ao **nível conceitual e algébrico**.
  - Inclusão da análise de **efeitos estruturais e propriedades de fechamento**.
- **Ativação final:**  
  - Role: `core`  
  - Mode: `analytical`  
  - Constraint: `mandatory`



### 3.2 C18 — *Model real-world problems using formal language concepts*

- **Motivação do ajuste:**  
  Tornar explícita a fase de abstração e modelagem.
- **Ajustes realizados:**  
  - Separação clara entre modelagem, operações e transformações.
- **Ativação final:**  
  - Role: `core`  
  - Mode: `constructive`  
  - Constraint: `mandatory`



### 3.3 C19 — *Apply homomorphisms in formal languages*

- **Motivação do ajuste:**  
  Explicitar codificações e limites de equivalência formal.
- **Ajustes realizados:**  
  - Restrição do escopo à análise conceitual.
  - Classificação como competência de suporte.
- **Ativação final:**  
  - Role: `supporting`  
  - Mode: `interpretative`  
  - Constraint: `mandatory`



## 4. Ajustes na Competência Composta

### 4.1 C20 — *Model and analyze musical collections as formal languages*

- **Ajuste aplicado:**  
  - Consolidação como competência **composta de nível de tarefa**.
  - Exclusão de qualquer expectativa de evidência independente.
- **Relações definidas:**  

 ```
  C20 composes C18
  C20 composes C17
  C20 composes C19
  C20 composes C04
  C20 composes C13′
  C20 composes C05′
```


## 5. Ajustes de Ativação (Role, Mode, Constraint)

Após os ajustes, as ativações foram estabilizadas conforme a tabela a seguir:

| Competência | Role        | Mode              | Constraint |
| ----------- | ----------- | ----------------- | ---------- |
| C17         | core        | analytical        | mandatory  |
| C18         | core        | constructive      | mandatory  |
| C19         | supporting  | interpretative    | mandatory  |
| C04         | core        | artifact-oriented | mandatory  |
| C13′        | core        | analytical        | mandatory  |
| C05′        | transversal | justificatory     | mandatory  |
| C14         | extension   | analytical        | optional   |
| C20         | core        | integrative       | mandatory  |



## 7. Impacto dos Ajustes no CSP da TASK25.00

Os ajustes registrados resultaram em:

* maior clareza semântica entre **modelagem, operação e transformação**;
* eliminação de competências com **evidência não observável**;
* redução de sobreposição conceitual;
* alinhamento mais estrito entre **tarefa, LOs e competências**;
* melhoria da rastreabilidade ontológica para a **OntoKSD**.




