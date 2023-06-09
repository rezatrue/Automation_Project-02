import logging
import time

from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver
from pages.paymentdonepage import PaymentDonePage
from utilities.utils import Utils


class PaymentPage(BaseDriver):

    log = Utils.custom_logger(logLevel=logging.INFO)

    def __init__(self, driver):
        super().__init__(driver)
        self.addHandeler()
        self._nameOnCardInputXPath = "//*[@id='payment-form']//input[@name='name_on_card']"
        self._cardNumberInputXPath = "//*[@id='payment-form']//input[@name='card_number']"
        self._cvcInputXPath = "//*[@id='payment-form']//input[@name='cvc']"
        self._expiryMonthInputXPath = "//*[@id='payment-form']//input[@name='expiry_month']"
        self._expiryYearInputXPath = "//*[@id='payment-form']//input[@name='expiry_year']"
        self._confirmOrderBtnXPath = "//*[@id='payment-form']//button[@id='submit']"
        pass

    def getNameOnCardInputWE(self):
        return self.driver.find_element(By.XPATH, self._nameOnCardInputXPath)

    def getCardNumberInputWE(self):
        return self.driver.find_element(By.XPATH, self._cardNumberInputXPath)

    def getCvcInputWE(self):
        return self.driver.find_element(By.XPATH, self._cvcInputXPath)

    def getExpiryMonthInputWE(self):
        return self.driver.find_element(By.XPATH, self._expiryMonthInputXPath)

    def getExpiryYearInputWE(self):
        return self.driver.find_element(By.XPATH, self._expiryYearInputXPath)

    def getConfirmOrderBtnWE(self):
        return self.driver.find_element(By.XPATH, self._confirmOrderBtnXPath)

    def clickOnConfirmOrderBtn(self):
        self.clickAndWait(self.getConfirmOrderBtnWE())
        print("Click on pay & confirm order button")
        return PaymentDonePage(self.driver)

    def submitPaymentInf(self, card_name, card_number, cvc, ex_month, ex_year):
        self.inputText(self.getNameOnCardInputWE(), card_name)
        self.inputText(self.getCardNumberInputWE(), card_number)
        self.waitForSecond(1)
        self.inputText(self.getCvcInputWE(), cvc)
        self.inputText(self.getExpiryMonthInputWE(), ex_month)
        self.inputText(self.getExpiryYearInputWE(), ex_year)
        self.clickOnConfirmOrderBtn()
        pass