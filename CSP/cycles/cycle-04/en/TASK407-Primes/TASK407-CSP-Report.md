# TASK407 — CSP Report

## 1. Context and scope

**Task:** Prime Numbers and Their Smallest Divisors.  
**Target audience:** learners in introductory programming.

The learner must develop a program that repeatedly reads an integer `n`. For each positive value, it reports whether the value is prime. For a composite value, it reports the smallest positive divisor greater than 1. For 1, it states that the value is not prime and has no positive divisor greater than 1.

Input ends when `n ≤ 0`. The termination value must not be evaluated. All inputs are assumed to be valid integers.

The learner may research primality-checking algorithms. Source code must include comments explaining how divisors are checked, when the search stops and how prime values and 1 are handled. Any external source used must be identified in a comment. The selected implementation must produce the smallest divisor for composite values, even if the primality algorithm does not directly supply it.

The required deliverable is commented source code. Running the supplied example and comparing results is optional. Functions, arrays, a separate research report, an oral explanation and formal complexity analysis are not required. No particular primality algorithm is prescribed.


## 2. Knowledge mobilized

Identifiers and curricular granularity follow the previous reports. Programming topics retain the Algorithms and Programming Logic course-plan terminology used in TASK401.

| ID | Knowledge area | TASK407 application |
|---|---|---|
| K03 | Data types, constants and variables | Represent the integer input, candidate divisors and calculation or control values |
| K04 | Arithmetic and literal expressions | Implement divisibility calculations and candidate updates where used |
| K05 | Assignment statements | Store inputs and initialize and update search values |
| K06 | Input and output statements | Read successive integers and communicate classifications and divisors |
| K07 | Relational and logical operators | Express divisibility, classification and stopping conditions |
| K08 | Decision structures | Distinguish 1, prime values and composite values |
| K09 | Repetition structures | Repeat input and, where used, search for divisors |
| K12 | Software testing | Compare expected and actual behavior when optional verification is performed |
| K15 | Code comments | Document how the implemented algorithm operates and identify external sources when used |

Primality and divisibility form the mathematical context. Remainder operations and candidate-search limits are implementation details within the existing topics. No new knowledge or competency identity is proposed. K15 identifies the required documentation medium; the explanatory performances are specified through CM14 and CM15.


## 3. Learning objectives

| Objective | Bloom level | Competency |
|---|---|---|
| Read successive inputs and display the appropriate result | Apply | CM05 |
| Implement decisions for primality, composite values and the special case 1 | Apply | CM03 |
| Repeat processing while inputs are positive and terminate correctly | Apply | CM04 |
| Implement numeric operations needed for divisibility and divisor identification | Apply | CM20 |
| Explain the conditions that determine classification and divisor acceptance | Understand | CM14 |
| Explain repeated processing and the algorithm's continuation and stopping rules | Understand | CM15 |
| Optionally execute examples and judge agreement between expected and actual behavior | Apply and Evaluate | CM08 |


## 4. Reused competencies

CM03, CM04, CM05 and CM08 are reused from TASK401; CM14 and CM15 from the TASK401 adjustment; CM20 from TASK403. Their definitions and complete constitutive knowledge–Bloom pairings are preserved. Only manifestations and evidence are contextualized.

### CM03 — Implement decisions with Boolean conditions

**Definition:** implement Boolean conditions and conditional branches that select actions according to specified rules.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K07 — Relational and logical operators | Apply | Construct Boolean conditions using comparisons and logical combinations |
| K08 — Decision structures | Apply | Implement conditional branches that execute the appropriate actions according to condition results |

**Manifestation and evidence:** source code distinguishes 1, primes and composites. Divisor acceptance and classification conditions implement the mathematical rules. The smallest-divisor result is produced only for composite values; neither 1 nor a termination value is incorrectly classified as prime.

**Disposition:** meticulous.

### CM04 — Implement repetition with a stopping condition

**Definition:** implement repeated execution controlled by a condition or iteration limit, updating control values when required.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K09 — Repetition structures | Apply | Implement loops with appropriate continuation and stopping conditions |
| K05 — Assignment statements, when required | Apply | Initialize and update values used to control repetition |

**Manifestation and evidence:** source code processes positive inputs and reads another value after each result. Zero or a negative input stops processing immediately. Any iterative divisor search advances correctly and terminates according to the selected algorithm. Search state is initialized for each new input so previous results do not affect subsequent classifications.

**Disposition:** meticulous and persistent.

### CM05 — Implement input and output interaction

**Definition:** implement input and output operations that obtain data and communicate information clearly.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K06 — Input and output statements | Apply | Implement operations that receive data and present information |
| K03 — Data types, constants and variables | Apply | Represent received and displayed values using appropriate data types |

