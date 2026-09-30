# **Problem 3 (Task): Farmer Robot**
 
Authors: Luiz Gavaza &nbsp; Lais Salvador &nbsp;  Roberta Oliveira  &nbsp; Daniel Cason
 
Authors: Edeyson Gomes &nbsp;  Jéssica Santana

## **Task: The Farmer Robot**

### **1. Introduction**  
The company **Farmer Robot** is developing a prototype robot to identify herds in livestock farms where animals roam freely (extensive livestock farming). This robot is equipped with a highly advanced visualization module capable of classifying animals as bovine, caprine, or swine. To improve farm management—such as selecting the appropriate feed for each herd—it is essential to identify which herds are present in the enclosures. To minimize transportation costs for delivering feed, the robot must send feed requests when it identifies a minimum number of individuals in a given herd. These minimum quantities are predefined with the farm owner. However, the Farmer Robot company has not yet developed the module responsible for performing this identification.  

A technician at Farmer Robot, who is also a student in one of UFBA's Computing courses, brought this problem to their classmates so they could collaboratively develop a prototype for the robot's identification module. Due to budget constraints, Farmer Robot is seeking the most cost-effective solution for this initial prototype.  

During their initial research, the students determined that a simple finite state machine could solve the problem. How they reached this conclusion is an interesting question. Additionally, the students discovered a mathematical expression frequently used in protocols, which is easy to understand and could be part of the solution's documentation. This expression can be constructed once the solution is implemented using a finite state machine. The students presented this possibility in a meeting, and the company expressed interest in learning more about this aspect.  

The company is also interested in determining whether a rule can be established to calculate the minimum number of states and transitions required based on the minimum herd quantities to be identified. This would enable more accurate budgeting for the project.  

The suggested tool for simulating the robot's identification module is **JFLAP**.  



### **2. Process**  
During the solution development process, the **Problem-Based Learning (PBL)** methodology will be used. This approach leverages real-world problems to stimulate the development of critical thinking, teamwork, and problem-solving skills while fostering knowledge construction around a specific topic.  

The process must be documented using the **PBL whiteboard**, which consists of the columns **QUESTIONS, FACTS, IDEAS/HYPOTHESES, and ACTIONS**. During each team meeting, a version of the whiteboard should be created, thereby documenting the steps taken in constructing the solution. This documentation will be part of the group's evaluation. Additionally, a shared document will be provided to record the **Logbook**, containing meeting minutes, participant names, discussion points, and challenges encountered, as explained during a synchronous session.  



### **3. Deliverables**  
A team member must submit the following by **8:20 PM on March 31, 2021**, via UFBA's virtual learning environment (AVA):  

1. A file for the **JFLAP simulator** containing the robot's identification module. 

2. A **report**, written in the SBC (Brazilian Computing Society) article format, that thoroughly details the design and functionality of the robot's identification module.  

The report must describe the system's operations and include at least **two examples** of how it functions. Additionally, the report should address the company's documentation and budgeting inquiries.  



### **4. Knowledge/Concepts Involved**  

    1. Finite State Machines

    2. Regular Languages  

    3. Regular Expressions  



### **5. Learning Objectives**  

#### **5.1 General Objective**  
Develop a herd identification module for the farmer robot prototype using knowledge of finite state machines and regular expressions.  

#### **5.2 Specific Objectives**  

1. Identify the functionalities of the farmer robot's identification module.

2. Apply the concept of finite state machines to solve the herd identification problem.  

3. Research and use regular expressions as part of the documentation and solution.  

4. Investigate the relationship between the minimum number of herds to be identified and the minimum states and transitions required in the finite state machine.  

5. Use the **JFLAP** tool to simulate the robot's identification process.  

6. Prepare a detailed report in the SBC article format, describing the robot's identification module's operations and providing examples of its functionality.  


### </a> References 
RAMOS, M. V. M.; JOSE NETO, J.; VEGA, I. S. **Linguagens Formais: Teoria, Modelagem e Implementação**. Editora Bookman, 2009.

MENEZES, Paulo Blauth. **Linguagens formais e autômatos**. 6. ed. Bookman, 2011.