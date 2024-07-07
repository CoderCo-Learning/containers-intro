# Intro to Containers

## How to

- Make sure to have python and docker desktop or rancher destkop installed.
- Create a virtual environemnt for your python and install app requirements like Flask etc



## Run app directly

- `python3 app.py`

## Run your container

- `docker build -t coderco .`

- `docker run -p 5000:5000 coderco`
- open `localhost:5000` on your browser or curl localhost:5000
