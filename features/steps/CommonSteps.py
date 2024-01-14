from logging import raiseExceptions
from behave import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from faker import Faker
from datetime import datetime, date , timedelta
from json import dumps
import time, os, requests, json

@given('que esteja logado no sistema')
def step_impl(context):
    context.execute_steps(u'''
        Dado que esteja na página de login do Bright
        Quando insiro rafael@datacomrn.com.br no campo email do login
        E insiro 123456 no campo senha do login
        E clico no botão realizar login
    ''')
    time.sleep(2)
#cadastro steps################################

@given(u'Que tenha uma modalidade cadastrada')
def step_impl(context):
    try:
        fake = Faker('pt_BR')
        fakeModalidade = fake.name()
        context.variables['globalModalidade'] = fakeModalidade

        token = context.variables['token_api']
        headers = {
            'Authorization': f'Bearer {token}'
        }
        myobj = {
            'nome': context.variables['globalModalidade']
            }
        requests.post(context.variables['url_api_modalidades'], json = myobj , headers = headers)
        time.sleep(1)
        #pegando o id criado , buscando pelo ultimo criado, invertendo a lista e pegando a primeira posição
        id_item = sorted(json.loads(requests.get(context.variables['url_api_modalidades'], headers=headers).content), key=lambda x: x['created_at'], reverse=True)

        context.variables['idModalidade'] = id_item[0]['id']
    except:
        raise Exception(id_item.content.decode('utf-8'))

@given(u'Que tenha uma categoria cadastrada')
def step_impl(context):
    try:
        fake = Faker('pt_BR')
        CategoriaFaker = fake.name()
        context.variables['globalCategoria'] = CategoriaFaker
        token = context.variables['token_api']
        headers = {
            'Authorization': f'Bearer {token}'
        }
        myobj = {
            'nome': context.variables['globalCategoria']
            }
        requests.post(context.variables['url_api_categorias'], json = myobj , headers = headers)
        time.sleep(1)
        #pegando o id criado , buscando pelo ultimo criado, invertendo a lista e pegando a primeira posição
        id_item = sorted(json.loads(requests.get(context.variables['url_api_categorias'], headers=headers).content), key=lambda x: x['created_at'], reverse=True)

        context.variables['idCategoria'] = id_item[0]['id']
    except:
        raise Exception(id_item.content.decode('utf-8'))
@given(u'Que tenha uma nova modalidade cadastrada')
def step_impl(context):
    context.execute_steps(u'''
        Quando Entro em Modalidades
        E Clico no botão + NOVA MODALIDADE
        E escrevo NovaModalidadeFaker no campo Nome
        E Clico em Criar
        Então Mensagem de criação foi exibida
        ''')
    
@given(u'Que tenha uma nova categoria cadastrada')
def step_impl(context):
    context.execute_steps(u'''
        Quando Entro em Categorias
        E Clico no botão + NOVA CATEGORIA
        E Insiro NAO-ALUNO no campo Nome
        E Clico em Criar
        Então Mensagem de criação foi exibida de categorias
        ''')

@given(u'Que tenha um Estado civil cadastrado')
def step_impl(context):
    try:
        fake = Faker('pt_BR')
        fakeEstadoCivil = fake.name()
        context.variables['globalEstadoCivil'] = fakeEstadoCivil
        token = context.variables['token_api']
        headers = {
            'Authorization': f'Bearer {token}'
        }
        myobj = {
            "nome": context.variables["globalEstadoCivil"]
            }
        criacao = requests.post(context.variables['url_api_Estado_civil'], json = myobj , headers = headers)
        time.sleep(1)
        #pegando o id criado , buscando pelo ultimo criado, invertendo a lista e pegando a primeira posição
        id_item = sorted(json.loads(requests.get(context.variables['url_api_Estado_civil'], headers=headers).content), key=lambda x: x['created_at'], reverse=True)

        context.variables['idEstadoCivil'] = id_item[0]['id']
    except:
        raise Exception(id_item.content.decode('utf-8'))
