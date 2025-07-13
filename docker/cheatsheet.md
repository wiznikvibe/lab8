# Docker Cheatsheet for Data Scientists

## Table of Contents
1. [Docker Basics](#docker-basics)
2. [Core Commands](#core-commands)
3. [Images & Containers](#images--containers)
4. [Dockerfile Essentials](#dockerfile-essentials)
5. [Data Science Workflows](#data-science-workflows)
6. [Volume Management](#volume-management)
7. [Networking](#networking)
8. [Docker Compose](#docker-compose)
9. [Best Practices](#best-practices)
10. [Common Data Science Images](#common-data-science-images)
11. [Troubleshooting](#troubleshooting)

## Docker Basics

### What is Docker?
Docker is a containerization platform that packages applications and their dependencies into lightweight, portable containers. For data scientists, it ensures reproducible environments across different machines and teams.

### Key Concepts
- **Image**: A read-only template used to create containers
- **Container**: A running instance of an image
- **Dockerfile**: A text file containing instructions to build an image
- **Volume**: Persistent storage that survives container restarts
- **Port**: Network endpoint for communication

## Core Commands

### Installation & Setup
```bash
# Check Docker version
docker --version

# Test Docker installation
docker run hello-world

# View system information
docker info

# Login to Docker Hub
docker login
```

### Basic Container Operations
```bash
# Run a container
docker run <image>

# Run container in background (detached)
docker run -d <image>

# Run container interactively
docker run -it <image> bash

# Run with custom name
docker run --name my-container <image>

# Run with port mapping
docker run -p 8888:8888 <image>

# Run with volume mounting
docker run -v /host/path:/container/path <image>
```

### Container Management
```bash
# List running containers
docker ps

# List all containers (including stopped)
docker ps -a

# Stop a container
docker stop <container_id>

# Start a stopped container
docker start <container_id>

# Restart a container
docker restart <container_id>

# Remove a container
docker rm <container_id>

# Remove all stopped containers
docker container prune
```

### Container Interaction
```bash
# Execute command in running container
docker exec <container_id> <command>

# Open interactive shell in running container
docker exec -it <container_id> bash

# View container logs
docker logs <container_id>

# Follow logs in real-time
docker logs -f <container_id>

# Copy files to/from container
docker cp <container_id>:/path/to/file /host/path
docker cp /host/path <container_id>:/path/to/file
```

## Images & Containers

### Image Management
```bash
# List local images
docker images

# Pull an image from Docker Hub
docker pull <image>:<tag>

# Build image from Dockerfile
docker build -t <image_name> .

# Build with custom Dockerfile
docker build -f Dockerfile.custom -t <image_name> .

# Remove an image
docker rmi <image_id>

# Remove unused images
docker image prune

# Tag an image
docker tag <image_id> <new_name>:<tag>

# Push image to registry
docker push <image_name>:<tag>
```

### Image Information
```bash
# Show image details
docker inspect <image_id>

# Show image history
docker history <image_id>

# Show image layers
docker image inspect <image_id>
```

## Dockerfile Essentials

### Basic Dockerfile Structure
```dockerfile
# Use official base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONPATH=/app
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (for better caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 8888

# Set default command
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--no-browser", "--allow-root"]
```

### Common Dockerfile Instructions
```dockerfile
# Base image
FROM ubuntu:20.04

# Maintainer information
LABEL maintainer="your-email@example.com"

# Environment variables
ENV VAR_NAME=value

# Run commands
RUN apt-get update && apt-get install -y package

# Copy files
COPY source destination
ADD source destination  # Also supports URLs and tar extraction

# Set working directory
WORKDIR /path/to/directory

# Expose ports
EXPOSE 8080

# Create volumes
VOLUME ["/data"]

# Set user
USER username

# Entry point (always executed)
ENTRYPOINT ["executable", "param1"]

# Default command (can be overridden)
CMD ["param1", "param2"]
```

## Data Science Workflows

### Jupyter Notebook Setup
```bash
# Run Jupyter notebook
docker run -p 8888:8888 -v $(pwd):/home/jovyan/work jupyter/scipy-notebook

# Custom Jupyter with specific Python version
docker run -p 8888:8888 -v $(pwd):/home/jovyan/work jupyter/tensorflow-notebook

# Jupyter with GPU support
docker run --gpus all -p 8888:8888 -v $(pwd):/tf/notebooks tensorflow/tensorflow:latest-gpu-jupyter
```

### Data Science Dockerfile Example
```dockerfile
FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install additional data science packages
RUN pip install \
    pandas \
    numpy \
    scikit-learn \
    matplotlib \
    seaborn \
    jupyter \
    plotly \
    streamlit

# Copy source code
COPY . .

# Create data directory
RUN mkdir -p /app/data

# Expose ports for Jupyter and Streamlit
EXPOSE 8888 8501

# Default command
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--no-browser", "--allow-root"]
```

### Machine Learning Model Serving
```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy model and serving script
COPY model/ ./model/
COPY serve.py .

# Expose port
EXPOSE 5000

# Run serving script
CMD ["python", "serve.py"]
```

## Volume Management

### Types of Volumes
```bash
# Named volume
docker volume create my-data-volume
docker run -v my-data-volume:/data <image>

# Bind mount (host directory)
docker run -v /host/path:/container/path <image>

# Anonymous volume
docker run -v /container/path <image>
```

### Volume Commands
```bash
# List volumes
docker volume ls

# Inspect volume
docker volume inspect <volume_name>

# Remove volume
docker volume rm <volume_name>

# Remove unused volumes
docker volume prune
```

### Data Science Volume Examples
```bash
# Mount datasets directory
docker run -v /home/user/datasets:/data <image>

# Mount notebooks directory
docker run -v $(pwd)/notebooks:/notebooks <image>

# Mount multiple directories
docker run \
  -v $(pwd)/data:/data \
  -v $(pwd)/notebooks:/notebooks \
  -v $(pwd)/models:/models \
  <image>
```

## Networking

### Basic Networking
```bash
# List networks
docker network ls

# Create network
docker network create <network_name>

# Connect container to network
docker network connect <network_name> <container_name>

# Run container on specific network
docker run --network <network_name> <image>
```

### Port Mapping
```bash
# Map single port
docker run -p 8888:8888 <image>

# Map multiple ports
docker run -p 8888:8888 -p 5000:5000 <image>

# Map to random host port
docker run -P <image>

# Map to specific host interface
docker run -p 127.0.0.1:8888:8888 <image>
```

## Docker Compose

### Basic docker-compose.yml
```yaml
version: '3.8'

services:
  jupyter:
    image: jupyter/scipy-notebook
    ports:
      - "8888:8888"
    volumes:
      - ./notebooks:/home/jovyan/work
    environment:
      - JUPYTER_ENABLE_LAB=yes

  postgres:
    image: postgres:13
    environment:
      - POSTGRES_DB=datadb
      - POSTGRES_USER=datauser
      - POSTGRES_PASSWORD=datapass
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

volumes:
  postgres_data:
```

### Advanced Data Science Stack
```yaml
version: '3.8'

services:
  jupyter:
    build: .
    ports:
      - "8888:8888"
    volumes:
      - ./notebooks:/app/notebooks
      - ./data:/app/data
    environment:
      - JUPYTER_ENABLE_LAB=yes
    depends_on:
      - postgres
      - redis

  postgres:
    image: postgres:13
    environment:
      - POSTGRES_DB=ml_db
      - POSTGRES_USER=ml_user
      - POSTGRES_PASSWORD=ml_pass
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:alpine
    ports:
      - "6379:6379"

  mlflow:
    image: python:3.9
    command: >
      bash -c "pip install mlflow psycopg2-binary &&
               mlflow server --host 0.0.0.0 --port 5000 
               --backend-store-uri postgresql://ml_user:ml_pass@postgres/ml_db"
    ports:
      - "5000:5000"
    depends_on:
      - postgres

volumes:
  postgres_data:
```

### Docker Compose Commands
```bash
# Start services
docker-compose up

# Start in background
docker-compose up -d

# Stop services
docker-compose down

# View logs
docker-compose logs

# Scale services
docker-compose scale jupyter=3

# Build services
docker-compose build

# Pull latest images
docker-compose pull
```

## Best Practices

### Security
```dockerfile
# Use non-root user
RUN useradd -m -u 1000 datauser
USER datauser

# Use specific image tags
FROM python:3.9.7-slim

# Remove package manager cache
RUN apt-get update && apt-get install -y package \
    && rm -rf /var/lib/apt/lists/*
```

### Performance
```dockerfile
# Use multi-stage builds
FROM python:3.9 AS builder
COPY requirements.txt .
RUN pip install --user -r requirements.txt

FROM python:3.9-slim
COPY --from=builder /root/.local /root/.local
```

### Caching
```dockerfile
# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy code last
COPY . .
```

### Environment Variables
```bash
# Use .env file
docker run --env-file .env <image>

# Set environment variables
docker run -e ENVIRONMENT=production <image>
```

## Common Data Science Images

### Official Images
- `python:3.9-slim` - Minimal Python
- `jupyter/scipy-notebook` - Jupyter with scientific packages
- `jupyter/tensorflow-notebook` - Jupyter with TensorFlow
- `jupyter/pyspark-notebook` - Jupyter with PySpark
- `rocker/rstudio` - RStudio Server

### Machine Learning Images
- `tensorflow/tensorflow:latest-gpu` - TensorFlow with GPU
- `pytorch/pytorch:latest` - PyTorch
- `huggingface/transformers-pytorch-gpu` - Transformers with GPU
- `continuumio/anaconda3` - Anaconda distribution

### Database Images
- `postgres:13` - PostgreSQL
- `mysql:8.0` - MySQL
- `mongo:latest` - MongoDB
- `redis:alpine` - Redis

### Big Data Images
- `apache/spark:latest` - Apache Spark
- `apache/airflow:latest` - Apache Airflow
- `elasticsearch:7.15.0` - Elasticsearch

## Troubleshooting

### Common Issues

#### Container Won't Start
```bash
# Check logs
docker logs <container_id>

# Run interactively to debug
docker run -it <image> bash

# Check if port is already in use
netstat -tlnp | grep 8888
```

#### Permission Issues
```bash
# Fix volume permissions
sudo chown -R $(id -u):$(id -g) /path/to/volume

# Run as current user
docker run --user $(id -u):$(id -g) <image>
```

#### Out of Space
```bash
# Remove unused containers
docker container prune

# Remove unused images
docker image prune

# Remove unused volumes
docker volume prune

# Remove everything unused
docker system prune -a
```

#### Memory Issues
```bash
# Check container resource usage
docker stats

# Limit container memory
docker run -m 2g <image>

# Limit CPU
docker run --cpus="1.5" <image>
```

### Debugging Commands
```bash
# Inspect container
docker inspect <container_id>

# Check container processes
docker exec <container_id> ps aux

# Check container environment
docker exec <container_id> env

# Check container filesystem
docker exec <container_id> df -h

# Monitor container stats
docker stats <container_id>
```

### Useful Aliases
```bash
# Add to ~/.bashrc or ~/.zshrc
alias dps='docker ps'
alias dpa='docker ps -a'
alias di='docker images'
alias dex='docker exec -it'
alias dlog='docker logs'
alias dstop='docker stop $(docker ps -q)'
alias dclean='docker system prune -f'
```

## Quick Reference

### Essential Commands for Data Scientists
```bash
# Quick Jupyter setup
docker run -p 8888:8888 -v $(pwd):/home/jovyan/work jupyter/scipy-notebook

# Quick Python environment
docker run -it --rm -v $(pwd):/app -w /app python:3.9 python script.py

# Quick database
docker run -d -p 5432:5432 -e POSTGRES_PASSWORD=password postgres

# Quick Redis cache
docker run -d -p 6379:6379 redis

# Build and run custom image
docker build -t my-ds-project . && docker run -p 8888:8888 my-ds-project
```

### Environment Variables for Data Science
```bash
# Jupyter
JUPYTER_ENABLE_LAB=yes
JUPYTER_TOKEN=your_token

# Python
PYTHONPATH=/app
PYTHONUNBUFFERED=1

# Database
DATABASE_URL=postgresql://user:pass@host:port/db
REDIS_URL=redis://host:port

# ML
CUDA_VISIBLE_DEVICES=0,1
MLFLOW_TRACKING_URI=http://localhost:5000
```

This cheatsheet covers the essential Docker knowledge for data scientists, from basic container operations to advanced multi-service deployments. Practice these commands and gradually build more complex workflows as you become comfortable with Docker's capabilities.