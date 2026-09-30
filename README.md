# Competency Specification Process (CSP)

The **Competency Specification Process (CSP)** is a structured, process-driven methodology designed to **derive, model, refine, and validate educational competencies** from authentic instructional tasks.
Developed within the doctoral research project *OntoKSD: A Process-Driven Ontology for Competency Specification in Computing Education*, CSP provides a bottom-up and evidence-based approach to competency engineering aligned with:

* **ACM/IEEE CC2020 Framework**,
* **Bloom’s Revised Taxonomy**,
* **Computing knowledge vocabularies** (CC2020, CS2013, CCS2012), and
* The **OntoKSD ontology**, which offers semantic grounding for all produced artifacts.

This repository contains the **full documentation**, **examples**, **artifacts**, and **templates** associated with the CSP, serving as an open, reproducible resource for educators and researchers working with competency-based education in Computing.

---

## 🚀 Objectives

The CSP aims to:

* Provide a **systematic and reproducible** method for defining competencies from instructional tasks.
* Ensure **semantic coherence and interoperability** through integration with the OntoKSD ontology.
* Support **curricular alignment**, **learner assessment**, and **educational resource annotation**.
* Enable **reuse of competencies** across tasks, courses, and curricula.
* Facilitate **expert review and validation** using clear procedural checkpoints.
* Strengthen the connection between **task-level evidence** (e.g., PBL activities) and **competency models** adopted in Computing Education.

---

## 📘 What the CSP Produces

The process generates several formalized artifacts:

* **Knowledge–Skill (KS) pairs**
* **Dispositions**
* **Competency textual descriptions**
* **Bloom-level mappings**
* **Knowledge area links** (CC2020, CS2013, etc.)
* **Reuse evidence** and alignment rationales
* **Structured competency tables**
* **Ontology-ready specifications** (TTL files or structured templates)

These artifacts feed directly into **OntoKSD**, enabling reasoning, validation, and semantic search.

---

## 📁 Repository Structure (Summary)

```markdown
/
├── 📂 CSP.v2/                              # Refined and expanded version of the CSP
│   ├── 📁 2021/
│   │   ├── 🌐 en/                          # Revised CSP analyses (+ refinement cycles)
│   │   └── 🇧🇷 pt/
│   ├── 📁 2022/
│   │   ├── 🌐 en/
│   │   └── 🇧🇷 pt/
│   ├── 📁 2025/                            # New CSP tasks (MusicCollection, TicTacToe, etc.)
│   │   ├── 🌐 en/
│   │   └── 🇧🇷 pt/
│   ├── 🔗 Competence x Task.md             # Mapping between competencies and tasks
│   ├── 📝 Plano_Ensino_Competências.md     # Competency-based teaching plan
│   ├── 📄 Syllabus_Theory_Computation.md
│   ├── 📄 Syllabus_Theory_Computation_Competences.md
│   └── 📘 Reports/                         # Updated CSP templates and methodological guides
│
├── 📄 Competence List.md                   # Global catalog of competencies
├── 📘 OntoKSD.md                           # Ontology documentation (EN)
├── 📘 OntoKSD.pt.md                        # Ontology documentation (PT)
├── 📄 README.md                            # Project overview (EN)
├── 📄 README.pt.md                         # Project overview (PT)
└── 🗂️ OCSP.vpp                             # Visual modeling project (with backups)
```

---

## 🧩 The CSP in a Nutshell

The CSP follows a **block-structured, multi-phase workflow**, ensuring rigor and traceability:

### **1. Instructional Entity Analysis**

* Identify and analyze tasks (PBL cases, exercises, projects).
* Extract relevant cognitive demands and required knowledge.

### **2. Competency Authoring**

* Specify **Knowledge–Skill pairs**, dispositions, and preliminary competencies.
* Align each KS with Bloom’s verbs and relevant Computing knowledge areas.

### **3. Expert Review & Validation**

* Validate clarity, coherence, and correctness with domain experts.
* Revise based on feedback.

### **4. Semantic Structuring**

* Prepare the validated competencies for integration into the OntoKSD ontology.
* Generate formal specifications, mappings, and reusable competency modules.

This ensures that every competency is **grounded in authentic evidence**, **semantically interoperable**, and **pedagogically sound**.

---

## 🌐 GitHub Pages Documentation

This repository includes a public documentation site powered by **GitHub Pages**.

Once deployed, it will be available at:

```
https://<EdeysonGomes>.github.io/<OKSD>/
```

The site provides:

* A high-level introduction to the CSP
* Step-by-step guides
* Examples for training authors and educators
* Visual artifacts (diagrams, tables, workflows)
* Links to OntoKSD ontology modules

If you want, I can generate a complete **documentation landing page (`index.md`)** for GitHub Pages as well.

---

## 🤝 Contributing

Researchers, educators, and curriculum designers are invited to:

* Propose new instructional tasks
* Submit CSP reports
* Suggest improvements to the methodology
* Contribute competency modules
* Discuss OntoKSD integration

Contributions follow standard GitHub pull request workflow.

---

## 📄 License

Specify your license here (MIT recommended for academic projects).

---

## 🧭 Citation

If this repository or the CSP is used in academic work:

```bibtex
@misc{gomes2025csp,
  author       = {Edeyson Gomes},
  title        = {Competency Specification Process (CSP)},
  year         = {2025},
  note         = {GitHub Repository},
  url          = {https://github.com/<username>/<repo>}
}
```



---

### 🚧 Project Under Development

This repository is currently **under active construction** as part of the ongoing refinement of the doctoral thesis. Contents, structure, and documentation are being updated continuously.



