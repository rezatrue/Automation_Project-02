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
        self.hoverOn(pp.hoverOverOnNthImage(1))
        pp.clickOnAddToCard()
        pp.clickOnContinueShopping()
        self.hoverOn(pp.hoverOverOnNthImage(2))
        pp.clickOnAddToCard()
        pp.clickOnContinueShopping()
        pp.clickOnCart()
        pass