@given(u'Que tenha dois Estados civis cadastrado')
def step_impl(context):
    context.execute_steps(u'''
        Quando Entro em Estado civil
        E Clico no botão + NOVO ESTADO CIVIL
        E digito EstadoCivilFaker no campo Nome de Estado civil
        E Clico em Criar de Estado civil
        E Clico no botão + NOVO ESTADO CIVIL
        E escrevo NovoEstadoCivilFaker no campo Nome de Estado civil
        E Clico em Criar de Estado civil        
        ''')
    time.sleep(1)

@given(u'Que tenha um Genero cadastrado')
def step_impl(context):
    try:
        fake = Faker('pt_BR')
        GeneroFaker = fake.name()
        context.variables['globalGenero'] = GeneroFaker
        token = context.variables['token_api']
        headers = {
            'Authorization': f'Bearer {token}'
        }
        myobj = {
            'nome': context.variables['globalGenero']
            }
        requests.post(context.variables['url_api_Genero'], json = myobj , headers = headers)
        time.sleep(1)

        #pegando o id criado , buscando pelo ultimo criado, invertendo a lista e pegando a primeira posição
        id_item = sorted(json.loads(requests.get(context.variables['url_api_Genero'], headers=headers).content), key=lambda x: x['created_at'], reverse=True)

        context.variables['idGenero'] = id_item[0]['id']
    except:
        raise Exception(id_item.content.decode('utf-8'))

@given(u'Que tenha um Naipe cadastrado')
def step_impl(context):
    try:
        fake = Faker('pt_BR')
        NaipeFaker = fake.name()
        context.variables['globalNaipe'] = NaipeFaker
        token = context.variables['token_api']
        headers = {
            'Authorization': f'Bearer {token}'
        }
        myobj = {
            'nome': context.variables['globalNaipe']
            }
        requests.post(context.variables['url_api_Naipe'], json = myobj , headers = headers)
        time.sleep(1)

        #pegando o id criado , buscando pelo ultimo criado, invertendo a lista e pegando a primeira posição
        id_item = sorted(json.loads(requests.get(context.variables['url_api_Naipe'], headers=headers).content), key=lambda x: x['created_at'], reverse=True)

        context.variables['idNaipe'] = id_item[0]['id']
    except:
        raise Exception(id_item.content.decode('utf-8'))
@given(u'Que tenha dois Naipes cadastrado')
def step_impl(context):
    context.execute_steps(u'''
        Quando Entro em Naipe
        E Clico no botão + NOVO NAIPE
        E digito NaipeFaker no campo Nome de Naipe
        E Clico em Criar de Naipe
        E Clico no botão + NOVO NAIPE
        E insiro teste no campo Nome de Naipe
        E Clico em Criar de Naipe
        Então Mensagem de criação foi exibida de Naipe
        ''')

@given(u'Que tenha um MetodoPagamento cadastrado')
def step_impl(context):
    try:
        fake = Faker('pt_BR')
        context.variables['globalMetodoPagamento'] = fake.name()

        token = context.variables['token_api']
        headers = {
            'Authorization': f'Bearer {token}'
        }
        myobj = {
            'nome': context.variables['globalMetodoPagamento']
            }

        requests.post(context.variables['url_api_metodoPagamento'], json = myobj , headers = headers)
        time.sleep(1)


        #pegando o id criado , buscando pelo ultimo criado, invertendo a lista e pegando a primeira posição
        id_item = sorted(json.loads(requests.get(context.variables['url_api_metodoPagamento'], headers=headers).content), key=lambda x: x['created_at'], reverse=True)

        context.variables['idMetodoPagamento'] = id_item[0]['id']
    except:
        raise Exception(id_item.content.decode('utf-8'))
@given(u'Que tenha dois MetodoPagamentos cadastrado')
def step_impl(context):
    context.execute_steps(u'''
        Quando Entro em MetodoPagamento
        E Clico no botão + NOVO MetodoPagamento
        E digito MetodoPagamentoFaker no campo Nome de MetodoPagamento
        E Clico em Criar de MetodoPagamento
        E Clico no botão + NOVO MetodoPagamento
        E insiro misto no campo Nome de MetodoPagamento
        E Clico em Criar de MetodoPagamento
        Então Mensagem de criação foi exibida de MetodoPagamento
        ''')

