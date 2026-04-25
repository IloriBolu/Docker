from flask import Flask, jsonify
import logging, json, sys
from datetime import datetime

app = Flask(__name__)

class JSONFormatter(logging.Formatter):
    def format(self, record):
        return json.dumps({
            "time": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "message": record.getMessage()
        })

handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(JSONFormatter())

app.logger.handlers = []
app.logger.addHandler(handler)
app.logger.setLevel(logging.INFO)

@app.route("/")
def home():
    app.logger.info("home hit")
    return "API running"

@app.route("/error")
def error():
    app.logger.error("forced error happened")
    return jsonify({"error": "fail"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)