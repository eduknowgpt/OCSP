### Análise de Algoritmo em C

Com base no algoritmo acima, e supondo que os valores fornecidos para as variáveis **"A"**, **"B"**, **"C"** e **"D"** sejam, respectivamente, **10, 15, 20 e 25**, pode-se afirmar que, após execução do referido algoritmo, os valores dessas variáveis serão, respectivamente: *(0,5 pontos)*

```c
int main(){
    float a,b,c,d;
    scanf("%d%d%d%d",&a,&b,&c,&d);
    a = b;
    b = c;
    c = d;
    d = a;
    b = a + b/2;
    c = c+b;
    d = d + (b*2) - a;
}
```

Alternativas:

    (a) 15 - 17,5 - 42,5 - 35

    (b) 15 - 17,5 - 42,5 - 50

    (c) 15 - 25 - 50 - 45

    (d) 15 - 25 - 50 - 50

    (e) 15 - 30 - 55 - 60