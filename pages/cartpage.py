import logging
import time

from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver
from pages.checkoutpage import CheckoutPage
from utilities.utils import Utils


class CartPage(BaseDriver):

    log = Utils.custom_logger(logLevel=logging.INFO)

    def __init__(self, driver):
        super().__init__(driver)
        self.addHandeler()
        self._itemsXpath = "//tr[contains(@id,'product-')]"
        self._removeItemXpath = "//a[@class='cart_quantity_delete']"
        self._proceedCheckoutBtnXPath = "//*[@id='do_action']//a[@class='btn btn-default check_out']"
        pass

    def getItems(self):
        return self.driver.find_elements(By.XPATH, self._itemsXpath)

    def getItemCounts(self):
        self.log.info("%s Items in the Cart" % str(len(self.getItems())))
        return len(self.getItems())

    def getItem(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)

    def removeAllItemsfromCart(self):
        for i in range(0, len(self.getItems())):
            print(self._itemsXpath + "["+str(i+1)+"]" + self._removeItemXpath)
            self.clickOnWe(self.getItem(self._itemsXpath + "[1]" + self._removeItemXpath))
            time.sleep(10)


    def getProceedCheckoutBtnWE(self):
        return self.driver.find_element(By.XPATH, self._proceedCheckoutBtnXPath)

    def clickOnProceedCheckoutBtn(self):
        self.clickAndWait(self.getProceedCheckoutBtnWE())
        print("Click on proceed to checkout button")
        return CheckoutPage(self.driver)