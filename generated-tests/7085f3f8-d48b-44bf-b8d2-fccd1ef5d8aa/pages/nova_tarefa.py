from datetime import datetime
from urllib.parse import urljoin

from playwright.sync_api import Page, expect


class NovaTarefaPage:
    page_path = "/xtwins-site-simples/nova-tarefa.html"

    def __init__(self, page: Page, app_url: str) -> None:
        self.page = page
        self.app_url = app_url

    def assert_pagina(self) -> None:
        assert self.page.url == urljoin(self.app_url, self.page_path)

    def campo_titulo(self):
        return self.page.get_by_role("textbox", name="Título", exact=True)

    def preencher_titulo(self, valor: str) -> None:
        self.campo_titulo().fill(valor)

    def assert_campo_titulo_visivel(self) -> None:
        expect(self.campo_titulo()).to_be_visible()

    def campo_data_limite(self):
        return self.page.get_by_role("textbox", name="Data limite", exact=True)

    def preencher_data_limite(self, valor: str) -> None:
        if not valor:
            self.campo_data_limite().fill("")
            return
        data_iso = datetime.strptime(valor.replace("-", "/"), "%d/%m/%Y").date().isoformat()
        self.campo_data_limite().fill(data_iso)

    def guardar(self) -> None:
        self.page.get_by_role("button", name="Guardar", exact=True).click()

    def cancelar(self) -> None:
        self.page.get_by_role("link", name="Cancelar", exact=True).click()

    def selecao_prioridade(self):
        return self.page.get_by_role("combobox", name="Prioridade", exact=True)

    def selecionar_prioridade(self, valor: str) -> None:
        self.selecao_prioridade().select_option(valor)

    def assert_prioridade(self, valor: str) -> None:
        expect(self.selecao_prioridade()).to_have_value(valor)
