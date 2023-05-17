from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class LoginPage(BaseDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__url = "https://automationexercise.com/login"
        self.__signUpFormXPath = "//div[@class='signup-form']/h2[text()='New User Signup!']"
        self.__nameInputXPath = "//div[@class='signup-form']//input[@name='name']"
        self.__emailInputXPath = "//div[@class='signup-form']//input[@name='email']"
        self.__signupButtonXPath = "//div[@class='signup-form']//button[text()='Signup']"
        self.__htmlBodyTag = "body"
        pass

    def getPageUrl(self):
        return self.url
    def getPageBodyWE(self):
        return self.driver.find_element(By.TAG_NAME, self.__htmlBodyTag)

    def getSignUpFormWE(self):
        return self.driver.find_element(By.XPATH, self.__signUpFormXPath)

    def getNameInputWE(self):
        return self.driver.find_element(By.XPATH, self.__nameInputXPath)

    def getEmailInputWE(self):
        return self.driver.find_element(By.XPATH, self.__emailInputXPath)

    def getSignupButtonWE(self):
        return self.driver.find_element(By.XPATH, self.__signupButtonXPath)

    def fillupSignupForm(self, name, email):
        BaseDriver.inputText(self.getNameInputWE(), name)
        BaseDriver.inputText(self.getEmailInputWE(), email)
        BaseDriver.waitForSecond(2)
        BaseDriver.clickAndWait(self.getSignupButtonWE(), self.__htmlBodyTag)
        pass