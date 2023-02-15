import datetime
import logging

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import ConfigFiles.CustomLogger as cl
from ConfigFiles.CommonMethods import CommonMethods

class SeleniumDriver:

    log = cl.customLogger(logging.DEBUG)
    CM = CommonMethods()

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15, poll_frequency=.5)

    def getByType(self, locatorType="xpath"):
        if(locatorType.upper() == "ID"):
            return By.ID
        elif (locatorType.upper() == "XPATH"):
            return By.XPATH
        elif (locatorType.upper() == "CSS"):
            return By.CSS_SELECTOR
        if (locatorType.upper() == "CLASS"):
            return By.CLASS_NAME
        if (locatorType.upper() == "LINK"):
            return By.LINK_TEXT
        if (locatorType.upper() == "PARTIAL"):
            return By.PARTIAL_LINK_TEXT
        if (locatorType.upper() == "NAME"):
            return By.NAME
        if (locatorType.upper() == "TAG"):
            return By.TAG_NAME

    def getElement(self, locator, locatorType="xpath"):
        element = None
        try:
            element = self.wait.until(EC.presence_of_element_located(((self.getByType(locatorType), locator))))
            self.log.info("Element has been found successfully with locatorType: {0} and locator: {1}".format(locatorType, locator))
            self.CM.allureSteps("Element has been found successfully with locatorType: {0} and locator: {1}".format(locatorType, locator))
        except:
            self.log.info(
                "Element could NOT be found or does not exist with locatorType: {0} and locator: {1}, please check locators".format(locatorType, locator))
            self.CM.allureSteps("Element could NOT be found or does not exist with locatorType: {0} and locator: {1}, please check locators".format(locatorType, locator))
        return element

    def getElements(self, locator, locatorType="xpath"):
        element = None
        try:
            element = self.wait.until(EC.presence_of_all_elements_located(((self.getByType(locatorType), locator))))
            self.log.info("Elements have been found successfully with locatorType: {0} and locator: {1}".format(locatorType, locator))
            self.CM.allureSteps("Elements have been found successfully with locatorType: {0} and locator: {1}".format(locatorType, locator))
        except:
            self.log.error(
                "Elements could NOT be found or does not exist with locatorType: {0} and locator: {1}, please check locators".format(locatorType, locator))
            self.CM.allureSteps("Elements could NOT be found or does not exist with locatorType: {0} and locator: {1}, please check locators".format(locatorType, locator))
        return element

    def clickElement(self, locator, locatorType="xpath"):
        element = None
        try:
            element = self.wait.until(EC.element_to_be_clickable(((self.getByType(locatorType), locator))))
            element.click()
            self.log.info("Element has been clicked correctly with locatorType: {0} and locator: {1}".format(locatorType, locator))
            self.CM.allureSteps("Element has been clicked correctly with locatorType: {0} and locator: {1}".format(locatorType, locator))
        except:
            self.log.error(
                "Element has been clicked correctly with locatorType: {0} and locator: {1}".format(locatorType,
                                                                                                   locator))
            self.CM.allureSteps("Element has been clicked correctly with locatorType: {0} and locator: {1}".format(locatorType,
                                                                                                   locator))
    def sendKeys(self, data, locator, locatorType="xpath"):
        element = None
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("Data {0} has been typed correctly on element with locatorType: {1} and locator: {2}".format(data, locatorType, locator))
            self.CM.allureSteps("Data {0} has been typed correctly on element with locatorType: {1} and locator: {2}".format(data, locatorType, locator))
        except:
            self.log.error("Data {0} could NOT be sent to element with locatorType: {1} and locator: {2}".format(data, locatorType, locator))
            self.CM.allureSteps("Data {0} could NOT be sent to element with locatorType: {1} and locator: {2}".format(data, locatorType, locator))

    def Log(self, text, attahSS=False, status='Info', screenshotSection=''):
        status = status.upper()
        if attahSS:
            with allure.step(text):
                allure.attach(self.driver.get_screenshot_as_png(), name=screenshotSection + datetime.datetime.now().strftime("%d_%m_%y_%H_%M_%S_%f") + ".png", attachment_type=AttachmentType.PNG)
                if status == "INFO":
                    self.log.info(text)
                elif status == "ERROR":
                    self.log.error(text)
                    assert False
        else:
            with allure.step(text):
                if status == "ERROR":
                    assert False








