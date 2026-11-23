import os

from pytest_bdd import given, parsers, then, when

from pages.aceder_as_tarefas import IniciarSessaoPage, ListaDeTarefasPage


@given('o utilizador está na página "Iniciar sessão"')
def o_utilizador_esta_na_pagina_iniciar_sessao(page, app_url):
    pagina = IniciarSessaoPage(page, app_url)
    pagina.abrir("/xtwins-site-simples/login.html")
    pagina.verificar_pagina("/xtwins-site-simples/login.html")


@when(parsers.parse('o utilizador preenche o campo "Email" com o email do utilizador'))
def o_utilizador_preenche_o_campo_email_com_o_email_do_utilizador(page, app_url):
    IniciarSessaoPage(page, app_url).preencher_email(os.environ["LOGIN_EMAIL"])


@when(parsers.parse('preenche o campo "Password" com a palavra-passe do utilizador'))
def preenche_o_campo_password_com_a_palavra_passe_do_utilizador(page, app_url):
    IniciarSessaoPage(page, app_url).preencher_password(os.environ["LOGIN_PASSWORD"])


@when(parsers.parse('seleciona o botão "Entrar"'))
def seleciona_o_botao_entrar(page, app_url):
    IniciarSessaoPage(page, app_url).selecionar_entrar()


@then(parsers.parse('a página "Lista de tarefas" é apresentada'))
def a_pagina_lista_de_tarefas_e_apresentada(page, app_url):
    ListaDeTarefasPage(page, app_url).verificar_pagina("/xtwins-site-simples/tarefas.html")


@given(parsers.parse('o utilizador acede à página "Lista de tarefas" sem sessão iniciada'))
def o_utilizador_acede_a_pagina_lista_de_tarefas_sem_sessao_iniciada(page, app_url):
    ListaDeTarefasPage(page, app_url).abrir("/xtwins-site-simples/tarefas.html")


@when(parsers.parse('a página é apresentada'))
def a_pagina_e_apresentada(page, app_url):
    ListaDeTarefasPage(page, app_url).verificar_pagina("/xtwins-site-simples/tarefas.html")


@then(parsers.parse('a página "Lista de tarefas" é apresentada sem exigir autenticação'))
def a_pagina_lista_de_tarefas_e_apresentada_sem_exigir_autenticacao(page, app_url):
    ListaDeTarefasPage(page, app_url).verificar_pagina("/xtwins-site-simples/tarefas.html")


@when(parsers.parse('o utilizador seleciona a ligação "Continuar sem sessão"'))
def o_utilizador_seleciona_a_ligacao_continuar_sem_sessao(page, app_url):
    IniciarSessaoPage(page, app_url).continuar_sem_sessao()


@then(parsers.parse('a área "As minhas tarefas" é apresentada com a lista de tarefas'))
def a_area_as_minhas_tarefas_e_apresentada_com_a_lista_de_tarefas(page, app_url):
    ListaDeTarefasPage(page, app_url).verificar_area_minhas_tarefas()


@then(parsers.parse('as colunas "Tarefa", "Prioridade", "Data limite" e "Ações" são apresentadas'))
def as_colunas_tarefa_prioridade_data_limite_e_acoes_sao_apresentadas(page, app_url):
    ListaDeTarefasPage(page, app_url).verificar_colunas()


@then(parsers.parse('a indicação de "{total:d} tarefas por fazer" é apresentada'))
def a_indicacao_de_tarefas_por_fazer_e_apresentada(page, app_url, total):
    ListaDeTarefasPage(page, app_url).verificar_tarefas_por_fazer(total)
