import logging
import time

from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver
from pages.paymentpage import PaymentPage
from utilities.utils import Utils


class CheckoutPage(BaseDriver):

    log = Utils.custom_logger(logLevel=logging.INFO)

    def __init__(self, driver):
        super().__init__(driver)
        self.addHandeler()
        self._placrOrderBtnXPath = "//*[@id='cart_items']//a[@class='btn btn-default check_out']"
        pass

    def getPlacrOrderBtnWE(self):
        return self.driver.find_element(By.XPATH, self._placrOrderBtnXPath)

    def clickOnPlacrOrderBtn(self):
        self.scrollToElement(self.getPlacrOrderBtnWE())
        self.clickAndWait(self.getPlacrOrderBtnWE())
        print("Click on place order button")
        return PaymentPage(self.driver)
