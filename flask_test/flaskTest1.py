#!/usr/bin/env/py35
# coding=utf-8
from flask import Flask

app = Flask(__name__)
app.route('/hello')
def hello():
    return "hello flask"

if __name__ == '__main__':
    app.run()