# CSP-Report  
**Task ID (suggested):** TASKxx.xx — Multiple-of-27 Check (C)  
**Task Title:** Verification of Divisibility by 27 in C (Validated Input)

---

## Introduction

Grounded in the principles of the **Competency Specification Process (CSP)**, this report documents the **Competency Authoring phase** applied to a learning task in introductory C programming focused on **input handling, basic validation, and conditional decision-making**.

The task requires learners to implement an interactive program that requests an **integer positive number** and determines whether the value is a **multiple of 27**, reporting an unambiguous result to the user. From a CSP perspective, the task provides a well-bounded scenario to elicit competencies across the **Knowledge–Skill–Disposition (K–S–D)** triad, combining:

- **Knowledge elements** related to integer data, sequential execution, divisibility, and the modulo operator;
- **Skills** evidenced through correct implementation of input, validation, and conditional logic;
- **Dispositions** reflected in attention to correctness, clarity, and responsible authorship of a functional artifact.

Accordingly, this task supports explicit alignment between task requirements, expected evidence, and competency activation within the CSP framework.

---

## 1. Instructional Entity Analysis

### Title

    Verification of Divisibility by 27 (Validated Integer Input)

### Description

Learners must develop a program in **C** that reads an **integer** from the user, verifies whether the input satisfies the requirement of being **positive**, and then determines whether the number is a **multiple of 27** using a computationally verifiable criterion (e.g., remainder of integer division). The program must present a clear message indicating whether the input value **is** or **is not** a multiple of 27.  
If the input is not positive, the program must handle this case explicitly (e.g., by reporting invalid input and prompting for a valid value, depending on the adopted approach).

### Solution Development Process

The expected learner approach involves the following stages:

- **Interpret the problem constraints**, identifying required properties: integer type, positivity, divisibility by 27, and clear output.
- **Define the control flow** (input → validation → divisibility check → output).
- **Implement validation logic** to ensure the program handles non-positive values as invalid.
- **Implement the divisibility rule** using the modulo operator and a conditional structure.
- **Test the program** with representative values (multiple, non-multiple, and invalid input) and refine messages and logic.

### Expected Outcomes

Learners are expected to produce:

- A **compilable and executable C program** that reads an integer input and outputs the correct result.
- Correct handling of the **positivity constraint**, with explicit behavior for invalid values.
- Correct use of conditional logic for divisibility checking and user feedback.
- A minimal set of **demonstrated test executions**, including at least one multiple of 27, one non-multiple, and one invalid value.

### Acquisition Context

This task is carried out in an introductory unit of **Programming Logic / C Programming**, typically in an early module of a **Technical Program in Informatics** (or first programming course at higher education level). It can be conducted in a laboratory environment using a standard C compiler (e.g., GCC) and terminal interaction.

### Target Audience Profile

- **Educational Level:** Introductory programming learners (technical or undergraduate).
- **Prior Knowledge:** Variables, integer types, assignment, basic input/output, and simple conditionals.
- **Programming Experience:** Beginner level with initial exposure to structured programming.
- **Learning Needs:** Practice in translating a simple mathematical condition into executable logic with validated input.

### Proficiency Scale

Performance can be rated using a **0.0–10.0** numeric scale (increments of 0.1), considering:

- **Technical correctness** (validation + divisibility logic),
- **Robustness** (explicit handling of invalid inputs),
- **Clarity of interaction** (unambiguous output),
- **Basic code organization** (readability and coherence).

---

## 2. Knowledge Enumeration

This section enumerates the **knowledge elements explicitly activated** by the task. Items are framed as **conceptual knowledge needed to support observable learner actions**, avoiding skills and dispositions.

### 2.1. Fundamentals of Programming

- **K1 — Variables and integer data types**
  - Understanding integer representation and declaration in C.
  - Distinguishing integer input from other numeric types.

- **K2 — Input and output in C**
  - Reading values from standard input and presenting results in standard output.
  - Understanding input formatting expectations for integers.

- **K3 — Sequential execution model**
  - Understanding that statements are executed in order and determine program flow.

### 2.2. Mathematical and Logical Foundations

- **K4 — Divisibility as a computational condition**
  - Understanding the notion of “multiple of 27” as a divisibility property.

- **K5 — Modulo operator and remainder of integer division**
  - Interpreting `n % 27 == 0` as “n is divisible by 27”.

- **K6 — Boolean conditions and conditional selection**
  - Understanding how Boolean expressions guide conditional execution (`if/else`).

### 2.3. Constraint and Validation

