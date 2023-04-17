# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 17:26:44 2023

@author: I2612
"""
# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)
@app.route("/")

def example():
    return "Docker Challenge!"
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=int("5000"),debug=True)