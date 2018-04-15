# -*- coding: utf-8 -*-
from flask import Flask, render_template, json, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_len', methods=['GET', 'POST'])
def get_len():
    #name = request.form['name']
    name = input("Passs: ")
    return json.dumps({'len': str(name), 'path': str("/static/happy.png")})


if __name__ == '__main__':
    app.run(debug=True)
