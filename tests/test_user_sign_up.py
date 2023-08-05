import time

from functional.Generator.generator import TestDataGenerator
from pages.home_page import HomePage
from pages.sign_up_page import SignUpPage


def test_user_sign_up(
        home_page: HomePage,
        sign_up_page: SignUpPage
):

    home_page.open_page()
    home_page.click_sign_up()

    email, username, password = TestDataGenerator().generate_user_data()

    sign_up_page.wait_page()
    sign_up_page.fill_email_field(email)
    sign_up_page.fill_username_field(username)
    sign_up_page.fill_password_field(password)

    time.sleep(5)

