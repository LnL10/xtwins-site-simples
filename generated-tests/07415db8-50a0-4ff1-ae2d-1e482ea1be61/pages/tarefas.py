from urllib.parse import urljoin

from playwright.sync_api import Page, expect


class Tarefas:
    page_path = "/xtwins-site-simples/tarefas.html"

    def __init__(self, page: Page, app_url: str | None = None):
        self.page = page
        self.app_url = app_url

    def open(self):
        self.page.goto(urljoin(self.app_url, self.page_path))
        self.assert_open()

    def assert_open(self):
        expect(self.page).to_have_url(urljoin(self.app_url, self.page_path))

    @staticmethod
    def _numero(total):
        try:
            return int(total)
        except ValueError:
            numeros = {"três": 3}
            if total not in numeros:
                raise ValueError(f"Número de tarefas não reconhecido: {total}")
            return numeros[total]

    def assert_listing(self, total):
        expect(self.page.locator("tbody tr")).to_have_count(self._numero(total))
        expect(self.page.get_by_role("columnheader", name="Prioridade", exact=True)).to_be_visible()
        expect(self.page.get_by_role("columnheader", name="Data limite", exact=True)).to_be_visible()
        expect(self.page.get_by_role("checkbox", name="Rever requisitos", exact=True)).to_be_visible()
        expect(self.page.get_by_role("checkbox", name="Preparar demonstração", exact=True)).to_be_visible()
        expect(self.page.get_by_role("checkbox", name="Enviar relatório semanal", exact=True)).to_be_visible()

    def assert_summary(self, texto):
        expect(self.page.get_by_text(texto, exact=True)).to_have_text(texto)

    def assert_task_without_due_date(self, titulo):
        expect(self.page.get_by_role("checkbox", name=titulo, exact=True)).to_be_visible()
        expect(
            self.page.get_by_role("row")
            .filter(has_text=titulo)
            .get_by_role("cell", name="—", exact=True)
        ).to_be_visible()

    def assert_task_visible(self, titulo):
        expect(self.page.get_by_role("checkbox", name=titulo, exact=True)).to_be_visible()
