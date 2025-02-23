# Intro to Containers

- [Reading material](intro.md)

## Prerequisites

- Ensure you have Python and Docker Desktop (or Rancher Desktop) installed on your machine.
- Create a virtual environment for your Python project and install the required packages like Flask.


## Setting Up the Application

1. **Create and activate a virtual environment**:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. **Install Flask**:
    ```sh
    pip install flask
    ```

3. **Create `app.py`**:
    ```python
    from flask import Flask

    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'We are running our first container - from CoderCo'

    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
    ```

4. **Create `requirements.txt`**:
    ```txt
    flask
    ```

## Running the Application Directly

1. **Run the Flask app**:
    ```sh
    python3 app.py
    ```

2. **Access the app**:
    - Open `http://localhost:5000` in your browser
    - Or run `curl http://localhost:5000` in your terminal

## Running the Application in a Docker Container

1. **Create a `Dockerfile`**:
    ```Dockerfile
    # this is your base image
    FROM python:3.9

    # we set the working dir in yourr container
    WORKDIR /usr/src/app

    # copying reqs file to your container so you can install the app reqs ygm
    COPY requirements.txt ./
    RUN pip install --no-cache-dir -r requirements.txt

    # copy your app code fam
    COPY . .

    # expose/open up the port on your container so you can access your app ygm
    EXPOSE 5000

    # running app in container
    CMD ["python", "app.py"]
    ```

2. **Build the Docker image**:
    ```sh
    docker build -t coderco .
    ```

3. **Run the Docker container**:
    ```sh
    docker run -p 5001:5001 coderco
    ```

4. **Access the app**:
    - Open `http://localhost:5000` in your browser
    - Or run `curl http://localhost:5000` in your terminal


## Challenge

- Access our challenge [here](./challenge/README.md)
