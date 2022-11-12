from flask import Flask, redirect, url_for, request, jsonify, abort
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    print(url_for("hello_world")) # makes a url to the fuction not the deco
    return redirect('/hello')

@app.route('/hello')
def hello_world():
    return "Go to '/login' with a json"

@app.route('/login', methods=['POST'])
def login():
    content = request.json
    if not content:
        return abort(400, "You need to post data")
    name = content.get("name")
    if not name:
        return abort(400, "Name is required")
    return """{} are the top G\n
go to page "{}/next"
           """.format(name, name)


@app.route('/<string:name>/next')
def next(name):
    return """ {} Make a blog post \n This with jason, params: header, body \n send a POST request on '{}\write' """.format(name, name)

@app.route('/<string:name>/write', methods=['POST'])
def write(name):
    letter = request.json
    if not letter:
        return abort(400, "jason with header and/or body is missing!")
    header = letter.get("header")
    body = letter.get("body")
    if not (body or header):
        return abort(400,"header or body is required, PS {} is retarded".format(name))
    return "{}\n{}".format(header, body)


    

app.run(host='0.0.0.0', port=3000)
