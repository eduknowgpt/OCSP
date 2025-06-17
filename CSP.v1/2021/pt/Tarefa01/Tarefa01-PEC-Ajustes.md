# Relatório de Resultados da Revisão e Ajustes da Especificação de Competências: Tarefa01 - A Máquina de Refrigerantes e Lanches

## **Introdução**  

O processo de revisão, baseado nos feedbacks dos especialistas **P1 e P2**, identificou **áreas-chave para aprimoramento** no modelo de especificação de competências. Essas percepções foram categorizadas em **cinco temas principais**:  
- **Granularidade do Conhecimento** → Garantir um nível adequado de detalhamento.  
- **Adequação do Conhecimento** → Alinhar as competências com conhecimentos relevantes e aplicáveis.  
- **Vocabulário Controlado** → Padronizar a terminologia para melhorar a consistência.  
- **Verbos da Taxonomia de Bloom** → Melhorar a clareza na descrição das habilidades.  
- **Clareza Textual** → Refinar descrições para evitar ambiguidades.  

Com base nessas recomendações, **vários aprimoramentos foram implementados** para melhorar a especificidade, clareza e reutilização das competências.  



## **Resultados da Revisão e Ajustes Implementados**  

### **Aprimoramento da Granularidade do Conhecimento**  
Com base nas observações dos revisores, **o sistema de classificação do conhecimento foi atualizado de CC2012 para CS2013**, que oferece uma taxonomia mais **detalhada** e **hierárquica**. Essa mudança garante **maior especificidade**, tornando as competências **mais reutilizáveis** e **melhor alinhadas às tarefas educacionais**.  

### **Ajustes Específicos nas Competências**  

- **Competência A: "Desenvolver Soluções de Problemas Usando Autômatos"**  
  - O elemento de conhecimento **"Autômato Finito"** foi **redefinido** como **"Máquinas de Estados Finitos"**.  
  - **"Análise de Requisitos"** foi **redefinido** como **"Engenharia de Requisitos"**.  
 

- **Competência B: "Determinar Quando Usar um DFA ou um NFA"**  
  - O título da competência foi **redefinido** como **"Justificar o Uso de Autômatos Finitos Determinísticos (DFA)"**.  
  - O conhecimento **"Autômato Finito"** foi **redefinido** como **"Autômatos Finitos Determinísticos (DFA)"**.  
  - **"Análise de Requisitos"** foi **redefinido** como **"Engenharia de Requisitos"**.  
  - Um novo **par conhecimento-habilidade** foi adicionado: **"Pensamento Analítico e Crítico (FPK) - Aplicar"**, ampliando a clareza e profundidade da competência.  

- **Competência C: "Testar Autômatos Usando Simuladores"**  
  - O **elemento de conhecimento "Autômatos sobre Objetos Infinitos" foi substituído por "Máquinas de Estados Finitos"** para melhorar a clareza. 
  - Um **novo par conhecimento-habilidade foi introduzido** → **"Modelagem e Simulação - Aplicar"**, garantindo que os estudantes apliquem seus conhecimentos de modelagem ao testar autômatos com simuladores.  

- **Competências D e E: Fusão e Aprimoramento**  
   - As competências **"Determinar Expressões Regulares que Representam Autômatos"** e **"Relacionar Expressões Regulares com Autômatos Finitos"** foram **fundidas** em uma **única competência**: **"Definir Expressões Regulares para Autômatos Finitos."**  
  - Ajustes no conhecimento incluíram:  
    - **"Autômato Finito - Compreender"** foi **redefinido** como **"Máquinas de Estados Finitos - Compreender."**  
    - **"Linguagens Regulares - Compreender"** foi **redefinido** como **"Expressões Regulares - Aplicar."**  
    - **"Pensamento Analítico e Crítico (FPK)"** permaneceu **inalterado**.  

- **Competência F: "Escrita Colaborativa de Relatório Técnico"**  
  - A competência foi **redefinida** como **"Escrever um Relatório Técnico."**  
  - O conhecimento **"Relatório Técnico"** foi **redefinido** como **"Comunicação Escrita (FPK)."**  
  - O nível da Taxonomia de Bloom permaneceu **"Aplicar" (Escrever, Estruturar, Revisar, Refinar).**  



