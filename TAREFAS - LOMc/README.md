# Acervo documental da primeira versão do CSP e do trabalho com LOMc

Este diretório reúne tarefas, especificações de competências, anotações, orientações de revisão, registros de sugestões e exemplos em RDF relacionados ao desenvolvimento colaborativo de Edeyson Andrade Gomes e Jéssica Santana e ao trabalho utilizado na dissertação de Jéssica Santana. Essa contextualização de autoria e uso foi fornecida pelo responsável pelo acervo.

A expressão “primeira versão do CSP” identifica o acervo retrospectivamente. Os documentos preservam nomenclaturas, códigos e estados próprios; não devem ser interpretados como uma aplicação integral do processo de referência consolidado posteriormente na tese de doutorado. A pasta também contém materiais com referências a um segundo ciclo e versões de trabalho, não apenas um conjunto fechado de documentos iniciais.

Inventário verificado em **24 de novembro de 2026**: **81 arquivos preexistentes**, sendo **67 DOCX, 8 PDF e 6 RDF**, distribuídos em seis pastas principais e dois documentos na raiz. Este README não integra essa contagem.

> **Situação de compartilhamento:** a anonimização dos revisores ainda está incompleta. Há nomes em documentos de revisão e em cópias históricas, inclusive uma associação explícita entre códigos e nomes. O uso de “Revisor 1” e “Revisor 2” em parte dos textos não torna o conjunto anônimo. Prepare uma cópia revisada para divulgação e preserve os originais em acesso restrito.

## Organização e função dos materiais

| Local | Arquivos | Conteúdo e finalidade |
|---|---:|---|
| `Anotações das Tarefas/` | 26 | Anotações de tarefas, registros de análise e revisão, orientações do processo, listas de códigos e textos de reespecificação. |
| `Competências_Tarefas_PBL/` | 7 | Especificações por tarefa e um documento da máquina de vender com códigos de competências. |
| `Códigos em RDF/` | 6 | Codificações de recursos e competências com vocabulários LOM/LOMc e referências de conhecimento e habilidades. |
| `Sugestões_Revisores/` | 6 | Sugestões organizadas para os seis problemas, com identificação por códigos parcialmente aplicada. |
| `Tarefas Anteriores/` | 22 | Versões anteriores, versões com correções e planos de ensino em DOCX/PDF. |
| `Tarefas-LOMCBokCs13_VersãoFinal/` | 12 | Seis tarefas em DOCX e seis em PDF, em uma pasta denominada “VersãoFinal”. |
| `Competências Refinadas.docx` | 1 | Notas de consolidação, redução de associações e reúso, com referências aos códigos utilizados nesse documento. |
| `Tabela com Todas as Competências_.docx` | 1 | Tabelas de competências dos seis casos, com atitudes, conhecimentos e habilidades. |

### Anotações das Tarefas

- `Analise das Entrevistas/Anotações das Tarefas/`: um documento de anotação da máquina de vender.
- `Anotação das Tarefas PBL/`: seis documentos de anotação; a subpasta `Tarefas com todos os conhecimentos/` reúne outros seis documentos.
- `Competências após Revisão/`: duas listas de códigos e três documentos intitulados como reespecificações. O arquivo de Controle de Tráfego não apresentou texto recuperável na inspeção do conteúdo XML; conferir visualmente antes de utilizá-lo como fonte de decisões.
- `Processo de Anotação e Revisão/`: orientações de anotação e revisão, com diagramas e trechos de trabalho. O arquivo de revisão inclui uma anotação interna que identifica os revisores; não é um guia público já saneado.
- `Tarefa PBL_Original/`: seis cópias de tarefas que também contêm sugestões e anotações. O nome da pasta não significa que os arquivos sejam enunciados sem intervenções.

### Tarefas Anteriores

- `Correção_Tarefas - LOMC Bok-Cs13/`: seis versões com correções e sugestões.
- `Plano de Ensino/`: dois documentos de competências e dois planos de ensino em PDF, relativos a MATA51 e MATC94.
- `Tarefas - LOMc Bok Cs2013/`: seis documentos de tarefas.
- `Tarefas LOMc - Cs2012/`: seis documentos de tarefas.