@given(u'Que tenha um Conhecimento cadastrado')
def step_impl(context):
    try:
        fake = Faker('pt_BR')
        ConhecimentoFaker = fake.name()
        context.variables['globalConhecimento'] = ConhecimentoFaker
        token = context.variables['token_api']
        headers = {
            'Authorization': f'Bearer {token}'
        }
        myobj = {
            'nome': context.variables['globalConhecimento']
            }
        requests.post(context.variables['url_api_Conhecimento'], json = myobj , headers = headers)
        time.sleep(1)
        
        #pegando o id criado , buscando pelo ultimo criado, invertendo a lista e pegando a primeira posição
        id_item = sorted(json.loads(requests.get(context.variables['url_api_Conhecimento'], headers=headers).content), key=lambda x: x['created_at'], reverse=True)

        context.variables['idConhecimento'] = id_item[0]['id']
    except:
        raise Exception(id_item.content.decode('utf-8'))

@given(u'Que tenha dois Conhecimentos cadastrado')
def step_impl(context):
    context.execute_steps(u'''
        Quando Entro em Conhecimento
        E Clico no botão + NOVO CONHECIMENTO
        E digito ConhecimentoFaker no campo Nome de Conhecimento
        E Clico em Criar de Conhecimento
        E Clico no botão + NOVO CONHECIMENTO
        E insiro misto no campo Nome de Conhecimento
        E Clico em Criar de Conhecimento
        Então Mensagem de criação foi exibida de Conhecimento
        ''')

@given(u'Que tenha um Tipo de turma cadastrado')
def step_impl(context):
    try:
        fake = Faker('pt_BR')
        TipoDeTurmaFaker = fake.name()
        context.variables['globalTipoTurma'] = TipoDeTurmaFaker
        token = context.variables['token_api']
        headers = {
            'Authorization': f'Bearer {token}'
        }
        myobj = {
            'nome': context.variables['globalTipoTurma']
            }
        requests.post(context.variables['url_api_TipoDeTurma'], json = myobj , headers = headers)
        time.sleep(1)
        
        #pegando o id criado , buscando pelo ultimo criado, invertendo a lista e pegando a primeira posição
        id_item = sorted(json.loads(requests.get(context.variables['url_api_TipoDeTurma'], headers=headers).content), key=lambda x: x['created_at'], reverse=True)

        context.variables['idTipoTurma'] = id_item[0]['id']
    except:
        raise Exception(id_item.content.decode('utf-8'))
@given(u'Que tenha dois tipos de turmas cadastrado')
def step_impl(context):
    context.execute_steps(u'''
        Quando Entro em Tipo de turma
        E Clico no botão + NOVO TIPO DE TURMA
        E digito TipoDeTurmaFaker no campo Nome de TipoDeTurma
        E Clico em Criar de TipoDeTurma
        E Clico no botão + NOVO TIPO DE TURMA
        E Insiro Profissional no campo Nome de TipoDeTurma
        E Clico em Criar de TipoDeTurma
        ''')
    time.sleep(1)

@given(u'Que tenha dois Generos cadastrado')
def step_impl(context):
    context.execute_steps(u'''
        Quando Entro em Genero
        E Clico no botão + NOVO GENERO
        E digito GeneroFaker no campo Nome de Genero
        E Clico em Criar de Genero
        E Clico no botão + NOVO GENERO
        E Insiro homem no campo Nome de Genero
        E Clico em Criar de Genero
        ''')
    time.sleep(1)
    
