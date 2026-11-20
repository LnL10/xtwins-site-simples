from pytest_bdd import given, parsers, then, when

from pages.tarefas import ListaDeTarefas, NovaTarefa


@given(parsers.parse('que acedo à página "{pagina}"'))
def acedo_a_pagina(page, app_url, pagina):
    ListaDeTarefas(page, app_url).aceder_a_pagina(pagina)


@when("a página é apresentada")
def pagina_e_apresentada(page, app_url):
    ListaDeTarefas(page, app_url).verificar_pagina()


@then('vejo uma tabela com as colunas "Tarefa", "Prioridade", "Data limite" e "Ações"')
def vejo_tabela_com_colunas(page, app_url):
    ListaDeTarefas(page, app_url).verificar_colunas()


@then(parsers.parse('seleciono a ligação "{ligacao}"'))
def seleciono_ligacao(page, app_url, ligacao):
    ListaDeTarefas(page, app_url).selecionar_ligacao(ligacao)


@then(parsers.parse('vejo o formulário "{formulario}" na página "{pagina}"'))
def vejo_formulario_na_pagina(page, app_url, formulario, pagina):
    NovaTarefa(page, app_url).verificar_formulario(formulario, pagina)


@then(parsers.parse('preencho o campo "{campo}" com "{valor}"'))
def preencho_campo(page, app_url, campo, valor):
    NovaTarefa(page, app_url).preencher_campo(campo, valor)


@then(parsers.parse('seleciono a opção "{opcao}" no seletor "{seletor}"'))
def seleciono_opcao_no_seletor(page, app_url, opcao, seletor):
    NovaTarefa(page, app_url).selecionar_opcao(seletor, opcao)


@when(parsers.parse('seleciono o botão "{botao}"'))
def seleciono_botao(page, app_url, botao):
    NovaTarefa(page, app_url).selecionar_botao(botao)


@then(parsers.parse('vejo na tabela da página "{pagina}" uma tarefa com prioridade "{prioridade}" e sem data limite'))
def vejo_tarefa_com_prioridade_e_sem_data_limite(page, app_url, pagina, prioridade):
    ListaDeTarefas(page, app_url).verificar_tarefa_sem_data_limite(pagina, prioridade)


@then(parsers.parse('vejo no seletor "{seletor}" as opções "{opcao_baixa}", "{opcao_media}" e "{opcao_alta}", com "{opcao_selecionada}" selecionada por predefinição'))
def vejo_opcoes_de_prioridade(page, app_url, seletor, opcao_baixa, opcao_media, opcao_alta, opcao_selecionada):
    NovaTarefa(page, app_url).verificar_opcoes_do_seletor(
        seletor, (opcao_baixa, opcao_media, opcao_alta), opcao_selecionada
    )
