import pytest

from pages.homepage import HomePage
from utilities.utils import Utils
from ddt import ddt
import json

@ddt
@pytest.mark.usefixtures("setup")
class TestUserRegistration:
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.hp = HomePage(self.driver)
        self.utils = Utils()

    @staticmethod
    def read_csv_test_data():
        with open("../testdata/testdata.json", "r") as file:
            test_data = json.load(file)
        return test_data

    @pytest.mark.parametrize("test_data", read_csv_test_data().values())
    def test_register_and_delete_account(self, test_data):
        actual = False
        self.hp.openPageUrl()
        lp = self.hp.clickOnSignupButton()
        if lp.isFormHeaderPresent():
            sp = lp.fillupSignupForm(test_data['name'], test_data['email'])
            if sp.isSignupFormPresent():
                acp = sp.fillupAccountInformationForm(test_data['title'], test_data['password'], test_data['date'], test_data['month'], test_data['year'], test_data['firstname'], test_data['lastname'], test_data['address'], test_data['country'], test_data['state'], test_data['city'], test_data['zip'], test_data['phone'])
                if acp.ifPageTitlePresent():
                    acp.clickRegistrationContinueButton()
                    if self.hp.isLogoutButtonPresent():
                        dap = self.hp.clickOnDeleteAccountButton()
                        if dap.isPageTitlePresent():
                            dap.clickOnContinueButton()
                            if self.hp.isSignUpButtonPresent():
                                actual = True

        assert actual == test_data['expected']
        pass
