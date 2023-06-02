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
        # self._addToCartXPath = "//div[@class='overlay-content']/a"
        self._addToCartXPath = ".//a[contains(@class,'add-to-cart')]"
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
            we = self.getProdutcsImageWrppersWE()[num]
            self.scrollToElement(we)
            if pix != 0:
                self._scrollPixels(pix)
            self.hoverOn(we)
            self.waitForSecond(2)
            return we
        pass

    def _scrollPixels(self, pixels):
        self.scrollToPixels(pixels)

    def clickOnAddToCart(self, parent):
        we = parent.find_element(By.XPATH, self._addToCartXPath)
        self.actionClickOn(we)
        self.waitForSecond(5)
        pass

    def clickOnContinueShopping(self):
        self.switchToPopup()
        self.clickOnWe(self.getContinueShoppingWE())
        self.waitForSecond(2)
        self.switchBackToMain()

        pass

    def clickOnCart(self):
        self.scrollToElement(self.getCartBtnWE())
        self.clickOnWe(self.getCartBtnWE())
        self.addHandeler()
        return CartPage(self.driver)
