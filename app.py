from flask import Flask
import redis
import os

app = Flask(__name__)
redis_host = os.getenv('REDIS_HOST', 'redis')
cache = redis.Redis(host=redis_host, port=6379)

@app.route('/')
def hello():
    count = cache.incr('hits')
    return f'Hello from DevOps! I have been seen {count} times.'

@app.route('/health')
def health():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
