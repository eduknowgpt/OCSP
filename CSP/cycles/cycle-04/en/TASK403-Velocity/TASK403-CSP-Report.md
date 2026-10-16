# TASK403 - CSP Report

## 1. Context and specification scope

**Task:** A Program to Explore the Average Velocity Formula.  
**Author:** Prof. Margeylson Graça, IFBA - Valença Campus.  
**Target audience:** upper secondary learners in introductory programming.  
**Catalog scope:** programming competencies established for Cycle 4, without reuse of identities from Cycles 1-3.

The learner investigates the relationship between displacement, time interval and average velocity, documents the formula rearrangements and develops an interactive program. The program receives two positive values and an unknown marker, calculates the third quantity, validates inputs and permits repeated calculations until an exit command is entered.

The physical model is straight-line motion in the positive direction without reversal. Units are fixed and coherent; positive-only values are a task restriction. A missing-value marker is distinct from an exit command and is recognized before numeric validation.

Required deliverables are source code with comments and a brief description of the identification logic, validation rules, units and examples. Test cases remain optional. Function-based organization, arrays, execution tracing and an oral defense are not added as requirements.

## 2. Knowledge anchored in curricular topics

Existing identifiers and curricular granularity follow TASK401 and TASK402. Only two interdisciplinary knowledge areas are added; neither is misrepresented as explicit programming-course content.

| ID | Knowledge area | Reference | TASK403 application |
|---|---|---|---|
| K03 | Data types, constants and variables | Programming plan: Fundamentals | Represent known values, markers and results |
| K04 | Arithmetic and literal expressions | Programming plan: Fundamentals | Calculate the missing quantity |
| K05 | Assignment statements | Programming plan: Fundamentals | Store inputs, results and loop-control values |
| K06 | Input and output statements | Programming plan: Fundamentals | Request values and display results and units |
| K07 | Relational and logical operators | Programming plan: Decision structures | Check positivity, denominators and marker counts |
| K08 | Decision structures | Programming plan: Decision structures | Select a formula or reject invalid input |
| K09 | Repetition structures | Programming plan: Repetition structures | Repeat attempts/calculations and recognize exit |
| K12 | Software testing | Programming plan: Software testing | Compare expected and observed results when optional tests are performed |
| K17 | Physical quantities, units and average velocity | Physics content specified by TASK403 | Interpret displacement, elapsed time, average velocity and model restrictions |
| K18 | Algebraic rearrangement of formulas | Mathematics content specified by TASK403 | Isolate one quantity from the relationship |

Operator precedence, zero-denominator checks and marker handling remain details within these topics rather than separate knowledge identities. K17 and K18 are proposed additions to the shared knowledge catalog.

## 3. Learning objectives

| Objective | Bloom level | Main competency |
|---|---|---|
| Explain the physical meaning and units of the quantities within the stated model | Understand | CM22 |
| Rearrange the relationship to calculate each quantity | Apply | CM19 |
| Implement the calculations using numeric variables and expressions | Apply | CM20 |
| Select the calculation and reject invalid inputs | Apply | CM03, CM21 |
| Implement input/output and repeated calculations with termination | Apply | CM05, CM04 |

Optional verification activates CM08. CM18 is applicable only if explanation of both variable updates and arithmetic evaluation is requested; documentation of formula rearrangement alone does not establish its complete composition.

## 4. Competency specifications and explicit reuse

### Reused competencies

The following definitions and KS pairings are copied unchanged from TASK401. Only manifestations and evidence are contextualized. Conditional details already present in their catalog specifications are preserved, not used to remove a pair for this task.

### CM03 - Implement decisions with Boolean conditions

**Status:** reused from TASK401.

**Definition:** implement Boolean conditions and conditional branches that select actions according to specified rules.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K07 - Relational and logical operators | Apply | Construct Boolean conditions using comparisons and logical combinations. |
| K08 - Decision structures | Apply | Implement conditional branches that execute the appropriate actions according to condition results. |

**TASK403 manifestation and evidence:** identify the unknown quantity and select the correct calculation or error branch. Code and, where applicable, execution or test records must show that the branches implement the specified rules for each unknown and for invalid combinations.

**Disposition:** meticulous.

### CM04 - Implement repetition with a stopping condition

**Status:** reused from TASK401.

**Definition:** implement repeated execution controlled by a condition or iteration limit, updating control values when required.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K09 - Repetition structures | Apply | Implement loops with appropriate continuation and stopping conditions. |
| K05 - Assignment statements, when required | Apply | Initialize and update values used to control repetition. |

**TASK403 manifestation and evidence:** repeat attempts and calculations until the exit command is recognized. Code and, where applicable, execution or test records must show that invalid input permits another attempt; the exit command stops execution without requesting remaining values.

