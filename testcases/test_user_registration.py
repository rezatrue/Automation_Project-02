import logging

import pytest

from pages.homepage import HomePage
from utilities.utils import Utils

@pytest.mark.usefixtures("setup")
class TestUserRegistration:
    log = Utils.custom_logger(logLevel=logging.INFO)

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.hp = HomePage(self.driver)
        self.utils = Utils()

    @pytest.mark.dependency()
    @pytest.mark.parametrize("test_data", Utils().read_csv_test_data("./testdata/testdata.csv"))
    # @pytest.mark.parametrize("test_data", Utils().read_json_test_data("../testdata/testdata.json").values())
    # @pytest.mark.parametrize("test_data", Utils().read_xlsx_test_data("../testdata/testdata.xlsx", "signup"))
    def test_register_account(self, test_data):
        self.log.info("---------------->test_register_account")
        actual = False
        # self.hp.openPageUrl()
        lp = self.hp.clickOnSignupButton()
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

        if test_data['expected'] == "TRUE":
            expected = True
        elif test_data['expected'] == "FALSE":
            expected = False
        assert actual == expected
        pass

    @pytest.mark.dependency(depends=["test_register_account"])
    def test_delete_account(self):
        self.log.info("---------------->test_delete_account")
        result = False
        if self.hp.isLogoutButtonPresent():
            dap = self.hp.clickOnDeleteAccountButton()
            if dap.isPageTitlePresent():
                result = True
                dap.clickOnContinueButton()
                # if self.hp.isSignUpButtonPresent():
        assert result
        pass