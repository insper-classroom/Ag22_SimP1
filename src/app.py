from flask import Flask, request, jsonify
from pathlib import Path
import pandas as pd


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, Prova AG22!</p>"






if __name__ == '__main__':
    app.run(debug=True)