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
        time.sleep(1)
        pp.hoverOverOnNthImage(0)
        time.sleep(1)
        pp.clickOnAddToCart()
        time.sleep(1)
        pp.clickOnContinueShopping()
        time.sleep(1)
        pp.hoverOverOnNthImage(1)
        time.sleep(1)
        pp.clickOnAddToCard()
        time.sleep(1)
        pp.clickOnContinueShopping()
        time.sleep(1)
        pp.clickOnCart()
        pass