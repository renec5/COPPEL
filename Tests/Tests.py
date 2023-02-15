import logging
import time
import unittest
import pytest
import ConfigFiles.CustomLogger as cl
from Pages.WelcomePage import WelcomePage
from Pages.LoginPage import LoginPage
from ConfigFiles.CommonMethods import CommonMethods
import os


@pytest.mark.usefixtures("oneTimeSetUp", "cleanLogs")
class Tests(unittest.TestCase):

    log = cl.customLogger(logging.DEBUG)
    CM = CommonMethods()

    @pytest.fixture(autouse=True)
    def classSetUp(self, oneTimeSetUp, cleanLogs):
        self.WP = WelcomePage(self.driver)
        self.LP = LoginPage(self.driver)

    @pytest.mark.smoke
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_invalid_login(self):
        self.CM.printTestName("Invalid Login")
        self.WP.goToLoginPage()
        self.LP.validLogin("evilsnake_@hotmail.com", "12345")
        flag = self.LP.validateInvalidLogin()
        self.assertTrue(flag,
                        "Invalid Login Failed, we were able to login even with incorrect credentials")

    @pytest.mark.smoke
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_serachProducts(self):
        productTosearch = "Pantallas"
        self.WP.searchProducts(productTosearch)
        self.assertTrue(self.WP.validateSearchResults(productTosearch), "Element searched failed")
        time.sleep(7)

"""
para correr los tests con retries de los tests fallidos
# py.test -s -v --reruns 1 --reruns-delay 2 Tests/Tests.py --browser chrome

para correr los tests con retries de los tests fallidos y aparte generar el reporte de allure
# py.test --alluredir='/Users/rene.cortes/Desktop/COPPELReports' -s -v --reruns 1 --reruns-delay 2 Tests/Tests.py --browser chrome

para generar el reporte HTML del allure report .xml que se genera previamente
# allure serve /Users/rene.cortes/Desktop/COPPELReports 

para correr los tests con marker 
py.test --alluredir='/Users/rene.cortes/PycharmProjects/COPPEL/AllureReports' -s -v --reruns 1 --reruns-delay 2 Tests/Tests.py --browser chrome -m smoke

"""