from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver


class AccountCreatedPage(BaseDriver):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
        self.url = "https://automationexercise.com/account_created"
        self.titleXPath = "//section[@id='form']//h2"
        self.pageTitle = "Account Created!"
        self.continueButtonXPath = "//a[text()='Continue']"
        self.googeAddUrl = "https://automationexercise.com/account_created#google_vignette"
        self.aswift_IframesXpath = "//iframe[contains(@id,'aswift_')]"
        self.adIframeXpath = "//iframe[@id='ad_iframe']"
        self.closeAddButtonXPath = "//div[@id='dismiss-button']/div/span"
        self.closeAddBtn1XPath = "//div[@id='dismiss-button']//*[name()='path'][1]"
        pass

    def getPageUrl(self):
        return self.url

    def getPageTitleWE(self):
        return self.driver.find_element(By.XPATH, self.titleXPath)

    def getPageTitle(self):
        return self.pageTitle

    def getContinueButtonWE(self):
        return self.driver.find_element(By.XPATH, self.continueButtonXPath)

    def getGoogleAddUrl(self):
        return self.googeAddUrl

    def getAswift_IframesWE(self):
        return self.driver.find_elements(By.XPATH, self.aswift_IframesXpath)

    def getAdIframeWE(self):
        return self.driver.find_element(By.XPATH, self.adIframeXpath)

    def getCloseAddButtonWE(self):
        return self.driver.find_element(By.XPATH, self.closeAddButtonXPath)

    def getCloseAddBtn1WE(self):
        return self.driver.find_element(By.XPATH, self.closeAddBtn1XPath)

    def getPageTitleText(self):
        return BaseDriver.getText(self.getPageTitleWE())

    def clickRegistrationContinueButton(self):
        BaseDriver.clickAndWait(self.getContinueButtonWE())
        time.sleep(2)
        gAddUrl = self.googeAddUrl
        if self.getCurrentUrl() == gAddUrl:
            time.sleep(2)
            iframes = self.accountCreatedPage.getAswift_IframesWE()
            if len(iframes) > 0:
                for frame in iframes:
                    if self.browserAction.switchToIframe(frame):
                        if self.browserAction.isPresent(self.accountCreatedPage.getCloseAddBtn1WE()):
                            self.browserAction.clickAndWait(self.accountCreatedPage.getCloseAddBtn1WE())
                            break
                        if self.browserAction.switchToIframe(self.accountCreatedPage.getAdIframeWE()):
                            self.browserAction.clickAndWait(self.accountCreatedPage.getCloseAddButtonWE())
                        else:
                            self.browserAction.switchBackFromIframe()
            else:
                print("No Add Iframe detected")