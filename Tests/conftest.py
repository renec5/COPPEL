import shutil

import pytest
import logging
import os
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

@pytest.fixture(scope="session")
def cleanLogs():
    logFile = open("Automation.log", 'w')
    logFile.close()
    shutil.rmtree("/Users/rene.cortes/PycharmProjects/COPPEL/AllureReports")
    os.mkdir("/Users/rene.cortes/PycharmProjects/COPPEL/AllureReports")

"""
@pytest.fixture(scope='session')
def generateAllureReport():
    os.system('allure serve /Users/rene.cortes/Desktop/COPPELReports')
"""

def pytest_addoption(parser):
    parser.addoption("--browser", help="Please enter a browser to perform the tests example: \n --browser chrome")