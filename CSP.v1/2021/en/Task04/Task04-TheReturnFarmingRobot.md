# **Problem 4 (Task): The farmer robot returns**
 
 Authors: Luiz Gavaza &nbsp; Lais Salvador &nbsp; Roberta Oliveira &nbsp; Jessica Santana &nbsp; Otávio Neto
 
 Contributors: Edeyson Gomes
 
## **Task: The Return of the Farmer Robot**

### **1. Introduction**

The company **Farmer Robot** was highly satisfied with the proposed solution for signaling food delivery and is now excited about implementing a new functionality: in addition to navigating through the herd and sending food delivery alerts, the robot must also be capable of returning to its starting point to perform another task. The company already has "external sensor" kits to guide the robot to the herds, but the challenge is figuring out how to make the robot return to its starting point. As previously agreed with the farmer, the robot should still issue food delivery alerts based on the minimum number of herd members detected.

The UFBA student team responsible for developing the initial prototype studied this navigation problem and realized that a simple finite state machine (FSM) is insufficient to solve it. Understanding how they reached this conclusion is an interesting question. Upon further exploration of the problem of returning to the starting point, the students observed that adding an **auxiliary memory device** to the FSM could model a solution to support the robot's navigation.

The students also noted that the **Food Delivery Module** from the original Farmer Robot problem could be extended with the proposed navigation module. Alternatively, the two modules could operate as separate solutions running in parallel, with some form of communication between them. Additionally, the company expressed interest in a **notation system** to specify rules for generating location sequences, to aid in documenting and improving the robot's navigation module.

The suggested tool for simulating the robot's navigation module and generating location sequences is **JFLAP**.



### **2. Process**

During the solution development process, the **Problem-Based Learning (PBL)** methodology will be employed. This approach uses real-world problems to stimulate critical thinking, teamwork, and problem-solving skills while fostering knowledge construction on a specific topic.

The process must be documented using the **PBL Whiteboard**, which consists of the columns: QUESTIONS, FACTS, IDEAS/HYPOTHESES, and ACTIONS. In each team meeting, a version of the whiteboard must be created to document the steps taken to build the solution. Additionally, a shared document will be provided for filling out the **Logbook**, which must include meeting minutes, participant names, discussion points, and challenges encountered. This documentation will be an integral part of the group’s evaluation. Each team member's participation/contribution is crucial and will also be individually assessed based on observations by the tutors and feedback from peers.



### **3. Deliverables**

A team member must submit the following by **8:20 PM on April 28, 2021**, via UFBA's virtual learning environment (AVA):  

1. A file for the **JFLAP simulator** containing the robot's navigation module.  

2. A **report**, written in the SBC (Brazilian Computing Society) article format, that thoroughly details the design and functionality of the robot's navigation module.  

The report must describe the system's operations and include at least **two examples** of its functionality. If a rule-based notation system was developed, the report must also include examples of location sequence generation. If not developed, the report should detail the main difficulties encountered.



### **4. Knowledge/Concepts Involved**

    1. Pushdown Automata 
    
    2. Context-Free Grammars  



### **5. Learning Objectives**

#### **5.1 General Objective**

Develop a navigation module for the Farmer Robot, enabling it to return to its starting point after issuing a food delivery alert.

#### **5.2 Specific Objectives**

1. Understand the functionalities and challenges of the Farmer Robot's navigation problem.  

2. Investigate the use of auxiliary memory devices in a finite state machine to model a solution for returning to the starting point.  

3. Analyze the feasibility of extending the Food Delivery Module with the proposed navigation module or developing parallel solutions capable of communication.  

4. Research and propose a notation system to specify rules for generating location sequences for documentation and module improvement.  

5. Use the **JFLAP** tool to simulate the robot's navigation process and generate location sequences.  

### </a> References 
RAMOS, M. V. M.; JOSE NETO, J.; VEGA, I. S. **Linguagens Formais: Teoria, Modelagem e Implementação**. Editora Bookman, 2009.

MENEZES, Paulo Blauth. **Linguagens formais e autômatos**. 6. ed. Bookman, 2011.