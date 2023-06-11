import logging

from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from pages.cartpage import CartPage
from pages.deleteAccountPage import DeleteAccountPage
from pages.loginPage import LoginPage
from pages.productspage import ProductsPage
from utilities.utils import Utils

class HomePage(BaseDriver):
    log = Utils.custom_logger(logLevel=logging.INFO)
    def __init__(self, driver):
        print("--> Home  Page loading ...")
        super().__init__(driver)
        self.addHandeler()
        self.__url = "https://automationexercise.com/"
        self.__SignUpXPath = "//a[contains(text(),'Signup / Login')]"
        self.__deleteAccountBtnXPath = "//a[contains(text(),'Delete Account')]"
        self.__logoutBtnXPath = "//a[contains(text(),'Logout')]"
        self.__htmlBodyTag = "body"
        self._cartBtnXPath = "//ul[@class='nav navbar-nav']/li/a[contains(text(),'Cart')]"
        self._productBtnXPath = "//ul[@class='nav navbar-nav']/li/a[contains(text(),'Products')]"

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
        self.log.info("Sing Up button clicked")
        return LoginPage(self.driver)
        pass

    def clickOnDeleteAccountButton(self):
        self.clickAndWait(self.getDeleteAccountButtonWE())
        self.log.info("Delete Account button clicked")
        return DeleteAccountPage(self.driver)
        pass

    def isLogoutButtonPresent(self):
        return self.isPresent(self.__logoutBtnXPath)
        pass

    def isSignUpButtonPresent(self):
        return self.isPresent(self.__SignUpXPath)

    def getProductBtnButtonWE(self):
        return self.driver.find_element(By.XPATH, self._productBtnXPath)

    def clickOnProductBtn(self):
        self.clickAndWait(self.getProductBtnButtonWE())
        print("Clicked on products from the manu")
        self.log.info("Clicked on products from the manu")
        return ProductsPage(self.driver)

    def getCartButtonWE(self):
        return self.driver.find_element(By.XPATH, self._cartBtnXPath)

    def clickOnCartBtn(self):
        self.clickAndWait(self.getCartButtonWE())
        self.log.info("Clicked on Cart from the manu")
        return CartPage(self.driver)