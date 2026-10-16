# TASK406 — School Census

Author: Edeyson Gomes

Contributor: Jéssica Santana, Marcos Bião

Write a program that reads student records and displays a summary of the collected data.

For each student, read:

- **Name**
- **Sex:** `M` for male or `F` for female
- **Myopia:** a Boolean value
- **Hypermetropia:** a Boolean value
- **Astigmatism:** a Boolean value

Each condition must be entered separately: `true` means the student has the condition, and `false` means the student does not.

Stop reading when the name `FIM` is entered. Check this name before requesting the remaining fields. The termination entry must not be counted as a student.

Assume that all student records contain valid inputs. Each record represents a different student, and a student may have more than one condition.

## Required results

After input ends, display:

| Category | Required counts |
|---|---|
| Students | Total students, total boys and total girls |
| Myopia | Total students, boys and girls with myopia |
| Hypermetropia | Total students, boys and girls with hypermetropia |
| Astigmatism | Total students, boys and girls with astigmatism |
| At least one condition | Students with myopia OR hypermetropia OR astigmatism |
| Myopia and hypermetropia | Students with both conditions |
| Myopia and astigmatism | Students with both conditions |
| Hypermetropia and astigmatism | Students with both conditions |
| All three conditions | Students with myopia AND hypermetropia AND astigmatism |

Count each student only once within each category. Pairwise counts include students who also have the third condition. For example, a student with all three conditions contributes to each individual-condition count, each pairwise count, the all-three count and the at-least-one count.

If `FIM` is entered before any student record, display zero for every count.

## Example

For the following records, followed by `FIM`:

| Name | Sex | Myopia | Hypermetropia | Astigmatism |
|---|---|---|---|---|
| Ana | F | true | false | true |
| Bruno | M | false | true | false |
| Carla | F | true | true | true |
| Diego | M | false | false | false |

The expected results are:

| Category | Total | Boys | Girls |
|---|---|---|---|
| Students | 4 | 2 | 2 |
| Myopia | 2 | 0 | 2 |
| Hypermetropia | 2 | 1 | 1 |
| Astigmatism | 2 | 0 | 2 |

| Combination | Count |
|---|---|
| At least one condition | 3 |
| Myopia and hypermetropia | 1 |
| Myopia and astigmatism | 2 |
| Hypermetropia and astigmatism | 1 |
| All three conditions | 1 |

Output formatting may vary, provided every count is clearly labeled.

## Submission

Submit the program’s source code. As an optional check, run the example and the case where `FIM` is entered immediately, then compare the actual results with the expected results.
