from urllib.parse import urljoin

from playwright.sync_api import expect


class TarefasPage:
    def __init__(self, page, app_url):
        self.page = page
        self.app_url = app_url

    def open(self, page_path):
        self.page.goto(urljoin(self.app_url, page_path))

    def assert_current_page(self, page_path):
        expect(self.page).to_have_url(urljoin(self.app_url, page_path))

    def area_as_minhas_tarefas(self):
        return self.page.get_by_role("heading", name="As minhas tarefas", exact=True)

    def assert_area_as_minhas_tarefas_visible(self):
        expect(self.area_as_minhas_tarefas()).to_be_visible()

    def table(self):
        return self.page.get_by_role("table")

    def assert_table_visible(self):
        expect(self.table()).to_be_visible()

    def column(self, name):
        return self.page.get_by_role("columnheader", name=name, exact=True)

    def assert_columns_visible(self):
        expect(self.column("Tarefa")).to_be_visible()
        expect(self.column("Prioridade")).to_be_visible()
        expect(self.column("Data limite")).to_be_visible()
        expect(self.column("Ações")).to_be_visible()

    def tasks_remaining(self, total):
        return self.page.get_by_text(f"{total} tarefas por fazer", exact=True)

    def assert_tasks_remaining_text(self, total):
        expect(self.tasks_remaining(total)).to_have_text(f"{total} tarefas por fazer")

    def iniciar_sessao(self):
        return self.page.get_by_role("link", name="Iniciar sessão", exact=True)

    def click_iniciar_sessao(self):
        self.iniciar_sessao().click()
