## CSP Refinement Report

Following the sequential application of the **Competency Specification Process (CSP)** across multiple instructional tasks (TASK01–TASK05), a set of methodological refinements was progressively identified. These refinements did not emerge from recall-based accounts, participant feedback, or learner observation. Instead, they resulted from the **systematic analysis of instructional artifacts** produced during **Phase 1 (Competency Authoring)** and from **structured expert feedback** obtained during **Phase 2 (Expert Review)**. 

The iterative interaction between competency authoring, expert review, and subsequent adjustments revealed recurring modeling tensions and procedural limitations. Addressing these issues led to the progressive stabilization of the CSP as a methodological framework for competency specification. Importantly, many of these refinements also exposed representational limitations that later informed the conceptual design of the **OntoKSD ontology**, demonstrating how competency specification practice functioned as a source of ontology requirements.

For clarity, the refinements are organized into three complementary categories: (i) methodological refinements to the CSP process, (ii) conceptual refinements in competency modeling, and (iii) technical and representational refinements supporting traceability and computational interoperability.



### 1. Methodological Refinements to the CSP Process

#### 1.1 Explicit and Justified Bloom Alignment

An early methodological issue observed during **Phase 1** concerned the explicit determination of cognitive levels in **Bloom’s Revised Taxonomy** for each knowledge–skill pairing. Although Bloom-aligned verbs were initially used to indicate intended learning outcomes, the rationale underlying the selection of specific cognitive levels was not consistently documented. As a result, competencies with similar surface formulations could be interpreted as operating at different cognitive depths, reducing interpretability and comparability across tasks.

To mitigate this limitation, the CSP was refined to require that each knowledge–skill pairing be explicitly associated with clearly defined Bloom-aligned verbs treated as observable indicators of cognitive demand. This refinement improved internal coherence and reduced ambiguity in the interpretation of expected learner performance.

During **Phase 2**, expert reviewers confirmed the necessity of this refinement and emphasized that verb selection alone was insufficient in cases involving formal modeling or system integration. Consequently, the CSP specification template was extended with a dedicated **“Bloom’s Taxonomy Alignment”** subsection, explicitly documenting the intended cognitive scope and the rationale supporting Bloom-level assignments. 

This addition strengthened methodological transparency and auditability, enabling readers to trace how cognitive expectations were defined, examined, and validated within the CSP. Moreover, it marked an important conceptual transition in which Bloom levels evolved from purely pedagogical annotations into semantic constraints guiding knowledge–skill pairing interpretation.



#### 1.2 Standardization of CSP Artifacts and Reporting Structure

Repeated application of the CSP also revealed that the initial organization of reports and artifacts, while operationally functional, lacked sufficient formalization to guarantee procedural consistency and reproducibility. Early iterations relied on partially ad hoc documentation structures, increasing variability across tasks and complicating cross-task comparison and auditability.

To address this issue, the CSP was progressively complemented with a set of **standardized reporting templates**, each aligned with a specific phase of the process:

- Instructional Entity Analysis Report  
- CSP Phase 1A & Phase 1B Template Report  
- CSP Phase 2 – Expert Review (CSRP) Template Report  
- CSP Review Guide  
- CSP Phase 3 – Semantic Structuring Report  

These templates were introduced as procedural instruments rather than rigid prescriptions. They evolved alongside the CSP itself, based on recurring issues identified through competency specification and expert review cycles. Their adoption improved explicitness, comparability, and transferability of the process while preserving flexibility for application in different instructional domains.

Collectively, these methodological refinements contributed to transforming the CSP from an initial procedural outline into a more transparent and replicable framework for competency specification.



### 2. Conceptual Refinements in Competency Modeling

#### 2.1 Competency Granularity and Atomicity Control

The iterative application of the CSP revealed the need to balance competencies that were excessively broad—thus difficult to evaluate or reuse—and competencies that were excessively atomic, which fragmented instructional meaning and reduced pedagogical coherence. 

