from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time

class BaseDriver:

    def __init__(self, driver):
        self.driver = driver
        pass

    def closeBrowser(self):
        self.driver.quit()
        print("Browser closed")
        pass

    def openUrlAndCheck(self, url, tag):
        self.driver.get(url)
        wait = WebDriverWait(self.driver, 10)
        try:
            wait.until(expected_conditions.presence_of_element_located((By.TAG_NAME, tag)))
            return True
        except TimeoutException:
            return False
        pass

    def clickAndWait(self, sbwe, tag):
        sbwe.click()
        wait = WebDriverWait(self.driver, 10)
        try:
            wait.until(expected_conditions.visibility_of_element_located((By.TAG_NAME, tag)))
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

    def waitForSecond(self, sec):
        self.driver.implicitly_wait(sec)
        # time.sleep(sec)

    def selectDropdownItem(self, we, opt):
        ddelement = Select(we)
        ddelement.select_by_visible_text(opt)

    def scrollToElement(self, we):
        actions = ActionChains(self.driver)
        actions.move_to_element(we).perform()

    def switchToIframe(self, iframeXpath):
        # driver.switch_to.frame("ID")
        # driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, "iframe#upload_file_frame"))
        # driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='upload_file_frame']"))
        try:
            WebDriverWait(self.driver, 20).until(
                expected_conditions.frame_to_be_available_and_switch_to_it(iframeXpath))
        except:
            print("failed to switch to iframe: ")
            return False
        return True

    def switchBackFromIframe(self):
        self.driver.switch_to.default_content()
        pass

    def isPresent(self, we):
        try:
            element = we
            if element is not None:
                print("Element present in the page")
        except NoSuchElementException:
            print("Not in the current DOM")
            return False
        return True

    def getCurrentUrl(self):
        return self.driver.current_url
        pass