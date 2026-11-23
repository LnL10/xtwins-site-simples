import os

from pytest_bdd import given, when, then, parsers

from pages.login import LoginPage
from pages.tarefas import TarefasPage


@given('o utilizador está na página "Iniciar sessão"')
def utilizador_esta_na_pagina_iniciar_sessao(page, app_url):
    LoginPage(page, app_url).open("/xtwins-site-simples/login.html")
    LoginPage(page, app_url).assert_current_page("/xtwins-site-simples/login.html")


@when('o utilizador seleciona a ligação "Continuar sem sessão"')
def utilizador_seleciona_a_ligacao_continuar_sem_sessao(page, app_url):
    LoginPage(page, app_url).click_continuar_sem_sessao()


@then('a área "As minhas tarefas" é apresentada com a lista de tarefas')
def area_as_minhas_tarefas_e_apresentada_com_a_lista_de_tarefas(page, app_url):
    tarefas = TarefasPage(page, app_url)
    tarefas.assert_area_as_minhas_tarefas_visible()
    tarefas.assert_table_visible()


@then('as colunas "Tarefa", "Prioridade", "Data limite" e "Ações" são apresentadas')
def as_colunas_sao_apresentadas(page, app_url):
    TarefasPage(page, app_url).assert_columns_visible()


@then(parsers.parse('a indicação de "{total:d} tarefas por fazer" é apresentada'))
def a_indicacao_de_tarefas_por_fazer_e_apresentada(page, app_url, total):
    TarefasPage(page, app_url).assert_tasks_remaining_text(total)


@given('o utilizador acede à página "Lista de tarefas" sem sessão iniciada')
def utilizador_acede_a_lista_de_tarefas_sem_sessao(page, app_url):
    TarefasPage(page, app_url).open("/xtwins-site-simples/tarefas.html")


@then('a página é apresentada')
def a_pagina_e_apresentada(page, app_url):
    TarefasPage(page, app_url).assert_current_page("/xtwins-site-simples/tarefas.html")


@when('o utilizador seleciona a ligação "Iniciar sessão"')
def utilizador_seleciona_a_ligacao_iniciar_sessao(page, app_url):
    TarefasPage(page, app_url).click_iniciar_sessao()


@then('a página "Iniciar sessão" é apresentada')
def a_pagina_iniciar_sessao_e_apresentada(page, app_url):
    LoginPage(page, app_url).assert_current_page("/xtwins-site-simples/login.html")


@then(parsers.parse('o campo "{campo}" é apresentado'))
def o_campo_e_apresentado(page, app_url, campo):
    LoginPage(page, app_url).assert_field_visible(campo)


@then(parsers.parse('o botão "{botao}" é apresentado'))
def o_botao_e_apresentado(page, app_url, botao):
    LoginPage(page, app_url).assert_button_visible(botao)


@then(parsers.parse('a ligação "{ligacao}" é apresentada'))
def a_ligacao_e_apresentada(page, app_url, ligacao):
    LoginPage(page, app_url).assert_link_visible(ligacao)


@when(parsers.parse('o utilizador preenche o campo "{campo}" com o email do utilizador'))
def utilizador_preenche_o_campo_com_o_email_do_utilizador(page, app_url, campo):
    LoginPage(page, app_url).fill_field(campo, os.environ["LOGIN_EMAIL"])


@when(parsers.parse('preenche o campo "{campo}" com a palavra-passe do utilizador'))
def preenche_o_campo_com_a_palavra_passe_do_utilizador(page, app_url, campo):
    LoginPage(page, app_url).fill_field(campo, os.environ["LOGIN_PASSWORD"])


@when(parsers.parse('seleciona o botão "{botao}"'))
def seleciona_o_botao(page, app_url, botao):
    LoginPage(page, app_url).click_button(botao)


@then('a página "Lista de tarefas" é apresentada')
def a_pagina_lista_de_tarefas_e_apresentada(page, app_url):
    TarefasPage(page, app_url).assert_current_page("/xtwins-site-simples/tarefas.html")
