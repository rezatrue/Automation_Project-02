from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://automationexercise.com/"
        self.SignUpXPath = "//a[contains(text(),'Signup / Login')]"
        self.deleteAccountBtnXPath = "//a[contains(text(),'Delete Account')]"
        self.logoutBtnXPath = "//a[contains(text(),'Logout')]"
        pass

    def getPageUrl(self):
        return self.url

    def getSignUpButtonWE(self):
        return self.driver.find_element(By.XPATH, self.SignUpXPath)

    def getLogoutButtonWE(self):
        return self.driver.find_element(By.XPATH, self.logoutBtnXPath)

    def getDeleteAccountButtonWE(self):
        return self.driver.find_element(By.XPATH, self.deleteAccountBtnXPath)