**Disposition:** meticulous and persistent.

### CM05 - Implement input and output interaction

**Status:** reused from TASK401.

**Definition:** implement input and output operations that obtain data and communicate information clearly.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K06 - Input and output statements | Apply | Implement operations that receive data and present information. |
| K03 - Data types, constants and variables | Apply | Represent received and displayed values using appropriate data types. |

**TASK403 manifestation and evidence:** request quantities and markers, and display the calculated quantity, value and unit. Code and, where applicable, execution or test records must show that messages explain the marker, exit command and fixed units; input and output correspond to the selected calculation.

**Disposition:** considerate and meticulous.

### CM08 - Verify program behavior with test cases

**Status:** reused from TASK401.

**Definition:** use test cases to compare observed and expected behavior and judge conformity to specified requirements.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K12 - Software testing | Apply | Execute representative test cases with specified inputs and expected results. |
| K12 - Software testing | Evaluate | Judge conformity to requirements by comparing observed and expected results. |

**TASK403 manifestation and evidence:** when optional tests are performed, verify all three calculations and invalid-input behavior. Code and, where applicable, execution or test records must show that the record compares expected and observed outcomes and supports a conclusion about correctness.

**Disposition:** meticulous and persistent.

### CM18 - Explain variable updates and arithmetic evaluation

**Status:** composite reused from TASK402; its atoms were specified in the TASK401 adjustment.

**Definition:** explain how variable updates and arithmetic expression evaluation jointly determine values during program execution.

**Fixed components:** CM17 - Explain variable updates and CM12 - Explain arithmetic expression evaluation.

| Component | Complete constitutive KS pairs |
|---|---|
| CM17 | K03 × Understand; K05 × Understand |
| CM12 | K04 × Understand |

**TASK403 manifestation and evidence:** if explicitly requested, explain how inputs are stored, used as operands and combined to obtain the result. Both atomic criteria and their relationship must be explained. Formula documentation without explanation of variable updates is insufficient.

**Disposition:** communicative and meticulous.

No definition or constitutive pair of CM18, CM17 or CM12 is changed. The task associates with the complete composite; the component links are not additional direct task associations.

### New competencies

The new codes below are proposed continuations of the current CM catalog. Their definitions and operations are independent of the TASK403 interface and example values.

### CM19 - Rearrange formulas to isolate a quantity

**Definition:** rearrange a formula through valid algebraic operations to express a selected quantity in terms of the others.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K18 - Algebraic rearrangement of formulas | Apply | Isolate a selected quantity using equivalent transformations and respecting denominator restrictions. |

**TASK403 manifestation:** derive Vₘ = Δs/Δt, Δs = VₘΔt and Δt = Δs/Vₘ from the reference relationship.

**Evidence and criterion:** written rearrangements or code comments; each expression is algebraically correct and its required nonzero denominator is respected.

**Disposition:** meticulous.

### CM20 - Implement numeric calculations

**Definition:** implement numeric calculations using suitable variable types, arithmetic expressions and assignments.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K03 - Data types, constants and variables | Apply | Represent numeric inputs and results using appropriate types and variables. |
| K04 - Arithmetic and literal expressions | Apply | Encode a calculation with appropriate operands and operator precedence. |
| K05 - Assignment statements | Apply | Assign inputs, intermediate values and results to the appropriate variables. |

**TASK403 manifestation:** implement the three rearranged calculations, preserving fractional results where relevant.

**Evidence and criterion:** source code and output examples; operands, operations and assigned results agree with the documented formulas.

**Disposition:** meticulous.

### CM21 - Validate input values and operation conditions

**Definition:** validate input values and operation conditions, rejecting invalid combinations before processing them.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K03 - Data types, constants and variables | Apply | Check input compatibility with the required types and representations. |
| K07 - Relational and logical operators | Apply | Express the conditions that make inputs and operations valid. |
| K08 - Decision structures | Apply | Accept valid combinations and reject invalid ones before performing the operation. |

**TASK403 manifestation:** recognize the marker before numeric checks, require exactly two positive numbers and one unknown, reject invalid text and prevent division by zero. The exit command is recognized separately.

**Evidence and criterion:** validation code and usage examples; invalid attempts do not trigger a calculation and receive an intelligible instruction for retrying.

**Disposition:** meticulous and responsible.

### CM22 - Interpret physical quantities and their relationships

**Definition:** explain physical quantities, their units and their relationship within a stated model of motion.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K17 - Physical quantities, units and average velocity | Understand | Explain displacement, elapsed time, average velocity, their units and the assumptions under which their relationship is used. |

