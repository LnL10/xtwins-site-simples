from datetime import datetime
from urllib.parse import urljoin

from playwright.sync_api import Page, expect


class NovaTarefa:
    page_path = "/xtwins-site-simples/nova-tarefa.html"

    def __init__(self, page: Page, app_url: str | None = None):
        self.page = page
        self.app_url = app_url

    def open(self):
        self.page.goto(urljoin(self.app_url, self.page_path))
        self.assert_open()

    def assert_open(self):
        expect(self.page).to_have_url(urljoin(self.app_url, self.page_path))

    def _titulo(self):
        return self.page.get_by_role("textbox", name="Título", exact=True)

    def _data_limite(self):
        return self.page.get_by_role("textbox", name="Data limite", exact=True)

    def _prioridade(self):
        return self.page.get_by_role("combobox", name="Prioridade", exact=True)

    def assert_priority_options(self, selecionada):
        expect(self.page.get_by_role("option", name="Baixa", exact=True)).to_be_attached()
        expect(self.page.get_by_role("option", name="Média", exact=True)).to_be_attached()
        expect(self.page.get_by_role("option", name="Alta", exact=True)).to_be_attached()
        expect(self._prioridade()).to_have_value(selecionada)

    def select_priority(self, prioridade):
        self._prioridade().select_option(prioridade)

    def assert_priority_value(self, prioridade):
        expect(self._prioridade()).to_have_value(prioridade)

    def _guardar(self):
        self.page.get_by_role("button", name="Guardar", exact=True).click()

    @staticmethod
    def _iso_date(data):
        if "/" in data or ("-" in data and len(data.split("-", 1)[0]) != 4):
            return datetime.strptime(data.replace("-", "/"), "%d/%m/%Y").date().isoformat()
        return data

    def save_title(self, titulo):
        self._titulo().fill(titulo)
        self._guardar()

    def save_title_and_due_date(self, titulo, data):
        self._titulo().fill(titulo)
        self._data_limite().fill(self._iso_date(data))
        self._guardar()
