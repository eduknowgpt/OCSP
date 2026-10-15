# CSP Competency–Task Matrix — Cycle 1

## Purpose

This matrix summarizes the current relationships between the competencies and the five instructional tasks in Cycle 1. It supports human inspection of competency creation, reuse, and distribution across tasks.

The canonical data sources are:

- `CSP-Competency-Registry.csv`;
- `CSP-Task-Competency-Mapping.csv`.

## Competency–Task Matrix

| ID | Competency | Origin | Task01 | Task02 | Task03 | Task04 | Task05 |
| --- | --- | --- | :---: | :---: | :---: | :---: | :---: |
| C01 | Develop Problem Solutions Using Automata | Task01 | C | — | — | — | — |
| C02 | Justify the Use of Deterministic Finite Automata (DFAs) | Task01 | C | — | — | — | — |
| C03 | Test Automata Using Simulators | Task01 | C | — | R | R | — |
| C04 | Define Regular Expressions for Finite Automata | Task01 | C | — | R | — | — |
| C05 | Write a Technical Report | Task01 | C | R | R | R | R |
| C06 | Develop Problem-Solving Solutions Using Finite State Machines | Task03 | R | — | C | — | — |
| C07 | Develop Problem-Solving Solutions Using Turing Machines | Task02 | — | C | — | — | S→C07.01 |
| C08 | Identify Turing Machine Variants | Task02 | — | C | — | — | S→C08.01 |
| C09 | Apply Turing Machine Variants | Task02 | — | C | — | — | S→C09.01 |
| C10 | Test Turing Machines Using Simulators | Task02 | — | C | — | — | R |
| C11 | Identify Patterns in Finite State Machines | Task03 | — | — | C | — | — |
| C12 | Develop Problem-Solving Solutions Using Pushdown Automata | Task04 | — | — | — | C | — |
| C13 | Interpret Rule-Based Notation | Task04 | — | — | — | C | — |
| C14 | Differentiate Classifications of Formal Grammars | Task04 | — | — | — | C | — |
| C07.01 | Develop Integrated Multi-Agent Solutions Using Turing Machines | Task05 | — | — | — | — | C |
| C08.01 | Analyze the System-Level Adequacy of Turing Machine Variants | Task05 | — | — | — | — | C |
| C09.01 | Apply and Coordinate Turing Machine Variants in Integrated Architectures | Task05 | — | — | — | — | C |

### Legend

- **C** — competency created in the task;
- **R** — competency reused from another task;
- **S→ID** — base competency reused and qualified into the indicated additive specialization;
- **—** — competency is not currently associated with the task.

## Summary by Task

| Task | Created | Reused | Total | Reuse rate |
| --- | ---: | ---: | ---: | ---: |
| Task01 | 5 | 1 | 6 | 16.7% |
| Task02 | 4 | 1 | 5 | 20% |
| Task03 | 2 | 3 | 5 | 60% |
| Task04 | 3 | 2 | 5 | 40% |
| Task05 | 3 | 2 | 5 | 40% |
| **Cycle 1** | **17** | **9** | **26** | **34.6%** |

The totals count current task–competency relationships. They do not represent the number of unique competencies in the repository.

## Summary by Origin Task

| Origin task | Competencies created | Number |
| --- | --- | ---: |
| Task01 | C01, C02, C03, C04, C05 | 5 |
| Task02 | C07, C08, C09, C10 | 4 |
| Task03 | C06, C11 | 2 |
| Task04 | C12, C13, C14 | 3 |
| Task05 | C07.01, C08.01, C09.01 | 3 |
| **Cycle 1** | **C01–C14; C07.01; C08.01; C09.01** | **17** |

## Historical and Interpretive Notes

### C01

C01 was created in Task01 and remains associated with it. During the second Task01 iteration, C06 was added as a more precise finite-state competency. The authors documented this as an additive refinement: C06 complements C01 rather than replacing or reformulating it.

### C06

C06 was created during Task03. In the second Task01 iteration, it was reused and added to Task01 because its finite-state scope is more precise than the broader scope of C01. The matrix therefore shows:

- **C** for C06 in Task03;
- **R** for C06 in Task01.

### Creation and reuse counts

Cycle 1 contains 17 unique competencies. The current matrix contains 26 task–competency relationships:

- 17 creation relationships currently associated with their origin tasks;
- 9 reuse relationships;
- C01 and C06 both associated with Task01 in accordance with the documented additive refinement.

### Task05 additive specializations

Task05 initially reused C07–C10 and C05. After expert review, the adjustments report qualified the expanded enactment of C07–C09 and formalized C07.01, C08.01, and C09.01 through an additive specialization strategy. The matrix preserves the base-to-specialization links and counts the three derived competencies as the current Task05 associations. C10 and C05 remain direct reused associations.

## Reading Guidance

Use this matrix for overview and comparison. Use `CSP-Task-Competency-Mapping.csv` when the analysis requires review decisions, reuse modes, iterations, source documents, or historical association status. Use `CSP-Competency-Registry.csv` when the analysis requires canonical competency titles, origin, current specification files, or total usage counts.
