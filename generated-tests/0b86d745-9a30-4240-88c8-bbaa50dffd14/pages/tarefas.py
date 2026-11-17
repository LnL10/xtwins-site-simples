from urllib.parse import urljoin

from playwright.sync_api import expect


class ListaDeTarefas:
    page_path = "/xtwins-site-simples/tarefas.html"

    def __init__(self, page, app_url):
        self.page = page
        self.app_url = app_url

    def abrir(self):
        self.page.goto(urljoin(self.app_url, self.page_path))

    def verificar_pagina_aberta(self):
        expect(self.page).to_have_url(urljoin(self.app_url, self.page_path))

    def verificar_colunas(self):
        for nome in ("Tarefa", "Prioridade", "Data limite", "Ações"):
            expect(self.page.get_by_role("columnheader", name=nome, exact=True)).to_be_visible()

    def verificar_estados_iniciais(self):
        expect(self.page.get_by_role("checkbox", name="Rever requisitos", exact=True)).not_to_be_checked()
        expect(self.page.get_by_role("checkbox", name="Preparar demonstração", exact=True)).not_to_be_checked()
        expect(self.page.get_by_role("checkbox", name="Enviar relatório semanal", exact=True)).to_be_checked()

    def verificar_total_e_estados(self, total):
        expect(self.page.locator("tbody tr")).to_have_count(total)
        self.verificar_estados_iniciais()

    def selecionar_ligacao(self, nome):
        self.page.get_by_role("link", name=nome, exact=True).click()
