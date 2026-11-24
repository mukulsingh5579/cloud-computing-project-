# Cost Optimization Report

Student: Mukul Singh
Roll Number: 2410030823
University: IILM University

## Technique 1: Lightweight container images
Use slim base images and remove unnecessary packages.
Measure image size before and after rebuilding.

## Technique 2: Resource requests and limits
Set CPU and memory requests based on measured workload.
Compare allocated and consumed resources.

## Technique 3: Horizontal autoscaling
Use HPA to adjust application replicas based on CPU demand.
Compare replica counts and resource consumption under the same workload.

## Measurement worksheet

| Metric | Before | After |
|---|---|---|
| Image size (MB) | Enter measured value | Enter measured value |
| CPU usage (millicores) | Enter measured value | Enter measured value |
| Memory usage (MiB) | Enter measured value | Enter measured value |
| Replicas | Enter measured value | Enter measured value |
| Monthly estimated cost | Enter measured value | Enter measured value |

Do not report estimated savings as measured savings.
Use the same workload and observation period for fair comparison.
For a local Minikube cluster, report resource usage rather than claiming
a real cloud billing reduction.
