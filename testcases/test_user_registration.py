import time
import pytest

from pages.homepage import HomePage
from utilities.utils import Utils


@pytest.mark.usefixtures("setup")
class TestUserRegistration:
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.hp = HomePage(self.driver)
        self.utils = Utils()

    def test_register_and_delete_account(self):
        self.hp.openPageUrl()
        lp = self.hp.clickOnSignupButton()
        if lp.isFormHeaderPresent():
            sp = lp.fillupSignupForm("name", "mail123981@yahoo.com")
            if sp.isSignupFormPresent():
                acp = sp.fillupAccountInformationForm('mr', "password", "1", "January", "2000", "firstname",
                                                        "lastname",
                                                        "House #1, Road #1", "United States", "New York",
                                                        "New York city",
                                                        "11201",
                                                        '+18801244589')
                if acp.ifPageTitlePresent():
                    acp.clickRegistrationContinueButton()

        if self.hp.isLogoutButtonPresent():
            dap = self.hp.clickOnDeleteAccountButton()
            if dap.isPageTitlePresent():
                dap.clickOnContinueButton()

        if self.hp.isSignUpButtonPresent():
            assert True
        else:
            assert False
        pass
