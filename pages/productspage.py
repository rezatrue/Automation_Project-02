import time

from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver
from pages.cartpage import CartPage

class ProductsPage(BaseDriver):

    def __init__(self, driver):
        print("--> Products  Page loading ...")
        super().__init__(driver)
        self.addHandeler()
        self.url = "https://automationexercise.com/products"
        self._productImageWrappersXPath = "//div[@class='product-image-wrapper']"
        self._viewProductXPath = "//div[@class='product-image-wrapper']//a[contains(text(),'View Product')]"
        # self._addToCartXPath = "//div[@class='overlay-content']/a"
        self._addToCartXPath = ".//a[contains(@class,'add-to-cart')]"
        self._continueShoppingXPath = "//div[@id='cartModal']//button[contains(text(),'Continue Shopping')]"
        self._cartBtnXPath = "//ul[@class='nav navbar-nav']//a[contains(text(),'Cart')]"

        self._searchInputXPath = "//input[@id='search_product']"
        self._searchBtnXPath = "//button[@id='submit_search']"
        self._pruductsNameXPath = "//div[@class='single-products']/div/p"
        self._searchTitleXPath = "//h2[contains(text(),'Searched Products')]"
        self._categoryheadXPath = "//h2[contains(text(),'Category')]"
        self._categoryMenXPath = "//*[@id='accordian']/div[2]/div[1]/h4/a"
        self._categorySubitemsXPath = "//*[@id='{}']/div/ul/li/a"
        self._subItemXPath = "//*[@id='{}']/div/ul/li[{}]/a"
        self._displayProductHeaderXPath = "//h2[@class='title text-center']"
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

    def getSearchInputFieldWE(self):
        return self.driver.find_element(By.XPATH, self._searchInputXPath)

    def getSearchBtnWE(self):
        return self.driver.find_element(By.XPATH, self._searchBtnXPath)

    def getPruductsNameWEs(self):
        return self.driver.find_elements(By.XPATH, self._pruductsNameXPath)

    def searchProduct(self, name):
        self.inputText(self.getSearchInputFieldWE(), name)
        self.clickAndWait(self.getSearchBtnWE())
        isexist = self.waitForItemLoad(self._searchTitleXPath, 5)
        if isexist == False:
            time.sleep(5)
        pass

    def getProductsList(self):
        products = []
        for element in self.getPruductsNameWEs():
            products.append(self.getText(element))
        return products
        pass

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
        return CartPage(self.driver)


    def getCategoryheadWE(self):
        return self.driver.find_element(By.XPATH, self._categoryheadXPath)
    def scrollToCategory(self):
        self.scrollToElement(self.getCategoryheadWE())
        pass

    def getCategoryheadMenWE(self):
        return self.driver.find_element(By.XPATH, self._categoryMenXPath)

    def getCategoryMenWE(self):
        return self.driver.find_element(By.XPATH, self._categoryMenXPath)

    def getDisplayProductHearWE(self):
        return self.driver.find_element(By.XPATH, self._displayProductHeaderXPath)

    def getProductHeader(self):
        return self.getText(self.getDisplayProductHearWE())
    def getCategorySubmenuListWE(self, category):
        return self.driver.find_elements(By.XPATH, self._categorySubitemsXPath.format(category))

    def getCategorySubmenuWE(self, cat, num):
        return self.driver.find_element(By.XPATH, self._subItemXPath.format(cat, num))

    def clickOnSubmenu(self, cat, num):
        self.driver.refresh() # need to use as item get slate
        self.clickOnWe(self.getCategoryMenWE())
        self.clickOnWe(self.getCategorySubmenuWE(cat, num))
        time.sleep(5)
        return self.getProductHeader()
        pass