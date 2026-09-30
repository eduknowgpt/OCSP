# CSP Competency–Task Matrix — Cycle 2

## Adjusted associations

| ID | Competency | Origin | Task201 | Task202 | Task203 | Task204 |
| --- | --- | --- | :---: | :---: | :---: | :---: |
| C02 | Justify the Use of Deterministic Finite Automata (DFAs) | task-01 | R | — | — | R |
| C03 | Test Automata Using Simulators | task-01 | R | R | — | R |
| C04 | Define Regular Expressions for Finite Automata | task-01 | R | — | — | — |
| C05 | Write a Technical Report | task-01 | R | R | R | R |
| C06 | Develop Problem-Solving Solutions Using Finite State Machines | task-03 | R | — | — | R |
| C07 | Develop Problem-Solving Solutions Using Turing Machines | task-02 | — | — | R | — |
| C08 | Identify Turing Machine Variants | task-02 | — | — | R | — |
| C09 | Apply Turing Machine Variants | task-02 | — | — | R | — |
| C10 | Test Turing Machines Using Simulators | task-02 | — | — | R | — |
| C11 | Identify Patterns in Finite State Machines | task-03 | R | — | — | — |
| C12 | Develop Problem-Solving Solutions Using Pushdown Automata | task-04 | — | R | — | — |
| C13 | Interpret Rule-Based Notation | task-04 | — | H → C13.01 | — | — |
| C14 | Differentiate Classifications of Formal Grammars | task-04 | — | R | — | R |
| C13.01 | Interpret Formal Grammar-Based Rules | task-202 | — | C | — | — |
| C15 | Understand the Halting Problem and its Implications | task-204 | — | — | — | C |
| C16 | Interpret Turing Machine Concepts to Analyze Computational System Capabilities | task-204 | — | — | — | C |

C = identifier created in the task; R = existing identifier reused; H = historical base association, excluded from adjusted totals; — = no adjusted association. C13.01 preserves its base relation to C13. C16 is one identity despite the title refinement.

## Quantitative summary

| Task | Created identifiers | Reused identifiers | Adjusted associations | Reuse rate |
| --- | ---: | ---: | ---: | ---: |
| Task201 | 0 | 6 | 6 | 100.0% |
| Task202 | 1 | 4 | 5 | 80.0% |
| Task203 | 0 | 5 | 5 | 100.0% |
| Task204 | 2 | 5 | 7 | 71.4% |
| Cycle 2 | 3 | 20 | 23 | 87.0% |

There are 15 distinct identifiers in the adjusted sets and 16 in the registry when the historical C13 base is included. The mapping contains 24 records: 23 current and one historical. Its rows are associations, not every intermediate specification state.

## Documented activation constraints

| Competency | Task201 | Task202 | Task203 | Task204 |
| --- | :---: | :---: | :---: | :---: |
| C02 | NS | — | — | O |
| C03 | NS | NS | — | Cond |
| C04 | NS | — | — | — |
| C05 | NS | NS | NS | M |
| C06 | NS | — | — | M |
| C07 | — | — | NS | — |
| C08 | — | — | NS | — |
| C09 | — | — | O | — |
| C10 | — | — | NS | — |
| C11 | NS | — | — | — |
| C12 | — | NS | — | — |
| C13 | — | H | — | — |
| C14 | — | NS | — | O |
| C13.01 | — | NS | — | — |
| C15 | — | — | — | M |
| C16 | — | — | — | O / Cond |

M = mandatory; O = optional; Cond = conditional; NS = formal constraint label not specified. O / Cond preserves a documented alternative. NS does not imply optionality. No observed activation count is inferred.

## Task204 roles

| ID | Constraint | Mode | Role |
| --- | --- | --- | --- |
| C06 | mandatory | constructive | supporting |
| C02 | optional | justificatory | extension |
| C03 | conditional | artifact-oriented | supporting |
| C14 | optional | analytical | extension |
| C05 | mandatory | artifact-oriented | transversal |
| C15 | mandatory | analytical; justificatory | core |
| C16 | optional / conditional | interpretative | supporting / extension |

Simulation and the connection to the Chomsky Hierarchy remain objectives in the task statement. The adjusted labels for C03 and C14 do not, alone, authorize omission of those activities.

## Historical interpretation

The initial Task202 set contains five reused identities, including C13. Its adjusted set contains four reused identities and the newly created C13.01. C13 is preserved as the base, not deleted.

Task204 initially proposes C15 and C16. Review and adjustments differentiate their roles and refine components. The change from Apply to Interpret in C16's title is a rename within one identity; the possible future incorporation of its content into C15 has not been implemented.

Source: [mapping](CSP-Task-Competency-Mapping.csv), [registry](CSP-Competency-Registry.csv), and [lifecycle](CSP-Competency-Lifecycle.csv).

