import time
from functional.API.auth_api import AuthAPI
from pages.home_page import HomePage


def test_user_login():
    res = AuthAPI.get_current_user('awdwa')
    print(res)

