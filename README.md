# Network Traffic Anomaly Detection using Unsupervised Learning

## Overview

This project implements an unsupervised machine learning pipeline for detecting anomalous network traffic using the CICIDS2017 intrusion detection dataset.

The pipeline includes:

- Data preprocessing
- Feature scaling
- Exploratory data analysis
- PCA dimensionality reduction
- DBSCAN clustering
- Anomaly visualization

The objective is to identify suspicious network behavior without relying on supervised labels.

---

## Dataset

Dataset used:

- CICIDS2017
- DDoS-Friday network traffic flow data

The dataset contains flow-based network traffic features representing both benign and malicious activity.

---

## Technologies Used

- Python
- pandas
- NumPy
- scikit-learn
- matplotlib
- Jupyter Notebook

---

## Project Structure

```text
network-anomaly-detection/
│
├── assets/
│   └── dbscan_pca.png
│
├── data/
│
├── notebooks/
│   └── eda.ipynb
│
├── results/
│   ├── anomaly_results.csv
│   └── plots/
│       └── dbscan_pca.png
│
├── src/
│   ├── preprocess.py
│   ├── dbscan_model.py
│   └── visualize.py
│
├── .gitignore
├── README.md
├── main.py
└── requirements.txt
