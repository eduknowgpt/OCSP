### Analysis of a C Algorithm

Based on the algorithm below, and assuming that the values entered for variables **A**, **B**, **C**, and **D** are **10, 15, 20, and 25**, respectively, what will their respective values be after the algorithm is executed? *(0.5 points)*

```c
int main(void) {
    float a, b, c, d;

    scanf("%f%f%f%f", &a, &b, &c, &d);

    a = b;
    b = c;
    c = d;
    d = a;
    b = a + b / 2;
    c = c + b;
    d = d + (b * 2) - a;

    return 0;
}
```

Answer choices:

(a) 15 - 17.5 - 42.5 - 35

(b) 15 - 17.5 - 42.5 - 50

(c) 15 - 25 - 50 - 45

(d) 15 - 25 - 50 - 50

(e) 15 - 30 - 55 - 60