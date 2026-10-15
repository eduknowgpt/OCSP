# CSP Refinement Following Cycles 1–3

Refinement identifier: RF-01-03  
Date: 2 October 2026  
Scope: 14 Theory of Computation tasks from the 2021, 2022 and 2025 applications.

## 1. Purpose

The completion of the three CSP application cycles enabled a joint examination of competency creation, reuse and semantic continuity. This refinement consolidates the resulting specification corpus by aligning repeated definitions, clarifying the evidence associated with contextual reuse, and preserving the decisions through which the competency set was established.

The process retains the instructional tasks, competency origins, adopted specializations and composition relations. Reconciliation of repeated component tables follows the task-level specifications and implemented adjustments. One additional reuse association is adopted to express PDA construction explicitly in TASK25.02. The refinement is dated after the three applications and is not presented as a review event that occurred during them.

## 2. Basis for the refinement

The reference corpus comprises task descriptions, CSP reports, expert-review reports and implemented adjustments where available, together with the three cycle registries, mappings and lifecycle records. Cycle 3 uses integrated specification reports. The catalog serves as a consolidated representation whose wording and chronology must remain consistent with the originating task packages.

Three distinctions guide the decisions:

1. A competency identity and its origin persist when it is reused. A new context alone does not create a new identity.
2. Knowledge–skill pairings and dispositions describe the reference definition. Role, mode and constraint describe its association with a task.
3. Historical proposals and review decisions remain traceable even when the maintained representation is corrected. A present refinement cannot supply evidence of an undocumented past approval.

The adjusted task-level definition is adopted as the reference where a later copy changes components without a corresponding documented revision. This is the reference-selection decision of RF-01-03; it does not assert that every earlier difference was necessarily a transcription error.

## 3. Decisions adopted

### RF-01 — Preserve identity and correct documentary chronology

C01 remains associated with Task01. C06 originates in Task03 and is additionally associated with Task01 in its second iteration. The statement that C01 was discontinued is removed from the maintained catalog history.

C15 and C16 originate in Task204, Cycle 2. C17, C18, C19 and C20 originate in TASK25.00, Cycle 3; C21 originates in TASK25.05, Cycle 3. Catalog labels that assigned these specifications to earlier application cycles are replaced by task-grounded histories. Separate review and adjustment events are not assigned to integrated Cycle 3 reports.

The additive specializations C07.01, C08.01 and C09.01 remain preserved. C13.01 retains C13 as its base; C05.01 retains C05. C20 retains its six components: C18, C17, C19, C04, C23 and C05.01. Earlier draft labels in the C20 catalog are aligned with these identifiers. C23 remains an independent identity.

### RF-02 — Reconcile repeated component specifications

| Competency | Adopted reference | Application of the refinement |
| --- | --- | --- |
| C01 | Task01 adjustments: three knowledge pairings | Complete the abbreviated second-iteration row; preserve its unchanged definition |
| C02 | Requirements Engineering; Creative retained among dispositions | Align later copies with the Task01 adjusted definition |
| C03 | Four Task01 dispositions; FSM, troubleshooting and simulation at Apply | Remove the unexplained additional disposition from maintained copies; retain simulation-target qualifications |
| C04 | Finite State Machines — Understand; Regular Expressions — Apply | Restore the reference pairing while retaining analytical activation where documented |
| C06 | FSM — Create; supporting knowledge — Apply; five Task03 dispositions | Align Task01 iteration 2 and Cycle 3 copies with the Task03 reference |
| C09 | Turing Machines — Apply; Inventive retained | Restore the Task02 reference instead of treating Inventive and Investigative as synonyms |
| C13.01 | PDA — Analyze; Analytical Rigor retained | Align TASK25.02 with the Task202 adjusted specification |
| C05, C07, C10, C14, C16 | Documented source components and example verbs | Harmonize repeated reference tables and distinguish contextual examples from definition changes |

The pairings used for C06 and C12 include observable actions already recorded in the detailed source specifications. Titles, origin tasks and prior specialization decisions remain unchanged. Reference tables in the catalog and repeated task tables use the same maintained values. Previous file contents remain available in the refinement archive.

### RF-03 — Qualify contextual simulation reuse

C03 retains Finite State Machines in its reference knowledge. Its recorded use with a PDA is described as contextual reuse of the simulation and testing procedure with an explicitly identified target model. PDA execution evidence does not, by itself, establish the entire FSM-specific reference performance.

This qualification preserves the adopted task associations and avoids an undocumented expansion of C03. Task04 wording is clarified so that the presence of FSM knowledge in reused C03 is consistent with the PDA solution model. In TASK25.02, C12 represents PDA construction directly.

### RF-04 — Make PDA-construction coverage explicit in TASK25.02

C12 is added to LO4 as a core, constructive and mandatory association. Its origin remains Task04, Cycle 1. C18, C17, C02 and C13.01 remain associated with LO4 in their supporting scopes; C22 continues to represent construction of the corresponding grammar.

