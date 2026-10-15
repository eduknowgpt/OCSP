# CSP Competency Lifecycle Across Cycles 1–3

## Conclusion and scope

The three cycle datasets agree on the origin task of every shared identifier. Their current-association counts reconcile. This supports the recorded provenance of 28 distinct retained identities across 14 tasks. It does not establish complete consistency of the component tables: unresolved knowledge, Bloom-level and disposition differences remain, and the supplementary catalog contains contradictory lifecycle claims.

This documentary comparison covers Cycle 1 (2021), Cycle 2 (2022), and the five consolidated Theory of Computation applications of Cycle 3 (2025). Cycle 4 and other task collections are outside scope. Sources were read on 2 October 2026. No source report, competency definition or per-cycle CSV was changed by this comparison.

The companion [task matrix](CSP-Cross-Cycle-Task-Competency-Matrix.md) provides the complete task view, counting rules and cross-cycle flows.

## Interpretation rules

- Origin identifies the first retained specification of a stable competency identifier. Earlier unnamed proposals are recorded separately where relevant.
- Task reports, reviews and implemented adjustments establish decisions. CSVs consolidate them; agreement among CSVs is not independent evidence. Supplementary catalog statements are checked against task packages.
- A new specialization is a new identity with a preserved base. A composite has component links. Neither relation deletes its related identities.
- Contextual role, mode and constraint belong to the task association. They do not silently replace knowledge–skill pairings or dispositions in the reusable definition.
- Lifecycle order is documentary order. Task01’s second iteration reuses C06 from Task03, despite the smaller task number. Exact meeting dates are not reconstructed.
- A source difference is classified as a documented revision, contextual variation, editorial difference or unresolved definition difference. Earlier reviewed versions are not overwritten with later wording.

## Verification results

| Check | Result |
| --- | --- |
| Shared identifier origins in the three registries and mappings | No contradictory origin task found |
| Current association totals | 26 + 23 + 41 = 90 |
| Creation and reuse | 28 creation associations; 62 reuse associations |
| Unique identities | 28; repeated registry entries are not additional identities |
| Per-cycle registry association counts | Reconciled with current mapping rows |
| Source references | Eleven cells retain the old Task04 review path; see F09 |
| Cycle 3 report-content hashes in mapping | Match the current source files |
| Full component-table comparison | 75 table blocks spanning all 28 identities; differences below |
| Supplementary catalog history | Conflicts found; see F08 |

Cycle 2 often records contextual activation without repeating complete component tables. Such rows support reuse provenance, not an independent verification of every component. The table snapshots below therefore distinguish complete specification evidence from task-activation summaries.

## Findings and proposed corrections

The actions below are recommendations. They have not been applied to the source records. Differences with an unlocated revision are not automatically classified as author errors: an additional documented decision could explain them.

<a id="f01"></a>

### F01 — C06: cognitive level and dispositions differ

Classification: Definition difference requiring reconciliation.

Task03 adjustments pair Finite State Machines with Create and list Inventive, Collaborative, Responsible, Proactive, Creative. Task01 iteration 2 retains Create but omits Inventive. TASK25.01 and TASK25.05 use Apply and Analytical, Responsible, Proactive, Collaborative. These are component tables, not only contextual activation labels. No corresponding identity-level revision was located in the inspected task packages.

Evidence: [Task03, Section 3.1, line 49](<cycle-01/en/Task03/Task03-CSP-Adjustments.md>); [Task01, second summary, line 47](<cycle-01/en/Task01/Review2/Task01-CSP-Report-v2.md>); [TASK25.01, C06 summary, line 114](<cycle-03/en/TASK25.01 - TheVendingMachine/TASK25.01-CSP-Report.md>); [TASK25.05, C06 summary, line 185](<cycle-03/en/TASK25.05 - OnlineJudges/TASK25.05-CSP-Report.md>).

Recommended action: Retain Task03 origin and all adopted associations. Establish which definition version the later tables reuse. If the change was unintended, restore the source components in the current reuse tables; if intentional, document the revision and its scope before propagating it. Do not silently rewrite the historical Create entry.

<a id="f02"></a>

### F02 — C04: Understand becomes Analyze

Classification: Definition difference requiring reconciliation.

Task01 and Task03 adjusted tables use Finite State Machines — Understand. TASK25.00 and TASK25.01 use Analyze. Task201 explicitly preserves the reusable definition while documenting analytical activation; that decision alone does not authorize replacing the component Bloom level.

Evidence: [Task03, revised set, line 108](<cycle-01/en/Task03/Task03-CSP-Adjustments.md>); [Task201, rationale, line 21](<cycle-02/en/Task201/TASK201-CSP-Adjustment.md>); [TASK25.00, C04 summary, line 217](<cycle-03/en/TASK25.00 - MusicCollection/Task25.00-CSP-Report.md>).

Recommended action: Keep the analytical task role. Reconcile the definition-level Understand/Analyze difference through an identified version or an editorial restoration supported by the originating records.

<a id="f03"></a>

### F03 — C13.01: PDA pairing and disposition vocabulary differ

Classification: Definition difference requiring reconciliation.

Task202 specifies Pushdown Automata — Analyze; TASK25.02 specifies Understand. The earlier disposition Analytical Rigor becomes Analytical. Task202 explicitly explains several other abbreviated disposition labels, but the later loss of Rigor is not explained by that note.

Evidence: [Task202, summary, line 119](<cycle-02/en/Task202/TASK202-CSP-Adustments.md>); [TASK25.02, summary, line 301](<cycle-03/en/TASK25.02 - TheMinotaursLabyrinth/TASK25.02-CSP-Report.md>).

Recommended action: Preserve Task202 origin and the specialization relation to C13. Reconcile PDA level and disposition labels with the intended definition version; do not treat a transversal activation role as authorization to alter components.

<a id="f04"></a>

### F04 — C02: Requirements Engineering narrows to Elicitation

Classification: Definition difference requiring reconciliation.

Task01 adjustments specify Requirements Engineering and include Creative. TASK25.01, TASK25.02 and TASK25.05 use Requirements Elicitation and omit Creative. These knowledge labels are not automatically interchangeable: the current files do not record a corresponding revision to the reusable definition.

Evidence: [Task01, validated summary, line 156](<cycle-01/en/Task01/Task01-CSP-Adjustments.md>); [TASK25.01, summary, line 298](<cycle-03/en/TASK25.01 - TheVendingMachine/TASK25.01-CSP-Report.md>); [TASK25.02, summary, line 193](<cycle-03/en/TASK25.02 - TheMinotaursLabyrinth/TASK25.02-CSP-Report.md>); [TASK25.05, summary, line 293](<cycle-03/en/TASK25.05 - OnlineJudges/TASK25.05-CSP-Report.md>).

Recommended action: Keep C02 identity. Record an accepted vocabulary relationship if elicitation is only a contextual focus, and retain the complete definition separately. Resolve the disposition omission explicitly.

<a id="f05"></a>

### F05 — C03: disposition addition and PDA scope

Classification: Component difference and scope boundary.

Task01 adjusted C03 has four dispositions; Task03, Task04 and Cycle 3 tables add Investigative. The addition has no separate explanation in the inspected reuse rationale. C03 also supports PDA testing in Task04, Task202 and TASK25.02 while its retained knowledge table names Finite State Machines. Task04 Section 2.1 says finite automata remain only in C14, yet its final C03 row still contains Finite State Machines.

Evidence: [Task01, C03, line 159](<cycle-01/en/Task01/Task01-CSP-Adjustments.md>); [Task03, C03, line 107](<cycle-01/en/Task03/Task03-CSP-Adjustments.md>); [Task04, scope statement, line 24](<cycle-01/en/Task04/Task04-CSP-Adjustments.md>); [Task04, C03 row, line 141](<cycle-01/en/Task04/Task04-CSP-Adjustments.md>); [Task202, PDA testing, line 184](<cycle-02/en/Task202/TASK202-CSP-Adustments.md>); [TASK25.02, Section 9.2, line 459](<cycle-03/en/TASK25.02 - TheMinotaursLabyrinth/TASK25.02-CSP-Report.md>).

Recommended action: Preserve the recorded reuse. Reconcile the disposition version and clarify whether the reusable simulation definition is intentionally general or FSM-specific. Correct Task04’s overbroad wording without silently substituting PDA knowledge into a preserved table.

<a id="f06"></a>

### F06 — C09: current task follows a conflicting catalog formulation

Classification: Component difference with local convention.

Task02 uses Turing Machines — Apply and Inventive. TASK25.03 uses Turing Machine Variants — Apply and Investigative. Its note explicitly acknowledges Investigative/Inventive disagreement in its source and adopts a local choice. This is traceable but does not establish a global revision of C09.

Evidence: [Task02, C09, line 77](<cycle-01/en/Task02/Task02-CSP-Adjustments.md>); [TASK25.03, disposition note, line 364](<cycle-03/en/TASK25.03 - TrafficControl/TASK25.03-CSP-Report.md>).

Recommended action: Keep the accepted conditional analytical activation. Identify the authoritative disposition and knowledge-label version and record the decision. Do not silently equate Inventive and Investigative.

<a id="f07"></a>

### F07 — C01: shortened second-iteration row is not the full definition

Classification: Incomplete repeated table.

The Task01 adjustment has three C01 knowledge pairings. Its second-iteration table lists only Finite State Machines for C01; the following continuation rows belong to C06. The narrative explicitly preserves C01 unchanged. The shorter row must not be interpreted as deletion of Requirements Engineering and Analytical and Critical Thinking.

Evidence: [Task01, full C01, line 153](<cycle-01/en/Task01/Task01-CSP-Adjustments.md>); [Task01, second C01 row, line 46](<cycle-01/en/Task01/Review2/Task01-CSP-Report-v2.md>).

Recommended action: In a future editorial correction, repeat the complete C01 block or label the row as an abbreviated reference to the unchanged definition. Preserve both C01 and C06 associations.

<a id="f08"></a>

### F08 — Catalog chronology conflicts with task-level origins

Classification: Origin and lifecycle conflict in supplementary sources.

C01_LifeCycle says C06 replaced C01 and C01 was discontinued, contradicting the explicit additive Task01 decision. C15 and C16 catalog histories label their original definition Cycle 1 although the task packages introduce them in Task204, Cycle 2. C17–C21 histories label original definition Cycle 1 and final version Cycle 2 despite Cycle 3 origins. Several describe separate CSRP/adjustment stages that are not established for those integrated Cycle 3 packages. These labels cannot be adopted as the CSP application-cycle chronology.

Evidence: [C01 catalog history, line 5](<../../Catálogo/C01_LifeCycle.md>); [Task01 additive decision, line 29](<cycle-01/en/Task01/Review2/Task01-CSP-Report-v2.md>); [C15 catalog history, line 4](<../../Catálogo/C15_LifeCycle.md>); [C16 catalog history, line 4](<../../Catálogo/C16_LifeCycle.md>); [C21 catalog history, line 4](<../../Catálogo/C21_LifeCycle.md>); [C17 catalog history, line 4](<../../Catálogo/C17_LifeCycle.md>); [C18 catalog history, line 5](<../../Catálogo/C18_LifeCycle.md>); [C19 catalog history, line 5](<../../Catálogo/C19_LifeCycle.md>); [C20 catalog history, line 6](<../../Catálogo/C20_LifeCycle.md>).

Recommended action: Align catalog origin fields with the task reports. If Cycle 1/2 meant internal draft iterations, rename them explicitly and supply evidence; do not conflate them with CSP application cycles. Preserve substantive component decisions without inventing dated review events.

<a id="f09"></a>

### F09 — Eleven references point to a renamed Task04 review

Classification: Reference maintenance.

The former Task04-CSRP-Report.md path is absent. The existing file is Task04-CSP-Review-Report.md. Three Cycle 1 registry cells, five Cycle 1 mapping cells and three Cycle 2 registry cells still use the former path. Cycle 3 uses the current path.

Evidence: [Cycle 1 registry](<cycle-01/CSP-Competency-Registry.csv>); [Cycle 1 mapping](<cycle-01/CSP-Task-Competency-Mapping.csv>); [Cycle 2 registry](<cycle-02/CSP-Competency-Registry.csv>); [Existing review](<cycle-01/en/Task04/Task04-CSP-Review-Report.md>).

Recommended action: Update the eleven path cells, preserving the historical filename as an alias if useful. This is a reference correction and does not change competencies or review outcomes.

<a id="f10"></a>

### F10 — TASK25.02: PDA construction lacks a direct construction association

Classification: Open methodological coverage decision.

LO4 requires construction of a PDA, but the retained association lists C18, C17, C02 and C13.01. C12 is mentioned only as a proposed addition in Section 9.2. C22 constructs the corresponding CFG and does not automatically cover PDA construction. C02 justification of DFA use and C13.01 grammar interpretation also require care when used for finite-state insufficiency or general notation.

Evidence: [TASK25.02, LO4, line 436](<cycle-03/en/TASK25.02 - TheMinotaursLabyrinth/TASK25.02-CSP-Report.md>); [TASK25.02, open decisions, line 459](<cycle-03/en/TASK25.02 - TheMinotaursLabyrinth/TASK25.02-CSP-Report.md>).

Recommended action: Consider adding existing C12 to LO4 as an explicit author decision, following the adopted C06 correction in TASK25.01. Until adopted, keep C12 outside TASK25.02 totals and preserve all original supporting links.

<a id="f11"></a>

### F11 — Conditional associations and task requirements need distinct interpretation

Classification: Activation/evidence boundary.

Task204 retains simulation and hierarchy objectives despite conditional/optional labels. TASK25.01 retains simulator and regular-expression requirements; TASK25.05 retains simulator and TM-concept objectives despite conditional associations. Task203 and TASK25.03 permit analytical C09 use, but discussion alone does not establish implemented variant performance. C14’s language/grammar classification contribution to TASK25.05 LO8 does not replace C21 complexity analysis.

Evidence: [Task204, activation summary, line 363](<cycle-02/en/Task204/TASK204-CSP-Adjustments.md>); [TASK25.01, boundaries, line 420](<cycle-03/en/TASK25.01 - TheVendingMachine/TASK25.01-CSP-Report.md>); [TASK25.05, LO mappings, line 380](<cycle-03/en/TASK25.05 - OnlineJudges/TASK25.05-CSP-Report.md>); [Task203, evidence overlap, line 43](<cycle-02/en/Task203/TASK203-CSP-Adjustments.md>).

Recommended action: Retain adopted labels. Define the condition and the evidence for each association when revising assessment documentation; do not count an association as proof of mastery or remove a task requirement because a competency is conditional.

<a id="f12"></a>

### F12 — First conceptual proposal differs from retained identifier origin

Classification: Origin convention requiring explicit wording.

Task03’s preliminary report proposes grammar classification and its adjustments remove it. The retained identifier C14 is specified in Task04. Likewise, the consolidated C04 identity follows the Task01 merger of two preliminary proposals. A statement that these ideas first appeared only in the final retained task would erase part of the history.

Evidence: [Task03 preliminary proposal, line 346](<cycle-01/en/Task03/Task03-CSP-Report.md>); [Task03 removal, line 33](<cycle-01/en/Task03/Task03-CSP-Adjustments.md>); [Task01 merger, line 44](<cycle-01/en/Task01/Task01-CSP-Adjustments.md>).

