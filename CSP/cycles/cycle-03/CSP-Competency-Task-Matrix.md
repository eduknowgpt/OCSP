# CSP Competency–Task Matrix — Cycle 3

Current associations after [RF-01-03](../CSP-Post-Cycle-Refinement-Report.md). The 2025 baseline remains recoverable through include_in_pre_refinement_analysis and the archive.

| ID | Origin | TASK301 | TASK302 | TASK303 | TASK304 | TASK305 |
| --- | --- | :---: | :---: | :---: | :---: | :---: |
| C02 | task-01 | — | R | R | — | R |
| C03 | task-01 | — | R | R | — | R |
| C04 | task-01 | R | R | — | — | — |
| C05 | task-01 | — | — | — | — | R |
| C05.01 | task301 | C | R | R | R | — |
| C06 | task-03 | — | R | — | — | R |
| C07 | task-02 | — | — | — | R | — |
| C09 | task-02 | — | — | — | R | — |
| C10 | task-02 | — | — | — | R | — |
| C12 | task-04 | — | — | R* | — | — |
| C13 | task-04 | — | — | — | — | — |
| C13.01 | task-202 | — | H → C23 | R | H → C23 | — |
| C14 | task-04 | R | — | R | — | R |
| C15 | task-204 | — | — | — | — | R |
| C16 | task-204 | — | — | — | R | R |
| C17 | task301 | C | R | R | R | — |
| C18 | task301 | C | R | R | R | — |
| C19 | task301 | C | — | R | — | — |
| C20 | task301 | C | — | — | — | — |
| C21 | task305 | — | — | — | — | C |
| C22 | task303 | — | — | C | — | — |
| C23 | task301 | C | R | — | R | — |

C = created; R = reused; R* = reuse added by post-cycle refinement; H = historical association excluded from current totals. C13 remains a reference base; C12 was added to TASK303 without creating an identity.

## Current totals

| Task | Created | Reused | Associations | Reuse rate |
| --- | ---: | ---: | ---: | ---: |
| TASK301 | 6 | 2 | 8 | 25.0% |
| TASK302 | 0 | 8 | 8 | 100.0% |
| TASK303 | 1 | 9 | 10 | 90.0% |
| TASK304 | 0 | 8 | 8 | 100.0% |
| TASK305 | 1 | 7 | 8 | 87.5% |
| Total | 8 | 34 | 42 | 81.0% |

## Baseline totals

| Task | Created | Reused | Associations | Reuse rate |
| --- | ---: | ---: | ---: | ---: |
| TASK301 | 6 | 2 | 8 | 25.0% |
| TASK302 | 0 | 8 | 8 | 100.0% |
| TASK303 | 1 | 8 | 9 | 88.9% |
| TASK304 | 0 | 8 | 8 | 100.0% |
| TASK305 | 1 | 7 | 8 | 87.5% |
| Total | 8 | 33 | 41 | 80.5% |

## Activation constraints

| ID | TASK301 | TASK302 | TASK303 | TASK304 | TASK305 |
| --- | :---: | :---: | :---: | :---: | :---: |
| C02 | — | mandatory | mandatory | — | optional |
| C03 | — | conditional | mandatory | — | conditional |
| C04 | mandatory | conditional | — | — | — |
| C05 | — | — | — | — | mandatory |
| C05.01 | mandatory | mandatory | mandatory | mandatory | — |
| C06 | — | mandatory | — | — | mandatory |
| C07 | — | — | — | mandatory | — |
| C09 | — | — | — | conditional | — |
| C10 | — | — | — | mandatory | — |
| C12 | — | — | mandatory | — | — |
| C13.01 | — | — | mandatory | — | — |
| C14 | optional | — | mandatory | — | optional |
| C15 | — | — | — | — | mandatory |
| C16 | — | — | — | mandatory | conditional |
| C17 | mandatory | mandatory | mandatory | mandatory | — |
| C18 | mandatory | mandatory | mandatory | mandatory | — |
| C19 | mandatory | — | conditional | — | — |
| C20 | mandatory | — | — | — | — |
| C21 | — | — | — | — | mandatory |
| C22 | — | — | mandatory | — | — |
| C23 | mandatory | mandatory | — | mandatory | — |

## Post-cycle refinement metadata — RF-01-03

Refinement date: 2 October 2026. The original application year is unchanged. `include_in_pre_refinement_analysis` preserves membership in the pre-refinement current set; `include_in_current_analysis` selects the maintained set. `post_cycle_refinement_id` and `refinement_date` identify updated mappings. `reference_refinement_id` identifies reconciled definition references in the registry. Lifecycle events use `reference_alignment` or `association_added`, `specification_stage=post_cycle_refinement`, an explicit date and `refinement_id=RF-01-03`. Earlier events retain their previous dates and point to archived evidence where the source was updated. No review or approval is inferred. See the [refinement report](../CSP-Post-Cycle-Refinement-Report.md).
