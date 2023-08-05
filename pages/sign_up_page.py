from playwright.sync_api import Page
from config import settings
from pages.base_page import BPage


class SignUpPage(BPage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.base_url = settings.SIGN_UP_URL
        self.page = page
        self._need_account_button = page.locator('//p//a[@ui-sref="app.login"]')
        self._username_form = page.locator('[type="text"]')
        self._email_form = page.locator('[type="email"]')
        self._password_form = page.locator('[type="password"]')
        self._sign_button = page.locator('[type="submit"]')

    def wait_page(self):
        self.page.wait_for_load_state()

    def open_page(self):
        self.page.goto(self.base_url, wait_until='load')

    def fill_username_field(self, username: str):
        self._username_form.fill(username)

    def fill_email_field(self, email: str):
        self._email_form.fill(email)

    def fill_password_field(self, password: str):
        self._password_form.fill(password)

    def click_sign_up_button(self):
        self._sign_button.click()
