# **Problem 1 (Task): The vending machine for sodas and snacks**

Authors: Luiz Gavaza  &nbsp;  Lais Salvador  &nbsp;   David Moises &nbsp;    Roberta Oliveira

Contributors: Edeyson Gomes &nbsp;  Jéssica Santana

21 de September de 2020

## **Task: Machine for sodas and snacks**

### **1.  Problem**

The company **Refrigerantes e Salgados S.A.** decided to develop new solutions for their vending machines for soft drinks and snacks, based on well-structured hardware and software designs, accompanied by precise and user-friendly documentation.

The idea emerged during a conversation between one of the company’s IT technicians and a group of students from the Department of Computer Science at UFBA. They realized that certain state machines, known as automata, can support the functionalities of vending machines while requiring minimal memory and being simple to configure.

The company’s machines need to be configured to sell at least three (3) products, accept coins and banknotes of R$1.00 and R$2.00, and provide change. The company’s product portfolio includes soft drinks priced at R$3.00 and R$5.00, as well as snacks priced at R$5.00 and R$7.00.

The students also mentioned a tool called **JFLAP** for testing/simulating solutions that use these automata. They explained that JFLAP provides a graphical interface that could contribute to the documentation of these new vending machine solutions. Another interesting point is that the IT technician, who has worked with regular expressions before, had heard that regular expressions are related to some types of automata. He would like to verify if this information is correct (investigate); if so, he would appreciate at least one example of how this could work for a portion of the automaton constructed for one of the vending machines. He also believes that regular expressions could help document these machines and future projects.

**CHALLENGE**: The IT technician promised an additional bonus if the students could help promote the new machines by implementing a modification that allows the machines to randomly provide a bonus change of R$1.00 if the amount inserted by the customer matches the exact price of the selected product.


### **2. Process**

The solution will be developed using the **Problem-Based Learning (PBL)** methodology, which leverages real-world problems to stimulate critical thinking, teamwork, and problem-solving skills. This approach also aids in the construction of knowledge on a specific topic. 

The process must be documented using the **PBL Whiteboard**, composed of the following columns: **QUESTIONS**, **FACTS**, **IDEAS/HYPOTHESES**, and **ACTIONS**. During each team meeting, a new version of the whiteboard should be created, providing a step-by-step documentation of the solution development. The description of this process will be part of the group’s evaluation. 

Additionally, a shared document will be provided to record the **Logbook**, as demonstrated during a synchronous session. This log will serve as a complementary record of the team’s progress and decisions throughout the project.


### **3. Deliverable**

You must submit your deliverable on the **UFBA LMS (Moodle)** platform by **20:20 on October 13, 2020**, in the designated space. The submission should include:

1. **Automaton File**:  
   An automaton representing a vending machine for soft drinks and snacks that can be tested/simulated using JFLAP. The automaton must reflect the intended functionalities and operations of the vending machine.

2. **Detailed Report**:  
   A report following the **Sociedade Brasileira de Computação (SBC)** article format, describing in detail the design and functionality of the vending machine system. The report should include:
   - A clear explanation of the operations performed by the system to process payments and deliver the selected product.
   - At least two examples illustrating the vending machine’s functionality.
   - If applicable, the report should also include a **regular expression** for a portion of the automaton, along with the method used to construct this expression.
   - If it is not feasible to include the regular expression, the report must provide a detailed justification explaining the reason for this limitation.

By fulfilling these requirements, the submission will provide the necessary tools for the company’s technology team to evaluate and simulate the vending machine system effectively.




### **4 Knowledge/Concepts Involved** 
    1. Deterministic Finite Automata (DFA)

    2. Non-Deterministic Finite Automata  (NFA ou NDFA)

    3. Regular Expressions (RE)



### **5. Learning objectives** 

#### **5.1 General objective** 
Develop finite automata and regular expressions to solve “real” problems, as is the case with the machine project of the he company **Refrigerantes e Salgados S.A.*** 

#### **5.2 Specific objectives** 


   1. **Identify** the functionalities of the system designed by the user.

   2. **Reconcile** the functionalities desired by the user with the functionalities of the automaton to be developed.

   3. **Evaluate** the use of non-determinism in the developed automaton.

   4. **Associate** machine options, coins, notes with symbols of an alphabet.

   5. **Specify** technical reports.

   6. **Use** simulation tools for AF


### </a> References 
This problem is based on the lecture notes of Professor Martin Musicante 2</sup> do DIMAP - UFRN. <sup>2<https://sigaa.ufrn.br/sigaa/public/docente/portal.jsf?siape=12212512></sup>

RAMOS, M. V. M.; JOSE NETO, J.; VEGA, I. S. **Linguagens Formais: Teoria, Modelagem e Implementação**. Editora Bookman, 2009.

MENEZES, Paulo Blauth. **Linguagens formais e autômatos**. 6. ed. Bookman, 2011.
