# TASK410 — CSP Report

## 1. Context and scope

**Task:** Football Preferences Survey.  
**Author:** professor from Univasf.  
**Target audience:** learners in introductory programming.

The learner must develop a program that processes an unknown number of survey respondents in Porto Alegre. Each record contains a preferred club (`1` — Grêmio, `2` — Internacional, `3` — other clubs), a nonnegative salary and a birthplace code (`0` — Porto Alegre, `1` — another city).

Club code `0` ends input before salary or birthplace is requested. The termination entry is not a respondent. All inputs are assumed valid, and each record represents a different respondent. Fractional salaries and zero salaries are allowed.

The program displays supporter counts for the three club categories, separate average salaries for Grêmio and Internacional supporters, the number born in Porto Alegre who support other clubs, and the total respondents. Averages include zero salaries and are displayed in Brazilian reais with two decimal places. An empty club category produces `No respondents in this category` instead of an average. Immediate termination produces zero counts and this message for both averages.

The required deliverable is source code. Verification using the example and empty-category cases is optional. Functions, arrays, storage of all records, input validation and individual explanations are not required.


## 2. Knowledge mobilized

The Algorithms and Programming Logic course plan used in TASK401 remains a terminology reference.

| ID | Knowledge area | TASK410 application |
|---|---|---|
| K03 | Data types, constants and variables | Represent club and birthplace codes, integer counts, salaries, sums and averages |
| K04 | Arithmetic and literal expressions | Increment counts, accumulate salaries and calculate group averages |
| K05 | Assignment statements | Initialize and update counters, sums and input values |
| K06 | Input and output statements | Read records and present labeled results and formatted averages |
| K07 | Relational and logical operators | Recognize termination, select groups, combine birthplace and club conditions, and check nonzero counts |
| K08 | Decision structures | Select updates and choose between calculating an average and displaying an empty-category message |
| K09 | Repetition structures | Process respondents until club code `0` is entered |
| K12 | Software testing | Compare expected and actual results when optional verification is performed |

Counters, salary accumulators, arithmetic means and zero-denominator checks remain details within these existing topics. No new knowledge identities are proposed.

## 3. Learning objectives

| Objective | Bloom level | Competency |
|---|---|---|
| Read respondent data and display the complete summary | Apply | CM05 |
| Select category updates and protect average calculations for empty groups | Apply | CM03 |
| Process an unknown number of records with correct sentinel termination | Apply | CM04 |
| Accumulate counts and salaries and calculate separate group averages | Apply | CM20 |
| Optionally execute cases and judge agreement between expected and actual results | Apply and Evaluate | CM08 |

## 4. Reused competencies

CM03, CM04, CM05 and CM08 are reused from TASK401; CM20 is reused from TASK403. 

Their definitions and complete constitutive knowledge–Bloom pairings are preserved, following the approach used in TASK406. 

Only manifestations and evidence are contextualized. No new competencies are proposed.

### CM03 — Implement decisions with Boolean conditions

**Definition:** implement Boolean conditions and conditional branches that select actions according to specified rules.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K07 — Relational and logical operators | Apply | Construct Boolean conditions using comparisons and logical combinations |
| K08 — Decision structures | Apply | Implement conditional branches that execute the appropriate actions according to condition results |

**Manifestation and evidence:** source code selects the appropriate club count and salary sum, counts Porto Alegre-born respondents only when their club code is `3`, and calculates each average only when its group's count is positive. Empty categories produce the specified message without division by zero.

**Disposition:** meticulous.

### CM04 — Implement repetition with a stopping condition

**Definition:** implement repeated execution controlled by a condition or iteration limit, updating control values when required.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K09 — Repetition structures | Apply | Implement loops with appropriate continuation and stopping conditions |
| K05 — Assignment statements, when required | Apply | Initialize and update values used to control repetition |

**Manifestation and evidence:** source code reads successive club codes, processes each complete respondent once and stops at `0` without requesting further fields or updating respondent totals. Immediate termination still produces the complete summary.

**Disposition:** meticulous and persistent.

### CM05 — Implement input and output interaction

**Definition:** implement input and output operations that obtain data and communicate information clearly.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K06 — Input and output statements | Apply | Implement operations that receive data and present information |
| K03 — Data types, constants and variables | Apply | Represent received and displayed values using appropriate data types |

**Manifestation and evidence:** source code receives the three fields using the stated codes and supports fractional salaries. Output clearly labels the three supporter counts, two average results or messages, the birthplace-and-club count and total respondents. Numeric averages are shown in reais with two decimal places.

**Disposition:** considerate and meticulous.

### CM20 — Implement numeric calculations

**Definition:** implement numeric calculations using suitable variable types, arithmetic expressions and assignments.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K03 — Data types, constants and variables | Apply | Represent numeric inputs and results using appropriate types and variables |
| K04 — Arithmetic and literal expressions | Apply | Encode a calculation with appropriate operands and operator precedence |
| K05 — Assignment statements | Apply | Assign inputs, intermediate values and results to the appropriate variables |

**Manifestation and evidence:** source code initializes counts and salary sums to zero and updates them consistently. Each average uses its own club's salary sum divided by its supporter count, preserving fractional results. Respondents with zero salaries still increase their club's count. Other-club salaries do not enter either main-club average. The total equals the sum of the three category counts.

**Disposition:** meticulous.

### CM08 — Verify program behavior with test cases

**Activation:** optional.

**Definition:** use test cases to compare observed and expected behavior and judge conformity to specified requirements.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K12 — Software testing | Apply | Execute representative test cases with specified inputs and expected results |
| K12 — Software testing | Evaluate | Judge conformity to requirements by comparing observed and expected results |

**Manifestation and evidence:** optional records compare the supplied example's counts and averages, immediate termination and cases with no supporters of one main club. They check the expected empty-category messages and conclude whether behavior meets the specification. Running the program without comparison and judgment does not demonstrate the complete competency.

**Disposition:** meticulous and persistent.

## 5. Activation and performance criteria

| Code | Constraint | Mode | Role | Requirement or condition |
|---|---|---|---|---|
| CM03 | mandatory | constructive | core | Select category updates and handle empty groups before division |
| CM04 | mandatory | constructive | core | Process records until club code `0` |
| CM05 | mandatory | constructive | core | Read the survey data and display all required results |
| CM20 | mandatory | constructive | core | Accumulate counts and salary sums and calculate group averages |
| CM08 | optional | operational;evaluative | supporting | Perform and evaluate optional verification |

`mandatory` denotes a task requirement; `optional` denotes elective verification. There are five direct associations: four mandatory and one optional, with no competency composition.

**Expected performance:** the program counts each respondent once, excludes the sentinel, maintains correct club totals and calculates separate averages using all corresponding salaries, including zero. It counts Porto Alegre-born other-club supporters correctly and handles empty input or empty categories without division by zero. All outputs are labeled, and numeric averages have two decimal places.

For the supplied example, the club counts are 2, 1 and 1; both main-club averages are R$3000.00; the Porto Alegre-born other-club count is 1; and total respondents are 4.

Source code is the main evidence of construction. Optional execution records strengthen behavioral verification. Intended activation does not, by itself, establish individual learner mastery.