@given('que tenha uma pessoa fisica cadastrada')
def step_impl(context):
    context.execute_steps(u'''
        dado Que tenha um Estado civil cadastrado
        E Que tenha um Genero cadastrado
        ''')
    try:
        fake = Faker('pt_BR')
        fakeCPF = fake.cpf()
        context.variables['globalPessoaCPF'] = fakeCPF
        nomeFaker = fake.name()
        context.variables['globalPessoaNome'] = nomeFaker
        token = context.variables['token_api']
        headers = {
            'Authorization': f'Bearer {token}'
        }
        myobj = {
            "cpf": context.variables['globalPessoaCPF'],
            "nomepessoa": context.variables['globalPessoaNome'],
            "email": "carisa@gmail.com",
            "datanascimento": "1982-03-08",
            "nomemae": fake.name(),
            "nomepai": fake.name(),
            "nomeresponsavel": fake.name(),
            "rgnumero": "00123",
            "rgemissor": "SSP",
            "genero_id": context.variables['idGenero'],
            "estadocivil_id": context.variables['idEstadoCivil'],
            "naturalidade": "DOMINGO O'KON",
            "telefone": "",
            "whatsapp": "(84) 90610-4601",
            "cep": "61.532-020",
            "logradouro": "R. Sem Nome",
            "numero": "11",
            "complemento": "",
            "bairro": "Lagoa Nova",
            "cidade": "Natal",
            "uf": "RN",
            "nomemedico": "DR. MEDICO",
            "planosaude": "PLANO"
        }
        debug = requests.post(context.variables['url_api_pessoa_fisica'], json = myobj , headers = headers)
        time.sleep(1)


        #pegando o id criado , buscando pelo ultimo criado, invertendo a lista e pegando a primeira posição
        id_item = sorted(json.loads(requests.get(context.variables['url_api_pessoa_fisica'], headers=headers).content), key=lambda x: x['created_at'], reverse=True)

        context.variables['idPessoa'] = id_item[0]['id']
    except:
        raise Exception(id_item.content.decode('utf-8'))

@given('que tenha duas pessoa fisica cadastrada')
def step_impl(context):
    context.execute_steps(u'''
        Dado Que tenha um Genero cadastrado
        E Que tenha um Estado civil cadastrado
        ''')
    try:
        fake = Faker('pt_BR')
        fakeCPF = fake.cpf()
        context.variables['globalPessoaCPF'] = fakeCPF
        nomeFaker = fake.name()
        context.variables['globalPessoaNome'] = nomeFaker
        token = context.variables['token_api']
        headers = {
            'Authorization': f'Bearer {token}'
        }
        myobj = {
            "cpf": context.variables['globalPessoaCPF'],
            "nomepessoa": context.variables['globalPessoaNome'],
            "email": "carisa@gmail.com",
            "datanascimento": "1982-03-08",
            "nomemae": fake.name(),
            "nomepai": fake.name(),
            "nomeresponsavel": fake.name(),
            "rgnumero": "00123",
            "rgemissor": "SSP",
            "genero_id": context.variables['idGenero'],
            "estadocivil_id": context.variables['idEstadoCivil'],
            "naturalidade": "DOMINGO O'KON",
            "telefone": "",
            "whatsapp": "(84) 90610-4601",
            "cep": "61.532-020",
            "logradouro": "R. Sem Nome",
            "numero": "11",
            "complemento": "",
            "bairro": "Lagoa Nova",
            "cidade": "Natal",
            "uf": "RN",
            "nomemedico": "DR. MEDICO",
            "planosaude": "PLANO"
        }
        requests.post(context.variables['url_api_pessoa_fisica'], json = myobj , headers = headers)
        time.sleep(1)


        #pegando o id criado , buscando pelo ultimo criado, invertendo a lista e pegando a primeira posição
        id_item = sorted(json.loads(requests.get(context.variables['url_api_pessoa_fisica'], headers=headers).content), key=lambda x: x['created_at'], reverse=True)

        context.variables['idPessoa'] = id_item[0]['id']

        fake = Faker('pt_BR')
        fakeCPF = fake.cpf()
        context.variables['globalPessoaCPFNovo'] = fakeCPF
        nomeFaker = fake.name()
        context.variables['globalPessoaNomeNovo'] = nomeFaker
        myobj = {
            "cpf": context.variables['globalPessoaCPFNovo'],
            "nomepessoa": context.variables['globalPessoaNomeNovo'],
            "email": "carisa@gmail.com",
            "datanascimento": "1982-03-08",
            "nomemae": fake.name(),
            "nomepai": fake.name(),
            "nomeresponsavel": fake.name(),
            "rgnumero": "00123",
            "rgemissor": "SSP",
            "genero_id": context.variables['idGenero'],
            "estadocivil_id": context.variables['idEstadoCivil'],
            "naturalidade": "DOMINGO O'KON",
            "telefone": "",
            "whatsapp": "(84) 90610-4601",
            "cep": "61.532-020",
            "logradouro": "R. Sem Nome",
            "numero": "11",
            "complemento": "",
            "bairro": "Lagoa Nova",
            "cidade": "Natal",
            "uf": "RN",
            "nomemedico": "DR. MEDICO",
            "planosaude": "PLANO"
        }
        requests.post(context.variables['url_api_pessoa_fisica'], json = myobj , headers = headers)
        time.sleep(1)


        #pegando o id criado , buscando pelo ultimo criado, invertendo a lista e pegando a primeira posição
        id_item = sorted(json.loads(requests.get(context.variables['url_api_pessoa_fisica'], headers=headers).content), key=lambda x: x['created_at'], reverse=True)

        context.variables['idPessoaNova'] = id_item[0]['id']
    except:
        raise Exception(id_item.content.decode('utf-8'))

