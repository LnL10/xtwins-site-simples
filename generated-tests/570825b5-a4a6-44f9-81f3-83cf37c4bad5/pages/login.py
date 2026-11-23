from urllib.parse import urljoin

from playwright.sync_api import expect


class LoginPage:
    def __init__(self, page, app_url):
        self.page = page
        self.app_url = app_url

    def open(self, page_path):
        self.page.goto(urljoin(self.app_url, page_path))

    def assert_current_page(self, page_path):
        expect(self.page).to_have_url(urljoin(self.app_url, page_path))

    def field(self, campo):
        return self.page.get_by_role("textbox", name=campo, exact=True)

    def assert_field_visible(self, campo):
        expect(self.field(campo)).to_be_visible()

    def fill_field(self, campo, value):
        self.field(campo).fill(value)

    def button(self, botao):
        return self.page.get_by_role("button", name=botao, exact=True)

    def click_button(self, botao):
        self.button(botao).click()

    def assert_button_visible(self, botao):
        expect(self.button(botao)).to_be_visible()

    def continuar_sem_sessao(self):
        return self.page.get_by_role("link", name="Continuar sem sessão", exact=True)

    def click_continuar_sem_sessao(self):
        self.continuar_sem_sessao().click()

    def link(self, ligacao):
        return self.page.get_by_role("link", name=ligacao, exact=True)

    def assert_link_visible(self, ligacao):
        expect(self.link(ligacao)).to_be_visible()
