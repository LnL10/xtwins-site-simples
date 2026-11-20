from urllib.parse import urljoin
from playwright.sync_api import expect
from datetime import date

class ListaDeTarefas:
    page_path = '/xtwins-site-simples/tarefas.html'

    def __init__(self, page, app_url):
        self.page = page
        self.app_url = app_url

    def aceder_a_pagina(self, pagina):
        if pagina != 'Lista de tarefas':
            raise ValueError(f'Página não suportada: {pagina}')
        self.page.goto(urljoin(self.app_url, self.page_path))

    def verificar_pagina(self):
        expect(self.page).to_have_url(urljoin(self.app_url, self.page_path))

    def verificar_colunas(self):
        for coluna in ('Tarefa', 'Prioridade', 'Data limite', 'Ações'):
            expect(self.page.get_by_role('columnheader', name=coluna, exact=True)).to_be_visible()

    def selecionar_ligacao(self, ligacao):
        expect(self.page.get_by_role('link', name=ligacao, exact=True)).to_be_visible()
        self.page.get_by_role('link', name=ligacao, exact=True).click()

    def verificar_tarefa_sem_data_limite(self, pagina, prioridade):
        if pagina != 'Lista de tarefas':
            raise ValueError(f'Página não suportada: {pagina}')
        expect(self.page.get_by_role('cell', name='Rever plano de testes', exact=True)).to_be_visible()
        expect(self.page.get_by_role('row').filter(has_text='Rever plano de testes').get_by_role('cell', name=prioridade, exact=True)).to_be_visible()
        expect(self.page.get_by_role('row').filter(has_text='Rever plano de testes').get_by_role('cell', name='—', exact=True)).to_be_visible()

    def verificar_tarefa_com_data_limite(self, tarefa, prioridade, data_limite):
        data_formatada = date.fromisoformat(data_limite).strftime('%d/%m/%Y')
        expect(self.page.get_by_role('cell', name=tarefa, exact=True)).to_have_text(tarefa)
        expect(self.page.get_by_role('row').filter(has_text=tarefa).get_by_role('cell', name=prioridade, exact=True)).to_have_text(prioridade)
        expect(self.page.get_by_role('row').filter(has_text=tarefa).get_by_role('cell', name=data_formatada, exact=True)).to_have_text(data_formatada)

class NovaTarefa:
    page_path = '/xtwins-site-simples/nova-tarefa.html'

    def __init__(self, page, app_url):
        self.page = page
        self.app_url = app_url

    def verificar_formulario(self, formulario, pagina):
        if pagina != 'Nova tarefa':
            raise ValueError(f'Página não suportada: {pagina}')
        expect(self.page).to_have_url(urljoin(self.app_url, self.page_path))
        expect(self.page.get_by_role('heading', name=formulario, exact=True)).to_be_visible()

    def preencher_campo(self, campo, valor):
        self.page.get_by_role('textbox', name=campo, exact=True).fill(valor)

    def selecionar_opcao(self, seletor, opcao):
        self.page.get_by_role('combobox', name=seletor, exact=True).select_option(label=opcao)

    def selecionar_botao(self, botao):
        self.page.get_by_role('button', name=botao, exact=True).click()

    def verificar_opcoes_do_seletor(self, seletor, opcoes, opcao_selecionada):
        for opcao in opcoes:
            expect(self.page.get_by_role('option', name=opcao, exact=True)).to_be_attached()
        expect(self.page.get_by_role('combobox', name=seletor, exact=True)).to_have_value(opcao_selecionada)
