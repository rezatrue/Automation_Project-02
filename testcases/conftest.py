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
    request.cls.driver = driver
    yield
    driver.close()
