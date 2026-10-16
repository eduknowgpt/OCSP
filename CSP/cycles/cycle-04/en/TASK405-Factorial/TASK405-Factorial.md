# TASK405 — Calculating Factorials Using Functions and Loops

**Author:** Marco Bião.

Write a program that reads a positive integer `n`, indicating how many values will be processed. Then read each of the `n` integer values individually, calculate its factorial and display the result.

The factorial calculation must be implemented in a separate function named `factorial(x)`. The function must receive a nonnegative integer as a parameter, calculate its factorial using a loop and return the result.

If a negative value is entered, display an error message and request a replacement. Rejected values must not count toward the `n` values to be processed.

Assume that `n` is a positive integer and that all subsequent inputs are integers. The program must validate whether each value `x` is nonnegative.

## Calculation

The factorial of a nonnegative integer `x` is:

`x! = 1 × 2 × … × x`, for `x ≥ 1`.

By definition, `0! = 1`.

## Output

Display each result in the format:

`x! = result`

## Examples

For `n = 3`:

| Value entered | Expected behavior |
|---|---|
| 0 | Display `0! = 1` |
| 4 | Display `4! = 24` |
| -2 | Display an error message and request a replacement |
| 5 | Display `5! = 120` |

The program processes three valid values: 0, 4 and 5.

## Optional extensions

- Handle values whose factorial exceeds the supported numeric range, using an appropriate numeric representation or displaying a limit message.
- Store all results in a list and display a final summary.

## Submission

Submit the program’s source code, including the separate factorial function, loops and negative-input validation. As an optional check, run the example and compare the actual behavior with the expected behavior.