from playwright.sync_api import Page
from config import settings
from pages.sign_up_page import SignUpPage


class LoginPage(SignUpPage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.base_url = settings.LOGIN_URL
        self.page = page
        self._need_account_button = page.locator('//p//a[@ui-sref="app.register"]')

    def open_page(self):
        self.page.goto(self.base_url, wait_until='load')

    def sign_in(self):
        self._email_form.fill('azrlckgi@tcvubciz.com')
        self._password_form.fill('1234Aa')
        self._sign_button.click()
