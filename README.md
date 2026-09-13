
# Machine Learning-Driven Identification of Therapeutic Checkpoints in Rheumatoid Arthritis: A Network-Based Approach to Discover Resolution-Promoting Agents

## Overview
Rheumatoid Arthritis (RA) is a chronic autoimmune and inflammatory disease that leads to progressive joint destruction. While conventional clinical approaches heavily rely on anti-inflammatory mechanisms, a significant percentage of patients experience relapse. This project shifts the paradigm toward **Resolution Pharmacology**. We present a comprehensive bioinformatics and machine learning pipeline designed to identify therapeutic checkpoints within the synovial tissue microenvironment that disrupt the "Resolution of Inflammation" pathway, ultimately proposing novel resolution-promoting agents.

## Research Objectives
This reproducible computational pipeline was developed to address three major research gaps:
* **Target Identification:** Extracting specific therapeutic checkpoints (Hub genes) within the protein-protein interaction network of RA synovial tissue that are directly linked to the resolution of inflammation.
* **Generalizability:** Overcoming the overfitting and batch-effect limitations of single-dataset studies by employing machine learning algorithms tested on completely independent external cohorts.
* **Drug Repurposing:** Translating systemic genomic data into pharmacotherapy by utilizing reverse signature analysis (pattern matching) to discover FDA-approved or novel compounds capable of reversing the pathological signature.

## Computational Pipeline & Methodology
1. **Data Acquisition & Preprocessing:** Processed transcriptomic data from synovial tissue utilizing libraries such as SciPy and Statsmodels. We designated **GSE55235** as the discovery/training dataset and **GSE77298** exclusively as the independent external validation dataset.
2. **Network Pharmacology:** Extracted standardized biological targets from the Reactome database. Integrated differential expression results with STRING PPI networks and applied the Betweenness Centrality algorithm via `networkx` to isolate the top 15 fundamental bottlenecks (Hubs).
3. **Machine Learning Benchmarking:** Evaluated Random Forest, SVM, and XGBoost classifiers equipped with K-Fold Cross-Validation on the 15 candidate features. The optimal model was directly tested on the external dataset (GSE77298) to confirm true biological validity without synthetic batch-effect merging.
4. **Reverse Signature Analysis:** Queried the validated upregulated and downregulated checkpoints through the L1000CDS2 database to identify top drug candidates capable of inducing resolution-promoting phenotypic shifts.

## Repository Structure
To ensure full reproducibility and transparent evaluation, this repository is structured as follows:
* **`Data/`**: Contains the processed expression matrices and clinical metadata for both the discovery and external validation cohorts.
* **`Notebooks/`**: Houses the primary Jupyter Notebook (Google Colab compatible) containing the end-to-end Python pipeline.
* **`Results/`**: Stores high-resolution statistical visualizations, including PCA plots, Volcano plots, and Clustered Heatmaps.
* **`Root Directory`**: Contains the `app.py` script, `requirements.txt`, and result matrices (`.csv`) driving the interactive web application.

## Interactive Dashboard
The results of this study have been deployed as a lightweight, interactive web application via **Streamlit Community Cloud**. The dashboard allows stakeholders and peer reviewers to dynamically explore the network centralities of the therapeutic checkpoints and the final proposed resolution-promoting drugs.

🔗 **Live Dashboard Access:** [https://ml-driven-ra-drug-repurposing.streamlit.app/](https://ml-driven-ra-drug-repurposing.streamlit.app/)

```
