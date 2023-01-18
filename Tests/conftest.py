import pytest
import logging
from ConfigFiles.WebDriverFactory import WebDriverFactory

@pytest.fixture()
def oneTimeSetUp(request, browser):

    wdf = WebDriverFactory(browser)
    driver = wdf.getDriverInstance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption('--browser')

def pytest_addoption(parser):
    parser.addoption("--browser", help="Please enter a browser to perform the tests example: \n --browser chrome")