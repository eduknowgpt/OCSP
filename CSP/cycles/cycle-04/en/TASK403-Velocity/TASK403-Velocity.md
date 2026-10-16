### TASK403: A Program to Explore the Average Velocity Formula

Author: Prof. Margeylson Graça, IFBA – Valença Campus

#### 1. Pedagogical Context

The school’s Physics teacher has invited you to collaborate on an interdisciplinary activity to help students understand **average velocity**, focusing on **reasoning about the formula** rather than performing manual calculations.

The idea is to create an **interactive program** that allows students to explore the relationship between **displacement (Δs)**, **time interval (Δt)**, and **average velocity (Vₘ)**.

Students should investigate this relationship and answer: **how can one of these quantities be calculated when the other two are known?**

To simplify the activity, consider straight-line motion without changes in direction, oriented in the positive direction of the reference frame. In this case, displacement has the same numerical value as the distance traveled. Only positive values will be used; this is a restriction of the activity, not a general rule for all motion.

#### 2. Task Objective

Develop a program that allows the user to **provide two of the three values** — Vₘ, Δs, and Δt — and **automatically calculates the third**, reinforcing:

- understanding of the relationship between the quantities;
- rearranging formulas to isolate a variable;
- using conditional structures and repetition loops.

#### 3. Problem Description

You accepted the collaboration under the following condition:

> The program must allow the user to enter exactly two values among average velocity, displacement, and time interval, marking the unknown quantity. The system must identify and calculate the missing value.

#### 4. Activity Requirements

**4.1. Conceptual Study**

Before implementing the program, the student must:

1. **Investigate how average velocity is calculated**, interpreting the physical meaning of Vₘ, Δs, and Δt.
2. **Study how to rearrange the formula** to calculate:
   - Δs from Vₘ and Δt;
   - Δt from Δs and Vₘ;
   - Vₘ from Δs and Δt.

The rearranged formulas must be documented in writing or in code comments.

**4.2. Functional Requirements**

The program must:

1. Request input for the three quantities:
   - average velocity (Vₘ);
   - displacement (Δs);
   - time interval (Δt).

2. Allow the user to enter **exactly two positive numeric values** and mark the third quantity as unknown.
   - The student must choose how the unknown value is marked and explain this in the program’s messages: an empty input, a special character, or `0`.
   - If `0` is chosen, it must serve exclusively as a marker for a missing value, not as data used in the calculation.

3. Identify the unknown quantity and calculate its value using the appropriate rearrangement.

4. Display:
   - the calculated quantity;
   - the numeric result;
   - the corresponding unit.

Use a fixed set of units and state it in the program’s messages, for example: **kilometers, hours, and kilometers per hour**, or **meters, seconds, and meters per second**. Unit conversion is not required.

**4.3. Validation and Error Handling**

The program must use **conditional structures** to check that:

- the two supplied values are numeric and greater than zero;
- exactly one quantity has been marked as unknown;
- the denominators used in the calculations are nonzero.

If the user supplies fewer than two valid values, provides all three quantities, or enters invalid input, the program must **display guidance and request the inputs again without performing the calculation**.

If `0` is the chosen marker, it must be identified as an unknown value before validating the numeric data.

Optionally, include educational messages explaining the restrictions, such as “The time interval must be greater than zero” or “Use only positive values in this activity.”

**4.4. Repetition**

The program must support **multiple calculations without being restarted**.

1. Use a **repetition loop** to:
   - request input;
   - validate the values;
   - calculate and display the result when the inputs are valid;
   - allow another attempt or a new calculation.

2. Define an exit command and clearly indicate when it can be used. For example, entering `f` in the first field of each new attempt.

When the command is recognized, the program must display a farewell message and exit without requesting the remaining values.

The exit command must differ from the marker used for the unknown quantity.

#### 5. Expected Deliverables

The student must submit:

1. **Program source code**, with brief comments explaining:
   - the calculations performed;
   - the formula rearrangements;
   - input validation.

2. **A brief written description**, in a `.md` file or code comment, containing:
   - the logic used to identify the unknown quantity;
   - the chosen marker and exit command;
   - the units and validation criteria;
   - usage examples with inputs and outputs.

3. **Optional but desirable:** test cases showing:
   - the two supplied values and the unknown quantity;
   - the expected result;
   - the actual result;
   - examples of invalid input and the program’s response.