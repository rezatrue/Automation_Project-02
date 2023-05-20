from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from pages.signupPage import SignupPage


class LoginPage(BaseDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.__url = "https://automationexercise.com/login"
        self.__signUpFormXPath = "//div[@class='signup-form']/h2[text()='New User Signup!']"
        self.__nameInputXPath = "//div[@class='signup-form']//input[@name='name']"
        self.__emailInputXPath = "//div[@class='signup-form']//input[@name='email']"
        self.__signupButtonXPath = "//div[@class='signup-form']//button[text()='Signup']"
        self.__htmlBodyTag = "body"
        pass

    def getPageUrl(self):
        return self.__url

    def getSignUpFormWE(self):
        return self.driver.find_element(By.XPATH, self.__signUpFormXPath)

    def getNameInputWE(self):
        return self.driver.find_element(By.XPATH, self.__nameInputXPath)

    def getEmailInputWE(self):
        return self.driver.find_element(By.XPATH, self.__emailInputXPath)

    def getSignupButtonWE(self):
        return self.driver.find_element(By.XPATH, self.__signupButtonXPath)

    def isFormHeaderPresent(self):
        return self.isPresent(self.__signUpFormXPath)

    def fillupSignupForm(self, name, email):
        self.inputText(self.getNameInputWE(), name)
        self.inputText(self.getEmailInputWE(), email)
        self.waitForSecond(2)
        self.clickAndWait(self.getSignupButtonWE())
        return SignupPage(self.driver)
        pass
