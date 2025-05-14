# ML CI/CD Pipeline Demo

[![CI Status](https://github.com/Erinliu0819/ml-ci-cd-pipeline-demo/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/Erinliu0819/ml-ci-cd-pipeline-demo/actions)
[![Docker Image](https://img.shields.io/badge/docker-latest-blue)](https://hub.docker.com/r/YourUsername/ml-api)

A fully automated **CI/CD demo** that trains, tests, packages, and deploys a **Random Forest** model on the Iris dataset.

## Features

- **Automated training** of a Random Forest classifier  
- **Unit test** ensuring ≥ 90% accuracy on Iris  
- **Linting** with Pylint for code quality  
- **Model serialization** (`model.joblib`) for fast startup  
- **Dockerized** ML service, pushed to Docker Hub on each commit

