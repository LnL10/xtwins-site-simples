from pytest_bdd import parsers, then

from pages.tarefas import ListaDeTarefas


@then(
    parsers.parse(
        'vejo na tabela da página "Lista de tarefas" a tarefa "{tarefa}" '
        'com prioridade "{prioridade}" e data limite "{data_limite}"'
    )
)
def vejo_tarefa_com_data_limite(page, app_url, tarefa, prioridade, data_limite):
    ListaDeTarefas(page, app_url).verificar_tarefa_com_data_limite(
        tarefa, prioridade, data_limite
    )
