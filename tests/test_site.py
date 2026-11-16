"""Um teste por requisito importante de requirements/requisitos-gestor-tarefas.md."""

import datetime as dt
import re

from playwright.sync_api import expect


def test_raiz_abre_iniciar_sessao(site, page):
    page.goto(site.base)
    expect(page).to_have_url(re.compile(r"login\.html$"))
    expect(page.get_by_role("heading", name="Iniciar sessão")).to_be_visible()


def test_login_com_sucesso_abre_tarefas(site, page):
    site.login(email="Ana.Silva@Example.com")
    expect(page).to_have_url(re.compile(r"tarefas\.html$"))
    expect(page.get_by_text("Ana Silva")).to_be_visible()
    expect(page.get_by_text("2 tarefas por fazer")).to_be_visible()
    expect(page.locator("#lista-tarefas tr")).to_have_count(3)


def test_login_com_campos_vazios(site, page):
    site.login(email="", password="")
    expect(page.get_by_role("alert")).to_have_text("Preencha o email e a password.")
    expect(page).to_have_url(re.compile(r"login\.html$"))


def test_login_com_password_errada(site, page):
    site.login(password="errada")
    expect(page.get_by_role("alert")).to_have_text("Email ou password incorretos.")


def test_paginas_exigem_sessao(site, page):
    for path in ("tarefas.html", "nova-tarefa.html"):
        page.goto(site.base + path)
        expect(page).to_have_url(re.compile(r"login\.html$"))


def test_terminar_sessao(site, page):
    site.login()
    page.get_by_role("button", name="Terminar sessão").click()
    expect(page).to_have_url(re.compile(r"login\.html$"))
    expect(page.get_by_role("status")).to_have_text("Sessão terminada.")
    page.goto(site.base + "tarefas.html")
    expect(page).to_have_url(re.compile(r"login\.html$"))


def test_marcar_concluida_atualiza_contador(site, page):
    site.login()
    page.get_by_label("Concluída: Rever requisitos").check()
    expect(page.get_by_text("1 tarefa por fazer")).to_be_visible()
    page.reload()
    expect(page.get_by_label("Concluída: Rever requisitos")).to_be_checked()
    page.get_by_label("Concluída: Rever requisitos").uncheck()
    expect(page.get_by_text("2 tarefas por fazer")).to_be_visible()


def test_apagar_todas_mostra_sem_tarefas(site, page):
    site.login()
    page.get_by_role("button", name="Apagar Rever requisitos").click()
    expect(page.get_by_role("status")).to_have_text("Tarefa apagada.")
    expect(page.locator("#lista-tarefas tr")).to_have_count(2)
    page.get_by_role("button", name="Apagar Preparar demonstração").click()
    page.get_by_role("button", name="Apagar Enviar relatório semanal").click()
    expect(page.get_by_text("Não tem tarefas.")).to_be_visible()
    expect(page.get_by_text("0 tarefas por fazer")).to_be_visible()


def test_nova_tarefa_validacoes(site, page):
    site.login()
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
    site.login()
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
    site.login()
    page.get_by_role("link", name="Nova tarefa").click()
    page.get_by_label("Título").fill("Não guardar")
    page.get_by_role("link", name="Cancelar").click()
    expect(page).to_have_url(re.compile(r"tarefas\.html$"))
    expect(page.locator("#lista-tarefas tr")).to_have_count(3)
