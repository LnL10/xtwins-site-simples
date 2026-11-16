from urllib.parse import urljoin

from playwright.sync_api import Page, expect


class NovaTarefa:
    page_path = "/xtwins-site-simples/nova-tarefa.html"

    def __init__(self, page: Page, app_url: str):
        self.page = page
        self.app_url = app_url

    def assert_pagina(self) -> None:
        assert self.page.url == urljoin(self.app_url, self.page_path)

    def selecionar_prioridade(self, prioridade: str) -> None:
        self.page.get_by_role("combobox", name="Prioridade").select_option(
            label=prioridade
        )

    def assert_prioridade_selecionada(self, prioridade: str) -> None:
        expect(self.page.get_by_role("option", name=prioridade)).to_be_selected()
