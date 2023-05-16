from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

class BaseDriver:

    def __init__(self, driver):
        self.driver = driver
        pass

    def openUrlAndCheck(self, url, we):
        self.driver.get(url)
        wait = WebDriverWait(self.driver, 10)
        try:
            wait.until(expected_conditions.visibility_of_element_located(we))
            return True
        except TimeoutException:
            return False
        pass

    def clickAndWait(self, sbwe, we):
        sbwe.click()
        wait = WebDriverWait(self.driver, 10)
        try:
            wait.until(expected_conditions.visibility_of_element_located(we))
            return True
        except TimeoutException:
            return False
        pass

    def inputText(self, we, text):
        we.send_keys(text)

    def getText(self, we):
        return we.text

    def clickOnWe(self, we):
        we.click()

    def selectDropdownItem(self, we, opt):
        ddelement = Select(we)
        ddelement.select_by_visible_text(opt)

    def scrollToElement(self, we):
        actions = ActionChains(self.driver)
        actions.move_to_element(we).perform()

