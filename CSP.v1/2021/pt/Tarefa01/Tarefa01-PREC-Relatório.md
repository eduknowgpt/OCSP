# Relatório de Revisão de Especificação de Competências Baseado no CSRP: Tarefa 1 – A Máquina de Vendas de Refrigerantes e Lanches

## 1. Introdução

Este relatório documenta a revisão das especificações de competências associadas à tarefa de Aprendizagem Baseada em Problemas (ABP) "A Máquina de Vendas de Refrigerantes e Lanches". A revisão foi conduzida utilizando o processo estruturado Processo de Especificação e Revisão de Competências (PREC), com o objetivo de avaliar a clareza, precisão, alinhamento pedagógico e relevância das competências definidas, incluindo seus conhecimentos, habilidades e disposições associados.

A análise foi baseada em entrevistas realizadas com dois instrutores experientes, utilizando um protocolo de entrevista estruturado. Em vez de apresentar uma transcrição completa do guia de entrevista, este relatório resume a estrutura do instrumento e sintetiza as percepções dos revisores. Os resultados da revisão são organizados de acordo com as principais etapas do CSRP, destacando pontos fortes, inconsistências e sugestões de melhoria no processo de especificação de competências.

## 2. Resumo das Recomendações

### 2.1 Granularidade do Conhecimento

**P1:** *"Em relação ao conhecimento abordado na tarefa, seria benéfico ajustá-lo para um nível menor de granularidade. A granularidade atual é muito alta, dificultando a compreensão. Por exemplo, no conhecimento sobre autômatos finitos, autômatos determinísticos não foram especificados, apenas autômatos finitos foram mencionados, o que causou confusão. Portanto, sugiro modificar a taxonomia de conhecimento."*  

**P2:** *"O principal problema para mim é a granularidade do conhecimento. A taxonomia utilizada é a ACM CCS 2012, mas o nível de granularidade é muito amplo. Ao comparar o conhecimento listado nas tarefas, a maioria não está explicitamente listada na taxonomia, impossibilitando sua anotação adequada. Por exemplo, na Tarefa 1 ('A Máquina de Vendas de Refrigerantes e Lanches'), autômatos finitos determinísticos e não determinísticos, assim como expressões regulares, não estão incluídos na taxonomia—ela lista apenas 'linguagens regulares'. Assim, todas essas anotações precisam ser revisadas."*  

### 2.2 Vocabulário Controlado

**P1:** *"É necessário garantir a padronização das descrições de competências para manter a consistência na documentação das competências educacionais."*  

**P2:** *"Ao analisar as competências descritas, notei uma falta de padronização nos termos usados nos recursos anotados. Para garantir que possam ser facilmente compreendidos e reutilizados, um sistema de mapeamento de termos deve ser implementado."*  

### 2.3 Verbos da Taxonomia de Bloom

**P1:** *"Achei interessante o uso de múltiplos verbos, pois permite uma descrição mais clara das ações esperadas para cada par conhecimento-habilidade."*  

**P2:** *"Os verbos selecionados melhoram efetivamente a clareza das habilidades e estão bem alinhados com a tarefa e os objetivos de aprendizagem."*  

### 2.4 Clareza Textual nas Descrições de Competências

**P1:** *"Algumas descrições de competências e pares conhecimento-habilidade precisam ser reavaliadas para garantir que sejam mais diretas e livres de ambiguidade. Por exemplo, na Competência D: 'Determinar Expressões Regulares que Representam Autômatos', sugiro reformular o título, pois não é suficientemente claro."*  

**P2:** *"Várias competências precisam ser reformuladas. Algumas descrições são muito diretivas, enquanto outras são muito genéricas. É necessária maior clareza para que os leitores entendam completamente o que a tarefa está solicitando.*  

- *Nas **Competências C e D**, o texto descritivo sobre o conhecimento é desnecessário; sugiro remover a explicação sobre 'O Propósito da Modelagem e Simulação' e 'Revisão de Expressões Regulares.'*  

- *Em relação à **Competência D**, sugiro modificar o título de **'Determinar Expressões Regulares que Representam Autômatos'** para **'Como Relacionar Expressões Regulares e seus Autômatos Equivalentes.'** Acredito que essa redação torna a competência mais clara.*  

- *Além disso, recomendo fundir as **Competências D e E**, pois elas são idênticas."*  

### 2.5 Relevância e Adequação do Conhecimento

**P1:** *"O conhecimento descrito na tarefa deve estar melhor alinhado. Os objetivos específicos mencionam certos elementos de conhecimento que são esperados para aplicação, mas não consegui identificar onde os estudantes realmente os utilizariam. Por exemplo, o conhecimento sobre equivalência parece desnecessário, pois os estudantes podem precisar apenas responder sobre autômatos determinísticos.*  

- *Recomendo **remover os seguintes elementos de conhecimento**, pois não estão refletidos na descrição da tarefa:*  
    - Identificar a equivalência entre **Autômatos Finitos Determinísticos (AFD) e Autômatos Finitos Não Determinísticos (AFND)**.  
    - Identificar a equivalência entre **Autômatos Finitos (AF) e Expressões Regulares (ER)**.  
    - Aplicar a equivalência entre **AF e ER** para desenvolver **ER com base em AF existentes**.  

- *Da mesma forma, na **Competência B ('Equivalência de AFDs e AFNDs - Entender (Comparar)'),** o conhecimento sobre AFDs e AFNDs não está incluído na descrição da tarefa. As outras competências estão corretamente alinhadas."*  

