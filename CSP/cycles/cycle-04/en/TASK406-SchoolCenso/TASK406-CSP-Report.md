# TASK406 — CSP Report

Author: Edeyson Gomes

Contributor: Jéssica Santana, Marcos Bião

## 1. Context and scope

**Task:** School Census.  
**Target audience:** learners in introductory programming.

The learner must develop a program that reads student records containing a name, sex (`M` or `F`) and three independent Boolean values indicating myopia, hypermetropia and astigmatism. Input ends when the name `FIM` is entered. The program must check this sentinel before requesting the remaining fields and must not count it as a student.

The final summary includes total students, boys and girls; totals and sex-specific counts for each condition; the number with at least one condition; the three pairwise condition counts; and the number with all three conditions. This produces 17 labeled counts.

Conditions may overlap. A student is counted once within each applicable category. Pairwise counts include students with all three conditions, while the at-least-one count includes each qualifying student only once. 

All records are assumed valid, and each represents a different student. Input validation, duplicate detection, percentages, functions and storage of the complete collection are not required. Records can be processed individually using running counters.

The required deliverable is source code. Running the supplied example and the immediate-termination case and comparing their results is optional. No individual explanation or written design justification is required.


## 2. Knowledge mobilized

Programming topics retain the Algorithms and Programming Logic course-plan terminology used in TASK401.

| ID | Knowledge area | TASK406 application |
|---|---|---|
| K03 | Data types, constants and variables | Represent names, sex codes, independent Boolean values and integer counters |
| K04 | Arithmetic and literal expressions | Increment counters and calculate totals where appropriate |
| K05 | Assignment statements | Initialize counters to zero and update values for each record |
| K06 | Input and output statements | Read the sentinel and student fields and display labeled summary counts |
| K07 | Relational and logical operators | Compare the name and sex codes and express inclusive OR and AND conditions |
| K08 | Decision structures | Select which counters to update according to each student's attributes |
| K09 | Repetition structures | Process records until the sentinel is entered |
| K12 | Software testing | Compare expected and actual behavior when optional verification is performed |

Inclusive OR, conjunction and overlapping categories are operational details within K07 and K08. Counter accumulation remains within K03–K05. 
The task uses reported condition indicators as input; it does not require medical interpretation or diagnosis. No new knowledge identities are needed.


## 3. Learning objectives

| Objective | Bloom level | Competency |
|---|---|---|
| Read records and display all required labeled counts | Apply | CM05 |
| Implement conditions for sex-specific, individual-condition and combined-condition counts | Apply | CM03 |
| Process records until `FIM`, including immediate termination | Apply | CM04 |
| Initialize and update counters to produce correct totals | Apply | CM20 |
| Optionally execute cases and judge agreement between expected and actual behavior | Apply and Evaluate | CM08 |



## 4. Reused competencies

CM03, CM04, CM05 and CM08 are reused from TASK401; CM20 is reused from TASK403. 

Their definitions and complete constitutive knowledge–Bloom pairings are preserved, as in TASK404 and TASK405. Only manifestations and evidence are contextualized.

No new competencies are proposed.


### CM03 — Implement decisions with Boolean conditions

**Definition:** implement Boolean conditions and conditional branches that select actions according to specified rules.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K07 — Relational and logical operators | Apply | Construct Boolean conditions using comparisons and logical combinations |
| K08 — Decision structures | Apply | Implement conditional branches that execute the appropriate actions according to condition results |

**Manifestation and evidence:** source code implements the sex comparisons and Boolean conditions needed for all categories. It uses inclusive OR for at least one condition and AND for pairwise and triple combinations. A student with all three conditions contributes to every applicable category, including each pairwise count. The at-least-one counter is incremented only once per qualifying student. Decision logic permits overlapping condition categories rather than treating them as mutually exclusive.

**Disposition:** meticulous.


### CM04 — Implement repetition with a stopping condition

