# Introduction to Containers

## What are Containers?

Containers are a lightweight form of virtualisation that allows you to run applications in isolated environments. They bundle an application and all its dependencies into a single package that can run consistently across different computing environments.

### Key Concepts

- **Image**: A read-only template that contains the application and its dependencies. Images are used to create containers.
- **Container**: A runnable instance of an image. Containers are isolated from each other and the host system.
- **Docker**: A platform that enables developers to build, ship, and run containers easily.

## Why Use Containers?

- **Consistency**: Containers ensure that applications run the same way in different environments, eliminating the "works on my machine" problem.
- **Isolation**: Each container runs in its own isolated environment, making it easy to manage dependencies and avoid conflicts.
- **Portability**: Containers can run on any system that supports the container runtime, whether it's a developer's laptop, a test environment, or a production server.
- **Efficiency**: Containers share the host system's kernel and resources, making them more lightweight and efficient than traditional virtual machines.

## A Brief History of Containers

- **Chroot (1979)**: The concept of containers dates back to the introduction of `chroot` in Unix, which allowed changing the root directory for a process, providing a basic level of isolation.
- **Solaris Containers (2004)**: Solaris introduced more advanced container features with Solaris Containers, allowing multiple isolated instances of the operating system.
- **LXC (2008)**: Linux Containers (LXC) brought containerisation to the Linux platform, offering lightweight virtualisation.
- **Docker (2013)**: Docker made containers easy to use by providing a simple interface and powerful tools for building, sharing, and running containers.

## The Technology Behind Containers

Containers leverage two key Linux kernel features to provide isolation and resource control:

### Namespaces

Namespaces provide the isolation aspect of containers. They ensure that a process running inside a container cannot see or affect processes running outside the container. Different types of namespaces include:

- **PID namespace**: Isolates process IDs.
- **NET namespace**: Isolates network interfaces.
- **MNT namespace**: Isolates mount points.
- **UTS namespace**: Isolates hostname and domain name.
- **IPC namespace**: Isolates inter-process communication.
- **USER namespace**: Isolates user and group IDs.

### Control Groups (cgroups)

Control groups (cgroups) provide resource limiting and monitoring. They allow you to allocate resources such as CPU, memory, and I/O bandwidth to specific containers, ensuring that no single container can monopolize system resources. Cgroups help in:

- **Resource Limiting**: Restricting the amount of resources a container can use.
- **Prioritization**: Setting priority levels for different containers.
- **Accounting**: Monitoring resource usage by containers.
- **Control**: Freezing or thawing containers.


## Understanding Docker

Docker is the most popular platform for containerisation. It simplifies the process of creating and managing containers. Here's a quick overview of Docker's components:

- **Docker Engine**: The core of Docker, it runs and manages containers.
- **Docker Hub**: A public registry where Docker images can be stored and shared.
- **Dockerfile**: A script that defines how to build a Docker image, specifying the base image, application code, and dependencies.

### How Docker Works

1. **Write a Dockerfile**: Define the environment for your application.
2. **Build an Image**: Create an image from the Dockerfile.
3. **Run a Container**: Start a container from the image.

## Getting Started with Docker

### Install Docker

1. Download and install Docker Desktop from [Docker's official website](https://www.docker.com/products/docker-desktop).
2. Follow the installation instructions for your operating system.

### Basic Docker Commands

- `docker pull <image>`: Download an image from Docker Hub.
- `docker build -t <name> .`: Build an image from a Dockerfile.
- `docker run -p <host_port>:<container_port> <image>`: Run a container from an image.
- `docker ps`: List running containers.
- `docker stop <container_id>`: Stop a running container.
- `docker rm <container_id>`: Remove a stopped container.
- `docker rmi <image_id>`: Remove an image.

### Running Your First Container

Let's start by running a simple container to see Docker in action.

1. **Pull the hello-world image**:
    ```sh
    docker pull hello-world
    ```

2. **Run a container from the hello-world image**:
    ```sh
    docker run hello-world
    ```

This will download the image (if not already available locally) and run a container that prints a "Hello from Docker!" message, confirming that your Docker setup is working correctly.

## Summary

Containers are a powerful tool for modern app development, providing consistent, isolated, and portable environments. Docker simplifies the process of building, sharing, and running containers, making it accessible for developers and operations teams alike.

