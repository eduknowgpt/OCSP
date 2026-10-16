# TASK404 — CSP Report

## 1. Context and scope

**Task:** Area of Regular Polygons.  
**Author:** Marco Bião.  
**Target audience:** learners in introductory programming.

The learner must develop a program that reads the number of sides and the side length of a regular polygon. For three sides, it displays TRIANGLE and the area; for four, SQUARE and the area; for five, only PENTAGON.

The simplified description assumes valid inputs: a number of sides equal to 3, 4, or 5 and a positive side length. This convention defines the input domain without adding error handling. The formulas are provided.

The required deliverable is the source code. Running the examples and comparing their results is optional. Loops, functions, arrays, individual explanations, and calculation of the pentagon’s area are not required.

## 2. Knowledge mobilized

The identifiers and curricular granularity are preserved from previous reports. Programming topics follow the Algorithms and Programming Logic course plan used as a reference in TASK401.

| ID | Knowledge area | TASK404 application |
|---|---|---|
| K03 | Data types, constants and variables | Represent the number of sides, side length and area, preserving fractional values |
| K04 | Arithmetic and literal expressions | Implement the triangle and square formulas |
| K05 | Assignment statements | Store inputs and results |
| K06 | Input and output statements | Read data and display the name and, when required, the area in cm² |
| K07 | Relational and logical operators | Compare the number of sides with the specified values |
| K08 | Decision structures | Select the corresponding output and calculation |
| K12 | Software testing | Compare expected and actual results when optional verification is performed |

Regular polygons, area and units of measurement constitute the mathematical context. The formulas are provided for application; the task does not require their derivation or a geometric explanation. Therefore, no new knowledge or competency identity is proposed for this context. Square roots and operator precedence are treated as implementation details of the numeric expression.

## 3. Learning objectives

| Objective | Bloom level | Competency |
|---|---|---|
| Implement input reading and output presentation | Apply | CM05 |
| Select behavior according to the number of sides | Apply | CM03 |
| Implement the formulas using appropriate types, expressions and assignments | Apply | CM20 |
| Optionally run examples and evaluate agreement between expected and actual results | Apply and Evaluate | CM08 |

## 4. Reused competencies

### CM03 — Implement decisions with Boolean conditions

**Definition:** implement Boolean conditions and conditional branches that select actions according to specified rules.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K07 — Relational and logical operators | Apply | Construct Boolean conditions using comparisons and logical combinations |
| K08 — Decision structures | Apply | Implement conditional branches that execute the appropriate actions according to condition results |

**Manifestation and evidence:** the code distinguishes the three possible numbers of sides and produces the corresponding output. For cases 3 and 4, it selects the appropriate formula; for case 5, it displays only PENTAGON. The task uses equality comparisons without requiring unnecessary logical combinations.

**Disposition:** meticulous.

### CM05 — Implement input and output interaction

**Definition:** implement input and output operations that obtain data and communicate information clearly.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K06 — Input and output statements | Apply | Implement operations that receive data and present information |
| K03 — Data types, constants and variables | Apply | Represent received and displayed values using appropriate data types |

**Manifestation and evidence:** the code receives the number of sides and the side length and displays the polygon’s name. For the triangle and square, it also displays the area labeled in cm². Input and output representations accommodate fractional measurements and areas.

**Disposition:** considerate and meticulous.

### CM20 — Implement numeric calculations

**Definition:** implement numeric calculations using suitable variable types, arithmetic expressions and assignments.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K03 — Data types, constants and variables | Apply | Represent numeric inputs and results using appropriate types and variables |
| K04 — Arithmetic and literal expressions | Apply | Encode a calculation with appropriate operands and operator precedence |
| K05 — Assignment statements | Apply | Assign inputs, intermediate values and results to the appropriate variables |

**Manifestation and evidence:** the code implements `A = (√3 / 4) × l²` and `A = l²`, storing the results appropriately. Integer division must not cause truncation in the triangle’s coefficient. The syntax must implement the intended operations in the chosen language; mathematical exponent notation does not prescribe a specific operator.

**Disposition:** meticulous.

### CM08 — Verify program behavior with test cases

**Activation:** optional.

**Definition:** use test cases to compare observed and expected behavior and judge conformity to specified requirements.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K12 — Software testing | Apply | Execute representative test cases with specified inputs and expected results |
| K12 — Software testing | Evaluate | Judge conformity to requirements by comparing observed and expected results |

**Manifestation and evidence:** when performed, verification records inputs, expected outputs and actual outputs for all three cases and concludes whether the program meets the specification. For the triangle, it accounts for numerical approximation and decimal formatting. Running the program alone, without comparison and judgment, does not demonstrate the complete competency.

**Disposition:** meticulous and persistent.

## 5. Activation and performance criteria

| Code | Constraint | Mode | Role | Requirement or condition |
|---|---|---|---|---|
| CM03 | mandatory | constructive | core | Select behavior for 3, 4 or 5 sides |
| CM05 | mandatory | constructive | core | Receive data and present the requested information |
| CM20 | mandatory | constructive | core | Correctly implement both area calculations |
| CM08 | optional | operational;evaluative | supporting | Perform and evaluate the optional verification |

Activation values follow the terminology of previous reports: `mandatory` denotes a task requirement and `optional` denotes the elective verification. There are four direct associations: three mandatory and one optional, with no competency composition.

**Expected performance:** the program reads both inputs, correctly selects each case, calculates the areas without inappropriate truncation and presents the requested outputs. If optional verification is submitted, its records compare results and support a conclusion about correctness.

Source code is the main evidence of construction. Execution records strengthen the analysis of behavior. These specifications describe intended performances; they do not, by themselves, establish individual learner mastery.