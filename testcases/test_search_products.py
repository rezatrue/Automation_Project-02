import pytest

from pages.homepage import HomePage
from utilities.utils import Utils


@pytest.mark.usefixtures("setup")
class TestSearchProducts:

    @pytest.fixture(autouse=True)
    def setUp(self):
        self.hp = HomePage(self.driver)
        self.utils = Utils()
        pass

    @pytest.mark.parametrize('key', [('shirt')])
    def test_search_product(self, key):
        pp = self.hp.clickOnProductBtn()
        if pp.url != pp.getCurrentUrl():
            pp.driver.get(pp.url)
        pp.searchProduct(key)
        produts = pp.getProductsList()

        for name in produts:
            if "shirt" in name:
                print(f"Found in {name}")
            else:
                print(f"Not Found in {name}")
        pass

    def test_category_men_products(self):
        pp = self.hp.clickOnProductBtn()
        if pp.url != pp.getCurrentUrl():
            pp.driver.get(pp.url)
        pp.scrollToCategory()
        submenuList = pp.getCategorySubmenuListWE("Men")
        for i in range(1, len(submenuList)+1):
            cat_name = pp.clickOnSubmenu("Men", i)
            header = pp.getProductHeader()
            if cat_name in header:
                print("Nice work")
            else:
                print("Not working well")

        pass