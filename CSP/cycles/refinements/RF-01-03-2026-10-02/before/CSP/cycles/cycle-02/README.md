# CSP Cycle 2

## Scope

Cycle 2 records four CSP applications in 2022: Task201–Task204. The English task packages describe specification, expert review, and adjustments in Formal Languages and Computation Theory. This consolidation uses the corrected reports available on 29 September 2026; that date identifies this synthesis, not the dates of the methodological decisions.

The registry contains 16 competency identities involved in the cycle: 15 occur in the adjusted task sets, and C13 is retained as the historical base of C13.01. The files describe this cycle, not the entire CSP repository.

## Tasks

| Task | Title | Main focus |
| --- | --- | --- |
| Task201 | Surveillance Drone Prototype | FSM modeling and contextual reuse |
| Task202 | Team Control | PDA modeling and specialization of rule interpretation |
| Task203 | Parking Control | TM modeling and optional variant activation |
| Task204 | Online Judges at Logistic Solutions | Computational limits, FSM representation, and activation roles |

The models describe the adopted instructional progression. Their selection does not itself prove that every alternative formulation is impossible.

## Files

| File | Purpose |
| --- | --- |
| [CSP-Competency-Registry.csv](CSP-Competency-Registry.csv) | One record per identity involved in Cycle 2, with origin, definition references, and cycle-specific counts. |
| [CSP-Task-Competency-Mapping.csv](CSP-Task-Competency-Mapping.csv) | Adjusted task associations plus the historical C13 association in Task202. |
| [CSP-Competency-Lifecycle.csv](CSP-Competency-Lifecycle.csv) | Initial selections, review findings, and adopted changes. |
| [CSP-Competency-Task-Matrix.md](CSP-Competency-Task-Matrix.md) | Human-readable matrix and activation configuration. |
| [CSP-Data-Dictionary.md](CSP-Data-Dictionary.md) | Field definitions, controlled values, and counting conventions. |

The task reports are the documentary basis. The CSVs organize their contents; the matrix and totals are derived from those CSVs.

## Creation and reuse

| Task | Created identifiers | Reused identifiers | Adjusted associations | Reuse rate |
| --- | ---: | ---: | ---: | ---: |
| Task201 | 0 | 6 | 6 | 100.0% |
| Task202 | 1 | 4 | 5 | 80.0% |
| Task203 | 0 | 5 | 5 | 100.0% |
| Task204 | 2 | 5 | 7 | 71.4% |
| Cycle 2 | 3 | 20 | 23 | 87.0% |

Filter the mapping by `include_in_current_analysis=true` before counting. A created specialization counts as creation of an identifier; its relationship to the existing base is recorded separately. Optional and conditional associations remain in these totals. The figures describe documentary associations, not observed learner performance.

The 20 adjusted reuse associations use identities originating in Cycle 1. Cycle 2 introduces C13.01 in Task202 and C15 and C16 in Task204. No reuse of these three new identities in a later task is documented within this cycle.

## Preserved decisions

- Task201 retains six reused competencies. C04 receives contextual clarification without specialization.
- Task202 initially reuses C13 and adopts C13.01 after review. C13 remains defined and preserved as the base; it is not counted as an additional adjusted Task202 target.
- Task203 retains C09 without specialization. Its optional analytical or constructive activation is documented, including the overlap with C08's analytical evidence.
- Task204 retains both C15 and C16. C15 is mandatory and core. C16 remains optional/conditional and supporting/extension. The adjusted title uses Interpret; its earlier Apply title belongs to the same identifier.
- C15 and C16 component refinements remain documented in the adjustments. Changing a title or a component does not reset origin or count as a new identity.
- The conditional C03 and optional C14 classifications in Task204 do not withdraw simulation and Chomsky-Hierarchy objectives from the task statement.

## Source packages

| Task | Specification | Review | Adjustments |
| --- | --- | --- | --- |
| Task201 | [Report](en/Task201/Task201-CSP-Report.md) | [Review](en/Task201/TASK201-CSP-Review-Report.md) | [Adjustments](en/Task201/TASK201-CSP-Adjustment.md) |
| Task202 | [Report](en/Task202/Task202-CSP-Report.md) | [Review](en/Task202/TASK202-CSP-Review-Report.md) | [Adjustments](en/Task202/TASK202-CSP-Adustments.md) |
| Task203 | [Report](en/Task203/Task203-CSP-Report.md) | [Review](en/Task203/TASK203-CSP-Review-Report.md) | [Adjustments](en/Task203/TASK203-CSP-Adjustments.md) |
| Task204 | [Report](en/Task204/Task204-CSP-Report.md) | [Review](en/Task204/TASK204-CSRP-Report.md) | [Adjustments](en/Task204/TASK204-CSP-Adjustments.md) |

Historical filenames are preserved, including `TASK202-CSP-Adustments.md` and `TASK204-CSRP-Report.md`. CSV source paths are relative to the CSP directory: `cycles/cycle-02/...`. References to inherited definitions point to Cycle 1.

## Interpretation and maintenance

1. Keep competency origin and identifiers stable across cycles.
2. Use the lifecycle for the initial proposal and subsequent decisions. Do not overwrite initial C13 or C16 states with later formulations.
3. Interpret the lifecycle sequence as documentary order within this cycle. Event dates remain empty when not documented; iteration 1 denotes the single report–review–adjustment package, not a claim about unrecorded meetings.
4. Treat `not_specified` as an unassigned formal activation label. It does not imply that an activity was optional.
5. After an authorized source change, update the corresponding event or association, recalculate registry counts, and regenerate the matrix and summary.

The CSVs contain no claim that competencies were independently demonstrated by learners. Global approval labels, reviewer counts, and unrecorded event dates are not inferred.

