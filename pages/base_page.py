from playwright.sync_api import Page
from config import settings


class BPage:

    def __init__(self, page: Page):
        self.page = page
        self.base_url = settings.BASE_URL

        self._logo_button = page.locator('//a[@class="navbar-brand ng-binding"]')
        self._github_button = page.locator('//a[contains(@href, "github")]')
        self._home_button = page.locator('//ul[@show-authed="false"]//a[@ui-sref="app.home"]')
        self._sign_in_button = page.locator("//a[@ui-sref='app.login']")
        self._sign_up_button = page.locator("//a[@ui-sref='app.register']")

    def reload(self):
        self.page.reload(wait_until='load')

    def go_back(self):
        self.page.go_back()

    def go_github(self):
        self._github_button.click()

    def go_home_by_logo(self):
        self._logo_button.click()

    def go_home_by_button(self):
        self._home_button.click()

    def open_page(self):
        self.page.goto(self.base_url, wait_until='load')

    def click_login(self):
        self._sign_in_button.click()

    def click_sign_up(self):
        self._sign_up_button.click()

