# TASK411 — CSP Report

## 1. Context and scope

**Task:** Finding the Snake in a Grid.  
**Source:** UNIVASF — Task09 — Professor B.  
**Target audience:** learners in introductory programming.

The learner must implement a program that locates a snake's head in an `M × N` character matrix and returns every snake cell in order, from head to tail. Coordinates use **`[row, column]`**, with zero-based indexing. `M` is the number of rows and `N` the number of columns.

The head is `h`; body cells contain `<`, `>`, `v` or `^`; spaces are empty cells. Every arrow points to its predecessor toward the head. To move toward the tail, the algorithm selects an edge-adjacent body cell whose arrow points to the current cell. Occupied adjacency alone does not establish a path connection. The tail has no adjacent body cell pointing to it.

Input is assumed to contain exactly one valid connected snake, one head and one tail, without branches, loops or disconnected body cells. The matrix may be supplied directly as an array. No interactive input parser or invalid-grid handling is required.

Required deliverables are source code, the coordinate sequences produced for both examples and a brief explanation of arrow-based selection and tail recognition. Additional rectangular-grid and boundary-head checks are optional. No specific search strategy, visited-cell structure or function organization is prescribed.



## 2. Knowledge mobilized

Identifiers and curricular granularity follow the previous reports. Programming topics retain the course-plan terminology used in TASK401.

| ID | Knowledge area | TASK411 application |
|---|---|---|
| K03 | Data types, constants and variables | Represent symbols, dimensions, current position and coordinate pairs |
| K04 | Arithmetic and literal expressions | Calculate neighboring positions and traversal updates |
| K05 | Assignment statements | Initialize and update position and result values |
| K06 | Input and output statements | Present the required example sequences; interactive input is not required |
| K07 | Relational and logical operators | Compare symbols, test bounds and identify arrows pointing to the current cell |
| K08 | Decision structures | Select the head, the next connected cell and the stopping outcome |
| K09 | Repetition structures | Search the matrix and follow the path to the tail |
| K10 | Arrays and matrices | Access the grid by valid indexes and organize the ordered coordinate result |
| K12 | Software testing | Compare observed and expected behavior when optional verification is performed |

Neighbor relationships, index bounds and arrow direction are details within these existing topics. 
No new knowledge identities are proposed. 

K06 supports presentation of results without adding an input-reading requirement.


## 3. Learning objectives

| Objective | Bloom level | Competency |
|---|---|---|
| Access the matrix safely and maintain the current position and ordered result | Apply | CM02 |
| Implement arrow-based neighbor selection and tail recognition | Apply | CM03 |
| Traverse the grid and snake using appropriate continuation and stopping rules | Apply | CM04 |
| Explain how conditions select the next cell and identify the tail | Understand | CM14 |
| Explain repeated traversal and its stopping rule | Understand | CM15 |
| Optionally compare outputs with expectations and judge conformity | Apply and Evaluate | CM08 |

## 4. Reused competencies

CM02, CM03, CM04 and CM08 are reused from TASK401; CM14 and CM15 from the TASK401 adjustment. Their definitions and complete constitutive knowledge–Bloom pairings are preserved. Only manifestations and evidence are contextualized. No new competencies are proposed.

### CM02 — Maintain program data and state

**Definition:** initialize, access and update program data using an appropriate representation while preserving valid values and state consistency.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K03 — Data types, constants and variables | Apply | Represent data using appropriate types, constants and variables |
| K05 — Assignment statements | Apply | Initialize and update variable values consistently |
| K10 — Arrays and matrices | Apply | Store, access and update elements using valid indexes |
| K04 — Arithmetic and literal expressions, when required | Apply | Evaluate expressions to obtain values used in data initialization or updates |

**Manifestation and evidence:** source code accesses grid cells safely, maintains the current row and column, and constructs an ordered sequence of coordinate pairs. Each snake cell appears exactly once, with no spaces or omissions. Neighbor access respects matrix bounds. The grid itself need not be modified, and a separate visited structure is not mandatory when directional traversal already prevents revisiting.

**Disposition:** meticulous.

### CM03 — Implement decisions with Boolean conditions

**Definition:** implement Boolean conditions and conditional branches that select actions according to specified rules.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K07 — Relational and logical operators | Apply | Construct Boolean conditions using comparisons and logical combinations |
| K08 — Decision structures | Apply | Implement conditional branches that execute the appropriate actions according to condition results |