Os nomes `Cs2012`, `Cs2013` e `BokCs13` são os rótulos existentes nas pastas. Este README os preserva sem declarar equivalência entre os referenciais citados nos documentos.

## Identificação das tarefas

| Número local | Tema |
|---|---|
| 0 | Cálculo do Índice de Massa Corporal (IMC). |
| 1 | A máquina de vender refrigerantes e salgados. |
| 2 | Controle de tráfego. |
| 3 | Robô Fazendeiro. |
| 4 | O retorno do Robô Fazendeiro. |
| 5 | O Robô Fazendeiro e o Robô Alimentador. |

Esses números correspondem aos nomes locais. Não se deve inferir identidade com outras codificações de tarefas apenas pela numeração.

## Codificações RDF

| Arquivo | Conteúdo identificado no título interno |
|---|---|
| `CONTRAF.rdf` | Controle de Tráfego usando Máquinas de Turing. |
| `IMC.rdf` | Cálculo do Índice de Massa Corporal. |
| `Maq.rdf` | A máquina de vender refrigerantes e salgados. |
| `RETROBOF.rdf` | Retorno do Robô Fazendeiro usando Autômatos de Pilha. |
| `ROBOF.rdf` | O Robô Fazendeiro. |
| `ROBOFA.rdf` | Robô Fazendeiro usando Máquinas de Estados Finitos. |

Não foi estabelecida uma correspondência unívoca dos seis RDF com as seis tarefas. Em particular, `ROBOFA.rdf` não deve ser atribuído automaticamente à tarefa 5 pelo nome do arquivo: seu título interno descreve máquinas de estados finitos. A correspondência precisa ser confirmada pelo conteúdo e pela versão de referência.

A inspeção foi documental: não incluiu execução, validação semântica dos RDF ou comprovação de conformidade integral com padrões. Há dados de autoria e contato em alguns RDF; autoria de recursos e identidade de revisores são papéis diferentes.

## Como consultar o acervo

1. Para localizar os enunciados organizados como finais, comece por `Tarefas-LOMCBokCs13_VersãoFinal/`. A denominação “final” é a da pasta, não uma certificação independente da equivalência entre DOCX e PDF.
2. Consulte `Competências_Tarefas_PBL/` e as tabelas de códigos para examinar as especificações associadas.
3. Compare anotações, sugestões e reespecificações para reconstruir decisões. Uma sugestão registrada não demonstra, por si só, que o ajuste foi adotado.
4. Use `Tarefas Anteriores/` para comparar estados, preservando a referência ao caminho e ao conteúdo efetivamente consultados.
5. Examine o RDF como uma representação documental própria; não presuma que reproduza integralmente o último DOCX.

## Versões, códigos e limites de reconstrução

- Os identificadores de competências não têm significado estável em todas as listas. Por exemplo, `Códigos de Competências_.docx` atribui escrita de relatório técnico a C04, enquanto `Códigos de Competências - Ciclo 02.docx` utiliza C05. Informe sempre o arquivo e o estado de referência ao citar um código.
- Datas de criação/modificação dos arquivos podem refletir exportação ou preparação recente para compartilhamento. Elas não comprovam as datas das entrevistas ou decisões históricas.
- Os rótulos “ok”, “revisada”, “original” e “VersãoFinal” ajudam a localizar materiais, mas não estabelecem, isoladamente, uma sequência completa de aprovação.
- Há ao menos uma duplicação binária: o documento de retorno do robô na pasta `Tarefa PBL_Original/` e seu correspondente em `Correção_Tarefas - LOMC Bok-Cs13/` têm o mesmo SHA-256 na inspeção. Caminhos diferentes não significam necessariamente estados diferentes.
- O acervo preserva materiais de trabalho. Não constitui uma transcrição integral certificada de todas as entrevistas nem um histórico completo de revisões.

## Anonimização e preparação para compartilhamento

Antes de divulgar o conjunto:

- substituir nomes dos revisores por códigos consistentes em todos os documentos e versões destinadas à divulgação;
- remover da cópia pública qualquer legenda que associe código a nome, mantendo a chave de identificação separada e com acesso restrito;
- conferir comentários, alterações controladas, propriedades, cabeçalhos, rodapés, imagens e eventuais arquivos anexados;
- separar a autoria dos materiais e a atribuição de fontes da participação como revisor: não eliminar créditos autorais legítimos apenas porque são nomes de pessoas;
- revisar links externos que possam permitir acesso a outros documentos do trabalho;
- conferir o resultado no Word e nos PDF exportados antes do compartilhamento.

