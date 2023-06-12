import logging

from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from pages.signupPage import SignupPage
from utilities.utils import Utils

class LoginPage(BaseDriver):
    log = Utils.custom_logger(logLevel=logging.INFO)
    def __init__(self, driver):
        super().__init__(driver)
        self.addHandeler()
        self._url = "https://automationexercise.com/login"
        self._signUpFormXPath = "//div[@class='signup-form']/h2[text()='New User Signup!']"
        self._nameInputXPath = "//div[@class='signup-form']//input[@name='name']"
        self._emailInputXPath = "//div[@class='signup-form']//input[@name='email']"
        self._signupButtonXPath = "//div[@class='signup-form']//button[text()='Signup']"
        self._htmlBodyTag = "body"
        pass

    def getPageUrl(self):
        return self._url

    def getSignUpFormWE(self):
        return self.driver.find_element(By.XPATH, self._signUpFormXPath)

    def getNameInputWE(self):
        return self.driver.find_element(By.XPATH, self._nameInputXPath)

    def getEmailInputWE(self):
        return self.driver.find_element(By.XPATH, self._emailInputXPath)

    def getSignupButtonWE(self):
        return self.driver.find_element(By.XPATH, self._signupButtonXPath)

    def isFormHeaderPresent(self):
        return self.isPresent(self._signUpFormXPath)

    def fillupSignupForm(self, name, email):
        self.inputText(self.getNameInputWE(), name)
        self.inputText(self.getEmailInputWE(), email)
        self.waitForSecond(2)
        self.clickAndWait(self.getSignupButtonWE())
        self.log.info("First Sign Up form submmited")
        return SignupPage(self.driver)
        pass