**Manifestation and evidence:** source code recognizes `h` and selects only neighboring cells whose arrows point to the current position. For current position `[r, c]`, the possible successors are `[r, c-1]` containing `>`, `[r, c+1]` containing `<`, `[r-1, c]` containing `v`, or `[r+1, c]` containing `^`, provided the relevant position exists. No qualifying successor means the tail has been reached. Nearby occupied cells not satisfying this rule are not selected.

**Disposition:** meticulous.

### CM04 — Implement repetition with a stopping condition

**Definition:** implement repeated execution controlled by a condition or iteration limit, updating control values when required.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K09 — Repetition structures | Apply | Implement loops with appropriate continuation and stopping conditions |
| K05 — Assignment statements, when required | Apply | Initialize and update values used to control repetition |

**Manifestation and evidence:** source code searches for the head and repeatedly advances through the connected path. The current position is updated consistently, and traversal stops after including the tail. Dimensions and stopping rules support arbitrary valid rectangular matrices rather than hardcoded example positions.

**Disposition:** meticulous and persistent.

### CM14 — Explain conditional execution

**Definition:** explain how Boolean conditions determine the actions executed by conditional structures.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K07 — Relational and logical operators | Understand | Explain how comparisons and logical combinations determine a condition's truth value |
| K08 — Decision structures | Understand | Explain how condition results determine which branch is executed |

**Manifestation and evidence:** the required brief explanation connects arrow orientation to next-cell selection. It explains why the algorithm moves to a neighboring cell pointing back to the current cell, rather than following the current cell's arrow toward the head. It also explains how the absence of a successor identifies the tail. The explanation agrees with the implemented conditions.

**Disposition:** communicative and meticulous.

### CM15 — Explain repeated execution

**Definition:** explain how repetition structures control repeated execution and determine when it continues or stops.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K09 — Repetition structures | Understand | Explain the repeated action and the condition or iteration limit governing continuation and termination |

**Manifestation and evidence:** the required explanation describes repeated next-cell selection and termination at the tail. It relates the stopping rule to the implementation and explains how the traversal advances along the path without cycling. A separate formal proof or execution trace is not required.

**Disposition:** communicative and meticulous.

### CM08 — Verify program behavior with test cases

**Activation:** optional.

**Definition:** use test cases to compare observed and expected behavior and judge conformity to specified requirements.

| Knowledge | Bloom level | Observable operation |
|---|---|---|
| K12 — Software testing | Apply | Execute representative test cases with specified inputs and expected results |
| K12 — Software testing | Evaluate | Judge conformity to requirements by comparing observed and expected results |

**Manifestation and evidence:** optional verification records compare sequences with expected paths, check complete coverage without duplicates and conclude whether the implementation meets the requirements. Suggested extra cases use a rectangular grid and a head on a boundary. Producing both required example outputs is mandatory, but those outputs alone do not establish CM08's comparison and judgment operations.

**Disposition:** meticulous and persistent.

## 5. Activation and performance criteria

| Code | Constraint | Mode | Role | Requirement or condition |
|---|---|---|---|---|
| CM02 | mandatory | constructive | core | Maintain valid indexed access and an ordered coordinate result |
| CM03 | mandatory | constructive | core | Select successors using arrows and recognize the tail |
| CM04 | mandatory | constructive | core | Search and traverse with correct termination |
| CM14 | mandatory | explanatory | supporting | Explain the selection and tail-recognition conditions |
| CM15 | mandatory | explanatory | supporting | Explain traversal continuation and termination |
| CM08 | optional | operational;evaluative | supporting | Compare outputs with expectations and judge conformity |

There are six direct associations: five mandatory and one optional, with no competency composition. The same brief explanation may support CM14 and CM15, but their distinct criteria must both be satisfied.

**Expected performance:** the program locates the head, follows the arrow-defined connections and returns all snake cells exactly once in `[row, column]` order. It handles boundary positions safely and supports arbitrary valid matrix dimensions. The brief explanation accurately describes successor selection and stopping.

The required example outputs are:

**Example I — 12 cells:**

```text
[[3, 2], [2, 2], [2, 1], [2, 0],
 [1, 0], [1, 1], [0, 1], [0, 2],
 [0, 3], [1, 3], [2, 3], [3, 3]]
```

**Example II — 8 cells:**

```text
[[1, 2], [1, 3], [2, 3], [2, 2],
 [2, 1], [2, 0], [3, 0], [3, 1]]
```

Source code and required example outputs support assessment of construction. The brief explanation supports the explanatory competencies. These specifications describe intended performances and do not, by themselves, establish individual learner mastery.