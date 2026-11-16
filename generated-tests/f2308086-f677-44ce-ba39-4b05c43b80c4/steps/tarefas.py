from pytest_bdd import given, parsers, then, when

from pages.nova_tarefa import NovaTarefaPage
from pages.tarefas import TarefasPage


TAREFAS_INICIAIS = [
    "Rever requisitos",
    "Preparar demonstração",
    "Enviar relatório semanal",
]


@given(parsers.parse("que utilizo um navegador novo sem dados guardados"))
def navegador_novo_sem_dados_guardados():
    pass


@given(parsers.parse("que sou visitante e não tenho sessão iniciada"))
def visitante_sem_sessao_iniciada():
    pass


@when(parsers.parse('acedo à página "{pagina}"'))
def acedo_a_pagina(page, app_url, pagina):
    assert pagina == "Lista de tarefas"
    TarefasPage(page, app_url).navigate()


@then(parsers.parse('vejo "{quantidade}" tarefas na tabela da página "{pagina}", na coluna "{coluna}"'))
def vejo_tarefas_iniciais(page, app_url, quantidade, pagina, coluna):
    assert pagina == "Lista de tarefas"
    assert coluna == "Tarefa"
    TarefasPage(page, app_url).assert_tarefas_iniciais(quantidade, TAREFAS_INICIAIS)


@when(parsers.parse('acedo à página "{pagina}" num segundo navegador novo sem dados guardados'))
def acedo_a_pagina_num_segundo_navegador(page, app_url, pagina):
    assert pagina == "Lista de tarefas"
    TarefasPage(page, app_url).navigate()


@then(parsers.parse('vejo as mesmas "{quantidade}" tarefas iniciais na coluna "{coluna}" da página "{pagina}" que vi no primeiro navegador'))
def vejo_as_mesmas_tarefas_iniciais(page, app_url, quantidade, coluna, pagina):
    assert pagina == "Lista de tarefas"
    assert coluna == "Tarefa"
    TarefasPage(page, app_url).assert_tarefas_iniciais(quantidade, TAREFAS_INICIAIS)


@when(parsers.parse('seleciono a ligação "{ligacao}"'))
def seleciono_a_ligacao(page, ligacao):
    assert ligacao == "Nova tarefa"
    page.get_by_role("link", name=ligacao).click()


@then(parsers.parse('é apresentada a página "{pagina}" com o formulário "{formulario}"'))
def e_apresentada_a_pagina_com_o_formulario(page, app_url, pagina, formulario):
    assert pagina == "Nova tarefa"
    assert formulario == "Nova tarefa"
    NovaTarefaPage(page, app_url).assert_pagina()


@when(parsers.parse('preencho o campo "{campo}" com "{titulo}" e seleciono "{prioridade}" na lista "{lista}"'))
def preencho_o_campo_e_seleciono_na_lista(page, app_url, campo, titulo, prioridade, lista):
    assert campo == "Título"
    assert lista == "Prioridade"
    NovaTarefaPage(page, app_url).preencher_titulo_e_prioridade(titulo, prioridade)


@when(parsers.parse('seleciono o botão "{botao}"'))
def seleciono_o_botao(page, botao):
    assert botao == "Guardar"
    page.get_by_role("button", name=botao).click()


@then(parsers.parse('na página "{pagina}", a tarefa "{tarefa}" aparece no fim da tabela com o estado "{estado}"'))
def tarefa_aparece_no_fim_da_tabela(page, app_url, pagina, tarefa, estado):
    assert pagina == "Lista de tarefas"
    assert estado == "por fazer"
    TarefasPage(page, app_url).assert_tarefa_por_fazer(tarefa)


@then(parsers.parse("é apresentada uma mensagem de confirmação"))
def e_apresentada_uma_mensagem_de_confirmacao(page, app_url):
    TarefasPage(page, app_url).assert_mensagem_de_confirmacao()


@then(parsers.parse('a lista "{lista}" apresenta as opções "{baixa}", "{media}" e "{alta}", com "{selecionada}" selecionada por omissão'))
def lista_apresenta_opcoes_com_uma_selecionada_por_omissao(page, app_url, lista, baixa, media, alta, selecionada):
    assert lista == "Prioridade"
    assert (baixa, media, alta, selecionada) == ("Baixa", "Média", "Alta", "Média")
    NovaTarefaPage(page, app_url).assert_opcoes_de_prioridade()


@when(parsers.parse('escolho "{valor}" na lista "{lista}"'))
def escolho_valor_na_lista(page, app_url, valor, lista):
    assert lista == "Prioridade"
    NovaTarefaPage(page, app_url).escolher_prioridade(valor)


@then(parsers.parse('a lista "{lista}" apresenta "{valor}" selecionada'))
def lista_apresenta_valor_selecionado(page, app_url, lista, valor):
    assert lista == "Prioridade"
    NovaTarefaPage(page, app_url).assert_prioridade_selecionada(valor)
