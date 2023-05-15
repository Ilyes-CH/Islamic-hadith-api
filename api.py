from flask import Flask, jsonify, render_template
import json

app = Flask(__name__, template_folder='template')

@app.route('/', methods=["GET"])
def home():
    return render_template('index.html')

@app.route('/api/data', methods=["GET"])
def api_data():
    try:
        with open('hadith.json', 'r') as f:
            hadiths = json.load(f)

        response = {
            'message': 'Data retrieved successfully',
            'status': 200,
            'data': hadiths
        }

        return jsonify(response), 200

    except FileNotFoundError:
        response = {
            'message': 'Resource not found',
            'status': 404
        }
        return jsonify(response), 404

    except Exception as e:
        response = {
            'message': 'Internal server error',
            'status': 500.
        }
        return jsonify(response), 500

if __name__ == '__main__':
    app.run(port=9999, debug=True)
