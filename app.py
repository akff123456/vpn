from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import random
import datetime

app = Flask(__name__, static_folder='static')
CORS(app)

connected_clients = []

def generate_fake_ip():
    return "192.168.0.{}".format(random.randint(2, 254))

def generate_fake_device():
    return random.choice(["Android", "Windows 10", "iPhone", "MacOS"])

@app.route('/connect', methods=['POST'])
def connect_user():
    client = {
        "ip": generate_fake_ip(),
        "device": generate_fake_device(),
        "time": datetime.datetime.now().strftime("%H:%M:%S")
    }
    connected_clients.append(client)
    return jsonify({"status": "connected"})

@app.route('/clients', methods=['GET'])
def get_clients():
    return jsonify(connected_clients)

@app.route('/')
def serve_user():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/admin')
def serve_admin():
    return send_from_directory(app.static_folder, 'admin.html')

if __name__ == '__main__':
    app.run(debug=True)
