# TASK25.3 Cryptarithms: A Playful Approach to Teaching Basic Cryptography Concepts in K–12 Education

**Authors:**  
Edeyson Andrade Gomes¹, Laís do Nascimento Salvador¹  
¹Institute of Computing – Federal University of Bahia (UFBA)  
Salvador – BA – Brazil  

📧 [edeysongomes@ufba.br](mailto:edeysongomes@ufba.br) | [laisns@ufba.br](mailto:laisns@ufba.br)



## **Abstract (Portuguese)**

Cryptography is part of students’ daily lives, but its teaching in Basic Education is challenging due to its mathematical abstraction.  
Cryptarithms emerge as a playful approach to introduce cryptographic concepts, stimulating logical reasoning and creativity.  
This work proposes their use in activities aligned with the BNCC, where students solve and create cryptarithmic challenges, exploring mathematical operations and symbol substitution to represent numbers, promoting engagement and autonomy in learning.



## **Abstract (English)**

Cryptography is part of students' daily lives, but its teaching in Basic Education is challenging due to its mathematical abstraction.  
Cryptarithms emerge as a playful approach to introduce cryptographic concepts, stimulating logical reasoning and creativity.  
This work proposes their use in activities aligned with the BNCC, where students solve and create cryptarithmic challenges, exploring mathematical operations and symbol substitution to represent numbers, promoting engagement and autonomy in learning.



## **1. Introduction**

**Cryptography** plays a fundamental role in digital security, protecting data in passwords, financial transactions, and private communications [Stallings, 2005].  
Despite its growing relevance, the need to understand mathematical operations and algorithmic principles can make learning difficult for students who are still developing logical-mathematical thinking.

In this context, **cryptarithms** emerge as a playful and accessible alternative for introducing basic concepts of cryptography.  
By substituting numbers with symbols or letters in valid mathematical operations [Abbasian, 2010; Miklos], this approach stimulates students’ logical reasoning, creativity, and analytical abilities [Widodo, 2019].  
Moreover, by solving and creating their own challenges, students not only reinforce mathematical and computational concepts, but also develop **autonomy and problem-solving strategies**.

This work proposes the use of cryptarithms as a pedagogical tool to support the teaching of cryptography and **computational thinking** in Basic Education, in alignment with the guidelines of the **BNCC** [BNCC, 2017].  
The methodology encourages active student participation, promoting a more **engaging and interdisciplinary** teaching approach that meaningfully connects **Mathematics and Computing**.



## **2. General and Specific Objectives**

**General Objective:**  
Introduce basic concepts of cryptography through cryptarithms, using mathematical challenges as a tool to develop **computational thinking** and **logical reasoning** skills in Basic Education.

**Specific Objectives:**

* Explore the fundamentals of cryptography (substitution and transposition) [Stallings, 2005];  
* Develop skills in **pattern recognition and computational abstraction**;  
* Stimulate students’ **creativity** in designing their own challenges;  
* Promote **persistence and algorithmic thinking** in the search for efficient solutions.



## **3. Target Audience**

The activity is aimed at **students in upper elementary school (6th to 9th grade)** and **high school**, as well as **teachers** interested in innovative methodologies for teaching Computing and Mathematics.  
The proposal is **adaptable to different grade levels**, and can be applied in curricular settings or extracurricular workshops.



## **4. Skills Developed**

The proposal develops competencies in the areas of **Computational Thinking** and the **Digital World**, in accordance with the **BNCC** [BNCC, 2017] and the **Computing in Basic Education Supplement** [SBC, 2023].

### **Computational Thinking**

* **EF69CO04:** Problem decomposition — breaking complex challenges into smaller parts to facilitate solution.  
* **EF69CO03:** Precise description of solutions — formulating clear and detailed responses, reinforcing the structure of algorithms.

### **Digital World**

* **EF09CO05:** Information encoding — understanding the symbolic representation of numbers and letters in solving challenges, approaching the fundamentals of cryptography.

These skills foster **abstraction, logical reasoning, and autonomy**, preparing students for computational and mathematical challenges both inside and outside the school environment.



## **5. Resources, Materials, and Methodology**

