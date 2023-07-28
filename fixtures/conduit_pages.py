import pytest

from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.sign_up_page import SignUpPage


@pytest.fixture(scope='function')
def home_page(browser_page: Page) -> HomePage:
    return HomePage(browser_page)


@pytest.fixture(scope='function')
def login_page(browser_page: Page) -> LoginPage:
    return LoginPage(browser_page)


@pytest.fixture(scope='function')
def sign_up_page(browser_page: Page) -> SignUpPage:
    return SignUpPage(browser_page)
