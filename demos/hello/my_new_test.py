#!_*_coding:utf-8_*_
# Author:Jingkun
from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'