### **Padronização do Vocabulário Controlado**  
Tanto P1 quanto P2 enfatizaram que o **uso de múltiplos verbos** nas descrições das competências é **benéfico**, pois **esclarece as ações esperadas** para cada par conhecimento-habilidade. A padronização do **vocabulário controlado** assegura **maior consistência** e **alinhamento com os objetivos de aprendizagem predefinidos**.  

Para ampliar ainda mais a clareza, será estabelecido um **mapeamento estruturado do vocabulário**, definindo **termos preferenciais e sinônimos** para **manter coerência entre diferentes especificações de competências**.  





## **Ajustes nas Especificações de Competências**

## **Especificação da Competência A**

### A.1 Título da Competência

    Desenvolver soluções de problemas usando Autômatos

### A.2 Descrição da Competência

Esta competência se refere à capacidade de **projetar, construir e validar soluções baseadas em autômatos** que resolvam problemas computacionais bem definidos. Espera-se que os estudantes interpretem os requisitos do sistema e modelem comportamentos utilizando **máquinas de estados finitos**, aplicando métodos formais para garantir a **consistência lógica e a correção operacional**.

Os estudantes devem:

* **Traduzir especificações de problemas em modelos de autômatos** com estados e transições.
* **Implementar autômatos usando ferramentas apropriadas**, garantindo que seu comportamento esteja alinhado à lógica do sistema.
* **Refinar e testar o autômato** por meio de simulação, tratando casos extremos e melhorando a robustez.
* **Integrar restrições ou extensões** quando necessário, demonstrando flexibilidade e capacidade de adaptação na resolução de problemas.



## **Especificação da Competência B**

### B.1 Título da Competência

    Justificar o uso de Autômatos Finitos Determinísticos (DFAs)

### B.2 Descrição da Competência

Esta competência foca na capacidade dos estudantes de **distinguir entre autômatos finitos determinísticos e não determinísticos**, e **avaliar qual modelo é mais adequado** para determinado problema. A ênfase está na compreensão das implicações do determinismo no projeto de autômatos e na tomada de decisões fundamentadas com base nas restrições e complexidade do sistema.

Os estudantes devem ser capazes de:

* **Comparar modelos DFA e NFA** com base em suas diferenças estruturais e comportamentais.
* **Analisar os requisitos da tarefa** para identificar se o determinismo é essencial ou opcional.
* **Selecionar e justificar** o modelo mais apropriado para implementação.



## **Especificação da Competência C**

### C.1 Título da Competência

    Testar Autômatos Usando Simuladores
    

### C.2 Descrição da Competência

Esta competência está relacionada ao **uso de ferramentas de simulação** (ex.: JFLAP) para verificar a correção e o comportamento de implementações de autômatos. A ênfase está no teste sistemático e no refinamento iterativo dos modelos de máquinas de estados.

Os estudantes devem ser capazes de:

* **Operar simuladores de autômatos** para testar comportamento de entrada/saída e transições.
* **Interpretar os resultados da simulação**, identificando discrepâncias entre o comportamento esperado e o observado.
* **Diagnosticar e corrigir erros** por meio de ciclos de depuração.
* **Aplicar estratégias de resolução de problemas** para refinar o autômato até alcançar o desempenho desejado.



## **Especificação da Competência D+E**

### D+E.1 Título da Competência

    Definir Expressões Regulares para Autômatos Finitos

### D+E.2 Descrição da Competência

Esta competência foca na capacidade de **relacionar expressões regulares a autômatos finitos**, tanto em nível teórico quanto prático.

Os estudantes devem ser capazes de:

* **Compreender a equivalência** entre expressões regulares e autômatos finitos.
* **Construir expressões regulares** que representem a mesma linguagem aceita por um autômato dado.
* **Traduzir estruturas de autômatos em expressões**, usando notação padrão e regras de simplificação.
* **Validar a correção** comparando o comportamento de ambas as representações por meio de testes ou provas formais.


