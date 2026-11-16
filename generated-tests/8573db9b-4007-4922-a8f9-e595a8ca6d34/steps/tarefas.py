from pytest_bdd import given, parsers, then, when

from pages.lista_de_tarefas import ListaDeTarefas
from pages.nova_tarefa import NovaTarefa


@given(
    'que existem as tarefas "Preparar relatório", "Comprar leite" e '
    '"Enviar fatura", com as prioridades "Alta", "Média" e "Baixa", '
    'respetivamente, e que "Enviar fatura" está concluída'
)
def existem_as_tarefas_com_prioridades():
    pass


@given(
    'que os dados das tarefas "Rever requisitos", "Preparar demonstração" e '
    '"Enviar relatório semanal" estão guardados no navegador, com prioridades '
    '"Alta", "Média" e "Baixa", respetivamente, sem datas limite, e que '
    'apenas "Enviar relatório semanal" está concluída'
)
def dados_das_tarefas_estao_guardados_no_navegador():
    pass


@given("que estou a usar um navegador novo")
def estou_a_usar_um_navegador_novo():
    pass


@when(parsers.parse('abro a página "{pagina}"'))
def abro_a_pagina(pagina, page, app_url):
    if pagina == "Lista de tarefas":
        ListaDeTarefas(page, app_url).open()


@when(parsers.parse('seleciono o link "{link}" na página "{pagina}"'))
def seleciono_o_link_na_pagina(link, pagina, page, app_url):
    if pagina == "Lista de tarefas" and link == "Nova tarefa":
        ListaDeTarefas(page, app_url).selecionar_link_nova_tarefa()


@when(parsers.parse('seleciono a opção "{prioridade}" na lista "Prioridade" da página "Nova tarefa"'))
def seleciono_a_opcao_na_lista_prioridade(prioridade, page, app_url):
    NovaTarefa(page, app_url).selecionar_prioridade(prioridade)


@then(parsers.parse('a opção "{prioridade}" está selecionada na lista "Prioridade" da página "Nova tarefa"'))
def opcao_esta_selecionada_na_lista_prioridade(prioridade, page, app_url):
    NovaTarefa(page, app_url).assert_prioridade_selecionada(prioridade)


@then(
    'vejo a página "Nova tarefa" e o formulário com o campo "Título", '
    'a lista "Prioridade" e o campo "Data limite"'
)
def vejo_a_pagina_nova_tarefa(page, app_url):
    NovaTarefa(page, app_url).assert_pagina()


@then(
    parsers.parse(
        'vejo a tarefa "{titulo}" com prioridade "{prioridade}" e data limite '
        '"{data_limite}" na página "Lista de tarefas"'
    )
)
def vejo_a_tarefa_com_prioridade_e_data_limite(
    titulo, prioridade, data_limite, page, app_url
):
    ListaDeTarefas(page, app_url).assert_tarefa(titulo, prioridade, data_limite)


@then(parsers.parse('a caixa de verificação da tarefa "{titulo}" está desmarcada'))
def caixa_de_verificacao_da_tarefa_esta_desmarcada(titulo, page, app_url):
    ListaDeTarefas(page, app_url).assert_caixa_desmarcada(titulo)


@then(parsers.parse('a caixa de verificação da tarefa "{titulo}" está marcada'))
def caixa_de_verificacao_da_tarefa_esta_marcada(titulo, page, app_url):
    ListaDeTarefas(page, app_url).assert_caixa_marcada(titulo)


@then(parsers.parse('o título "{titulo}" não aparece riscado'))
def titulo_nao_aparece_riscado(titulo, page, app_url):
    ListaDeTarefas(page, app_url).assert_titulo_riscado(titulo, riscado=False)


@then(parsers.parse('o título "{titulo}" aparece riscado'))
def titulo_aparece_riscado(titulo, page, app_url):
    ListaDeTarefas(page, app_url).assert_titulo_riscado(titulo, riscado=True)


@then(parsers.parse('o resumo apresenta "{resumo}"'))
def resumo_apresenta_texto(resumo, page, app_url):
    ListaDeTarefas(page, app_url).assert_resumo(resumo)
