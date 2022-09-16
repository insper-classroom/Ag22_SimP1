# Ag22_SimP1
Simulado da P1


O diagrama de classes mostra como funciona um sistema de LMS 

Explicação das classes

Termine de implementar a classe:
Baseie os nomes dos métodos no diagrama de classe
A descrição do que as funções devem fazer é conforme a seguir


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




**pensar em persistência?**

Implemente a função *xyz* que lista todas as submissões de um determinado aluno 

Crie os testes .... 

Checar se as submissões têm texto no atributo  `resposta` 

Checar se as submissões do estudante são de tarefas pertencentes a turmas que o estudante cursa 


Checar se o estudante só pertence a determinada turma uma vez

Checar se todas as turmas que o estudante tem em aberto são do ano atual




Crie um endpoint/um web service rest/etc que encapsule a função xyz da classe xyz 

Usando o postman, crie um trecho de código que use a biblioteca requests e que acesse seu próprio código

Para testar, rode o flask e execute o web service e num outro terminal ou janela execute o código com requests 


**Questões conceituais**

Faz um diag seq 

Refletir sobre restfullness 

Pensar sobre encapsulamento um pouco 



Faça um diagrama de sequência do que acontece quando o método *listar_notas_estudante()* de FachadaTarefa é chamado (num papel e anexe uma foto)

A classe FachadaTarefa e seu método listar_notas_estudante() são RESTful? Por que não são?  (no simulado pode consultar a aula da semana 5). Como seria o acesso às notas do estudante para uma tarefa de maneira mais RESTful. Dê exemplos de como ficariam os endpoints. 



