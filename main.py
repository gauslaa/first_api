from flask import Flask, redirect, url_for, request, jsonify, abort
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/info')
def search():
    args = request.args
    print(args)
    return args

@app.route('/product/<var>')
def get_product(var):
    return "The product is " + str(var)

@app.route('/disp_jason/<jas>')
def disp_jason(jas):
    print(jas)
    return "GD"

@app.route('/message/<int:uuid>', methods=['POST'])
def add_message(uuid):
    content = request.json
    if content:
        if content.get("mytext"):
            return jsonify({"uuid":uuid})
        return abort(400,"mytext is required")
    return "content is required"

@app.route('/message/<string:uuid>', methods=['POST'])
def add_message_str(uuid):
    return "uuid must be int"



@app.route('/path/<int:direction>')
def path(direction):
    if direction == None:
        return "Change ~/path/ --- "
    elif direction == 1:
        return redirect(url_for("zzz"))

@app.route('/zzz')
def zzz():
    return "You do not want de be here"


@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        jaso = request
        print(jaso)
        return redirect(url_for('/disp_jason'))
    return redirect(url_for("/"))

app.run(host='0.0.0.0', port=3000)
