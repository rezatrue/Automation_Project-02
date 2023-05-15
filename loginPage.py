from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://automationexercise.com/login"
        self.SignUpFormXPath = "//div[@class='signup-form']/h2[text()='New User Signup!']"
        self.nameInputXPath = "//div[@class='signup-form']//input[@name='name']"
        self.emailInputXPath = "//div[@class='signup-form']//input[@name='email']"
        self.signupButtonXPath = "//div[@class='signup-form']//button[text()='Signup']"
        pass

    def getPageUrl(self):
        return self.url

    def getSignUpFormWE(self):
        return self.driver.find_element(By.XPATH, self.SignUpFormXPath)

    def getNameInputWE(self):
        return self.driver.find_element(By.XPATH, self.nameInputXPath)

    def getEmailInputWE(self):
        return self.driver.find_element(By.XPATH, self.emailInputXPath)

    def getSignupButtonWE(self):
        return self.driver.find_element(By.XPATH, self.signupButtonXPath)