The required PDA artifact and task deliverables are unchanged. The addition makes an existing required performance explicit in the competency mapping. The 2025 baseline contains nine associations; the maintained set contains ten. The new association is recorded as a decision of 2 October 2026, with the earlier set preserved.

### RF-05 — Specify the interpretation of activation and evidence

Existing mandatory, conditional and optional labels are retained. Task requirements remain in force regardless of those labels. Conditional simulation evidence does not authorize omission of a required simulator activity. Conceptual discussion of a Turing-machine variant is distinguished from evidence of implementing that variant. C14 contributes language-class comparison; C21 carries computational-complexity classification in TASK25.05.

C02 and C13.01 retain their scopes when they support broader task reasoning. A finite-state insufficiency argument alone does not demonstrate every part of positive DFA-use justification, and symbol naming alone does not demonstrate grammar-rule interpretation. These boundaries delimit the conclusions supported by an association.

### RF-06 — Repair source references

The eleven outdated references to Task04-CSRP-Report.md are updated to the existing Task04-CSP-Review-Report.md. The contents and outcome of the expert review are preserved.

### RF-07 — Synchronize the maintained records

The cycle registries, mappings, lifecycle files and readable views are updated together. Earlier lifecycle events cite the preserved source version where a report has been maintained. New events explicitly identify RF-01-03 and its date. Current report hashes are recalculated; baseline membership remains separately queryable.

## 4. Quantitative effect

| Scope | Before refinement | After refinement | Change |
| --- | ---: | ---: | --- |
| Distinct competency identities across three cycles | 28 | 28 | No new identity |
| Tasks | 14 | 14 | No new task |
| Current task–competency associations | 90 | 91 | Reuse of C12 added to TASK25.02 |
| Creation associations | 28 | 28 | Origins preserved |
| Reuse associations | 62 | 63 | One additional documented reuse |
| Overall association reuse rate | 68.9% | 69.2% | Denominator changes from 90 to 91 |
| Cycle 3 associations | 41 | 42 | TASK25.02 changes from nine to ten |
| Cycle 3 reuse associations | 33 | 34 | Eight creations remain |
| Cycle 3 reuse rate | 80.5% | 81.0% | All activation constraints remain included |

The pre-refinement figures remain valid for the archived corpus. Results reported for the maintained corpus must identify the inclusion of RF-01-03. Counts describe documentary associations and do not measure learner attainment.

## 5. Resolution of the preceding comparison

| Previous point | Treatment in RF-01-03 | Status |
| --- | --- | --- |
| F01: C06 components | Task03 reference restored in repeated tables | Reconciled |
| F02: C04 Bloom pairing | Understand restored; analytical activation preserved | Reconciled |
| F03: C13.01 components | Task202 pairing and disposition label restored | Reconciled |
| F04: C02 knowledge/dispositions | Task01 reference adopted | Reconciled |
| F05: C03 dispositions and PDA use | Reference dispositions restored; contextual scope qualified | Reconciled with explicit evidence boundary |
| F06: C09 catalog variant | Task02 reference adopted | Reconciled |
| F07: abbreviated C01 | Complete component block restored | Corrected |
| F08: catalog chronology | Task-grounded histories and preserved identities | Corrected |
| F09: old source paths | Existing review filename used | Corrected |
| F10: PDA construction | C12 added as a dated post-cycle association | Adopted |
| F11: activation/evidence distinctions | Existing labels retained with operational interpretation | Delimited; no claim of full mastery |
| F12: proposal versus identifier origin | Precursor history retained; origins unchanged | Preserved and clarified |
| F13: example verbs and labels | Source-reference tables harmonized | Reconciled |

## 6. Implications for the thesis

The three applications retain their empirical role in developing and examining competency specification, reuse, specialization and composition. RF-01-03 strengthens documentary consistency and makes the reference used in each repeated specification inspectable. It also provides an explicit example of post-application refinement: the inclusion of an existing competency to cover a performance already required by a task.

The resulting corpus supports claims about documented origins and maintained specification relations. It does not establish that every association represents an independently demonstrated competency, that every possible interpretation has been validated, or that the ontology has undergone an additional empirical evaluation. These distinctions preserve the scope of the original work while making the maintained evidence more precise.

## 7. Preservation and validation

Previous versions of every changed existing file are retained in the [refinement archive](refinements/RF-01-03-2026-10-02/README.md). A file manifest identifies the former and current content hashes and the decisions applied. Initial proposals and expert-review reports are preserved. Historical lifecycle source links identify the corresponding archived report where necessary.

Validation checks reconcile origins, current and baseline association totals, reference-table components, unchanged activation labels, C12 coverage in LO4, foreign-key relations, source paths and file hashes. No new approval category or undocumented event date is inferred.

The maintained [competency lifecycle](CSP-Cross-Cycle-Competency-Lifecycle.md) and [task matrix](CSP-Cross-Cycle-Task-Competency-Matrix.md) provide the cross-cycle views after this refinement.
