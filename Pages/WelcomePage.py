import time

from ConfigFiles.SeleniumDriver import SeleniumDriver


class WelcomePage(SeleniumDriver):

    _iniciarSesionDropDownBtn = "//a[@id='Header_GlobalLogin_signInQuickLink']"
    _iniciarSesionOption = "//a[@id='signInQuickLink']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def goToLoginPage(self):
        self.clickElement(self._iniciarSesionDropDownBtn)
        time.sleep(4)
        self.clickElement(self._iniciarSesionOption)
        time.sleep(4)