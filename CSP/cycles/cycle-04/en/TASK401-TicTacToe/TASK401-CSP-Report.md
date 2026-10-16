# TASK401 - CSP Report

## 1. Context and specification scope

**Task:** Tic-Tac-Toe implementation, 3 × 3 board, two human players.  
**Educational setting:** first year of the Integrated Technical Program in Informatics, IFBA, Valença Campus.  
**Course:** Algorithms and Programming Logic, Eduardo Cambruzzi, 2026.
**CSP cycle:** 04.  

This report specifies reusable competencies and their situated activation in TASK401. Knowledge is organized primarily at the level used by the course plan: data types, expressions, decision structures, repetition structures, data structures, functions and software testing. Indexing, Boolean operations and function returns are explained within these topics rather than assigned separate knowledge identities. Competencies describe coherent performances that mobilize those curricular topics.

CM01-CM10 are proposed as new competency identities for Cycle 4, within the High School Algorithms and Programming Logic context. This cycle does not reuse competency identities from the previous cycles. Their general definitions support potential reuse in other tasks of this new catalog.

### Task requirements

Groups of two or three learners implement a text-based or graphical game. The program represents the board, alternates X/O turns, rejects malformed or illegal moves, recognizes row, column and diagonal wins, recognizes draws, and displays the current board after each accepted move. The artifact must be complete, logically consistent and robust against incorrect input.

The documented assessment includes source code, execution of a complete match, and individual oral explanation of the code, functions and execution flow. Technical correctness, justification of data and control structures, effective participation and acknowledged responsibilities are assessed.

## 2. Knowledge anchored in the course plan

The course plan is the primary knowledge reference. Its content headings and stated objectives are retained, with no separate catalog item for every operator, index operation, input check or function parameter. Task examples and assessment criteria provide the necessary operational detail.

The local K identifiers are cross-references, not new competency codes. The catalog contains **13 curricular knowledge areas**. Existing identifiers are retained; gaps correspond to knowledge areas removed from this specification.

| ID | Knowledge area | Direct course-plan anchor | TASK401 application |
|---|---|---|---|
| K01 | Algorithms: concept, properties and construction | 2. Algorithms | Relate game rules, ordered actions and termination to an implementable solution |
| K03 | Data types, constants and variables | 4. Fundamentals | Represent symbols, positions, current player and game status |
| K04 | Arithmetic and literal expressions | 4. Fundamentals | Compute positions where needed and express textual values |
| K05 | Assignment statements | 4. Fundamentals | Initialize and update board cells and control variables |
| K06 | Input and output statements | 4. Fundamentals | Receive moves and display prompts, board and outcomes |
| K07 | Relational and logical operators | 5. Decision structures | Express bounds, occupancy and winning conditions |
| K08 | Decision structures | 5. Simple, compound and selection decisions | Accept or reject a move and choose a game outcome |
| K09 | Repetition structures | 6. Pre-test, post-test and control-variable repetition | Maintain the match loop, repeat input or traverse positions |
| K10 | Basic data structures: arrays and matrices | 7. Basic data structures | Store, access and update the board |
| K11 | Modularization: functions and parameter passing | 8. Modularization | Organize responsibilities and exchange data between functions |
| K12 | Software testing | 9. Software testing | Compare expected and observed game behavior |
| K14 | Software debugging | Objective: debug software; expected outcome: identify and repair errors | Locate and correct a failure where a diagnostic opportunity exists |
| K15 | Code comments | 4. Fundamentals | Support understanding of the implemented code when comments are used |

## 3. Learning objectives

By completing the proposed assessment, each learner should be able to:

1. Relate game rules to observable program behavior.
2. Maintain a coherent board and current-player state.
3. Implement Boolean decisions and controlled repetition.
4. Obtain input, provide intelligible output and reject invalid operations.
5. Explain function responsibilities and implement a bounded function where modularization is assessed.
6. Verify expected behavior and diagnose a presented or observed failure.
7. Trace, explain and justify the solution individually.
8. Fulfil an agreed contribution to the group work.

The technical and explanatory objectives are specified through the competencies below. Individual tracing and justification support assessment, while group participation remains a task requirement; they are not separate knowledge areas or competency identities in this report. 

## 4. Competency specifications

CM01-CM10 are anchored in the curricular areas in section 2. Each definition combines an action, an object and a quality condition. The task-specific manifestation and assessment evidence are separate from identity. Dispositions are expected orientations, not inferred personality traits. Knowledge-Bloom pairings express the operation to be assessed in this task, not a permanent level attached to a knowledge object.

