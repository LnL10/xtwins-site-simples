from urllib.parse import urljoin

from playwright.sync_api import Page, expect


class ListaDeTarefas:
    page_path = "/xtwins-site-simples/tarefas.html"

    def __init__(self, page: Page, app_url: str):
        self.page = page
        self.app_url = app_url

    def open(self) -> None:
        self.page.goto(urljoin(self.app_url, self.page_path))

    def selecionar_link_nova_tarefa(self) -> None:
        self.page.get_by_role("link", name="Nova tarefa").click()

    def assert_tarefa(self, titulo: str, prioridade: str, data_limite: str) -> None:
        expect(self.page.get_by_role("cell", name=titulo)).to_be_visible()
        expect(self.page.get_by_role("cell", name=prioridade)).to_be_visible()
        expect(self.page.get_by_role("cell", name=data_limite)).to_be_visible()

    def assert_caixa_desmarcada(self, titulo: str) -> None:
        expect(self.page.get_by_role("checkbox", name=titulo)).not_to_be_checked()

    def assert_caixa_marcada(self, titulo: str) -> None:
        expect(self.page.get_by_role("checkbox", name=titulo)).to_be_checked()

    def assert_titulo_riscado(self, titulo: str, riscado: bool) -> None:
        locator = self.page.get_by_text(titulo)
        expect(locator).to_be_visible()
        text_decoration = locator.evaluate(
            "element => getComputedStyle(element).textDecorationLine"
        )
        if riscado:
            assert "line-through" in text_decoration
        else:
            assert "line-through" not in text_decoration

    def assert_resumo(self, resumo: str) -> None:
        expect(self.page.get_by_role("paragraph", name=resumo)).to_be_visible()
