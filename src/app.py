from flask import Flask, request, jsonify
from pathlib import Path
import pandas as pd


app = Flask(__name__)


@app.before_first_request
def executa_antes_do_primeiro_request():
    pass
    

@app.route("/")
def hello_world():
    return "<p>Hello, Prova AG22!</p>"






if __name__ == '__main__':
    app.run(debug=True)