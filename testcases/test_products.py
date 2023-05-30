import time

import pytest

from pages.homepage import HomePage
from utilities.utils import Utils


@pytest.mark.usefixtures("setup")
class TestProducts:

    @pytest.fixture(autouse=True)
    def setUp(self):
        self.hp = HomePage(self.driver)
        self.utils = Utils()
        pass

    def test_add_products(self):
        pp = self.hp.clickOnProductBtn()
        time.sleep(10)
        pp.hoverOverOnNthImage(2)
        time.sleep(10)
        pp.clickOnAddToCart()
        time.sleep(10)
        pp.clickOnContinueShopping()
        time.sleep(10)
        # pp.hoverOverOnNthImage(3)
        # pp.clickOnAddToCard()
        # pp.clickOnContinueShopping()
        pp.clickOnCart()
        pass