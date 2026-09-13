
# Machine Learning-Driven Identification of Therapeutic Checkpoints in Rheumatoid Arthritis: A Network-Based Approach to Discover Resolution-Promoting Agents

## Overview
Rheumatoid Arthritis (RA) is a chronic autoimmune and inflammatory disease that leads to progressive joint destruction[cite: 3]. While conventional clinical approaches heavily rely on anti-inflammatory mechanisms, a significant percentage of patients experience relapse[cite: 3]. This project shifts the paradigm toward **Resolution Pharmacology**[cite: 3]. We present a comprehensive bioinformatics and machine learning pipeline designed to identify therapeutic checkpoints within the synovial tissue microenvironment that disrupt the "Resolution of Inflammation" pathway, ultimately proposing novel resolution-promoting agents[cite: 1, 3].

## Research Objectives
This reproducible computational pipeline was developed to address three major research gaps:
* **Target Identification:** Extracting specific therapeutic checkpoints (Hub genes) within the protein-protein interaction network of RA synovial tissue that are directly linked to the resolution of inflammation[cite: 3].
* **Generalizability:** Overcoming the overfitting and batch-effect limitations of single-dataset studies by employing machine learning algorithms tested on completely independent external cohorts[cite: 1, 3].
* **Drug Repurposing:** Translating systemic genomic data into pharmacotherapy by utilizing reverse signature analysis (pattern matching) to discover FDA-approved or novel compounds capable of reversing the pathological signature[cite: 1, 3].

## Computational Pipeline & Methodology
1. **Data Acquisition & Preprocessing:** Processed transcriptomic data from synovial tissue utilizing libraries such as SciPy and Statsmodels[cite: 1]. We designated **GSE55235** as the discovery/training dataset and **GSE77298** exclusively as the independent external validation dataset[cite: 1]. 
2. **Network Pharmacology:** Extracted standardized biological targets from the Reactome database[cite: 1, 2]. Integrated differential expression results with STRING PPI networks and applied the Betweenness Centrality algorithm via `networkx` to isolate the top 15 fundamental bottlenecks (Hubs)[cite: 1].
3. **Machine Learning Benchmarking:** Evaluated Random Forest, SVM, and XGBoost classifiers equipped with K-Fold Cross-Validation on the 15 candidate features[cite: 1]. The optimal model was directly tested on the external dataset (GSE77298) to confirm true biological validity without synthetic batch-effect merging[cite: 1].
4. **Reverse Signature Analysis:** Queried the validated upregulated and downregulated checkpoints through the L1000CDS2 database to identify top drug candidates capable of inducing resolution-promoting phenotypic shifts[cite: 1].

## Repository Structure
To ensure full reproducibility and transparent evaluation, this repository is structured as follows:
* **`Data/`**: Contains the processed expression matrices and clinical metadata for both the discovery and external validation cohorts[cite: 2].
* **`Notebooks/`**: Houses the primary Jupyter Notebook (Google Colab compatible) containing the end-to-end Python pipeline[cite: 1, 2].
* **`Results/`**: Stores high-resolution statistical visualizations, including PCA plots, Volcano plots, and Clustered Heatmaps[cite: 1, 2].
* **`Root Directory`**: Contains the `app.py` script, `requirements.txt`, and result matrices (`.csv`) driving the interactive web application[cite: 1, 2].

## Interactive Dashboard
The results of this study have been deployed as a lightweight, interactive web application via **Streamlit Community Cloud**[cite: 1]. The dashboard allows stakeholders and peer reviewers to dynamically explore the network centralities of the therapeutic checkpoints and the final proposed resolution-promoting drugs[cite: 1]. 

```
