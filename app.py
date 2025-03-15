from flask import Flask, request, jsonify
import json
from predict_threat import detect_threat
from automated_response import block_ip, send_alert

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze_traffic():
    data = request.json
    result = detect_threat(data)

    if result == "Threat Detected":
        ip = data.get("src_ip", "Unknown")
        block_ip(ip)
        send_alert(ip)

    return jsonify({"message": result})

if __name__ == "__main__":
    app.run(debug=True)
