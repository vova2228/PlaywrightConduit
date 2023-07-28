import time

from pages.home_page import HomePage


def test_user_login(
        home_page: HomePage
):
    home_page.open_page()
    home_page.click_article_author('Try to transmit the HTTP card, maybe it will override the multi-byte hard drive!')
    time.sleep(5)