### CM01 - Analyze computational requirements

**Definition:** analyze a problem's rules, inputs and constraints to identify the behavior required of a computational solution.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K01 - Algorithms | Analyze | Distinguish inputs, processing steps and expected outputs, examining their relationships with the problem's rules and constraints. |

**TASK401 manifestation:** distinguish valid and invalid moves, turn alternation and termination conditions. Explain why a winning board must be classified as a win even when all cells are occupied.

**TASK401 evidence and criterion:** a brief requirements analysis or targeted individual questioning; the learner correctly distinguishes the relevant elements and explains how their relationships determine the required behavior.

**Disposition:** investigative and meticulous. 

**Alignment:** 

BNCC General Competency 2 (GC2) supports problem formulation and analysis. Computing-Specific Competency 1 for High School (CE1) supports proposing and analyzing computational solutions. These are broad contributions rather than equivalences.

The competency has a **NarrowerThanExternalAlignment** with EM13CO02: requirements analysis contributes to refinement from specification to implementation but does not cover the complete process.

### CM02 - Maintain program data and state

**Definition:** initialize, access and update program data using an appropriate representation while preserving valid values and state consistency.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K03 - Data types, constants and variables | Apply | Represent data using appropriate types, constants and variables. |
| K05 - Assignment statements | Apply | Initialize and update variable values consistently. |
| K10 - Arrays and matrices | Apply | Store, access and update elements using valid indexes. |
| K04 - Arithmetic and literal expressions, when required | Apply | Evaluate expressions to obtain values used in data initialization or updates. |

**TASK401 manifestation:** represent the nine board cells using empty/X/O values and maintain the current player. An accepted move updates one empty cell; a rejected move preserves the board and current player.

**TASK401 evidence and criterion:** source code, execution and an individual update demonstration; the learner uses valid indexes and preserves the permitted values and expected state changes.

**Disposition:** meticulous.

**Alignment:**

BNCC General Competency 5 (GC5) supports using and creating digital technologies. Computing-Specific Competency 4 for High School (CE4) supports producing computational artifacts, while Computing-Specific Competency 1 for High School (CE1) supports constructing computational solutions. These are broad contributions rather than equivalences.

The competency has a **NarrowerThanExternalAlignment** with EM13CO02: representing and manipulating program data contributes to refinement from specification to implementation but does not cover the complete process.

### CM03 - Implement decisions with Boolean conditions

**Definition:** implement Boolean conditions and conditional branches that select actions according to specified rules.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K07 - Relational and logical operators | Apply | Construct Boolean conditions using comparisons and logical combinations. |
| K08 - Decision structures | Apply | Implement conditional branches that execute the appropriate actions according to condition results. |

**TASK401 manifestation:** determine whether a move is accepted and whether the match continues, ends in victory or ends in a draw. Identify a winning line by checking that its three cells contain the same non-empty symbol.

**TASK401 evidence and criterion:** source code and execution with cases producing true and false conditions; the implemented branches follow the game rules, empty lines are not classified as victories, and victory takes precedence over a draw.

**Disposition:** meticulous.

**Alignment:**

BNCC General Competency 2 (GC2) supports problem solving through analysis and the construction of solutions. Computing-Specific Competency 1 for High School (CE1) supports proposing and constructing computational solutions. These are broad contributions rather than equivalences.

The competency has a **NarrowerThanExternalAlignment** with EM13CO02: translating specified rules into Boolean conditions and conditional branches contributes to refinement from specification to implementation but does not cover the complete process.

### CM04 - Implement repetition with a stopping condition

**Definition:** implement repeated execution controlled by a condition or iteration limit, updating control values when required.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K09 - Repetition structures | Apply | Implement loops with appropriate continuation and stopping conditions. |
| K05 - Assignment statements, when required | Apply | Initialize and update values used to control repetition. |

**TASK401 manifestation:** maintain the match loop until victory or draw, repeat input after rejection and traverse board cells where required by the chosen algorithm.

**TASK401 evidence and criterion:** source code and an individual execution trace; repetition continues and terminates according to the game rules, and rejected input does not consume a valid turn.

**Disposition:** meticulous and persistent.

**Alignment:**

BNCC General Competency 2 (GC2) supports problem solving and solution construction. Computing-Specific Competency 1 for High School (CE1) supports proposing and analyzing computational solutions. These are broad contributions rather than equivalences.

