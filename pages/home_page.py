from playwright.sync_api import Page
from pages.base_page import BPage


class HomePage(BPage):

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self._page = page
        self._global_feed = page.locator('//*[contains(text(), "Global Feed")]')
        self._block_tags = page.locator('//*[@class = "col-md-3"]//*[@class = "tag-list"]')
        self._article_list = page.locator('//article-list')

    def click_tag_by_name(self, tag_name: str):
        self._block_tags.locator(f'//a[contains(text(), "{tag_name}")]').click()

    def click_article_by_title(self, article_title: str):
        self._article_list.locator(f'//h1[text()="{article_title}"]').click()

    def click_article_by_row_num(self, num: int):
        self._article_list.locator(f'//article-preview[{num}]').click()

    def click_article_author(self, article_title: str):
        self._article_list.locator(f'//h1[text()="{article_title}"]//preceding::a[@class="author ng-binding"]').click()

