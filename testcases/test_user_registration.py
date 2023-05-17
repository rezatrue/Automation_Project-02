import time

import pytest


@pytest.mark.usefixtures("setup")
class TestUserRegistration:
    @pytest.mark.first
    def testVerifyPageIsvisible(self):
        res = self.homepage.openPageUrl()
        assert res

    @pytest.mark.second
    def testVerifyNewUserSignUp(self):
        self.homepage.clickOnSignupButton()
        swe = self.loginPage.getSignUpFormWE()
        assert swe

    @pytest.mark.third
    def testVerifyAccountInformation(self):
        self.loginPage.fillupSignupForm("name", "mail123981@yahoo.com")
        actualTitle = self.signupPage.getSignUpFormTitleText()
        expectedTitle = self.signupPage.getSignupFormExpectedTitle()
        assert (actualTitle.lower() == expectedTitle.lower())

    @pytest.mark.fourth
    def testVerifyAccountInformationFormSubimision(self):
        self.signupPage.fillupAccountInformationForm('mr', "password", "1", "January", "2000", "firstname", "lastname",
                                                     "House #1, Road #1", "United States", "New York", "New York city", "11201",
                                                     '+18801244589')

        titleExpected = self.accountCreatedPage.getPageTitle()
        titleActual = self.browserAction.getPageTitleText()
        assert (titleExpected.lower() == titleActual.lower())
        self.accountCreatedPage.clickRegistrationContinueButton()

        pass

    @pytest.mark.fifth
    def testDeleteAccount(self):
        ep = self.homepage.isLogoutButtonPresent()
        if ep:
            print("Logged in as username")
        else:
            print("Not logged in")

        self.homepage.clickOnDeleteAccountButton()

        actualText = self.deleteAccountPage.getPageTitle().lower()
        expectedText = self.deleteAccountPage.getPageTitle().lower()
        if expectedText in actualText:
            print("Page title match")
        else:
            print("No such Page title present")
        self.deleteAccountPage.clickOnContinueButton()
        time.sleep(2)

        if self.homepage.isSignUpButtonPresent():
            print("Account successfully Deleted")

        assert (actualText == expectedText)
        pass
