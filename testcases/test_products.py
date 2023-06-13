import logging
import time

import pytest

from pages.cartpage import CartPage
from pages.homepage import HomePage
from utilities.utils import Utils


@pytest.mark.usefixtures("setup")
class TestProducts:
    log = Utils.custom_logger(logLevel=logging.INFO)

    @pytest.fixture(autouse=True)
    def setUp(self):
        self.hp = HomePage(self.driver)
        self.utils = Utils()
        pass

    def test_add_products(self):
        self.log.info("---------------->test_add_products")
        pp = self.hp.clickOnProductBtn()
        if pp.getPageUrl() != pp.getCurrentUrl():
            pp.driver.get(pp.getPageUrl())
        we = pp.hoverOverOnNthImage(0)
        pp.clickOnAddToCart(we)
        time.sleep(1)
        pp.clickOnContinueShopping()
        time.sleep(2)
        we = pp.hoverOverOnNthImage(1, -40)
        pp.clickOnAddToCart(we)
        time.sleep(1)
        pp.clickOnContinueShopping()
        time.sleep(2)
        cp = pp.clickOnCart()
        assert cp.getItemCounts() == 2
        pass

    def test_remove_products(self):
        self.log.info("---------------->test_remove_products")
        cp = CartPage(self.driver)
        if cp.getPageUrl() != cp.getCurrentUrl():
            cp.driver.get(cp.getPageUrl())
        cp.removeAllItemsfromCart()
        assert True
        pass
