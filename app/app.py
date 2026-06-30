import os

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Secure DevSecOps Pipeline"

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/version")
def version():
    return jsonify({"version": "1.0.0"})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)  # nosec B104