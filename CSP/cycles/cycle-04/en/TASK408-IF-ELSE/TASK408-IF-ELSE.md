# TASK408 — Choosing Between IF–ELSE and Two Independent IF Statements

**Creator:** Prof. MSc Marcos Bião — Univasf, Salgueiro Campus.

Examine the following pseudocode fragments. Both classify an integer `x` as either positive or nonpositive.

Assume that `x` does not change during execution and that displaying a message does not modify it.

**Version A — Two independent IF statements**

```text
READ x

IF x > 0 THEN
    DISPLAY "Positive"
END IF

IF x <= 0 THEN
    DISPLAY "Nonpositive"
END IF
```

**Version B — IF–ELSE**

```text
READ x

IF x > 0 THEN
    DISPLAY "Positive"
ELSE
    DISPLAY "Nonpositive"
END IF
```

## Question

Consider the following statements:

**I.** Both versions display the same result for every integer input, but Version A evaluates two conditions and Version B evaluates one.

**II.** Version B explicitly represents two mutually exclusive and exhaustive alternatives: exactly one branch executes.

**III.** Version B is guaranteed to run faster in every programming language and execution environment.

**IV.** Two independent IF statements always behave like an IF–ELSE structure, regardless of their conditions or changes to the tested values.

Which statements are correct?

- **(a)** I only
- **(b)** II only
- **(c)** I and II only
- **(d)** II and III only
- **(e)** I, II and IV only

For this question, count condition evaluations according to the pseudocode, without assuming compiler optimizations.

## Submission

Select one alternative and briefly justify your answer. 

No program implementation or execution is required.