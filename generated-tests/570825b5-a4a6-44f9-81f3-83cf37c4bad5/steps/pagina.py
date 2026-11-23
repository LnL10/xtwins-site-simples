from pytest_bdd import when

from pages.tarefas import TarefasPage


@when("a página é apresentada")
def a_pagina_e_apresentada(page, app_url):
    TarefasPage(page, app_url).assert_current_page("/xtwins-site-simples/tarefas.html")
