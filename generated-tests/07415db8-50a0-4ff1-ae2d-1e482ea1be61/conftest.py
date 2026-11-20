import os

import pytest
from playwright.sync_api import Browser, Page, Playwright, sync_playwright

pytest_plugins = ["steps.ui_steps"]


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope="session")
def browser(playwright_instance: Playwright) -> Browser:
    browser = playwright_instance.chromium.launch(headless=True)
    yield browser
    browser.close()


@pytest.fixture
def context(browser: Browser):
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture
def page(context) -> Page:
    page = context.new_page()
    yield page
    page.close()


@pytest.fixture
def app_url() -> str:
    return os.environ["APP_URL"]