@given(u'Que tenha um Polo cadastrado')
def step_impl(context):
    try:
        fake = Faker('pt_BR')
        PoloFaker = fake.name()
        context.variables['globalPolo'] = PoloFaker
        token = context.variables['token_api']
        headers = {
            'Authorization': f'Bearer {token}'
        }
        myobj = {
        'nome': context.variables['globalPolo'],
        "email": "polo@polo.org",
        "telefone": "(99)99999-9999",
        "cep": "59.076-010",
        "logradouro": "R. Carvão de Pedra",
        "numero": "11",
        "complemento": "SALA 102",
        "bairro": "Lagoa Nova",
        "cidade": "Natal",
        "uf": "RN"
        }
        requests.post(context.variables['url_api_Polos'], json = myobj , headers = headers)
        time.sleep(1)
        
        #pegando o id criado , buscando pelo ultimo criado, invertendo a lista e pegando a primeira posição
        id_item = sorted(json.loads(requests.get(context.variables['url_api_Polos'], headers=headers).content), key=lambda x: x['created_at'], reverse=True)

        context.variables['idPolo'] = id_item[0]['id']
    except:
        raise Exception(id_item.content.decode('utf-8'))

@given(u'Que tenha uma Unidade cadastrado')
def step_impl(context):
    context.execute_steps(u'''
        Dado Que tenha um Polo cadastrado
    ''')
    try:
        fake = Faker('pt_BR')
        UnidadeFaker = fake.name()
        context.variables['globalUnidade'] = UnidadeFaker
        token = context.variables['token_api']
        headers = {
            'Authorization': f'Bearer {token}'
        }
        myobj = {
            "nome": context.variables['globalUnidade'],
            "polo_id": context.variables['idPolo'],
            "email": "unidade@unidade.org",
            "telefone": "(99)99999-9999",
            "cep": "59.076-010",
            "logradouro": "R. Carvão de Pedra",
            "numero": "11",
            "complemento": "SALA 102",  
            "bairro": "Lagoa Nova",
            "cidade": "Natal",
            "uf": "RN"
        }
        requests.post(context.variables['url_api_Unidades'], json = myobj , headers = headers)
        time.sleep(1)
        
        #pegando o id criado , buscando pelo ultimo criado, invertendo a lista e pegando a primeira posição
        id_item = sorted(json.loads(requests.get(context.variables['url_api_Unidades'], headers=headers).content), key=lambda x: x['created_at'], reverse=True)

        context.variables['idUnidade'] = id_item[0]['id']
    except:
        raise Exception(id_item.content.decode('utf-8'))

