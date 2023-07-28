import time

from pages.home_page import HomePage
from pages.sign_up_page import SignUpPage


def test_user_sign_up(
        home_page: HomePage,
        sign_up_page: SignUpPage
):

    home_page.open_page()
    home_page.click_sign_up()

    time.sleep(3)
