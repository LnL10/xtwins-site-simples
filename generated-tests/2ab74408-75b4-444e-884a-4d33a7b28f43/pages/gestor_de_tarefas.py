from urllib.parse import urljoin

from playwright.sync_api import expect


class ListaDeTarefas:
    page_path = "/xtwins-site-simples/tarefas.html"

    def __init__(self, page, app_url):
        self.page = page
        self.app_url = app_url

    def open(self):
        self.page.goto(urljoin(self.app_url, self.page_path))

    def assert_page(self):
        expect(self.page).to_have_url(urljoin(self.app_url, self.page_path))

    def locator(self, strategy, value, name=None):
        if strategy == "role":
            return self.page.get_by_role(value, name=name)
        if strategy == "text":
            return self.page.get_by_text(value)
        raise ValueError(f"Unsupported locator strategy: {strategy}")

    def assert_visible(self, strategy, value, name=None):
        expect(self.locator(strategy, value, name)).to_be_visible()

    def assert_hidden(self, strategy, value, name=None):
        expect(self.locator(strategy, value, name)).to_be_hidden()

    def assert_text(self, strategy, value, name=None):
        expect(self.locator(strategy, value, name)).to_be_visible()

    def click(self, strategy, value, name=None):
        self.locator(strategy, value, name).click()

    def check(self, task_name):
        self.page.get_by_role("checkbox", name=task_name).check()

    def uncheck(self, task_name):
        self.page.get_by_role("checkbox", name=task_name).uncheck()

    def assert_checked(self, task_name):
        expect(self.page.get_by_role("checkbox", name=task_name)).to_be_checked()

    def assert_task_visible(self, task_name):
        checkbox = self.page.get_by_role("checkbox", name=task_name)
        if checkbox.count():
            expect(checkbox).to_be_visible()
        else:
            expect(self.page.get_by_role("cell", name=task_name)).to_be_visible()

    def fill(self, strategy, value, name, text):
        self.locator(strategy, value, name).fill(text)


class IniciarSessao:
    page_path = "/xtwins-site-simples/login.html"

    def __init__(self, page, app_url):
        self.page = page
        self.app_url = app_url

    def open(self):
        self.page.goto(urljoin(self.app_url, self.page_path))

    def assert_page(self):
        expect(self.page).to_have_url(urljoin(self.app_url, self.page_path))

    def locator(self, strategy, value, name=None):
        if strategy == "role":
            return self.page.get_by_role(value, name=name)
        if strategy == "text":
            return self.page.get_by_text(value)
        raise ValueError(f"Unsupported locator strategy: {strategy}")

    def assert_visible(self, strategy, value, name=None):
        expect(self.locator(strategy, value, name)).to_be_visible()

    def click(self, strategy, value, name=None):
        self.locator(strategy, value, name).click()

    def fill(self, strategy, value, name, text):
        self.locator(strategy, value, name).fill(text)


class NovaTarefa:
    page_path = "/xtwins-site-simples/nova-tarefa.html"

    def __init__(self, page, app_url):
        self.page = page
        self.app_url = app_url

    def open(self):
        self.page.goto(urljoin(self.app_url, self.page_path))

    def assert_page(self):
        expect(self.page).to_have_url(urljoin(self.app_url, self.page_path))

    def locator(self, strategy, value, name=None):
        if strategy == "role":
            return self.page.get_by_role(value, name=name)
        if strategy == "text":
            return self.page.get_by_text(value)
        raise ValueError(f"Unsupported locator strategy: {strategy}")

    def assert_visible(self, strategy, value, name=None):
        expect(self.locator(strategy, value, name)).to_be_visible()

    def click(self, strategy, value, name=None):
        self.locator(strategy, value, name).click()

    def select_priority(self, option_name):
        self.page.get_by_role("combobox", name="Prioridade").select_option(label=option_name)

    def assert_priority_selected(self, option_name):
        option = self.page.get_by_role("option", name=option_name)
        expect(option).to_be_visible()
        assert option.evaluate("element => element.selected")
