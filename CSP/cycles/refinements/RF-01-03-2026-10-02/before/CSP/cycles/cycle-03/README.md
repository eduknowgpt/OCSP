# CSP Cycle 3 — Competency Creation and Reuse

## Scope and approach

This consolidation covers the five English Theory of Computation task packages revised for Cycle 3 (2025): TASK25.00, TASK25.01, TASK25.02, TASK25.03, and TASK25.05. Other materials in `pt/`, including TASK25.04 and programming tasks, are outside this dataset. These totals describe this documented scope, not every file stored under the cycle directory.

Task authors, specifiers, and reviewers discussed competency reuse during task development. The CSP reports integrate specification and available decision rationale. Separate review and adjustments reports were not produced for these packages. Their corresponding CSV fields remain empty.

## Files

| File | Purpose |
| --- | --- |
| [CSP-Competency-Registry.csv](CSP-Competency-Registry.csv) | Identity, origin, specialization, composition and cycle-specific counts. |
| [CSP-Task-Competency-Mapping.csv](CSP-Task-Competency-Mapping.csv) | One current task–identity association per pair, with activation and traceable sources; earlier replaced associations retained separately. |
| [CSP-Competency-Lifecycle.csv](CSP-Competency-Lifecycle.csv) | Documented creation, reuse, association addition and replacement. |
| [CSP-Competency-Task-Matrix.md](CSP-Competency-Task-Matrix.md) | Human-readable creation/reuse and activation matrices. |
| [CSP-Data-Dictionary.md](CSP-Data-Dictionary.md) | Field definitions, scope and counting rules. |

## Creation and reuse

| Task | Created | Reused | Associations | Reuse rate |
| --- | ---: | ---: | ---: | ---: |
| TASK25.00 | 6 | 2 | 8 | 25.0% |
| TASK25.01 | 0 | 8 | 8 | 100.0% |
| TASK25.02 | 1 | 8 | 9 | 88.9% |
| TASK25.03 | 0 | 8 | 8 | 100.0% |
| TASK25.05 | 1 | 7 | 8 | 87.5% |
| Consolidated scope | 8 | 33 | 41 | 80.5% |

The current sets contain 20 distinct competency identities and 41 task–competency associations. There are 8 creation associations and 33 reuse associations: 12 associations reuse identities originating within Cycle 3 and 21 associations reuse identities from earlier cycles. The registry contains 21 identities, including reference-only C13. The mapping contains 43 rows: 41 current and two historical C13.01 associations. The lifecycle contains 43 documentary events.

The eight new identities comprise six independent specifications (C17, C18, C19, C21, C22, C23), one specialization (C05.01), and one composite (C20). C05 remains the base of C05.01. C13.01 retains its Cycle 2 origin and C13 base.

## Source reports

- [TASK25.00](<en/TASK25.00 - MusicCollection/Task25.00-CSP-Report.md>).
- [TASK25.01](<en/TASK25.01 - TheVendingMachine/TASK25.01-CSP-Report.md>).
- [TASK25.02](<en/TASK25.02 - TheMinotaursLabyrinth/TASK25.02-CSP-Report.md>).
- [TASK25.03](<en/TASK25.03 - TrafficControl/TASK25.03-CSP-Report.md>).
- [TASK25.05](<en/TASK25.05 - OnlineJudges/TASK25.05-CSP-Report.md>).

## Preserved specification decisions

- TASK25.00 creates six identifiers and reuses C04 and C14. C20 integrates six component identities; its links do not generate additional association rows.
- TASK25.01 retains the adopted addition of C06 for LO3 construction. The earlier C13.01 association is replaced by C23 while preserving both identities.
- TASK25.02 creates C22 and retains its nine specified associations. Proposed inclusion of C12 remains outside the adopted set.
- TASK25.03 retains eight reused identities, including conditional C09. The earlier grammar-rule association gives way to C23 for notation.
- TASK25.05 creates C21 and reuses seven identities. Its year is 2025.

## Interpretation and maintenance

Creation counts identity origin. Reuse includes identities from earlier cycles and earlier tasks within this cycle. Mandatory, conditional and optional associations remain distinguishable. Counts describe specifications, not evidence that all competencies were assessed or mastered.

The lifecycle is a slice of documented Cycle 3 decisions. Event order indexes task packages and known association changes; it does not reconstruct meeting dates. Only documented changes receive events. Detailed component pairings and unresolved scope boundaries remain in the reports.

Paths in CSVs are relative to the CSP directory. SHA-256 values identify the exact report contents used for this consolidation; they are content checks, not public release identifiers. Inherited definition references are retained from the Cycle 2 registry. After a source change, update the affected mapping and lifecycle entries, recalculate registry counts, and regenerate the matrix.
