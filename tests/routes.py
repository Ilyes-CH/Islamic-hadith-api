
from flask import Flask, render_template, jsonify

app = Flask(__name__,template_folder='template')

@app.route('/',methods=["GET"])
def home():
    return render_template('index.html')

@app.route('/api/data')
def api_data():
    data = {
        'message':'hello from server',
        'status': 'ok'
    }
    return jsonify(data)
    