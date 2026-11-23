from datetime import datetime
from urllib.parse import urljoin
from playwright.sync_api import expect

class ListaDeTarefasPage:

    def __init__(self, page, app_url):
        self.page = page
        self.app_url = app_url

    def abrir(self, page_path):
        self.page.goto(urljoin(self.app_url, page_path))

    def verificar_url(self, page_path):
        expect(self.page).to_have_url(urljoin(self.app_url, page_path))

    def verificar_area_minhas_tarefas(self):
        expect(self.page.get_by_role('heading', name='As minhas tarefas', exact=True)).to_be_visible()
        expect(self.page.get_by_role('table')).to_be_visible()

    def verificar_colunas(self):
        expect(self.page.get_by_role('columnheader', name='Tarefa', exact=True)).to_be_visible()
        expect(self.page.get_by_role('columnheader', name='Prioridade', exact=True)).to_be_visible()
        expect(self.page.get_by_role('columnheader', name='Data limite', exact=True)).to_be_visible()
        expect(self.page.get_by_role('columnheader', name='Ações', exact=True)).to_be_visible()

    def verificar_indicacao_tarefas(self, total):
        expect(self.page.get_by_role('paragraph')).to_contain_text(f'{total} tarefas por fazer')

    def abrir_nova_tarefa(self):
        self.page.get_by_role('link', name='Nova tarefa', exact=True).click()

    def verificar_tarefa_visivel(self, titulo):
        expect(self.page.get_by_role('cell', name=titulo, exact=True)).to_be_visible()

    def verificar_prioridade_na_tarefa(self, titulo, prioridade):
        locator = self.page.get_by_role('row').filter(has_text=titulo).get_by_role('cell', name=prioridade, exact=True)
        expect(locator).to_contain_text(prioridade)

    def verificar_data_na_tarefa(self, titulo, data):
        data_apresentada = self._data_apresentada(data)
        locator = self.page.get_by_role('row').filter(has_text=titulo).get_by_role('cell', name=data_apresentada, exact=True)
        expect(locator).to_contain_text(data_apresentada)

    def verificar_titulo(self, titulo):
        expect(self.page.get_by_role('cell', name=titulo, exact=True)).to_contain_text(titulo)

    def verificar_prioridade(self, prioridade):
        expect(self.page.get_by_role('cell', name=prioridade, exact=True)).to_contain_text(prioridade)

    def verificar_data_sem_limite(self, titulo):
        locator = self.page.get_by_role('row').filter(has_text=titulo).get_by_role('cell', name='—', exact=True)
        expect(locator).to_contain_text('—')

    @staticmethod
    def _data_apresentada(valor):
        valor = valor.replace('-', '/')
        return datetime.strptime(valor, '%Y/%m/%d').strftime('%d/%m/%Y')

    def cancelar(self):
        self.page.get_by_role('link', name='Cancelar', exact=True).click()

    def marcar_tarefa(self, titulo):
        self.page.get_by_role('checkbox', name=titulo, exact=True).check()

    def desmarcar_tarefa(self, titulo):
        self.page.get_by_role('checkbox', name=titulo, exact=True).uncheck()

    def verificar_tarefa_marcada(self, titulo):
        expect(self.page.get_by_role('checkbox', name=titulo, exact=True)).to_be_checked()

    def verificar_tarefa_desmarcada(self, titulo):
        expect(self.page.get_by_role('checkbox', name=titulo, exact=True)).not_to_be_checked()

class NovaTarefaPage:

    def __init__(self, page, app_url):
        self.page = page
        self.app_url = app_url

    def verificar_url(self, page_path):
        expect(self.page).to_have_url(urljoin(self.app_url, page_path))

    def preencher_titulo(self, titulo):
        self.page.get_by_role('textbox', name='Título', exact=True).fill(titulo)

    def selecionar_prioridade(self, prioridade):
        self.page.get_by_role('combobox', name='Prioridade', exact=True).select_option(label=prioridade)

    def preencher_data_limite(self, data):
        valor = data.replace('-', '/')
        try:
            valor_iso = datetime.strptime(valor, '%d/%m/%Y').date().isoformat()
        except ValueError:
            valor_iso = data
        self.page.get_by_role('textbox', name='Data limite', exact=True).fill(valor_iso)

    def guardar(self):
        self.page.get_by_role('button', name='Guardar', exact=True).click()

    def consultar_prioridade(self):
        self.page.get_by_role('combobox', name='Prioridade', exact=True).click()

    def verificar_opcoes_prioridade(self):
        expect(self.page.get_by_role('option', name='Baixa', exact=True)).to_be_attached()
        expect(self.page.get_by_role('option', name='Média', exact=True)).to_be_attached()
        expect(self.page.get_by_role('option', name='Alta', exact=True)).to_be_attached()
        combobox = self.page.get_by_role('combobox', name='Prioridade', exact=True)
        expect(combobox).to_contain_text('Baixa')
        expect(combobox).to_contain_text('Média')
        expect(combobox).to_contain_text('Alta')

    def verificar_prioridade_selecionada(self, prioridade):
        expect(self.page.get_by_role('combobox', name='Prioridade', exact=True)).to_have_value(prioridade)

    def cancelar(self):
        self.page.get_by_role('link', name='Cancelar', exact=True).click()
