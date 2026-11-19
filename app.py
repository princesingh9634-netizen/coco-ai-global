from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("index.html")

@app.get("/api/status")
def status():
    return jsonify({
        "project": "COCO AI Global",
        "status": "prototype",
        "notice": "Demo data only. No deposits, withdrawals, staking, or real rewards are enabled."
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)