The competency has a **NarrowerThanExternalAlignment** with EM13CO02: translating repeated behavior into executable loops contributes to refinement from specification to implementation but does not cover the complete process.

### CM05 - Implement input and output interaction

**Definition:** implement input and output operations that obtain data and communicate information clearly.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K06 - Input and output statements | Apply | Implement operations that receive data and present information. |
| K03 - Data types, constants and variables | Apply | Represent received and displayed values using appropriate data types. |

**TASK401 manifestation:** indicate the current player, receive a position, display the board and report rejection, victory or draw.

**TASK401 evidence and criterion:** source code and an interaction demonstration; prompts, received values and displayed information are consistent with the board representation and game behavior.

**Disposition:** considerate and meticulous.

**Alignment:**

BNCC General Competency 5 (GC5) supports using and creating digital technologies. Computing-Specific Competency 4 for High School (CE4) supports producing computational artifacts. These are broad contributions rather than equivalences.

The competency has a **NarrowerThanExternalAlignment** with EM13CO02: implementing specified interactions contributes to refinement from specification to implementation but does not cover the complete process.

### CM06 - Validate inputs and operation preconditions

**Definition:** check inputs and operation preconditions, rejecting invalid values or actions before they cause an invalid state change.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K03 - Data types, constants and variables | Apply | Check whether input values are compatible with the required data types. |
| K07 - Relational and logical operators | Apply | Express conditions that determine whether values and operations are permitted. |
| K08 - Decision structures | Apply | Implement branches that accept or reject values and operations according to specified constraints. |
| K10 - Arrays and matrices, when used | Apply | Check index validity before accessing or updating elements. |

**TASK401 manifestation:** reject malformed input, out-of-range positions and occupied cells without overwriting a mark or switching the player. A graphical interface may prevent invalid selection rather than parse textual input.

**TASK401 evidence and criterion:** source code and demonstrations of invalid-input rejection; rejected attempts preserve the board and current player, and validation occurs before an invalid access or update.

**Disposition:** meticulous and responsible.

**Alignment:**

BNCC General Competency 2 (GC2) supports problem solving. Computing-Specific Competency 1 for High School (CE1) supports constructing and analyzing computational solutions. These are broad contributions rather than equivalences.

The competency has a **NarrowerThanExternalAlignment** with EM13CO02: translating constraints into executable checks contributes to refinement from specification to implementation but does not cover the complete process.



### CM07 - Organize a solution into functions

**Definition:** organize a computational solution into functions with clear responsibilities and appropriate data exchange.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K11 - Modularization: functions and parameter passing | Analyze | Distinguish responsibilities and dependencies to determine function boundaries. |
| K11 - Modularization: functions and parameter passing | Apply | Define and invoke functions using appropriate parameters and return values. |
| K11 - Modularization: functions and parameter passing | Create | Design and integrate a function organization that fulfils the solution requirements. |

**TASK401 manifestation:** organize responsibilities such as board display, move validation and outcome checking into functions. No fixed function names or number are required.

**TASK401 evidence and criterion:** source code and an individual explanation or bounded modification; functions have coherent responsibilities, exchange data appropriately and integrate correctly. Create is evidenced only when the learner designs the organization rather than reproduces a supplied structure.

**Disposition:** organized and meticulous.

**Alignment:**

BNCC General Competency 2 (GC2) supports solution design, while BNCC General Competency 5 (GC5) supports digital creation. Computing-Specific Competencies 1 and 4 for High School (CE1 and CE4) support constructing solutions and producing computational artifacts. These are broad contributions rather than equivalences.

The competency has a **NarrowerThanExternalAlignment** with EM13CO02: translating responsibilities into integrated functions contributes to refinement from specification to implementation but does not cover the complete process.

### CM08 - Verify program behavior with test cases

**Definition:** use test cases to compare observed and expected behavior and judge conformity to specified requirements.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K12 - Software testing | Apply | Execute representative test cases with specified inputs and expected results. |
| K12 - Software testing | Evaluate | Judge conformity to requirements by comparing observed and expected results. |

**TASK401 manifestation:** verify legal moves, invalid-input rejection, turn alternation, victory and draw.

**TASK401 evidence and criterion:** a concise test record containing cases, expected results, observed results and conclusions; the learner identifies conformity or discrepancies and acknowledges the limits of the cases examined.

**Disposition:** meticulous and persistent.

**Alignment:**

