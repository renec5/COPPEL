import logging
from ConfigFiles.SeleniumDriver import SeleniumDriver
from selenium.webdriver.support.wait import WebDriverWait
import ConfigFiles.CustomLogger as cl
import pdb


class LoginPage(SeleniumDriver):

    _emailField = "//input[@id='WC_AccountDisplay_FormInput_logonId_In_Logon_1']"
    _passwordField = "//input[@id='WC_AccountDisplay_FormInput_logonPassword_In_Logon_1']"
    _loginBtn = "//div[@id='btn-login']"
    _invalidLoginMessage = "//span[@id='logonErrorMessage']/p"

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15, poll_frequency=.5)

    def enterEmail(self, emailToEnter):
        self.sendKeys(emailToEnter, self._emailField)

    def enterPassword(self, passwordToEnter):
        self.sendKeys(passwordToEnter, self._passwordField)

    def clickLoginBtn(self):
        self.clickElement(self._loginBtn)

    def validateInvalidLogin(self):
        try:
            invalidLogin = self.getElement(self._invalidLoginMessage)
            flag = True
            # pdb.set_trace()
        except:
            flag = False
        if flag:
            return True
        else:
            return False


    def validLogin(self, userEmail, userPassword):
        self.enterEmail(userEmail)
        self.enterPassword(userPassword)
        self.clickLoginBtn()



