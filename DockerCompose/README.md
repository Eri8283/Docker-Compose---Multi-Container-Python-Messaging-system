# Docker Compose – The Spanish Inquisition

**Author:** Erioluwa Olaniran

## Purpose

This Docker Compose setup demonstrates inter-container communication in a creative way. The goal is to pass the message:

```
Nobody expects the Spanish Inquisition!
```

between at least **two containers** before it reaches standard output. The project emphasizes the use of Docker Compose for orchestrating multiple containers while exploring interesting ways of message passing.

## How It Works

* The composition uses **two containers**:

  1. **Sender Container** – Holds or generates the message.
  2. **Receiver Container** – Receives the message from the sender and outputs it to standard output.

* The message is passed using **shared volumes**, but could also be implemented via **network communication** or **message queues**, making the interaction between containers more engaging than a simple echo.

* Optionally, the message can be transformed in some way before reaching the receiver container to demonstrate processing across containers.

## Languages Used

* **Bash scripting** – for simple scripts to generate and pass the message.
* **Dockerfile / Docker Compose YAML** – to define container images and orchestration.
* Optional: **Python** or other scripting languages could be used inside containers for creative message handling.

## How to Run

1. Build and start the containers:

```bash
make up
```

2. Test the message passing:

```bash
make test
```

The output should display:

```
Nobody expects the Spanish Inquisition!
```

3. Stop the containers after testing:

```bash
make stop
```

## Notes

* The message **must actively pass between containers**; hardcoding the message in the final container will not meet the grading criteria.
* Creativity in how the message is passed or transformed is encouraged.
* Ensure all scripts and configuration files required for communication are included and properly referenced in `docker-compose.yml`.