Recommended action: Keep C14 origin Task04 and C04 origin Task01 under the stable-identifier convention, while recording precursor proposals separately. Do not assign a later ID retrospectively to an unnumbered discarded proposal.

<a id="f13"></a>

### F13 — Action-verb lists and labels are not identical across reuse

Classification: Editorial/version traceability.

C05, C07, C10 and C16 largely retain their knowledge components and Bloom levels, but later tables expand or shorten example verbs. C16 also uses adjectival dispositions where Task204 uses nouns and omits the FPK suffix in some tables. These differences do not establish a new identity, but exact verb lists should not be described as unchanged without an alias/version rule.

Evidence: [Task02, C07/C10 tables, line 68](<cycle-01/en/Task02/Task02-CSP-Adjustments.md>); [Task204, C16 table, line 278](<cycle-02/en/Task204/TASK204-CSP-Adjustments.md>); [TASK25.03, C07/C10/C16, line 83](<cycle-03/en/TASK25.03 - TrafficControl/TASK25.03-CSP-Report.md>); [TASK25.05, C05 table, line 359](<cycle-03/en/TASK25.05 - OnlineJudges/TASK25.05-CSP-Report.md>).

Recommended action: Use a stable reference definition and identify task-specific example verbs explicitly. Standardize confirmed label aliases without treating distinct dispositions as synonyms.

## Relations supported by the records

| Relation | Recorded links | Interpretation |
| --- | --- | --- |
| Additive specialization | C07.01 → C07; C08.01 → C08; C09.01 → C09; C13.01 → C13; C05.01 → C05 | New identities preserve their bases |
| Composition | C20 → C18, C17, C19, C04, C23, C05.01 | Six components support one music-specific integrated performance |
| Additive reassociation | C06 added to Task01 in iteration 2; C01 preserved | Does not establish a formal C06 → C01 specialization relation |
| Task-association replacement | C13.01 → C23 in TASK25.01 and TASK25.03 | Replaces a task link, not a competency identity or definition |
| Documented title revision | C11: Infer and Identify → Identify; C16: Apply → Interpret | Same stable identifier, with retained previous wording |

For maintenance, the most useful additional relation is **task association → definition version**. It would distinguish intended reuse from unnoticed changes in copied tables. Also useful are **decision → supporting report section**, **contextual activation → expected evidence**, and **precursor proposal → retained or rejected outcome**. These are recommendations for documentation; this report does not assert that new ontology relations were implemented.

## Competency inventory

