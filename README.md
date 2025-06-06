# 🧱 ECHO Backend

This repository contains the backend infrastructure for the **ECHO** project, deployed using Docker Compose. It includes all the core services required to run the `echo-api`, along with supporting services like MongoDB, MinIO (object storage), and Mongo Express (UI for MongoDB).

## 📦 Services Overview

| Service      | Description                                                     |
|--------------|-----------------------------------------------------------------|
| `mongodb`    | NoSQL database to store structured data                         |
| `mongo-express` | Web interface for managing MongoDB data                    |
| `api`        | FastAPI-based backend server (from [`echosoil/echo-api`](https://github.com/echosoil/echo-api)) |
| `minio`      | S3-compatible object storage for file uploads                   |

## 🐳 Running the Stack

Ensure you have Docker and Docker Compose installed.

```bash
# From inside echo-backend/
docker-compose up -d
```

This starts all services in the background. Access the FastAPI docs at [http://localhost:8000/docs](http://localhost:8000/docs).

## 📁 Volumes

To persist data across container restarts:

| Container     | Host Path             | Purpose                           |
|---------------|------------------------|-----------------------------------|
| `mongodb`     | `./mongodb-data/`      | Stores MongoDB data files         |
| `minio`       | `./minio-data/`        | Stores uploaded objects and files |

Make sure the folders exist or are created automatically on first run.

## ⚙️ Configuration

The containers use environment variables defined in `.env` files. You’ll typically need the following:

- `.env` for Docker Compose credentials
- `.env_keycloak`, `.env_zenodo`, `.env_s3`, `.env_ckan` – copied to the `api` container if needed

You may place these files either in the `echo-api` subdirectory or map them via volumes in Docker if required.

## 📜 Example `.env` for Docker Compose

```dotenv
# .env
MONGO_INITDB_ROOT_USERNAME=admin
MONGO_INITDB_ROOT_PASSWORD=your_password
MINIO_ROOT_USER=minioadmin
MINIO_ROOT_PASSWORD=minioadmin
```

## 🛑 Stopping the Stack

To stop and remove all containers:

```bash
docker-compose down
```

To stop only:

```bash
docker-compose stop
```

## 🧭 Repository Structure

```
echo-backend/
├── docker-compose.yml
├── mongodb-data/          # Persistent DB volume
├── minio-data/            # Persistent object storage
├── .env                   # Common Docker variables
└── echo-api/              # Linked or cloned repo from echosoil/echo-api
```

## 🪪 License

This repository is licensed under the **European Union Public License (EUPL)**.

## 🔗 Related Repositories

- 🔌 [`echosoil/echo-api`](https://github.com/echosoil/echo-api) – the API logic
- 🌱 [ECHO Website](https://echosoil.eu)

---

📬 For technical support, reach out via [GitHub Issues](https://github.com/echosoil/echo-backend/issues) or through your designated project contact.
