# ☁️ Cloud Infrastructure Monitor

> Real-time Monitoring & Alerting System built with FastAPI, MySQL, Docker, Kubernetes, and AWS

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110-green)
![Docker](https://img.shields.io/badge/Docker-Containerised-blue)
![Kubernetes](https://img.shields.io/badge/Kubernetes-EKS-orange)
![AWS](https://img.shields.io/badge/AWS-Deployed-yellow)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-black)

---

## 📋 Project Overview

Cloud Infrastructure Monitor is a production-grade microservices application that provides real-time monitoring and alerting for cloud infrastructure. It collects system metrics (CPU, memory, disk), stores them in a MySQL database, and triggers alerts when thresholds are breached.

This project demonstrates a complete end-to-end DevOps lifecycle — from local development to fully automated deployment on AWS using Kubernetes orchestration.

---

## 🛠️ Technology Stack

| Layer            | Technology                 |
| ---------------- | -------------------------- |
| Backend API      | Python 3.11 + FastAPI      |
| Database         | MySQL 8.0 + SQLAlchemy ORM |
| Containerisation | Docker + Docker Compose    |
| Orchestration    | Kubernetes (AWS EKS)       |
| CI/CD Pipeline   | GitHub Actions             |
| Image Registry   | Amazon ECR                 |
| Cloud Provider   | Amazon Web Services (AWS)  |
| Operating System | Linux (Ubuntu)             |

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────┐
│                  GitHub Actions CI/CD                │
│    Push to main → Build → Push ECR → Deploy EKS     │
└────────────────────────┬────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────┐
│                  AWS EKS Cluster                     │
│  ┌─────────────────────────────────────────────┐    │
│  │           Kubernetes Deployment              │    │
│  │   ┌──────────────┐   ┌──────────────────┐   │    │
│  │   │  FastAPI Pod  │   │   FastAPI Pod    │   │    │
│  │   │  (Replica 1) │   │   (Replica 2)   │   │    │
│  │   └──────┬───────┘   └───────┬──────────┘   │    │
│  │          └────────┬──────────┘              │    │
│  │        ┌──────────▼──────────┐              │    │
│  │        │  MySQL Database     │              │    │
│  │        │  (metrics + alerts) │              │    │
│  │        └─────────────────────┘              │    │
│  └─────────────────────────────────────────────┘    │
│                  LoadBalancer Service                │
└─────────────────────────────────────────────────────┘
```

---

## 📁 Project Structure

```
cloud-monitor/
├── app/
│   ├── main.py                  # FastAPI entry point
│   ├── database.py              # DB connection & session
│   ├── models.py                # SQLAlchemy models
│   ├── schemas.py               # Pydantic schemas
│   ├── routers/
│   │   ├── metrics.py           # Metrics API routes
│   │   ├── alerts.py            # Alerts API routes
│   │   └── health.py            # Health check routes
│   └── services/
│       ├── collector.py         # System metric collection
│       └── alerting.py          # Threshold alerting logic
├── kubernetes/
│   ├── deployment.yaml          # K8s deployment manifest
│   ├── service.yaml             # K8s service manifest
│   ├── configmap.yaml           # Environment config
│   └── secret.yaml              # Sensitive credentials
├── .github/
│   └── workflows/
│       └── ci-cd.yml            # GitHub Actions pipeline
├── Dockerfile                   # Container build instructions
├── docker-compose.yml           # Local development setup
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

- [Git](https://git-scm.com)
- [Python 3.11+](https://python.org)
- [Docker Desktop](https://docker.com)
- [AWS CLI](https://aws.amazon.com/cli)
- [kubectl](https://kubernetes.io/docs/tasks/tools)
- [eksctl](https://eksctl.io)

---

### ▶️ Run Locally

**1. Clone the repository**

```bash
git clone https://github.com/YOUR_USERNAME/cloud-monitor.git
cd cloud-monitor
```

**2. Set up Python environment**

```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

**3. Create environment file**

```bash
# Create .env file
echo "DATABASE_URL=mysql+pymysql://root:password@localhost:3306/cloudmonitor" > .env
```

**4. Start with Docker Compose**

```bash
docker-compose up --build
```

**5. Open in browser**

- API Root: http://localhost:8000
- Swagger Docs: http://localhost:8000/docs
- Health Check: http://localhost:8000/health
- System Metrics: http://localhost:8000/health/system

---

## 📡 API Endpoints

| Method | Endpoint                  | Description                  |
| ------ | ------------------------- | ---------------------------- |
| GET    | `/`                       | API status check             |
| GET    | `/health`                 | Health check                 |
| GET    | `/health/system`          | Live CPU, memory, disk usage |
| GET    | `/metrics`                | List all metrics             |
| POST   | `/metrics`                | Submit a new metric          |
| GET    | `/metrics/{service_name}` | Get metrics by service       |
| GET    | `/alerts`                 | List active alerts           |
| POST   | `/alerts`                 | Create a new alert           |
| PUT    | `/alerts/{id}/resolve`    | Resolve an alert             |

---

## 🧪 Example API Calls

**Submit a metric:**

```bash
curl -X POST "http://localhost:8000/metrics" \
  -H "Content-Type: application/json" \
  -d '{"service_name": "web-server", "metric_type": "cpu", "value": 72.5, "unit": "%"}'
```

**Get all metrics:**

```bash
curl http://localhost:8000/metrics
```

**Create an alert:**

```bash
curl -X POST "http://localhost:8000/alerts" \
  -H "Content-Type: application/json" \
  -d '{"service_name": "web-server", "alert_type": "cpu_threshold", "message": "CPU usage critical", "severity": "high"}'
```

**Resolve an alert:**

```bash
curl -X PUT "http://localhost:8000/alerts/1/resolve"
```

---

## 🚨 Alert Thresholds

| Metric | Medium | High | Critical |
| ------ | ------ | ---- | -------- |
| CPU    | 70%    | 85%  | 95%      |
| Memory | 75%    | 88%  | 95%      |
| Disk   | 80%    | 90%  | 95%      |

---

## ☁️ AWS Deployment

### Step 1 — Configure AWS CLI

```bash
aws configure
# Enter: Access Key ID, Secret Key, Region (us-east-1), Output (json)
```

### Step 2 — Create ECR Repository

```bash
aws ecr create-repository \
  --repository-name cloud-monitor \
  --region us-east-1
```

### Step 3 — Build & Push Docker Image

```bash
# Login to ECR
aws ecr get-login-password --region us-east-1 | \
  docker login --username AWS \
  --password-stdin ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com

# Build, tag and push
docker build -t cloud-monitor .
docker tag cloud-monitor:latest ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/cloud-monitor:latest
docker push ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/cloud-monitor:latest
```

### Step 4 — Create EKS Cluster

```bash
eksctl create cluster \
  --name cloud-monitor-cluster \
  --region us-east-1 \
  --nodegroup-name workers \
  --node-type t3.small \
  --nodes 2 \
  --managed
```

### Step 5 — Deploy to Kubernetes

```bash
# Update image URI in kubernetes/deployment.yaml first, then:
kubectl apply -f kubernetes/

# Get public URL
kubectl get service cloud-monitor-service
```

---

## 🔄 CI/CD Pipeline

The GitHub Actions pipeline at `.github/workflows/ci-cd.yml` automatically runs on every push to `main`:

```
Push to main
     │
     ▼
Install Dependencies
     │
     ▼
Build Docker Image
     │
     ▼
Push to Amazon ECR
     │
     ▼
Update kubeconfig for EKS
     │
     ▼
Deploy to Kubernetes ✅
```

### Required GitHub Secrets

Go to: **Settings → Secrets and Variables → Actions**

| Secret Name             | Description                |
| ----------------------- | -------------------------- |
| `AWS_ACCESS_KEY_ID`     | Your AWS access key        |
| `AWS_SECRET_ACCESS_KEY` | Your AWS secret access key |

---

## 💼 DevOps Skills Demonstrated

- ✅ Python backend development with FastAPI
- ✅ REST API design following OpenAPI specification
- ✅ Database schema design with SQLAlchemy ORM
- ✅ Docker containerisation and multi-service Docker Compose
- ✅ Kubernetes Deployments, Services, Secrets, and ConfigMaps
- ✅ CI/CD automation with GitHub Actions
- ✅ AWS ECR image registry management
- ✅ AWS EKS cluster provisioning and management
- ✅ Infrastructure as Code (Kubernetes manifests)
- ✅ Linux-based infrastructure

---

## 🔍 Troubleshooting

| Problem                   | Solution                                 |
| ------------------------- | ---------------------------------------- |
| `docker-compose up` fails | Make sure Docker Desktop is running      |
| Port 8000 in use          | Run `lsof -i :8000` and kill the process |
| MySQL connection refused  | Wait 30s for MySQL to fully start        |
| `kubectl` not found       | Install kubectl and add to PATH          |
| EKS nodes not ready       | Wait 5 more minutes for initialisation   |
| ECR push access denied    | Re-run the ECR login command             |
| GitHub Actions failing    | Check AWS secrets are set correctly      |

---

## 🧹 Cleanup

To avoid unexpected AWS charges on your free tier / credits:

```bash
# Delete EKS cluster
eksctl delete cluster --name cloud-monitor-cluster --region us-east-1

# Delete ECR repository
aws ecr delete-repository --repository-name cloud-monitor --region us-east-1 --force
```

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

> Built by Pramod — DevOps Portfolio Project 2024
