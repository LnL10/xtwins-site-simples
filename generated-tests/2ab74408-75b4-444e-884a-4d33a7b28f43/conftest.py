import os

import pytest
from playwright.sync_api import sync_playwright

pytest_plugins = ["steps.gestor_de_tarefas"]


@pytest.fixture
def app_url():
    return os.environ["APP_URL"]


@pytest.fixture
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        try:
            yield browser
        finally:
            browser.close()


@pytest.fixture
def context(browser):
    context = browser.new_context()
    try:
        yield context
    finally:
        context.close()


@pytest.fixture
def page(context):
    page = context.new_page()
    try:
        yield page
    finally:
        page.close()