**P2:** *"Ao definir uma competência ou habilidade, é essencial garantir que o conhecimento associado seja **relevante e aplicável** ao contexto educacional. No entanto, nos elementos de conhecimento listados na tarefa, há uma menção a **Autômatos Finitos Não Determinísticos (AFND)**, mas não consegui encontrar nenhuma referência a esse conhecimento no problema a ser resolvido.*  

- Além disso, alguns dos **objetivos de aprendizagem incluem elementos de conhecimento que não são abordados na descrição da tarefa**. Portanto, sugiro remover os seguintes elementos de conhecimento:  
    - Identificar a equivalência entre **AFD e AFND**.  
    - Identificar a equivalência entre **AF e ER**.  
    - Aplicar a equivalência entre **AF e ER** para desenvolver **ER com base em AF existentes**.  

- *Da mesma forma, na **Competência B ('Equivalência de AFDs e AFNDs - Entender (Comparar)'),** o conhecimento sugerido não é coberto pela **descrição do caso ABP**, portanto deve ser removido."*  

## 2.6 Sugestões de Revisão

### Sugestões de P1
- **Granularidade do Conhecimento** → O nível atual é muito alto e deve ser ajustado para fornecer mais especificidade.  
- **Conhecimento e Conceitos**  
  - Remover **Autômatos Finitos Não Determinísticos (AFND)**, pois não são abordados na descrição da tarefa.  
  - Remover **objetivos de aprendizagem** não explicitamente abordados na tarefa:  
    - Identificar a equivalência entre **AFD e AFND**.  
    - Identificar a equivalência entre **AF e ER**.  
    - Aplicar a equivalência entre **AF e ER** para desenvolver **ER com base em AF existentes**.  
- **Competência B**  
  - Revisar e reformular o título em relação a **quando usar AFD ou AFND**.  
  - Remover o **par conhecimento-habilidade 'Equivalência de AFDs e AFNDs - Entender (Comparar)'**, pois não é relevante para a tarefa.  
  - Remover referências ao **conhecimento sobre AFND**, pois não é abordado na tarefa.  

### Sugestões de P2
- **Granularidade do Conhecimento** → O nível é muito alto e precisa de refinamento.  
- **Refinamento Textual** → Algumas descrições são **muito diretivas**, enquanto outras são **muito genéricas**. Ajustes devem melhorar clareza e precisão.  
- **Competência B**  
  - Concorda com P1 sobre a remoção do **par conhecimento-habilidade 'Equivalência de AFDs e AFNDs - Entender (Comparar)'**.  
- **Competência C**  
  - Remover a explicação sobre **o propósito da modelagem e simulação**, incluindo otimização, tomada de decisão, considerações de segurança e treinamento.  
- **Competência D**  
  - Remover a **explicação sobre revisão de expressões regulares e sua equivalência com autômatos finitos**.  
  - Modificar o título da Competência D de **"Determinar Expressões Regulares que Representam Autômatos"** para **"Como Relacionar Expressões Regulares e seus Autômatos Equivalentes"** para maior clareza.  
- **Competência E**  
  - Fundir **Competência E com Competência D**, pois são essencialmente as mesmas.  

## 3. Conclusão e Próximos Passos

O **processo de revisão de especificação de competências** forneceu insights críticos sobre áreas que requerem melhorias, particularmente em relação à **granularidade do conhecimento, precisão textual e alinhamento das competências com os objetivos de aprendizagem da tarefa**. Guiado pelo feedback dos revisores, uma série de refinamentos direcionados será implementada para melhorar a **clareza, relevância e valor educacional** das especificações de competências.

Uma conclusão central da revisão é que **o nível atual de granularidade do conhecimento é excessivamente amplo**, limitando a eficácia da anotação e reduzindo a precisão conceitual. Para resolver isso, uma **taxonomia de conhecimento mais estruturada e refinada** será adotada, permitindo maior especificidade e melhor alinhamento com o escopo real da tarefa. Como parte desse ajuste, **conceitos relacionados a Autômatos Finitos Não Determinísticos (AFND)**—que não estão presentes no cenário ABP—serão revisados ou removidos.

Além disso, **a clareza textual será significativamente aprimorada** com o refinamento de formulações vagas e a eliminação de descrições excessivamente prescritivas. Algumas declarações de competências foram consideradas muito genéricas ou muito diretivas. Para melhorar a coerência e usabilidade, **os títulos das competências serão reformulados**, **entradas redundantes (ex.: Competências D e E) serão fundidas**, e **conteúdo explicativo não ancorado na tarefa será removido**. A Competência B, em particular, será reestruturada para refletir com mais precisão seu foco pretendido.

Vários **objetivos de aprendizagem e descrições de competências** também serão revisados para garantir que mapeiem diretamente às demandas da tarefa. Itens de conhecimento que não são **explicitamente necessários** pelo caso ABP serão removidos, evitando assim desalinhamento entre os resultados esperados e as competências realmente desenvolvidas.

Olhando para frente, a integração de um **vocabulário padronizado e uma taxonomia de conhecimento estruturada** apoiará maior consistência, reusabilidade e alinhamento entre as tarefas ABP. A **natureza iterativa do CSRP** continuará sendo uma ferramenta valiosa para refinar e validar competências conforme os contextos de aprendizagem evoluem.

Ao implementar essas melhorias, o framework de competências se tornará **mais robusto, pedagogicamente sólido e reutilizável**, oferecendo maior suporte a estudantes, instrutores e designers de currículo engajados em **educação em computação baseada em competências**.

> Essas revisões garantirão que a especificação de competências funcione não apenas como um instrumento de avaliação válido, mas também como um modelo instrucional reutilizável para futuras experiências de aprendizagem baseadas em ABP.
