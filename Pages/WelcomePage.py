import time
import pdb
from ConfigFiles.SeleniumDriver import SeleniumDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class WelcomePage(SeleniumDriver):

    _iniciarSesionDropDownBtn = "//a[@id='Header_GlobalLogin_signInQuickLink']"
    _iniciarSesionOption = "//a[@id='signInQuickLink']"
    _emailField = "//input[@name='logonId']"
    _passwordField = "//input[@name='logonPassword']"
    _searchBar = "//input[@id='SimpleSearchForm_SearchTerm']"
    _searchBtn = "(//a[@title='Buscar'])[2]"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30, poll_frequency=.5)

    def goToLoginPage(self):
        self.clickElement(self._iniciarSesionDropDownBtn)
        time.sleep(2)
        self.clickElement(self._iniciarSesionOption)
        """
        pdb.set_trace()
        
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, self._iniciarSesionDropDownBtn)))
        element.click()
        """

        time.sleep(2)

    def searchProducts(self, productToSearch):
        self.sendKeys(productToSearch, self._searchBar)
        self.clickElement(self._searchBtn)

    def validateSearchResults(self, productSearched):
        # pdb.set_trace()
        productSearchResult = self.getElement("//h1[contains(text(),'" + productSearched + "')]")
        self.Log("Results for product searched are displayed on screen", True)
        return (True if productSearchResult.is_displayed() else False)
