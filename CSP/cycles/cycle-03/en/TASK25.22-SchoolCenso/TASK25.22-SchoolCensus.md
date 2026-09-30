# Task25.22 — School Census and Computational Thinking in Natural Language

### Autor: Edeyson Gomes


## Task Description

In this task, you will take on the role of a **data detective** helping your school understand information from a small **school census**.

Your mission is to describe, in **clear natural language**, how a computer could read student records, organize the information, count cases, compare groups, and produce useful results. You will not write code yet. Instead, you will practice something that every programmer needs to do before coding: **thinking carefully about the problem and describing the solution step by step**.

The activity is organized into **four progressive challenges**. In each challenge, the school census receives new information, such as sex and visual conditions. Your algorithm must then be adapted to answer new questions. At each stage, you will reuse what you already built, improve your reasoning, and make your solution more complete.

This task connects Computing to real situations in school life, showing how data can be collected, represented, processed, and interpreted to support decisions. By the end, you should be able to explain how an algorithm processes records, uses conditions, updates counters, calculates results, and checks whether the solution is correct, clear, and efficient.



## What You Are Expected to Learn

By completing the four challenges, you should be able to:

1. Recognize a **data record** and identify the fields needed to solve a problem, such as `Name`, `Sex`, `Myopia`, `Hypermetropia`, or `Astigmatism`.

2. Describe an **algorithm in natural language**, organizing the steps clearly enough for another person — or a future program — to follow.

3. Use **logical decisions** with expressions such as `if`, `else`, `and`, and `or` to classify students and count information correctly.

4. Explain how **counters, totals, averages, and proportions** are produced from a set of records.

5. Reuse, adapt, and improve an algorithm as new fields, rules, and combined conditions are added.

6. Review your own solution, finding logical mistakes, repeated steps, or opportunities to make the algorithm simpler and clearer.

7. Connect the activity to real situations in which data is collected and analyzed to support decisions, such as school censuses, surveys, health records, and public statistics.





## Task Stages — Progressive Challenges

### Challenge 1 — First Census: Counting by Sex

**Your mission:**  
Describe, in natural language, an algorithm that reads a list of student records with the fields `Name` and `Sex`.

Your algorithm must discover:

- how many boys are registered;
- how many girls are registered;
- how many students are registered in total.

Explain how the algorithm reads **one record at a time**, checks the `Sex` field, and updates the correct counters.

**Key ideas:**  
Sequential processing, simple conditions, counters.




### Challenge 2 — Adding a New Clue: Myopia

**Your mission:**  
Now the census includes a new field: `Myopia`.

Adapt your previous algorithm so it can:

- count students with myopia;
- count boys with myopia;
- count girls with myopia;
- calculate the proportion or average of students with myopia in each group;
- calculate the overall proportion or average of students with myopia.

Reuse the logic from Challenge 1 and clearly explain what needs to be added or changed.

**Key ideas:**  
Counters, accumulators, averages, proportions, adaptation.




### Challenge 3 — Two Visual Conditions: Myopia and Hypermetropia

**Your mission:**  
Now each student record includes two visual conditions: `Myopia` and `Hypermetropia`.

Adapt your algorithm to produce **detailed counts and results**, including:

- total number of students;
- total number of boys and girls;
- total number of students with **myopia**;
- total number of students with **hypermetropia**;
- number of boys and girls with **myopia**;
- number of boys and girls with **hypermetropia**;
- number of students who have **myopia OR hypermetropia** (at least one condition);
- number of students who have **myopia AND hypermetropia** (both conditions).

In addition, your algorithm should:

- calculate proportions or averages for each relevant group;
- clearly explain how each counter is updated;
- show how decisions are made using logical operators.

### Important

Be careful to distinguish between:

- students who have **only one condition**, and  
- students who have **both conditions at the same time**.

Your algorithm must not count the same student incorrectly.

### Key ideas

Composite conditions, logical operators (`AND`, `OR`), detailed counting, classification, and refinement of previous solutions.






### Challenge 4 — The Complete Census: Three Conditions and Combinations

**Your mission:**  
In the final challenge, each student record includes three visual conditions: `Myopia`, `Hypermetropia`, and `Astigmatism`.

Describe a complete and well-organized algorithm that produces **detailed counts and results**, including:

- total number of students;
- total number of boys and girls;
- total number of students with **myopia**;
- total number of students with **hypermetropia**;
- total number of students with **astigmatism**;
- number of boys and girls with **myopia**;
- number of boys and girls with **hypermetropia**;
- number of boys and girls with **astigmatism**;
- number of students who have **myopia OR hypermetropia OR astigmatism**;
- number of students who have **myopia AND hypermetropia**;
- number of students who have **myopia AND astigmatism**;
- number of students who have **hypermetropia AND astigmatism**;
- number of students who have **all three conditions**.

In addition, your algorithm should:

- calculate proportions or averages for each relevant group;
- clearly explain how each counter is updated;
- show how simple and combined conditions are checked;
- organize the solution so that it can be reused or adapted if a new visual condition is added in the future.

### Important

At this stage, your solution should look like a well-planned algorithm, not just a list of separate calculations.

Be careful to distinguish between:

- students with **only one condition**;
- students with **two combined conditions**;
- students with **all three conditions**.

### Key ideas

Combined conditions, logical operators (`AND`, `OR`), repetition, modular reasoning, reuse, detailed counting, and solution refinement.



## Final Notes

- Write your algorithms as if you were giving clear instructions to another person — or preparing the logic that could later become a computer program.
- Be precise, but use **natural language**, not programming code.
- Organize your answer step by step, using names for counters, fields, and conditions.
- Each challenge builds on the previous one: **reuse, adapt, and improve your solution** instead of starting from zero.
- Focus on **clarity, logical correctness, and good organization**.
- Before submitting, review your algorithm and check whether any student could be counted incorrectly.

This task will help you think like a computing student: reading data, organizing information, making decisions with conditions, calculating results, and explaining your reasoning clearly.