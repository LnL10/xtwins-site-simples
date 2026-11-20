from pytest_bdd import given, parsers, then, when

from pages.iniciar_sessao import IniciarSessao
from pages.nova_tarefa import NovaTarefa
from pages.tarefas import Tarefas


def _pagina(page, app_url, nome):
    paginas = {
        "Iniciar sessão": IniciarSessao(page, app_url),
        "Nova tarefa": NovaTarefa(page, app_url),
        "Lista de tarefas": Tarefas(page, app_url),
    }
    if nome not in paginas:
        raise ValueError(f"Página não reconhecida: {nome}")
    return paginas[nome]


@given(parsers.parse('estou na página "{pagina}"'))
def estou_na_pagina(page, app_url, pagina):
    _pagina(page, app_url, pagina).open()


@given(parsers.parse('abro a página "{pagina}" sem iniciar sessão'))
def abro_pagina_sem_iniciar_sessao(page, app_url, pagina):
    _pagina(page, app_url, pagina).open()


@when('seleciono "Continuar sem sessão"')
def seleciono_continuar_sem_sessao(page, app_url):
    IniciarSessao(page, app_url).continuar_sem_sessao()


@then(parsers.parse('é apresentada a página "{pagina}"'))
def e_apresentada_a_pagina(page, app_url, pagina):
    _pagina(page, app_url, pagina).assert_open()


@then(parsers.parse('continua apresentada a página "{pagina}"'))
def continua_apresentada_a_pagina(page, app_url, pagina):
    _pagina(page, app_url, pagina).assert_open()


@then(parsers.parse('são apresentadas {total} tarefas, cada uma com a respetiva prioridade, data-limite e uma caixa de verificação que indica o estado'))
def sao_apresentadas_tarefas(page, total):
    Tarefas(page).assert_listing(total)


@then(parsers.parse('é indicada a existência de "{texto}"'))
def e_indicada_a_existencia(page, texto):
    Tarefas(page).assert_summary(texto)


@then(parsers.parse('o campo "Prioridade" apresenta as opções "Baixa", "Média" e "Alta", com "{selecionada}" selecionada por predefinição'))
def prioridade_apresenta_opcoes(page, selecionada):
    NovaTarefa(page).assert_priority_options(selecionada)


@when(parsers.parse('seleciono "{prioridade}" no campo "Prioridade"'))
def seleciono_prioridade(page, prioridade):
    NovaTarefa(page).select_priority(prioridade)


@then(parsers.parse('o campo "Prioridade" apresenta "{prioridade}" selecionada'))
def prioridade_apresenta_selecionada(page, prioridade):
    NovaTarefa(page).assert_priority_value(prioridade)


@when(parsers.re(r'preencho o campo "Título" com "(?P<titulo>.*?)"(?: e o campo "Data limite" com "(?P<data>.*?)")? e seleciono "Guardar"'))
def preencho_titulo_e_guardo(page, titulo, data):
    nova_tarefa = NovaTarefa(page)
    if data is None:
        nova_tarefa.save_title(titulo)
    else:
        nova_tarefa.save_title_and_due_date(titulo, data)


@then(parsers.parse('a tarefa "{titulo}" é apresentada na tabela da página "Lista de tarefas" com a coluna "Data limite" vazia'))
def tarefa_apresentada_com_data_limite_vazia(page, titulo):
    Tarefas(page).assert_task_without_due_date(titulo)


@then(parsers.parse('a tarefa "{titulo}" é apresentada na página "Lista de tarefas"'))
def tarefa_apresentada_na_lista(page, titulo):
    Tarefas(page).assert_task_visible(titulo)
