## CSP Refinement Report

Throughout the implementation of the **Competency Specification Process (CSP)**, a set of methodological refinements was progressively identified as a consequence of its application across multiple instructional tasks. These refinements were not recall-based or participant-driven; rather, they resulted from **systematic analysis of instructional artifacts** produced during **Phase 1 (Competency Authoring)** and from **structured expert feedback** documented in **Phase 2 (Expert Review)**. Together, these iterative cycles contributed to the consolidation and maturation of the CSP as a methodological framework for competency specification.

An early methodological issue observed during **Phase 1** concerned the **explicit determination of cognitive levels** in **Bloom’s Revised Taxonomy** for each knowledge–skill pairing. Although Bloom-aligned verbs were initially employed to indicate intended learning outcomes, the **justification for the selected cognitive levels** was not always explicitly documented. This limited the interpretability of the specifications, particularly when competencies with similar surface structures were intended to operate at distinct cognitive depths.

To mitigate this limitation, the CSP was refined to require that each knowledge–skill pairing be **explicitly associated with clearly defined Bloom-aligned verbs**, serving as observable indicators of the intended cognitive demand. This adjustment improved the internal coherence of competency specifications and reduced ambiguity in the interpretation of expected learner performance across tasks.

During **Phase 2**, expert reviewers confirmed the relevance of this refinement and further indicated the need to **explicitly document the rationale underlying Bloom-level assignments**, rather than relying exclusively on verb selection. The review highlighted that, in the absence of such documentation, distinctions among cognitive processes such as *Understand*, *Apply*, *Analyze*, and *Create* could remain underspecified, particularly in tasks involving formal modeling and system integration.

In response to these findings, the CSP specification template was extended with a dedicated **“Bloom’s Taxonomy Alignment”** subsection. This subsection records the **intended cognitive scope** of each knowledge–skill pairing, as established through the interaction between competency specification artifacts and expert review criteria. The inclusion of this subsection strengthens **methodological transparency**, allowing readers to trace how cognitive expectations were defined, examined, and validated within the CSP, without relying on implicit interpretation.

Concurrently, the repeated application of the CSP across different tasks indicated that the initial organization of reports and artifacts—while functional—lacked sufficient formalization to guarantee **procedural consistency and reproducibility**. Early iterations relied on partially ad hoc document structures, which increased the risk of variation in documentation practices across tasks.

To address this issue, the CSP was progressively complemented with a set of **standardized reporting templates**, each aligned with a specific phase of the process, including:

* **Instructional Entity Analysis Report**
* **CSP Phase 1A & Phase 1B Template Report**
* **CSP Phase 2 – Expert Review (CSRP) Template Report**
* **CSP Review Guide**
* **CSP Phase 3 – Semantic Structuring Report**

These templates were introduced as **procedural instruments**, not as fixed prescriptions. They were iteratively refined alongside the CSP itself, based on the analysis of competency specifications and expert review outcomes across successive tasks. Their adoption supports greater **explicitness, auditability, and transferability** of the CSP, while maintaining flexibility for application in different instructional domains.

Collectively, these refinements contributed to the evolution of the CSP from an initial procedural outline into a **robust, transparent, and replicable framework** for competency modeling in education. The refined process supports explicit cognitive alignment, systematic expert validation, and semantic structuring of competencies, strengthening the methodological foundations of the CSP without involving personal data, learner behavior analysis, or human subject experimentation, in accordance with the principles underlying the **TCLE**.



### Standardized Competency Identifiers

Another significant refinement that emerged from the iterative application of the **Competency Specification Process (CSP)** was the adoption of **short, unique identifiers (IDs)** for each competency (e.g., *C01*, *C02*, *C05*). In the initial stages, competencies were labeled using alphabetic conventions—such as *Competency A* in *Task 01*—which proved sufficient in isolated or small-scale contexts. However, as the corpus of competencies expanded and cross-referencing across tasks, phases, and reports became more frequent, this approach revealed clear limitations in scalability and consistency.

To address these issues, a **globally sequential numeric scheme** was introduced, assigning each competency a unique identifier in the form `CXX`. This scheme is independent of task origin, instructional context, or development phase, thereby providing a stable and unambiguous reference mechanism throughout the CSP lifecycle. The adoption of numeric identifiers substantially improved coordination and communication among stakeholders, particularly during iterative expert review cycles and comparative analyses involving multiple competencies.

Although full competency titles remain essential for conveying semantic intent and instructional meaning, they are often **too verbose or cognitively demanding** for repeated use in technical discussions, interdisciplinary collaboration, or multilingual documentation. In contrast, concise and standardized identifiers support **clarity, efficiency, and traceability**, especially in activities such as expert feedback consolidation, semantic structuring, versioning, and automated report generation. Consequently, the systematic inclusion of competency IDs was established as a requirement across all CSP-related artifacts.

Beyond their practical role in human-centered workflows, standardized identifiers also play a critical function in **semantic and computational representations**. In machine-readable formalisms—such as RDF graphs and OWL axioms within the **OntoKSD ontology**—stable identifiers are indispensable for ensuring referential integrity, enabling SPARQL queries, supporting automated reasoning, and facilitating alignment with external competency frameworks.

This refinement highlights how incremental procedural adjustments, motivated by practical use and iterative reflection, can yield substantial benefits in both **methodological robustness** and **technical interoperability** within the CSP framework.


### Refinamento da Granularidade Competencial

Aspecto: ajuste progressivo do nível de atomicidade das competências.

Descrição:
A aplicação reiterada do CSP evidenciou a necessidade de equilibrar competências excessivamente amplas (difíceis de avaliar e reutilizar) e competências excessivamente atômicas (que fragmentam o sentido instrucional). Esse refinamento levou à consolidação de competências funcionalmente avaliáveis, semanticamente coerentes e potencialmente reutilizáveis entre tarefas.

Contribuição ao CSP:

- Favorece subsunção e reuso (competências gerais vs. especializadas).

- Sustenta hierarquias ontológicas (competência composta × atômica).

- Evita inflacionamento artificial do catálogo.

Alinhamento direto com os requisitos ontológicos da OntoKSD (competências atômicas, compostas e relações de generalização).



## Reuse Analysis Implications for CSP Refinement

The expert review of the CSP application in **Task201** contributed to the identification of **methodological refinements** that emerged from the **iterative application of the CSP in authentic instructional contexts**. Rather than motivating structural modifications to the process, these refinements clarify how existing CSP phases and artifacts can be **more explicitly and consistently operationalized** when competencies are reused across tasks.

First, the review revealed the importance of **explicitly documenting the mode of competency activation** during reuse. Expert feedback indicated that a given competency may be enacted in different ways—such as **constructive**, **analytical**, **justificatory**, or **artifact-oriented**—depending on task demands and expected evidence. Making these activation modes explicit enhances transparency in competency reuse, improves interpretability during expert review, and reduces ambiguity across CSP iterations.

Second, the application of the CSP highlighted the value of **systematically recording scope tensions** observed in broadly defined competencies, particularly those involving **symbolic or analytical reasoning**. The review indicated that such tensions do not signal deficiencies in the competency framework; instead, they constitute valuable empirical evidence for refining competency descriptions and reuse guidelines, without resorting to unnecessary fragmentation or proliferation of new competencies.

Together, these reuse-related refinements illustrate how the CSP **progressively matures through repeated application and expert review**, strengthening both its procedural clarity and its capacity to support **consistent, transparent, and reusable competency specifications**.

