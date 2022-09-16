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

# TODO: definir rota  @app.route( etc)
def listar_tarefas():
    """Deve retornar uma lista com o nome de todas as tarefas"""
    # TODO: Chamar quadronegro.FachadaTarefas.listar_tarefas
    # implementar lá
    pass

# TODO: definir rota  @app.route( etc)
def listar_notas_estudante(nome_tarefa:str, nome_estudante:str):
    """Deve retornar uma lista com as notas que o estudante obteve em todas as suas submissões para uma dada tarefa"""
    # TODO: chamar a função correspondente de FachadaTarefas
    # implementar lá
    pass

# TODO: definir rota  @app.route( etc)
def listar_disciplinas(nome_estudante:str):
    # TODO: chamar a função correspondente de FachadaTarefas
    # implementar lá
    pass



if __name__ == '__main__':
    app.run(debug=True)