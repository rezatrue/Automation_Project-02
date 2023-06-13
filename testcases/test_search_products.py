import logging

import pytest
import softest

from pages.homepage import HomePage
from utilities.utils import Utils


@pytest.mark.usefixtures("setup")
class TestSearchProducts(softest.TestCase):
    log = Utils.custom_logger(logLevel=logging.INFO)

    @pytest.fixture(autouse=True)
    def setUp(self):
        self.hp = HomePage(self.driver)
        self.utils = Utils()
        pass

    @pytest.mark.parametrize('key', [('shirt')])
    def test_search_product(self, key):
        self.log.info("---------------->test_search_product")
        pp = self.hp.clickOnProductBtn()
        if pp.url != pp.getCurrentUrl():
            pp.driver.get(pp.url)
        pp.searchProduct(key)
        produts = pp.getProductsList()
        self.utils.assertListItemText(produts, "shirt")
        pass

    def test_category_men_products(self):
        self.log.info("---------------->test_category_men_products")
        pp = self.hp.clickOnProductBtn()
        if pp.url != pp.getCurrentUrl():
            pp.driver.get(pp.url)
        pp.scrollToCategory()
        submenuList = pp.getCategorySubmenuListWE("Men")
        for i in range(1, len(submenuList)+1):
            cat_name = pp.clickOnSubmenu("Men", i)
            header = pp.getProductHeader()
            self.utils.assertListItemText(header, cat_name)

        pass