- **K7 — Input constraint: positivity**
  - Understanding the constraint “positive integer” as `n > 0`.
  - Recognizing invalid cases (zero and negative values) and the need for explicit handling.

**Analytical Note:**  
The listed knowledge elements are directly traceable to task requirements: reading integer input, validating positivity, computing divisibility by 27 via modulo, and producing a clear decision output.

---

## 3. Learning Objectives Identification

> **By the end of this task, the learner should be able to:**

1. **LO1 — Implement** a C program that reads an integer input and produces a decision output based on a numeric condition.
2. **LO2 — Validate** the positivity constraint (`n > 0`) and handle invalid inputs explicitly.
3. **LO3 — Apply** the modulo operator to determine whether a number is a multiple of 27 (`n % 27 == 0`).
4. **LO4 — Test** the program using representative inputs (multiple, non-multiple, invalid) and confirm output correctness.

**Analytical Note:**  
These objectives use observable verbs (implement, validate, apply, test) and map primarily to **Apply**, with supporting elements of **Analyze** when diagnosing invalid cases and verifying outcomes.

---

## 4. Competency Definition

## General Competency (BNCC – Computing in Basic Education)

- **Design and implement computational solutions** that read data, enforce constraints, and produce correct decisions using structured programming constructs, with clear communication and responsible authorship.

---

## Competency Cxx.xx.1 Specification

### Competency Title

    Validate integer input constraints in interactive C programs.

### Textual Description

This competency involves the ability to **read integer input**, verify whether it satisfies a stated constraint (here, **positivity**), and enforce the constraint through explicit program behavior. In this task, the learner must detect non-positive values and ensure the program responds consistently (e.g., indicating invalid input or requesting a valid value, depending on the chosen design).

The competency emphasizes **correct constraint interpretation**, **explicit checking**, and **coherent handling** of invalid cases in interactive programs.

### Knowledge Specification

- **Input and Output in C**
  - Understanding how integer input is captured and how feedback is communicated to the user.
  - **Bloom Alignment:** Apply  
  - **Knowledge–Skill Pairing:** Input/Output / Apply  
  - **Verb Annotation:** Read, Handle, Display

- **Constraint Interpretation (Positivity)**
  - Understanding the constraint “positive integer” and how to encode it as `n > 0`.
  - **Bloom Alignment:** Apply  
  - **Knowledge–Skill Pairing:** Constraints / Apply  
  - **Verb Annotation:** Validate, Check, Enforce

- **Conditional Structures**
  - Understanding how `if/else` supports enforcement of acceptance/rejection behavior.
  - **Bloom Alignment:** Apply  
  - **Knowledge–Skill Pairing:** Conditionals / Apply  
  - **Verb Annotation:** Select, Branch, Decide

### Disposition Specification

- **Meticulous** — checks constraints carefully and avoids accepting invalid inputs.
- **Responsible** — ensures program behavior is reliable and consistent in interaction.

### Summary Table

| **Code**    | **Competency**                                           | **Dispositions**             | **Knowledge**                         | **Skill**                          |
|------------|-----------------------------------------------------------|------------------------------|--------------------------------------|------------------------------------|
| Cxx.xx.1   | Validate integer input constraints in interactive programs | Meticulous, Responsible      | Input/Output in C                     | Apply (Read, Handle, Display)      |
|            |                                                           |                              | Constraint Interpretation (Positivity) | Apply (Validate, Check, Enforce)   |
|            |                                                           |                              | Conditional Structures                | Apply (Select, Branch, Decide)     |

### Activation Definition

- **ActivationConstraint:** `mandatory`  
  Input validation is required by the task statement (“integer and positive”) and must be enforced explicitly.

- **ActivationMode:** `constructive`  
  Learners construct validation logic within an executable program.

- **ActivationRole:** `core`  
  The competency directly determines whether the program meets task requirements.

---

## Competency Cxx.xx.2 Specification

### Competency Title

    Determine divisibility by a constant using modulo and conditional logic.

### Textual Description

This competency involves the ability to **translate a mathematical property (divisibility)** into a **computational decision rule**, using the modulo operator and conditional structures. In this task, the learner checks whether the validated integer input is a **multiple of 27** by evaluating whether the remainder of division by 27 equals zero, and then communicates the result clearly to the user.

The competency emphasizes correct application of **integer arithmetic**, **Boolean conditions**, and **decision output**.

### Knowledge Specification

- **Divisibility and Remainder**
  - Understanding “multiple of 27” as a remainder-based condition.
  - **Bloom Alignment:** Apply  
  - **Knowledge–Skill Pairing:** Divisibility / Apply  
  - **Verb Annotation:** Interpret, Determine

