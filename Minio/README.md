# MinIO Docker Setup

This directory contains a Docker Compose configuration to run MinIO object storage.

## Quick Start

1. **Create data directory:**
   ```bash
   mkdir data
   ```

2. **Start MinIO:**
   ```bash
   docker-compose up -d
   ```

3. **Access MinIO:**
   - **API Endpoint:** http://localhost:9000
   - **Console (Web UI):** http://localhost:9001
   - **Username:** minioadmin
   - **Password:** minioadmin123

4. **Stop MinIO:**
   ```bash
   docker-compose down
   ```

## Configuration

The Docker Compose file includes:
- MinIO server running on port 9000 (API) and 9001 (Console)
- Local folder binding (`./data:/data`) for direct host access
- Health checks to ensure the service is running
- Auto-restart policy

## Default Credentials

- **Root User:** minioadmin
- **Root Password:** minioadmin123

⚠️ **Security Note:** Change these default credentials in production environments!

## Data Persistence

Data is stored in the local `data` folder, which is bound to `/data` inside the container. This means:

- ✅ You can directly access files in the `data` folder on your host
- ✅ Easy to backup by copying the `data` folder
- ✅ You can see what MinIO is storing
- ✅ Easy to share data between host and container

To completely remove all data:
```bash
rm -rf data
```

## Useful Commands

- View logs: `docker-compose logs -f minio`
- Check status: `docker-compose ps`
- Restart service: `docker-compose restart minio`
