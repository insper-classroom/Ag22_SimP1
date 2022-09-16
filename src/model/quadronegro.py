import datetime
import difflib 


def corrigir(gabarito, resposta):
    dif = difflib.SequenceMatcher(None, gabarito, resposta)
    return 10*(1 - dif.ratio())


class User(object):
    def __init__(self, nome):
        self.nome = nome 


class Professor(object):
    def __init__(self, nome):
        self.nome = nome
        self.turmas = [] 

class Estudante(object):
    def __init__(self, nome):    
        self.nome = nome
        self.turmas = [] 
        self.submissoes = []

    def matricular(self, turma:Turma):
        self.turmas.append(turma)
        turma.estudantes.append(self)

class Disciplina(object):
    def __init__(self,nome):
        self.nome = nome 

class Turma(object):
    EM_ABERTO = 0 
    CONCLUIDO = 1
    CANCELADO = 2
    def __init__(self,disciplina:Disciplina, nome:str, data = datetime.now):
        self.nome = nome
        self.status = Turma.EM_ABERTO
        self.data = data
        self.estudantes = []
        self.disciplina = disciplina
        self.tarefas = []


class Tarefa(object):
    submissoes = []
    def __init__(self, turma, gabarito):
        self.turma = turma 
        self.gabarito = gabarito

    def submeter(self, resposta, aluno, data = datetime.now):
        submissao = Submissao(resposta)
        submissao.nota = corrigir(self.gabarito, submissao.resposta)
        Tarefa.submissoes.append(submissao)
        aluno.submissoes.append(submissao) # TODO: isso é um bom encapsulamento? Por quê? 

    @classmethod
    def listar_submissoes_aluno(cls, estudante:Estudante): 
        """Lista todas as submissões de um dado aluno"""
        # TODO: implementar
        pass


class Submissao(object):
    def __init(self, tarefa, resposta):
        self.__nota == 0 
        self.tarefa = tarefa 
        self.resposta = resposta 

    @property
    def nota(self):
        return self.__nota

    @nota.getter
    def get_nota(self):
        return self.__nota

    @nota.setter
    def set_nota(self, nova_nota):
        self.__nota = nova_nota

class FachadaTarefa:
    def listar_tarefas():
        """Deve retornar uma lista com o nome de todas as tarefas"""
        pass

    def listar_notas_estudante(nome_tarefa:str, nome_estudante:str):
        """Deve retornar uma lista com as notas que o estudante obteve em todas as suas submissões para uma dada tarefa"""
        pass 

    def listar_disciplinas(nome_estudante:str): 
        """Deve retornar os nomes de todas as disciplinas que alguém cursa"""
        pass 

if __name__ == "__main__":
    d = Disciplina("DevLife")
    tur = Turma(d, "DevLife 2022/1")
    estudante = Estudante("Diana Deana")
    estudante.matricular(tur)
    tarefa = Tarefa(tur, "Pedro Álvares Cabral")
    tur.tarefas.append(tarefa)
    tarefa.submeter("Pedro A", estudante, datetime.datetime(2022, 09, 16))
    









