
# Machine Learning-Driven Identification of Therapeutic Checkpoints in Rheumatoid Arthritis

**A Network-Based Approach to Discover Resolution-Promoting Agents**

## 📌 Overview & Live Dashboard

Rheumatoid Arthritis (RA) is a chronic inflammatory disease where conventional anti-inflammatory treatments often result in patient relapse. This project shifts the paradigm toward **Resolution Pharmacology** by presenting a comprehensive bioinformatics and machine learning pipeline. It is designed to identify therapeutic checkpoints within the synovial microenvironment that disrupt the "Resolution of Inflammation" pathway, ultimately proposing novel resolution-promoting agents. The results of this study have been deployed as a lightweight, interactive web application.

> **🔗 Live Dashboard Access:** [Explore the Interactive Tool Here](https://ml-driven-ra-drug-repurposing.streamlit.app/)

## 🎯 Research Objectives

* **Target Identification:** Extract specific therapeutic checkpoints (Hub genes) within the RA synovial protein-protein interaction network that are directly linked to inflammation resolution.
* **Generalizability:** Overcome overfitting and batch-effect limitations of single-dataset studies by testing machine learning algorithms on completely independent external cohorts.
* **Drug Repurposing:** Translate systemic genomic data into pharmacotherapy using reverse signature analysis (pattern matching) to discover compounds capable of reversing the pathological signature.

## 🛠️ Computational Pipeline

* **Data Acquisition & Preprocessing:** Processed transcriptomic data (GSE55235 as discovery, GSE77298 exclusively as external validation) utilizing SciPy and Statsmodels.
* **Network Pharmacology:** Intersected Reactome pathways with STRING PPI networks, applying Betweenness Centrality via NetworkX to isolate the top 15 fundamental bottlenecks.
* **Machine Learning Benchmarking:** Evaluated Random Forest, SVM, and XGBoost using Stratified 5-Fold Cross-Validation. The optimal model was tested on the external dataset without synthetic batch-effect merging to confirm true biological validity.
* **Reverse Signature Analysis:** Queried the validated upregulated and downregulated checkpoints through the L1000CDS2 database to identify top drug candidates.

## 📊 Key Findings & Repository Structure

* **Genomic Separation:** 2,135 significant DEGs perfectly separated RA from healthy controls.
* **Validated Checkpoints:** Pinpointed critical hubs including **MYC, PTPRC, and JUN**.
* **Model Accuracy:** Random Forest achieved **86.96% accuracy** on the unseen external validation cohort.
* **Proposed Agents:** Discovered **Manumycin A** and **Salermide** as top candidate resolution-promoting drugs.
  
## 📁 Repository Structure 

├── Data/                   # Raw and processed datasets (GSE55235, GSE77298)
├── Notebooks/              # Jupyter notebooks containing the full reproducible pipeline
├── Results/                # Output plots (PCA, Volcano, Heatmap, Confusion Matrix, etc.)
├── app.py                  # Source code for the interactive Streamlit dashboard
├── requirements.txt        # Python dependencies
├── top_hub_genes.csv       # List of the identified therapeutic checkpoints
└── top_candidate_drugs.csv # List of computationally repurposed drugs
