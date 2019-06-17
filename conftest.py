import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    # fp = webdriver.FirefoxProfile()                        #для FireFox
    # fp.set_preference("intl.accept_languages", language)
    # browser = webdriver.Firefox(firefox_profile=fp)

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)

    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()