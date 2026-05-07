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

The goal is to identify suspicious network behavior without supervised labels.

---

## Dataset

Dataset used:

- CICIDS2017
- DDoS-Friday network traffic data

The dataset contains flow-based network traffic features representing benign and malicious behavior.

---

## Technologies Used

- Python
- pandas
- scikit-learn
- matplotlib
- PyTorch
- Jupyter Notebook

---

## Project Structure

```text
network-anomaly-detection/
│
├── data/
├── notebooks/
├── results/
│   └── plots/
├── src/
│   ├── preprocess.py
│   ├── dbscan_model.py
│   └── visualize.py
│
├── main.py
├── requirements.txt
└── README.md