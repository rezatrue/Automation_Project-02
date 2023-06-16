import logging
import time

import pytest

from pages.homepage import HomePage
from pages.loginPage import LoginPage
from utilities.utils import Utils


@pytest.mark.usefixtures("setup")
class TestPlaceOrderRegisterWhileCheckout:
    log = Utils.custom_logger(logLevel=logging.INFO)

    @pytest.fixture(autouse=True)
    def setUp(self):
        self.hp = HomePage(self.driver)
        self.utils = Utils()
        pass

    @pytest.mark.dependency()
    def test_place_order(self):
        self.log.info("----------------> test_place_order")
        pp = self.hp.clickOnProductBtn()
        if pp.getPageUrl() != pp.getCurrentUrl():
            pp.driver.get(pp.getPageUrl())
        we = pp.hoverOverOnNthImage(0)
        pp.clickOnAddToCart(we)
        time.sleep(1)
        pp.clickOnContinueShopping()
        time.sleep(2)
        we = pp.hoverOverOnNthImage(2, -40)
        pp.clickOnAddToCart(we)
        time.sleep(1)
        pp.clickOnContinueShopping()
        time.sleep(2)
        cp = pp.clickOnCart()
        cp.clickOnProceedCheckoutBtn()
        assert True
        pass

    @pytest.mark.dependency(depends=["test_place_order"])
    @pytest.mark.parametrize("test_data", Utils().read_xlsx_test_data("./testdata/testdata.xlsx", "checkout"))
    def test_register_login(self, test_data):
        self.log.info("----------------> test_register_login")
        actual = False
        lp = LoginPage(self.driver)
        if lp.getPageUrl() != lp.getCurrentUrl():
            lp.driver.get(lp.getPageUrl())
        if lp.isFormHeaderPresent():
            sp = lp.fillupSignupForm(test_data['name'], test_data['email'])
            if sp.isSignupFormPresent():
                acp = sp.fillupAccountInformationForm(test_data['title'], test_data['password'], test_data['date'], test_data['month'], test_data['year'], test_data['firstname'], test_data['lastname'], test_data['address'], test_data['country'], test_data['state'], test_data['city'], test_data['zip'], test_data['phone'])
                if acp is not None:
                    actual = True
                    if acp.ifPageTitlePresent():
                        acp.clickRegistrationContinueButton()

        assert actual == test_data['expected']

        pass

    @pytest.mark.dependency(depends=["test_place_order", "test_register_login"], scope='class')
    @pytest.mark.parametrize('card_name, card_number, cvc, ex_month, ex_year', [('Visa', '411111111111111111', '311', '02', '2027')])
    def test_check_out(self, card_name, card_number, cvc, ex_month, ex_year):
        self.log.info("----------------> test_check_out")
        cp = self.hp.clickOnCartBtn()
        if cp.getPageUrl() != cp.getCurrentUrl():
            cp.driver.get(cp.getPageUrl())
        cop = cp.clickOnProceedCheckoutBtn()
        payp = cop.clickOnPlacrOrderBtn()
        pdp = payp.submitPaymentInf(card_name, card_number, cvc, ex_month, ex_year)
        assert pdp.isPaymentDonePage()
        pdp.clickOnContinueBtn()
        pass

    @pytest.mark.dependency(depends=["test_register_login"], scope='class')
    def test_delete_account(self):
        self.log.info("----------------> test_delete_account")
        isdeleted = False
        dap = self.hp.clickOnDeleteAccountButton()
        if dap.isPageTitlePresent():
            dap.clickOnContinueButton()
            if self.hp.isSignUpButtonPresent():
                isdeleted = True
        assert isdeleted
        pass