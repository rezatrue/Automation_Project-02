import logging

from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.utils import Utils


class AccountCreatedPage(BaseDriver):
    log = Utils.custom_logger(logLevel=logging.INFO)
    def __init__(self, driver):
        super().__init__(driver)
        self.addHandeler()
        self._url = "https://automationexercise.com/account_created"
        self._titleXPath = "//section[@id='form']//h2"
        self._pageTitle = "Account Created!"
        self._continueButtonXPath = "//a[text()='Continue']"
        self._googeAddUrl = "https://automationexercise.com/account_created#google_vignette"
        self._aswift_IframesXpath = "//iframe[contains(@id,'aswift_')]"
        self._adIframeXpath = "//iframe[@id='ad_iframe']"
        self._closeAddButtonXPath = "//div[@id='dismiss-button']/div/span"
        self._closeAddBtn1XPath = "//div[@id='dismiss-button']//*[name()='path'][1]"
        pass

    def getPageUrl(self):
        return self._url

    def getPageTitleWE(self):
        return self.driver.find_element(By.XPATH, self._titleXPath)

    def getPageTitle(self):
        return self._pageTitle

    def getContinueButtonWE(self):
        return self.driver.find_element(By.XPATH, self._continueButtonXPath)

    def getGoogleAddUrl(self):
        return self._googeAddUrl

    def getAswift_IframesWE(self):
        return self.driver.find_elements(By.XPATH, self._aswift_IframesXpath)

    def getAdIframeWE(self):
        return self.driver.find_element(By.XPATH, self._adIframeXpath)

    def getCloseAddButtonWE(self):
        return self.driver.find_element(By.XPATH, self._closeAddButtonXPath)

    def getCloseAddBtn1WE(self):
        return self.driver.find_element(By.XPATH, self._closeAddBtn1XPath)

    def getPageTitleText(self):
        return self.getText(self.getPageTitleWE())

    def ifPageTitlePresent(self):
        titleExpected = self.getPageTitle()
        titleActual = self.getPageTitleText()
        if (titleExpected.lower() == titleActual.lower()):
            return True
        return False
    def clickRegistrationContinueButton(self):
        self.clickOnWe(self.getContinueButtonWE())
        self.waitForSecond(2)
        self.log.info("Continue Sign Up button clicked")

        gAddUrl = self._googeAddUrl
        if self.getCurrentUrl() == gAddUrl:
            self.waitForSecond(2)
            iframes = self.getAswift_IframesWE()
            if len(iframes) > 0:
                for frame in iframes:
                    if self.switchToIframe(frame):
                        if self.isPresent(self._closeAddBtn1XPath):
                            self.clickAndWait(self.getCloseAddBtn1WE())
                            break
                        if self.switchToIframe(self.getAdIframeWE()):
                            self.clickAndWait(self.getCloseAddButtonWE())
                        else:
                            self.switchBackFromIframe()
            else:
                print("No Add Iframe detected")