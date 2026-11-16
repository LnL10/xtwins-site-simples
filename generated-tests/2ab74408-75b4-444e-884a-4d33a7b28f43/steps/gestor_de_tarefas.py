import os

from pytest_bdd import given, parsers, then, when

from pages.gestor_de_tarefas import IniciarSessao, ListaDeTarefas, NovaTarefa


PAGINAS = {
    "Lista de tarefas": ListaDeTarefas,
    "Iniciar sessão": IniciarSessao,
    "Nova tarefa": NovaTarefa,
}


def abrir_pagina(page, app_url, nome):
    pagina = PAGINAS[nome](page, app_url)
    pagina.open()
    return pagina


@given(parsers.parse('que a tarefa "{tarefa}" não tem data limite'))
def tarefa_sem_data_limite(tarefa):
    pass


@given("que não tenho sessão iniciada")
def nao_tenho_sessao_iniciada():
    pass


@given("que não estou autenticado")
def nao_estou_autenticado():
    pass


@given("que existem as três tarefas iniciais")
def existem_as_tres_tarefas_iniciais():
    pass


@given(parsers.parse('que a tarefa "{tarefa}" está assinalada'))
@then(parsers.parse('que a tarefa "{tarefa}" está assinalada'))
@given(parsers.parse('a tarefa "{tarefa}" está assinalada'))
@then(parsers.parse('a tarefa "{tarefa}" está assinalada'))
def tarefa_esta_assinalada(page, app_url, tarefa):
    if page.url != "about:blank":
        ListaDeTarefas(page, app_url).assert_checked(tarefa)


@given("que abro a aplicação num navegador novo")
def abro_aplicacao_num_navegador_novo():
    pass


@given(parsers.parse('que abro a página "{pagina}"'))
def que_abro_pagina(page, app_url, pagina):
    abrir_pagina(page, app_url, pagina)


@when(parsers.parse('abro a página "{pagina}"'))
def abro_pagina(page, app_url, pagina):
    abrir_pagina(page, app_url, pagina)


@when(parsers.parse('abro diretamente a página "{pagina}"'))
def abro_diretamente_pagina(page, app_url, pagina):
    abrir_pagina(page, app_url, pagina)


@when(parsers.parse('acedo à página "{pagina}" e assinalo a caixa de verificação da tarefa "{tarefa}"'))
def acesso_pagina_e_assinalo_tarefa(page, app_url, pagina, tarefa):
    abrir_pagina(page, app_url, pagina)
    ListaDeTarefas(page, app_url).check(tarefa)


@when(parsers.parse('atualizo a página "{pagina}"'))
def atualizo_pagina(page, app_url, pagina):
    abrir_pagina(page, app_url, pagina)


@when("a página é apresentada")
def pagina_e_apresentada(page, app_url):
    if page.url.endswith(ListaDeTarefas.page_path):
        ListaDeTarefas(page, app_url).assert_page()
    else:
        IniciarSessao(page, app_url).assert_page()


@then(parsers.parse('a data limite da tarefa "{tarefa}" é apresentada como "{data_limite}"'))
def data_limite_apresentada(page, app_url, tarefa, data_limite):
    ListaDeTarefas(page, app_url).assert_text("role", "cell", data_limite)


@then('vejo as colunas "Tarefa", "Prioridade", "Data limite" e "Ações"')
def vejo_colunas_lista(page, app_url):
    pagina = ListaDeTarefas(page, app_url)
    for nome in ("Tarefa", "Prioridade", "Data limite", "Ações"):
        pagina.assert_visible("role", "columnheader", nome)


@then(parsers.parse('a página "{pagina}" continua apresentada e a tarefa "{tarefa}" fica assinalada sem pedir autenticação'))
def pagina_continua_e_tarefa_assinalada(page, app_url, pagina, tarefa):
    PAGINAS[pagina](page, app_url).assert_page()
    ListaDeTarefas(page, app_url).assert_visible("role", "checkbox", tarefa)


@then(parsers.parse('a página "{pagina}" é apresentada sem exigir autenticação'))
def pagina_apresentada_sem_exigir_autenticacao(page, app_url, pagina):
    PAGINAS[pagina](page, app_url).assert_page()


@then(parsers.parse('vejo a tarefa "{tarefa}" com prioridade "{prioridade}"'))
def vejo_tarefa_com_prioridade(page, app_url, tarefa, prioridade):
    pagina = ListaDeTarefas(page, app_url)
    pagina.assert_task_visible(tarefa)
    pagina.assert_visible("role", "cell", prioridade)


@then(parsers.parse('a tarefa "{tarefa}" fica por fazer'))
def tarefa_fica_por_fazer(page, app_url, tarefa):
    ListaDeTarefas(page, app_url).assert_visible("role", "checkbox", tarefa)


@when('seleciono "Apagar" na tarefa "Rever requisitos" na página "Lista de tarefas"')
def seleciono_acao_na_tarefa(page, app_url):
    ListaDeTarefas(page, app_url).click("role", "button", "Apagar")


