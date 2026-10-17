# CSP Data Dictionary — Cycle 4

## Scope and format

Eleven task reports, TASK401–TASK411, with the TASK401 adjustment taking precedence. CSVs use UTF-8 with BOM, comma separators, one header row and standard quoted escaping. Boolean values are lowercase true/false; list fields use semicolons except explicitly named JSON arrays. Empty fields mean unavailable or inapplicable, never zero. Paths are relative to this deliverables directory. Snapshot hashes identify exact source bytes.

## Source precedence

1. TASK401 adjustment overrides its original CM10 definition, CM07 activation and direct association table; it introduces CM12–CM17 specifications and the conditional CM12 extension.
2. Current TASK402 report defines CM18 and supersedes the earlier CM10 association. The adjustment’s earlier TASK402 recommendation is not substituted for the current report.
3. Current TASK405 includes CM23 BNCC alignment. Current TASK408 retains CM14 only. CM24 withdrawal is documented separately, with no active K19 pairing.
4. Current TASK411 uses [row, column]. Required example outputs do not automatically establish optional CM08 comparison and judgment.
5. Older per-task CSVs are not authoritative where they conflict with current reports/adjustments.

## Schemas

### CSP-Competency-Registry.csv

| Field | Definition |
| --- | --- |
| `cycle_id` | Dataset scope, cycle-04; distinct from identity origin. |
| `competency_id` | Stable CM identifier; CM24 is withdrawn and excluded from current counts. |
| `competency_title` | Current canonical English title; historical rows may refer to an earlier specification. |
| `origin_task` | Task where the identity was first specified, including origins as a component. |
| `origin_iteration` | Blank: no artificial iteration number assigned. |
| `registry_status` | active or withdrawn; active means retained in this documentary catalog, not formally approved. |
| `current_specification_file` | Relative snapshot containing the authoritative current definition; blank for the withdrawn proposal. |
| `definition_review_file` | Preserved TASK401 review for CM10; blank does not mean a formal review occurred. |
| `definition_adjustments_file` | Authoritative TASK401 adjustment when it specifies the identity or its reformulation. |
| `current_task_ids` | Semicolon-separated distinct direct current task associations; composition does not populate this field. |
| `current_task_count` | Count of distinct direct current task associations. |
| `current_reuse_count` | Count of direct current rows with usage_type=reused. |
| `historical_association_count` | Legacy field: distinct task–identity pairs represented by current AND historical mapping rows; not historical-only rows. |
| `notes` | Source-qualified interpretation or limitation. |
| `origin_cycle_id` | cycle-04 for all CM identities; no identity reuse from Cycles 1–3. |
| `creation_type` | original or composite; a composite retains complete components. |
| `base_competency_id` | Blank: no specialization asserted. |
| `cycle_participation` | current for a direct association; component_only for active atoms without direct rows; withdrawn for CM24. |
| `initial_title` | Earliest retained identity title; not a reconstruction of every intermediate proposal. |
| `definition_review_scope` | Scope note or pointer to the conversation decision record; not a review outcome. |
| `current_association_files` | Semicolon-separated snapshots of reports with current direct associations. |
| `component_competency_ids` | Fixed complete component IDs; blank for noncomposites. Never extra task associations. |
| `definition_source_sha256` | Hash of the authoritative definition snapshot; blank for CM24 because no current definition is retained. |
| `reference_refinement_id` | Blank: no external refinement identifier invented. |
| `definition` | Canonical current definition, not a task manifestation. |
| `disposition` | Expected orientation copied from the definition source, not an observed personality trait. |
| `ks_pairs_json` | JSON array of complete knowledge–Bloom pairings, source labels/conditions and observable operations. Composite arrays are unions of atoms; withdrawn CM24 has an empty array. |
| `specification_status` | documented_proposal or withdrawn_proposal; does not assert formal validation. |
| `bncc_alignment_scope` | Qualified source-reference note; task-level alignments must not be inferred automatically. |

### CSP-Task-Competency-Mapping.csv

| Field | Definition |
| --- | --- |
| `cycle_id` | Dataset scope, cycle-04; distinct from identity origin. |
| `task_id` | TASK401–TASK411, preserving the Cycle 4 identifiers. |
| `competency_id` | Stable CM identifier; CM24 is withdrawn and excluded from current counts. |
| `competency_title` | Current canonical English title; historical rows may refer to an earlier specification. |
| `usage_type` | created when the association task equals origin_task; reused otherwise. Component-only origins need not have a direct creation association. |
| `origin_task` | Task where the identity was first specified, including origins as a component. |
| `reuse_mode` | contextual_activation for reuse; composition for composite creation; not_applicable otherwise. |
| `mapping_status` | current, historical_replaced or historical_withdrawn. |
| `include_in_current_analysis` | true only for current rows; filter before all association statistics. |
| `association_iteration` | Blank: version sequence not established by an iteration scheme. |
| `review_decision` | Blank: no formal approval inferred. |
| `role_in_task` | Canonical functional title; activation_role is the formal core/supporting/extension label. |
| `report_file` | Snapshot supporting the report association; historical CM24 points to a conversation decision note. |
| `review_file` | Blank in mapping: a separate association approval is not inferred. |
| `adjustments_file` | TASK401 adjustment, authoritative over its original activation table. |
| `notes` | Source-qualified interpretation or limitation. |
| `origin_cycle_id` | cycle-04 for all CM identities; no identity reuse from Cycles 1–3. |
| `specification_stage` | current_report, adjusted, prior_specification, prior_association or conversation_record, as applicable. |
| `base_competency_id` | Blank: no specialization asserted. |
| `related_competency_id` | Replacement target for historical CM10 (CM18) or relevant event; blank otherwise. |
| `activation_constraint` | mandatory, optional or conditional; a prospective task requirement, not attainment. |
| `activation_mode` | Source mode, including semicolon-separated combinations such as operational;evaluative. |
| `activation_role` | Source role: core, supporting or extension. |
| `predominant_bloom_levels` | Blank: complete component-specific levels remain in registry ks_pairs_json, rather than an inferred single level. |
| `evidence_file` | Principal relative documentary source. |
| `evidence_section` | Section/table locator within evidence_file. |
| `activation_evidence_file` | Snapshot supporting activation labels. |
| `activation_evidence_section` | Activation-table locator or conversation decision locator. |
| `evidence_basis` | documentary_specification or conversation_decision_record; neither is observed student performance. |
| `component_competency_ids` | Fixed complete component IDs; blank for noncomposites. Never extra task associations. |
| `reuse_origin_scope` | within_cycle for reuse, not_applicable for creation. |
| `source_sha256` | SHA-256 of the cited documentary snapshot; for CM24 this hashes the decision note, not an unavailable original report. |

