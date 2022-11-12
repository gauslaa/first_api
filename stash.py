from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/greeting/<string:name>', methods=['GET'])
def greeting(name):
    return f"Hello {name}! Nice to meet you"
    

app.run(host='0.0.0.0', port=3000)