BNCC General Competency 2 (GC2) supports systematic investigation and checking. Computing-Specific Competency 1 for High School (CE1) supports analyzing computational solutions. These are broad contributions rather than equivalences.

The competency has a **PartialAlignment** with EM13CO06 when correctness is evaluated using explicit criteria and associated measures, such as the number of successful cases for each requirement. This does not establish evaluation of other software quality characteristics.

It also has a **PartialAlignment** with EM13CO02 because testing supports checking refinements, although verification alone does not establish the complete construction process.

### CM09 - Diagnose a program failure

**Definition:** identify the cause of a program failure by relating execution behavior to the expected result.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K14 - Software debugging | Analyze | Identify the statement, condition or data manipulation responsible for an observed failure. |
| K12 - Software testing, when a correction is performed | Apply | Repeat relevant test cases to check the correction. |

**TASK401 manifestation:** diagnose an overwritten cell, premature draw or incorrect player change.

**TASK401 evidence and criterion:** an observed or instructor-provided failure, an explanation of the relevant execution steps and a causal explanation; the learner identifies why the failure occurs rather than merely describes the incorrect output. Correction and retesting provide additional evidence but are not required to establish diagnosis itself.

**Disposition:** investigative and persistent.

**Alignment:**

BNCC General Competency 2 (GC2) supports investigating causes. Computing-Specific Competency 1 for High School (CE1) supports analyzing computational solutions. These are broad contributions rather than equivalences.

The competency has a **PartialAlignment** with EM13CO02: diagnosis informs solution refinement but does not itself establish the complete refinement process.

A **PartialAlignment** with EM13CO06 is applicable when diagnosis contributes to an explicit evaluation of software correctness, rather than merely locating an error.


### CM10 - Explain a computational solution

**Definition:** explain the purpose, behavior and organization of a computational solution accurately and clearly.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K01 - Algorithms | Understand | Explain the purpose and sequence of actions of an algorithm. |
| K03 - Data types, constants and variables | Understand | Explain how data is represented and organized. |
| K10 - Arrays and matrices | Understand | Explain how data is represented and organized. |
| K08 - Decision structures | Understand | Explain how decisions determine program behavior. |
| K09 - Repetition structures | Understand | Explain how repetition determines program behavior. |
| K11 - Modularization: functions and parameter passing | Understand | Explain function responsibilities and data exchange. |
| K15 - Code comments, when used | Understand | Interpret comments in relation to the code they describe. |

**TASK401 manifestation:** explain individually how the board is represented, moves are processed and the match is controlled.

**TASK401 evidence and criterion:** answers to targeted questions using the implemented code; the explanation is technically accurate, coherent and understandable. Oral explanation is the instrument used here, not a restriction on the reusable competency.

**Disposition:** communicative and responsible.

**Alignment:**

BNCC General Competency 4 (GC4) supports communication through different languages. Computing-Specific Competency 6 for High School (CE6) supports expressing and sharing computational solutions. These are broad contributions rather than equivalences.

The competency has a **PartialAlignment** with EM13CO19 when code and program execution are used as digital presentation resources. Explanation addresses presentation of the product but does not establish negotiation or the full scope of media and digital tools.

## 5. Competency activation and evidence

The table describes the opportunities provided by TASK401. Evidence must be attributed to each learner: a correct group artifact does not demonstrate that every participant can implement or explain all its parts.

| Code | Activation constraint | Activation mode | Activation role | Condition or requirement | Main evidence |
|---|---|---|---|---|---|
| CM01 | conditional | analytical | supporting | An explicit requirements-analysis question or activity is provided | Relationship between rules, inputs and expected behavior |
| CM02 | mandatory | constructive | core | Data representation and updates are required | Code, execution and an individual data-update demonstration |
| CM03 | mandatory | constructive | core | Decisions are required by the game rules | Conditions and branches exercised with contrasting cases |
| CM04 | mandatory | constructive | core | Repeated execution and termination are required | Loop execution, continuation and termination |
| CM05 | mandatory | constructive | core | User interaction is required | Input/output demonstration and corresponding code |
| CM06 | mandatory | constructive | core | Invalid-input and illegal-move rejection are required | Rejection cases and preservation of valid state |
| CM07 | conditional | analytical;constructive | core | Function organization is explicitly required in the implementation | Function responsibilities, data exchange and integration |
| CM08 | conditional | operational;evaluative | core | Explicit verification against expected results is requested | Test cases, expected and observed results, and a conclusion |
| CM09 | conditional | analytical | supporting | A failure occurs during development or is provided for diagnosis | Relevant execution steps and causal explanation |
| CM10 | mandatory | explanatory | core | Individual explanation is required | Accurate explanation of the implemented solution |

