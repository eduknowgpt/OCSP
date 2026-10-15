# CSP Data Dictionary — Cycle 3

## Format and scope

This consolidation covers the five English Theory of Computation task packages revised for Cycle 3 (2025): TASK25.00, TASK25.01, TASK25.02, TASK25.03, and TASK25.05. Other materials in `pt/`, including TASK25.04 and programming tasks, are outside this dataset. These totals describe this documented scope, not every file stored under the cycle directory.

The CSVs use UTF-8, comma delimiters, a header row and standard double-quote escaping. Identifiers are text, counts and sequence numbers are integers, and Boolean flags use true/false. Semicolons delimit lists. Paths beginning `cycles/` are relative to the CSP directory. Empty fields represent absent or inapplicable information as defined below.

Principal Cycle 2 columns are retained. Cycle 3 adds composition links, reuse-origin scope, and source hashes. Registry grain is one identity; mapping grain is one task–identity association; lifecycle grain is one documented event.

## CSP-Competency-Registry.csv

| Field | Definition |
| --- | --- |
| `cycle_id` | Dataset scope: cycle-03; independent of identity origin. |
| `competency_id` | Stable identifier; decimals identify documented derived competencies. |
| `competency_title` | Identity title from the origin registry or originating report; mapping titles preserve task wording and capitalization. |
| `origin_task` | Task in which the identity originated. Reuse preserves this value. |
| `origin_iteration` | Inherited origin iteration or 1 for the integrated originating package. Not a count of meetings. |
| `registry_status` | active: retained competency identity; this is not a global approval decision. |
| `current_specification_file` | Inherited definition reference for prior-cycle identities; originating integrated report for new identities. |
| `definition_review_file` | Inherited definition-review reference when available; empty for identities originating in the integrated Cycle 3 reports. |
| `definition_adjustments_file` | Inherited definition-adjustments reference when available; empty for new Cycle 3 identities. |
| `current_task_ids` | Semicolon-separated current task associations within this five-task scope. |
| `current_task_count` | Number of distinct current task associations in this scope. |
| `current_reuse_count` | Number of current associations classified as reused in this scope. |
| `historical_association_count` | Number of distinct task–identity pairs represented in the mapping, including current and historical pairs. Zero for a reference-only base. |
| `notes` | Source-qualified interpretation or limitation. |
| `origin_cycle_id` | cycle-01, cycle-02 or cycle-03, according to the documented creation task. |
| `creation_type` | original, specialization or composite. All three create a distinct identity. |
| `base_competency_id` | Preserved base identifier for a derived competency; blank otherwise. |
| `cycle_participation` | current or reference_only. C13 is a preserved base without a task association in this dataset. |
| `initial_title` | Inherited reference title for prior-cycle identities or title in the originating Cycle 3 report; not a reconstruction of every earlier title. |
| `definition_review_scope` | Clarifies whether the cited review addresses the competency or its base. |
| `current_association_files` | Semicolon-separated integrated reports supporting current task associations. |
| `component_competency_ids` | Six semicolon-separated component IDs for composite C20. Empty otherwise. Links do not count as new task associations. |
| `definition_source_sha256` | SHA-256 for new Cycle 3 definition reports. Empty for inherited definitions, whose contents were not rehashed in this consolidation. |

## CSP-Task-Competency-Mapping.csv

| Field | Definition |
| --- | --- |
| `cycle_id` | Dataset scope: cycle-03; independent of identity origin. |
| `task_id` | task-25.00, task-25.01, task-25.02, task-25.03 or task-25.05. Origins may refer to earlier cycles. |
| `competency_id` | Stable identifier; decimals identify documented derived competencies. |
| `competency_title` | Identity title from the origin registry or originating report; mapping titles preserve task wording and capitalization. |
| `usage_type` | created when task_id equals origin_task; reused otherwise. |
| `origin_task` | Task in which the identity originated. Reuse preserves this value. |
| `reuse_mode` | contextual_activation for reuse; additive_specialization for new C05.01; composition for new C20; not_applicable for independent creations. |
| `mapping_status` | current or historical_replaced. Historical C13.01 associations in TASK25.01 and TASK25.03 point to C23. |
| `include_in_current_analysis` | true for current associations; false for historical rows. Filter on this field before counting. |
| `association_iteration` | 1 indexes the integrated current package. Empty for earlier associations whose iteration is not established. |
| `review_decision` | Empty: no separate formal approval outcome is inferred from the integrated discussions. |
| `role_in_task` | Short functional label based on the competency title; activation_role retains the formal task role. |
| `report_file` | Integrated task report documenting the association and available decisions. |
| `review_file` | Empty: no separate CSP-Review document was produced for these packages. |
| `adjustments_file` | Empty: no separate CSP-Adjustments document was produced for these packages. |
| `notes` | Source-qualified interpretation or limitation. |
| `origin_cycle_id` | cycle-01, cycle-02 or cycle-03, according to the documented creation task. |
| `specification_stage` | integrated for consolidated records; prior_association for earlier replaced associations. |
| `base_competency_id` | Preserved base identifier for a derived competency; blank otherwise. |
| `related_competency_id` | Specialization base, or replacement target C23 for historical mapping and replacement events. |
| `activation_constraint` | mandatory, conditional or optional for current rows; not_specified for historical rows without documented activation labels. |
| `activation_mode` | Source activation mode; semicolons join concurrent modes. |
| `activation_role` | core, supporting, extension or transversal for current rows; not_specified for historical rows. |
| `predominant_bloom_levels` | Empty: component-specific Bloom mappings are retained in source reports and are not replaced by an inferred predominant level. |
| `evidence_file` | Principal source path supporting the row. |
| `evidence_section` | Section or table locator in the principal source. |
| `activation_evidence_file` | Semicolon-separated task package sources supporting the activation synthesis. |
| `activation_evidence_section` | Activation table locator. Empty for historical rows without recorded activation labels. |
| `evidence_basis` | documentary_specification. Does not encode observed learner performance. |
| `component_competency_ids` | Six semicolon-separated component IDs for composite C20. Empty otherwise. Links do not count as new task associations. |
| `reuse_origin_scope` | within_cycle or prior_cycle for reused rows; not_applicable for creation. |
| `source_sha256` | SHA-256 of the source report bytes, allowing content-level verification. |

