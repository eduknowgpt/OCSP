# Problema 25.01: A máquina de vender refrigerantes e salgados

**Autores:** Luiz Gavaza, Lais Salvador, David Moises e Roberta Oliveira  
**Colaboradores:** Edeyson Gomes e Jéssica Santana  
**Estagiário docente:** Marcos Bião  
**Atualização:** 25 de setembro de 2025  

> Este problema é baseado nas notas de aula do professor **Martin Musicante** do **DIMAP – UFRN**.



## 1. Problema

A empresa **Refrigerantes e Salgados S.A.** resolveu desenvolver novas soluções para as suas máquinas de vender refrigerantes e salgados, baseadas em projetos de hardware e software bem estruturados, acompanhados de uma documentação precisa e de fácil uso.

A ideia surgiu quando um técnico de informática da empresa estava conversando com um grupo de estudantes do Instituto de Computação da UFBA. Eles perceberam que há algumas máquinas de estados, chamados **autômatos**, que atendem às funcionalidades das máquinas de venda, além de usarem pouca memória e serem de simples configuração.

As máquinas da empresa devem ser configuradas para vender no mínimo **três (3) produtos** e receber **moedas e notas de R\$ 1,00 e R\$ 2,00**, além de prever a funcionalidade de **troco**. No portfólio da empresa há opções para venda de:
- refrigerantes de **R\$ 5,00** e **R\$ 7,00**;
- pacotes de salgados de **R\$ 7,00** e **R\$ 10,00**.

Os estudantes também comentaram sobre uma ferramenta chamada **JFLAP**[^1] para testar/simular soluções que utilizam esses autômatos. Eles explicaram que a JFLAP apresenta uma interface gráfica que pode contribuir para a documentação dessas novas soluções para as máquinas de venda.

Outro ponto interessante é que o técnico de informática já trabalhou com **expressões regulares** e ouviu dizer que expressões regulares têm relação com alguns desses autômatos. Ele gostaria de saber se essa informação procede (*investigar*); caso afirmativo, gostaria de ter **pelo menos um exemplo** de como isso funcionaria para um trecho do autômato construído para alguma máquina de venda. Ele acredita que as expressões regulares também podem ajudar na documentação dessas máquinas e de projetos futuros.

### Desafio

O técnico de informática prometeu um **bônus adicional** se eles conseguirem ajudar na divulgação das novas máquinas, ao implementar uma modificação que permita que as máquinas possam **aleatoriamente dar um troco bônus de R\$ 1,00**, caso o valor inserido pelo cliente seja **exatamente o preço do produto selecionado**.



## 2. Produto

Você deverá postar no **Moodle UFBA** até as **23:59h do dia 13/10/2025**, no espaço apropriado para tal:

1. Um **arquivo com um autômato** que contenha uma máquina de vender refrigerantes e salgados, de forma que a equipe de tecnologia da empresa **Refrigerantes e Salgados S.A.** possa testar/simular no **JFLAP**;  
2. Um **relatório no modelo de artigos da SBC**[^2] (Sociedade Brasileira de Computação) que descreva com o máximo de detalhes o funcionamento do sistema da máquina de vender refrigerantes e salgados.

O relatório deverá:
- descrever quais as **operações executadas pelo sistema** para receber o pagamento do cliente e entregar o produto escolhido;
- apresentar **ao menos dois (2) exemplos** de funcionamento.

Caso seja possível atender ao pedido do técnico, o relatório também deve conter:
- a **expressão regular** correspondente a um trecho do autômato analisado;
- o **método de construção** dessa expressão.

Caso não seja possível, apresentar no relatório uma **justificativa** para essa impossibilidade.



## 3. Conhecimentos / Conceitos Envolvidos

a. Autômatos Finitos Determinísticos  
b. Autômatos Finitos Não-Determinísticos  
c. Expressões Regulares  



## 4. Objetivos de Aprendizagem

### 4.1 Objetivo Geral

Desenvolver **autômatos finitos** e **expressões regulares** para resolver problemas “reais”, como é o caso do projeto de máquinas da empresa **Refrigerantes e Salgados S.A.**

### 4.2 Objetivos Específicos

I. Identificar as funcionalidades do sistema idealizado pelo usuário.  
II. Conciliar as funcionalidades desejadas pelo usuário com as funcionalidades do autômato a ser desenvolvido.  
III. Avaliar o uso de **não-determinismo** no autômato desenvolvido.  
IV. Associar opções da máquina, moedas e notas com **símbolos de um alfabeto**.  
V. Especificar **relatórios de cunho técnico**.  
VI. Usar **ferramentas de simulação** para autômatos finitos.



## Referências

RAMOS, M. V. M.; JOSE NETO, J.; VEGA, I. S.  
*Linguagens Formais: Teoria, Modelagem e Implementação.* Editora Bookman, 2009.

MENEZES, Paulo Blauth.  
*Linguagens formais e autômatos.* 6. ed. Bookman, 2011.



[^1]: https://www.jflap.org/  
[^2]: https://www.sbc.org.br/wp-content/uploads/2024/07/modelosparapublicaodeartigos.zip
