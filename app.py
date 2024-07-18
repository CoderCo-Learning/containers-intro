from flask import Flask
import redis
import os

app = Flask(__name__)
redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = os.getenv("REDIS_PORT", 6379)
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)

@app.route('/')
def welcome():
    return "Welcome to Mo's CoderCo Containers Challenge using Flask and Redis!"

@app.route('/count')
def count():
    redis_client.incr('visit_count')
    count = redis_client.get('visit_count')
    return f"Visit count: {count}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