## **Especificação da Competência F**

### F.1 Título da Competência

    Escrever um Relatório Técnico

### F.2 Descrição da Competência

Esta competência envolve a **produção colaborativa de um relatório técnico bem organizado** que comunique efetivamente o design, implementação e avaliação de soluções baseadas em autômatos.

Os estudantes devem demonstrar a capacidade de:

* **Escrever e estruturar um relatório** que sintetize o trabalho da equipe em uma narrativa coerente.
* **Aplicar convenções de escrita técnica**, assegurando clareza, precisão e lógica.
* **Documentar os resultados e raciocínios técnicos**, incluindo diagramas, representações formais e resultados de testes.
* **Revisar e aperfeiçoar o relatório de forma colaborativa**, integrando feedback dos colegas e seguindo padrões de apresentação.



## Tabela de Ajustes nas Competências

| **ID**  | **Competência** | **Disposições** | **Conhecimento** | **Habilidade** |
|---------|--------|-----------|-----------|-------------------|
| (A) | **Desenvolver soluções de problemas usando Autômatos.** | Colaborativo, Responsável, Proativo, Criativo | Máquinas de Estados Finitos | **Aplicar (Construir, Desenvolver, Projetar)** |
|         |                                   |                                 | Engenharia de Requisitos | **Aplicar (Interpretar, Implementar, Organizar)** |
|         |                                   |                                 | Pensamento Analítico e Crítico (FPK) | **Aplicar** |
|  |  |                                        |       |       
| (B) | **Justificar o uso de Autômatos Finitos Determinísticos (DFAs).** | Investigativo, Colaborativo, Responsável, Proativo | Autômatos Finitos Determinísticos (DFAs) | **Compreender (Comparar)** |
|         |                                   |                                 | Engenharia de Requisitos | **Aplicar** |
|         |                                   |                                 | Pensamento Analítico e Crítico (FPK) | **Aplicar** |
|  |  |                                        |       |       
| (C) | **Testar autômatos usando simuladores.** | Investigativo, Colaborativo, Responsável, Proativo, Criativo | Máquinas de Estados Finitos | **Aplicar (Experimentar, Relacionar, Simular)** |
|         |                                   |                                 | Resolução de Problemas e Solução de Problemas (FPK) | **Aplicar** |
|         |                                   |                                 | Modelagem e Simulação | **Aplicar** |
|  |  |                                        |       |       
| (D+E) | **Definir Expressões Regulares para Autômatos Finitos.** | Investigativo, Colaborativo, Responsável, Proativo, Criativo | Máquinas de Estados Finitos | **Compreender** |
|         |                                   |                                 | Expressões Regulares | **Aplicar** |
|         |                                   |                                 | Pensamento Analítico e Crítico (FPK) | **Aplicar** |
|  |  |                                        |       |       
| (F) | **Escrever um relatório técnico.** | Colaborativo, Minucioso, Responsável | Comunicação Escrita (FPK) | **Aplicar** |





## **Conclusão**  

O **processo de revisão da especificação de competências** resultou em **aperfeiçoamentos substanciais**, incorporando recomendações de especialistas para refinar definições, aumentar a especificidade, padronizar a terminologia e melhorar a clareza textual.  

Ao adotar uma taxonomia de conhecimento mais detalhada (CS2013), as competências tornaram-se mais precisas e reutilizáveis. Além disso, a introdução de vocabulário controlado e mapeamento estruturado de termos garante maior consistência nas descrições.  

A fusão de competências redundantes e os ajustes nos elementos de conhecimento e habilidades resultaram em um modelo mais coerente e estruturado.  

Para o futuro, *refinamentos iterativos contínuos e avaliações estruturadas por pares permanecerão essenciais para manter um modelo de especificação de competências de alta qualidade.* Esses aprimoramentos contribuirão para uma abordagem mais eficaz de aprendizagem baseada em competências, garantindo que as competências permaneçam claras, aplicáveis e alinhadas aos objetivos educacionais. 🚀
