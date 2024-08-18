import pytest
from selenium import webdriver


# @pytest.fixture(params=['chrome', 'firefox'])
# def driver(request):
#     if request.param == 'chrome':
#         browser = webdriver.Chrome()
#         browser.maximize_window()
#     elif request.param == 'firefox':
#         browser = webdriver.Firefox()
#         browser.maximize_window()
#     else:
#         raise ValueError('Unknown browser')
#     yield browser
#     browser.quit()

@pytest.fixture
def driver(request):
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    browser.quit()
