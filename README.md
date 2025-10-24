# 🎯 Anime Recommendation System - MLOps

## 📖 Project Overview
This project implements a **Hybrid Anime Recommendation System** using **Deep Learning**, combining **collaborative filtering** and **content-based filtering** for accurate and personalized anime recommendations. Users interact via a **Flask web interface** built with HTML and CSS.

The project demonstrates end-to-end **MLOps practices**, including:

- 🧪 **Experiment tracking** with Comet-ML  
- 📦 **Data versioning** with DVC  
- 🐳 **Containerized deployment** with Docker  
- 🔄 **CI/CD pipelines** using Jenkins and Docker-in-Docker  
- ☁️ **Cloud deployment** on **GCP Kubernetes** with GCR and Buckets  

---

## ✨ Features
- 🤝 Hybrid recommendation engine for improved accuracy  
- 🧠 Deep learning-based models for collaborative and content-based filtering  
- 🌐 Flask web app interface with interactive search and recommendations  
- 📊 Comet-ML integration for experiment tracking (parameters, metrics, artifacts)  
- 💾 DVC for dataset, preprocessing, and model artifact versioning  
- 🐳 Dockerized deployment with Jenkins CI/CD pipelines  
- ☁️ Scalable deployment on GCP Kubernetes cluster  
- 🔒 Secure storage using GCP Buckets and IAM roles  

---


## 📁 Folder Structure
```
.
├── artifacts/                 # DVC-tracked data and model artifacts
├── config/                    # YAML config files and paths
├── custom_jenkins/            # Jenkins Dockerfile for CI/CD
├── pipeline/                  # Training & prediction pipelines
├── src/                       # Core Python modules (ingestion, processing, training)
├── static/                    # CSS files for Flask app
├── templates/                 # HTML templates for Flask app
├── application.py             # Flask app entrypoint
├── Dockerfile                 # Dockerfile for Flask deployment
├── Jenkinsfile                # Jenkins CI/CD pipeline
├── deployment.yaml            # Kubernetes deployment configuration
├── requirements.txt           # Python dependencies
├── setup.py                   # Package setup
├── tester.py                  # Testing scripts
└── README.md                  # Project documentation
```

## 🛠 Tech Stack

- Programming & ML: Python, NumPy, Pandas, PyTorch/TensorFlow, Scikit-Learn
- Web Framework: Flask, HTML, CSS
- Experiment Tracking: Comet-ML 🧪
- Data Versioning: DVC 💾
- Containerization & CI/CD: Docker 🐳, Docker-in-Docker, Jenkins 🔄
- Cloud & Deployment: GCP ☁️, Kubernetes, GCR, Buckets, IAM 🔒
- Version Control: Git/GitHub

## ⚡ Setup & Installation

### 1. Clone the repository
```bash
git clone <repo-url>
cd Anime-Recommendation-System-MLOps
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Set up GCP credentials
```bash
export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/service-account.json"
```
### 4. Set up Comet-ML
```bash
export COMET_API_KEY="your-comet-api-key"
export COMET_PROJECT_NAME="anime-recommender"
export COMET_WORKSPACE="your-workspace"
```
### 5. Initialize DVC and pull data
```bash
dvc pull
```
### 6. Run Flask app locally

```bash
python application.py
```
### 7. Build Docker image
```bash
docker build -t anime-recommender .
```
### 8. Deploy on GCP Kubernetes
```bash
kubectl apply -f deployment.yaml
```
## 🔄 Pipeline Overview

- 💾 Data Ingestion: Pull anime datasets from GCP Buckets
- 🧹 Data Processing: Clean and preprocess data for training
- 🧠 Model Training: Hybrid deep learning recommendation model with Comet-ML logging
- 📊 Experiment Tracking: Hyperparameters, metrics, and artifacts logged in Comet-ML dashboard
- 🏷 Model Versioning: DVC tracks model weights and artifacts
- 🌐 Prediction Pipeline: Serves personalized recommendations via Flask API

## 🚀 CI/CD Workflow
1. Jenkins triggers on push to GitHub repository
2. Builds Docker image using Docker-in-Docker setup
3. Pushes image to GCR
4. Deploys updated image to GCP Kubernetes cluster

## 💾 DVC & Data Management
- All datasets, processed data, and model artifacts are tracked with DVC
- Remote storage uses GCP Buckets
- Reproducibility: All experiments can be reproduced with exact datasets, model weights, and tracked configurations in Comet-ML

## 🔮 Future Improvements
- Real-time streaming recommendations ⚡
- User feedback loop for continuous learning 🔄
- Enhanced model explainability for personalized insights 🧩
- Kubernetes autoscaling for high traffic ☁️

## 👤 Authors & Contributors

- Subrat Mishra – Data Scientist & AI Engineer
- Portfolio: mishra-subrat.netlify.app

## 🔗 Useful-Links
- [Comet-ML Experiment Dashboard](https://www.comet.com/subrat1920/recommendation-system-experiment/view/new/panels)
- [Dagshub-Pipeline Orchestration](https://dagshub.com/Subrat1920/Anime-Recommendation-System-MLOps?filter=dvc)