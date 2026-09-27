from flask import Flask
import redis
import os

app = Flask(__name__)
redis_host = os.getenv('REDIS_HOST', 'redis')
redis_port = int(os.getenv('REDIS_PORT', 6379))
r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

@app.route('/')
def hello():
    count = r.incr('visits')
    return f"<h1>Hello from Flask!</h1><p>Visits: {count}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
