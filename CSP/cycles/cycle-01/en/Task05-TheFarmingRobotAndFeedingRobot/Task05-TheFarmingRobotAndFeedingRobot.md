# **Problem 5 (Task): The Farmer Robot and the Feeder Robot**
 
Authors: Luiz Gavaza &nbsp; Lais Salvador &nbsp; Roberta Oliveira &nbsp; Jessica Santana &nbsp; Otávio Neto

Contributor: Edeyson Gomes
 
## Task: The Farmer Robot and the Feeder Robot

### **1. Introduction**

The company **Farmer Robot** was highly satisfied with the solutions proposed for the problems of signaling food delivery and the robot's return to the starting point. Now, the innovation department is excited about implementing a new functionality and introducing a new robot: the Farmer Robot, while traversing herds and issuing food delivery alerts, must also communicate the path the **Feeder Robot** should follow to deliver the appropriate supplies to the herd. This new robot, the Feeder Robot, is in its prototype phase, with the initial demand focusing on implementing its navigation module.

Meanwhile, the UFBA student team responsible for developing the initial Farmer Robot modules, upon studying the new demands, found in the literature an **abstract machine with sequential read and write access to an unlimited memory device**. This machine can incorporate the Farmer Robot's modules as well as the Feeder Robot's navigation module. This finding was shared with the company's innovation team, which then proposed enhancements to the Farmer Robot modules. For example, upon reviewing the solution proposed for the food delivery signaling problem, the students realized they could improve it by allowing the farmer to specify the minimum quantities of herd members as inputs to the machine. 

Additionally, after several meetings with the innovation team, it was decided—both to standardize documentation and to train the maintenance team—that the same **abstract machine model** should be used to implement both the enhanced Farmer Robot navigation module and the Feeder Robot navigation module.

The suggested tool for simulating the robots' modules is **JFLAP[^1]**.

[^1]: www.jflap.com



### **2. Process**

The **Problem-Based Learning (PBL)** methodology will be employed during the solution development process. This approach uses real-world problems to stimulate critical thinking, teamwork, and problem-solving skills while fostering knowledge construction around a specific topic.

The process must be documented using the **PBL Whiteboard**, which consists of the columns: QUESTIONS, FACTS, IDEAS/HYPOTHESES, and ACTIONS. In each team meeting, a version of the whiteboard must be created and shared with the tutors, highlighting the evolving process of building the solution. Additionally, each team will maintain a **shared Logbook**, which must include meeting minutes, participant names, discussion points, and challenges encountered. This documentation will be part of the group evaluation. In the PBL approach, each team member's **participation and contribution** is crucial. Thus, each student will also be individually assessed based on tutor observations and peer feedback.



### **3. Deliverables**

A team member must submit the following by **8:20 PM on May 24, 2021**, via UFBA's virtual learning platform (AVA):  

1. A file for the **JFLAP simulator** containing the Farmer Robot's identification and navigation modules as well as the Feeder Robot's navigation module.  
2. A **report**, written in the SBC (Brazilian Computing Society) article format, that thoroughly details the design and functionality of the developed modules for the robots.  

The report must include the operations executed by the system and at least **two detailed examples** of the functionality of each developed module.


### **4. Knowledge/Concepts Involved**

    1. Turing Machine  

    2. Variations of Turing Machine  



### **5. Learning Objectives**

#### **5.1 General Objectives**

Develop identification and navigation modules for the Farmer Robot and the Feeder Robot using knowledge of Turing Machines.


#### **5.2 Specific Objectives**

1. Understand the new demands and functionalities related to the Farmer Robot and the Feeder Robot.  

2. Investigate the abstract machine with sequential read and write access to an unlimited memory device and its application to the robots' modules.  

3. Revise the solution proposed for the food delivery signaling problem, enabling the farmer to specify the minimum number of herd members as inputs to the machine.  

4. Develop navigation modules for the Farmer Robot and Feeder Robot using the same abstract machine model to standardize documentation and training.  

5. Use the **JFLAP** tool to simulate the processes of the robots' modules.  

### </a> References 
RAMOS, M. V. M.; JOSE NETO, J.; VEGA, I. S. **Linguagens Formais: Teoria, Modelagem e Implementação**. Editora Bookman, 2009.

MENEZES, Paulo Blauth. **Linguagens formais e autômatos**. 6. ed. Bookman, 2011.
