from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from datetime import datetime
import platform
import os

app = Flask(__name__, static_folder="static")
CORS(app)

clients = []

@app.route("/")
def index():
    return send_from_directory("static", "index.html")

@app.route("/admin")
def admin():
    return send_from_directory("static", "admin.html")

@app.route("/connect", methods=["POST"])
def connect():
    # Получаем IP, даже если через прокси (Render, Cloudflare и т.д.)
    ip = request.headers.get("X-Forwarded-For", request.remote_addr).split(",")[0].strip()
    device = request.user_agent.platform or platform.system()
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Добавляем, если такого IP ещё нет
    if not any(client["ip"] == ip for client in clients):
        clients.append({"ip": ip, "device": device, "time": time})
    return jsonify({"success": True})

@app.route("/clients")
def get_clients():
    return jsonify(clients)

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory("static", path)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
