# MATC94 – Introdução às Linguagens Formais e Teoria da Computação

**Profa.** Laís Salvador

**Estagiário Docente:** Marcos Bião

**Anotador de Competências:** Edeyson Andrade Gomes

## Temas dedicados ao problema

* Linguagens formais
* Representação de linguagens
* Operações com linguagens



## Apresentação do problema

Um certo colecionador de arte dispõe de partituras e gravações de músicas, as quais ele precisa catalogar e processar mediante computador. O colecionador em questão é muito exigente com o tratamento do seu material e garante que, para cada música na sua coleção, a partitura corresponde exatamente à gravação correspondente.

Algumas das partituras que o colecionador possui são apenas para um instrumento. Outras são para vários instrumentos. Cada partitura para um instrumento pode ser vista como uma sequência de símbolos musicais. No caso das partituras para vários instrumentos, elas podem ser vistas como sequências, mas de símbolos compostos: cada elemento da sequência é formado por um número finito de símbolos musicais. Cada música pode ter um número arbitrário de símbolos.

Veja os exemplos de partituras para um instrumento e partituras para três instrumentos, respectivamente:

### Um instrumento

![Partitura para um instrumento](./img01.jpg)

Note que cada nota pode ser vista de forma independente como um símbolo (escrito em um pentagrama).
No exemplo a seguir, correspondente a uma partitura para três instrumentos, cada um deles possui uma representação similar à vista acima: cada instrumento possui o seu próprio pentagrama e, em cada um deles, as notas são superpostas em cada tempo.

### Três instrumentos

![Partitura para três instrumentos](./img02.jpg)

Cada música pode pertencer a um ou mais gêneros musicais. Para cada gênero, o colecionador precisa definir quais as músicas que pertencem a ele. Alguns gêneros são formados por um conjunto finito de músicas, mas outros são definidos de forma geral, pela forma dos compassos (por exemplo, o gênero das valsas é formado por todas aquelas músicas com compassos ¾).

O nosso colecionador não admite falhas nas respostas às suas questões. Ele formulou algumas questões e precisa que as mesmas sejam respondidas de forma que não exista dúvida sobre a veracidade das respostas. Isto só pode ser feito mediante uma justificativa matemática para cada uma das questões.

Felizmente, a Teoria da Computação nos fornece ferramentas para responder ao questionário do colecionador, já que cada nota musical pode ser vista como um símbolo, o qual pode ser usado para construir sequências, as quais representarão as partituras para um instrumento só.



## Questões (a serem respondidas pelo grupo, sempre justificando a resposta)

1. É verdade que cada música pode ser vista como uma string?
2. É possível formar uma música a partir da concatenação de outras? O resultado pode ser chamado de música, também?
3. Um trecho de uma determinada música é também uma música? O trecho pode estar no início, no meio ou no fim da música original?
4. Caso eu decidisse reescrever uma música no sentido inverso (de trás para a frente), o resultado também pode ser considerado uma música? Qual é a operação que eu devo aplicar para obter essa música “ao contrário”?
5. O conjunto das músicas de rock que eu possuo tem 3500 elementos. Eu tenho um conjunto de 700 óperas. Também conto com o conjunto das músicas que eu gostaria ainda de escrever, mas esse conjunto, por enquanto, não tem nenhuma música nele. Para me ajudar neste período de vácuo criativo, definir os seguintes conjuntos:

    a) O conjunto das músicas formadas pelos trechos iniciais (20 primeiras notas) de cada música de rock da minha coleção.
    
   b) O conjunto formado pela repetição de uma mesma música, 0, 1, 2, 3, 4, 5, … vezes.
   
   c) O conjunto formado apenas pela música vazia (aquela que não contém nenhuma nota).
   
   d) O conjunto das músicas românticas: {m | m é uma música que contém a palavra “amor” na sua letra}.
   
   e) O conjunto de músicas que são óperas **ou** que são românticas.
   
   f) O conjunto das músicas que são óperas **e** rock ao mesmo tempo.
   
   g) Se eu tenho coleções de músicas: valsas para flauta, valsas para piano, valsas para trompete e valsas para violoncelo — como posso fazer para obter uma coleção de valsas para os quatro instrumentos combinados?
   
   h) É possível ter a coleção de todas aquelas músicas que **não são óperas**?
   
   i) Conhecendo cada partitura e o seu arquivo MP3 correspondente, é possível usar cada um de forma intercambiável (é possível ver uma delas como a codificação da outra)?



## Autoria

Atividade baseada no problema **Coleção de Músicas**, do prof. *Martin Musicante* – UFRN.

