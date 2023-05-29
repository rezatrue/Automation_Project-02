from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver


class ProductsPage(BaseDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self._url = "https://automationexercise.com/products"
        self._appProductImageWrappersXPath = "//div[@class='product-image-wrapper']"
        self._addToCartXPath = "//div[@class='overlay-content']/a"
        self._continueShoppingXPath = "//div[@id='cartModal']//button[contains(text(),'Continue Shopping')]"
        self._cartBtnXPath = "//ul[@class='nav navbar-nav']//a[contains(text(),'Cart')]"
        pass

    def getProdutcsImageWrppersWE(self):
        return self.driver.find_elements(By.XPATH, self._appProductImageWrappersXPath)

    def getAddToCartWE(self):
        return self.driver.find_elements(By.XPATH, self._addToCartXPath)

    def getContinueShoppingWE(self):
        return self.driver.find_elements(By.XPATH, self._continueShoppingXPath)

    def hoverOverOnNthImage(self, num):
        if num <= len(self.getProdutcsImageWrppersWE()):
            self.scrollToElement(self.getProdutcsImageWrppersWE()[num])
            self.hoverOn(self.getProdutcsImageWrppersWE()[num])
            self.waitForSecond(2)
        pass

    def clickOnAddToCart(self):
        self.clickOnWe(self.getAddToCartWE())
        self.waitForSecond(3)
        pass

    def clickOnContinueShopping(self):
        self.clickOnWe(self.getContinueShoppingWE())
        self.waitForSecond(1)
        pass