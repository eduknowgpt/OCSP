# CSP Cycle 1 Data Dictionary

## Purpose

This document defines the fields and controlled values used in:

- CSP-Competency-Registry.csv;
- CSP-Task-Competency-Mapping.csv;
- CSP-Competency-Lifecycle.csv.

All files use UTF-8 encoding, comma-separated fields, and one header row.

## General Conventions

| Convention | Definition |
| --- | --- |
| Competency identifier | C followed by two digits, such as C05. |
| Task identifier | task- followed by two digits, such as task-03. |
| Cycle identifier | cycle- followed by two digits, such as cycle-01. |
| Boolean value | Lowercase true or false. |
| Empty value | Information is unavailable or not applicable. It does not mean zero. |
| Multiple identifiers | Semicolon-separated, such as task-01;task-03. |
| File path | Relative to the CSP repository root, using forward slashes. |
| Event date | ISO 8601 date, YYYY-MM-DD, when supported by evidence; otherwise empty. |

## 1. Competency Registry

File: CSP-Competency-Registry.csv

Each row represents one competency identity.

| Field | Type | Required | Definition |
| --- | --- | :---: | --- |
| cycle_id | identifier | Yes | Cycle in which the competency was created. |
| competency_id | identifier | Yes | Stable competency identifier. |
| competency_title | text | Yes | Current canonical title. |
| origin_task | identifier | Yes | Task in which the competency was first created. |
| origin_iteration | integer | Yes | CSP iteration in which the competency was created. |
| registry_status | controlled text | Yes | Current state of the competency in the repository. |
| current_specification_file | path | Yes | File containing the current audited specification. |
| definition_review_file | path | Yes | Review supporting the current definition. |
| definition_adjustments_file | path | Yes | Adjustments supporting the current definition. |
| current_task_ids | identifier list | No | Tasks with current associations to the competency. |
| current_task_count | integer | Yes | Number of current task associations. |
| current_reuse_count | integer | Yes | Number of current associations classified as reuse. |
| historical_association_count | integer | Yes | Number of current and historical task associations. |
| notes | text | No | Context needed to interpret the registry entry. |

### registry_status

| Value | Definition |
| --- | --- |
| active | Available for current or future use; it may have no current task association. |
| deprecated | Retained for history but discouraged for new use. |
| replaced | Superseded by another competency identity. |
| retired | No longer available for new use. |

Cycle 1 currently uses only active.

## 2. Task–Competency Mapping

File: CSP-Task-Competency-Mapping.csv

Each row represents one competency association with one task and iteration.

| Field | Type | Required | Definition |
| --- | --- | :---: | --- |
| cycle_id | identifier | Yes | Cycle containing the task. |
| task_id | identifier | Yes | Task associated with the competency. |
| competency_id | identifier | Yes | Competency used by the task. |
| competency_title | text | Yes | Canonical title at the audited state. |
| usage_type | controlled text | Yes | Whether the task created or reused the competency. |
| origin_task | identifier | Yes | Task in which the competency was created. |
| reuse_mode | controlled text | Yes | How reuse is represented. |
| mapping_status | controlled text | Yes | Current or historical state of the association. |
| include_in_current_analysis | boolean | Yes | Whether the row is included in current quantitative results. |
| association_iteration | integer | Yes | Iteration in which the association was established. |
| review_decision | controlled text | Yes | Final decision recorded by the associated review. |
| role_in_task | text | Yes | Task-specific function of the competency. |
| report_file | path | Yes | CSP report documenting the association. |
| review_file | path | Yes | Expert review relevant to the association. |
| adjustments_file | path | No | Adjustments report; empty when no separate file exists. |
| notes | text | No | Additional interpretation or historical context. |

### usage_type

| Value | Definition |
| --- | --- |
| created | The competency originated in the associated task. |
| reused | The competency originated in another task. |

Validation rule: usage_type is created if and only if task_id equals origin_task.

### reuse_mode

| Value | Definition |
| --- | --- |
| not_applicable | Used when usage_type is created. |
| direct | Existing definition is used without a task-specific change to its identity or definition. |
| contextual_activation | The same competency is activated in a materially different context while preserving its identity. |
| revised_definition | The competency definition was refined before or during reuse while preserving its identifier and origin. |
| specialized_into | A reused base competency was qualified and subsequently represented by a documented derived specialization in the task. |
| additive_specialization | The current competency was created as a specialization that preserves an explicit relation to its base competency. |
| additive_refinement | An existing competency was added to a task to provide greater precision while the earlier association was retained. |

