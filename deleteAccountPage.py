from selenium.webdriver.common.by import By


class DeleteAccountPage:

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://automationexercise.com/delete_account"
        self.titleXPath = "//section[@id='form']//h2"
        self.pageTitle = "ACCOUNT DELETED!"
        self.continueButtonXPath = "//a[text()='Continue']"

        pass

    def getPageUrl(self):
        return self.url

    def getPageTitleWE(self):
        return self.driver.find_element(By.XPATH, self.titleXPath)

    def getPageTitle(self):
        return self.pageTitle

    def getContinueButtonWE(self):
        return self.driver.find_element(By.XPATH, self.continueButtonXPath)

