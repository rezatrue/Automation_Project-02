from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class HomePage(BaseDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.__url = "https://automationexercise.com/"
        self.__SignUpXPath = "//a[contains(text(),'Signup / Login')]"
        self.__deleteAccountBtnXPath = "//a[contains(text(),'Delete Account')]"
        self.__logoutBtnXPath = "//a[contains(text(),'Logout')]"
        self.__htmlBodyTag = "body"
        pass

    def getSignUpButtonWE(self):
        return self.driver.find_element(By.XPATH, self.__SignUpXPath)

    def getLogoutButtonWE(self):
        return self.driver.find_element(By.XPATH, self.__logoutBtnXPath)

    def getDeleteAccountButtonWE(self):
        return self.driver.find_element(By.XPATH, self.__deleteAccountBtnXPath)

    def openPageUrl(self):
        return self.openUrlAndCheck(self.__url, self.__htmlBodyTag)
        pass

    def clickOnSignupButton(self):
        return self.clickAndWait(self.getSignUpButtonWE())
        pass

    def clickOnDeleteAccountButton(self):
        return self.clickAndWait(self.getDeleteAccountButtonWE())
        pass

    def isLogoutButtonPresent(self):
        return self.isPresent(self.getLogoutButtonWE())
        pass

    def isSignUpButtonPresent(self):
        return self.isPresent(self.getSignUpButtonWE())