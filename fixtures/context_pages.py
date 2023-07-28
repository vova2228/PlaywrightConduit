import pytest
from playwright.sync_api import sync_playwright, Page, BrowserContext


def get_option(option: str, request):
    custom_browser = request.config.getoption("--browser")
    match option:
        case '--browser':
            return custom_browser[0] if len(custom_browser) > 0 else 'chromium'
        case _:
            return request.config.getoption(option)


def get_firefox_browser(playwright, **kwargs):
    return playwright.firefox.launch(
        headless=kwargs['custom_headless'],
        slow_mo=kwargs['custom_slowmo']
    )


def get_chrome_browser(playwright, **kwargs):
    return playwright.chromium.launch(
        headless=kwargs['custom_headless'],
        slow_mo=kwargs['custom_slowmo']
    )


def get_context(browser) -> BrowserContext:
    context = browser.new_context()
    return context


@pytest.fixture(scope="function")
def browser_page(request, ) -> Page:
    playwright = sync_playwright().start()
    custom_browser = get_option('--browser', request)
    custom_headless = not get_option('--headed', request)
    custom_slowmo = get_option('--slowmo', request)
    match custom_browser:
        case 'firefox':
            browser = get_firefox_browser(playwright, custom_headless=custom_headless, custom_slowmo=custom_slowmo)
        case _:
            browser = get_chrome_browser(playwright, custom_headless=custom_headless, custom_slowmo=custom_slowmo)

    context = get_context(browser)
    page_data = context.new_page()

    yield page_data
    for context in browser.contexts:
        context.close()
    browser.close()
    playwright.stop()
