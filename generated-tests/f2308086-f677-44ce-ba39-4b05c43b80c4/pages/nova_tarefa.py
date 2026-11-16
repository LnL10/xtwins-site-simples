from urllib.parse import urljoin


class NovaTarefaPage:
    page_path = "/xtwins-site-simples/nova-tarefa.html"

    def __init__(self, page, app_url):
        self.page = page
        self.app_url = app_url

    def assert_pagina(self):
        assert self.page.url == urljoin(self.app_url, self.page_path)
        assert self.page.get_by_role("heading", name="Nova tarefa").is_visible()

    def preencher_titulo_e_prioridade(self, titulo, prioridade):
        self.page.get_by_role("textbox", name="Título").fill(titulo)
        self.page.get_by_role("combobox", name="Prioridade").select_option(label=prioridade)

    def guardar(self):
        self.page.get_by_role("button", name="Guardar").click()

    def assert_opcoes_de_prioridade(self):
        prioridade = self.page.get_by_role("combobox", name="Prioridade")
        opcoes = prioridade.evaluate(
            "element => Array.from(element.options, option => option.textContent.trim())"
        )
        selecionada = prioridade.evaluate(
            "element => element.selectedOptions[0].textContent.trim()"
        )
        assert opcoes == ["Baixa", "Média", "Alta"]
        assert selecionada == "Média"

    def escolher_prioridade(self, valor):
        self.page.get_by_role("combobox", name="Prioridade").select_option(label=valor)

    def assert_prioridade_selecionada(self, valor):
        assert self.page.get_by_role("option", name=valor).is_selected()
