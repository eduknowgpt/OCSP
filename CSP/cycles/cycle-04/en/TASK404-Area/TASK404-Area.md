# TASK404 — Area of Regular Polygons

**Author:** Marco Bião.

Write a program that reads the number of sides of a regular polygon and its side length, in centimeters. Based on the number of sides, display:

- **3 sides:** `TRIANGLE` and its area, in cm².
- **4 sides:** `SQUARE` and its area, in cm².
- **5 sides:** `PENTAGON`.

Assume that the number of sides entered will be 3, 4, or 5 and that the side length will be positive. For the pentagon, display only its name.

## Formulas

Let `l` be the side length:

| Polygon | Area |
|---|---|
| Equilateral triangle | `A = (√3 / 4) × l²` |
| Square | `A = l²` |

## Examples

| Number of sides | Side length (cm) | Expected output |
|---|---|---|
| 3 | 4 | TRIANGLE — approximate area of 6.93 cm² |
| 4 | 4 | SQUARE — area of 16 cm² |
| 5 | 4 | PENTAGON |

Number formatting may vary; no fixed number of decimal places is required.

## Submission

Submit the program’s source code. As an optional check, run the three examples and compare the actual results with the expected results.