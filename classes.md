# Diagrama de classes 

Diagrama de classes da aplicação

Explicação


```mermaid
classDiagram
direction LR
class User {
+nome: str
}
class Professor {
turmas_lecionadas:list~Turma~ 
}
class Estudante {
+estudante_id:str
turmas_cursadas:list~Turma~ 
submissoes:list~Submissao~ 
}
class Disciplina {
turmas_oferecidas:list~Turma~
}
class Turma {
disciplina:Disciplina
}
class Tarefa {
$ tarefas: list~Tarefa~ *da classe*
submissoes:list~Submissao~
$ classmethod obter_tarefas():list~Tarefa~ 
}
class Submissao {
tarefa:Tarefa
}
class FachadaTarefa{
+listar_tarefas():list~str~
+listar_notas_estudante(nome_tarefa:str, nome_estudante:str):->list~dict~
+listar_disciplinas(nome_estudante:str):->list~dict~
}
Estudante "n" -- "m" Turma 
Estudante "1" -- "n" Submissao 
Tarefa "1" -- "n" Submissao
Turma "1" -- "n" Tarefa
Disciplina "1" -- "n" Turma 
Professor "n" -- "m" Turma
User <|-- Estudante
User <|-- Professor
FachadaTarefa ..> Tarefa 
FachadaTarefa ..> Estudante
```

