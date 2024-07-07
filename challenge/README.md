# CoderCo Containers Challenge

Building a Multi-Container Application

## Objective

Create a multi-container application that consists of a simple Python Flask web application and a Redis database. The Flask application should use Redis to store and retrieve data.

## Requirements

1. **Flask Web Application**:
   - A Flask app that has two routes:
     - `/`: Displays a welcome message.
     - `/count`: Increments and displays a visit count stored in Redis.

2. **Redis Database**:
   - Use Redis as a key-value store to keep track of the visit count.

3. **Dockerize Both Services**:
   - Create Dockerfiles for both the Flask app and Redis.
   - Use Docker Compose to manage the multi-container application.

## Test the Application

Access the Welcome Page:

Open your browser and go to `http://localhost:5000` to see the welcome message.
Test the Visit Count:

Navigate to `http://localhost:5000/count` to see the visit count increment each time you refresh the page.


## Bonus

- Persistent Storage for Redis: Configure Redis to use a volume to persist its data.
- Environment Variables: Modify the Flask application to read Redis connection details from environment variables and update the docker-compose.yml accordingly.
- Scaling the Application: Scale the Flask service to run multiple instances and load balance between them using Docker Compose.
