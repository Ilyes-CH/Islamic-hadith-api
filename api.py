from flask import Flask, render_template
import json

app = Flask(__name__,template_folder='template')


@app.route('/',methods=["GET"])
def home():
    return render_template('index.html')


@app.route('/api/data')
def api_data():
   try:
        with open('hadith.json','r') as f:
            hadiths=json.load(f)
            
        data = {'Headers':{
            'message':'hello from server',
            'status': '200 ok',
            },
                'content': hadiths
                }

        return data , 200
    
   except:
       print('Error 500')
       api_data()


if __name__=='__main__':
    app.run(port=9999, debug=True)