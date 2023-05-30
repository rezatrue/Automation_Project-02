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
    def getCartBtnWE(self):
        return self.driver.find_elements(By.XPATH, self._cartBtnXPath)

    def hoverOverOnNthImage(self, num):
        if num <= len(self.getProdutcsImageWrppersWE()):
            self.scrollToElement(self.getProdutcsImageWrppersWE()[num])
            self.hoverOn(self.getProdutcsImageWrppersWE()[num])
            self.waitForSecond(4)
        pass

    def clickOnAddToCart(self):
        self.waitForSecond(2)
        self.actionClickOn(self.getAddToCartWE())
        self.waitForSecond(10)
        pass

    def clickOnContinueShopping(self):
        self.switchToPopup()
        self.clickOnWe(self.getContinueShoppingWE())
        self.switchBackToMain()
        self.waitForSecond(2)
        pass

    def clickOnCart(self):
        self.scrollToElement(self.getCartBtnWE())
        self.clickOnWe(self.getCartBtnWE())
        self.waitForSecond(10)