| ID | Retained title | Origin | Type | Current task associations | Reuse associations |
| --- | --- | --- | --- | ---: | ---: |
| [C01](#c01) | Develop Problem Solutions Using Automata | Task01 / cycle-01 | independent | 1 | 0 |
| [C02](#c02) | Justify the Use of Deterministic Finite Automata (DFAs) | Task01 / cycle-01 | independent | 6 | 5 |
| [C03](#c03) | Test Automata Using Simulators | Task01 / cycle-01 | independent | 9 | 8 |
| [C04](#c04) | Define Regular Expressions for Finite Automata | Task01 / cycle-01 | independent | 5 | 4 |
| [C05](#c05) | Write a Technical Report | Task01 / cycle-01 | independent | 10 | 9 |
| [C05.01](#c05-01) | Write mathematically rigorous answers | TASK25.00 / cycle-03 | specialization of C05 | 4 | 3 |
| [C06](#c06) | Develop Problem-Solving Solutions Using Finite State Machines | Task03 / cycle-01 | independent | 6 | 5 |
| [C07](#c07) | Develop Problem-Solving Solutions Using Turing Machines | Task02 / cycle-01 | independent | 3 | 2 |
| [C07.01](#c07-01) | Develop Integrated Multi-Agent Solutions Using Turing Machines | Task05 / cycle-01 | specialization of C07 | 1 | 0 |
| [C08](#c08) | Identify Turing Machine Variants | Task02 / cycle-01 | independent | 2 | 1 |
| [C08.01](#c08-01) | Analyze the System-Level Adequacy of Turing Machine Variants | Task05 / cycle-01 | specialization of C08 | 1 | 0 |
| [C09](#c09) | Apply Turing Machine Variants | Task02 / cycle-01 | independent | 3 | 2 |
| [C09.01](#c09-01) | Apply and Coordinate Turing Machine Variants in Integrated Architectures | Task05 / cycle-01 | specialization of C09 | 1 | 0 |
| [C10](#c10) | Test Turing Machines Using Simulators | Task02 / cycle-01 | independent | 4 | 3 |
| [C11](#c11) | Identify Patterns in Finite State Machines | Task03 / cycle-01 | independent | 2 | 1 |
| [C12](#c12) | Develop Problem-Solving Solutions Using Pushdown Automata | Task04 / cycle-01 | independent | 2 | 1 |
| [C13](#c13) | Interpret Rule-Based Notation | Task04 / cycle-01 | independent | 1 | 0 |
| [C13.01](#c13-01) | Interpret Formal Grammar-Based Rules | Task202 / cycle-02 | specialization of C13 | 2 | 1 |
| [C14](#c14) | Differentiate Classifications of Formal Grammars | Task04 / cycle-01 | independent | 6 | 5 |
| [C15](#c15) | Understand the Halting Problem and its Implications | Task204 / cycle-02 | independent | 2 | 1 |
| [C16](#c16) | Interpret Turing Machine Concepts to Analyze Computational System Capabilities | Task204 / cycle-02 | independent | 3 | 2 |
| [C17](#c17) | Apply operations on formal languages | TASK25.00 / cycle-03 | independent | 4 | 3 |
| [C18](#c18) | Model real-world problems using formal language concepts | TASK25.00 / cycle-03 | independent | 4 | 3 |
| [C19](#c19) | Apply homomorphisms in formal languages | TASK25.00 / cycle-03 | independent | 2 | 1 |
| [C20](#c20) | Model and analyze musical collections as formal languages | TASK25.00 / cycle-03 | composite | 1 | 0 |
| [C21](#c21) | Analyze Computational Complexity and the Implications of NP-Hardness | TASK25.05 / cycle-03 | independent | 1 | 0 |
| [C22](#c22) | Define Context-Free Grammars for Pushdown Automata | TASK25.02 / cycle-03 | independent | 1 | 0 |
| [C23](#c23) | Interpret and apply algebraic notation for strings and languages | TASK25.00 / cycle-03 | independent | 3 | 2 |

## Lifecycle and component evidence by competency

The use tables include historical associations separately. Formal activation labels are reproduced where present; an absent label is not interpreted as optional. Component snapshots reproduce knowledge, skills and dispositions from the named final/adjusted tables. They are documentary versions, not newly approved definitions. Differences in action verbs are retained rather than normalized away.

<a id="c01"></a>

### C01 — Develop Problem Solutions Using Automata

Origin: Task01 — cycle-01. Definition reference: [definition](<cycle-01/en/Task01/Task01-CSP-Adjustments.md>).

Reason for creation: Represent the general ability to construct an automata-based solution to the vending-machine problem.

Documented development: Task01 adjustment refines knowledge and terminology. Its second iteration retains C01 and adds C06; the current second-iteration table explicitly includes both.

| Cycle / task | Record | How the competency is used | Activation: role / mode / constraint | Evidence |
| --- | --- | --- | --- | --- |
| cycle-01 / Task01 | created | General automata-based solution development | not specified / not specified / not specified | [report](<cycle-01/en/Task01/Task01-CSP-Adjustments.md>) |

Lifecycle records: [cycle-01 events E001, E002, E003](<cycle-01/CSP-Competency-Lifecycle.csv>).

#### Component-table snapshots

| Source / table start | Dispositions | Knowledge–skill pairs as recorded |
| --- | --- | --- |
| [Task01-CSP-Adjustments.md, line 153](<cycle-01/en/Task01/Task01-CSP-Adjustments.md>) | Collaborative, Responsible, Proactive, Creative | Finite State Machines — Create (Construct, Develop, Design)<br>Requirements Engineering — Apply (Interpret, Implement, Organize)<br>Analytical and Critical Thinking (FPK) — Apply |
| [Task01-CSP-Report-v2.md, line 46](<cycle-01/en/Task01/Review2/Task01-CSP-Report-v2.md>) | Collaborative, Responsible, Proactive, Creative | Finite State Machines — Create (Construct, Develop, Design) |

Consistency follow-up: [F07](#f07), [F08](#f08).

<a id="c02"></a>

### C02 — Justify the Use of Deterministic Finite Automata (DFAs)

Origin: Task01 — cycle-01. Definition reference: [definition](<cycle-01/en/Task01/Task01-CSP-Adjustments.md>).

Reason for creation: Make justification of the deterministic finite-state model explicit and distinguish justification from construction.

Documented development: Task01 narrows the original DFA/NFA choice proposal to DFA justification. Later tasks retain the identity but vary its instructional role.

| Cycle / task | Record | How the competency is used | Activation: role / mode / constraint | Evidence |
| --- | --- | --- | --- | --- |
| cycle-01 / Task01 | created | Justification of the deterministic finite-state model | not specified / not specified / not specified | [report](<cycle-01/en/Task01/Task01-CSP-Adjustments.md>) |
| cycle-02 / Task201 | reused | Model justification | not_specified / justificatory;analytical / not_specified | [report](<cycle-02/en/Task201/TASK201-CSP-Adjustment.md>) |
| cycle-02 / Task204 | reused | Model justification | extension / justificatory / optional | [report](<cycle-02/en/Task204/TASK204-CSP-Adjustments.md>) |
| cycle-03 / TASK25.01 | reused | Justify the deterministic finite-state representation against the task requirements. | supporting / justificatory / mandatory | [report](<cycle-03/en/TASK25.01 - TheVendingMachine/TASK25.01-CSP-Report.md>) |
| cycle-03 / TASK25.02 | reused | Support analysis of finite-state suitability and insufficiency; positive DFA-use scope remains a boundary. | supporting / justificatory / mandatory | [report](<cycle-03/en/TASK25.02 - TheMinotaursLabyrinth/TASK25.02-CSP-Report.md>) |
| cycle-03 / TASK25.05 | reused | Optionally justify the deterministic finite-state workflow abstraction. | extension / justificatory / optional | [report](<cycle-03/en/TASK25.05 - OnlineJudges/TASK25.05-CSP-Report.md>) |

Lifecycle records: [cycle-01 events E004, E005](<cycle-01/CSP-Competency-Lifecycle.csv>); [cycle-02 events C02-E002, C02-E008, C02-E014, C02-E051, C02-E058, C02-E065](<cycle-02/CSP-Competency-Lifecycle.csv>); [cycle-03 events C03-E010, C03-E018, C03-E036](<cycle-03/CSP-Competency-Lifecycle.csv>).

#### Component-table snapshots

| Source / table start | Dispositions | Knowledge–skill pairs as recorded |
| --- | --- | --- |
| [Task01-CSP-Adjustments.md, line 156](<cycle-01/en/Task01/Task01-CSP-Adjustments.md>) | Investigative, Collaborative, Responsible, Proactive, Creative | Deterministic Finite Automata (DFAs) — Understand (Interpret, Explain)<br>Requirements Engineering — Apply<br>Analytical and Critical Thinking (FPK) — Apply |
| [Task01-CSP-Report-v2.md, line 50](<cycle-01/en/Task01/Review2/Task01-CSP-Report-v2.md>) | Investigative, Collaborative, Responsible, Proactive, Creative | Deterministic Finite Automata (DFAs) — Understand (Interpret, Explain)<br>Requirements Engineering — Apply<br>Analytical and Critical Thinking (FPK) — Apply |
| [TASK25.01-CSP-Report.md, line 298](<cycle-03/en/TASK25.01 - TheVendingMachine/TASK25.01-CSP-Report.md>) | Investigative, Collaborative, Responsible, Proactive | Deterministic Finite Automata (DFAs) — Understand (Identify, Explain, Recognize)<br>Requirements Elicitation — Apply (Identify, Interpret, Organize)<br>Analytical and Critical Thinking (FPK) — Apply (Analyze, Evaluate, Justify) |
| [TASK25.02-CSP-Report.md, line 193](<cycle-03/en/TASK25.02 - TheMinotaursLabyrinth/TASK25.02-CSP-Report.md>) | Investigative, Collaborative, Responsible, Proactive | Deterministic Finite Automata (DFAs) — Understand (Identify, Explain, Recognize)<br>Requirements Elicitation — Apply (Identify, Interpret, Organize)<br>Analytical and Critical Thinking (FPK) — Apply (Analyze, Evaluate, Justify) |
| [TASK25.05-CSP-Report.md, line 293](<cycle-03/en/TASK25.05 - OnlineJudges/TASK25.05-CSP-Report.md>) | Investigative, Collaborative, Responsible, Proactive | Deterministic Finite Automata (DFAs) — Understand (Identify, Explain, Recognize)<br>Requirements Elicitation — Apply (Identify, Interpret, Organize)<br>Analytical and Critical Thinking (FPK) — Apply (Analyze, Evaluate, Justify) |

Consistency follow-up: [F04](#f04), [F10](#f10).

<a id="c03"></a>

### C03 — Test Automata Using Simulators

Origin: Task01 — cycle-01. Definition reference: [definition](<cycle-01/en/Task01/Task01-CSP-Adjustments.md>).

Reason for creation: Represent simulator use, troubleshooting and model testing as an identifiable performance.

Documented development: Task01 replaces Automata over Infinite Objects with Finite State Machines and adds Modeling and Simulation. Subsequent PDA use retains the identifier but exposes a scope issue.

| Cycle / task | Record | How the competency is used | Activation: role / mode / constraint | Evidence |
| --- | --- | --- | --- | --- |
| cycle-01 / Task01 | created | Simulation and validation of the vending-machine automaton | not specified / not specified / not specified | [report](<cycle-01/en/Task01/Task01-CSP-Adjustments.md>) |
| cycle-01 / Task03 | reused | Simulation and validation of the Farmer Robot finite-state model | not specified / not specified / not specified | [report](<cycle-01/en/Task03/Task03-CSP-Adjustments.md>) |
| cycle-01 / Task04 | reused | Simulation and validation of a pushdown-automaton model | not specified / not specified / not specified | [report](<cycle-01/en/Task04/Task04-CSP-Adjustments.md>) |
| cycle-02 / Task201 | reused | Simulation and validation | not_specified / artifact-oriented / not_specified | [report](<cycle-02/en/Task201/TASK201-CSP-Adjustment.md>) |
| cycle-02 / Task202 | reused | PDA simulation | not_specified / artifact-oriented / not_specified | [report](<cycle-02/en/Task202/TASK202-CSP-Adustments.md>) |
| cycle-02 / Task204 | reused | FSM simulation | supporting / artifact-oriented / conditional | [report](<cycle-02/en/Task204/TASK204-CSP-Adjustments.md>) |
| cycle-03 / TASK25.01 | reused | Use simulation evidence to investigate payment/selection behavior; conditional label preserves task simulator requirements. | supporting / artifact-oriented / conditional | [report](<cycle-03/en/TASK25.01 - TheVendingMachine/TASK25.01-CSP-Report.md>) |
| cycle-03 / TASK25.02 | reused | Test the PDA/grammar behavior in JFLAP; retained FSM knowledge scope requires clarification. | supporting / artifact-oriented / mandatory | [report](<cycle-03/en/TASK25.02 - TheMinotaursLabyrinth/TASK25.02-CSP-Report.md>) |
| cycle-03 / TASK25.05 | reused | Simulate and test the workflow FSM under the recorded conditional association. | supporting / artifact-oriented / conditional | [report](<cycle-03/en/TASK25.05 - OnlineJudges/TASK25.05-CSP-Report.md>) |

Lifecycle records: [cycle-01 events E006, E007, E008, E009](<cycle-01/CSP-Competency-Lifecycle.csv>); [cycle-02 events C02-E003, C02-E009, C02-E015, C02-E020, C02-E025, C02-E031, C02-E052, C02-E059, C02-E066](<cycle-02/CSP-Competency-Lifecycle.csv>); [cycle-03 events C03-E011, C03-E019, C03-E037](<cycle-03/CSP-Competency-Lifecycle.csv>).

#### Component-table snapshots

| Source / table start | Dispositions | Knowledge–skill pairs as recorded |
| --- | --- | --- |
| [Task01-CSP-Adjustments.md, line 159](<cycle-01/en/Task01/Task01-CSP-Adjustments.md>) | Collaborative, Responsible, Proactive, Creative | Finite State Machines — Apply (Experiment, Relate, Simulate)<br>Problem Solving and Troubleshooting (FPK) — Apply<br>Modeling and Simulation — Apply |
| [Task03-CSP-Adjustments.md, line 107](<cycle-01/en/Task03/Task03-CSP-Adjustments.md>) | Investigative, Collaborative, Responsible, Proactive, Creative | Finite State Machines — Apply<br>Problem Solving and Troubleshooting (FPK) — Apply<br>Modeling and Simulation — Apply |
| [Task04-CSP-Adjustments.md, line 141](<cycle-01/en/Task04/Task04-CSP-Adjustments.md>) | Investigative, Collaborative, Responsible, Proactive, Creative | Finite State Machines — Apply<br>Problem Solving and Troubleshooting (FPK) — Apply<br>Modeling and Simulation — Apply |
| [Task01-CSP-Report-v2.md, line 53](<cycle-01/en/Task01/Review2/Task01-CSP-Report-v2.md>) | Collaborative, Responsible, Proactive, Creative | Finite State Machines — Apply (Experiment, Relate, Simulate)<br>Problem Solving and Troubleshooting (FPK) — Apply<br>Modeling and Simulation — Apply |
| [TASK25.01-CSP-Report.md, line 334](<cycle-03/en/TASK25.01 - TheVendingMachine/TASK25.01-CSP-Report.md>) | Investigative, Collaborative, Responsible, Proactive, Creative | Finite State Machines — Apply (Simulate, execute, validate)<br>Modeling and Simulation — Apply (Test, Validate)<br>Problem Solving and Troubleshooting (FPK) — Apply (Diagnose, Correct) |
| [TASK25.02-CSP-Report.md, line 371](<cycle-03/en/TASK25.02 - TheMinotaursLabyrinth/TASK25.02-CSP-Report.md>) | Investigative, Collaborative, Responsible, Proactive, Creative | Finite State Machines — Apply (Simulate, execute, validate)<br>Modeling and Simulation — Apply (Test, Validate)<br>Problem Solving and Troubleshooting (FPK) — Apply (Diagnose, Correct) |
| [TASK25.05-CSP-Report.md, line 257](<cycle-03/en/TASK25.05 - OnlineJudges/TASK25.05-CSP-Report.md>) | Investigative, Collaborative, Responsible, Proactive, Creative | Finite State Machines — Apply (Simulate, execute, validate)<br>Modeling and Simulation — Apply (Test, Validate)<br>Problem Solving and Troubleshooting (FPK) — Apply (Diagnose, Correct) |

Consistency follow-up: [F05](#f05), [F09](#f09), [F11](#f11).

<a id="c04"></a>

### C04 — Define Regular Expressions for Finite Automata

Origin: Task01 — cycle-01. Definition reference: [definition](<cycle-01/en/Task03/Task03-CSP-Adjustments.md>).

Reason for creation: Consolidate the overlapping regular-expression proposals in Task01 into one identity linking automata and regular expressions.

Documented development: Task01 merges two regular-expression proposals. Task03 reviews the definition before reuse. Task201 explicitly documents analytical activation without creating a specialization.

| Cycle / task | Record | How the competency is used | Activation: role / mode / constraint | Evidence |
| --- | --- | --- | --- | --- |
| cycle-01 / Task01 | created | Representation of finite-automaton behavior with regular expressions | not specified / not specified / not specified | [report](<cycle-01/en/Task01/Task01-CSP-Adjustments.md>) |
| cycle-01 / Task03 | reused | Definition of regular expressions corresponding to the finite-state model | not specified / not specified / not specified | [report](<cycle-01/en/Task03/Task03-CSP-Adjustments.md>) |
| cycle-02 / Task201 | reused | Symbolic reasoning supporting FSM modeling | supporting / analytical;conceptual / not_specified | [report](<cycle-02/en/Task201/TASK201-CSP-Adjustment.md>) |
| cycle-03 / TASK25.00 | reused | Describe song collections through regular expressions and conceptual representation correspondence. | core / artifact-oriented / mandatory | [report](<cycle-03/en/TASK25.00 - MusicCollection/Task25.00-CSP-Report.md>) |
| cycle-03 / TASK25.01 | reused | Investigate regular-expression correspondence as a conditional extension. | extension / analytical / conditional | [report](<cycle-03/en/TASK25.01 - TheVendingMachine/TASK25.01-CSP-Report.md>) |

Lifecycle records: [cycle-01 events E010, E011, E012, E013](<cycle-01/CSP-Competency-Lifecycle.csv>); [cycle-02 events C02-E004, C02-E010, C02-E016](<cycle-02/CSP-Competency-Lifecycle.csv>); [cycle-03 events C03-E001, C03-E012](<cycle-03/CSP-Competency-Lifecycle.csv>).

#### Component-table snapshots

| Source / table start | Dispositions | Knowledge–skill pairs as recorded |
| --- | --- | --- |
| [Task01-CSP-Adjustments.md, line 162](<cycle-01/en/Task01/Task01-CSP-Adjustments.md>) | Investigative, Collaborative, Responsible, Proactive, Creative | Finite State Machines — Understand<br>Regular Expressions — Apply<br>Analytical and Critical Thinking (FPK) — Apply |
| [Task03-CSP-Adjustments.md, line 108](<cycle-01/en/Task03/Task03-CSP-Adjustments.md>) | Investigative, Collaborative, Responsible, Proactive, Creative | Finite State Machines — Understand<br>Regular Expressions — Apply<br>Analytical and Critical Thinking (FPK) — Apply |
| [Task01-CSP-Report-v2.md, line 56](<cycle-01/en/Task01/Review2/Task01-CSP-Report-v2.md>) | Investigative, Collaborative, Responsible, Proactive, Creative | Finite State Machines — Understand<br>Regular Expressions — Apply<br>Analytical and Critical Thinking (FPK) — Apply |
| [Task25.00-CSP-Report.md, line 217](<cycle-03/en/TASK25.00 - MusicCollection/Task25.00-CSP-Report.md>) | Investigative; Collaborative; Responsible; Proactive; Creative | Finite State Machines — Analyze<br>Regular Expressions — Apply<br>Analytical and Critical Thinking (FPK) — Apply |
| [TASK25.01-CSP-Report.md, line 370](<cycle-03/en/TASK25.01 - TheVendingMachine/TASK25.01-CSP-Report.md>) | Investigative; Collaborative; Responsible; Proactive; Creative | Finite State Machines — Analyze<br>Regular Expressions — Apply<br>Analytical and Critical Thinking (FPK) — Apply |

Consistency follow-up: [F02](#f02), [F11](#f11), [F12](#f12).

<a id="c05"></a>

### C05 — Write a Technical Report

Origin: Task01 — cycle-01. Definition reference: [definition](<cycle-01/en/Task01/Task01-CSP-Adjustments.md>).

Reason for creation: Represent technical documentation of the solution, modeling decisions and results.

Documented development: Task01 refines the title from Collaborative Technical Report Writing. TASK25.00 creates C05.01; C05 remains reusable and returns in TASK25.05.

| Cycle / task | Record | How the competency is used | Activation: role / mode / constraint | Evidence |
| --- | --- | --- | --- | --- |
| cycle-01 / Task01 | created | Documentation of the solution and results | not specified / not specified / not specified | [report](<cycle-01/en/Task01/Task01-CSP-Adjustments.md>) |
| cycle-01 / Task02 | reused | Documentation of the traffic-control solution | not specified / not specified / not specified | [report](<cycle-01/en/Task02/Task02-CSP-Adjustments.md>) |
| cycle-01 / Task03 | reused | Documentation of the Farmer Robot solution | not specified / not specified / not specified | [report](<cycle-01/en/Task03/Task03-CSP-Adjustments.md>) |
| cycle-01 / Task04 | reused | Documentation of the return-navigation solution | not specified / not specified / not specified | [report](<cycle-01/en/Task04/Task04-CSP-Adjustments.md>) |
| cycle-01 / Task05 | reused | Documentation of the robot modules and examples | not specified / not specified / not specified | [report](<cycle-01/en/Task05/TASK05-CSP-Adjustments.md>) |
| cycle-02 / Task201 | reused | Technical reporting | transversal / artifact-oriented;justificatory / not_specified | [report](<cycle-02/en/Task201/TASK201-CSP-Adjustment.md>) |
| cycle-02 / Task202 | reused | Technical reporting | transversal / not_specified / not_specified | [report](<cycle-02/en/Task202/TASK202-CSP-Adustments.md>) |
| cycle-02 / Task203 | reused | Technical reporting | transversal / artifact-oriented / not_specified | [report](<cycle-02/en/Task203/TASK203-CSP-Adjustments.md>) |
| cycle-02 / Task204 | reused | Technical reporting as evidence vehicle | transversal / artifact-oriented / mandatory | [report](<cycle-02/en/Task204/TASK204-CSP-Adjustments.md>) |
| cycle-03 / TASK25.05 | reused | Communicate the model, computational analysis and conclusions in the SBC article. | transversal / artifact-oriented / mandatory | [report](<cycle-03/en/TASK25.05 - OnlineJudges/TASK25.05-CSP-Report.md>) |

Lifecycle records: [cycle-01 events E014, E015, E016, E017, E018, E019](<cycle-01/CSP-Competency-Lifecycle.csv>); [cycle-02 events C02-E005, C02-E011, C02-E017, C02-E022, C02-E027, C02-E033, C02-E039, C02-E044, C02-E049, C02-E054, C02-E061, C02-E068](<cycle-02/CSP-Competency-Lifecycle.csv>); [cycle-03 events C03-E038](<cycle-03/CSP-Competency-Lifecycle.csv>).

#### Component-table snapshots

| Source / table start | Dispositions | Knowledge–skill pairs as recorded |
| --- | --- | --- |
| [Task01-CSP-Adjustments.md, line 165](<cycle-01/en/Task01/Task01-CSP-Adjustments.md>) | Collaborative, Meticulous, Responsible | Written Communication (FPK) — Apply (Write, Structure, Revise, Refine) |
| [Task02-CSP-Adjustments.md, line 82](<cycle-01/en/Task02/Task02-CSP-Adjustments.md>) | Collaborative, Meticulous, Responsible | Written Communication (FPK) — Apply (Write, Structure, Revise, Refine) |
| [Task03-CSP-Adjustments.md, line 109](<cycle-01/en/Task03/Task03-CSP-Adjustments.md>) | Collaborative, Meticulous, Responsible | Written Communication (FPK) — Apply |
| [Task04-CSP-Adjustments.md, line 142](<cycle-01/en/Task04/Task04-CSP-Adjustments.md>) | Collaborative, Meticulous, Responsible | Written Communication (FPK) — Apply |
| [TASK05-CSP-Adjustments.md, line 135](<cycle-01/en/Task05/TASK05-CSP-Adjustments.md>) | Collaborative; Meticulous; Responsible | Written Communication — Apply. |
| [Task01-CSP-Report-v2.md, line 59](<cycle-01/en/Task01/Review2/Task01-CSP-Report-v2.md>) | Collaborative, Meticulous, Responsible | Written Communication (FPK) — Apply (Write, Structure, Revise, Refine) |
| [TASK25.05-CSP-Report.md, line 363](<cycle-03/en/TASK25.05 - OnlineJudges/TASK25.05-CSP-Report.md>) | Collaborative, Meticulous, Responsible | Written Communication (FPK) — Apply (Document, Present, Write, Revise) |

Consistency follow-up: [F09](#f09), [F13](#f13).

<a id="c05-01"></a>

### C05.01 — Write mathematically rigorous answers

Origin: TASK25.00 — cycle-03. Definition reference: [definition](<cycle-03/en/TASK25.00 - MusicCollection/Task25.00-CSP-Report.md>).

Reason for creation: Specify mathematically rigorous written answers with definitions, arguments, examples and counterexamples beyond generic technical reporting.

Documented development: Created in TASK25.00 as specialization of C05; reused in TASK25.01, TASK25.02 and TASK25.03. It is not substituted for C05 in TASK25.05.

Relation: additive specialization of [C05](CSP-Cross-Cycle-Competency-Lifecycle.md#c05).

| Cycle / task | Record | How the competency is used | Activation: role / mode / constraint | Evidence |
| --- | --- | --- | --- | --- |
| cycle-03 / TASK25.00 | created | Justify answers through definitions, formal arguments, examples and counterexamples. | transversal / justificatory / mandatory | [report](<cycle-03/en/TASK25.00 - MusicCollection/Task25.00-CSP-Report.md>) |
| cycle-03 / TASK25.01 | reused | Justify correctness, recognition and model limitations in the technical report. | transversal / justificatory / mandatory | [report](<cycle-03/en/TASK25.01 - TheVendingMachine/TASK25.01-CSP-Report.md>) |
| cycle-03 / TASK25.02 | reused | Justify correctness, equivalence claims and model limitations in the report. | transversal / justificatory / mandatory | [report](<cycle-03/en/TASK25.02 - TheMinotaursLabyrinth/TASK25.02-CSP-Report.md>) |
| cycle-03 / TASK25.03 | reused | Produce rigorous correctness, modeling and computational-limit arguments. | transversal / justificatory / mandatory | [report](<cycle-03/en/TASK25.03 - TrafficControl/TASK25.03-CSP-Report.md>) |

Lifecycle records: [cycle-03 events C03-E002, C03-E013, C03-E020, C03-E028](<cycle-03/CSP-Competency-Lifecycle.csv>).

#### Component-table snapshots

| Source / table start | Dispositions | Knowledge–skill pairs as recorded |
| --- | --- | --- |
| [Task25.00-CSP-Report.md, line 297](<cycle-03/en/TASK25.00 - MusicCollection/Task25.00-CSP-Report.md>) | Meticulous; Responsible | Written Communication (FPK) — Apply<br>Analytical and Critical Thinking (FPK) — Analyze / Evaluate |
| [TASK25.01-CSP-Report.md, line 263](<cycle-03/en/TASK25.01 - TheVendingMachine/TASK25.01-CSP-Report.md>) | Meticulous; Responsible | Written Communication (FPK) — Apply<br>Analytical and Critical Thinking (FPK) — Analyze / Evaluate |
| [TASK25.02-CSP-Report.md, line 336](<cycle-03/en/TASK25.02 - TheMinotaursLabyrinth/TASK25.02-CSP-Report.md>) | Meticulous; Responsible | Written Communication (FPK) — Apply<br>Analytical and Critical Thinking (FPK) — Analyze / Evaluate |
| [TASK25.03-CSP-Report.md, line 304](<cycle-03/en/TASK25.03 - TrafficControl/TASK25.03-CSP-Report.md>) | Meticulous; Responsible | Written Communication (FPK) — Apply<br>Analytical and Critical Thinking (FPK) — Analyze / Evaluate |

Comparison result: no contradictory origin or component-level difference identified in these displayed final/adjusted snapshots. Where there is only one complete table, this establishes a reference, not repeated independent verification.

<a id="c06"></a>

### C06 — Develop Problem-Solving Solutions Using Finite State Machines

Origin: Task03 — cycle-01. Definition reference: [definition](<cycle-01/en/Task03/Task03-CSP-Adjustments.md>).

Reason for creation: Name the finite-state solution-construction scope more precisely in Task03; later reuse in Task01 does not move its origin.

Documented development: Created in Task03, then associated additively with Task01 in its second iteration. TASK25.01 later adds C06 to LO3 to cover recognizer construction explicitly.

| Cycle / task | Record | How the competency is used | Activation: role / mode / constraint | Evidence |
| --- | --- | --- | --- | --- |
| cycle-01 / Task01 | reused | Finite-state modeling of the vending-machine solution | not specified / not specified / not specified | [report](<cycle-01/en/Task01/Review2/Task01-CSP-Report-v2.md>) |
| cycle-01 / Task03 | created | Construction of the Farmer Robot finite-state solution | not specified / not specified / not specified | [report](<cycle-01/en/Task03/Task03-CSP-Adjustments.md>) |
| cycle-02 / Task201 | reused | FSM modeling | core / constructive;analytical / not_specified | [report](<cycle-02/en/Task201/TASK201-CSP-Adjustment.md>) |
| cycle-02 / Task204 | reused | FSM representation of OJ outcomes | supporting / constructive / mandatory | [report](<cycle-02/en/Task204/TASK204-CSP-Adjustments.md>) |
| cycle-03 / TASK25.01 | reused | Construct the vending-machine recognizer for LO3; added while retaining the original supporting associations. | core / constructive / mandatory | [report](<cycle-03/en/TASK25.01 - TheVendingMachine/TASK25.01-CSP-Report.md>) |
| cycle-03 / TASK25.05 | reused | Construct the finite-state representation of the Online Judge workflow. | supporting / constructive / mandatory | [report](<cycle-03/en/TASK25.05 - OnlineJudges/TASK25.05-CSP-Report.md>) |

Lifecycle records: [cycle-01 events E020, E021, E022](<cycle-01/CSP-Competency-Lifecycle.csv>); [cycle-02 events C02-E001, C02-E007, C02-E013, C02-E050, C02-E057, C02-E064](<cycle-02/CSP-Competency-Lifecycle.csv>); [cycle-03 events C03-E014, C03-E039](<cycle-03/CSP-Competency-Lifecycle.csv>).

#### Component-table snapshots

| Source / table start | Dispositions | Knowledge–skill pairs as recorded |
| --- | --- | --- |
| [Task03-CSP-Adjustments.md, line 105](<cycle-01/en/Task03/Task03-CSP-Adjustments.md>) | Inventive, Collaborative, Responsible, Proactive, Creative | Finite State Machines — Create<br>Requirements Engineering — Apply<br>Analytical and Critical Thinking (FPK) — Apply |
| [Task01-CSP-Report-v2.md, line 47](<cycle-01/en/Task01/Review2/Task01-CSP-Report-v2.md>) | Collaborative, Responsible, Proactive, Creative | Finite State Machines — Create (Construct, Develop, Design)<br>Requirements Engineering — Apply (Interpret, Implement, Organize)<br>Analytical and Critical Thinking (FPK) — Apply |
| [TASK25.01-CSP-Report.md, line 114](<cycle-03/en/TASK25.01 - TheVendingMachine/TASK25.01-CSP-Report.md>) | Analytical; Responsible; Proactive; Collaborative | Finite State Machines — Apply (Design, Construct, Model, Validate)<br>Requirements Engineering — Apply (Interpret, Specify, Translate)<br>Analytical and Critical Thinking (FPK) — Apply (Analyze, Evaluate, Justify) |
| [TASK25.05-CSP-Report.md, line 185](<cycle-03/en/TASK25.05 - OnlineJudges/TASK25.05-CSP-Report.md>) | Analytical; Responsible; Proactive; Collaborative | Finite State Machines — Apply (Design, Construct, Model, Validate)<br>Requirements Engineering — Apply (Interpret, Specify, Translate)<br>Analytical and Critical Thinking (FPK) — Apply (Analyze, Evaluate, Justify) |

Consistency follow-up: [F01](#f01).

<a id="c07"></a>

### C07 — Develop Problem-Solving Solutions Using Turing Machines

Origin: Task02 — cycle-01. Definition reference: [definition](<cycle-01/en/Task02/Task02-CSP-Adjustments.md>).

Reason for creation: Represent construction of a Turing-machine solution for traffic classification and counting.

Documented development: Task02 clarifies foundational construction scope and excludes the Church–Turing Thesis from assessed components. Task05 creates C07.01; later reuse of C07 remains valid.

| Cycle / task | Record | How the competency is used | Activation: role / mode / constraint | Evidence |
| --- | --- | --- | --- | --- |
| cycle-01 / Task02 | created | Construction of a Turing-machine solution for traffic control | not specified / not specified / not specified | [report](<cycle-01/en/Task02/Task02-CSP-Adjustments.md>) |
| cycle-01 / Task05 | historical; excluded from current totals | Task05 formalized C07.01 as an additive specialization of C07. | not specified / not specified / not specified | [report](<cycle-01/en/Task05/TASK05-CSP-Adjustments.md>) |
| cycle-02 / Task203 | reused | TM-based parking control | core / constructive / not_specified | [report](<cycle-02/en/Task203/TASK203-CSP-Adjustments.md>) |
| cycle-03 / TASK25.03 | reused | Construct the traffic-counting/classification Turing Machine with the required outputs. | core / constructive / mandatory | [report](<cycle-03/en/TASK25.03 - TrafficControl/TASK25.03-CSP-Report.md>) |

Lifecycle records: [cycle-01 events E023, E024, E025](<cycle-01/CSP-Competency-Lifecycle.csv>); [cycle-02 events C02-E035, C02-E040, C02-E045](<cycle-02/CSP-Competency-Lifecycle.csv>); [cycle-03 events C03-E029](<cycle-03/CSP-Competency-Lifecycle.csv>).

#### Component-table snapshots

| Source / table start | Dispositions | Knowledge–skill pairs as recorded |
| --- | --- | --- |
| [Task02-CSP-Adjustments.md, line 72](<cycle-01/en/Task02/Task02-CSP-Adjustments.md>) | Collaborative, Responsible, Proactive, Creative, Inventive | Turing Machines — Create (Develop, Invent, Construct)<br>Requirements Engineering — Apply (Interpret, Organize)<br>Analytical and Critical Thinking (FPK) — Apply (Decompose, Identify) |
| [TASK25.03-CSP-Report.md, line 195](<cycle-03/en/TASK25.03 - TrafficControl/TASK25.03-CSP-Report.md>) | Collaborative, Responsible, Proactive, Creative, Inventive | Turing Machines — Create (Design, Construct, Develop, Validate)<br>Requirements Engineering — Apply (Interpret, Organize, Specify)<br>Analytical and Critical Thinking (FPK) — Apply (Decompose, Identify, Justify) |

Consistency follow-up: [F13](#f13).

<a id="c07-01"></a>

### C07.01 — Develop Integrated Multi-Agent Solutions Using Turing Machines

Origin: Task05 — cycle-01. Definition reference: [definition](<cycle-01/en/Task05/TASK05-CSP-Adjustments.md>).

Reason for creation: Add system-level construction and integration of interacting robot behaviors to the C07 base.

Documented development: Formalized in Task05 adjustments as additive specialization of C07. No later current reuse is documented in the audited tasks.

Relation: additive specialization of [C07](CSP-Cross-Cycle-Competency-Lifecycle.md#c07).

| Cycle / task | Record | How the competency is used | Activation: role / mode / constraint | Evidence |
| --- | --- | --- | --- | --- |
| cycle-01 / Task05 | created | Integrated construction of a multi-agent computational system | not specified / not specified / not specified | [report](<cycle-01/en/Task05/TASK05-CSP-Adjustments.md>) |

Lifecycle records: [cycle-01 events E043](<cycle-01/CSP-Competency-Lifecycle.csv>).

#### Component-table snapshots

| Source / table start | Dispositions | Knowledge–skill pairs as recorded |
| --- | --- | --- |
| [TASK05-CSP-Adjustments.md, line 131](<cycle-01/en/Task05/TASK05-CSP-Adjustments.md>) | Collaborative; Responsible; Proactive; Creative; Inventive | Turing Machines (Universal and Integrated Use) — Create: Design, Integrate, Construct.<br>Requirements Engineering (System-Level) — Apply: Elicit, Formalize, Align.<br>Analytical and Critical Thinking (FPK) — Analyze: Decompose, Examine, Evaluate. |

Comparison result: no contradictory origin or component-level difference identified in these displayed final/adjusted snapshots. Where there is only one complete table, this establishes a reference, not repeated independent verification.

<a id="c08"></a>

### C08 — Identify Turing Machine Variants

Origin: Task02 — cycle-01. Definition reference: [definition](<cycle-01/en/Task02/Task02-CSP-Adjustments.md>).

Reason for creation: Separate recognition and differentiation of Turing-machine variants from their application.

Documented development: Task02 separates identification from application. Task05 creates C08.01 for system-level analysis. Task203 retains C08 as theoretical justification.

| Cycle / task | Record | How the competency is used | Activation: role / mode / constraint | Evidence |
| --- | --- | --- | --- | --- |
| cycle-01 / Task02 | created | Identification and explanation of Turing-machine variants | not specified / not specified / not specified | [report](<cycle-01/en/Task02/Task02-CSP-Adjustments.md>) |
| cycle-01 / Task05 | historical; excluded from current totals | Task05 formalized C08.01 as an additive specialization of C08. | not specified / not specified / not specified | [report](<cycle-01/en/Task05/TASK05-CSP-Adjustments.md>) |
| cycle-02 / Task203 | reused | Comparison and justification of TM variants | not_specified / analytical;justificatory / not_specified | [report](<cycle-02/en/Task203/TASK203-CSP-Adjustments.md>) |

Lifecycle records: [cycle-01 events E026, E027, E028](<cycle-01/CSP-Competency-Lifecycle.csv>); [cycle-02 events C02-E036, C02-E041, C02-E046](<cycle-02/CSP-Competency-Lifecycle.csv>).

#### Component-table snapshots

| Source / table start | Dispositions | Knowledge–skill pairs as recorded |
| --- | --- | --- |
| [Task02-CSP-Adjustments.md, line 75](<cycle-01/en/Task02/Task02-CSP-Adjustments.md>) | Investigative, Collaborative, Responsible, Proactive | Turing Machines — Understand (Differentiate, Recognize, Explain)<br>Analytical and Critical Thinking (FPK) — Apply |

Comparison result: no contradictory origin or component-level difference identified in these displayed final/adjusted snapshots. Where there is only one complete table, this establishes a reference, not repeated independent verification.

<a id="c08-01"></a>

### C08.01 — Analyze the System-Level Adequacy of Turing Machine Variants

Origin: Task05 — cycle-01. Definition reference: [definition](<cycle-01/en/Task05/TASK05-CSP-Adjustments.md>).

Reason for creation: Represent system-level adequacy analysis of Turing-machine variants as decision support.

Documented development: Formalized in Task05 adjustments as additive specialization of C08. Analyze describes its decision-support role; detailed component mappings remain authoritative.

Relation: additive specialization of [C08](CSP-Cross-Cycle-Competency-Lifecycle.md#c08).

| Cycle / task | Record | How the competency is used | Activation: role / mode / constraint | Evidence |
| --- | --- | --- | --- | --- |
| cycle-01 / Task05 | created | System-level analysis supporting design decisions | not specified / not specified / not specified | [report](<cycle-01/en/Task05/TASK05-CSP-Adjustments.md>) |

Lifecycle records: [cycle-01 events E044](<cycle-01/CSP-Competency-Lifecycle.csv>).

#### Component-table snapshots

| Source / table start | Dispositions | Knowledge–skill pairs as recorded |
| --- | --- | --- |
| [TASK05-CSP-Adjustments.md, line 132](<cycle-01/en/Task05/TASK05-CSP-Adjustments.md>) | Investigative; Collaborative; Responsible; Proactive | Turing Machine Variants (System-Level Perspective) — Analyze: Compare, Examine, Differentiate.<br>Analytical and Critical Thinking (FPK) — Analyze: Evaluate, Justify, Relate. |

Comparison result: no contradictory origin or component-level difference identified in these displayed final/adjusted snapshots. Where there is only one complete table, this establishes a reference, not repeated independent verification.

<a id="c09"></a>

### C09 — Apply Turing Machine Variants

Origin: Task02 — cycle-01. Definition reference: [definition](<cycle-01/en/Task02/Task02-CSP-Adjustments.md>).

Reason for creation: Represent application and adaptation of predefined Turing-machine variants.

Documented development: Task05 creates C09.01 while preserving C09. Task203 retains C09 and documents optional analytical/constructive activation. TASK25.03 uses conditional analytical activation.

| Cycle / task | Record | How the competency is used | Activation: role / mode / constraint | Evidence |
| --- | --- | --- | --- | --- |
| cycle-01 / Task02 | created | Application of a suitable Turing-machine variant | not specified / not specified / not specified | [report](<cycle-01/en/Task02/Task02-CSP-Adjustments.md>) |
| cycle-01 / Task05 | historical; excluded from current totals | Task05 formalized C09.01 as an additive specialization of C09. | not specified / not specified / not specified | [report](<cycle-01/en/Task05/TASK05-CSP-Adjustments.md>) |
| cycle-02 / Task203 | reused | Optional variant use; analytical by default and constructive when implemented | extension / analytical|constructive / optional | [report](<cycle-02/en/Task203/TASK203-CSP-Adjustments.md>) |
| cycle-03 / TASK25.03 | reused | Evaluate variants; application evidence depends on actually adopting and using a variant. | extension / analytical / conditional | [report](<cycle-03/en/TASK25.03 - TrafficControl/TASK25.03-CSP-Report.md>) |

Lifecycle records: [cycle-01 events E029, E030, E031](<cycle-01/CSP-Competency-Lifecycle.csv>); [cycle-02 events C02-E037, C02-E042, C02-E047](<cycle-02/CSP-Competency-Lifecycle.csv>); [cycle-03 events C03-E030](<cycle-03/CSP-Competency-Lifecycle.csv>).

#### Component-table snapshots

| Source / table start | Dispositions | Knowledge–skill pairs as recorded |
| --- | --- | --- |
| [Task02-CSP-Adjustments.md, line 77](<cycle-01/en/Task02/Task02-CSP-Adjustments.md>) | Inventive, Responsible, Proactive, Collaborative, Creative | Turing Machines — Apply (Use, Adapt, Implement)<br>Analytical and Critical Thinking (FPK) — Apply |
| [TASK25.03-CSP-Report.md, line 376](<cycle-03/en/TASK25.03 - TrafficControl/TASK25.03-CSP-Report.md>) | Investigative; Responsible; Proactive; Collaborative; Creative | Turing Machine Variants — Apply (Select, Adapt, Use)<br>Analytical and Critical Thinking (FPK) — Apply (Analyze, Evaluate, Decide) |

Consistency follow-up: [F06](#f06), [F11](#f11).

<a id="c09-01"></a>

### C09.01 — Apply and Coordinate Turing Machine Variants in Integrated Architectures

Origin: Task05 — cycle-01. Definition reference: [definition](<cycle-01/en/Task05/TASK05-CSP-Adjustments.md>).

Reason for creation: Represent assignment, adaptation and coordination of variants within an integrated architecture.

Documented development: Formalized in Task05 adjustments as additive specialization of C09. Later use of base C09 does not retire this specialized identity.

Relation: additive specialization of [C09](CSP-Cross-Cycle-Competency-Lifecycle.md#c09).

| Cycle / task | Record | How the competency is used | Activation: role / mode / constraint | Evidence |
| --- | --- | --- | --- | --- |
| cycle-01 / Task05 | created | Coordination and application of variants in an integrated architecture | not specified / not specified / not specified | [report](<cycle-01/en/Task05/TASK05-CSP-Adjustments.md>) |

Lifecycle records: [cycle-01 events E045](<cycle-01/CSP-Competency-Lifecycle.csv>).

#### Component-table snapshots

| Source / table start | Dispositions | Knowledge–skill pairs as recorded |
| --- | --- | --- |
| [TASK05-CSP-Adjustments.md, line 133](<cycle-01/en/Task05/TASK05-CSP-Adjustments.md>) | Inventive; Responsible; Proactive; Collaborative; Creative | Turing Machine Variants (Integrated and Coordinated Use) — Apply: Select, Adapt, Coordinate.<br>System-Level Requirements Engineering — Apply: Interpret, Align, Constrain.<br>Analytical and Critical Thinking (FPK) — Analyze: Examine, Evaluate, Justify. |

Comparison result: no contradictory origin or component-level difference identified in these displayed final/adjusted snapshots. Where there is only one complete table, this establishes a reference, not repeated independent verification.

<a id="c10"></a>

### C10 — Test Turing Machines Using Simulators

Origin: Task02 — cycle-01. Definition reference: [definition](<cycle-01/en/Task02/Task02-CSP-Adjustments.md>).

Reason for creation: Represent simulation, diagnosis and refinement of Turing-machine behavior.

Documented development: Task02 refines simulation knowledge. Task05 reuses it across modules; Task203 and TASK25.03 retain TM-specific testing.

| Cycle / task | Record | How the competency is used | Activation: role / mode / constraint | Evidence |
| --- | --- | --- | --- | --- |
| cycle-01 / Task02 | created | Simulation and validation of Turing machines in JFLAP | not specified / not specified / not specified | [report](<cycle-01/en/Task02/Task02-CSP-Adjustments.md>) |
| cycle-01 / Task05 | reused | Simulation and validation of the robot modules in JFLAP | not specified / not specified / not specified | [report](<cycle-01/en/Task05/TASK05-CSP-Adjustments.md>) |
| cycle-02 / Task203 | reused | Simulation and testing | transversal / artifact-oriented / not_specified | [report](<cycle-02/en/Task203/TASK203-CSP-Adjustments.md>) |
| cycle-03 / TASK25.03 | reused | Simulate and examine TM execution, outputs and edge cases. | supporting / artifact-oriented / mandatory | [report](<cycle-03/en/TASK25.03 - TrafficControl/TASK25.03-CSP-Report.md>) |

Lifecycle records: [cycle-01 events E032, E033, E034](<cycle-01/CSP-Competency-Lifecycle.csv>); [cycle-02 events C02-E038, C02-E043, C02-E048](<cycle-02/CSP-Competency-Lifecycle.csv>); [cycle-03 events C03-E031](<cycle-03/CSP-Competency-Lifecycle.csv>).

#### Component-table snapshots

| Source / table start | Dispositions | Knowledge–skill pairs as recorded |
| --- | --- | --- |
| [Task02-CSP-Adjustments.md, line 79](<cycle-01/en/Task02/Task02-CSP-Adjustments.md>) | Collaborative, Responsible, Proactive, Creative | Turing Machines — Apply (Simulate, Evaluate, Verify)<br>Problem Solving and Troubleshooting (FPK) — Apply (Diagnose, Debug, Refine)<br>Modeling and Simulation — Apply |
| [TASK05-CSP-Adjustments.md, line 134](<cycle-01/en/Task05/TASK05-CSP-Adjustments.md>) | Collaborative; Responsible; Proactive; Creative | Turing Machines — Apply: Simulate, Evaluate, Verify.<br>Problem Solving and Troubleshooting — Apply: Diagnose, Debug, Refine.<br>Modeling and Simulation — Apply. |
| [TASK25.03-CSP-Report.md, line 339](<cycle-03/en/TASK25.03 - TrafficControl/TASK25.03-CSP-Report.md>) | Collaborative, Responsible, Proactive, Creative | Turing Machines — Apply (Simulate, Evaluate, Verify)<br>Modeling and Simulation — Apply (Test, Interpret, Validate, Refine)<br>Problem Solving and Troubleshooting (FPK) — Apply (Diagnose, Debug, Refine) |

Consistency follow-up: [F13](#f13).

<a id="c11"></a>

### C11 — Identify Patterns in Finite State Machines

Origin: Task03 — cycle-01. Definition reference: [definition](<cycle-01/en/Task03/Task03-CSP-Adjustments.md>).

Reason for creation: Represent structural pattern identification in FSMs, including regularity, redundancy and refinement reasoning.

Documented development: Task03 renames Infer and Identify Patterns to Identify Patterns and refines components. Task201 reuses it for structural generalization and state-growth reasoning.

| Cycle / task | Record | How the competency is used | Activation: role / mode / constraint | Evidence |
| --- | --- | --- | --- | --- |
| cycle-01 / Task03 | created | Analysis of patterns in states and transitions | not specified / not specified / not specified | [report](<cycle-01/en/Task03/Task03-CSP-Adjustments.md>) |
| cycle-02 / Task201 | reused | Structural pattern analysis | not_specified / analytical / not_specified | [report](<cycle-02/en/Task201/TASK201-CSP-Adjustment.md>) |

Lifecycle records: [cycle-01 events E035, E036](<cycle-01/CSP-Competency-Lifecycle.csv>); [cycle-02 events C02-E006, C02-E012, C02-E018](<cycle-02/CSP-Competency-Lifecycle.csv>).

#### Component-table snapshots

| Source / table start | Dispositions | Knowledge–skill pairs as recorded |
| --- | --- | --- |
| [Task03-CSP-Adjustments.md, line 106](<cycle-01/en/Task03/Task03-CSP-Adjustments.md>) | Inventive, Creative, Meticulous | Finite State Machines — Analyze<br>Analytical and Critical Thinking (FPK) — Apply |

Comparison result: no contradictory origin or component-level difference identified in these displayed final/adjusted snapshots. Where there is only one complete table, this establishes a reference, not repeated independent verification.

<a id="c12"></a>

### C12 — Develop Problem-Solving Solutions Using Pushdown Automata

Origin: Task04 — cycle-01. Definition reference: [definition](<cycle-01/en/Task04/Task04-CSP-Adjustments.md>).

Reason for creation: Represent construction of a pushdown-automaton solution using stack memory for return navigation.

Documented development: Task04 refines the model and components to PDA construction. Task202 reuses C12. Its possible inclusion in TASK25.02 remains a proposal, not a current association.

| Cycle / task | Record | How the competency is used | Activation: role / mode / constraint | Evidence |
| --- | --- | --- | --- | --- |
| cycle-01 / Task04 | created | Construction of the stack-based return-navigation model | not specified / not specified / not specified | [report](<cycle-01/en/Task04/Task04-CSP-Adjustments.md>) |
| cycle-02 / Task202 | reused | PDA modeling | core / constructive / not_specified | [report](<cycle-02/en/Task202/TASK202-CSP-Adustments.md>) |

Lifecycle records: [cycle-01 events E037, E038](<cycle-01/CSP-Competency-Lifecycle.csv>); [cycle-02 events C02-E019, C02-E024, C02-E030](<cycle-02/CSP-Competency-Lifecycle.csv>).

#### Component-table snapshots

| Source / table start | Dispositions | Knowledge–skill pairs as recorded |
| --- | --- | --- |
| [Task04-CSP-Adjustments.md, line 138](<cycle-01/en/Task04/Task04-CSP-Adjustments.md>) | Inventive, Collaborative, Responsible, Proactive, Creative | Pushdown Automata — Create<br>Requirements Engineering — Apply<br>Analytical and Critical Thinking (FPK) — Apply |

Consistency follow-up: [F09](#f09), [F10](#f10).

<a id="c13"></a>

### C13 — Interpret Rule-Based Notation

Origin: Task04 — cycle-01. Definition reference: [definition](<cycle-01/en/Task04/Task04-CSP-Adjustments.md>).

Reason for creation: Represent interpretation of rule-based notation, instantiated through context-free grammars and PDA correspondence in Task04.

Documented development: Task04 records CFG/PDA components. Task202 initially reuses C13 and then creates C13.01. C13 is preserved as a base and is not an additional final Task202 target.

| Cycle / task | Record | How the competency is used | Activation: role / mode / constraint | Evidence |
| --- | --- | --- | --- | --- |
| cycle-01 / Task04 | created | Interpretation of context-free notation for navigation sequences | not specified / not specified / not specified | [report](<cycle-01/en/Task04/Task04-CSP-Adjustments.md>) |
| cycle-02 / Task202 | historical; excluded from current totals | Base preserved. Initial association is traced through C13.01 in the adjusted set; this is not deletion of C13. | not_specified / interpretative;analytical / not_specified | [report](<cycle-02/en/Task202/TASK202-CSP-Review-Report.md>) |

Lifecycle records: [cycle-01 events E039, E040](<cycle-01/CSP-Competency-Lifecycle.csv>); [cycle-02 events C02-E021, C02-E026, C02-E029](<cycle-02/CSP-Competency-Lifecycle.csv>).

#### Component-table snapshots

| Source / table start | Dispositions | Knowledge–skill pairs as recorded |
| --- | --- | --- |
| [Task04-CSP-Adjustments.md, line 139](<cycle-01/en/Task04/Task04-CSP-Adjustments.md>) | Inventive, Collaborative, Responsible, Proactive, Creative | Context-Free Grammars — Understand<br>Pushdown Automata — Understand<br>Analytical and Critical Thinking (FPK) — Apply |

Consistency follow-up: [F09](#f09).

<a id="c13-01"></a>

### C13.01 — Interpret Formal Grammar-Based Rules

Origin: Task202 — cycle-02. Definition reference: [definition](<cycle-02/en/Task202/TASK202-CSP-Adustments.md>).

Reason for creation: Make formal-grammar interpretation explicit where the generic C13 title was considered ambiguous; preserve the C13 base.

Documented development: Created in Task202 adjustments. Earlier associations in TASK25.01 and TASK25.03 give way to C23 for notation; TASK25.02 retains C13.01 for grammar interpretation.

Relation: additive specialization of [C13](CSP-Cross-Cycle-Competency-Lifecycle.md#c13).

| Cycle / task | Record | How the competency is used | Activation: role / mode / constraint | Evidence |
| --- | --- | --- | --- | --- |
| cycle-02 / Task202 | created | Interpretation of formal grammar-based rules | not_specified / interpretative;analytical / not_specified | [report](<cycle-02/en/Task202/TASK202-CSP-Adustments.md>) |
| cycle-03 / TASK25.01 | historical; excluded from current totals | Earlier grammar-rule association replaced by C23 for algebraic notation; C13.01 remains defined and is currently reused in TASK25.02. | not_specified / not_specified / not_specified | [report](<cycle-03/en/TASK25.01 - TheVendingMachine/TASK25.01-CSP-Report.md>) |
| cycle-03 / TASK25.02 | reused | Interpret productions, derivations and their relation to the PDA; distinguish grammar rules from general notation. | transversal / analytical / mandatory | [report](<cycle-03/en/TASK25.02 - TheMinotaursLabyrinth/TASK25.02-CSP-Report.md>) |
| cycle-03 / TASK25.03 | historical; excluded from current totals | Earlier grammar-rule association replaced by C23 for algebraic notation; C13.01 remains defined and is currently reused in TASK25.02. | not_specified / not_specified / not_specified | [report](<cycle-03/en/TASK25.03 - TrafficControl/TASK25.03-CSP-Report.md>) |

Lifecycle records: [cycle-02 events C02-E032](<cycle-02/CSP-Competency-Lifecycle.csv>); [cycle-03 events C03-E009, C03-E021, C03-E027](<cycle-03/CSP-Competency-Lifecycle.csv>).

#### Component-table snapshots

| Source / table start | Dispositions | Knowledge–skill pairs as recorded |
| --- | --- | --- |
| [TASK202-CSP-Adustments.md, line 119](<cycle-02/en/Task202/TASK202-CSP-Adustments.md>) | Analytical Rigor, Responsibility, Reflective, Collaborative | Context-Free Grammars — Understand<br>Pushdown Automata — Analyze<br>Formal Reasoning in Computation Theory — Analyze |
| [TASK25.02-CSP-Report.md, line 301](<cycle-03/en/TASK25.02 - TheMinotaursLabyrinth/TASK25.02-CSP-Report.md>) | Analytical; Responsible; Reflective; Collaborative | Context-Free Grammars — Understand<br>Pushdown Automata — Understand<br>Formal Reasoning in Computation Theory — Analyze |

Consistency follow-up: [F03](#f03), [F10](#f10).

<a id="c14"></a>

### C14 — Differentiate Classifications of Formal Grammars

Origin: Task04 — cycle-01. Definition reference: [definition](<cycle-01/en/Task04/Task04-CSP-Adjustments.md>).

Reason for creation: Represent comparison of regular and context-free classifications and their computational models in the retained Task04 set.

Documented development: A similarly titled proposal occurs in preliminary Task03 and is removed after review. The retained identifier C14 originates in Task04 under the registry convention. Earlier conceptual mention is not silently assigned the later identifier.

| Cycle / task | Record | How the competency is used | Activation: role / mode / constraint | Evidence |
| --- | --- | --- | --- | --- |
| cycle-01 / Task04 | created | Comparison of regular and context-free formalisms | not specified / not specified / not specified | [report](<cycle-01/en/Task04/Task04-CSP-Adjustments.md>) |
| cycle-02 / Task202 | reused | Formal model justification | not_specified / analytical;justificatory / not_specified | [report](<cycle-02/en/Task202/TASK202-CSP-Adustments.md>) |
| cycle-02 / Task204 | reused | Formal grammar classification | extension / analytical / optional | [report](<cycle-02/en/Task204/TASK204-CSP-Adjustments.md>) |
| cycle-03 / TASK25.00 | reused | Compare regular and context-free classifications in the optional extension. | extension / analytical / optional | [report](<cycle-03/en/TASK25.00 - MusicCollection/Task25.00-CSP-Report.md>) |
| cycle-03 / TASK25.02 | reused | Compare language classes and justify expressive-power distinctions. | supporting / analytical / mandatory | [report](<cycle-03/en/TASK25.02 - TheMinotaursLabyrinth/TASK25.02-CSP-Report.md>) |
| cycle-03 / TASK25.05 | reused | Optionally connect formal language classes to the analysis; C21 carries complexity classification. | extension / analytical / optional | [report](<cycle-03/en/TASK25.05 - OnlineJudges/TASK25.05-CSP-Report.md>) |

Lifecycle records: [cycle-01 events E041, E042](<cycle-01/CSP-Competency-Lifecycle.csv>); [cycle-02 events C02-E023, C02-E028, C02-E034, C02-E053, C02-E060, C02-E067](<cycle-02/CSP-Competency-Lifecycle.csv>); [cycle-03 events C03-E003, C03-E022, C03-E040](<cycle-03/CSP-Competency-Lifecycle.csv>).

#### Component-table snapshots

| Source / table start | Dispositions | Knowledge–skill pairs as recorded |
| --- | --- | --- |
| [Task04-CSP-Adjustments.md, line 140](<cycle-01/en/Task04/Task04-CSP-Adjustments.md>) | Inventive, Collaborative, Responsible, Proactive | Regular Languages — Understand<br>Context-Free Languages — Understand<br>Analytical and Critical Thinking (FPK) — Apply |
| [Task25.00-CSP-Report.md, line 240](<cycle-03/en/TASK25.00 - MusicCollection/Task25.00-CSP-Report.md>) | Inventive; Collaborative; Responsible; Proactive | Regular Languages — Understand<br>Context-Free Languages — Understand<br>Analytical and Critical Thinking — Apply |
| [TASK25.02-CSP-Report.md, line 229](<cycle-03/en/TASK25.02 - TheMinotaursLabyrinth/TASK25.02-CSP-Report.md>) | Inventive; Collaborative; Responsible; Proactive | Regular Languages — Understand<br>Context-Free Languages — Understand<br>Analytical and Critical Thinking — Apply |
| [TASK25.05-CSP-Report.md, line 329](<cycle-03/en/TASK25.05 - OnlineJudges/TASK25.05-CSP-Report.md>) | Inventive; Collaborative; Responsible; Proactive | Regular Languages — Understand<br>Context-Free Languages — Understand<br>Analytical and Critical Thinking — Apply |

Consistency follow-up: [F09](#f09), [F11](#f11), [F12](#f12).

<a id="c15"></a>

### C15 — Understand the Halting Problem and its Implications

Origin: Task204 — cycle-02. Definition reference: [definition](<cycle-02/en/Task204/TASK204-CSP-Adjustments.md>).

Reason for creation: Represent conceptual explanation of the Halting Problem and general limits of automated program analysis.

Documented development: Introduced in Task204 report, then reviewed and refined in its adjustments. Reused as core theoretical reasoning in TASK25.05.

| Cycle / task | Record | How the competency is used | Activation: role / mode / constraint | Evidence |
| --- | --- | --- | --- | --- |
| cycle-02 / Task204 | created | Explanation of the Halting Problem | core / analytical;justificatory / mandatory | [report](<cycle-02/en/Task204/TASK204-CSP-Adjustments.md>) |
| cycle-03 / TASK25.05 | reused | Explain the Halting Problem and limits of general termination analysis. | core / analytical;justificatory / mandatory | [report](<cycle-03/en/TASK25.05 - OnlineJudges/TASK25.05-CSP-Report.md>) |

Lifecycle records: [cycle-02 events C02-E055, C02-E062, C02-E069](<cycle-02/CSP-Competency-Lifecycle.csv>); [cycle-03 events C03-E041](<cycle-03/CSP-Competency-Lifecycle.csv>).

#### Component-table snapshots

| Source / table start | Dispositions | Knowledge–skill pairs as recorded |
| --- | --- | --- |
| [TASK204-CSP-Adjustments.md, line 152](<cycle-02/en/Task204/TASK204-CSP-Adjustments.md>) | Collaboration, Responsibility, Proactivity, Creativity | Halting Problem — Understand (Describe, Explain, Justify)<br>Computability — Understand (Classify, Recognize, Explain)<br>Turing Machines — Understand (Explain, Relate)<br>Analytical and Critical Thinking — Apply (Evaluate, Structure, Argue) |
| [TASK25.05-CSP-Report.md, line 148](<cycle-03/en/TASK25.05 - OnlineJudges/TASK25.05-CSP-Report.md>) | Collaboration, Responsibility, Proactivity, Creativity | Halting Problem — Understand (Describe, Explain, Justify)<br>Computability — Understand (Classify, Recognize, Explain)<br>Turing Machines — Understand (Explain, Relate)<br>Analytical and Critical Thinking — Apply (Evaluate, Structure, Argue) |

Consistency follow-up: [F08](#f08).

<a id="c16"></a>

### C16 — Interpret Turing Machine Concepts to Analyze Computational System Capabilities

Origin: Task204 — cycle-02. Definition reference: [definition](<cycle-02/en/Task204/TASK204-CSP-Adjustments.md>).

Reason for creation: Represent conceptual interpretation of Turing-machine capabilities separately from machine construction and the central Halting Problem explanation.

Documented development: Introduced in Task204 with Apply in its title; adjustments adopt Interpret and refine components. Possible incorporation into C15 is prospective and is not implemented.

| Cycle / task | Record | How the competency is used | Activation: role / mode / constraint | Evidence |
| --- | --- | --- | --- | --- |
| cycle-02 / Task204 | created | Interpretative support; no independent minimum-task evidence | supporting|extension / interpretative / optional|conditional | [report](<cycle-02/en/Task204/TASK204-CSP-Adjustments.md>) |
| cycle-03 / TASK25.03 | reused | Interpret computability and TM capabilities to support model-suitability arguments. | supporting / analytical / mandatory | [report](<cycle-03/en/TASK25.03 - TrafficControl/TASK25.03-CSP-Report.md>) |
| cycle-03 / TASK25.05 | reused | Use TM and computability concepts to interpret system capabilities when activated. | supporting / interpretative / conditional | [report](<cycle-03/en/TASK25.05 - OnlineJudges/TASK25.05-CSP-Report.md>) |

Lifecycle records: [cycle-02 events C02-E056, C02-E063, C02-E070, C02-E071](<cycle-02/CSP-Competency-Lifecycle.csv>); [cycle-03 events C03-E032, C03-E042](<cycle-03/CSP-Competency-Lifecycle.csv>).

#### Component-table snapshots

| Source / table start | Dispositions | Knowledge–skill pairs as recorded |
| --- | --- | --- |
| [TASK204-CSP-Adjustments.md, line 282](<cycle-02/en/Task204/TASK204-CSP-Adjustments.md>) | Collaboration, Responsibility, Proactivity, Creativity | Turing Machines — Understand (Explain, Relate, Interpret)<br>Computability — Understand (Classify, Distinguish, Explain)<br>Analytical and Critical Thinking — Apply (Analyze, Structure, Justify) |
| [TASK25.03-CSP-Report.md, line 231](<cycle-03/en/TASK25.03 - TrafficControl/TASK25.03-CSP-Report.md>) | Collaborative, Responsible, Proactive, Creative | Turing Machines — Understand (Explain, Interpret)<br>Computability — Understand (Classify, Distinguish)<br>Analytical and Critical Thinking (FPK) — Apply (Analyze, Justify) |
| [TASK25.05-CSP-Report.md, line 221](<cycle-03/en/TASK25.05 - OnlineJudges/TASK25.05-CSP-Report.md>) | Collaborative, Responsible, Proactive, Creative | Turing Machines — Understand (Explain, Interpret)<br>Computability — Understand (Classify, Distinguish)<br>Analytical and Critical Thinking (FPK) — Apply (Analyze, Justify) |

Consistency follow-up: [F08](#f08), [F11](#f11), [F13](#f13).

<a id="c17"></a>

### C17 — Apply operations on formal languages

Origin: TASK25.00 — cycle-03. Definition reference: [definition](<cycle-03/en/TASK25.00 - MusicCollection/Task25.00-CSP-Report.md>).

Reason for creation: Represent operations on languages and analysis of their structural consequences independently of domain abstraction.

Documented development: Created in TASK25.00 with conceptual/algebraic scope; reused in three later tasks. Analytical activation does not replace the component-level Apply/Analyze mappings.

| Cycle / task | Record | How the competency is used | Activation: role / mode / constraint | Evidence |
| --- | --- | --- | --- | --- |
| cycle-03 / TASK25.00 | created | Apply concatenation, closure, reversal and other language operations to musical collections. | core / analytical / mandatory | [report](<cycle-03/en/TASK25.00 - MusicCollection/Task25.00-CSP-Report.md>) |
| cycle-03 / TASK25.01 | reused | Analyze valid and invalid payment and product-selection sequences using language operations. | core / analytical / mandatory | [report](<cycle-03/en/TASK25.01 - TheVendingMachine/TASK25.01-CSP-Report.md>) |
| cycle-03 / TASK25.02 | reused | Characterize valid and invalid outward-and-return route languages. | core / analytical / mandatory | [report](<cycle-03/en/TASK25.02 - TheMinotaursLabyrinth/TASK25.02-CSP-Report.md>) |
| cycle-03 / TASK25.03 | reused | Support formal sequence analysis; tape manipulation alone does not establish language-operation performance. | core / analytical / mandatory | [report](<cycle-03/en/TASK25.03 - TrafficControl/TASK25.03-CSP-Report.md>) |

Lifecycle records: [cycle-03 events C03-E004, C03-E015, C03-E023, C03-E033](<cycle-03/CSP-Competency-Lifecycle.csv>).

#### Component-table snapshots

| Source / table start | Dispositions | Knowledge–skill pairs as recorded |
| --- | --- | --- |
| [Task25.00-CSP-Report.md, line 363](<cycle-03/en/TASK25.00 - MusicCollection/Task25.00-CSP-Report.md>) | Epistemic Rigor; Intellectual Responsibility; Persistence | Language Theory — Understand<br>Operations on Formal Languages — Apply / Analyze<br>Regular Expressions (conceptual) — Apply<br>Analytical and Critical Thinking (FPK) — Analyze |
| [TASK25.01-CSP-Report.md, line 151](<cycle-03/en/TASK25.01 - TheVendingMachine/TASK25.01-CSP-Report.md>) | Epistemic Rigor; Intellectual Responsibility; Persistence | Language Theory — Understand<br>Operations on Formal Languages — Apply / Analyze<br>Regular Expressions (conceptual) — Apply<br>Analytical and Critical Thinking (FPK) — Analyze |
| [TASK25.02-CSP-Report.md, line 118](<cycle-03/en/TASK25.02 - TheMinotaursLabyrinth/TASK25.02-CSP-Report.md>) | Epistemic Rigor; Intellectual Responsibility; Persistence | Language Theory — Understand<br>Operations on Formal Languages — Apply / Analyze<br>Regular Expressions (conceptual) — Apply<br>Analytical and Critical Thinking (FPK) — Analyze |
| [TASK25.03-CSP-Report.md, line 120](<cycle-03/en/TASK25.03 - TrafficControl/TASK25.03-CSP-Report.md>) | Epistemic Rigor; Intellectual Responsibility; Persistence | Language Theory — Understand<br>Operations on Formal Languages — Apply / Analyze<br>Regular Expressions (conceptual) — Apply<br>Analytical and Critical Thinking (FPK) — Analyze |

Consistency follow-up: [F08](#f08), [F10](#f10).

<a id="c18"></a>

### C18 — Model real-world problems using formal language concepts

Origin: TASK25.00 — cycle-03. Definition reference: [definition](<cycle-03/en/TASK25.00 - MusicCollection/Task25.00-CSP-Report.md>).

Reason for creation: Represent domain abstraction through alphabets, strings and languages without conflating it with recognizer construction.

Documented development: Created in TASK25.00, not inherited from an earlier task. Reused for abstraction in three later tasks; recognizer construction remains a distinct performance.

| Cycle / task | Record | How the competency is used | Activation: role / mode / constraint | Evidence |
| --- | --- | --- | --- | --- |
| cycle-03 / TASK25.00 | created | Abstract songs and collections as alphabets, strings and languages. | core / constructive / mandatory | [report](<cycle-03/en/TASK25.00 - MusicCollection/Task25.00-CSP-Report.md>) |
| cycle-03 / TASK25.01 | reused | Abstract products, payments and interactions into symbols and languages. | core / constructive / mandatory | [report](<cycle-03/en/TASK25.01 - TheVendingMachine/TASK25.01-CSP-Report.md>) |
| cycle-03 / TASK25.02 | reused | Abstract positions, movements and routes as formal symbols and languages. | core / constructive / mandatory | [report](<cycle-03/en/TASK25.02 - TheMinotaursLabyrinth/TASK25.02-CSP-Report.md>) |
| cycle-03 / TASK25.03 | reused | Abstract sensor readings and vehicle categories as symbols and formal inputs. | core / constructive / mandatory | [report](<cycle-03/en/TASK25.03 - TrafficControl/TASK25.03-CSP-Report.md>) |

Lifecycle records: [cycle-03 events C03-E005, C03-E016, C03-E024, C03-E034](<cycle-03/CSP-Competency-Lifecycle.csv>).

#### Component-table snapshots

| Source / table start | Dispositions | Knowledge–skill pairs as recorded |
| --- | --- | --- |
| [Task25.00-CSP-Report.md, line 432](<cycle-03/en/TASK25.00 - MusicCollection/Task25.00-CSP-Report.md>) | Epistemic Rigor; Intellectual Responsibility; Reflectiveness | Language Theory — Understand<br>Formal Languages — Apply<br>Homomorphisms and Codifications (conceptual) — Apply<br>Analytical and Critical Thinking (FPK) — Analyze |
| [TASK25.01-CSP-Report.md, line 189](<cycle-03/en/TASK25.01 - TheVendingMachine/TASK25.01-CSP-Report.md>) | Epistemic Rigor; Intellectual Responsibility; Reflectiveness | Language Theory — Understand<br>Formal Languages — Apply<br>Homomorphisms and Codifications (conceptual) — Apply<br>Analytical and Critical Thinking (FPK) — Analyze |
| [TASK25.02-CSP-Report.md, line 156](<cycle-03/en/TASK25.02 - TheMinotaursLabyrinth/TASK25.02-CSP-Report.md>) | Epistemic Rigor; Intellectual Responsibility; Reflectiveness | Language Theory — Understand<br>Formal Languages — Apply<br>Homomorphisms and Codifications (conceptual) — Apply<br>Analytical and Critical Thinking (FPK) — Analyze |
| [TASK25.03-CSP-Report.md, line 158](<cycle-03/en/TASK25.03 - TrafficControl/TASK25.03-CSP-Report.md>) | Epistemic Rigor; Intellectual Responsibility; Reflectiveness | Language Theory — Understand<br>Formal Languages — Apply<br>Homomorphisms and Codifications (conceptual) — Apply<br>Analytical and Critical Thinking (FPK) — Analyze |

Consistency follow-up: [F08](#f08), [F10](#f10).

<a id="c19"></a>

### C19 — Apply homomorphisms in formal languages

Origin: TASK25.00 — cycle-03. Definition reference: [definition](<cycle-03/en/TASK25.00 - MusicCollection/Task25.00-CSP-Report.md>).

Reason for creation: Represent homomorphisms, codifications, preserved properties and limits of representation equivalence.

Documented development: Created in TASK25.00. TASK25.02 retains conditional reuse for explicit homomorphisms; assigning symbols alone does not establish this performance.

| Cycle / task | Record | How the competency is used | Activation: role / mode / constraint | Evidence |
| --- | --- | --- | --- | --- |
| cycle-03 / TASK25.00 | created | Analyze score/recording codifications, homomorphisms and limits of equivalence. | supporting / interpretative / mandatory | [report](<cycle-03/en/TASK25.00 - MusicCollection/Task25.00-CSP-Report.md>) |
| cycle-03 / TASK25.02 | reused | Analyze explicit homomorphisms or representation transformations when the solution uses them. | supporting / analytical / conditional | [report](<cycle-03/en/TASK25.02 - TheMinotaursLabyrinth/TASK25.02-CSP-Report.md>) |

Lifecycle records: [cycle-03 events C03-E006, C03-E025](<cycle-03/CSP-Competency-Lifecycle.csv>).

#### Component-table snapshots

| Source / table start | Dispositions | Knowledge–skill pairs as recorded |
| --- | --- | --- |
| [Task25.00-CSP-Report.md, line 500](<cycle-03/en/TASK25.00 - MusicCollection/Task25.00-CSP-Report.md>) | Epistemic Rigor; Intellectual Responsibility; Reflectiveness | Formal Languages — Understand<br>Homomorphisms — Apply<br>Codifications — Apply<br>Analytical and Critical Thinking (FPK) — Analyze |
| [TASK25.02-CSP-Report.md, line 408](<cycle-03/en/TASK25.02 - TheMinotaursLabyrinth/TASK25.02-CSP-Report.md>) | Epistemic Rigor; Intellectual Responsibility; Reflectiveness | Formal Languages — Understand<br>Homomorphisms — Apply<br>Codifications — Apply<br>Analytical and Critical Thinking (FPK) — Analyze |

Consistency follow-up: [F08](#f08).

<a id="c20"></a>

### C20 — Model and analyze musical collections as formal languages

Origin: TASK25.00 — cycle-03. Definition reference: [definition](<cycle-03/en/TASK25.00 - MusicCollection/Task25.00-CSP-Report.md>).

Reason for creation: Represent the coherent integration of six competencies in the Music Collection task while retaining component identities.

Documented development: Created in TASK25.00 as the composite of C18, C17, C19, C04, C23 and C05.01. Other tasks do not reuse this music-specific composite.

Components: [C18](CSP-Cross-Cycle-Competency-Lifecycle.md#c18), [C17](CSP-Cross-Cycle-Competency-Lifecycle.md#c17), [C19](CSP-Cross-Cycle-Competency-Lifecycle.md#c19), [C04](CSP-Cross-Cycle-Competency-Lifecycle.md#c04), [C23](CSP-Cross-Cycle-Competency-Lifecycle.md#c23), [C05.01](CSP-Cross-Cycle-Competency-Lifecycle.md#c05-01).

| Cycle / task | Record | How the competency is used | Activation: role / mode / constraint | Evidence |
| --- | --- | --- | --- | --- |
| cycle-03 / TASK25.00 | created | Integrate modeling, operations, transformations, notation and justification across the full music response. | core / integrative / mandatory | [report](<cycle-03/en/TASK25.00 - MusicCollection/Task25.00-CSP-Report.md>) |

Lifecycle records: [cycle-03 events C03-E007](<cycle-03/CSP-Competency-Lifecycle.csv>).

#### Component-table snapshots

| Source / table start | Dispositions | Knowledge–skill pairs as recorded |
| --- | --- | --- |
| [Task25.00-CSP-Report.md, line 573](<cycle-03/en/TASK25.00 - MusicCollection/Task25.00-CSP-Report.md>) | Epistemic Rigor; Intellectual Responsibility; Reflectiveness; Persistence | Language Theory — Understand<br>Formal Languages — Apply<br>Regular Expressions — Apply<br>Homomorphisms and Codifications — Apply<br>Analytical and Critical Thinking (FPK) — Analyze<br>Technical Written Communication (FPK) — Create |

Consistency follow-up: [F08](#f08).

<a id="c21"></a>

### C21 — Analyze Computational Complexity and the Implications of NP-Hardness

Origin: TASK25.05 — cycle-03. Definition reference: [definition](<cycle-03/en/TASK25.05 - OnlineJudges/TASK25.05-CSP-Report.md>).

Reason for creation: Represent complexity, scalability and implications of NP-hardness for execution limits and feasibility in TASK25.05.

Documented development: Created in TASK25.05 in 2025. The current report and Cycle 3 records agree; catalog chronology conflicts and is not used to change origin.

| Cycle / task | Record | How the competency is used | Activation: role / mode / constraint | Evidence |
| --- | --- | --- | --- | --- |
| cycle-03 / TASK25.05 | created | Analyze TSP/timetabling complexity, scalability and execution limits when explaining TLE. | core / analytical / mandatory | [report](<cycle-03/en/TASK25.05 - OnlineJudges/TASK25.05-CSP-Report.md>) |

Lifecycle records: [cycle-03 events C03-E043](<cycle-03/CSP-Competency-Lifecycle.csv>).

#### Component-table snapshots

| Source / table start | Dispositions | Knowledge–skill pairs as recorded |
| --- | --- | --- |
| [TASK25.05-CSP-Report.md, line 110](<cycle-03/en/TASK25.05 - OnlineJudges/TASK25.05-CSP-Report.md>) | Collaborative, Responsible, Proactive, Creative | Computational Complexity — Analyze (Decompose, Relate, Interpret)<br>Complexity Classes and Intractability (P, NP, NP-hard, NP-complete) — Understand (Explain, Distinguish, Justify)<br>Algorithmic Scalability (Conceptual Perspective) — Understand (Relate, Interpret, Explain)<br>Analytical and Critical Thinking (FPK) — Analyze (Evaluate, Structure, Argue) |

Consistency follow-up: [F08](#f08).

<a id="c22"></a>

### C22 — Define Context-Free Grammars for Pushdown Automata

Origin: TASK25.02 — cycle-03. Definition reference: [definition](<cycle-03/en/TASK25.02 - TheMinotaursLabyrinth/TASK25.02-CSP-Report.md>).

Reason for creation: Represent construction of a context-free grammar corresponding to a PDA, separately from interpreting existing grammar rules.

Documented development: Created in TASK25.02 as an independent competency for PDA–CFG representation. It is not recorded as a specialization of C13.01.

| Cycle / task | Record | How the competency is used | Activation: role / mode / constraint | Evidence |
| --- | --- | --- | --- | --- |
| cycle-03 / TASK25.02 | created | Construct a CFG corresponding to the PDA and explain their relationship. | supporting / constructive / mandatory | [report](<cycle-03/en/TASK25.02 - TheMinotaursLabyrinth/TASK25.02-CSP-Report.md>) |

Lifecycle records: [cycle-03 events C03-E026](<cycle-03/CSP-Competency-Lifecycle.csv>).

#### Component-table snapshots

| Source / table start | Dispositions | Knowledge–skill pairs as recorded |
| --- | --- | --- |
| [TASK25.02-CSP-Report.md, line 265](<cycle-03/en/TASK25.02 - TheMinotaursLabyrinth/TASK25.02-CSP-Report.md>) | Investigative; Meticulous; Responsible; Proactive | Pushdown Automata — Analyze (Identify, Analyze, Abstract)<br>Context-Free Grammars — Apply (Construct, Express, Translate)<br>Analytical and Critical Thinking (FPK) — Apply (Reason, Validate, Justify) |

Consistency follow-up: [F10](#f10).

<a id="c23"></a>

### C23 — Interpret and apply algebraic notation for strings and languages

Origin: TASK25.00 — cycle-03. Definition reference: [definition](<cycle-03/en/TASK25.00 - MusicCollection/Task25.00-CSP-Report.md>).

Reason for creation: Represent algebraic notation for strings and languages as an independent scope, distinct from grammar-rule interpretation.

Documented development: Created in TASK25.00 independently of C13/C13.01. It replaces task associations for algebraic notation in TASK25.01 and TASK25.03, without deleting the grammar identities.

| Cycle / task | Record | How the competency is used | Activation: role / mode / constraint | Evidence |
| --- | --- | --- | --- | --- |
| cycle-03 / TASK25.00 | created | Interpret and apply algebraic notation consistently in formal answers. | transversal / analytical / mandatory | [report](<cycle-03/en/TASK25.00 - MusicCollection/Task25.00-CSP-Report.md>) |
| cycle-03 / TASK25.01 | reused | Express strings, sequence sets and algebraic relationships precisely. | transversal / analytical / mandatory | [report](<cycle-03/en/TASK25.01 - TheVendingMachine/TASK25.01-CSP-Report.md>) |
| cycle-03 / TASK25.03 | reused | Use algebraic notation for inputs and sequences, distinct from grammar-rule interpretation. | transversal / analytical / mandatory | [report](<cycle-03/en/TASK25.03 - TrafficControl/TASK25.03-CSP-Report.md>) |

Lifecycle records: [cycle-03 events C03-E008, C03-E017, C03-E035](<cycle-03/CSP-Competency-Lifecycle.csv>).

#### Component-table snapshots

| Source / table start | Dispositions | Knowledge–skill pairs as recorded |
| --- | --- | --- |
| [Task25.00-CSP-Report.md, line 634](<cycle-03/en/TASK25.00 - MusicCollection/Task25.00-CSP-Report.md>) | Meticulous; Responsible | Language Theory — Understand<br>Formal Languages — Apply<br>Written Communication (FPK) — Apply<br>Analytical and Critical Thinking (FPK) — Analyze |
| [TASK25.01-CSP-Report.md, line 227](<cycle-03/en/TASK25.01 - TheVendingMachine/TASK25.01-CSP-Report.md>) | Meticulous; Responsible | Language Theory — Understand<br>Formal Languages — Apply<br>Written Communication (FPK) — Apply<br>Analytical and Critical Thinking (FPK) — Analyze |
| [TASK25.03-CSP-Report.md, line 268](<cycle-03/en/TASK25.03 - TrafficControl/TASK25.03-CSP-Report.md>) | Meticulous; Responsible | Language Theory — Understand<br>Formal Languages — Apply<br>Written Communication (FPK) — Apply<br>Analytical and Critical Thinking (FPK) — Analyze |

Comparison result: no contradictory origin or component-level difference identified in these displayed final/adjusted snapshots. Where there is only one complete table, this establishes a reference, not repeated independent verification.

## Preservation-first correction sequence

1. Correct broken reference paths and explicitly abbreviated tables, retaining historical versions.
2. Reconcile C02, C03, C04, C06, C09 and C13.01 against their task-level definitions and any documented revisions. Record whether each difference is an editorial error, contextual subset, accepted alias or revised definition.
3. Align supplementary catalog chronology and lifecycle status with task evidence. Retain C01 and all documented specializations.
4. Decide methodological proposals separately, especially direct PDA-construction coverage in TASK25.02. An unadopted recommendation must not enter the current matrix.
5. After accepted source corrections, regenerate the per-cycle datasets and these cross-cycle views. A coherent count cannot compensate for an unresolved component definition.

## Source-content manifest

The following hashes identify the inspected local source content. They are not Git commit identifiers and do not imply that historical versions were independently preserved in the public repository. Source packages include the task, initial report, review and adjustments where available; the Cycle 3 packages use integrated reports.

| Source | SHA-256 |
| --- | --- |
| [cycle-01/CSP-Competency-Lifecycle.csv](<cycle-01/CSP-Competency-Lifecycle.csv>) | `47eb0ac829c377adaf85efff4458d1f781eacc8c15a5fe16a9894a0ddc526525` |
| [cycle-01/CSP-Competency-Registry.csv](<cycle-01/CSP-Competency-Registry.csv>) | `d3bdec2636127dc39b588f75e587ad91354ba6d22733e8cbab51823fe6cbbd14` |
| [cycle-01/CSP-Competency-Task-Matrix.md](<cycle-01/CSP-Competency-Task-Matrix.md>) | `584139262e1b9ea9384a9db2f67c4a561ca43ebf2b531cef8cecb0f9465ae61d` |
| [cycle-01/CSP-Data-Dictionary.md](<cycle-01/CSP-Data-Dictionary.md>) | `63c1de32d1a402c4e8e6d855c145bb57dad32376129bbc9b61f09f2024a40998` |
| [cycle-01/CSP-Task-Competency-Mapping.csv](<cycle-01/CSP-Task-Competency-Mapping.csv>) | `824fdce2545ab63477bc84e8ec59a3fcc733aaa0fa9251cbd3c4eee08864258e` |
| [cycle-01/en/Task01/Review2/Task01-CSP-Report-v2.md](<cycle-01/en/Task01/Review2/Task01-CSP-Report-v2.md>) | `4b67967ebcf23a90d244982e89e1c40f1f5e674df82956030ad86b0ea22a63e4` |
| [cycle-01/en/Task01/Review2/Task01-CSP-Review-Report-v2.md](<cycle-01/en/Task01/Review2/Task01-CSP-Review-Report-v2.md>) | `436e006e886d2a4b00908932e3c85ab4293affc38c9ad4ed9353af2516765938` |
| [cycle-01/en/Task01/Task01-CSP-Adjustments.md](<cycle-01/en/Task01/Task01-CSP-Adjustments.md>) | `35985d5c5ca00218f47062a60042c48f8554f69a0ae4ead53f679d41da838c2a` |
| [cycle-01/en/Task01/Task01-CSP-Report.md](<cycle-01/en/Task01/Task01-CSP-Report.md>) | `cceb5dad8db321033edc54229757244281940e36dd179f787a21cf9a184259fd` |
| [cycle-01/en/Task01/Task01-CSP-Review-Report.md](<cycle-01/en/Task01/Task01-CSP-Review-Report.md>) | `4878c8cf462063fb455f3e9afd5684386e7ea4ebf2732371ba7d10c8818cfd48` |
| [cycle-01/en/Task01/Task01-TheVendingMachine.md](<cycle-01/en/Task01/Task01-TheVendingMachine.md>) | `52f2b602d9693fb71b0cf0c89fe9c1fd9e0e3b0881fa04d293498ebec7694e12` |
| [cycle-01/en/Task02/Task02-CSP-Adjustments.md](<cycle-01/en/Task02/Task02-CSP-Adjustments.md>) | `5562e6deed5f31604691281d4b87513df34e8d9defff5935b58cc7a4aa4322bf` |
| [cycle-01/en/Task02/Task02-CSP-Report.md](<cycle-01/en/Task02/Task02-CSP-Report.md>) | `5cd7ae3018627f4e2ce45200e68136cd9ca3b44e1780a653f4a691c417a798fe` |
| [cycle-01/en/Task02/Task02-CSP-Review-Report.md](<cycle-01/en/Task02/Task02-CSP-Review-Report.md>) | `8b186eb09fda61d38f9aafd3a775876977c2031f1b71ded2e6be310c8a056594` |
| [cycle-01/en/Task02/Task02-TrafficControl.md](<cycle-01/en/Task02/Task02-TrafficControl.md>) | `938ccbf9878cfefd7ca38b1ed1b34551b5dd8b07d07db75cbd1ba114e7c392eb` |
| [cycle-01/en/Task03/Task03-CSP-Adjustments.md](<cycle-01/en/Task03/Task03-CSP-Adjustments.md>) | `2a1fc9d0504b27c21878a34f80b9a825ee60d8a0b02c2b1e15b647c8f4af96f7` |
| [cycle-01/en/Task03/Task03-CSP-Report.md](<cycle-01/en/Task03/Task03-CSP-Report.md>) | `d0f2bca2e17f54d13af2feb45a5817fad8e4ebb6e735a4b1a3c9a79aa79dc384` |
| [cycle-01/en/Task03/Task03-CSP-Review-Report.md](<cycle-01/en/Task03/Task03-CSP-Review-Report.md>) | `aa619b8a0a7579390ab1ab951c7c8e34fbe430d018701bdac6ec8a9a040c373e` |
| [cycle-01/en/Task03/Task03-FarmingRobot.md](<cycle-01/en/Task03/Task03-FarmingRobot.md>) | `4e2cdab3bcaf78e28b88157cad9fe521a3787095f22bda84531c2b735440e297` |
| [cycle-01/en/Task04/Task04-CSP-Adjustments.md](<cycle-01/en/Task04/Task04-CSP-Adjustments.md>) | `802a7a7a8a64d8e19b3310be2bbfde61d62a15a1ac226c3003c48016bfb1037a` |
| [cycle-01/en/Task04/Task04-CSP-Report.md](<cycle-01/en/Task04/Task04-CSP-Report.md>) | `7a06abb22269f7e22accc1fb791e6626a93629b8ca6ce6254762dafb9381b86a` |
| [cycle-01/en/Task04/Task04-CSP-Review-Report.md](<cycle-01/en/Task04/Task04-CSP-Review-Report.md>) | `48091e2d6bd44e7557caaeae06ab2d4a8d289fef43c551a3b2f436bbdb62537e` |
| [cycle-01/en/Task04/Task04-TheReturnFarmingRobot.md](<cycle-01/en/Task04/Task04-TheReturnFarmingRobot.md>) | `b022554fab6f106edc0fc321f609342f0667f08f6e199f7c784b41637b827295` |
| [cycle-01/en/Task05/TASK05-CSP-Adjustments.md](<cycle-01/en/Task05/TASK05-CSP-Adjustments.md>) | `0075ba657930c4a9aea21b74cbe3838a0bc9584e76ef1fdfbddaaabb36572164` |
| [cycle-01/en/Task05/Task05-CSP-Report.md](<cycle-01/en/Task05/Task05-CSP-Report.md>) | `e31d164146e027c22a455ddb4d2f6293486c56d3faa64abbd1354baa937cc8ed` |
| [cycle-01/en/Task05/Task05-CSP-Review-Report.md](<cycle-01/en/Task05/Task05-CSP-Review-Report.md>) | `821562e4e936151663744b4d5710a54a19cc030d1172a0310e65072d536c47f4` |
| [cycle-01/en/Task05/Task05-TheFarmingRobotAndFeedingRobot.md](<cycle-01/en/Task05/Task05-TheFarmingRobotAndFeedingRobot.md>) | `b9bd052ffc1d759b6f22d670236b6c6fb657fe810c5d7d7420adc5be23850422` |
| [cycle-01/README.md](<cycle-01/README.md>) | `be03e26f71812b7b7d9977990748eaa035535371f31959e00481cb9c67842ab4` |
| [cycle-02/CSP-Competency-Lifecycle.csv](<cycle-02/CSP-Competency-Lifecycle.csv>) | `7e3908ff2966ea66a3461f1cbabeb2e123fa7ffce8ba34824e559e157a72fa15` |
| [cycle-02/CSP-Competency-Registry.csv](<cycle-02/CSP-Competency-Registry.csv>) | `30601b8456ee1e2a16fd0337b3205e46dc2672b712dd1095963710479608d1f4` |
| [cycle-02/CSP-Competency-Task-Matrix.md](<cycle-02/CSP-Competency-Task-Matrix.md>) | `2396dd7a9e483a36dcb9815c88f02c37cbeca157d29a9730a6aeca74260a1528` |
| [cycle-02/CSP-Data-Dictionary.md](<cycle-02/CSP-Data-Dictionary.md>) | `123065711ca74c8c239f08de3d2572c72757bca61b55b45277c5f997c41082dc` |
| [cycle-02/CSP-Task-Competency-Mapping.csv](<cycle-02/CSP-Task-Competency-Mapping.csv>) | `1adc43d24f1279414b084605fcf5312e01618f6c139f9a16ab81f8c146d8ed85` |
| [cycle-02/en/Task201/TASK201-CSP-Adjustment.md](<cycle-02/en/Task201/TASK201-CSP-Adjustment.md>) | `47e5acc1aa7b580611f5dac0d09c13f42816772fed96e80a80d0c84a72c52446` |
| [cycle-02/en/Task201/Task201-CSP-Report.md](<cycle-02/en/Task201/Task201-CSP-Report.md>) | `f03949b4279cf678202c1c3bf44d9bc85d8e66c341348085b9bcfaecf84edab1` |
| [cycle-02/en/Task201/TASK201-CSP-Review-Report.md](<cycle-02/en/Task201/TASK201-CSP-Review-Report.md>) | `ab6b7e7a3c71370cce900405afd19fe62ebd296ba322adde0ca8229c232ade5b` |
| [cycle-02/en/Task201/Task201-DroneMonitoring.md](<cycle-02/en/Task201/Task201-DroneMonitoring.md>) | `89d79bd230c2d6e3516f6979a7f4d17fa5f8d890ad61fdfc648a1b0de31d2065` |
| [cycle-02/en/Task202/TASK202-CSP-Adustments.md](<cycle-02/en/Task202/TASK202-CSP-Adustments.md>) | `95070d329aef115fe45d69ba4ee9ba8fe3b816e7662ad904be5b29a61ec260fa` |
| [cycle-02/en/Task202/Task202-CSP-Report.md](<cycle-02/en/Task202/Task202-CSP-Report.md>) | `197d5f537f24f6205b257758ba525efe6efbbc36e01f5a0b7dc73575f8ee729a` |
| [cycle-02/en/Task202/TASK202-CSP-Review-Report.md](<cycle-02/en/Task202/TASK202-CSP-Review-Report.md>) | `0c87f1d519f7ed06402a4da3345d214d0fa3ac42932df3c50d6eb5f6fff715dd` |
| [cycle-02/en/Task202/Task202-TeamControl.md](<cycle-02/en/Task202/Task202-TeamControl.md>) | `723bb21c5aea0343d67ffd3923aa81e06ec1d8efb5dc88581289169a51222dd6` |
| [cycle-02/en/Task203/TASK203-CSP-Adjustments.md](<cycle-02/en/Task203/TASK203-CSP-Adjustments.md>) | `f29329fa29a55fd53e7bc215056e91413a105f66bd7d51552cc114ab313b07d8` |
| [cycle-02/en/Task203/Task203-CSP-Report.md](<cycle-02/en/Task203/Task203-CSP-Report.md>) | `ec6e9c6172cf9e7faecb4c219a30ae5b7cdc7c43a5c199539431743395153a55` |
| [cycle-02/en/Task203/TASK203-CSP-Review-Report.md](<cycle-02/en/Task203/TASK203-CSP-Review-Report.md>) | `209d0519063a754335db506bfb6518337e309ac223a53058e9dd0debf9221f4c` |
| [cycle-02/en/Task203/Task203-ParkingControl.md](<cycle-02/en/Task203/Task203-ParkingControl.md>) | `cce2ad1272a4fac4acb3be797a8f76741de34d3714a28d7207d3a7be8f624e30` |
| [cycle-02/en/Task204/TASK204-CSP-Adjustments.md](<cycle-02/en/Task204/TASK204-CSP-Adjustments.md>) | `0ec0a8d5b43b6f8b53134cfe88ce70c6c60e6f0f5b644863c521efa69dc64972` |
| [cycle-02/en/Task204/Task204-CSP-Report.md](<cycle-02/en/Task204/Task204-CSP-Report.md>) | `614dc34b893a471ec108b8b5b7b676ada54b8eccdabaa4289674488050928dd3` |
| [cycle-02/en/Task204/TASK204-CSRP-Report.md](<cycle-02/en/Task204/TASK204-CSRP-Report.md>) | `ce8dcbad1724d35908ee28707eddc853f2c6d1aac18de3e2bec7b3b84d98ff94` |
| [cycle-02/en/Task204/Task204-OnlineJudges.md](<cycle-02/en/Task204/Task204-OnlineJudges.md>) | `5a819a32f6d940df4a5bf3370ff3c1a6b8bf5b15cc316d2dcf4c5cf2b87a0937` |
| [cycle-02/README.md](<cycle-02/README.md>) | `c0fcf2f229b3aa85ebfc12eeb00c920f4e8d66af42c6add8b9007cb55e819414` |
| [cycle-03/CSP-Competency-Lifecycle.csv](<cycle-03/CSP-Competency-Lifecycle.csv>) | `1b8119e9c24f25c76907ef17255cdda23c401451c882e4c05f963eb68ecbdf8e` |
| [cycle-03/CSP-Competency-Registry.csv](<cycle-03/CSP-Competency-Registry.csv>) | `08d1fc324e502ae2ea15c4f66a64469b6bc412baecc31a38acdb22ac4a2271e5` |
| [cycle-03/CSP-Competency-Task-Matrix.md](<cycle-03/CSP-Competency-Task-Matrix.md>) | `0504fa596f82670a5b34c575f78571020d72598b0f87b0042b0afc708f83404a` |
| [cycle-03/CSP-Data-Dictionary.md](<cycle-03/CSP-Data-Dictionary.md>) | `ab5288a6713b42c59a7c4d40b96035ce75069d4e8dfd1976d3ef085a53f930a9` |
| [cycle-03/CSP-Task-Competency-Mapping.csv](<cycle-03/CSP-Task-Competency-Mapping.csv>) | `e17d67f71b40772e7e93a752ae443a010c97c01acf390db86f1e6d2c422ad418` |
| [cycle-03/en/TASK25.00 - MusicCollection/Task25.00 - MusicCollection.md](<cycle-03/en/TASK25.00 - MusicCollection/Task25.00 - MusicCollection.md>) | `84ccc1e2a46fcb73fdb993e435e921cba5d520b96024fc1f21e980c71b7404ee` |
| [cycle-03/en/TASK25.00 - MusicCollection/Task25.00-CSP-Report.md](<cycle-03/en/TASK25.00 - MusicCollection/Task25.00-CSP-Report.md>) | `a54e8761cf1f57a0ff5c311e24efd9b350f3385546e3f7058e0d89ee17c6abb3` |
| [cycle-03/en/TASK25.01 - TheVendingMachine/TASK25.01 - TheVendingMachine.md](<cycle-03/en/TASK25.01 - TheVendingMachine/TASK25.01 - TheVendingMachine.md>) | `2adf1fd8e26adf452df655f140f8ae8b92f2a47391a4400cb212ff1e7ecdc7b8` |
| [cycle-03/en/TASK25.01 - TheVendingMachine/TASK25.01-CSP-Report.md](<cycle-03/en/TASK25.01 - TheVendingMachine/TASK25.01-CSP-Report.md>) | `f63b00f26a0a20d3a2c05c13712504d29e0cfe6f110a817c9799e3e2ab702921` |
| [cycle-03/en/TASK25.02 - TheMinotaursLabyrinth/TASK25.02 - TheMinotaursLabyrinth.md](<cycle-03/en/TASK25.02 - TheMinotaursLabyrinth/TASK25.02 - TheMinotaursLabyrinth.md>) | `b01014af986c75ad3ce54810a8c0014498669cebef68f023cc31cb8ed5f8444c` |
| [cycle-03/en/TASK25.02 - TheMinotaursLabyrinth/TASK25.02-CSP-Report.md](<cycle-03/en/TASK25.02 - TheMinotaursLabyrinth/TASK25.02-CSP-Report.md>) | `9b3b99ac2346d853faba3b1fe1e45bf73fb8804bb5b445217f67d9234440b8cb` |
| [cycle-03/en/TASK25.03 - TrafficControl/TASK25.03 - TrafficControl.md](<cycle-03/en/TASK25.03 - TrafficControl/TASK25.03 - TrafficControl.md>) | `681019bcebf71e778f758865d0acbbed09e1ce582c51bce3b80d9bc88c4b61c9` |
| [cycle-03/en/TASK25.03 - TrafficControl/TASK25.03-CSP-Report.md](<cycle-03/en/TASK25.03 - TrafficControl/TASK25.03-CSP-Report.md>) | `021c58134d2f2d37c2e2d8e16ada2ead28db39bdbedd002d4ab65bbc6f577717` |
| [cycle-03/en/TASK25.05 - OnlineJudges/TASK25.05 - OnlineJudges.md](<cycle-03/en/TASK25.05 - OnlineJudges/TASK25.05 - OnlineJudges.md>) | `5e8fb5206a721614d97d9897f244c04d39f54ea211570a0ea469064cf902be15` |
| [cycle-03/en/TASK25.05 - OnlineJudges/TASK25.05-CSP-Report.md](<cycle-03/en/TASK25.05 - OnlineJudges/TASK25.05-CSP-Report.md>) | `e418eddab767e9f1280977cb1de8215344bbd400d4ed58b3bdca5dc47e11e365` |
| [cycle-03/README.md](<cycle-03/README.md>) | `6dc8e49d48e97833a63c468627c694aae246234313f88c791b133697c7b03830` |
| [../../Catálogo/C01_LifeCycle.md](<../../Catálogo/C01_LifeCycle.md>) | `ffd81fb2a04d2fb5674590f13606174e7e9efa8752d9ec9015057e33803aa962` |
| [../../Catálogo/C15_LifeCycle.md](<../../Catálogo/C15_LifeCycle.md>) | `8f11563caa1ffb086e2bbdc8c4acde1f21180be7026fd075ad6dfd726fa49d99` |
| [../../Catálogo/C16_LifeCycle.md](<../../Catálogo/C16_LifeCycle.md>) | `23bcd1c1f69c9eb7a0ce4efe72a1093a7bc4bc1b2ac53c4358e98a3ee23fee75` |
| [../../Catálogo/C17_LifeCycle.md](<../../Catálogo/C17_LifeCycle.md>) | `4e86be596b858ecd3ee7745b48b8925c861ece1757514dfbf4eedc7f811584b6` |
| [../../Catálogo/C18_LifeCycle.md](<../../Catálogo/C18_LifeCycle.md>) | `d520d94036abd77cf5e905a7e3c89e1d26115be4c661068771fa9415cd8490de` |
| [../../Catálogo/C19_LifeCycle.md](<../../Catálogo/C19_LifeCycle.md>) | `ab64d9eab3d8639210698725e69384fd05415393c75e121a65d526d0768b2074` |
| [../../Catálogo/C20_LifeCycle.md](<../../Catálogo/C20_LifeCycle.md>) | `5c4d9662c6c4c99425ae01860e69ac4f249c23a4442cbbdab7cf28e3e8ed5336` |
| [../../Catálogo/C21_LifeCycle.md](<../../Catálogo/C21_LifeCycle.md>) | `9fcdc268690f6a172199229f41e8ce6171fafc71cf2225dd91444b03e8030027` |
