from urllib.parse import urljoin

from playwright.sync_api import expect


class NovaTarefa:
    page_path = "/xtwins-site-simples/nova-tarefa.html"

    def __init__(self, page, app_url):
        self.page = page
        self.app_url = app_url

    def verificar_pagina_aberta(self):
        expect(self.page).to_have_url(urljoin(self.app_url, self.page_path))

    def verificar_prioridade(self, valor):
        expect(self.page.get_by_role("combobox", name="Prioridade", exact=True)).to_have_value(valor)

    def selecionar_prioridade(self, valor):
        self.page.get_by_role("combobox", name="Prioridade", exact=True).select_option(label=valor)
