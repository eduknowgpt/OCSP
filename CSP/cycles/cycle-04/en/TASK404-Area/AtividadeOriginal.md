Classificação e Cálculo de Áreas de Polígonos Regulares a partir do Número de Lados e Medida do Lado

Autor: Marco Bião

Escreva um programa para ler o número de lados de um polígono regular e a medida do
lado (em cm). Calcular e imprimir o seguinte: 
- Se o número de lados for igual a 3 escrever TRIÂNGULO e o valor da área.
- Se o número de lados for igual a 4 escrever QUADRADO e o valor da sua área.
- Se o número de lados for igual a 5 escrever PENTÁGONO.



Fórmulas Gerais e Cálculos**

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