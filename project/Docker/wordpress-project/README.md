# 🐳 Dockerized WordPress Deployment with Docker Compose

A simple **multi-container WordPress deployment** using **Docker Compose**, consisting of:

- 🌐 Nginx (Web Server)
- 🐘 PHP-FPM 8.3
- 🗄️ MySQL 8
- 📦 Docker Volumes for persistent database storage

This project demonstrates how multiple containers communicate together using Docker Compose while keeping each service independent.

---

# 📁 Project Structure

```
wordpress-project/
│
├── docker-compose.yml
│
├── php/
│   └── Dockerfile
│
├── nginx/
│   └── default.conf
│
└── wordpress/
    ├── wp-admin/
    ├── wp-content/
    ├── wp-includes/
    ├── index.php
    └── ...
```

---

# ⚙️ Services

| Service | Image | Purpose |
|----------|-------|----------|
| **Nginx** | nginx | Serves the WordPress website |
| **PHP-FPM** | php:8.3-fpm | Processes PHP files |
| **MySQL** | mysql:8 | Stores WordPress data |

---

# 🧱 Architecture

```
                 Browser
                    │
             http://SERVER_IP:8088
                    │
                    ▼
            +-----------------+
            |      Nginx      |
            +-----------------+
                    │
        FastCGI (Docker Network)
                    │
                    ▼
            +-----------------+
            |    PHP-FPM      |
            +-----------------+
                    │
          MySQL Client Library
                    │
                    ▼
            +-----------------+
            |     MySQL 8     |
            +-----------------+
                    │
             Docker Volume
             (mysql-data)
```

---

# ⚙️ docker-compose.yml Overview

The project uses Docker Compose to orchestrate three containers.

## Nginx

- Exposes port **8088**
- Serves WordPress files
- Passes PHP requests to PHP-FPM

```yaml
ports:
  - "8088:80"
```

---

## PHP

Built from a custom Dockerfile.

### Dockerfile

```dockerfile
FROM php:8.3-fpm

RUN docker-php-ext-install mysqli pdo pdo_mysql
```

Installed PHP extensions:

- mysqli
- PDO
- PDO MySQL

---

## MySQL

Uses the official MySQL 8 image.

Configured using environment variables.

```yaml
MYSQL_ROOT_PASSWORD
MYSQL_DATABASE
MYSQL_USER
MYSQL_PASSWORD
```

Database data is stored inside a Docker named volume.

---

# 🚀 Getting Started

## Clone Repository

```bash
git clone https://github.com/<your-username>/<repo-name>.git

cd wordpress-project
```

---

## Start Containers

```bash
docker compose up -d
```

---

## Verify Running Containers

```bash
docker compose ps
```

Example

```
NAME        IMAGE                   STATUS
php-nginx   nginx                   Up
php-fpm     wordpress-project-php   Up
mysql-db    mysql:8                 Up
```

---

## Access Website

Open your browser.

```
http://SERVER_IP:8088
```

or locally

```
http://localhost:8088
```

---

# 📂 Volumes

A Docker named volume stores MySQL data.

```
mysql-data
```

This prevents database loss when containers are recreated.

---

# 🌐 Networking

Docker Compose automatically creates an isolated network.

Containers communicate internally using service names.

Example:

```
fastcgi_pass php:9000;
```

No IP addresses are required.

---

# 📜 Nginx Configuration

The Nginx server is configured using

```
nginx/default.conf
```

Important directives:

```nginx
root /var/www/html;

index index.php index.html;

try_files $uri $uri/ /index.php?$query_string;

fastcgi_pass php:9000;
```

---

# 🛠 Commands Used

Start containers

```bash
docker compose up -d
```

Stop containers

```bash
docker compose down
```

Restart

```bash
docker compose restart
```

View running containers

```bash
docker compose ps
```

View logs

```bash
docker compose logs

docker compose logs nginx

docker compose logs php

docker compose logs mysql
```

Execute shell inside container

```bash
docker exec -it php-nginx bash

docker exec -it php-fpm bash

docker exec -it mysql-db bash
```

List Docker volumes

```bash
docker volume ls
```

Inspect Docker network

```bash
docker network ls

docker network inspect wordpress-project_default
```

---

# 🧠 Docker Concepts Demonstrated

✅ Docker Images

✅ Docker Containers

✅ Docker Compose

✅ Multi-container Applications

✅ Docker Networking

✅ Named Volumes

✅ Bind Mounts

✅ Custom Dockerfile

✅ PHP Extension Installation

✅ Nginx Reverse Proxy

✅ Persistent Database Storage

---

# 📚 Learning Outcomes

This project helped me understand:

- Building custom Docker images
- Writing Dockerfiles
- Managing multi-container applications
- Docker Compose orchestration
- Container networking
- Volume management
- Running PHP applications inside Docker
- Connecting PHP to MySQL
- Serving applications through Nginx
- Persistent storage using Docker volumes

---

# 🔮 Future Improvements

- Add `.env` support for environment variables
- Add HTTPS using Nginx and Let's Encrypt
- Add phpMyAdmin
- Add Redis caching
- Configure automatic backups
- Add Health Checks
- Add Restart Policies
- Deploy using a reverse proxy
- Deploy to a cloud VPS
- CI/CD using GitHub Actions

---

# 📸 Screenshots

```
screenshots/

├── docker-compose-ps.png
<img width="1313" height="110" alt="image" src="https://github.com/user-attachments/assets/8b53e6c7-e1ca-4281-8c76-cb368de49a48" />
├── wordpress-homepage.png
<img width="1911" height="999" alt="image" src="https://github.com/user-attachments/assets/d4d74c07-a654-4394-a3c0-1599f54451bf" />
└── architecture.png
<img width="425" height="177" alt="image" src="https://github.com/user-attachments/assets/ff59aeb9-a047-4c4c-a583-e8955a13b0c9" />

```

# 👨‍💻 Author

**Shyam Prakash S**

Linux System Administrator | DevOps Enthusiast

- 🐧 Linux Administration
- 🐳 Docker & Docker Compose
- ☁️ DevOps
- 🖥️ Nginx & Apache
- 🗄️ MySQL
- 🐍 Python Automation

LinkedIn:
https://linkedin.com/in/shyam-ps

GitHub:
https://github.com/shyam-prakash-s
