from pytest_bdd import parsers, then, when

from pages.tarefas import ListaDeTarefasPage, NovaTarefaPage


@when(parsers.parse('o utilizador seleciona o botão "Cancelar"'))
def selecionar_botao_cancelar(page, app_url):
    NovaTarefaPage(page, app_url).cancelar()


@then(parsers.parse('a caixa de verificação da tarefa "{titulo}" não está selecionada'))
def verificar_tarefa_nao_selecionada(page, app_url, titulo):
    ListaDeTarefasPage(page, app_url).verificar_tarefa_desmarcada(titulo)


@when(parsers.parse('o utilizador seleciona a caixa de verificação da tarefa "{titulo}"'))
def selecionar_caixa_de_verificacao(page, app_url, titulo):
    ListaDeTarefasPage(page, app_url).marcar_tarefa(titulo)


@then(parsers.parse('a caixa de verificação da tarefa "{titulo}" está selecionada'))
def verificar_tarefa_selecionada(page, app_url, titulo):
    ListaDeTarefasPage(page, app_url).verificar_tarefa_marcada(titulo)


@when(parsers.parse('o utilizador desmarca a caixa de verificação da tarefa "{titulo}"'))
def desmarcar_caixa_de_verificacao(page, app_url, titulo):
    ListaDeTarefasPage(page, app_url).desmarcar_tarefa(titulo)
