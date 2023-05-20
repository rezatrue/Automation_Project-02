from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class DeleteAccountPage(BaseDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.__url = "https://automationexercise.com/delete_account"
        self.__titleXPath = "//section[@id='form']//h2"
        self.__pageTitle = "ACCOUNT DELETED!"
        self.__continueButtonXPath = "//a[text()='Continue']"
        pass

    def getPageUrl(self):
        return self.__url

    def getPageTitleWE(self):
        return self.driver.find_element(By.XPATH, self.__titleXPath)


    def getContinueButtonWE(self):
        return self.driver.find_element(By.XPATH, self.__continueButtonXPath)

    def getPageTitle(self):
        return self.getText(self.getPageTitleWE())

    def clickOnContinueButton(self):
        self.clickAndWait(self.getContinueButtonWE())

    def isPageTitlePresent(self):
        actualText = self.getPageTitle()
        expectedText = self.__pageTitle
        if expectedText.lower() == actualText.lower():
            return True
        return False
        pass