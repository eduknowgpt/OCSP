# CSP Data Dictionary — Cycle 2

## Format and scope

The three CSV files use UTF-8, comma delimiters, a header row, and standard double-quote escaping. Identifiers and controlled values are text; counts and sequence numbers are integers; booleans are lowercase true/false. Empty cells denote unavailable or inapplicable values as specified below. Semicolons separate lists; a vertical bar separates documented alternatives.

Paths beginning `cycles/` are relative to the CSP directory. The same naming convention and principal fields as Cycle 1 are retained. Cycle-specific activation and provenance fields extend that schema; Cycle 1 files are not modified.

Registry grain: one competency identity involved in Cycle 2. Mapping grain: one adjusted task–identity association, plus historical associations that explain a changed identity in the adjusted set. Lifecycle grain: one documented event. Initial and review states of continuing identities are retained in the lifecycle instead of duplicating all mapping rows.

## Registry — CSP-Competency-Registry.csv

| Field | Definition |
| --- | --- |
| `cycle_id` | Scope of this dataset or event: cycle-02. This is not necessarily the competency's origin cycle. |
| `competency_id` | Stable identifier; decimals identify documented derived competencies. |
| `competency_title` | Canonical cycle-end title. Capitalization is normalized; full source descriptions remain authoritative. |
| `origin_task` | Task in which the identifier originated; unchanged by reuse or renaming. |
| `origin_iteration` | Iteration in the origin reference; 1 for the documented package. |
| `registry_status` | active: retained competency identity; this is not a global approval decision. |
| `current_specification_file` | Definition reference. Reused identities retain Cycle 1 definition sources; new identities point to Cycle 2 adjustments. |
| `definition_review_file` | Review associated with the definition. For C13.01 this reviews its base C13; see definition_review_scope. |
| `definition_adjustments_file` | Source of the current recorded definition or refinement. |
| `current_task_ids` | Semicolon-separated adjusted task IDs within Cycle 2. |
| `current_task_count` | Number of distinct current task associations within Cycle 2. |
| `current_reuse_count` | Current associations classified as reused within Cycle 2. |
| `historical_association_count` | Number of distinct task–identifier pairs ever represented in this cycle mapping, including current pairs. Not the number of lifecycle events. |
| `notes` | Source-qualified interpretation or limitation. |
| `origin_cycle_id` | Cycle of creation: cycle-01 or cycle-02. |
| `creation_type` | original or specialization. Specialization is counted as creation of a new identity. |
| `base_competency_id` | Preserved base identifier for a derived competency; blank otherwise. |
| `cycle_participation` | current or historical_only. C13 is historical_only within this cycle and remains active as a base. |
| `initial_title` | Title at the first Cycle 2 state represented here. Reused identities use the inherited Cycle 1 reference title, not necessarily their earliest historical wording. C16 initially uses Apply and currently uses Interpret. |
| `definition_review_scope` | Clarifies whether the cited review addresses the competency or its base. |
| `current_association_files` | Semicolon-separated evidence files for adjusted associations. |

## Mapping — CSP-Task-Competency-Mapping.csv

| Field | Definition |
| --- | --- |
| `cycle_id` | Scope of this dataset or event: cycle-02. This is not necessarily the competency's origin cycle. |
| `task_id` | Task identifier, task-201 through task-204. Origin references also use Cycle 1 task IDs. |
| `competency_id` | Stable identifier; decimals identify documented derived competencies. |
| `competency_title` | Canonical cycle-end title. Capitalization is normalized; full source descriptions remain authoritative. |
| `usage_type` | created when task_id equals origin_task; reused otherwise. |
| `origin_task` | Task in which the identifier originated; unchanged by reuse or renaming. |
| `reuse_mode` | contextual_activation; additive_specialization; specialized_into; or not_applicable. See controlled values. |
| `mapping_status` | current or historical_specialized; historical C13 points to C13.01. |
| `include_in_current_analysis` | Boolean true/false. Only true rows enter adjusted totals. |
| `association_iteration` | 1 denotes the single documented report–review–adjustment package for the task. |
| `review_decision` | Documented competency-level outcome or concise summary. Task201/202 values before the semicolon are alignment; after it, detected tension. No global Approved status is invented. |
| `role_in_task` | Human-readable function within the task. |
| `report_file` | Initial specification source. |
| `review_file` | Expert-review source. |
| `adjustments_file` | Implemented-adjustments source. |
| `notes` | Source-qualified interpretation or limitation. |
| `origin_cycle_id` | Cycle of creation: cycle-01 or cycle-02. |
| `specification_stage` | Mapping: adjusted or initial_reviewed. Lifecycle: initial, review, or adjusted. |
| `base_competency_id` | Preserved base identifier for a derived competency; blank otherwise. |
| `related_competency_id` | Related identity: base or derived identifier, interpreted with event type or mapping status. |
| `activation_constraint` | mandatory, optional, conditional, optional / conditional, or not_specified. |
| `activation_mode` | Documented modes; semicolon joins concurrent descriptions and  /  separates alternative modes. |
| `activation_role` | Documented role label;  /  preserves alternatives. not_specified means no formal role label was assigned in this extraction. |
| `predominant_bloom_levels` | Task-level predominant levels where a source table supplies them. Empty for Task204: component-specific pairings are not collapsed into a new predominant level. |
| `evidence_file` | Principal source path supporting the row. |
| `evidence_section` | Section or table locator in the principal source. |
| `activation_evidence_file` | Semicolon-separated task package sources supporting the activation synthesis. |
| `activation_evidence_section` | Locations of activation descriptions in those sources. |
| `evidence_basis` | documentary_specification. Does not encode observed learner performance. |

