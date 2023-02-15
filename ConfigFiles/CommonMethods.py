import logging
import allure

import ConfigFiles.CustomLogger as cl


class CommonMethods:

    log = cl.customLogger(logging.DEBUG)

    def printTestName(self, testName):
        msg = "\n\n\n" + "*"*80 + "\n" + testName.center(80, "*") + "\n" + "*"*80 + "\n\n\n"
        self.log.info(msg)

    def allureSteps(self, text):
        with allure.step(text):
            pass
