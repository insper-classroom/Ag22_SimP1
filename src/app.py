from flask import Flask, request, jsonify
from pathlib import Path
import pandas as pd


app = Flask(__name__)
app.list_of_dicts = []

# mais sobre a biblioteca pathlib: https://docs.python.org/3/library/pathlib.html
#@app.before_first_request
def load_dados():
    FILE = Path(__file__).resolve()
    src_folder = FILE.parents[0]
    rel_arquivo = Path('recursos/itens.csv')
    # concatena os paths
    arquivo = src_folder / rel_arquivo
    
    data = pd.read_csv(arquivo.resolve(), encoding="utf-8")
    app.list_of_dicts = data[['ean', 'name']].dropna().to_dict(orient="records")

