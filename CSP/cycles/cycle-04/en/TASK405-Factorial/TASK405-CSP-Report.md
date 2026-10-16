# TASK405 — CSP Report

## 1. Context and scope

**Task:** Calculating Factorials Using Functions and Loops.  
**Author:** Marco Bião.  
**Target audience:** learners in introductory programming.

The learner must develop a program that reads a positive integer `n` and processes `n` valid nonnegative integer values. For each value `x`, the program calls a separate function named `factorial(x)`, which calculates the factorial using a loop and returns the result. The program displays each result as `x! = result`.

Negative values must produce an error message and a request for a replacement. Rejected values do not count toward the `n` values to be processed. The calculation must handle `0! = 1` correctly.

The task assumes that `n` is positive and all subsequent inputs are integers. Validation of nonnumeric input or of the initial count is not an additional requirement. Large-number handling and a stored-results summary are optional extensions.

The required deliverable is source code. Running the example and comparing results is optional. Individual explanations, execution tracing and a written design justification are not required.

## 2. Knowledge mobilized

Identifiers and curricular granularity follow the previous reports. Programming topics retain the Algorithms and Programming Logic course-plan terminology used in TASK401.

| ID | Knowledge area | TASK405 application |
|---|---|---|
| K03 | Data types, constants and variables | Represent the count, input value, loop counters and integer results |
| K04 | Arithmetic and literal expressions | Calculate successive products and counter increments |
| K05 | Assignment statements | Initialize and update the accumulator, counters and results |
| K06 | Input and output statements | Read values and display error messages and factorial results |
| K07 | Relational and logical operators | Check nonnegativity and repetition conditions |
| K08 | Decision structures | Accept valid values and reject negative values |
| K09 | Repetition structures | Process the requested values, repeat rejected input and calculate factorials |
| K11 | Modularization: functions and parameter passing | Define and call the factorial function with a parameter and return value |
| K12 | Software testing | Compare expected and actual behavior when optional verification is performed |

Factorial is the mathematical context. Applying its supplied definition does not require a new mathematical competency. Accumulation and counter updates remain details within the existing curricular topics. Arrays or lists are not required by the baseline task.

## 3. Learning objectives

| Objective | Bloom level | Competency |
|---|---|---|
| Receive the count and values and display results and error messages | Apply | CM05 |
| Reject negative values before calculating their factorials | Apply | CM03 |
| Control processing, repeated input and iterative multiplication | Apply | CM04 |
| Implement factorial calculations using suitable variables, expressions and assignments | Apply | CM20 |
| Implement and invoke a function with a parameter and return value | Apply | CM23 |
| Optionally execute examples and judge agreement between expected and actual behavior | Apply and Evaluate | CM08 |

## 4. Competency specifications

CM03, CM04, CM05 and CM08 are reused from TASK401; CM20 is reused from TASK403. Their definitions and complete constitutive knowledge–Bloom pairings are preserved. Only manifestations and evidence are contextualized. CM23 is proposed as a new identity for bounded function implementation.

### CM03 — Implement decisions with Boolean conditions

**Definition:** implement Boolean conditions and conditional branches that select actions according to specified rules.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K07 — Relational and logical operators | Apply | Construct Boolean conditions using comparisons and logical combinations |
| K08 — Decision structures | Apply | Implement conditional branches that execute the appropriate actions according to condition results |

**Manifestation and evidence:** source code checks whether `x` is nonnegative and selects acceptance or rejection. Negative values receive an error message and are not passed to the factorial calculation. Simple comparisons suffice; unnecessary logical combinations are not required.

**Disposition:** meticulous.

### CM04 — Implement repetition with a stopping condition

**Definition:** implement repeated execution controlled by a condition or iteration limit, updating control values when required.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K09 — Repetition structures | Apply | Implement loops with appropriate continuation and stopping conditions |
| K05 — Assignment statements, when required | Apply | Initialize and update values used to control repetition |

**Manifestation and evidence:** source code processes exactly `n` valid values, requests replacements for negative inputs and uses a loop inside `factorial(x)`. Counters and stopping conditions prevent rejected inputs from consuming a valid-value position. The factorial loop terminates correctly, including for zero.

**Disposition:** meticulous and persistent.

### CM05 — Implement input and output interaction

**Definition:** implement input and output operations that obtain data and communicate information clearly.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K06 — Input and output statements | Apply | Implement operations that receive data and present information |
| K03 — Data types, constants and variables | Apply | Represent received and displayed values using appropriate data types |

