from pytest_bdd import given, parsers, then, when

from pages.nova_tarefa import NovaTarefa
from pages.tarefas import ListaDeTarefas


@given(parsers.parse('que acedo ao endereço "{endereco}"'))
def acedo_ao_endereco(page, app_url, endereco):
    ListaDeTarefas(page, app_url).abrir()


@given("que utilizo um navegador")
def utilizo_um_navegador():
    pass


@when(parsers.parse('a página "Lista de tarefas" é aberta'))
def pagina_lista_de_tarefas_e_aberta(page, app_url):
    ListaDeTarefas(page, app_url).verificar_pagina_aberta()


@then('é apresentada a tabela com as colunas "Tarefa", "Prioridade", "Data limite" e "Ações"')
def tabela_com_colunas_esperadas(page, app_url):
    ListaDeTarefas(page, app_url).verificar_colunas()


@then("são apresentadas as tarefas iniciais e registo os nomes e estados apresentados")
def tarefas_iniciais_apresentadas(page, app_url):
    ListaDeTarefas(page, app_url).verificar_estados_iniciais()


@when(parsers.parse('abro um navegador novo e acedo ao endereço "{endereco}"'))
def abro_navegador_novo_e_acedo_ao_endereco(page, app_url, endereco):
    ListaDeTarefas(page, app_url).abrir()


@then(parsers.parse('são apresentadas "{total:d}" tarefas com os mesmos nomes e estados que no navegador anterior'))
def tarefas_apresentadas_com_estados_iguais(page, app_url, total):
    ListaDeTarefas(page, app_url).verificar_total_e_estados(total)


@when(parsers.parse('seleciono a ligação "{nome}"'))
def seleciono_a_ligacao(page, app_url, nome):
    ListaDeTarefas(page, app_url).selecionar_ligacao(nome)


@then(parsers.parse('é apresentada a página "{nome}"'))
def pagina_nova_tarefa_apresentada(page, app_url, nome):
    NovaTarefa(page, app_url).verificar_pagina_aberta()


@then(parsers.parse('a opção "{valor}" está selecionada por predefinição na "seleção de prioridade"'))
def prioridade_predefinida_selecionada(page, app_url, valor):
    NovaTarefa(page, app_url).verificar_prioridade(valor)


@when(parsers.parse('seleciono "{valor}" na "seleção de prioridade"'))
def seleciono_prioridade(page, app_url, valor):
    NovaTarefa(page, app_url).selecionar_prioridade(valor)


@then(parsers.parse('a opção "{valor}" está selecionada na "seleção de prioridade"'))
def prioridade_selecionada(page, app_url, valor):
    NovaTarefa(page, app_url).verificar_prioridade(valor)