Foram encontradas designações A1/A2, R1/R2, P1/P2 e Revisor 1/Revisor 2. A equivalência entre todas elas deve ser verificada nos registros, sem associação automática por semelhança da numeração. Não registrar a chave nominal no README público.

Não foi detectado nome dos dois revisores procurados no texto extraído de três dos seis documentos de `Sugestões_Revisores/`; isso não certifica anonimização do acervo nem elimina possibilidades de identificação indireta.

## Estrutura completa dos arquivos preexistentes

Os caminhos abaixo preservam os nomes encontrados, inclusive acentos, espaços, sublinhados e grafias históricas.

```text
TAREFAS - LOMc/
├── Anotações das Tarefas/
│   ├── Analise das Entrevistas/
│   │   └── Anotações das Tarefas/
│   │       └── Anotação de Competências da Tarefa_ “A máquina de vender refrigerantes e salgados”.docx
│   ├── Anotação das Tarefas PBL/
│   │   ├── Tarefas com todos os conhecimentos/
│   │   │   ├── Problema 0 (Tarefa)_ IMC.docx
│   │   │   ├── Problema 1 (Tarefa)_ A máquina de vender refrigerantes e salgados.docx
│   │   │   ├── Problema 2 (Tarefa)_ Controle de tráfego.docx
│   │   │   ├── Problema 3 (Tarefa)_ Robô Fazendeiro.docx
│   │   │   ├── Problema 4 (Tarefa)_ O retorno do Robô fazendeiro.docx
│   │   │   └── Problema 5 (Tarefa)_ O robô fazendeiro e o robô alimentador.docx
│   │   ├── 0_Anotação do Cálculo IMC - ok.docx
│   │   ├── 1_Anotação da Máquina de Vender Salgados - OK.docx
│   │   ├── 2_Anotação da Tarefa de Controle de Tráfego - ok.docx
│   │   ├── 3_Anotação do Robô Fazendeiro - ok_.docx
│   │   ├── 4_Anotação do Retorno do Robô Fazendeiro_.docx
│   │   └── 5_Anotação do Robô fazendeiro e o Robô alimentador.docx
│   ├── Competências após Revisão/
│   │   ├── Códigos de Competências - Ciclo 02.docx
│   │   ├── Códigos de Competências_.docx
│   │   ├── Re-Especificação de Competências Controle de Tráfego.docx
│   │   ├── Re-Especificação de Competências IMC.docx
│   │   └── Re-Especificação de Competências Máquina de Vender Refrigerante e Salgados.docx
│   ├── Processo de Anotação e Revisão/
│   │   ├── Processo de Anotação_.docx
│   │   └── Processo de Revisão.docx
│   └── Tarefa PBL_Original/
│       ├── Cópia de Problema 0 (Tarefa)_ IMC.docx
│       ├── Cópia de Problema 1 (Tarefa)_ A máquina de vender refrigerantes e salgados.docx
│       ├── Cópia de Problema 2 (Tarefa)_ Controle de tráfego.docx
│       ├── Cópia de Problema 3 (Tarefa)_ Robô Fazendeiro.docx
│       ├── Cópia de Problema 4 (Tarefa)_ O retorno do Robô fazendeiro.docx
│       └── Cópia de Problema 5 (Tarefa)_ O robô fazendeiro e o robô alimentador.docx
├── Competências_Tarefas_PBL/
│   ├── Competência_ Tarefa03.docx
│   ├── Competência_Tarefa_01_.docx
│   ├── Competência_Tarefa_02.docx
│   ├── Competência_Tarefa_04.docx
│   ├── Competência_Tarefa_05.docx
│   ├── Competência_Tarefa_0_.docx
│   └── Máquina de Vender Refrigerante e Salgados com Código das Competências_.docx
├── Códigos em RDF/
│   ├── CONTRAF.rdf
│   ├── IMC.rdf
│   ├── Maq.rdf
│   ├── RETROBOF.rdf
│   ├── ROBOF.rdf
│   └── ROBOFA.rdf
├── Sugestões_Revisores/
│   ├── Tarefa 03_Robo Fazendeiro.docx
│   ├── Tarefa_01_Máquina de Vender Refrigerante_.docx
│   ├── Tarefa_02_Controle de Trafégo.docx
│   ├── Tarefa_04_O Retorno do Robo Fazendeiro.docx
│   ├── Tarefa_05_O robô fazendeiro e o robô alimentador.docx
│   └── Tarefa_0_IMC.docx
├── Tarefas Anteriores/
│   ├── Correção_Tarefas - LOMC Bok-Cs13/
│   │   ├── Problema 0 (Tarefa)_ IMC.docx
│   │   ├── Problema 1 (Tarefa)_ A máquina de vender refrigerantes e salgados.docx
│   │   ├── Problema 2 (Tarefa)_ Controle de tráfego.docx
│   │   ├── Problema 3 (Tarefa)_ Robô Fazendeiro_c.docx
│   │   ├── Problema 4 (Tarefa)_ O retorno do Robô fazendeiro.docx
│   │   └── Problema 5 (Tarefa)_ O robô fazendeiro e o robô alimentador.docx
│   ├── Plano de Ensino/
│   │   ├── Competências_MATA512022.2.docx
│   │   ├── Competências_MATC942022.1.docx
│   │   ├── MATA512022.2.pdf
│   │   └── MATC942022.1.pdf
│   ├── Tarefas - LOMc Bok Cs2013/
│   │   ├── Problema 0 (Tarefa)_ IMC.docx
│   │   ├── Problema 1 (Tarefa)_ A máquina de vender refrigerantes e salgados.docx
│   │   ├── Problema 2 (Tarefa)_ Controle de tráfego.docx
│   │   ├── Problema 3 (Tarefa)_ Robô Fazendeiro.docx
│   │   ├── Problema 4 (Tarefa)_ O retorno do Robô fazendeiro.docx
│   │   └── Problema 5 (Tarefa)_ O robô fazendeiro e o robô alimentador.docx
│   └── Tarefas LOMc - Cs2012/
│       ├── Problema 0 (Tarefa)_ IMC.docx
│       ├── Problema 1 (Tarefa)_ A máquina de vender refrigerantes e salgados.docx
│       ├── Problema 2 (Tarefa)_ Controle de tráfego.docx
│       ├── Problema 3 (Tarefa)_ Robô Fazendeiro.docx
│       ├── Problema 4 (Tarefa)_ O retorno do Robô fazendeiro.docx
│       └── Problema 5 (Tarefa)_ O robô fazendeiro e o robô alimentador.docx
├── Tarefas-LOMCBokCs13_VersãoFinal/
│   ├── Tarefas/
│   │   ├── Problema 0 (Tarefa)_ IMC.docx
│   │   ├── Problema 1 (Tarefa)_ A máquina de vender refrigerantes e salgados.docx
│   │   ├── Problema 2 (Tarefa)_ Controle de tráfego.docx
│   │   ├── Problema 3 (Tarefa)_ Robô Fazendeiro.docx
│   │   ├── Problema 4 (Tarefa)_ O retorno do Robô fazendeiro.docx
│   │   └── Problema 5 (Tarefa)_ O robô fazendeiro e o robô alimentador.docx
│   └── Tarefas em PDF/
│       ├── Problema 0 (Tarefa)_ IMC.pdf
│       ├── Problema 1 (Tarefa)_ A máquina de vender refrigerantes e salgados.pdf
│       ├── Problema 2 (Tarefa)_ Controle de tráfego.pdf
│       ├── Problema 3 (Tarefa)_ Robô Fazendeiro.pdf
│       ├── Problema 4 (Tarefa)_ O retorno do Robô fazendeiro.pdf
│       └── Problema 5 (Tarefa)_ O robô fazendeiro e o robô alimentador.pdf
├── Competências Refinadas.docx
└── Tabela com Todas as Competências_.docx
```

## Uso e atribuição

Ao utilizar os materiais, identifique sua relação com o trabalho colaborativo e com a dissertação de Jéssica Santana, além da versão documental efetivamente consultada. A existência deste README não concede nova licença nem substitui condições de uso e atribuição presentes nos recursos originais.
