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

    def clickAndWait(self, sbwe):
        sbwe.click()
        self.waitForSecond(3)
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
        # first move to the element
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", we)
        # then scroll by x, y values, in this case 10 pixels up
        self.driver.execute_script("window.scrollBy(0, -50);")

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

    def isPresent(self, xpath):
        try:
            element = self.driver.find_element(By.XPATH, xpath)
            if element is not None:
                print("Element present in the page")
        except NoSuchElementException:
            print("Not in the current DOM")
            return False
        return True

    def getCurrentUrl(self):
        return self.driver.current_url
        pass

    def hoverOn(self, we):
        actions = ActionChains(self.driver)
        actions.move_to_element(we).perform()
        pass