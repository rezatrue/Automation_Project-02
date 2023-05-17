from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class AccountCreatedPage(BaseDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.__url = "https://automationexercise.com/account_created"
        self.__titleXPath = "//section[@id='form']//h2"
        self.__pageTitle = "Account Created!"
        self.__continueButtonXPath = "//a[text()='Continue']"
        self.__googeAddUrl = "https://automationexercise.com/account_created#google_vignette"
        self.__aswift_IframesXpath = "//iframe[contains(@id,'aswift_')]"
        self.__adIframeXpath = "//iframe[@id='ad_iframe']"
        self.__closeAddButtonXPath = "//div[@id='dismiss-button']/div/span"
        self.__closeAddBtn1XPath = "//div[@id='dismiss-button']//*[name()='path'][1]"
        pass

    def getPageUrl(self):
        return self.__url

    def getPageTitleWE(self):
        return self.driver.find_element(By.XPATH, self.__titleXPath)

    def getPageTitle(self):
        return self.__pageTitle

    def getContinueButtonWE(self):
        return self.driver.find_element(By.XPATH, self.__continueButtonXPath)

    def getGoogleAddUrl(self):
        return self.__googeAddUrl

    def getAswift_IframesWE(self):
        return self.driver.find_elements(By.XPATH, self.__aswift_IframesXpath)

    def getAdIframeWE(self):
        return self.driver.find_element(By.XPATH, self.__adIframeXpath)

    def getCloseAddButtonWE(self):
        return self.driver.find_element(By.XPATH, self.__closeAddButtonXPath)

    def getCloseAddBtn1WE(self):
        return self.driver.find_element(By.XPATH, self.__closeAddBtn1XPath)

    def getPageTitleText(self):
        return self.getText(self.getPageTitleWE())

    def clickRegistrationContinueButton(self):
        self.clickOnWe(self.getContinueButtonWE())
        self.waitForSecond(2)

        gAddUrl = self.__googeAddUrl
        if self.getCurrentUrl() == gAddUrl:
            self.waitForSecond(2)
            iframes = self.getAswift_IframesWE()
            if len(iframes) > 0:
                for frame in iframes:
                    if self.switchToIframe(frame):
                        if self.isPresent(self.getCloseAddBtn1WE()):
                            self.clickAndWait(self.getCloseAddBtn1WE())
                            break
                        if self.switchToIframe(self.getAdIframeWE()):
                            self.clickAndWait(self.getCloseAddButtonWE())
                        else:
                            self.switchBackFromIframe()
            else:
                print("No Add Iframe detected")