**Manifestation and evidence:** source code receives integer values and clearly identifies each prime classification or smallest-divisor result. For 1, the output states both that it is not prime and that it has no positive divisor greater than 1. Termination values receive no primality evaluation.

**Disposition:** considerate and meticulous.

### CM20 — Implement numeric calculations

**Definition:** implement numeric calculations using suitable variable types, arithmetic expressions and assignments.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K03 — Data types, constants and variables | Apply | Represent numeric inputs and results using appropriate types and variables |
| K04 — Arithmetic and literal expressions | Apply | Encode a calculation with appropriate operands and operator precedence |
| K05 — Assignment statements | Apply | Assign inputs, intermediate values and results to the appropriate variables |

**Manifestation and evidence:** source code implements the selected algorithm's numeric operations correctly. For a divisor-based approach, integer remainder calculations, candidate updates and any search-bound expressions agree with the intended operations. A reported divisor divides `n` exactly and is the smallest divisor greater than 1. An alternative primality algorithm must be complemented by correct smallest-divisor identification.

**Disposition:** meticulous.

### CM14 — Explain conditional execution

**Definition:** explain how Boolean conditions determine the actions executed by conditional structures.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K07 — Relational and logical operators | Understand | Explain how comparisons and logical combinations determine a condition's truth value |
| K08 — Decision structures | Understand | Explain how condition results determine which branch is executed |

**Manifestation and evidence:** code comments explain how the implemented checks distinguish prime values, composite values and 1, and how a divisor is accepted. The account relates conditions to their consequences and explains how the smallest-divisor requirement is satisfied. Comments that merely restate statement syntax or label a branch do not establish the complete explanation.

**Disposition:** communicative and meticulous.

### CM15 — Explain repeated execution

**Definition:** explain how repetition structures control repeated execution and determine when it continues or stops.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K09 — Repetition structures | Understand | Explain the repeated action and the condition or iteration limit governing continuation and termination |

**Manifestation and evidence:** code comments explain the positive-input processing loop and the search's stopping rule. Where the selected algorithm uses repeated divisor checks, comments identify the candidate progression and explain when and why further checks stop. The explanation agrees with the actual implementation; it need not describe an algorithm that was not used.

**Disposition:** communicative and meticulous.

### CM08 — Verify program behavior with test cases

**Activation:** optional.

**Definition:** use test cases to compare observed and expected behavior and judge conformity to specified requirements.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K12 — Software testing | Apply | Execute representative test cases with specified inputs and expected results |
| K12 — Software testing | Evaluate | Judge conformity to requirements by comparing observed and expected results |

**Manifestation and evidence:** optional records compare the supplied sequence's expected and actual results: 7 is prime; 12 has smallest divisor 2; 25 has smallest divisor 5; 1 receives its special message; and 0 ends processing without evaluation. A conclusion states whether the behavior meets the specification. Additional cases may strengthen verification but are not extra mandatory deliverables. Execution alone does not establish comparison and judgment.

**Disposition:** meticulous and persistent.

## 5. Activation and performance criteria

| Code | Constraint | Mode | Role | Requirement or condition |
|---|---|---|---|---|
| CM03 | mandatory | constructive | core | Implement classification and divisor-selection decisions |
| CM04 | mandatory | constructive | core | Repeat processing and stop at a nonpositive input |
| CM05 | mandatory | constructive | core | Read inputs and display the required results |
| CM20 | mandatory | constructive | core | Implement numeric operations and smallest-divisor identification |
| CM14 | mandatory | explanatory | supporting | Explain classification and divisor-selection conditions in comments |
| CM15 | mandatory | explanatory | supporting | Explain repetition and stopping rules in comments |
| CM08 | optional | operational;evaluative | supporting | Perform and evaluate optional verification |

`mandatory` denotes a task requirement; `optional` denotes elective verification. There are seven direct associations: six mandatory and one optional, with no competency composition. Explanatory evidence is collected through the required comments rather than an additional oral or written assessment.

**Expected performance:** every positive input receives the correct result; composites receive their smallest divisor greater than 1; 1 is handled separately; and nonpositive inputs terminate processing without evaluation. Code comments accurately explain the checks and stopping rules. If external sources are used, comments identify them. Optional verification compares outcomes and supports a correctness judgment.

Correct output alone does not establish CM14 or CM15. Conversely, an accurate explanation does not establish a correct implementation. Code and comments provide complementary evidence of the constructive and explanatory performances. These specifications describe intended performances and do not, by themselves, establish individual learner mastery.

