from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from pages.deleteAccountPage import DeleteAccountPage
from pages.loginPage import LoginPage


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
        self.clickAndWait(self.getSignUpButtonWE())
        return LoginPage(self.driver)
        pass

    def clickOnDeleteAccountButton(self):
        self.clickAndWait(self.getDeleteAccountButtonWE())
        return DeleteAccountPage(self.driver)
        pass

    def isLogoutButtonPresent(self):
        return self.isPresent(self.__logoutBtnXPath)
        pass

    def isSignUpButtonPresent(self):
        return self.isPresent(self.__SignUpXPath)
