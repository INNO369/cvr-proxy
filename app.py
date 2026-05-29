from flask import Flask, request, jsonify, Response
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app, origins="*")

CVR_BASE = "https://distribution.virk.dk"

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok", "service": "CVR Proxy"})

@app.route('/cvr', methods=['POST'])
def cvr_proxy():
    auth = request.headers.get('X-CVR-Auth')
    if not auth:
        return jsonify({"error": "Missing X-CVR-Auth header"}), 401

    try:
        body = request.get_json()
        r = requests.post(
            f"{CVR_BASE}/cvr-permanent/virksomhed/_search",
            json=body,
            headers={
                "Authorization": f"Basic {auth}",
                "Content-Type": "application/json"
            },
            timeout=30
        )
        return Response(
            r.content,
            status=r.status_code,
            content_type='application/json'
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
