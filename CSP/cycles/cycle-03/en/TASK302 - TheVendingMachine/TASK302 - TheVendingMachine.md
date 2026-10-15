# TASK302: The Vending Machine for Soft Drinks and Snacks

Authors: Luiz Gavaza, Lais Salvador, David Moises, and Roberta Oliveira

Collaborators: Edeyson Gomes, Jéssica Santana, and Marcos Bião

Updated: September 2025

## 1. Problem

The company Refrigerantes e Salgados S.A. has decided to develop new solutions for its soft-drink and snack vending machines, based on well-structured hardware and software designs accompanied by precise, easy-to-use documentation.

The idea arose when one of the company's IT technicians was talking to a group of students from UFBA's Institute of Computing. They realized that certain state machines, called automata, could support the vending machines' functions while requiring little memory and being straightforward to configure.

The company's machines must be configured to sell at least three products, accept coins and banknotes in denominations of R$1.00 and R$2.00, and provide change. The company's product range includes:

- soft drinks priced at R$5.00 and R$7.00;
- snack packets priced at R$7.00 and R$10.00.

The students also mentioned JFLAP[^1], a tool for testing and simulating automata-based solutions. They explained that its graphical interface could support the documentation of the new vending-machine solutions.

The IT technician has previously worked with regular expressions and has heard that they are related to some of these automata. The technician would like the students to investigate whether this is correct. If it is, the technician would like at least one example showing how this relationship works for a portion of the automaton constructed for a vending machine. Regular expressions might also help document these machines and future projects.

### Challenge

The IT technician has promised an additional bonus if the students help promote the new machines by implementing a modification that allows them to randomly dispense R$1.00 in bonus change when the amount inserted by the customer exactly matches the price of the selected product.

## 2. Deliverables

Submit the following to the designated space on UFBA Moodle by 11:59 p.m. on October 13, 2025:

1. A file containing an automaton that models a soft-drink and snack vending machine, allowing the technology team at Refrigerantes e Salgados S.A. to test or simulate it in JFLAP.
2. A report using the SBC (Brazilian Computer Society) article template[^2], describing the operation of the vending-machine system in as much detail as possible.

The report must:

- describe the operations performed by the system to receive payment and dispense the selected product;
- present at least two examples of its operation.

If the technician's request can be met, the report must also include:

- the regular expression corresponding to a portion of the automaton under analysis;
- the method used to construct that expression.

If the request cannot be met, the report must justify why.

## 3. Knowledge and Concepts

a. Deterministic Finite Automata
b. Nondeterministic Finite Automata
c. Regular Expressions

## 4. Learning Objectives

### 4.1 General Objective

Develop finite automata and regular expressions to solve real-world problems, such as the design of vending machines for Refrigerantes e Salgados S.A.

### 4.2 Specific Objectives

I. Identify the functions of the system envisioned by the user.
II. Reconcile the functions requested by the user with those of the automaton to be developed.
III. Evaluate the use of nondeterminism in the automaton.
IV. Associate machine options, coins, and banknotes with alphabet symbols.
V. Specify technical reports.
VI. Use simulation tools for finite automata.

## References

RAMOS, M. V. M.; JOSE NETO, J.; VEGA, I. S. *Linguagens Formais: Teoria, Modelagem e Implementação.* Bookman, 2009.

MENEZES, Paulo Blauth. *Linguagens formais e autômatos.* 6th ed. Bookman, 2011.

[^1]: https://www.jflap.org/
[^2]: https://www.sbc.org.br/wp-content/uploads/2024/07/modelosparapublicaodeartigos.zip
