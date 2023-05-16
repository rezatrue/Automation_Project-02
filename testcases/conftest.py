import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.accountCreatedPage import AccountCreatedPage
from browserAction import BrowserAction
from pages.deleteAccountPage import DeleteAccountPage
from pages.homepage import HomePage
from pages.loginPage import LoginPage
from pages.signupPage import SignupPage


@pytest.fixture(scope="class")
def setup(request):
    opts = webdriver.ChromeOptions()
    opts.add_argument("--start-maximized")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=opts)
    homepage = HomePage(driver)
    loginPage = LoginPage(driver)
    signupPage = SignupPage(driver)
    accountCreatedPage = AccountCreatedPage(driver)
    deleteAccountPage = DeleteAccountPage(driver)
    browserAction = BrowserAction(driver)
    request.cls.homepage = homepage
    request.cls.loginPage = loginPage
    request.cls.signupPage = signupPage
    request.cls.accountCreatedPage = accountCreatedPage
    request.cls.deleteAccountPage = deleteAccountPage
    request.cls.browserAction = browserAction
    yield
    driver.close()
