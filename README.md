# ChaosForge

ChaosForge is a chaos engineering and observability simulation platform built using Python and Flask.

The goal of the project is to intentionally simulate production failures such as application crashes, latency spikes, CPU exhaustion, and memory leaks in order to test monitoring, alerting, resilience, and GitOps workflows using production-grade DevOps tooling.

Instead of building a feature-heavy application, ChaosForge focuses on operational engineering concepts used by SREs and DevOps engineers in real-world distributed systems.

---

# Project Goals

ChaosForge is designed to demonstrate:

- Failure simulation
- Application observability
- Infrastructure resilience
- Monitoring and alerting
- Chaos engineering concepts
- GitOps deployment workflows
- Kubernetes self-healing behavior
- Production-grade DevOps practices

---

# Current Features

## Healthy Endpoint

Simulates a healthy production service.

### Endpoint
```http
GET /success
```

### Response
```json
{
  "status": "success",
  "message": "ChaosForge healthy"
}
```

---

## Failure Toggle Endpoint

Enables or disables application-wide failure mode.

When enabled:
- `/success` returns HTTP 500
- error metrics increase
- logs emit critical failures

### Endpoint
```http
POST /toggle-error
```

### Response
```json
{
  "status": "success",
  "error_mode": true,
  "message": "Chaos mode toggled"
}
```

---

## Slow Response Simulation

Introduces artificial latency using `time.sleep()`.

Used for:
- latency monitoring
- p95/p99 visualization
- SLO/SLA simulations

### Endpoint
```http
GET /slow-down
```

### Response
```json
{
  "status": "slow",
  "message": "Response delayed intentionally by 5 seconds"
}
```

---

## Health Check Endpoint

Used for:
- liveness probes
- readiness probes
- service monitoring

### Endpoint
```http
GET /health
```

### Healthy Response
```json
{
  "status": "UP",
  "message": "Application healthy"
}
```

### Failure Response
```json
{
  "status": "DOWN",
  "message": "Chaos mode active"
}
```

---

## Metrics Endpoint

Exposes Prometheus-compatible metrics for observability.

### Endpoint
```http
GET /metrics
```

### Exposed Metrics
- request count
- error count
- request latency
- CPU chaos events
- memory chaos events

---

## CPU Burn Simulation

Artificially generates high CPU utilization.

Used for:
- Kubernetes autoscaling demonstrations
- resource monitoring
- CPU alert simulations

### Endpoint
```http
POST /cpu-burn
```

### Response
```json
{
  "status": "success",
  "message": "CPU burn simulation completed"
}
```

---

## Memory Leak Simulation

Artificially increases memory consumption by retaining allocated memory references.

Used for:
- OOMKilled demonstrations
- memory pressure testing
- memory alert simulations

### Endpoint
```http
POST /memory-leak
```

### Response
```json
{
  "status": "warning",
  "message": "Memory leak simulated",
  "allocations": 1
}
```

---

# Project Architecture

```text
chaosforge/
├── .github/workflows
│       └── chaos_controller.py
├── app/
│   ├── controllers/
│   │   └── chaos_controller.py
│   │
│   ├── services/
│   │   └── chaos_service.py
│   │
│   ├── metrics/
│   │   └── prometheus_metrics.py
│   │
│   ├── models/
│   │   └── state.py
│   │
│   ├── utils/
│   │   ├── cpu_stress.py
│   │   └── memory_stress.py
│   │   └── metrics.py
│   └── app.py
├── Dockerfile
├── docker-compose.yaml
├── .dockerignore
├── k8s/
├── requirements.txt
├── Makefile
├── .gitignore
└── README.md
```

---

# Technology Stack

## Backend
- Python
- Flask

## Observability
- Prometheus Client Library

## Chaos Engineering
- CPU stress simulation
- Memory leak simulation
- Failure injection
- Latency simulation

---

# Metrics Instrumentation

ChaosForge currently exposes:

| Metric | Purpose |
|---|---|
| `chaosforge_requests_total` | Total API requests |
| `chaosforge_errors_total` | Total simulated failures |
| `chaosforge_request_latency_seconds` | Request latency histogram |
| `chaosforge_cpu_burn_total` | CPU chaos simulations |
| `chaosforge_memory_leak_total` | Memory leak simulations |

---

# Running Locally

## Clone Repository

```bash
git clone https://github.com/nsahil992/ChaosForge
cd chaosforge
```

---