**Materials:** paper, pencil, eraser, and printed challenge cards.  
These simple resources support tangible manipulation of problems and collaborative learning.

### **Activity Stages**

1. **Introduction and Motivation:**

   * Initial questions:
     * “How do we protect our information on the internet?”  
     * “Have you ever used a password or secret code?”  

   * Discussion about the importance of cryptography in everyday life.  
   * Practical examples: passwords, messages, ciphers in games and play (e.g., Caesar cipher).

2. **Theoretical Exploration:**

   * Introduction to the concepts of **cryptography and substitution**;  
   * Demonstration of **historical ciphers** (Caesar, Vigenère);  
   * Discussion of **password strength and security**.

3. **Cryptarithmic Challenges:**

   * Distribution of problems to groups;  
   * Collaborative solving, with emphasis on **decomposition and logical reasoning**;  
   * Teacher mediation to discuss strategies and verify the validity of solutions.

4. **Challenge Creation:**

   * Each group designs its own cryptarithmic problem;  
   * The challenges are exchanged among groups for cross-solving.



## **6. Example of a Problem Solved Step by Step**

### **Statement**

In the distant **Realm of the Magic Mirrors**, a mathematical oracle revealed the following challenge:

> “Find the magic number! Multiply it by 4 and you will see the perfect reflection.”

| Number        | Operation | Result       |
|--------------|-----------|--------------|
| **A B C D E** | × 4      | **E D C B A** |

**Challenge:**  
Find the distinct digits A, B, C, D, and E that make the equation true.

---

### **Step 1: Finding the First Digits**

Digit **A** cannot be 0.  
Since 4 × A = E and E ≤ 9, we have:

* If A = 1, then E = 4  
* If A = 2, then E = 8  

Testing the mirror condition, only A = 2 yields consistency.  
Thus, **A = 2** and **E = 8**.

---

### **Step 2: Determining Digit C**

| Number        | Operation | Result       |
|--------------|-----------|--------------|
| **2 B C D 8** | × 4      | **8 D C B 2** |

For the third digit to remain C, the product (4 × C + x) must end in C.  
Testing:

* 4 × 6 = 24 → 24 + 2 = 26 ✅  
* 4 × 9 = 36 → 36 + 3 = 39 ✅  

C can be 6 or 9.

---

### **Case 1: C = 6**

| Number        | Operation | Result       |
|--------------|-----------|--------------|
| **2 B 6 D 8** | × 4      | **8 D 6 B 2** |

From the second column: 4 × B + 2 = D  
If B = 1, then D = 6 (repeated). ❌  
Therefore, **C ≠ 6**.

---

### **Case 2: C = 9**

| Number        | Operation | Result       |
|--------------|-----------|--------------|
| **2 B 9 D 8** | × 4      | **8 D 9 B 2** |

From the second column: 4 × B + 3 = D  
B = 1 → D = 7 ✅  

**Conclusion:**  
A = 2, B = 1, C = 9, D = 7, E = 8  

🔹 **Magic number: 21978 × 4 = 87912**



## **7. Assessment**

Assessment will be **process-based and formative**, grounded on:

* **Engagement and collaboration** during the activity;  
* **Organization of logical reasoning and clarity of explanations**;  
* **Creation of new cryptarithmic challenges**, encouraging authorship and creative thinking;  
* **Oral presentation of results**, with justifications and step-by-step explanations.

This approach makes it possible to evaluate **conceptual understanding**, the **development of computational skills**, and **collaborative group work**.



## **References**

* Abbasian, G. (2010). *Cryptarithms and Logical Thinking in Mathematics Education.*  
* BNCC (2017). *Base Nacional Comum Curricular.* Ministério da Educação.  
* Miklos, D. *Mathematical Puzzles in Cryptarithms.*  
* SBC (2023). *Computação na Educação Básica: Complemento à BNCC.* Sociedade Brasileira de Computação.  
* Stallings, W. (2005). *Cryptography and Network Security: Principles and Practice.* Pearson.  
* Widodo, S. (2019). *Enhancing Problem Solving Through Cryptarithmetic Games in Mathematics Learning.*  
