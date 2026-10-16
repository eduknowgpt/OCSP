# TASK409 — Excess Fishing Weight

**Creator:** Prof. MSc Marcos Bião — Univasf, Salgueiro Campus.

João "Papo-de-Pescador", an honest man, bought a microcomputer to keep track of his daily fishing yield. Whenever he brings in a catch weighing more than the limit established by the state’s fishing regulations (50 kilograms), he must pay a fine of R$4.00 per excess kilogram.

João needs you to write a program that reads the variable `P` (fish weight) and checks whether there is any excess. If there is, store the excess weight in the variable `E` (Excess) and the fine João must pay in the variable `M`. Otherwise, assign zero to both variables.

Display the values of `E` and `M`.

## Input

Read the catch weight in kilograms. Assume that the input is a valid nonnegative number. Fractional weights are allowed.

## Examples

| Fish weight — P (kg) | Excess weight — E (kg) | Fine — M (R$) |
|---|---|---|
| 40 | 0 | 0.00 |
| 50 | 0 | 0.00 |
| 55 | 5 | 20.00 |
| 52.5 | 2.5 | 10.00 |

## Output

Display the excess weight in kilograms and the fine in Brazilian reais, with the fine formatted to two decimal places.

## Submission

Submit the program’s source code. As an optional check, run the examples and compare the actual results with the expected results.