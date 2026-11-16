from urllib.parse import urljoin


class TarefasPage:
    page_path = "/xtwins-site-simples/tarefas.html"

    def __init__(self, page, app_url):
        self.page = page
        self.app_url = app_url

    def navigate(self):
        self.page.goto(urljoin(self.app_url, self.page_path))

    def assert_tarefas_iniciais(self, quantidade, tarefas):
        assert int(quantidade) == len(tarefas)
        for tarefa in tarefas:
            assert self.page.get_by_role("cell", name=tarefa).is_visible()

    def assert_tarefa_por_fazer(self, tarefa):
        checkbox = self.page.get_by_role("checkbox", name=tarefa)
        assert checkbox.is_visible()
        assert not checkbox.is_checked()

    def assert_mensagem_de_confirmacao(self):
        mensagem = self.page.get_by_role("status")
        assert mensagem.is_visible()
        assert mensagem.inner_text().strip()
