"""Testes do próprio site (não são testes gerados pelo xTwins).

Por omissão servem a pasta website/ num servidor local, no mesmo caminho do GitHub Pages.
Para testar o site publicado: SITE_URL=https://lnl10.github.io/xtwins-site-simples/ pytest tests
"""

import os
import socket
import sys
import threading
from functools import partial
from http.server import ThreadingHTTPServer
from pathlib import Path

import pytest
from playwright.sync_api import Page, sync_playwright

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from serve import PREFIX, WEBSITE, Handler  # noqa: E402

EMAIL = "ana.silva@example.com"
PASSWORD = "Cliente#2026"


@pytest.fixture(scope="session")
def site_url():
    if os.environ.get("SITE_URL"):
        yield os.environ["SITE_URL"].rstrip("/") + "/"
        return
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        port = s.getsockname()[1]
    server = ThreadingHTTPServer(("127.0.0.1", port), partial(Handler, directory=str(WEBSITE)))
    threading.Thread(target=server.serve_forever, daemon=True).start()
    yield f"http://127.0.0.1:{port}{PREFIX}/"
    server.shutdown()


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    errors = []
    page.on("pageerror", lambda error: errors.append(str(error)))
    yield page
    context.close()
    assert not errors, f"Erros de JavaScript: {errors}"


class Site:
    def __init__(self, page: Page, base: str):
        self.page = page
        self.base = base

    def open(self, path):
        self.page.goto(self.base + path)
        self.page.wait_for_selector("body[data-ready=true]")
        return self.page

    def login(self, email=EMAIL, password=PASSWORD):
        self.open("login.html")
        self.page.get_by_label("Email").fill(email)
        self.page.get_by_label("Password").fill(password)
        self.page.get_by_role("button", name="Entrar").click()


@pytest.fixture
def site(page, site_url):
    return Site(page, site_url)