**Manifestation and evidence:** source code reads `n` and each value individually, requests a replacement after rejection and displays valid results as `x! = result`. The output identifies the value being processed rather than the total input count.

**Disposition:** considerate and meticulous.

### CM20 — Implement numeric calculations

**Definition:** implement numeric calculations using suitable variable types, arithmetic expressions and assignments.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K03 — Data types, constants and variables | Apply | Represent numeric inputs and results using appropriate types and variables |
| K04 — Arithmetic and literal expressions | Apply | Encode a calculation with appropriate operands and operator precedence |
| K05 — Assignment statements | Apply | Assign inputs, intermediate values and results to the appropriate variables |

**Manifestation and evidence:** source code initializes the product to 1 and performs the successive multiplications needed to calculate `x!`. Each function call starts a fresh calculation, and zero returns 1. Results must be correct within the chosen numeric representation's supported range; handling values beyond that range remains an optional extension.

**Disposition:** meticulous.

### CM23 — Implement a function with parameters and a return value

**Status:** proposed new competency; not an equivalent or replacement for CM07.

**Definition:** implement and invoke a function with a specified responsibility, using parameters to receive data and a return value to provide its result.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K11 — Modularization: functions and parameter passing | Apply | Define and invoke a function that receives the required data through parameters and returns the result to its caller |

**Manifestation and evidence:** source code defines `factorial(x)`, receives the value through its parameter, calculates the factorial using a loop and returns the result. The calling code invokes the function for each accepted value and uses the returned result in the output. Printing a result inside the function without returning it does not satisfy the required contract.

**Disposition:** organized and meticulous.

**BNCC Computing alignment:**

| Framework reference | Relationship | Justification and scope |
|---|---|---|
| Computing-Specific Competency 1 for High School (CE1) | GeneralFrameworkAlignment | Implementing a specified function contributes to constructing a computational solution. CM23 alone does not establish analysis of computational feasibility, efficiency or limits. |
| Computing-Specific Competency 4 for High School (CE4) | GeneralFrameworkAlignment | Defining and integrating a function contributes to producing a computational artifact. The full creative, ethical and legal scope of CE4 is not assessed by this bounded implementation task. |
| EM13CO02 | NarrowerThanExternalAlignment | Translating a specified function responsibility into executable code, with parameter passing and a return value, contributes to refinement from specification to implementation. CM23 covers a bounded implementation step, not the complete exploration and construction of a solution through multiple levels of abstraction. |

In TASK405, the specification of `factorial(x)` establishes its input, responsibility and returned result; the source code realizes that contract and connects it to the caller. This is the task-specific evidence for the contribution to EM13CO02. The alignment does not raise the constitutive Bloom level above Apply or imply independent design of a modular architecture.



### CM08 — Verify program behavior with test cases

**Activation:** optional.

**Definition:** use test cases to compare observed and expected behavior and judge conformity to specified requirements.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K12 — Software testing | Apply | Execute representative test cases with specified inputs and expected results |
| K12 — Software testing | Evaluate | Judge conformity to requirements by comparing observed and expected results |

**Manifestation and evidence:** optional records compare expected and actual behavior for zero, positive values and a negative input followed by a valid replacement. They verify that exactly `n` valid results are produced and conclude whether the specification is met. Running the program without comparison and judgment does not demonstrate the complete competency.

**Disposition:** meticulous and persistent.


## 5. Activation and performance criteria

| Code | Constraint | Mode | Role | Requirement or condition |
|---|---|---|---|---|
| CM03 | mandatory | constructive | core | Accept nonnegative values and reject negative values |
| CM04 | mandatory | constructive | core | Control input processing, retries and factorial iteration |
| CM05 | mandatory | constructive | core | Read inputs and display results and error messages |
| CM20 | mandatory | constructive | core | Implement correct factorial calculations |
| CM23 | mandatory | constructive | core | Define and invoke the required function with parameter and return value |
| CM08 | optional | operational;evaluative | supporting | Perform and evaluate optional verification |

`mandatory` denotes a task requirement; `optional` denotes elective verification. There are six direct associations: five mandatory and one optional, with no competency composition. CM03 and CM04 cover different aspects of input handling: the acceptance decision and the repeated request.

**Expected performance:** the program produces exactly `n` valid factorial results, rejects negative inputs without counting them, calculates `0!` correctly and uses the required iterative function with parameter passing and return. Repeated calls produce independent, correct results within the supported numeric range. If optional verification is submitted, its records compare outcomes and support a correctness judgment.

Source code is the main evidence of construction. Execution records strengthen behavioral verification. These specifications describe intended performances and do not, by themselves, establish individual learner mastery.

