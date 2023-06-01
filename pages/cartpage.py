import logging

from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver
from utilities.utils import Utils


class CartPage(BaseDriver):

    log = Utils.custom_logger(logLevel=logging.INFO)

    def __init__(self, driver):
        super().__init__(driver)
        self._itemsXpath = "//tr[contains(@id,'product-')]"
        self._removeItemXpath = "//a[@class='cart_quantity_delete']"
        pass

    def getItems(self):
        return self.driver.find_elements(By.XPATH, self._itemsXpath)

    def getItemCounts(self):
        self.log.info("%s Items in the Cart" % str(len(self.getItems())))
        return len(self.getItems())

    def getItem(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)

    def removeAllItemsfromCart(self):
        for i in len(self.getItems()):
            print(self._itemsXpath + "["+(i+1)+"]" + self._removeItemXpath)
            self.clickOnWe(self.getItem(self._itemsXpath + "["+(i+1)+"]" + self._removeItemXpath))