**TASK403 manifestation:** explain the quantities and coherent units, and distinguish the positive-only task restriction from a universal physical rule.

**Evidence and criterion:** conceptual preparation reflected in formula documentation, comments or the brief description; quantities, units and stated assumptions are consistent. An unexplained correct numeric result alone does not establish this understanding.

**Disposition:** investigative and meticulous.

## 5. Competency activation and evidence

| Code | Constraint | Mode | Role | Condition or requirement |
|---|---|---|---|---|
| CM03 | mandatory | constructive | core | Select the calculation or rejection branch |
| CM04 | mandatory | constructive | core | Repeat attempts/calculations and terminate |
| CM05 | mandatory | constructive | core | Implement understandable interaction |
| CM08 | optional | operational;evaluative | supporting | Learner includes the optional test cases and evaluates their results |
| CM18 | conditional | explanatory | supporting | Complete explanation of updates and expression evaluation is requested |
| CM19 | mandatory | operational | core | Document all three formula rearrangements |
| CM20 | mandatory | constructive | core | Implement all three numeric calculations |
| CM21 | mandatory | constructive | core | Validate inputs and protect calculations |
| CM22 | mandatory | explanatory | supporting | Investigate the physical meaning of the relationship |

`mandatory` describes a task requirement; `optional` preserves the task's optional testing deliverable; `conditional` depends on an explicit additional request. These constraints do not establish observed learner mastery. Code, comments and the required description are the main evidence; no new oral assessment is imposed.

There are nine direct task associations: seven mandatory, one optional and one conditional. CM18's two composition links are not additional direct associations or independent achievements.

## 6. BNCC alignment and reuse rationale

GC denotes a BNCC General Competency and CE a Computing-Specific Competency for High School. These abbreviations are local; EM13COxx are official skill codes. Framework contributions are GeneralFrameworkAlignment, not equivalences.

| Competencies | Framework contribution and justification | Specific-skill relationship and limit |
|---|---|---|
| CM03, CM04, CM21 | GC2 and CE1: translate rules and constraints into executable decisions and repetition | NarrowerThanExternalAlignment with EM13CO02: individual implementation aspects contribute to refinement, not its complete scope |
| CM05, CM20 | GC5 and CE4: produce an interactive computational artifact | NarrowerThanExternalAlignment with EM13CO02: interaction and calculations realize parts of the specification |
| CM08 | GC2 and CE1: check computational behavior systematically | PartialAlignment with EM13CO06 when correctness criteria and associated measures are used; partial EM13CO02 through checking refinements |
| CM18 | GC4 and CE6: communicate relationships between updates and calculations | Conditional PartialAlignment with EM13CO19 when digital presentation resources are used; negotiation and the full media/tool scope are not established |
| CM19, CM22 | GC2: use a quantitative relationship to understand and solve a problem | No direct Computing-specific skill alignment asserted for algebra or physical understanding alone |

GC2 concerns investigation and problem solving; GC4 communication; GC5 digital culture. CE1 concerns proposing/analyzing computational solutions; CE4 artifact production; CE6 expression and sharing of computational solutions. No full physics or mathematics BNCC skill mapping is claimed.

### Explicit reuse decisions

| Decision | Competencies | Rationale |
|---|---|---|
| Direct reuse from TASK401 | CM03, CM04, CM05, CM08 | Same definitions, complete KS pairings and dispositions; only manifestations, evidence and activation are contextualized |
| Composite reuse from TASK402 | CM18 | Same fixed composition and definition, activated only under the full explanatory condition |
| Component reuse through CM18 | CM12, CM17, from TASK401 adjustment | Complete atomic pairings preserved; no extra direct task rows |
| New identities | CM19, CM20, CM21, CM22 | Algebraic transformation, numeric implementation, non-indexed validation and physical interpretation need explicit performances not fully represented by existing applicable identities |

CM02 is not reused: its constitutive array/matrix performance is not required here. CM06 is not reused by silently omitting its indexed-validation pairing; CM21 provides a separate stable composition for non-indexed validation. CM20 and CM21 are new identities with conceptual overlap, not asserted equivalents or specializations of CM02 and CM06.

CM10 is not reused because its full composition requires explanation of data structures, decisions, repetition and functions. Functions are not required in TASK403. CM11 is not selected merely because calculations are performed: independent tracing of supplied code is not a required deliverable. Existing titles are not sufficient to justify reuse when constitutive KS pairs differ.

The BNCC relationship types follow the qualified interpretations documented for TASK401 and TASK402. Sources are the TASK403 task text, the current TASK401 report and adjustment, the TASK402 report, the supplied programming course plan and the supplied BNCC Computing Complement. These are documentary specifications, not evidence of actual student attainment.