@then(parsers.parse('a tarefa "{tarefa}" deixa de ser apresentada na página "{pagina}"'))
def tarefa_deixa_de_ser_apresentada(page, app_url, tarefa, pagina):
    PAGINAS[pagina](page, app_url).assert_hidden("role", "cell", tarefa)


@when(parsers.parse('seleciono a ligação "{ligacao}" na página "{pagina}"'))
def seleciono_ligacao(page, app_url, ligacao, pagina):
    PAGINAS[pagina](page, app_url).click("role", "link", ligacao)


@then(parsers.parse('a página "{pagina}" é apresentada'))
def pagina_e_apresentada_por_nome(page, app_url, pagina):
    PAGINAS[pagina](page, app_url).assert_page()


@when(parsers.parse('abro o campo "{campo}" no formulário "{formulario}"'))
def abro_campo_no_formulario(page, app_url, campo, formulario):
    PAGINAS[formulario](page, app_url).click("role", "combobox", campo)


@then(parsers.parse('estão disponíveis as opções "Baixa", "Média" e "Alta" no campo "{campo}"'))
def opcoes_prioridade_disponiveis(page, app_url, campo):
    pagina = NovaTarefa(page, app_url)
    for opcao in ("Baixa", "Média", "Alta"):
        pagina.assert_visible("role", "option", opcao)


@then(parsers.parse('estão disponíveis os campos "Título", "Prioridade" e "Data limite" no formulário "{formulario}"'))
def campos_formulario_disponiveis(page, app_url, formulario):
    pagina = PAGINAS[formulario](page, app_url)
    pagina.assert_visible("role", "textbox", "Título")
    pagina.assert_visible("role", "combobox", "Prioridade")
    pagina.assert_visible("role", "textbox", "Data limite")


@then(parsers.parse('a opção "{opcao}" está selecionada por predefinição no campo "{campo}"'))
def opcao_selecionada_por_predefinicao(page, app_url, opcao, campo):
    NovaTarefa(page, app_url).assert_priority_selected(opcao)


@when(parsers.parse('a área "{area}" é apresentada'))
def area_apresentada(page, app_url, area):
    ListaDeTarefas(page, app_url).assert_visible("role", "heading", area)


@then(parsers.parse('é indicada a existência de "{quantidade}" tarefas por fazer'))
def quantidade_tarefas_por_fazer(page, app_url, quantidade):
    ListaDeTarefas(page, app_url).assert_text("text", f"{quantidade} tarefas por fazer")


@when(parsers.re(r'^seleciono "(?P<nome>[^"]+)"$'))
def seleciono_nome(page, app_url, nome):
    IniciarSessao(page, app_url).click("role", "link", nome)


@then(parsers.parse('a página "{pagina}" é apresentada sem iniciar sessão'))
def pagina_apresentada_sem_iniciar_sessao(page, app_url, pagina):
    PAGINAS[pagina](page, app_url).assert_page()


@then(parsers.parse('a tarefa "{tarefa}" continua assinalada'))
def tarefa_continua_assinalada(page, app_url, tarefa):
    ListaDeTarefas(page, app_url).assert_visible("role", "checkbox", tarefa)


@then(parsers.parse('estão disponíveis os campos "Email" e "Password" e o botão "Entrar" na página "{pagina}"'))
def campos_inicio_sessao_disponiveis(page, app_url, pagina):
    tela = PAGINAS[pagina](page, app_url)
    tela.assert_visible("role", "textbox", "Email")
    tela.assert_visible("role", "textbox", "Password")
    tela.assert_visible("role", "button", "Entrar")


@when(parsers.parse('preencho o campo "{campo}" com "{valor}" na página "{pagina}"'))
def preencho_campo_com_valor(page, app_url, campo, valor, pagina):
    PAGINAS[pagina](page, app_url).fill("role", "textbox", campo, valor)


@when(parsers.parse('preencho o campo "{campo}" com a palavra-passe da utilizadora Ana Silva na página "{pagina}"'))
def preencho_palavra_passe(page, app_url, campo, pagina):
    PAGINAS[pagina](page, app_url).fill("role", "textbox", campo, os.environ["LOGIN_PASSWORD"])


@when(parsers.parse('seleciono o botão "{botao}" na página "{pagina}"'))
def seleciono_botao(page, app_url, botao, pagina):
    PAGINAS[pagina](page, app_url).click("role", "button", botao)


@when(parsers.parse('desassinalo a caixa de verificação da tarefa "{tarefa}"'))
def desassinalo_tarefa(page, app_url, tarefa):
    ListaDeTarefas(page, app_url).uncheck(tarefa)


@then(parsers.parse('seleciono a opção "{opcao}" no campo "{campo}"'))
def seleciono_opcao_no_campo(page, app_url, opcao, campo):
    NovaTarefa(page, app_url).select_priority(opcao)


@then(parsers.parse('a opção "{opcao}" fica selecionada no campo "{campo}"'))
def opcao_fica_selecionada(page, app_url, opcao, campo):
    NovaTarefa(page, app_url).assert_priority_selected(opcao)
