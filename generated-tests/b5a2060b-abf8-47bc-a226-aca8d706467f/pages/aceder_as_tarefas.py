from datetime import datetime
from urllib.parse import urljoin

from playwright.sync_api import Page


class IniciarSessaoPage:
    def __init__(self, page: Page, app_url: str):
        self.page = page
        self.app_url = app_url

    def abrir(self, page_path: str) -> None:
        self.page.goto(urljoin(self.app_url, page_path))

    def preencher_email(self, valor: str) -> None:
        self.page.get_by_role("textbox", name="Email", exact=True).fill(valor)

    def preencher_password(self, valor: str) -> None:
        self.page.get_by_role("textbox", name="Password", exact=True).fill(valor)

    def selecionar_entrar(self) -> None:
        self.page.get_by_role("button", name="Entrar", exact=True).click()

    def continuar_sem_sessao(self) -> None:
        self.page.get_by_role("link", name="Continuar sem sessão", exact=True).click()

    def verificar_pagina(self, page_path: str) -> None:
        from playwright.sync_api import expect
        expect(self.page).to_have_url(urljoin(self.app_url, page_path))


class ListaDeTarefasPage:
    def __init__(self, page: Page, app_url: str):
        self.page = page
        self.app_url = app_url

    def abrir(self, page_path: str) -> None:
        self.page.goto(urljoin(self.app_url, page_path))

    def verificar_pagina(self, page_path: str) -> None:
        from playwright.sync_api import expect
        expect(self.page).to_have_url(urljoin(self.app_url, page_path))

    def verificar_area_minhas_tarefas(self) -> None:
        from playwright.sync_api import expect
        expect(self.page.get_by_role("heading", name="As minhas tarefas", exact=True)).to_be_visible()
        expect(self.page.get_by_role("table")).to_be_visible()

    def verificar_colunas(self) -> None:
        from playwright.sync_api import expect
        expect(self.page.get_by_role("columnheader", name="Tarefa", exact=True)).to_be_visible()
        expect(self.page.get_by_role("columnheader", name="Prioridade", exact=True)).to_be_visible()
        expect(self.page.get_by_role("columnheader", name="Data limite", exact=True)).to_be_visible()
        expect(self.page.get_by_role("columnheader", name="Ações", exact=True)).to_be_visible()

    def verificar_tarefas_por_fazer(self, total: int) -> None:
        from playwright.sync_api import expect
        expect(self.page.get_by_text(f"{total} tarefas por fazer", exact=True)).to_have_text(
            f"{total} tarefas por fazer"
        )
