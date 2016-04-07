# -*- coding: utf-8 -*-
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<html><head><meta charset=\"UTF-8\" /><title>Document</title></head><body><h1 style=\'font-size: 166px; margin: auto; text-shadow: 6px 6px 0 #f2f2f2;\'>СПАСИБО</h1></body></html>"

if __name__ == "__main__":
    app.run()