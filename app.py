from flask import Flask, jsonify
import redis, os, socket

app = Flask(__name__)
db = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=int(os.getenv("REDIS_PORT", "6379")),
    decode_responses=True,
    socket_connect_timeout=3
)

@app.route("/")
def home():
    count = db.incr("visitor_count")
    return f"""
    <html><body style="font-family:Arial;text-align:center;margin-top:80px">
    <h1>Cloud Visitor Counter</h1>
    <h2>Total Visitors: {count}</h2>
    <p>Flask + Redis + Docker + Kubernetes</p>
    <p>Instance: {socket.gethostname()}</p>
    <a href="/count">View Counter API</a>
    </body></html>
    """

@app.route("/health")
def health():
    return jsonify(status="healthy"), 200

@app.route("/ready")
def ready():
    db.ping()
    return jsonify(status="ready"), 200

@app.route("/count")
def count():
    return jsonify(visitor_count=int(db.get("visitor_count") or 0))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
