# Opty - Orchestration

This repository contains the Docker Compose configuration to orchestrate the infrastructure and services of the Opty application.

## Prerequisites

Before starting, make sure you have installed:

- [Docker](https://docs.docker.com/get-docker/) (version 20.10 or higher)
- [Docker Compose](https://docs.docker.com/compose/install/) (version 2.0 or higher)

Verify installations:
```bash
docker --version
docker compose version
```

## Configuration

### 1. Clone the Repository

```bash
git clone <repository-url>
cd opty-orchestration
```

### 2. Configure Environment Variables

Create a `.env` file based on `.env.example`:

```bash
cp .env.example .env
```

Edit the `.env` file and configure the variables:

## Running the Project

### Production Mode

To run in production mode:

```bash
docker compose up -d
```

Useful commands:
```bash
# View logs from all services
docker compose logs -f

# View logs from a specific service
docker compose logs -f socket-backend

# View container status
docker compose ps

# Stop all services
docker compose down
```

### Development Mode

For development, use the following command:

```bash
docker compose -f docker-compose.yml -f docker-compose-dev.yml up -d
```

In development mode, the following ports will be accessible:
- **MongoDB**: `localhost:27017`
- **Socket Backend**: `localhost:8080`

This allows you to connect local tools directly to the services.

### Rebuild Services

If there are changes to images or you need to force a rebuild:

```bash
# Production
docker compose up -d --build

# Development
docker compose -f docker-compose.yml -f docker-compose-dev.yml up -d --build
```