### mapping_status

| Value | Definition |
| --- | --- |
| current | Association belongs to the audited current mapping. |
| historical_replaced | Association is retained for history but has been replaced in the task. |
| historical_removed | Association was removed from the task without a replacement. |
| historical_specialized | Base association is retained to trace the creation of a current specialized competency. |

### include_in_current_analysis

| Value | Interpretation |
| --- | --- |
| true | Include in current totals, creation counts, reuse counts, and reuse rates. |
| false | Preserve for historical analysis and exclude from current totals. |

### review_decision

Documented values in Cycle 1:

- Approved;
- Approved with Revisions;
- Needs Revision;
- Approved with Required Revisions.

The value records the review outcome. It does not by itself indicate whether a later adjustments report was completed.

## 3. Competency Lifecycle

File: CSP-Competency-Lifecycle.csv

Each row represents one documented event affecting a competency.

| Field | Type | Required | Definition |
| --- | --- | :---: | --- |
| event_id | identifier | Yes | Unique lifecycle event identifier. |
| competency_id | identifier | Yes | Competency affected by the event. |
| event_sequence | integer | Yes | Order of events for the competency, beginning with 1. |
| event_type | controlled text | Yes | Kind of lifecycle event. |
| cycle_id | identifier | Yes | Cycle in which the event occurred. |
| task_id | identifier | Yes | Task that triggered or recorded the event. |
| iteration | integer | Yes | CSP iteration associated with the event. |
| event_date | date | No | Evidence-supported event date; empty when unavailable. |
| previous_state | controlled text | No | State immediately before the event. |
| resulting_state | controlled text | Yes | State after the event. |
| previous_title | text | No | Title before the event. |
| resulting_title | text | Yes | Title after the event. |
| decision | text | Yes | Decision or outcome associated with the event. |
| rationale | text | Yes | Reason for the event. |
| evidence_file | path | Yes | File supporting the event. |
| notes | text | No | Additional context. |

### event_type

| Value | Definition |
| --- | --- |
| created | Establishes a new competency identity. |
| revised | Changes wording, knowledge, mappings, or scope without changing identity. |
| renamed | Changes the canonical title while preserving identity. |
| reused | Associates an existing competency with another task. |
| replaced_in_task | Ends a task association because another competency becomes primary. |
| removed_from_task | Ends a task association without recording a replacement. |
| deprecated | Marks the competency as discouraged for future use. |
| reactivated | Returns a deprecated or retired competency to active use. |

Cycle 1 currently uses created, revised, renamed, reused, and replaced_in_task.

### Lifecycle states

| Value | Definition |
| --- | --- |
| active_associated | Active in the repository and associated with at least one task at that point. |
| active_unmapped | Active in the repository without a current task association. |
| deprecated | Available for historical reference but discouraged for reuse. |
| retired | No longer available for new use. |

## 4. Derived Matrix

File: CSP-Competency-Task-Matrix.md

The matrix is derived from mapping rows where include_in_current_analysis is true.

| Symbol | Meaning |
| --- | --- |
| C | usage_type is created. |
| R | usage_type is reused. |
| — | No current association. |

## 5. Quantitative Definitions

### Current relationship count

Count mapping rows where include_in_current_analysis is true.

### Creation count by task

Count current mapping rows for the selected task where usage_type is created.

### Reuse count by task

Count current mapping rows for the selected task where usage_type is reused.

### Reuse rate by task

Reuse rate equals reused relationships divided by the sum of created and reused relationships.

### Unique competencies

Count distinct competency_id values in the registry.

### First reuse

For a competency, use the first lifecycle event with event_type reused, ordered by the documented task and iteration sequence.

## 6. Validation Rules

1. Every mapping competency_id exists in the registry.
2. Every lifecycle competency_id exists in the registry.
3. Each competency has exactly one origin_task.
4. Every competency has one created lifecycle event.
5. event_sequence is unique and consecutive within each competency.
6. Created mappings satisfy task_id equals origin_task.
7. Reused mappings satisfy task_id differs from origin_task.
8. Registry usage counts equal the corresponding current mapping counts.
9. Matrix totals equal the current mapping totals.
10. Historical rows are excluded from current results.
11. File paths identify the artifact supporting the relationship or event.
12. Mapping titles match the canonical registry title unless the lifecycle explicitly records a rename.
