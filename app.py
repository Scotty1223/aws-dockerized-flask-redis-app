from flask import Flask
import redis
import os

app = Flask(__name__)

cache = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=6379,
    decode_responses=True
)

@app.route("/")
def home():
    visits = cache.incr("visits")

    return f"""
    <html>
        <head>
            <title>AWS Docker Project</title>
        </head>
        <body>
            <h1>Secure Dockerized Web Application on AWS</h1>
            <h2>Page Visits: {visits}</h2>

            <p>This Flask application is running inside Docker on an AWS EC2 instance.</p>

            <p>The application communicates with a separate Redis container through an internal Docker network.</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
