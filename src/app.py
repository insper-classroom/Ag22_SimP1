import json
from flask import Flask, request, jsonify
from pathlib import Path
from src.model.quadronegro import *



app = Flask(__name__)


@app.before_first_request
def executa_antes_do_primeiro_request():
    d = Disciplina("DevLife")
    tur = Turma(d, "DevLife 2022/1")

    d2 = Disciplina("A Bug's Life")
    tur2 = Turma(d2, "B Life 2022/2")

    d3 = Disciplina("The Life of Pi")
    tur3 = Turma(d3, "Pi Life 2022/2")

    d4 = Disciplina("The Life of Brian")
    tur4 = Turma(d4, "Brian Life 2022/2")


    estudante = Estudante("Diana Deana")
    
    estudante.matricular(tur)
    estudante.matricular(tur2)
    estudante.matricular(tur3)
    estudante.matricular(tur4)
    
    tarefa = Tarefa(tur, "Pedro Álvares Cabral")
    tarefa2 = Tarefa(tur, "Cristóvão Colombo") # só para deixar o teste melhor

    tarefa.submeter("Pedro A", estudante, datetime.datetime(2022, 9, 16))
    tarefa.submeter("Pedro Álvares", estudante)    
    
    tarefa2.submeter("Francisco Pizarro", estudante, datetime.datetime(2022, 9, 16))

    # Testando a Q1
    resp = Tarefa.listar_submissoes_aluno(estudante)
    for r in resp:
        print(r)

    # Testes das novas funções

    tarefas = FachadaTarefa.listar_tarefas()
    print("Todas as tarefas")
    print(tarefas)

    disc = FachadaTarefa.listar_disciplinas("Diana Deana")
    print("Disciplinas da aluna")
    print(disc)

    notas_estudante = FachadaTarefa.listar_notas_estudante("Pedro Álvares Cabral", "Diana Deana")
    print("Notas numa disciplina")
    print(notas_estudante)



    

@app.route("/")
def hello_world():
    return "<p>Hello, Prova AG22!</p>"

# TODO: definir rota  @app.route( etc)
@app.route("/listar_tarefas")
def listar_tarefas():
    """Deve retornar uma lista com o nome de todas as tarefas"""
    # TODO: Chamar quadronegro.FachadaTarefas.listar_tarefas
    lista = FachadaTarefa.listar_tarefas()
    return jsonify(lista)

# TODO: definir rota  @app.route( etc)
@app.route("/listar_notas_estudante/<nome_estudante>/<nome_tarefa>", methods=['GET'])
def listar_notas_estudante(nome_tarefa:str, nome_estudante:str):
    """Deve retornar uma lista com as notas que o estudante obteve em todas as suas submissões para uma dada tarefa"""
    # Para testar precisa passar espaços e acentos por URLEncode, por exemplo
    # http://127.0.0.1:5000/listar_notas_estudante/Diana%20Deana/Pedro%20%C3%81lvares%20Cabral
    

    notas = FachadaTarefa.listar_notas_estudante(nome_tarefa, nome_estudante)
    return jsonify(notas)
    

# TODO: definir rota  @app.route( etc)
@app.route("/listar_disciplinas/<nome_estudante>", methods=['GET'])
def listar_disciplinas(nome_estudante:str):
    # TODO: chamar a função correspondente de FachadaTarefas
    # Exemplo de chamada: http://127.0.0.1:5000/listar_disciplinas/Diana%20Deana
    
    lista = FachadaTarefa.listar_disciplinas(nome_estudante) 
    return jsonify(lista)


if __name__ == '__main__':
    app.run(debug=True)