@given(u'Que tenha uma turma cadastrada')
def step_impl(context):
    context.execute_steps(u'''
        Dado Que tenha uma modalidade cadastrada
        E Que tenha uma Unidade cadastrado
        E que tenha duas pessoa fisica cadastrada
        E Que tenha um Naipe cadastrado
        E Que tenha um Tipo de turma cadastrado
        ''')
    try:
        fake = Faker('pt_BR')
        turmaFaker = fake.name()
        context.variables['globalTurma'] = turmaFaker
        token = context.variables['token_api']
        headers = {
            'Authorization': f'Bearer {token}'
        }
        myobj = {
            "nome": context.variables['globalTurma'],
            "polo_id": context.variables['idPolo'],
            "unidade_id": context.variables['idUnidade'],
            "modalidade_id": context.variables['idModalidade'],
            "coordenador_id": context.variables['idPessoa'],
            "professor_id": context.variables['idPessoaNova'],
            "horarioinicio": "13:51",
            "horariotermino": "16:39",
            "idademinima": 9,
            "idademaxima": 9,
            "segunda": 1,
            "terca": 1,
            "quarta": 1,
            "quinta": 1,
            "sexta": 0,
            "sabado": 0,
            "quantidademinima": 2,
            "quantidademaxima": 2,
            "naipe_id": context.variables['idNaipe'],
            "tipo_id": context.variables['idTipoTurma'],
            "ano": 2023
        }
        requests.post(context.variables['url_api_Turmas'], json = myobj , headers = headers)
        time.sleep(1)
        
        #pegando o id criado , buscando pelo ultimo criado, invertendo a lista e pegando a primeira posição
        id_item = sorted(json.loads(requests.get(context.variables['url_api_Turmas'], headers=headers).content), key=lambda x: x['created_at'], reverse=True)

        context.variables['idTurma'] = id_item[0]['id']
    except:
        raise Exception(id_item.content.decode('utf-8'))
@given(u'Que tenha um interesse cadastrado')
def step_impl(context):
    context.execute_steps(u'''
        Dado Que tenha uma turma cadastrada
        Quando Entro em Registrar interesse
        ''')
    try:
        token = context.variables['token_api']
        headers = {
            'Authorization': f'Bearer {token}'
        }
        myobj = {
            "turma_id": context.variables['idTurma'],
            "aluno_id": context.variables['idPessoa'],
            "observacao": "interesse na turma 18 do aluno 6"
        }
        criacao = requests.post(context.variables['url_api_Interesse'], json = myobj , headers = headers)
        time.sleep(1)
    except:
        raise Exception(criacao.content.decode('utf-8'))
@given(u'Que tenha uma VagaReservada cadastrada')
def step_impl(context):
    context.execute_steps(u'''
        Dado Que tenha uma turma cadastrada
        ''')
    try:
        token = context.variables['token_api']
        headers = {
            'Authorization': f'Bearer {token}'
        }
        myobj = {
            "turma_id": context.variables['idTurma'],
            "aluno_id": context.variables['idPessoa'],
            "observacao": "interesse na turma 18 do aluno 6"
        }
        criacao = requests.post(context.variables['url_api_VagaReservada'], json = myobj , headers = headers)
        time.sleep(1)
    except:
        raise Exception(criacao.content.decode('utf-8'))
@given(u'Que tenha uma Matricula cadastrada')
def step_impl(context):
    context.execute_steps(u'''
        Dado Que tenha uma turma cadastrada
        ''')
    try:
        token = context.variables['token_api']
        headers = {
            'Authorization': f'Bearer {token}'
        }
        myobj = {
            "turma_id": context.variables['idTurma'],
            "aluno_id": context.variables['idPessoa'],
            "observacao": "interesse na turma 18 do aluno 6"
        }
        criacao = requests.post(context.variables['url_api_Matricula'], json = myobj , headers = headers)
        time.sleep(1)
    except:
        raise Exception(criacao.content.decode('utf-8'))
@given(u'Que tenha um interesse e uma Matricula cadastrada')
def step_impl(context):
    context.execute_steps(u'''
        Dado Que tenha uma turma cadastrada
        Quando Entro em Registrar interesse
        E Clico no botão + NOVO INTERESSE
        E Digito 273.291.624-26 no campo CPF de interesse
        E Escolho PoloFaker no campo polo de interesse
        E Escolho caio no campo unidade de interesse
        E Escolho turma do chaves no campo turma de interesse 
        E Clico em criar de interesse
        E Entro em Matricular aluno
        E Clico no botão + NOVA MATRICULA
        E Digito 273.291.624-26 no campo CPF de Matricula
        E Escolho PoloFaker no campo polo de Matricula
        E Escolho caio no campo unidade de Matricula
        E Escolho turma do chaves no campo turma de Matricula 
        E Clico em criar de Matricula
        Então Mensagem de criação foi exibida de Matricula
        ''')

