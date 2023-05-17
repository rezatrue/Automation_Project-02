from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class SignupPage(BaseDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://automationexercise.com/signup"
        self.signupFormTitleXPath = "//div[@class='login-form']/h2"
        self.signupFormExpectedTitle = "Enter Account Information"
        self.genderInputXPath = "//input[@type='radio' and @value='{}']"
        self.passwordXPath = "//input[@id='password']"
        self.daysXPath = "//select[@id='days']"
        self.monthsXPath = "//select[@id='months']"
        self.yearsXPath = "//select[@id='years']"
        self.firstNameXPath = "//input[@id='first_name']"
        self.lastNameXPath = "//input[@id='last_name']"
        self.address1XPath = "//input[@id='address1']"
        self.countryXPath = "//select[@id='country']"
        self.stateXPath = "//input[@id='state']"
        self.cityXPath = "//input[@id='city']"
        self.zipcodeXPath = "//input[@id='zipcode']"
        self.phoneXPath = "//input[@id='mobile_number']"
        self.btnCreateAccountXPath = "//button[text()='Create Account']"
        self.footerXPath = "//footer[@id='footer']"
        pass

    def getPageUrl(self):
        return self.url

    def getSignUpFormTitleWE(self):
        return self.driver.find_element(By.XPATH, self.signupFormTitleXPath)

    def getSignupFormExpectedTitle(self):
        return self.signupFormExpectedTitle

    def getGenderInputWE(self, title):
        if (title.lower() == 'mrs') or (title.lower() == 'female') or (title.lower() == 'she'):
            input = 'Mrs'
        else:
            input = 'Mr'
        return self.driver.find_element(By.XPATH, self.genderInputXPath.format(input))

    def getPasswordWE(self):
        return self.driver.find_element(By.XPATH, self.passwordXPath)

    def getDaysWE(self):
        return self.driver.find_element(By.XPATH, self.daysXPath)

    def getMonthsWE(self):
        return self.driver.find_element(By.XPATH, self.monthsXPath)

    def getYearsWE(self):
        return self.driver.find_element(By.XPATH, self.yearsXPath)

    def getFirstNameWE(self):
        return self.driver.find_element(By.XPATH, self.firstNameXPath)

    def getLastNameWE(self):
        return self.driver.find_element(By.XPATH, self.lastNameXPath)

    def getAddress1WE(self):
        return self.driver.find_element(By.XPATH, self.address1XPath)

    def getCountryWE(self):
        return self.driver.find_element(By.XPATH, self.countryXPath)

    def getStateWE(self):
        return self.driver.find_element(By.XPATH, self.stateXPath)

    def getCityWE(self):
        return self.driver.find_element(By.XPATH, self.cityXPath)

    def getZipcodeWE(self):
        return self.driver.find_element(By.XPATH, self.zipcodeXPath)

    def getPhoneWE(self):
        return self.driver.find_element(By.XPATH, self.phoneXPath)

    def getBtnCreateAccountWE(self):
        return self.driver.find_element(By.XPATH, self.btnCreateAccountXPath)

    def getSignUpFormTitleText(self):
        return self.getText(self.getSignUpFormTitleWE())
        pass

    def getFooterWE(self):
        return self.driver.find_element(self.footerXPath)
        pass

    def fillupAccountInformationForm(self, title, password, date, month, year, firstname, lastname, address, country, statetx, city, ziptx, phone):
        self.clickOnWe(self.getGenderInputWE(title))
        self.inputText(self.getPasswordWE(), password)
        self.selectDropdownItem(self.getDaysWE(), date)
        self.selectDropdownItem(self.getMonthsWE(), month)
        self.selectDropdownItem(self.getYearsWE(), year)
        self.inputText(self.getFirstNameWE(), firstname)
        self.inputText(self.getLastNameWE(), lastname)
        self.inputText(self.getAddress1WE(), address)
        self.selectDropdownItem(self.getCountryWE(), country)
        self.inputText(self.getStateWE(), statetx)
        self.inputText(self.getCityWE(), city)
        self.waitForSecond(5)
        self.inputText(self.getZipcodeWE(), ziptx)
        self.inputText(self.getPhoneWE(), phone)
        self.waitForSecond(2)
        self.clickAndWait(self.getBtnCreateAccountWE())

        pass