## Lifecycle — CSP-Competency-Lifecycle.csv

| Field | Definition |
| --- | --- |
| `event_id` | Unique across this file, prefixed C02- to avoid Cycle 1 event-ID collisions. |
| `competency_id` | Stable identifier; decimals identify documented derived competencies. |
| `event_sequence` | Consecutive documentary ordering per competency within Cycle 2, beginning at 1; not a global lifetime sequence or timestamp. |
| `event_type` | created, reused, reviewed, activation_clarified, specialized_in_task, revised, or renamed. |
| `cycle_id` | Scope of this dataset or event: cycle-02. This is not necessarily the competency's origin cycle. |
| `task_id` | Task identifier, task-201 through task-204. Origin references also use Cycle 1 task IDs. |
| `iteration` | 1 for the single documented package; phases are represented separately by specification_stage. |
| `event_date` | ISO date only when documented for the event. Empty in this dataset; task dates and consolidation dates are not substituted. |
| `previous_state` | existing_identity, specified, or blank before creation. These are documentary states. |
| `resulting_state` | specified, reviewed, or base_preserved. They do not encode proficiency or global repository status. |
| `previous_title` | Title before the event; blank for creation. |
| `resulting_title` | Title after the event. C16 remains Apply until the explicit rename event. |
| `decision` | Documented decision or event summary. |
| `rationale` | Source-grounded reason for the event. |
| `evidence_file` | Principal source path supporting the row. |
| `notes` | Source-qualified interpretation or limitation. |
| `specification_stage` | Mapping: adjusted or initial_reviewed. Lifecycle: initial, review, or adjusted. |
| `evidence_section` | Section or table locator in the principal source. |
| `related_competency_id` | Related identity: base or derived identifier, interpreted with event type or mapping status. |

## Controlled interpretation

- `created` depends on identity origin, not on first appearance in this CSV or on mandatory status.
- `additive_specialization` records creation of C13.01 while preserving C13. `specialized_into` records the historical C13 association. The base remains defined.
- `contextual_activation` records reuse without a new identifier. It does not assert that the complete base definition was revalidated in every task.
- `not_applicable` is the reuse mode for original creations. A specialization uses `additive_specialization` even though usage_type is created.
- `reviewed` captures the review finding. `activation_clarified` captures adjusted role documentation or retention. Neither changes the competency's origin.
- `revised` captures C15/C16 component refinements; `renamed` captures C16's title change. These events do not count as new identities.
- `specialized_in_task` retains C13 as a base and traces its task association to C13.01; it is not a deletion event.
- Missing formal constraint or role labels are not inferred from the existence of a deliverable. Narrative functions remain in role_in_task.
- Historical scope and component differences remain in the reports. This dataset does not resolve them by silently preferring a table over prose.

## Counting rules

Let M be mapping rows with include_in_current_analysis=true.

1. Adjusted association count = number of rows in M = 23.
2. Created associations = rows in M with usage_type=created = 3.
3. Reused associations = rows in M with usage_type=reused = 20.
4. Reuse rate = 20 / 23 × 100 = 86.9565…%, displayed as 87.0%.
5. Distinct adjusted identities = distinct competency_id in M = 15.
6. Registry identities = 16, including historical-only C13.
7. Historical-only mapping rows = 1. The mapping therefore has 24 rows.
8. Specialization count among created identities = 1 (C13.01); original creations = 2 (C15 and C16).
9. Repeated stages and lifecycle events never add to association or creation totals.
10. Optional/conditional associations are included in M. A required-only analysis would be a different population and must be labeled separately.

All counts are Cycle 2 counts. Inherited origins remain in Cycle 1. The lifecycle is a Cycle 2 event slice, so inherited identities do not receive fabricated creation events here. The sequence follows task number and report → review → adjustments for indexing; exact chronological ordering of all historical revisions is not established.

## Validation and maintenance

- Each mapping and lifecycle identifier must exist in the registry.
- There is at most one current mapping per task–identifier pair.
- Every created mapping has task_id=origin_task; every reused mapping has a different origin.
- C13.01 has base_competency_id=C13; the base remains in the registry.
- C16 has one registry row and one adjusted Task204 association.
- Each of the three Cycle 2-created identities has one created lifecycle event.
- Registry counts and matrix totals must be recalculated from the mapping.
- A source change must be reflected in the appropriate stage without rewriting earlier events as if a later decision had already occurred.
