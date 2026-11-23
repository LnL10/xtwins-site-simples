from pytest_bdd import given, when, then, parsers

from pages.tarefas import ListaDeTarefasPage, NovaTarefaPage


@given(parsers.parse('o utilizador acede à página "Lista de tarefas" sem sessão iniciada'))
def acede_a_lista_de_tarefas(page, app_url):
    ListaDeTarefasPage(page, app_url).abrir("/xtwins-site-simples/tarefas.html")


@when("a página é apresentada")
def pagina_lista_e_apresentada(page, app_url):
    ListaDeTarefasPage(page, app_url).verificar_url("/xtwins-site-simples/tarefas.html")


@then(parsers.parse('a área "As minhas tarefas" é apresentada com a lista de tarefas'))
def area_minhas_tarefas_e_apresentada(page, app_url):
    ListaDeTarefasPage(page, app_url).verificar_area_minhas_tarefas()


@then(parsers.parse('as colunas "Tarefa", "Prioridade", "Data limite" e "Ações" são apresentadas'))
def colunas_sao_apresentadas(page, app_url):
    ListaDeTarefasPage(page, app_url).verificar_colunas()


@then(parsers.parse('a indicação de "{total:d} tarefas por fazer" é apresentada'))
def indicacao_de_tarefas_e_apresentada(page, app_url, total):
    ListaDeTarefasPage(page, app_url).verificar_indicacao_tarefas(total)


@when(parsers.parse('o utilizador seleciona a ligação "Nova tarefa"'))
def seleciona_ligacao_nova_tarefa(page, app_url):
    ListaDeTarefasPage(page, app_url).abrir_nova_tarefa()


@then(parsers.parse('a página "Nova tarefa" é apresentada'))
def pagina_nova_tarefa_e_apresentada(page, app_url):
    NovaTarefaPage(page, app_url).verificar_url("/xtwins-site-simples/nova-tarefa.html")


@when(parsers.parse('o utilizador preenche o campo "Título" com "{titulo}"'))
def preenche_titulo(page, app_url, titulo):
    NovaTarefaPage(page, app_url).preencher_titulo(titulo)


@when(parsers.parse('o utilizador seleciona "{prioridade}" na lista de seleção "Prioridade"'))
@when(parsers.parse('seleciona "{prioridade}" na lista de seleção "Prioridade"'))
def seleciona_prioridade(page, app_url, prioridade):
    NovaTarefaPage(page, app_url).selecionar_prioridade(prioridade)


@when(parsers.parse('preenche o campo "Data limite" com "{data}"'))
def preenche_data_limite(page, app_url, data):
    NovaTarefaPage(page, app_url).preencher_data_limite(data)


@when(parsers.parse('seleciona o botão "Guardar"'))
def seleciona_botao_guardar(page, app_url):
    NovaTarefaPage(page, app_url).guardar()


@then(parsers.parse('a página "Lista de tarefas" é apresentada'))
def pagina_lista_de_tarefas_e_apresentada(page, app_url):
    ListaDeTarefasPage(page, app_url).verificar_url("/xtwins-site-simples/tarefas.html")


@then(parsers.parse('a tarefa "{titulo}" é apresentada na coluna "Tarefa"'))
def tarefa_e_apresentada_na_coluna_tarefa(page, app_url, titulo):
    ListaDeTarefasPage(page, app_url).verificar_tarefa_visivel(titulo)


@then(parsers.parse('a tarefa apresenta "{prioridade}" na coluna "Prioridade"'))
def tarefa_apresenta_prioridade(page, app_url, prioridade):
    ListaDeTarefasPage(page, app_url).verificar_prioridade(prioridade)


@then(parsers.parse('a tarefa apresenta "{data}" na coluna "Data limite"'))
def tarefa_apresenta_data_limite(page, app_url, data):
    ListaDeTarefasPage(page, app_url).verificar_data_na_tarefa("Preparar relatório", data)


@then(parsers.parse('a página "Nova tarefa" continua apresentada'))
def pagina_nova_tarefa_continua_apresentada(page, app_url):
    NovaTarefaPage(page, app_url).verificar_url("/xtwins-site-simples/nova-tarefa.html")


@when('o utilizador consulta a lista de seleção "Prioridade"')
def consulta_lista_prioridade(page, app_url):
    NovaTarefaPage(page, app_url).consultar_prioridade()


@then(parsers.parse('a lista de seleção "Prioridade" apresenta as opções "Baixa", "Média" e "Alta"'))
def lista_prioridade_apresenta_opcoes(page, app_url):
    NovaTarefaPage(page, app_url).verificar_opcoes_prioridade()


@then(parsers.parse('a lista de seleção "Prioridade" apresenta a opção "{prioridade}" selecionada'))
def lista_prioridade_apresenta_opcao_selecionada(page, app_url, prioridade):
    NovaTarefaPage(page, app_url).verificar_prioridade_selecionada(prioridade)


@then(parsers.parse('a tarefa "{titulo}" é apresentada sem data limite na coluna "Data limite"'))
def tarefa_sem_data_limite(page, app_url, titulo):
    ListaDeTarefasPage(page, app_url).verificar_data_sem_limite(titulo)
