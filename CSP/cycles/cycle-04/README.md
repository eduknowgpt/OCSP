# CSP Cycle 4 — Competency Creation and Reuse

## Scope

Consolidation of the current local TASK401–TASK411 reports for introductory programming, preserving adjustments and source-qualified history. The dataset specifies intended competencies and activation, not observed student attainment. It does not certify that every task was administered in a particular course or class.

## Files

- [Competency registry](CSP-Competency-Registry.csv): current definitions, full KS pairings, origin, participation and withdrawn-identifier traceability.
- [Task–competency mapping](CSP-Task-Competency-Mapping.csv): direct current and explicitly historical associations, activation and evidence.
- [Competency–task matrix](CSP-Competency-Task-Matrix.md): current comparison view.
- [Lifecycle](CSP-Competency-Lifecycle.csv): source-supported creation, reuse and selected revision events.
- [Composition](CSP-Competency-Composition.csv): seven required parent–atom links, separate from task counts.
- [Data dictionary](CSP-Data-Dictionary.md): schemas, counting rules and source precedence.
- [Validation summary](validation-summary.json): reproducible totals and integrity-check result.
- `evidence/`: byte-preserved report snapshots and an explicitly labeled conversation decision note.

## Current totals

| Measure | Count |
| --- | ---: |
| tasks | 11 |
| active_identities | 23 |
| direct_identities | 20 |
| component_only_identities | 3 |
| withdrawn_identities | 1 |
| current_associations | 60 |
| creation_associations | 18 |
| reuse_associations | 42 |
| reuse_rate_percent | 70.0 |
| historical_mapping_rows | 2 |
| composition_links | 7 |
| lifecycle_events | 71 |

Activation: 46 mandatory, 8 optional and 6 conditional associations.

CM13, CM16 and CM17 are active component-only entries. CM14 and CM15 originated as components in TASK401 but also have later direct reuse associations. CM10 and CM18 remain fixed composites. All active CM identities originated in Cycle 4; the 70% reuse rate describes within-cycle reuse, not importation from earlier cycles.

## Authoritative decisions

- Apply TASK401’s adjustment over the original report: CM07 mandatory; CM10 composite; CM12 a conditional extension.
- Use current TASK402 CM18; retain the prior CM10 task link only as historical_replaced.
- Preserve CM23’s current BNCC alignment in its TASK405 source.
- Exclude K19 and CM24 from current specifications. CM24 appears only as withdrawn history, with no current definition or KS pairs. The decision note is not a substitute for an unavailable original report.
- Preserve TASK411 [row, column] coordinates. Required outputs and optional test evaluation are distinct.

## Compatibility and provenance

The principal Cycle 3 CSV columns are retained, with Cycle 4 additions for definitions and full KS arrays. Cycle 3 refinement fields are not populated with invented Cycle 4 events. The six user-named Cycle 3 files were inspected read-only; their task identifiers and prior-cycle identities were not copied into this dataset. Original reports and files in the synced project sources directory were not edited.

Generated locally under outputs/Cycle04-Consolidation/deliverables. Nothing has been published to or overwritten in I:/Meu Drive/OCSP/CSP/cycles/. To rebuild, run the sibling build.py from the original workspace; evidence is refreshed from the current reports. Existing source hashes are the content version markers; exact historical event dates remain blank.

## Validation

All integrity checks passed. The build checks 60 unique current associations against independent per-task totals, identifier resolution, complete acyclic compositions, current-source hashes, authoritative activation overrides and exclusion of withdrawn knowledge from active specifications. Read the dictionary before aggregating CSV rows. Historical and component-only entries must not inflate direct current totals.
