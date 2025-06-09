from flask import Flask, render_template_string
import redis
import os

app = Flask(__name__)
redis_host = os.getenv('REDIS_HOST', 'redis')
cache = redis.Redis(host=redis_host, port=6379)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>DevOps App</title>
    <style>
        body {
            background: #f0f2f5;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            text-align: center;
            padding-top: 10vh;
            color: #333;
        }
        .container {
            background: white;
            display: inline-block;
            padding: 40px;
            border-radius: 16px;
            box-shadow: 0 0 30px rgba(0,0,0,0.1);
        }
        h1 {
            font-size: 2.5rem;
            margin-bottom: 10px;
        }
        p {
            font-size: 1.2rem;
            margin-top: 0;
        }
        .footer {
            margin-top: 40px;
            font-size: 0.9rem;
            color: #777;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 Hello from DevOps!</h1>
        <p>I have been seen <strong>{{ count }}</strong> times.</p>
        <div class="footer">Version: {{ version }}</div>
    </div>
</body>
</html>
"""

@app.route('/')
def hello():
    try:
        count = cache.incr('hits')
    except redis.exceptions.RedisError:
        count = 'unavailable'
    version = os.getenv('APP_VERSION', 'unknown')
    return render_template_string(HTML_TEMPLATE, count=count, version=version)

@app.route('/version')
def version():
    return f"Version: {os.getenv('APP_VERSION', 'unknown')}"

@app.route('/health')
def health():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
