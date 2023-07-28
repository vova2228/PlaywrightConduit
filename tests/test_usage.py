import time

from pages.home_page import HomePage


def test_open_home_page(home_page: HomePage):
    home_page.open_page()
    home_page.click_login()
