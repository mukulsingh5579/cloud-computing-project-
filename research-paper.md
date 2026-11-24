# Containerized Web Application Deployment and Scalability Using Flask, Redis and Kubernetes

**Author:** Mukul Singh
**Roll Number:** 2410030823
**Institution:** IILM University

## Abstract
This paper examines a cloud-native visitor counter application built with
Flask and Redis. It discusses Docker-based packaging, Kubernetes
orchestration, horizontal autoscaling, hybrid cloud resilience and
resource optimization. The work presents an implementation design and
a measurement framework. Performance and cost conclusions require
experimental observations from a deployed environment.

## Keywords
Cloud computing, Docker, Kubernetes, Flask, Redis, HPA, hybrid cloud.

## 1. Introduction
Cloud-native applications use automation, containers and orchestration
to improve deployment consistency and operational flexibility.
A visitor counter provides a small example for studying these concepts.

## 2. Related Technologies
Flask is a Python web framework.
Redis is an in-memory data store.
Docker builds portable container images.
Kubernetes manages containerized workloads and services.
Horizontal Pod Autoscaling adjusts replica counts from observed metrics.

## 3. Proposed Methodology
The application receives browser requests through Flask. Each visit
increments a Redis counter. Docker packages the web application.
Kubernetes deploys the application and database as separate workloads.
HPA monitors CPU utilization and adjusts application replicas.

## 4. Hybrid Cloud Design
A primary cluster handles normal requests while a secondary cluster
provides a recovery environment. DNS or load-balancer traffic redirection
can support failover. Database replication and consistency are essential
because independent Redis databases can diverge.

## 5. Resource Optimization
Three techniques are considered: slim container images, resource
requests and limits, and HPA-based replica adjustment. Measurements
should use consistent workloads and observation periods.

## 6. Evaluation Framework
Evaluation metrics include response time, CPU usage, memory usage,
replica count, image size and application availability. Cost comparisons
must use actual infrastructure pricing and measured resource consumption.

## 7. Limitations
The design does not itself prove production failover or measured cost
savings. These require a deployed secondary cluster, traffic routing,
data replication and recorded experiments.

## 8. Conclusion
Flask, Redis, Docker and Kubernetes provide a useful platform for
studying cloud-native deployment. HPA and hybrid cloud designs can
improve scalability and resilience when correctly configured and tested.

## References
1. Flask Documentation. https://flask.palletsprojects.com/
2. Redis Documentation. https://redis.io/docs/
3. Docker Documentation. https://docs.docker.com/
4. Kubernetes Documentation. https://kubernetes.io/docs/
5. Burns, B. et al. (2016). Borg, Omega, and Kubernetes.
   ACM Queue, 14(1).
6. Kubernetes Horizontal Pod Autoscaling.
   https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/
