import time

from accountCreatedPage import AccountCreatedPage
from base import Base
from browserAction import BrowserAction
from deleteAccountPage import DeleteAccountPage
from homepage import HomePage
from loginPage import LoginPage
from signupPage import SignupPage


class RegisterUser:

    def __init__(self):
        base = Base()
        driver = base.getDriver()
        self.homepage = HomePage(driver)
        self.loginPage = LoginPage(driver)
        self.signupPage = SignupPage(driver)
        self.accountCreatedPage = AccountCreatedPage(driver)
        self.deleteAccountPage = DeleteAccountPage(driver)
        self.browserAction = BrowserAction(driver)
        pass

    def closeBrowser(self):
        self.browserAction.closeBrowser()
        pass

    def verifyPageIsvisible(self):
        url = self.homepage.getPageUrl()
        res = self.browserAction.openUrl(url)
        print(res)

    def verifyNewUserSignUp(self):
        sbwe = self.homepage.getSignUpButtonWE()
        self.browserAction.clickAndWait(sbwe)
        swe = self.loginPage.getSignUpFormWE()
        if swe != None:
            print("New User SignUp is present")
        else:
            print("No Form present for \"New User SignUp\"")

    def verifyAccountInformation(self):

        ni = self.loginPage.getNameInputWE()
        self.browserAction.inputText(ni, "name")
        ei = self.loginPage.getEmailInputWE()
        self.browserAction.inputText(ei, "mail123981@yahoo.com")
        btn = self.loginPage.getSignupButtonWE()
        time.sleep(5)
        self.browserAction.clickAndWait(btn)

        twe = self.signupPage.getSignUpFormTitleWE()
        actualTitle = self.browserAction.getText(twe)
        expectedTitle = self.signupPage.getSignupFormExpectedTitle()

        print("Actual: " + actualTitle)
        print("Expected: " + expectedTitle)

    def verifyAccountInformationFormSubimision(self):
        title = self.signupPage.getGenderInputWE('mr')
        self.browserAction.clickAndWait(title)

        pwwe = self.signupPage.getPasswordWE()
        self.browserAction.inputText(pwwe, "password")

        dwe = self.signupPage.getDaysWE()
        self.browserAction.selectDropdownItem(dwe, "1")
        mwe = self.signupPage.getMonthsWE()
        self.browserAction.selectDropdownItem(mwe, "January")
        ywe = self.signupPage.getYearsWE()
        self.browserAction.selectDropdownItem(ywe, "2000")

        fnwe = self.signupPage.getFirstNameWE()
        self.browserAction.inputText(fnwe, "firstname")
        lnwe = self.signupPage.getLastNameWE()
        self.browserAction.inputText(lnwe, "lastname")
        a1we = self.signupPage.getAddress1WE()
        self.browserAction.inputText(a1we, "House #1, Road #1")
        cowe = self.signupPage.getCountryWE()
        self.browserAction.selectDropdownItem(cowe, "United States")

        swe = self.signupPage.getStateWE()
        self.browserAction.inputText(swe, "New York")
        ciwe = self.signupPage.getCityWE()
        self.browserAction.inputText(ciwe, "New York")
        zcwe = self.signupPage.getZipcodeWE()
        self.browserAction.inputText(zcwe, "11201")
        pwe = self.signupPage.getPhoneWE()
        self.browserAction.inputText(pwe, '+18801244589')
        btn = self.signupPage.getBtnCreateAccountWE()
        time.sleep(5)
        self.browserAction.clickAndWait(btn)
        time.sleep(5)
        titleExpected = self.accountCreatedPage.getPageTitle()
        titleActual = self.browserAction.getText(self.accountCreatedPage.getPageTitleWE())
        print(titleActual)
        if titleExpected.lower() in titleActual.lower():
            print("Title visible")
        else:
            print("Title Not visible")

        self.browserAction.clickAndWait(self.accountCreatedPage.getContinueButtonWE())
        time.sleep(5)
        gAddUrl = self.accountCreatedPage.googeAddUrl
        if self.browserAction.getCurrentUrl() == gAddUrl:
            iframes = self.accountCreatedPage.getAswift_IframesWE()
            if len(iframes) > 0:
                for frame in iframes:
                    if self.browserAction.switchToIframe(frame):
                        if self.browserAction.switchToIframe(self.accountCreatedPage.getAdIframeWE()):
                            self.browserAction.clickAndWait(self.accountCreatedPage.getCloseAddButtonWE())
                        else:
                            self.browserAction.switchBackFromIframe()
            else:
                print("No Add Iframe detected")

        pass

    def deleteAccount(self):
        ep = self.browserAction.isPresent(self.homepage.getLogoutButtonWE())
        if ep:
            print("Logged in as username")
        else:
            print("Not logged in")

        self.browserAction.clickAndWait(self.homepage.getDeleteAccountButtonWE())

        actualText = self.browserAction.getText(self.deleteAccountPage.getPageTitleWE()).lower()
        expectedText = self.deleteAccountPage.getPageTitle().lower()
        if expectedText in actualText:
            print("Page title match")
        else:
            print("No such Page title present")
        time.sleep(5)
        self.browserAction.clickAndWait(self.deleteAccountPage.getContinueButtonWE())

        if self.browserAction.isPresent(self.homepage.getSignUpButtonWE()):
            print("Account successfully Deleted")

        pass