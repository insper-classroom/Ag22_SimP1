# Diagrama de classes 

Diagrama de classes da aplicação

Explicação


```mermaid 
classDiagram
class User {
+String nome
}
class Professor {
list~Turma~ turmas_lecionadas
}
class Estudante {
list~Turma~ turmas_cursadas
list~Submissao~ submissoes
}
class Disciplina {
list~Turma~ turmas_oferecidas
}
class Turma {
Disciplina disciplina
}
class Tarefa {
list~Submissao~ submissoes
}
class Submissao {
Tarefa tarefa
}
Estudante "n" -- "m" Turma 
Estudante "1" -- "n" Submissao 
Tarefa "1" -- "n" Submissao
Turma "1" -- "n" Tarefa
Disciplina "1" -- "n" Turma 
Professor "n" -- "m" Turma
User <|-- Estudante
User <|-- Professor
```

