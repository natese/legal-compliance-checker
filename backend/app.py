from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allows your frontend to connect

@app.route('/')
def home():
    return "Legal Compliance Checker API is running!"

@app.route('/check', methods=['POST'])
def check_compliance():
    data = request.get_json()
    location = data.get('location', '').lower()
    size = int(data.get('size', 0))
    collects_data = data.get('data', '')

    result = []
    if location == "eu" and collects_data == "yes":
        result.append("✅ Must comply with GDPR.")
    elif location == "us" and collects_data == "yes":
        result.append("✅ Should comply with CCPA or other US privacy laws.")
    else:
        result.append("✅ No major data privacy regulations detected.")

    if size > 5:
        result.append("⚠️ Check labor laws for businesses with more than 5 employees.")

    return jsonify({"report": result})

import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
