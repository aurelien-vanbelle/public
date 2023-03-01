import ping3
from flask import Flask, render_template , jsonify

hostname = "1.1.1.1"
app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    try:
        latency = round(ping3.ping(hostname, unit='ms'),2)
        return render_template('index.html', latency=latency , hostname=hostname)
    except Exception as e:
        return str(e)

@app.route('/ping', methods=['POST'])
def ping():
    try:
        latency = round(ping3.ping(hostname, unit='ms'),2)
        return jsonify(latency)
    except Exception as e:
        return str(e)
   
if __name__ == '__main__':
     app.run(debug=True,host='0.0.0.0')