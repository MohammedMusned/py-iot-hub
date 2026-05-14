# Project Describtion

This project is part of the **Back-End Developer Interview Test**.  
The goal is to create project simulates a simple IoT data management system.
It includes a front-end (for interaction), an API (for data management), a PostgreSQL database (for persistence), and a background service (to handle incoming telemetry data).
A device emulator will simulate real IoT devices sending telemetry data.

All details are provide in [PROJECT GUIDELINE](DOC/PROJECT_GUIDELINE.md).

---

## How to Run

Follow these steps to run the complete environment using Docker.

### 1. Setup Environment Variables
First, create your local configuration by copying the example file:
```bash
cp .env.example .env
```
*(You can leave the default values as they match the Docker setup).*

### 2. Start All Services
Build and start all services (PostgreSQL, MQTT Broker, Flask API, and Device Emulator):
```bash
docker-compose up -d --build
```

This single command starts:
- **PostgreSQL** database on port `5432`
- **Eclipse Mosquitto** MQTT broker on port `1883`
- **Flask API** on port `5000`
- **Device Emulator** that sends simulated telemetry data

Your API will now be available at `http://localhost:5000`.

To stop all services:
```bash
docker-compose down
```

## Documentation & Architecture

I've put together some docs and diagrams to give a better idea of how everything is structured under the hood. Check them out below:

- **[API Reference](api-list.md)**: A straightforward list of the available API endpoints.
- **[System Diagram](System_diagram.drawio.png)**: A high-level look at how the different components talk to each other.
- **[Database ERD](ER_diagram.drawio.png)**: Shows the layout of our database tables.