- **Modulo Operator**
  - Understanding `n % 27` as remainder and `== 0` as divisibility.
  - **Bloom Alignment:** Apply  
  - **Knowledge–Skill Pairing:** Integer Arithmetic / Apply  
  - **Verb Annotation:** Compute, Check, Apply

- **Conditional Decision and Output Messaging**
  - Understanding how to branch and output unambiguous results.
  - **Bloom Alignment:** Apply  
  - **Knowledge–Skill Pairing:** Conditionals + Output / Apply  
  - **Verb Annotation:** Decide, Report, Inform

### Disposition Specification

- **Precise** — uses correct computational criteria and avoids ambiguous outputs.
- **Meticulous** — verifies logic correctness through representative tests.

### Summary Table

| **Code**    | **Competency**                                                | **Dispositions**          | **Knowledge**                       | **Skill**                           |
|------------|----------------------------------------------------------------|---------------------------|--------------------------------------|-------------------------------------|
| Cxx.xx.2   | Determine divisibility by a constant using modulo and conditionals | Precise, Meticulous       | Divisibility and Remainder           | Apply (Interpret, Determine)        |
|            |                                                                |                           | Modulo Operator                      | Apply (Compute, Check, Apply)       |
|            |                                                                |                           | Conditional Decision + Output         | Apply (Decide, Report, Inform)      |

### Activation Definition

- **ActivationConstraint:** `mandatory`  
  Divisibility checking is the central requirement of the task.

- **ActivationMode:** `constructive`  
  Learners implement the computational rule within an executable artifact.

- **ActivationRole:** `core`  
  The competency is the primary determinant of functional correctness.

---

## Competency Cxx.xx.3 Specification

### Competency Title

    Test interactive programs with representative inputs.

### Textual Description

This competency involves the ability to **select and execute representative test inputs** to verify program behavior across distinct cases. In this task, the learner must test at least one value that is a multiple of 27, one that is not, and one invalid value (non-positive), confirming that the program produces correct and coherent outputs in each scenario.

The competency emphasizes systematic checking of **expected behavior** and detection of inconsistencies between requirements and observed results.

### Knowledge Specification

- **Basic Testing Notions**
  - Understanding test cases as representative inputs linked to expected outputs.
  - **Bloom Alignment:** Apply  
  - **Knowledge–Skill Pairing:** Testing / Apply  
  - **Verb Annotation:** Test, Verify, Check

- **Edge/Invalid Case Recognition**
  - Understanding invalid inputs (≤ 0) as boundary cases requiring verification.
  - **Bloom Alignment:** Analyze  
  - **Knowledge–Skill Pairing:** Case Analysis / Analyze  
  - **Verb Annotation:** Identify, Distinguish, Confirm

### Disposition Specification

- **Systematic** — tests across required categories rather than using a single example.
- **Persistent** — revises logic when test outputs contradict requirements.

### Summary Table

| **Code**    | **Competency**                                     | **Dispositions**        | **Knowledge**                   | **Skill**                            |
|------------|-----------------------------------------------------|--------------------------|----------------------------------|--------------------------------------|
| Cxx.xx.3   | Test interactive programs with representative inputs | Systematic, Persistent   | Basic Testing Notions            | Apply (Test, Verify, Check)          |
|            |                                                     |                          | Edge/Invalid Case Recognition    | Analyze (Identify, Distinguish)      |

### Activation Definition

- **ActivationConstraint:** `optional`  
  Testing is an expected best practice and may be explicitly required as evidence depending on the teacher’s assessment design.

- **ActivationMode:** `analytical`  
  Learners analyze program behavior under selected inputs and compare it to expected outcomes.

- **ActivationRole:** `supporting`  
  Testing supports correctness validation but is secondary to the implementation competencies.

---

## 5. Evidence Package (CSP)

### Required Evidence

- **Source code** implementing: integer input, positivity validation, multiple-of-27 check, and clear output.
- **Execution evidence** (screenshots or terminal log) covering:
  - one multiple of 27,
  - one non-multiple,
  - one invalid (≤ 0).

### Optional Evidence

- Brief written note describing:
  - the validation rule (`n > 0`);
  - the divisibility rule (`n % 27 == 0`).

---

## 6. Consolidated Summary

This task provides a compact instructional scenario for specifying foundational competencies in C programming, especially **validated input handling**, **divisibility decision logic**, and **basic testing practices**. The CSP structure ensures traceability from task requirements to knowledge elements, learning objectives, expected evidence, and competency activation definitions within the K–S–D model.

---