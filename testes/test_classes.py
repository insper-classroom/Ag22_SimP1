from src.model.quadronegro import *
import pytest

# Checar se as submissões têm texto no atributo  `resposta`
@pytest.mark.sim_ag22
def test_verificar_se_submissoes_possuem_texto_no_atributo_resposta():
    ### Vamos precisar criar um pequeno conjunto de objetos de teste em todo exemplo
    """ Neste caso "Checar se as submissões têm texto no atributo  `resposta`" pode ser um pouco ambíguo
    pode ser checar se há texto com comprimento maior que zero, ou se a variável é diferente de None
    Também não está claro se a submissão ser nula é uma falha ou não. Entendemos que seja
    Vamos ver se a classe evitou estas situações

    É importante dizer que numa avaliação o enunciado deveria ser mais específico


     """
    d = Disciplina("DevLife")
    tur = Turma(d, "DevLife 2022/1")
    estudante = Estudante("José En. Tulio")
    estudante.matricular(tur)
    tarefa = Tarefa(tur, "Soma dos quadrados da hipotenusa")

    # Vai falhar em todos os três mas para de executar na primeira falha
    # Mover para antes o teste de interesse
    verificar_submissao_vazia(tarefa, estudante)
    verificar_se_dispara_excecao(tarefa, estudante)  # Este teste passa. Acaba disparando exceção
    #verificar_submissao_nula(tarefa, estudante) - não foi necessário porque dá um erro na correção impedindo de criar submissão nula

        
## Verificar se lança exceção em ambos os casos
def verificar_se_dispara_excecao(tarefa, estudante):
    """Verifica se criar submissao com None dispara *qualquer* excecao"""
    """ O teste não falha porque de fato dá problema ao criar"""
    with pytest.raises(Exception) as exc:
        # Se nao disparar nenhuma excecao o teste falha
        tarefa.submeter(None, estudante)
       
## Checar se None é permitido no objeto
def verificar_submissao_nula(tarefa, estudante): 
    tarefa.submeter(None, estudante)
    submissoes = Tarefa.listar_submissoes_aluno(estudante)
    ultima = submissoes[-1]
    assert None != ultima.resposta, "Falha: foi permitido criar uma submissão com texto nulo"

## Verificar submissão vazia
def verificar_submissao_vazia(tarefa, estudante):
    tarefa.submeter("", estudante)
    submissoes = Tarefa.listar_submissoes_aluno(estudante)
    ultima = submissoes[-1]
    assert "" != ultima.resposta, "Falha: foi permitido criar uma submissão com texto vazio"

# Checar se as submissões do estudante são de tarefas pertencentes a turmas que o estudante cursa 
@pytest.mark.sim_ag22
def test_verificar_se_submissoes_do_estudante_sao_de_tarefas_de_turmas_do_estudante():

    d1 = Disciplina("DevLife")
    d2 = Disciplina("CDados")

    tur1 = Turma(d1, "DevLife 2022/1")
    tur2 = Turma(d2, "Ciência dos Dados")
    
    estudante = Estudante("Cássio Andor")
    
    estudante.matricular(tur1)
    estudante.matricular(tur2)    

    tarefa1_d1 = Tarefa(tur1, "IFs e condicionais")
    tarefa2_d1 = Tarefa(tur1, "Aventura submarina")
    tarefa1_d2 = Tarefa(tur2, "Distribuição normal")
    tarefa2_d2 = Tarefa(tur2, "Dataframes")

    tarefa1_d1.submeter("apenas uma resposta teste", estudante)
    tarefa2_d1.submeter("apenas uma resposta teste", estudante)
    tarefa1_d2.submeter("apenas uma resposta teste", estudante)
    tarefa2_d2.submeter("apenas uma resposta teste", estudante)
    
    todas_submissoes_aluno = Tarefa.listar_submissoes_aluno(estudante)
    todas_do_aluno = True

    for submissao in todas_submissoes_aluno: 
        if submissao.tarefa.turma not in estudante.turmas: 
            # se houver uma só turma errada já falha o teste
            todas_do_aluno = False
    
    assert True == todas_do_aluno, "Todas as submissões são de fato do aluno"


# Checar se o estudante só pertence a determinada turma uma vez
@pytest.mark.sim_ag22
def test_verificar_se_estudante_pertence_a_uma_turma():
    d1 = Disciplina("DevLife")
    d2 = Disciplina("CDados")
    tur1 = Turma(d1, "DevLife 2022/1")
    tur2 = Turma(d2, "Ciência dos Dados")   

    estudante = Estudante("Cássio Andor")
    
    estudante.matricular(tur1)
    estudante.matricular(tur2)    

    # Vamos tentar matricular o estudante várias vezes na mesma turma e ver o que acontece
    estudante.matricular(tur2)
    estudante.matricular(tur2)    

    

    # Algumas estratégias de testar: 
    # Usar turma como chave de um dicionário em que o valor é a contagem de vezes que está matriculado naquela turma e ver se há alguma turma com mais de uma matrícula
    # Usar a classe set e criar um conjunto com a lista de turmas. Testar se o tamanho do conjunto é menor que o tamanho da lista de turmas 

    # Vamos fazer o teste mais simples possível
    assert len(estudante.turmas) == 2, "Verificando se permitiu matricular em mais de uma turma de cada vez"



# Checar se todas as turmas do estudante são do ano atual
@pytest.mark.sim_ag22
def test_verificar_se_todas_as_turmas_do_estudante_sao_do_ano_atual():
    """  Uma possível causa """

    d1 = Disciplina("DevLife")
    d2 = Disciplina("CDados")
    tur1 = Turma(d1, "DevLife 2022/1", datetime.datetime(1919, 9, 20))
    tur2 = Turma(d2, "Ciência dos Dados", datetime.datetime(1919, 4, 20))

    estudante = Estudante("Cássio Andor")
    
    estudante.matricular(tur1)
    estudante.matricular(tur2)    

    agora = datetime.datetime.now()
    
    todas_atuais = True
    for t in estudante.turmas:
        if t.data.year != agora.year: 
            todas_atuais = False
    
    assert True == todas_atuais, "Verificacao se todas as turmas sao do ano atual "

