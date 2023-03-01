from flask import Flask, render_template, jsonify, request
import ipPublique
import ping3
import main
import subprocess


ping_target = "1.1.1.1"
app = Flask(__name__)
# default page
@app.route('/')
def home():
    latency = round(ping3.ping(ping_target, unit='ms'),2)
    return render_template('index.html', variable=ipPublique.public_ip, latency=latency , hostname=ping_target, nmap=main.hosts)


# -------------------------------API------------------------------------
# PING api request
# @app.route('/ping', methods=['POST'])
# def ping():
#     try:
#         latency = round(ping3.ping(ping_target, unit='ms'),2)
#         print("PINGED")
#         return jsonify(latency)
#     except Exception as e:
#         return str(e)

# Restart api request
@app.route('/restart_vm', methods=['POST'])
def restart_vm():
    vm_ip = '192.168.116.196'
    command = f"sudo reboot {vm_ip}"    
    subprocess.call(command, shell=True)
    return "La SemaBox a été redémarrée avec succès !"

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port='5000')