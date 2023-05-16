from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver


class HomePage(BaseDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__url = "https://automationexercise.com/"
        self.__SignUpXPath = "//a[contains(text(),'Signup / Login')]"
        self.__deleteAccountBtnXPath = "//a[contains(text(),'Delete Account')]"
        self.__logoutBtnXPath = "//a[contains(text(),'Logout')]"
        self.__htmlBodyTag = "body"
        pass

    def getPageUrl(self):
        return self.__url

    def getPageBodyWE(self):
        return self.driver.find_element(By.TAG_NAME, self.__htmlBodyTag)

    def getSignUpButtonWE(self):
        return self.driver.find_element(By.XPATH, self.__SignUpXPath)

    def getLogoutButtonWE(self):
        return self.driver.find_element(By.XPATH, self.__logoutBtnXPath)

    def getDeleteAccountButtonWE(self):
        return self.driver.find_element(By.XPATH, self.__deleteAccountBtnXPath)

    def openUrl(self):
        return BaseDriver.openUrlAndCheck(self.getPageUrl(), self.getPageBodyWE())
        pass

    def clickOnSignupButton(self):
        return BaseDriver.clickAndWait(self.getSignUpButtonWE(), self.getPageBodyWE())
        pass