@given(u'Que tenha um interesse e uma reserva cadastrada')
def step_impl(context):
    context.execute_steps(u'''
        Dado Que tenha uma turma cadastrada
        Quando Entro em Registrar interesse
        E Clico no botão + NOVO INTERESSE
        E Digito 273.291.624-26 no campo CPF de interesse
        E Escolho PoloFaker no campo polo de interesse
        E Escolho caio no campo unidade de interesse
        E Escolho turma do chaves no campo turma de interesse 
        E Clico em criar de interesse
        E Entro em Matricular aluno
        E Entro em Registrar vaga
        E Clico no botão + NOVA RESERVA
        E Digito 273.291.624-26 no campo CPF de VagaReservada
        E Escolho PoloFaker no campo polo de VagaReservada
        E Escolho caio no campo unidade de VagaReservada
        E Escolho turma do chaves no campo turma de VagaReservada 
        E Clico em criar de VagaReservada
        Então Mensagem de criação foi exibida de VagaReservada
        ''')

@given(u'Que tenha uma Matricula e uma reserva cadastrada')
def step_impl(context):
    context.execute_steps(u'''
        Dado Que tenha uma turma cadastrada
        Quando Entro em Registrar interesse
        E Entro em Registrar vaga
        E Clico no botão + NOVA RESERVA
        E Digito 273.291.624-26 no campo CPF de VagaReservada
        E Escolho PoloFaker no campo polo de VagaReservada
        E Escolho caio no campo unidade de VagaReservada
        E Escolho turma do chaves no campo turma de VagaReservada 
        E Clico em criar de VagaReservada
        E Entro em Matricular aluno
        E Clico no botão + NOVA MATRICULA
        E Digito 273.291.624-26 no campo CPF de Matricula
        E Escolho PoloFaker no campo polo de Matricula
        E Escolho caio no campo unidade de Matricula
        E Escolho turma do chaves no campo turma de Matricula 
        E Clico em criar de Matricula
        Então Mensagem de criação foi exibida de Matricula
        ''')

@given(u'Que tenha uma tabela de preços cadastrada')
def step_impl(context):
    context.execute_steps(u'''
        Dado Que tenha uma modalidade cadastrada
        E Que tenha uma categoria cadastrada
        E Que tenha uma Unidade cadastrado
        ''')
    try:
        token = context.variables['token_api']
        headers = {
            'Authorization': f'Bearer {token}'
        }
        myobj = {
            "unidade_id": context.variables['idUnidade'],
            "modalidade_id": context.variables['idModalidade'],
            "categoria_id": context.variables['idCategoria'],
            "data_inicio": str(date.today() + timedelta(1)),
            "valor_matricula": "100.00",
            "valor_mensalidade": "500.00"
        }
        criacao = requests.post(context.variables['url_api_Precos'], json = myobj , headers = headers)
    except:
        raise Exception(criacao.content.decode('utf-8'))
        
@given(u'Que tenha duas tabelas de preços cadastradas')
def step_impl(context):
    context.execute_steps(u'''
        Dado Que tenha um Polo cadastrado
        E Que tenha uma modalidade cadastrada
        E Que tenha uma categoria cadastrada
        E Que tenha uma Unidade cadastrado
        Quando Entro em preços
        E Clico no botão + NOVA TABELA
        E Escolho o polo PoloFaker de preços
        E Escolho a unidade UnidadeFaker de preços
        E Escolho a modalidade ModalidadeFaker de preços
        E Escolho a categoria CategoriaFaker de preços
        E Digito o valor da mensalidade 2 de preços
        E Digito o valor da matricula 2 de preços
        E Escolho a data de inicio de preços
        E Clico em criar de preços
        E Clico no botão + NOVA TABELA
        E Escolho o polo PoloFaker de preços
        E Escolho a unidade UnidadeFaker de preços
        E Escolho a modalidade NovaModalidadeFaker de preços
        E Escolho a categoria CategoriaFaker de preços
        E Digito o valor da mensalidade 2 de preços
        E Digito o valor da matricula 2 de preços
        E Escolho a data de inicio de preços
        E Clico em criar de preços
        ''')


