import logging
import time
import unittest
import pytest
import ConfigFiles.CustomLogger as cl
from Pages.WelcomePage import WelcomePage


@pytest.mark.usefixtures("oneTimeSetUp")
class Tests(unittest.TestCase):

    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def classSetUp(self, oneTimeSetUp):
        self.WP = WelcomePage(self.driver)

    def test_valid_login(self):
        self.WP.goToLoginPage()
        time.sleep(7)