**Activation constraint:** `mandatory` means required by the documented task; `conditional` means dependent on the stated activity, implementation requirement or diagnostic opportunity. No optional competency association is specified in this table.

**Activation mode:** describes how the competency is mobilized: analytical, constructive, operational, evaluative or explanatory. Semicolons indicate concurrent modes.

**Activation role:** `core` means directly contributing to the implementation, its verification or the required individual explanation; `supporting` means assisting analysis or diagnosis.

These fields describe task-level activation, not demonstrated individual mastery. For CM01, CM07 and CM08, the conditions make explicit performances that the baseline task does not require with sufficient precision. A complete match alone does not establish systematic verification in CM08. If the conditions are formally added to the task requirements, the corresponding constraints can be updated to `mandatory`.


Execution tracing is used as an assessment technique within debugging, explanation and loop verification; it is not a separate knowledge area in this version.

For CM07, Create is evidenced only when the learner designs the function organization. For CM09, correction and retesting are additional evidence when performed. If no diagnostic opportunity is provided, CM09 remains unassessed.

### Practical verification

| Case | Expected behavior |
|---|---|
| Legal move | One empty cell is updated and the player changes |
| Invalid input or occupied cell | The attempt is rejected without changing the board or player |
| Winning line | The correct winner is reported and the match ends |
| Full board without a win | A draw is reported and the match ends |
| Winning move fills the last cell | Victory takes precedence over a draw |

Tests should cover rows, columns and both diagonals. At least one complete match demonstrates integrated behavior. Individual questions check understanding of data, decisions, repetition and functions. A brief test record or a prepared faulty excerpt is an assessment addition and must be communicated before use.

## 6. Consolidated BNCC alignment

**GC** identifies a BNCC General Competency for Basic Education. **CE** identifies a Computing-Specific Competency for High School. These abbreviations are local references; **EM13COxx** are the official skill codes. Alignment indicates a justified contribution, not complete equivalence or demonstrated mastery of the external reference.

### Framework references

| Reference | Relevant scope |
|---|---|
| GC2 - BNCC General Competency 2 | Investigation, analysis and problem solving |
| GC4 - BNCC General Competency 4 | Communication through different languages |
| GC5 - BNCC General Competency 5 | Understanding, using and creating digital technologies |
| CE1 - Computing-Specific Competency 1 for High School | Proposing and analyzing computational solutions, considering their possibilities and limits |
| CE4 - Computing-Specific Competency 4 for High School | Producing computational artifacts with creative, ethical and legal responsibility |
| CE6 - Computing-Specific Competency 6 for High School | Expressing and sharing computational ideas and solutions |

The framework contributions above are **GeneralFrameworkAlignment** relationships. Each competency's justification is stated in section 4. The task addresses selected aspects of these broad references, not their full scope.

### Competency mapping

| Code | Competency | General BNCC | Computing-specific | Skill alignment |
|---|---|---|---|---|
| CM01 | Analyze computational requirements | GC2 | CE1 | EM13CO02: narrower |
| CM02 | Maintain program data and state | GC5 | CE1, CE4 | EM13CO02: narrower |
| CM03 | Implement decisions with Boolean conditions | GC2 | CE1 | EM13CO02: narrower |
| CM04 | Implement repetition with a stopping condition | GC2 | CE1 | EM13CO02: narrower |
| CM05 | Implement input and output interaction | GC5 | CE4 | EM13CO02: narrower |
| CM06 | Validate inputs and operation preconditions | GC2 | CE1 | EM13CO02: narrower |
| CM07 | Organize a solution into functions | GC2, GC5 | CE1, CE4 | EM13CO02: narrower |
| CM08 | Verify program behavior with test cases | GC2 | CE1 | EM13CO02 and EM13CO06: partial |
| CM09 | Diagnose a program failure | GC2 | CE1 | EM13CO02: partial; EM13CO06: conditional partial |
| CM10 | Explain a computational solution | GC4 | CE6 | EM13CO19: conditional partial |

**NarrowerThanExternalAlignment** means the competency addresses a defined part of a broader skill. 
**PartialAlignment** means the performances overlap but differ in scope. A conditional alignment applies only when its stated evidence is present.
