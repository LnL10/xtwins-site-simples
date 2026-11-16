"""Um teste por requisito importante de requirements/requisitos-gestor-tarefas.md."""

import datetime as dt
import re

from playwright.sync_api import expect


def test_raiz_abre_tarefas_sem_sessao(site, page):
    page.goto(site.base)
    expect(page).to_have_url(re.compile(r"tarefas\.html$"))
    expect(page.get_by_role("heading", name="As minhas tarefas")).to_be_visible()
    expect(page.get_by_role("link", name="Iniciar sessão")).to_be_visible()
    expect(page.get_by_role("button", name="Terminar sessão")).to_be_hidden()
    expect(page.get_by_text("2 tarefas por fazer")).to_be_visible()
    expect(page.locator("#lista-tarefas tr")).to_have_count(3)


def test_tarefas_iniciais_com_e_sem_data_limite(site, page):
    page.goto(site.base)
    linhas = page.locator("#lista-tarefas tr")
    expect(linhas.filter(has_text="Preparar demonstração").get_by_role("cell").nth(2)).to_have_text("31/12/2027")
    expect(linhas.filter(has_text="Rever requisitos").get_by_role("cell").nth(2)).to_have_text("—")


def test_login_com_sucesso_mostra_nome(site, page):
    site.open("tarefas.html")
    page.get_by_role("link", name="Iniciar sessão").click()
    expect(page).to_have_url(re.compile(r"login\.html$"))
    site.login(email="Ana.Silva@Example.com")
    expect(page).to_have_url(re.compile(r"tarefas\.html$"))
    expect(page.get_by_text("Ana Silva")).to_be_visible()
    expect(page.get_by_role("link", name="Iniciar sessão")).to_be_hidden()
    page.goto(site.base + "login.html")
    expect(page).to_have_url(re.compile(r"tarefas\.html$"))


def test_continuar_sem_sessao(site, page):
    site.open("login.html")
    page.get_by_role("link", name="Continuar sem sessão").click()
    expect(page).to_have_url(re.compile(r"tarefas\.html$"))


def test_login_com_campos_vazios(site, page):
    site.login(email="", password="")
    expect(page.get_by_role("alert")).to_have_text("Preencha o email e a password.")
    expect(page).to_have_url(re.compile(r"login\.html$"))


def test_login_com_password_errada(site, page):
    site.login(password="errada")
    expect(page.get_by_role("alert")).to_have_text("Email ou password incorretos.")


def test_terminar_sessao(site, page):
    site.login()
    page.get_by_role("button", name="Terminar sessão").click()
    expect(page).to_have_url(re.compile(r"tarefas\.html$"))
    expect(page.get_by_role("status")).to_have_text("Sessão terminada.")
    expect(page.get_by_role("link", name="Iniciar sessão")).to_be_visible()
    expect(page.get_by_text("Ana Silva")).to_be_hidden()


def test_marcar_concluida_atualiza_contador(site, page):
    site.open("tarefas.html")
    page.get_by_label("Rever requisitos").check()
    expect(page.get_by_text("1 tarefa por fazer")).to_be_visible()
    page.reload()
    expect(page.get_by_label("Rever requisitos")).to_be_checked()
    page.get_by_label("Rever requisitos").uncheck()
    expect(page.get_by_text("2 tarefas por fazer")).to_be_visible()


def test_apagar_todas_mostra_sem_tarefas(site, page):
    site.open("tarefas.html")
    page.get_by_role("row", name="Rever requisitos").get_by_role("button", name="Apagar").click()
    expect(page.get_by_role("status")).to_have_text("Tarefa apagada.")
    expect(page.locator("#lista-tarefas tr")).to_have_count(2)
    page.get_by_role("button", name="Apagar").first.click()
    page.get_by_role("button", name="Apagar").first.click()
    expect(page.get_by_text("Não tem tarefas.")).to_be_visible()
    expect(page.get_by_text("0 tarefas por fazer")).to_be_visible()


def test_nova_tarefa_validacoes(site, page):
    site.open("tarefas.html")
    page.get_by_role("link", name="Nova tarefa").click()
    page.get_by_role("button", name="Guardar").click()
    expect(page.get_by_role("alert")).to_have_text("O título é obrigatório.")
    page.get_by_label("Título").fill("  ab  ")
    ontem = (dt.date.today() - dt.timedelta(days=1)).isoformat()
    page.get_by_label("Data limite").fill(ontem)
    page.get_by_role("button", name="Guardar").click()
    expect(page.get_by_role("alert").locator("li")).to_have_text(
        ["O título deve ter entre 3 e 60 caracteres.", "A data limite não pode ser no passado."]
    )
    expect(page).to_have_url(re.compile(r"nova-tarefa\.html$"))


def test_nova_tarefa_criada(site, page):
    site.open("tarefas.html")
    page.get_by_role("link", name="Nova tarefa").click()
    expect(page.get_by_label("Prioridade")).to_have_value("Média")
    page.get_by_label("Título").fill("Comprar café")
    page.get_by_label("Prioridade").select_option("Alta")
    amanha = dt.date.today() + dt.timedelta(days=1)
    page.get_by_label("Data limite").fill(amanha.isoformat())
    page.get_by_role("button", name="Guardar").click()
    expect(page).to_have_url(re.compile(r"tarefas\.html$"))
    expect(page.get_by_role("status")).to_have_text("Tarefa criada.")
    ultima = page.locator("#lista-tarefas tr").last
    expect(ultima).to_contain_text("Comprar café")
    expect(ultima).to_contain_text("Alta")
    expect(ultima).to_contain_text(amanha.strftime("%d/%m/%Y"))
    expect(page.get_by_text("3 tarefas por fazer")).to_be_visible()


def test_cancelar_nao_cria(site, page):
    site.open("tarefas.html")
    page.get_by_role("link", name="Nova tarefa").click()
    page.get_by_label("Título").fill("Não guardar")
    page.get_by_role("link", name="Cancelar").click()
    expect(page).to_have_url(re.compile(r"tarefas\.html$"))
    expect(page.locator("#lista-tarefas tr")).to_have_count(3)


def test_titulo_identifica_uma_so_celula(site, page):
    """Um localizador pelo título (sem exact) encontra uma só célula e uma só caixa de verificação."""
    site.open("tarefas.html")
    expect(page.get_by_role("cell", name="Rever requisitos")).to_have_count(1)
    expect(page.get_by_role("checkbox", name="Rever requisitos")).to_have_count(1)
    expect(page.get_by_role("button", name="Apagar")).to_have_count(3)