This observation led to a progressive refinement of competency granularity criteria, promoting competencies that are simultaneously functionally assessable, semantically coherent, and reusable across instructional contexts. The refinement supported clearer subsumption relationships between general and specialized competencies and prevented artificial inflation of competency catalogs.

From an ontological perspective, this refinement directly informed OntoKSD requirements concerning the representation of atomic and composite competencies, as well as hierarchical relations such as aggregation and specialization.



#### 2.2 Competency Reuse and Contextual Activation

Expert review conducted across later tasks highlighted the importance of explicitly documenting how competencies are enacted when reused in distinct instructional contexts. The analysis demonstrated that the same competency may be activated in different ways—such as analytical, constructive, justificatory, or artifact-oriented—depending on task design, expected learner actions, and evidence requirements.

A crucial conceptual clarification emerged from this observation: **activation characteristics are not intrinsic properties of competencies**, but contextual properties of their enactment within a specific instructional entity. Consequently, activation attributes must be recorded at the level of the competency–task relationship rather than embedded in the competency definition itself.

Additionally, repeated reuse exposed scope tensions in broadly defined competencies, particularly those involving symbolic or formal reasoning. Rather than indicating deficiencies in the competency framework, these tensions served as empirical signals guiding either procedural clarification of reuse conditions or controlled specialization through derived competencies. This refinement contributed directly to OntoKSD constructs related to activation modeling, competency roles, and specialization mechanisms.



### 3. Technical and Representational Refinements

#### 3.1 Standardized Competency Identifiers

Another significant refinement emerging from the iterative application of the CSP was the adoption of **short, unique competency identifiers** (e.g., C01, C02, C05). In the initial stages of the process, competencies were labeled using alphabetic conventions tied to individual tasks, which proved sufficient in isolated contexts. However, as the competency corpus expanded and cross-referencing across tasks, reports, and expert review cycles became more frequent, this approach revealed clear limitations in scalability, traceability, and long-term consistency.

To address these limitations, a **globally sequential numeric identification scheme** was introduced, assigning each competency a persistent identifier independent of task origin, instructional context, or development phase. This refinement established a stable and unambiguous reference mechanism throughout the CSP lifecycle, improving communication among stakeholders, facilitating expert review consolidation, and enabling consistent traceability of competencies across successive iterations of the process.

Importantly, this refinement converges with the principles established in the **IEEE Reusable Competency Definition (RCD)** specification, which defines competencies as entities requiring unique and persistent identifiers to support reuse, interoperability, and machine-readable representation across systems and contexts. Within this perspective, competency identifiers are not merely organizational labels, but constitute essential elements for maintaining competency identity independently of contextual enactment.

Beyond their practical role in human-centered workflows, standardized identifiers also play a critical role in semantic and computational representations. In machine-readable environments—such as RDF graphs and OWL axioms within the OntoKSD ontology—stable identifiers ensure referential integrity, enable SPARQL querying, support automated reasoning, and facilitate alignment with external competency frameworks. The adoption of unique competency identifiers therefore contributes simultaneously to methodological robustness, semantic clarity, and technical interoperability.

This refinement illustrates how incremental procedural adjustments motivated by practical CSP application progressively aligned the process with established competency modeling standards, reinforcing the role of OntoKSD as a formally grounded representation layer capable of supporting reusable and interoperable competency specifications.




### 4. Summary: CSP Refinement as Ontology Requirement Elicitation

Taken together, these refinements demonstrate that the evolution of the CSP did not result from isolated procedural adjustments, but from the progressive stabilization of recurring patterns observed across successive instructional applications. Many of the difficulties initially perceived as methodological issues were ultimately recognized as representational limitations, motivating the introduction of formal constructs later incorporated into OntoKSD.

In this sense, CSP refinement should be understood not only as process improvement but also as a systematic form of **ontology requirement elicitation grounded in empirical competency specification practice**. The refined CSP thus emerges as both a methodological framework for competency authoring and a generative mechanism through which the ontological foundations of OntoKSD were progressively identified, validated, and operationalized, without involving personal data, learner behavior analysis, or human subject experimentation, in accordance with the principles underlying the TCLE.


