# TASK410 — Football Preferences Survey

**Author:** Professor from Univasf (Task05 - professor B).

A survey will be conducted in Porto Alegre with an unknown number of respondents. For each respondent, the following information will be collected:

- **Preferred football club:** `1` for Grêmio, `2` for Internacional or `3` for other clubs.
- **Salary:** a nonnegative amount in Brazilian reais.
- **Birthplace:** `0` for Porto Alegre or `1` for another city.

Write a program that reads each respondent’s data and displays a summary of the survey.

To end input, enter `0` when prompted for the preferred club. Check this termination value before requesting salary and birthplace. Do not count the termination entry as a respondent.

Assume that all inputs are valid. Fractional salary amounts and a salary of zero are allowed. Each record represents a different respondent.

## Required results

After input ends, display:

- The number of supporters in each category: Grêmio, Internacional and other clubs.
- The average salary of Grêmio supporters.
- The average salary of Internacional supporters.
- The number of respondents born in Porto Alegre whose preferred club is in the “other clubs” category.
- The total number of respondents.

Calculate each average using only the salaries and number of supporters in the corresponding club category. Include respondents whose salary is zero.

If a club has no supporters, display `No respondents in this category` instead of calculating its average.

If input ends before any respondent is entered, display zero for all counts and the corresponding message for both averages.

## Example

For the following records, followed by club code `0`:

| Preferred club | Salary (R$) | Birthplace |
|---|---|---|
| 1 — Grêmio | 2000.00 | 0 — Porto Alegre |
| 2 — Internacional | 3000.00 | 1 — Another city |
| 1 — Grêmio | 4000.00 | 1 — Another city |
| 3 — Other clubs | 1500.00 | 0 — Porto Alegre |

The expected results are:

| Result | Value |
|---|---|
| Grêmio supporters | 2 |
| Internacional supporters | 1 |
| Other-club supporters | 1 |
| Average salary of Grêmio supporters | R$3000.00 |
| Average salary of Internacional supporters | R$3000.00 |
| Respondents born in Porto Alegre who support other clubs | 1 |
| Total respondents | 4 |

## Output

Clearly label every result. Display average salaries in Brazilian reais with two decimal places.

## Submission

Submit the program’s source code. As an optional check, run the example and cases with no respondents or no supporters of one of the two main clubs, then compare the actual results with the expected results.