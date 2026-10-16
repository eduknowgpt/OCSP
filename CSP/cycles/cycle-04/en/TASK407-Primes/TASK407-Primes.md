# TASK407 — Prime Numbers and Their Smallest Divisors

Author: Edeyson Gomes

Write a program that repeatedly reads an integer `n`. 

While `n` is greater than zero, determine whether it is prime and display the corresponding result. 

After processing each positive value, read another integer.

Stop when a value less than or equal to zero is entered. Do not evaluate the termination value.

Assume that all inputs are valid integers.

## Required results

- If `n` is prime, display `n is prime`.
- If `n` is greater than 1 and is not prime, display its smallest positive divisor greater than 1.
- If `n` is 1, display `1 is not prime and has no positive divisor greater than 1`.

A prime number is an integer greater than 1 whose only positive divisors are 1 and itself. Here, “first divisor” means the smallest divisor greater than 1, considering candidates in ascending order.


## Algorithm and comments

You may research algorithms for checking whether a number is prime. Implement a suitable algorithm and explain its operation in code comments, including:

- How divisors are checked.
- When the search stops.
- How prime numbers and the value 1 are handled.

If you use an external source, identify it in a code comment. The program must report the smallest divisor for each composite number, even if the chosen primality algorithm does not directly provide it.


## Example

For the following inputs, entered in order:

| Input | Expected output |
|---|---|
| 7 | `7 is prime` |
| 12 | `The smallest divisor of 12 greater than 1 is 2` |
| 25 | `The smallest divisor of 25 greater than 1 is 5` |
| 1 | `1 is not prime and has no positive divisor greater than 1` |
| 0 | End the program without evaluating the value |

Output wording may vary, provided the results are clearly identified.

## Submission

Submit the program’s source code, including comments explaining the algorithm. As an optional check, run the example and compare the actual results with the expected results.
