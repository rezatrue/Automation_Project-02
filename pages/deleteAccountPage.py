from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver


class DeleteAccountPage(BaseDriver):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
        self.url = "https://automationexercise.com/delete_account"
        self.titleXPath = "//section[@id='form']//h2"
        self.pageTitle = "ACCOUNT DELETED!"
        self.continueButtonXPath = "//a[text()='Continue']"

        pass

    def getPageUrl(self):
        return self.url

    def getPageTitleWE(self):
        return self.driver.find_element(By.XPATH, self.titleXPath)

    def getPageTitle(self):
        return self.pageTitle

    def getContinueButtonWE(self):
        return self.driver.find_element(By.XPATH, self.continueButtonXPath)

    def getPageTitle(self):
        return BaseDriver.getText(self.getPageTitleWE())

    def clickOnContinueButton(self):
        BaseDriver.clickOnWe(self.getContinueButtonWE())