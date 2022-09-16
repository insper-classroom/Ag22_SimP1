# Diagrama de classes 

Diagrama de classes da aplicação

Explicação


```mermaid 
classDiagram
class User {
}
class Professor {
}
class Estudante {
}
class Disciplina {
}
class Turma {
}
class Tarefa {
}
class Submissao {
}
Estudante "n" -- "m" Turma 
Estudante "1" -- "n" Submissao 
Tarefa "1" -- "n" Submissão
Turma "1" -- "n" Tarefa
Disciplina "1" -- "n" Turma 
Professor "n" -- "m" Turma
User <|-- Estudante
User <|-- Professor



 



```

