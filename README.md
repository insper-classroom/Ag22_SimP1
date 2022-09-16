# Ag22_SimP1

# Simulado da P1

## Atenção: Realize todas as mudanças e consertos que eventualmente se tornarem necessário


O diagrama de classes mostra como funciona um sistema de LMS (Learning Management System) chamado QuadroNegro 

As classes de negócio estão no `model/quadronegro.py`

O web service Flask deve ficar em `app.py`

Os testes devem ficar na pasta `teste`

# Classes

Um estudante está matriculado em uma ou mais turmas. Ex.: "Diana está na Turma de DevLife de 2022/1"

Cada turma tem vários estudantes.

Uma turma está relacionada a uma disciplina. Por exemplo a turm a "Devlife 2022/1" está relacionada à disciplina "DevLife". 

As turmas têm status `EM_ABERTO` durante o ano corrente, mas depois precisam virar para status `CONCLUIDO`. 

Cada turma vai ter diversas instâncias da classe `Tarefa`, cada tarefa pertence só a uma turma.

Os objetos da classe `Tarefa` têm o método `submeter` que permitem que o aluno envie uma submissão para aquela tarefa e já auto-corrige. A correção neste exemplo só compara duas strings e a nota é quanto elas são similares. 

A classe `FachadaTarefa`  deve usar as demais classes do quadronegro para implementar o que está pedido nas docstrings do método (as strings soltas). Esta classe depois vai ser chamada em app.py. 

Tanto `Estudante` quando `Professor` são classes filhas da classe `User`. Você não vai precisar mexer em *User* nem em *Professor*.








# Diagrama de classes 

Diagrama de classes da aplicação




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




**pensar em persistência?**

Implemente a função Tarefa.listar_submissoes_aluno  que lista todas as submissões de um determinado aluno 

Crie os testes .... 

Checar se as submissões têm texto no atributo  `resposta` 

Checar se as submissões do estudante são de tarefas pertencentes a turmas que o estudante cursa 


Checar se o estudante só pertence a determinada turma uma vez

Checar se todas as turmas que o estudante tem em aberto são do ano atual




Crie um endpoint/um web service rest/etc que encapsule as função 
Usando o postman, teste e salve collections 

**Questões conceituais**

Faça um diagrama de sequência do que acontece quando o método *listar_notas_estudante()* de FachadaTarefa é chamado (num papel e anexe uma foto)


Pensar sobre encapsulamento um pouco fazer referência ao too - pesquise se necessário





A classe FachadaTarefa e seu método listar_notas_estudante() são RESTful? Por que não são?  (no simulado pode consultar a aula da semana 5). Como seria o acesso às notas do estudante para uma tarefa de maneira mais RESTful. Dê exemplos de como ficariam os endpoints. 



