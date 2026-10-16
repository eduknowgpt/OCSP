# TASK409 — CSP Report

## 1. Context and scope

**Task:** Excess Fishing Weight.  
**Author:** Marcos Bião.  
**Target audience:** learners in introductory programming.

The task retains the original narrative about João Papo-de-Pescador, who needs a program to monitor his daily fishing yield. Within the exercise, the catch limit is 50 kilograms and the fine is R$4.00 per excess kilogram. These values are problem specifications, not a statement about current fishing regulations.

The learner must read the catch weight into `P`. If `P > 50`, the program stores the excess weight in `E` and the corresponding fine in `M`. Otherwise, both variables receive zero. The program displays the excess in kilograms and the fine in Brazilian reais, with the fine formatted to two decimal places.

Input is assumed to be a valid nonnegative number. Fractional weights are allowed, and the fine is proportional to the excess. Exactly 50 kilograms does not incur a fine.

The required deliverable is source code. Running the supplied examples and comparing results is optional. Input validation, repeated calculations, functions, arrays and individual explanations are not required.

## 2. Knowledge mobilized

Programming topics retain the Algorithms and Programming Logic course-plan terminology used in TASK401.

| ID | Knowledge area | TASK409 application |
|---|---|---|
| K03 | Data types, constants and variables | Represent `P`, `E` and `M`, preserving fractional weights and monetary values |
| K04 | Arithmetic and literal expressions | Calculate excess weight by subtraction and the fine by multiplication |
| K05 | Assignment statements | Store the input and assign either calculated values or zeros |
| K06 | Input and output statements | Read catch weight and display excess and fine with labels, units and monetary formatting |
| K07 | Relational and logical operators | Compare the catch weight with the 50-kilogram limit |
| K08 | Decision structures | Select the excess-weight calculation or the zero-value outcome |
| K12 | Software testing | Compare expected and actual results when optional verification is performed |

The weight limit and monetary rate provide the problem context. Fractional arithmetic, the strict comparison and decimal formatting remain details within these existing topics. No new knowledge or competency identities are proposed.



## 3. Learning objectives

| Objective | Bloom level | Competency |
|---|---|---|
| Read catch weight and display excess weight and the formatted fine | Apply | CM05 |
| Select the appropriate outcome according to whether the catch exceeds the limit | Apply | CM03 |
| Calculate and store excess weight and the proportional fine, or assign zeros | Apply | CM20 |
| Optionally run the examples and judge agreement between expected and actual results | Apply and Evaluate | CM08 |


## 4. Reused competencies

CM03, CM05 and CM08 are reused from TASK401; CM20 is reused from TASK403. Their definitions and complete constitutive knowledge–Bloom pairings are preserved, as in TASK404. Only manifestations and evidence are contextualized.

### CM03 — Implement decisions with Boolean conditions

**Definition:** implement Boolean conditions and conditional branches that select actions according to specified rules.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K07 — Relational and logical operators | Apply | Construct Boolean conditions using comparisons and logical combinations |
| K08 — Decision structures | Apply | Implement conditional branches that execute the appropriate actions according to condition results |

**Manifestation and evidence:** source code distinguishes `P > 50` from `P <= 50`. Only the first case produces positive excess and a fine; the second assigns zero to both `E` and `M`. A simple comparison is sufficient. The boundary value 50 must follow the no-excess outcome.

**Disposition:** meticulous.

### CM05 — Implement input and output interaction

**Definition:** implement input and output operations that obtain data and communicate information clearly.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K06 — Input and output statements | Apply | Implement operations that receive data and present information |
| K03 — Data types, constants and variables | Apply | Represent received and displayed values using appropriate data types |

**Manifestation and evidence:** source code reads a catch weight that may contain a fractional part and displays both `E` and `M`. Output identifies excess weight in kilograms and the fine in Brazilian reais, with two decimal places for the fine. Both values are displayed even when zero.

**Disposition:** considerate and meticulous.

### CM20 — Implement numeric calculations

**Definition:** implement numeric calculations using suitable variable types, arithmetic expressions and assignments.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K03 — Data types, constants and variables | Apply | Represent numeric inputs and results using appropriate types and variables |
| K04 — Arithmetic and literal expressions | Apply | Encode a calculation with appropriate operands and operator precedence |
| K05 — Assignment statements | Apply | Assign inputs, intermediate values and results to the appropriate variables |

**Manifestation and evidence:** source code stores the input in `P` and, when the limit is exceeded, calculates `E = P - 50` and `M = E × 4`. Otherwise, it assigns zero to both result variables. Numeric representation preserves fractional excess; the fine is calculated on the excess rather than the full catch weight. Formatting the output does not replace the required calculations and assignments.

**Disposition:** meticulous.

### CM08 — Verify program behavior with test cases

**Activation:** optional.

**Definition:** use test cases to compare observed and expected behavior and judge conformity to specified requirements.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K12 — Software testing | Apply | Execute representative test cases with specified inputs and expected results |
| K12 — Software testing | Evaluate | Judge conformity to requirements by comparing observed and expected results |

**Manifestation and evidence:** optional records compare expected and actual outputs for the supplied examples: `P = 40` and `P = 50` produce zero excess and zero fine; `P = 55` produces `E = 5` and `M = 20.00`; `P = 52.5` produces `E = 2.5` and `M = 10.00`. The record concludes whether the calculation, boundary handling and required monetary formatting meet the specification. Execution alone, without comparison and judgment, does not demonstrate the complete competency.

**Disposition:** meticulous and persistent.

## 5. Activation and performance criteria

| Code | Constraint | Mode | Role | Requirement or condition |
|---|---|---|---|---|
| CM03 | mandatory | constructive | core | Select excess or no-excess behavior using the stated limit |
| CM05 | mandatory | constructive | core | Read weight and display both labeled results with the required formatting |
| CM20 | mandatory | constructive | core | Calculate and store excess and fine, or assign zeros |
| CM08 | optional | operational;evaluative | supporting | Perform and evaluate optional verification |

`mandatory` denotes a task requirement; `optional` denotes elective verification. There are four direct associations: three mandatory and one optional, with no competency composition.

**Expected performance:** the program accepts fractional weights, applies the strict 50-kilogram threshold correctly, stores results in `E` and `M` and displays both with appropriate units. The fine is proportional only to the excess and is shown with two decimal places. Weights at or below the limit produce zero for both results. Optional verification compares outcomes and supports a correctness judgment.

Source code is the main evidence of construction. Execution records strengthen behavioral verification. These specifications describe intended performances and do not, by themselves, establish individual learner mastery.