@given(u'Que tenha um plano de desconto cadastrado')
def step_impl(context):
    context.execute_steps(u'''
    Dado Que tenha uma modalidade cadastrada
    E Que tenha uma Unidade cadastrado
        ''')
    try:
        fake = Faker('pt_BR')
        descontoFaker = fake.name()
        context.variables['globalDescontos'] = descontoFaker
        token = context.variables['token_api']
        headers = {
            'Authorization': f'Bearer {token}'
        }
        myobj = {
            "unidade_id":context.variables['idUnidade'],
            "modalidade_id":context.variables['idModalidade'],
            "descricao":context.variables['globalDescontos'],
            "ano": "2023",
            "valor_desconto":"3",
            "n_meses":"4",
        }
        criacao = requests.post(context.variables['url_api_descontos'], json = myobj , headers = headers)
        time.sleep(1)
    except:
        raise Exception(criacao.content.decode('utf-8'))
@given(u'Que tenha dois plano de desconto cadastrado')
def step_impl(context):
    context.execute_steps(u'''
    Dado Que tenha uma modalidade cadastrada
    E Que tenha uma Unidade cadastrado
    Quando Entro em descontos
    E Clico no botão + NOVA TABELA
    E Escolho o polo PoloFaker de descontos
    E Escolho a unidade UnidadeFaker de descontos
    E Escolho a modalidade ModalidadeFaker de descontos
    E Escolho o nome do plano PlanoFaker de descontos
    E Digito o valor do desconto 33 de descontos
    E Clico em criar de descontos
    E Clico no botão + NOVA TABELA
    E Escolho o polo PoloFaker de descontos
    E Escolho a unidade UnidadeFaker de descontos
    E Escolho a modalidade ModalidadeFaker de descontos
    E Escolho o segundo nome do plano {plano} de descontos
    E Digito o valor do desconto 33 de descontos
    E Clico em criar de descontos
    Então Mensagem de criação foi exibida de descontos
        ''')


@given(u'que tenha uma tabela de preço e plano de desconto cadastrado')
def step_impl(context):
    context.execute_steps(u'''
    Dado Que tenha um Conhecimento cadastrado
    E Que tenha um MetodoPagamento cadastrado
    E Que tenha uma categoria cadastrada
        ''')
    try:
        fake = Faker('pt_BR')
        descontoFaker = fake.name()
        context.variables['globalDescontos'] = descontoFaker
        token = context.variables['token_api']
        headers = {
            'Authorization': f'Bearer {token}'
        }
        myobj = {
            "unidade_id":context.variables['idUnidade'],
            "modalidade_id":context.variables['idModalidade'],
            "descricao":context.variables['globalDescontos'],
            "ano": "2023",
            "valor_desconto":"3",
            "n_meses":"4",
        }
        criacao1 = requests.post(context.variables['url_api_descontos'], json = myobj , headers = headers)
        time.sleep(1)

        myobj = {
            "unidade_id": context.variables['idUnidade'],
            "modalidade_id": context.variables['idModalidade'],
            "categoria_id": context.variables['idCategoria'],
            "data_inicio": str(date.today()),
            "valor_matricula": "100.00",
            "valor_mensalidade": "500.00"
        }
        criacao2 = requests.post(context.variables['url_api_Precos'], json = myobj , headers = headers)
    except:
        raise Exception(criacao1.content.decode('utf-8'), criacao2.content.decode('utf-8'))
################################################


###############Download de arquivo#################
@when(u'Clico no botão PDF')
def step_impl(context):
    context.browser.find_element('xpath', '/html/body/div/div/div/div/main/div/div/form/div/div[1]/div[2]/div[4]/button/span').click()
    time.sleep(2)

@when(u'Clico no botão XLS')
def step_impl(context):
    context.browser.find_element('xpath', '/html/body/div/div/div/div/main/div/div/form/div/div[1]/div[2]/div[3]/button').click()
    time.sleep(2)

@then(u'verifico que o arquivo {arq} foi baixado')
def step_impl(context, arq):
    caminho_downloads = os.path.join(os.path.expanduser("~"), "Downloads")+"/"+arq
    assert os.path.exists(caminho_downloads)

@then(u'apago o arquivo {arq}')
def step_impl(context, arq):
    caminho_downloads = os.path.join(os.path.expanduser("~"), "Downloads")+"/"+arq
    os.remove(caminho_downloads)
################################################
