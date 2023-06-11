import logging

from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver
from utilities.utils import Utils


class PaymentDonePage(BaseDriver):

    log = Utils.custom_logger(logLevel=logging.INFO)

    def __init__(self, driver):
        super().__init__(driver)
        self.addHandeler()
        self._url = "https://automationexercise.com/payment_done/"
        self._continueBtnXPath = "//*[@id='form']//a[contains(text(),'Continue')]"
        pass

    def getContinueBtnWE(self):
        return self.driver.find_element(By.XPATH, self._continueBtnXPath)

    def isPaymentDonePage(self):
        if self._url in self.getCurrentUrl():
            return True
        else:
            return False

    def clickOnContinueBtn(self):
        self.clickAndWait(self.getContinueBtnWE())
        print("Click on continue button")
