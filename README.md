# DevOps intensive tasks
## Project Description
This project consists of two parts:
1. An Ansible playbook to configure a Debian 10 server and install and start PostgreSQL 16.
2. A Python HTTP server that returns "200 OK" when accessed at /healthz, and its Docker deployment.
### Ansible Playbook for PostgreSQL Setup
The Ansible playbook is designed to automate the installation and configuration of PostgreSQL 16 on a Debian 10 server. The playbook performs the following tasks:
- Updates the apt package manager.
- Installs the required packages and dependencies.
- Adds the PostgreSQL APT repository to the sources list.
- Updates the apt package manager again to include the new repository.
- Installs PostgreSQL 16 and its contrib packages.
- Configuration  pg_hba.conf and postgresql.conf files.
- Restarts the PostgreSQL service to apply the changes.
- Creates a new PostgreSQL database and user with the specified name and password.
- Grants all privileges on the new database to the new user.
The playbook assumes that you have already installed Ansible on your local machine and have access to the remote Debian 10 server via SSH.
### Python HTTP Server and Docker Deployment
The Python HTTP server is a simple application that returns `"200 OK"` when accessed at the `/health` endpoint. The application is implemented using the built-in `http.server` module in Python 3, and is designed to be deployed in a Docker container.
- Building a Docker image from the Dockerfile.
- Running the Docker container from the Docker image.
The Dockerfile specifies the base image (Python 3.11), installs the required packages and dependencies, copies the HTTP server code to the container, and exposes port 8080 for access from outside the container.
The Docker container is configured to automatically start the HTTP server when the container is started. The container can be accessed at `http://localhost:8000/healthz` (or the appropriate IP address and port) to verify that it is running correctly.
### Usage
To use the Ansible playbook follow the following steps:
- copy the project to your machine using the command `git clone https://github.com/K4vabanga/PT_START_INT-34.git`
- move to the project using the command `cd PT_START_INT-34/Ansible`
- edit the `inventory.yml` file by substituting your data
- start the execution of the playbook using the command `ansible-playbook playbook.yml`
To connect to a configured PostgreSQL server, use the following command `psql -h host -p port -U myuser -d mydatabase`
To use Python HTTP server and Docker deployment follow the following steps:
- copy the project to your machine using the command `git clone https://github.com/K4vabanga/PT_START_INT-34.git`
- move to the project using the command `cd PT_START_INT-34/CI_CD`
- Assemble the docker image using the command `docker build .`
- Run the docker container from the assembled image using the command `docker run -p 8000:8000 .`
You can access the HTTP server to make sure it is working correctly using the following command `curl http://localhost:8000/healthz`
