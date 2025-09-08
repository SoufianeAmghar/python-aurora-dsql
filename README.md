# python-aurora-dsql

A Python API project to connect to an Aurora DSQL Cluster, designed to test and measure load performance when deployed across multiple AWS regions.

---

## Overview

This project enables seamless programmatic connections to Amazon Aurora Distributed SQL (DSQL) clusters and runs complex query load tests to analyze database performance and scalability across different AWS regions.

---

## Features

- Connect securely to Aurora DSQL clusters using AWS IAM authentication tokens.
- Execute complex queries and load tests to benchmark cluster performance.
- Supports multi-region deployments for global-scale testing.
- Containerized with Docker and orchestrated with Docker Compose.

---

## Prerequisites

- AWS credentials with appropriate IAM permissions.
- Aurora DSQL cluster endpoint and region information.
- Docker and Docker Compose installed on your local machine.

---

## Setup

1. Clone the repository:

2. Update environment variables with your specific AWS credentials and Aurora cluster details:
- `AWS_REGION`
- `DB_HOSTNAME`
- `DB_USERNAME`
- Any other needed config.

3. Build and run the services using Docker Compose:


---

## Usage

- The `connection-service` handles creating database connections.
- The `load-service` runs load testing queries against the Aurora DSQL clusters.
- Monitor logs for load test progress and results.

---

## Technologies

- Python 3.12
- psycopg2 (PostgreSQL driver)
- AWS CLI (for generating IAM database auth tokens)
- Docker and Docker Compose

---

## License

This project is licensed under the MIT License.

---