## CSP-Competency-Lifecycle.csv

| Field | Definition |
| --- | --- |
| `event_id` | Unique event identifier prefixed C03-. |
| `competency_id` | Stable identifier; decimals identify documented derived competencies. |
| `event_sequence` | Consecutive ordering per identity within this dataset; task order and documented transitions, not exact chronology. |
| `event_type` | created, reused, association_added or association_replaced. No separate reviewed or approved event is inferred. |
| `cycle_id` | Dataset scope: cycle-03; independent of identity origin. |
| `task_id` | task-25.00, task-25.01, task-25.02, task-25.03 or task-25.05. Origins may refer to earlier cycles. |
| `iteration` | 1 for events in the integrated current package; blank when a prior-association iteration is not established. |
| `event_date` | Empty because an exact event date is not documented. The cycle year is 2025; no artificial full date is generated. |
| `previous_state` | Blank before creation; existing_identity for reuse or addition; associated before replacement. |
| `resulting_state` | specified, or association_replaced_identity_preserved. |
| `previous_title` | Blank for creation; existing title otherwise. |
| `resulting_title` | Title retained by the identity. Association replacement does not rename C13.01 as C23. |
| `decision` | Documented decision or event summary. |
| `rationale` | Source-grounded reason for the event. |
| `evidence_file` | Principal source path supporting the row. |
| `notes` | Source-qualified interpretation or limitation. |
| `specification_stage` | integrated for consolidated records; prior_association for earlier replaced associations. |
| `evidence_section` | Section or table locator in the principal source. |
| `related_competency_id` | Specialization base, or replacement target C23 for historical mapping and replacement events. |
| `component_competency_ids` | Six semicolon-separated component IDs for composite C20. Empty otherwise. Links do not count as new task associations. |
| `source_sha256` | SHA-256 of the source report bytes, allowing content-level verification. |

## Counting rules

The current sets contain 20 distinct competency identities and 41 task–competency associations. There are 8 creation associations and 33 reuse associations: 12 associations reuse identities originating within Cycle 3 and 21 associations reuse identities from earlier cycles. The registry contains 21 identities, including reference-only C13. The mapping contains 43 rows: 41 current and two historical C13.01 associations. The lifecycle contains 43 documentary events.

1. Filter `include_in_current_analysis=true`. Count each task–identifier pair once.
2. Creation requires equality between task_id and origin_task. Reuse preserves origin.
3. Reuse rate = reused current associations / all current associations = 33 / 41 = 80.4878…%, displayed as 80.5%.
4. New specializations and composites count as new identities. Their base/component links are separate relations, never extra associations.
5. Historical C13.01 rows and reference-only C13 do not enter current totals.
6. A competency reused in another task of the same cycle remains a reuse association, even though its identity was created within this cycle.
7. Lifecycle events do not increase association counts. The C06 association_added event in TASK25.01 is counted once as reuse.
8. Conditional and optional associations enter the main totals. A mandatory-only view requires an explicit filter and a different denominator.

Current activation distribution: conditional: 6, mandatory: 32, optional: 3.

## Historical interpretation

The historical C13.01 associations in TASK25.01 and TASK25.03 are supported by the current reports’ decision rationale. Their original activation labels and dates are not reconstructed. C23 retains its independent TASK25.00 origin; replacing an association is neither a specialization nor a deletion of C13.01.

New identities: C17, C18, C19 and C23 (independent), C05.01 (specialization) and C20 (composite) in TASK25.00; C22 in TASK25.02; C21 in TASK25.05. Earlier-cycle creation events are not fabricated in this lifecycle.

## Validation and maintenance

- Mapping, lifecycle, base and component identifiers must resolve to the registry.
- Current task–identity pairs must be unique and match the source activation tables.
- Each Cycle 3-created identity has exactly one creation event.
- Every current association has one creation, reuse or addition event.
- Registry counts, matrix cells and totals are derived from the same current mapping.
- Source hashes identify report content; repository publication or a release requires separate versioning.
- Task-specific component mappings and unresolved coverage boundaries remain in their reports. No competency proposed only as a recommendation enters the current mapping.
