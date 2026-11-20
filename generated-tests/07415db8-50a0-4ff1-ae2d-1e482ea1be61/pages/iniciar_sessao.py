from urllib.parse import urljoin

from playwright.sync_api import Page, expect


class IniciarSessao:
    page_path = "/xtwins-site-simples/login.html"

    def __init__(self, page: Page, app_url: str | None = None):
        self.page = page
        self.app_url = app_url

    def open(self):
        self.page.goto(urljoin(self.app_url, self.page_path))
        self.assert_open()

    def assert_open(self):
        expect(self.page).to_have_url(urljoin(self.app_url, self.page_path))

    def continuar_sem_sessao(self):
        self.page.get_by_role("link", name="Continuar sem sessão", exact=True).click()
