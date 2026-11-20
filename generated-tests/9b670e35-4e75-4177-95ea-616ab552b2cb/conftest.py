import os

import pytest
from playwright.sync_api import sync_playwright

pytest_plugins = ["steps.tarefas", "steps.criar_tarefa_data_limite"]


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
    yield page


@pytest.fixture
def app_url():
    return os.environ["APP_URL"]
