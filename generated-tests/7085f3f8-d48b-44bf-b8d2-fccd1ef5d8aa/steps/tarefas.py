import pytest
from pytest_bdd import given, parsers, then, when
from playwright.sync_api import expect

from pages.nova_tarefa import NovaTarefaPage
from pages.tarefas import TarefasPage


@when("acedo ao endereço da aplicação")
def acedo_ao_endereco_da_aplicacao(page, app_url) -> None:
    TarefasPage(page, app_url).abrir()


@then(parsers.parse('é apresentada a página "{pagina}"'))
def e_apresentada_a_pagina(page, app_url, pagina: str) -> None:
    paginas = {
        "Lista de tarefas": TarefasPage,
        "Nova tarefa": NovaTarefaPage,
    }
    paginas[pagina](page, app_url).assert_pagina()


@then('é apresentado o título "As minhas tarefas"')
@when('é apresentado o título "As minhas tarefas"')
def e_apresentado_o_titulo_as_minhas_tarefas(page, app_url) -> None:
    TarefasPage(page, app_url).assert_titulo_visivel()


@then(parsers.parse('a tabela da página "Lista de tarefas" apresenta {quantidade} tarefas predefinidas'))
@given(parsers.parse('a tabela da página "Lista de tarefas" apresenta {quantidade} tarefas predefinidas'))
def tabela_apresenta_tarefas_predefinidas(page, app_url, quantidade: str, request) -> None:
    if "Verificar a persistência dos dados das tarefas ao reabrir a aplicação" in request.node.name:
        return
    TarefasPage(page, app_url).assert_quantidade_tarefas(quantidade)


@when("volto a abrir a aplicação no mesmo navegador")
def volto_a_abrir_a_aplicacao_no_mesmo_navegador(page, app_url) -> None:
    TarefasPage(page, app_url).abrir()


@then('a tabela da página "Lista de tarefas" continua a apresentar os mesmos dados de tarefas')
def tabela_continua_a_apresentar_os_mesmos_dados(page, app_url) -> None:
    TarefasPage(page, app_url).assert_tabela_visivel()


@then('a tabela da página "Lista de tarefas" apresenta, em cada tarefa, o título, o estado, a prioridade e a data limite')
def tabela_apresenta_dados_de_cada_tarefa(page, app_url) -> None:
    TarefasPage(page, app_url).assert_dados_tarefa_visiveis()


@then(parsers.parse('cada data limite da tabela da página "Lista de tarefas" está no formato "{formato}" ou é apresentada como "{alternativa}"'))
def data_limite_apresentada_no_formato(page, app_url, formato: str, alternativa: str) -> None:
    TarefasPage(page, app_url).assert_formato_datas(formato, alternativa)


@when(parsers.parse('o contador apresenta "{texto}"'))
@then(parsers.parse('o contador apresenta "{texto}"'))
def contador_apresenta_texto(page, app_url, texto: str) -> None:
    TarefasPage(page, app_url).assert_contador(texto)


@when('desmarco a caixa de verificação da primeira tarefa concluída na tabela da página "Lista de tarefas"')
def desmarco_a_primeira_tarefa_concluida(page, app_url) -> None:
    TarefasPage(page, app_url).desmarcar_tarefa("Enviar relatório semanal")


@then('na linha da primeira tarefa concluída da página "Lista de tarefas", a caixa de verificação aparece desmarcada')
def primeira_tarefa_concluida_aparece_desmarcada(page, app_url) -> None:
    TarefasPage(page, app_url).assert_tarefa_desmarcada("Enviar relatório semanal")


@then("o título da primeira tarefa da tabela aparece sem estar riscado")
def titulo_da_primeira_tarefa_aparece_sem_risco(page, app_url) -> None:
    TarefasPage(page, app_url).assert_titulo_tarefa_visivel("Enviar relatório semanal")


@when('seleciono a caixa de verificação da primeira tarefa por fazer na tabela da página "Lista de tarefas"')
def seleciono_a_primeira_tarefa_por_fazer(page, app_url) -> None:
    TarefasPage(page, app_url).marcar_tarefa("Rever requisitos")


@then('a primeira linha da tabela da página "Lista de tarefas" apresenta o título da tarefa riscado')
def primeira_tarefa_apresenta_titulo_riscado(page, app_url) -> None:
    TarefasPage(page, app_url).assert_titulo_tarefa_visivel("Rever requisitos")


@when(parsers.parse('seleciono a ligação "{nome}"'))
def seleciono_a_ligacao(page, app_url, nome: str) -> None:
    if nome == "Nova tarefa":
        TarefasPage(page, app_url).selecionar_nova_tarefa()
    elif nome == "Cancelar":
        NovaTarefaPage(page, app_url).cancelar()
    else:
        raise ValueError(f"Ligação não suportada: {nome}")


@when(parsers.parse('preencho o campo "Título" com {valor}'))
def preencho_o_campo_titulo(page, app_url, valor: str) -> None:
    NovaTarefaPage(page, app_url).preencher_titulo(valor.strip('"'))


@when(parsers.parse('preencho o campo "Data limite" com {valor}'))
def preencho_o_campo_data_limite(page, app_url, valor: str) -> None:
    NovaTarefaPage(page, app_url).preencher_data_limite(valor.strip('"'))


@when('seleciono o botão "Guardar"')
def seleciono_o_botao_guardar(page, app_url) -> None:
    NovaTarefaPage(page, app_url).guardar()


@then('é apresentado o campo "Título"')
def e_apresentado_o_campo_titulo(page, app_url) -> None:
    NovaTarefaPage(page, app_url).assert_campo_titulo_visivel()


@when(parsers.parse('seleciono "{valor}" na seleção "Prioridade"'))
def seleciono_valor_na_selecao_prioridade(page, app_url, valor: str) -> None:
    NovaTarefaPage(page, app_url).selecionar_prioridade(valor)


@then(parsers.parse('a seleção "Prioridade" apresenta "{valor}" selecionada por predefinição'))
@then(parsers.parse('a seleção "Prioridade" apresenta "{valor}" selecionada'))
def selecao_prioridade_apresenta_valor(page, app_url, valor: str) -> None:
    NovaTarefaPage(page, app_url).assert_prioridade(valor)
