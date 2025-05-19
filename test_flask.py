# -*- coding: utf-8 -*-
"""
Created on Wed May  7 19:10:47 2025

@author: Gonca
"""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

if __name__ == '__main__':
    app.run()
    