## Create Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
make run
```

Application runs on:

```text
http://localhost:5050
```

---

# Example API Calls

## Healthy Request

```bash
curl http://localhost:5050/success
```

---

## Enable Failure Mode

```bash
curl -X POST http://localhost:5050/toggle-error
```

---

## Simulate Slow Response

```bash
curl http://localhost:5050/slow-down
```

---

## Simulate CPU Spike

```bash
curl -X POST http://localhost:5050/cpu-burn
```

---

## Simulate Memory Leak

```bash
curl -X POST http://localhost:5050/memory-leak
```

---

## View Metrics

```bash
curl http://localhost:5050/metrics
```

---

# Makefile Targets

| Target | Description |
|---|---|
| `make run` | Start Flask application |
| `make install` | Install dependencies |
| `make freeze` | Update requirements.txt |

---

# DevOps Stack

The next stages of the project will include:

- Docker
- Docker Compose
- GitHub Actions CI
- Kubernetes
- Helm
- ArgoCD
- Prometheus
- Grafana
- Loki
- Alertmanager
- K6 Load Testing
- Horizontal Pod Autoscaler
- GitOps Deployment Workflow

---

# Production Demonstrations

ChaosForge will eventually demonstrate:

- failure detection
- observability pipelines
- automated alerting
- Kubernetes self-healing
- autoscaling under load
- GitOps reconciliation
- deployment rollback workflows

---

# Development Workflow

This project follows a structured Git branching strategy.

| Branch | Purpose |
|---|---|
| `development` | Application development |
| `feature/docker` | Dockerization |
| `feature/docker-compose` | Docker Compose setup |
| `feature/ci` | GitHub Actions CI workflow |
| `feature/kubernetes` | Kubernetes manifests |
| `feature/helm` | Helm charts |
| `feature/argocd` | GitOps workflows |
| `feature/monitoring` | Prometheus/Grafana/Loki |



---

# Docker

ChaosForge is fully containerized using Docker.

## Build Docker Image

```bash

docker build -t nsahil992/chaosforge:1.0.0 .

```

## Run Container

```bash

docker run -p 5050:5050 nsahil992/chaosforge:1.0.0

```

---

# Docker Optimization

The project uses:

- Multi-stage Docker builds

- Slim Python base image

- Optimized dependency layers

- `.dockerignore`

## Image Size Optimization

| Built Type | Image Size |
|---|---|
| Initial Single Stage Build | 1.65 GB |
| Optimized Multi-Stage Build | 211 MB |


## Reduction Achieved

- Reduced image size by approximately **87.2%**

- Reduced image size by approximately **1.44 GB**

This optimization improves:

- Faster deployments

- Reduced registry storage

- Faster Kubernetes pull times

- Lower infrastructure overhead

---

# Docker Compose

ChaosForge uses Docker Compose for local infrastructure orchestration.

## Start Services

```bash

docker compose up

```

## Run in Detached Mode

```bash

docker compose up -d

```

## Stop Services

```bash

docker compose down

```

---

# GitHub Actions CI Pipeline

ChaosForge uses a self-hosted GitHub Actions runner.

## CI Pipeline Features

- Source checkout
- Python validation
- Docker image build
- Docker image testing
- DockerHub image push
- Branch-based pipeline execution
- Path-based workflow filtering

## Pipeline Triggers

```yaml

push:
  branches:
    - master
    - feature/**

```

---

# Kubernetes Deployment

ChaosForge is deployed on a multi-node Kubernetes cluster using Minikube.

## Kubernetes Features

- Multi-node cluster
- Namespace isolation
- Deployments
- Services
- Liveness probes
- Readiness probes
- Resource limits
- Node labeling
- Workload scheduling

---

# Kubernetes Architecture

| Node | Purpose |
|---|---|
| Node 1 | Application workloads |
| Node 2 | Platform & observability services |

---

# Start Kubernetes Cluster

```bash

minikube start \
  --nodes 2 \
  --cpus 2 \
  --memory 2200 \
  --driver=docker

```

---

# Label Kubernetes Nodes

## Application Node

```bash

kubectl label node minikube type=application

```

## Platform Services Node

```bash

kubectl label node minikube-m02 type=dependent-services

```

---

# Deploy Kubernetes Resources

```bash

kubectl apply -f k8s/

```

---

# Verify Deployment

```bash

kubectl get all -n chaosforge

```

---

# Port Forward Service

```bash

kubectl port-forward svc/chaosforge-service 5050:80 -n chaosforge

```

---