**Definition:** implement repeated execution controlled by a condition or iteration limit, updating control values when required.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K09 — Repetition structures | Apply | Implement loops with appropriate continuation and stopping conditions |
| K05 — Assignment statements, when required | Apply | Initialize and update values used to control repetition |

**Manifestation and evidence:** source code reads successive names and processes student fields only when the name differs from `FIM`. Each complete record is processed once. Reading the sentinel terminates input without requesting other fields or updating student counters. Immediate termination still produces the final zero-valued summary.

**Disposition:** meticulous and persistent.



### CM05 — Implement input and output interaction

**Definition:** implement input and output operations that obtain data and communicate information clearly.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K06 — Input and output statements | Apply | Implement operations that receive data and present information |
| K03 — Data types, constants and variables | Apply | Represent received and displayed values using appropriate data types |

**Manifestation and evidence:** source code receives the name, sex and three separate Boolean values for each student and presents all 17 counts with clear labels. The input representation distinguishes true from false, and the output distinguishes overall counts, boys, girls and condition combinations. A particular table layout is not required.

**Disposition:** considerate and meticulous.



### CM20 — Implement numeric calculations

**Definition:** implement numeric calculations using suitable variable types, arithmetic expressions and assignments.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K03 — Data types, constants and variables | Apply | Represent numeric inputs and results using appropriate types and variables |
| K04 — Arithmetic and literal expressions | Apply | Encode a calculation with appropriate operands and operator precedence |
| K05 — Assignment statements | Apply | Assign inputs, intermediate values and results to the appropriate variables |

**Manifestation and evidence:** source code uses integer counters initialized to zero and correct arithmetic updates. Counters retain accumulated values between records. Totals may be maintained directly or derived from appropriate component counts. Adding the three individual-condition totals is not a valid way to obtain the at-least-one total when conditions overlap. No separate numeric input field is required; the numeric operands are counts accumulated from the records.

**Disposition:** meticulous.


### CM08 — Verify program behavior with test cases

**Activation:** optional.

**Definition:** use test cases to compare observed and expected behavior and judge conformity to specified requirements.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K12 — Software testing | Apply | Execute representative test cases with specified inputs and expected results |
| K12 — Software testing | Evaluate | Judge conformity to requirements by comparing observed and expected results |

**Manifestation and evidence:** optional records compare all summary counts for the supplied example and confirm that immediate `FIM` produces zeros without requesting other fields. The example includes a student with no conditions and one with all three, exposing overlap and double-counting errors. Records conclude whether observed behavior meets the specification. Execution alone, without comparison and judgment, does not demonstrate the complete competency.

**Disposition:** meticulous and persistent.



## 5. Activation and performance criteria

| Code | Constraint | Mode | Role | Requirement or condition |
|---|---|---|---|---|
| CM03 | mandatory | constructive | core | Implement the Boolean decisions for all counting categories |
| CM04 | mandatory | constructive | core | Process records and stop correctly at `FIM` |
| CM05 | mandatory | constructive | core | Read student data and display the complete labeled summary |
| CM20 | mandatory | constructive | core | Initialize, accumulate and calculate correct counts |
| CM08 | optional | operational;evaluative | supporting | Perform and evaluate optional verification |

`mandatory` denotes a task requirement; `optional` denotes elective verification. 

There are five direct associations: four mandatory and one optional, with no competency composition. 

CM03 addresses category selection, CM04 repetition and termination, and CM20 numeric accumulation; these are distinct aspects of the same program.

**Expected performance:** the program processes every student once, excludes the sentinel and displays all 17 correct counts. 
Individual conditions can overlap; pairwise counts include the triple intersection; the inclusive-OR count avoids duplicate contributions. 
All outputs are zero when no records are entered. 
Optional verification compares observed and expected results and supports a correctness judgment.

> Source code is the main evidence of construction. 

Execution records strengthen behavioral verification. These specifications describe intended performances and do not, by themselves, establish individual learner mastery.

