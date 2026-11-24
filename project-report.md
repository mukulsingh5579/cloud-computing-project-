# CLOUD COMPUTING PROJECT REPORT

## Deploy a Visitor Counter Web App (Flask + Redis) on Docker and Kubernetes

**Submitted by:** Mukul Singh
**Roll Number:** 2410030823
**University:** IILM University
**Academic Session:** 2026-2027

## Abstract
This project designs a visitor counter application using Flask and Redis.
Docker packages the application, while Kubernetes manages deployment,
services and horizontal scaling. The project also studies hybrid cloud
failover and resource optimization.

## 1. Introduction
Cloud computing provides on-demand computing resources. Container
technology makes applications portable, and orchestration platforms
manage container workloads.

## 2. Objectives
- Develop a Flask visitor counter.
- Store visitor data in Redis.
- Containerize with Docker.
- Deploy on Kubernetes.
- Configure HPA.
- Design hybrid cloud failover.
- Evaluate three optimization techniques.

## 3. Technology Stack
Python, Flask, Redis, Docker, Docker Compose, Kubernetes, Minikube,
kubectl and Metrics Server.

## 4. Architecture
Browser -> Flask application -> Redis.
Docker packages the application.
Kubernetes Deployment manages replicas.
Service exposes the application.
HPA adjusts replicas using CPU metrics.

## 5. Containerization
The Dockerfile installs Python dependencies and runs Gunicorn.
Docker Compose starts Flask and Redis services.

## 6. Kubernetes
Deployment manifests define application replicas, resource requests,
limits, health probes and service discovery.

## 7. HPA
HPA targets 50 percent CPU utilization, with a minimum of two and
maximum of ten application replicas.

## 8. Hybrid Cloud
A primary and a secondary Kubernetes environment are proposed.
Traffic redirection and Redis data consistency require additional
infrastructure and verification.

## 9. Cost Optimization
The project evaluates slim images, resource requests/limits and
demand-based autoscaling. Actual measurements must be entered after tests.

## 10. Testing
Record application health, visitor count, pod status, service access,
HPA metrics and failover observations.

## 11. Results
Insert actual test outputs and screenshots here. No execution results
are claimed by this report until the tests have been performed.

## 12. Conclusion
The project demonstrates a cloud-native application architecture and
explains containerization, orchestration, scaling, resilience and
resource optimization.

## References
1. Flask documentation: https://flask.palletsprojects.com/
2. Redis documentation: https://redis.io/docs/
3. Docker documentation: https://docs.docker.com/
4. Kubernetes documentation: https://kubernetes.io/docs/
5. Kubernetes HPA: https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/
6. Minikube: https://minikube.sigs.k8s.io/docs/
