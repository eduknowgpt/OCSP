# TASK305: Online Judges at Logistic Solutions

Authors: Laís Salvador, Edeyson A. Gomes, and Luiz Gavaza

Year: 2025

## 1. Problem

Students at UFBA's Institute of Computing are preparing for the SBC Programming Marathon (http://maratona.sbc.org.br), where teams submit solutions to challenging problems through automated evaluation systems known as Online Judges (OJs).

These systems run submitted code on multiple test cases and return results such as:

- AC — Accepted: the solution passes all test cases.
- WA — Wrong Answer: incorrect output on at least one test case.
- TLE — Time Limit Exceeded: execution exceeds the time limit.
- CE — Compilation Error: compilation fails.
- RE — Runtime Error: an execution error, such as invalid memory access or division by zero.

During training, Carlos encountered a classic logistics problem: the Traveling Salesman Problem (TSP). He brought it to his team at the startup Logistic Solutions, which began submitting implementations to an OJ.

Although the team resolved compilation and runtime errors (CE and RE) and eliminated wrong answers (WA), all solutions continued to receive TLE.

This raised important questions:

- Was the issue in the solution logic or in the OJ's configuration?
- What strategies would be needed to achieve AC when solving TSP instances within the OJ's limits?

The startup's managers also wanted to understand these systems better. Carlos received two additional assignments:

- Assess whether the OJ could handle other complex problems, such as a Timetabling Problem (PT) reported by a university client.
- Investigate whether the OJ can identify reasons for TLE in different situations, for code written by both experienced programmers and programming learners.

When Carlos brought these questions to the Theory of Computation class, his classmates recognized that the OJ's behavior could be abstracted and explained through a Finite State Machine (FSM), representing:

- transitions among typical evaluation outcomes, such as AC, WA, TLE, CE, and RE;
- the OJ's operational workflow.

### Central Challenge

Students must:

- Investigate why TSP and PT solutions tend to receive TLE, relating those results to computational complexity.
- Model the OJ's operation through an FSM that clearly illustrates the evaluation cycle and its constraints.
- Investigate theoretical limitations of Online Judges arising from fundamental properties of languages, automata, and computational models.

## 2. Deliverables

Submit the deliverables through UFBA Moodle.

### Technical Article — SBC Format

Submit an article in the SBC format containing all analyses and results, including:

- the team's discussions of TSP and PT in OJs;
- reasoned hypotheses about the submission results for TSP and PT instances;
- characterization of TSP and PT, highlighting computational challenges, the difficulty of obtaining efficient exact solutions, reasons solutions may receive TLE, and strategies for addressing these difficulties.

#### Extra Challenge

- Evaluate TSP and PT code in an OJ and present results for different input sizes.

### Answers to the Startup's Managers

- Explain the limits of an OJ conceptually and practically.
- Indicate its capacity to evaluate different classes of problems.
- Provide theoretical grounds for explaining why some program behaviors are difficult or impossible to analyze completely, and how far an OJ can predict or diagnose causes of TLE.

### OJ Modeling

Present an FSM representing the OJ's behavior, including:

- a state diagram with transitions involving AC, WA, CE, RE, TLE, and other relevant states;
- a justification of how the FSM captures the system's general behavior;
- an account of the intrinsic limits of the model and the evaluation process.

The text must be clear, structured, and scientifically rigorous, connecting practical issues to course concepts and using bibliographic references correctly.

## 3. Learning Resources

HOPCROFT, J. E.; ULLMAN, J. D.; MOTWANI, R. *Introduction to Automata Theory, Languages, and Computation.* Campus, 2002.

SIPSER, M. *Introduction to the Theory of Computation.* Thomson Learning, 2007.

VIEIRA, Newton José. *Linguagens e Máquinas: Uma Introdução aos Fundamentos da Computação.* 2004.

ZIVIANI, Nivio. *Projeto de algoritmos: com implementações em Pascal e C.* Thomson, 2004. Available at: https://www2.dcc.ufmg.br/livros/algoritmos/

## 4. Concepts

- Recursively Enumerable Languages
- Undecidable Problems
- Universal Turing Machine
- P, NP, and NP-Complete Problems
- Finite State Machines
- Traveling Salesman Problem (TSP)
- Timetabling Problem (PT)
- Limitations of automated evaluation systems
- Time complexity and behaviors that cannot be analyzed in general
- Abstract models for analyzing computational systems

## 5. Learning Objectives

### 5.1 General Objective

Apply fundamental Theory of Computation concepts to model, analyze, and solve practical problems involving Online Judges and the computational complexity of real-world challenges such as TSP.

### 5.2 Specific Objectives

- Explain FSM principles and their application to OJs.
- Interpret TSP and PT and recognize their relationship with NP-completeness.
- Understand the Halting Problem and its implications.
- Apply FSMs to represent the OJ evaluation workflow.
- Use Turing Machine and recursively enumerable language concepts to analyze OJ capabilities and limitations.
- Use tools such as JFLAP to simulate and test the proposed FSM.
- Analyze reasons for TLE in relation to complexity, time limits, and algorithmic strategies.
- Distinguish practical from theoretical limitations of OJs.
- Design an FSM representing an OJ's behavior.
- Produce a technical report in the SBC format.
- Construct illustrative examples of the challenges posed by high-complexity problems.

## References

KIOTHEKA, F.; ALMEIDA, R. *Introdução à maratona de programação.* v. 1.7, 2022. Available at: https://www.inf.ufpr.br/maratona/livreto

BARBOSA, F.; JEOVANE, J.; AVELINO, G.; MAGALHÃES, A. Estudo de coloração de grafos aplicado ao problema de alocação de horários. In: ERCEMAPI, 12., 2024. Proceedings. SBC, 2024. pp. 139–148. DOI: https://doi.org/10.5753/ercemapi.2024.243698

CARDOSO, A. C.; FAGUNDES, F. Escalonamento de grade de horários de disciplinas com coloração de grafos. In: Jornada de Iniciação Científica do CEULP/ULBRA, 19., 2019. Available at: https://ulbra-to.br/jornada/trabalho/escalonamento-de-grade-de-horarios-de-disciplinas-com-coloracao-de-grafos

*Problem reformulated by Laís Salvador, Edeyson Gomes, and Marcos Bião in 2025.*
