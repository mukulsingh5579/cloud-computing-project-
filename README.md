# Mukul Singh - Cloud Computing Project

Roll Number: 2410030823
University: IILM University

Project: Flask + Redis Visitor Counter on Docker and Kubernetes.

## Local Docker run
Install Docker Desktop, then run:

    docker compose up --build

Open http://localhost:5000

## Kubernetes overview
Enable Minikube and Metrics Server, build the image in the Minikube
Docker environment, then apply the manifests in the kubernetes folder.

The HPA requires working Kubernetes resource metrics.

## Project contents
- app: Flask source
- kubernetes: Deployment, Service, Redis and HPA
- hybrid-cloud: primary and secondary templates
- cost-optimization: measurement worksheet
- documentation: project report
- research-paper: separate research paper

See documentation and hybrid-cloud guides before deployment.
Actual screenshots and measurements must be collected from real tests.