### CSP-Competency-Lifecycle.csv

| Field | Definition |
| --- | --- |
| `event_id` | Unique C04-E identifier, deterministic documentary order. |
| `competency_id` | Stable CM identifier; CM24 is withdrawn and excluded from current counts. |
| `event_sequence` | Per-identity documentary sequence; not exact calendar chronology. |
| `event_type` | created, reused, specification_reformulated, activation_revised, association_replaced, alignment_added, proposed or proposal_withdrawn. |
| `cycle_id` | Dataset scope, cycle-04; distinct from identity origin. |
| `task_id` | TASK401–TASK411, preserving the Cycle 4 identifiers. |
| `iteration` | Blank: no numerical event iteration is inferred. |
| `event_date` | Blank: exact event dates are not established. Build date is not an event date. |
| `previous_state` | Documentary state before the event; blank for creation/proposal. |
| `resulting_state` | Documentary state after the event. |
| `previous_title` | Previous retained title when applicable. |
| `resulting_title` | Title retained by the identity, including withdrawn CM24. |
| `decision` | Source-grounded event summary. |
| `rationale` | Documentary interpretation, without artificial formal approval. |
| `evidence_file` | Principal relative documentary source. |
| `notes` | Source-qualified interpretation or limitation. |
| `specification_stage` | current_report, adjusted, prior_specification, prior_association or conversation_record, as applicable. |
| `evidence_section` | Section/table locator within evidence_file. |
| `related_competency_id` | Replacement target for historical CM10 (CM18) or relevant event; blank otherwise. |
| `component_competency_ids` | Fixed complete component IDs; blank for noncomposites. Never extra task associations. |
| `source_sha256` | SHA-256 of the cited documentary snapshot; for CM24 this hashes the decision note, not an unavailable original report. |
| `refinement_id` | Blank: no post-cycle refinement ID assigned. |

### CSP-Competency-Composition.csv

| Field | Definition |
| --- | --- |
| `cycle_id` | Dataset scope, cycle-04; distinct from identity origin. |
| `composite_competency_id` | Composite parent identity: CM10 or CM18. |
| `component_competency_id` | Complete required atom identity. |
| `component_order` | Display ordering only; not a teaching or achievement sequence. |
| `component_required` | true: every listed component is constitutive. |
| `relationship_status` | current: relationship belongs to the authoritative composition. |
| `include_in_direct_task_counts` | false: composition is not a task association. |
| `component_ks_pairs_json` | Complete constitutive pairings of the component, including source conditions. |
| `evidence_file` | Principal relative documentary source. |
| `evidence_section` | Section/table locator within evidence_file. |
| `source_sha256` | SHA-256 of the cited documentary snapshot; for CM24 this hashes the decision note, not an unavailable original report. |

## Counting rules

Current totals: 11 tasks; 23 active identities; 20 identities directly associated; 3 component-only identities; 60 direct current associations (18 creation, 42 reuse); 7 composition links. One withdrawn identity and two historical mapping rows are excluded.
Activation distribution: mandatory 46; optional 8; conditional 6. Reuse rate = 42/60 = 70.00%.

Filter include_in_current_analysis=true before counting. Count each task–identity pair once. Include conditional and optional rows in the main denominator; mandatory-only views require their own denominator. A composite counts once per task. Component links do not increase association or attainment counts. All 23 active identities originate in Cycle 4, but only creation associations enter the creation-association count. Atoms first specified only as components have creation events without fabricated direct origin-task associations.

## Lifecycle limitations

The lifecycle preserves selected source-supported transitions, not every edit or intermediate proposal. The original broad CM10 source is retained, its structural revision is separate, and the former TASK402 association is historical. The conversation note supports CM24 proposal/withdrawal because the original pre-removal file is unavailable. Withdrawing CM24 does not renumber CM01–CM23. No dates, approvals, proficiency claims or retrospective redistribution of evidence are invented.

## BNCC interpretation

This consolidation does not add new alignment assertions. Qualified relationships and conditions remain in the specification snapshots, including the added CM23 alignment. Broad framework contributions are not skill equivalences. Prior-cycle competency identifiers are not merged with CM identifiers.

## Validation

Unique current task–identity pairs; registry references; complete composite unions; acyclic compositions; correct task totals; source hashes; and absence of K19 in active KS specifications are checked by the build. Registry statistics and the matrix derive from the same mapping. Snapshot reports retain their original embedded links; these may refer to wider workspace documents not included here. CSV documentary references resolve inside this package.
