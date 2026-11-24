# Hybrid Cloud Failover Design

## Primary environment
The primary Kubernetes cluster hosts the Flask application and Redis.

## Secondary environment
A separately provisioned Kubernetes cluster hosts backup application replicas and a secondary data service.

## Failover procedure
1. Monitor primary application health.
2. Detect primary endpoint failure.
3. Confirm secondary application and database health.
4. Redirect DNS or load-balancer traffic to the secondary endpoint.
5. Verify application response.
6. Restore primary service after investigation.

## Important
The supplied manifests are deployment templates, not an automatically
configured cross-cloud failover system. DNS/load-balancer automation,
database replication, secrets, TLS and independent clusters must be
configured and tested before production failover.

Independent Redis instances do not synchronize visitor counts.
A tested replication or shared data architecture is required.
