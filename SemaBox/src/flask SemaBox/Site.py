from flask import Flask, render_template, jsonify, request
import ipPublique
import ping3
import main
import subprocess


hostname = "1.1.1.1"
app = Flask(__name__)

@app.route('/')
def home():
    latency = round(ping3.ping(hostname, unit='ms'),2)
    return render_template('index.html', variable=ipPublique.public_ip, latency=latency , hostname=hostname, nmap=main.hosts)

@app.route('/ping', methods=['POST'])
def ping():
    try:
        latency = round(ping3.ping(hostname, unit='ms'),2)
        return jsonify(latency)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port='9999')