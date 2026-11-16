from urllib.parse import urljoin

from playwright.sync_api import Page, expect


class TarefasPage:
    page_path = "/xtwins-site-simples/tarefas.html"

    def __init__(self, page: Page, app_url: str) -> None:
        self.page = page
        self.app_url = app_url

    def abrir(self) -> None:
        self.page.goto(urljoin(self.app_url, self.page_path))

    def assert_pagina(self) -> None:
        assert self.page.url == urljoin(self.app_url, self.page_path)

    def titulo(self):
        return self.page.get_by_role("heading", name="As minhas tarefas", exact=True)

    def assert_titulo_visivel(self) -> None:
        expect(self.titulo()).to_be_visible()

    def linhas(self):
        return self.page.locator("tbody tr")

    def assert_quantidade_tarefas(self, quantidade: str) -> None:
        numeros = {"três": 3}
        expect(self.linhas()).to_have_count(numeros[quantidade])

    def tabela(self):
        return self.page.get_by_role("table")

    def assert_tabela_visivel(self) -> None:
        expect(self.tabela()).to_be_visible()

    def assert_dados_tarefa_visiveis(self) -> None:
        locators = (
            self.page.get_by_role("cell", name="Rever requisitos", exact=True),
            self.page.get_by_role("checkbox", name="Rever requisitos", exact=True),
            self.page.get_by_role("cell", name="Alta", exact=True),
            self.page.get_by_role("row").filter(has_text="Rever requisitos").get_by_role("cell", name="—", exact=True),
            self.page.get_by_role("cell", name="Preparar demonstração", exact=True),
            self.page.get_by_role("checkbox", name="Preparar demonstração", exact=True),
            self.page.get_by_role("cell", name="Média", exact=True),
            self.page.get_by_role("cell", name="31/12/2027", exact=True),
            self.page.get_by_role("cell", name="Enviar relatório semanal", exact=True),
            self.page.get_by_role("checkbox", name="Enviar relatório semanal", exact=True),
            self.page.get_by_role("cell", name="Baixa", exact=True),
            self.page.get_by_role("row").filter(has_text="Enviar relatório semanal").get_by_role("cell", name="—", exact=True),
        )
        for locator in locators:
            expect(locator).to_be_visible()

    def assert_formato_datas(self, formato: str, alternativa: str) -> None:
        import re

        padrao_data = r"\d{2}/\d{2}/\d{4}" if formato == "dd/mm/aaaa" else re.escape(formato)
        padrao_alternativa = "—" if alternativa == "-" else re.escape(alternativa)
        esperado = re.compile(rf"^(?:{padrao_data}|{re.escape(alternativa)}|{padrao_alternativa})$")
        locators = (
            self.page.get_by_role("row").filter(has_text="Rever requisitos").get_by_role("cell", name="—", exact=True),
            self.page.get_by_role("cell", name="31/12/2027", exact=True),
            self.page.get_by_role("row").filter(has_text="Enviar relatório semanal").get_by_role("cell", name="—", exact=True),
        )
        for locator in locators:
            expect(locator).to_have_text(esperado)

    def contador(self):
        return self.page.get_by_role("paragraph")

    def assert_contador(self, texto: str) -> None:
        expect(self.contador()).to_have_text(texto)

    def checkbox_tarefa(self, titulo: str):
        return self.page.get_by_role("checkbox", name=titulo, exact=True)

    def desmarcar_tarefa(self, titulo: str) -> None:
        self.checkbox_tarefa(titulo).uncheck()

    def marcar_tarefa(self, titulo: str) -> None:
        self.checkbox_tarefa(titulo).check()

    def assert_tarefa_desmarcada(self, titulo: str) -> None:
        expect(self.checkbox_tarefa(titulo)).not_to_be_checked()

    def assert_titulo_tarefa_visivel(self, titulo: str) -> None:
        expect(self.page.get_by_role("cell", name=titulo, exact=True)).to_be_visible()

    def selecionar_nova_tarefa(self) -> None:
        self.page.get_by_role("link", name="Nova tarefa", exact=True).click()
