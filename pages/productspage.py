from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver
from pages.cartpage import CartPage

class ProductsPage(BaseDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.addHandeler()
        self._url = "https://automationexercise.com/products"
        self._productImageWrappersXPath = "//div[@class='product-image-wrapper']"
        self._viewProductXPath = "//div[@class='product-image-wrapper']//a[contains(text(),'View Product')]"
        self._addToCartXPath = "//div[@class='overlay-content']/a"
        self._continueShoppingXPath = "//div[@id='cartModal']//button[contains(text(),'Continue Shopping')]"
        self._cartBtnXPath = "//ul[@class='nav navbar-nav']//a[contains(text(),'Cart')]"
        pass

    def getProdutcsImageWrppersWE(self):
        return self.driver.find_elements(By.XPATH, self._productImageWrappersXPath)
    def getviewProductWE(self):
        return self.driver.find_elements(By.XPATH, self._viewProductXPath)

    def getAddToCartWE(self):
        return self.driver.find_element(By.XPATH, self._addToCartXPath)

    def getContinueShoppingWE(self):
        return self.driver.find_element(By.XPATH, self._continueShoppingXPath)
    def getCartBtnWE(self):
        return self.driver.find_element(By.XPATH, self._cartBtnXPath)

    def hoverOverOnNthImage(self, num, pix = 0):
        if num <= len(self.getviewProductWE()):
            self.scrollToElement(self.getProdutcsImageWrppersWE()[num])
            if pix != 0:
                self._scrollPixels(pix)
            self.hoverOn(self.getProdutcsImageWrppersWE()[num])
            self.waitForSecond(4)
        pass

    def _scrollPixels(self, pixels):
        self.scrollToPixels(pixels)

    def clickOnAddToCart(self):
        self.waitForSecond(2)
        self.actionClickOn(self.getAddToCartWE())
        # self.clickOnWe(self.getAddToCartWE())
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
        self.addHandeler()
        return CartPage(self.driver)
