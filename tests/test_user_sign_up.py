import time

from functional.API.auth_api import AuthAPI
from functional.generator.generator import TestDataGenerator
from pages.home_page import HomePage
from pages.sign_up_page import SignUpPage
from utils.utils import Utils


def test_new_user_sign_up(
        home_page: HomePage,
        sign_up_page: SignUpPage
):

    home_page.open_page()
    home_page.click_sign_up_in_header()

    email, username, password = TestDataGenerator().generate_user_data()

    sign_up_page.wait_page()
    sign_up_page.fill_email_field(email)
    sign_up_page.fill_username_field(username)
    sign_up_page.fill_password_field(password)
    sign_up_page.click_sign_up_button()

    user_token = Utils.get_user_token_from_local_storage(home_page)
    backend_user = AuthAPI.get_current_user(user_token)

    assert email == backend_user.email
    assert username == backend_user.username
