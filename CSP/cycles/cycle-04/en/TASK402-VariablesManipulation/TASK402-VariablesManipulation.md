# TASK402 – Variable Manipulation

> Creator: Prof. Marcos Bião, MSc, Univasf – Salgueiro Campus  
> Contributors: Edeyson Gomes and Jéssica Santana

## 1. Problem

The learner must trace the execution of a C program and determine the final values of variables `a`, `b`, `c`, and `d`, given the inputs **10, 15, 20, and 25**, respectively.

```c
#include <stdio.h>

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

After execution, the values of `a`, `b`, `c`, and `d` will be, respectively:

- **(a)** 15 – 17.5 – 42.5 – 35
- **(b)** 15 – 17.5 – 42.5 – 50
- **(c)** 15 – 25 – 50 – 45
- **(d)** 15 – 25 – 50 – 50
- **(e)** 15 – 30 – 55 – 60

Assume that all four inputs were read successfully.

## 2. Process and Deliverables

The learner follows the statements in execution order, using the updated variable values and respecting operator precedence.

**Original deliverable:** the selected answer choice.

**Recommended supplementary evidence:** a table showing the values of all four variables after input and after each assignment. This record makes the reasoning observable; the selected answer alone does not demonstrate mastery of execution tracing.

## 3. Related Knowledge

| Code | Knowledge | Application in the task |
|---|---|---|
| K1 | Numeric data types and variables | Interpret the values stored in `float` variables. |
| K2 | Data input in C | Interpret how values are read using `scanf` and the `%f` format specifier. |
| K3 | Assignment statements | Track the replacement of variable values. |
| K4 | Arithmetic expressions and operator precedence | Evaluate expressions using current values. |
| K5 | Sequential execution | Follow statement order and dependencies. |

Execution tracing is the procedure that mobilizes this knowledge; it does not need to constitute an additional knowledge component.

## 4. Implicit Learning Objectives

The following objectives are inferred from the actions required by the task:

| Code | Objective | Bloom level |
|---|---|---|
| LO1 | Determine variable values after successive assignments, respecting execution order. | Apply |
| LO2 | Evaluate arithmetic expressions using updated values and operator precedence. | Apply |
| LO3 | Simulate the program’s sequential execution and determine its final state. | Apply |

The trace table makes LO1–LO3 observable. Producing it is a recommended addition, not a requirement of the original question.

## 5. Context and Target Audience

An introductory programming activity suitable for upper secondary technical education in Informatics, following instruction in variables, data input, assignments, arithmetic expressions, and sequential execution in C.

## 6. Performance Criteria

- **Initial:** recognizes statements but makes recurring errors when tracking updates.
- **Developing:** determines some states correctly, with inconsistencies in assignments or expression evaluation.
- **Expected:** correctly determines the states and final result, demonstrating the procedure through tracing or explanation.

These levels describe performance on this task, not general programming proficiency.