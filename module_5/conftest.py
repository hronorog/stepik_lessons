import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en-gb', help="Choose language for test")


@pytest.fixture(scope="function")
def browser(request):
    # узнаем язык сайта
    language = request.config.getoption("language")

    if language not in ['ru', 'en-gb', 'es', 'fr']:
        raise pytest.UsageError('Incorrect language')

    options = Options()  # получить языковую метку
    options.add_experimental_option('prefs', {'intl.accept_languages': language})

    print('\nStart...')
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)

    # передаем язык в объект браузера
    browser.user_language = language

    yield browser

    print("\nquit browser...")
    browser.quit()
