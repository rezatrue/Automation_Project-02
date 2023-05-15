from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

class BrowserAction:

    def __init__(self, driver):
        self.driver = driver
        pass

    def closeBrowser(self):
        self.driver.quit()
        print("Browser closed")
        pass

    def openUrl(self, url):
        self.driver.get(url)
        wait = WebDriverWait(self.driver, 10)

        try:
            wait.until(expected_conditions.visibility_of_element_located((By.TAG_NAME, "body")))
            print("Page is visible.")
            return True
        except TimeoutException:
            print("Page is not visible.")
            return False

    def clickAndWait(self, sbwe):
        sbwe.click()
        wait = WebDriverWait(self.driver, 10)

        try:
            wait.until(expected_conditions.visibility_of_element_located((By.TAG_NAME, "body")))
            print("Page is visible.")
            return True
        except TimeoutException:
            print("Page is not visible.")
            return False
        pass

    def inputText(self, we, text):
        we.send_keys(text)

    def getText(self, we):
        return we.text

    def selectDropdownItem(self, we, opt):
        ddelement = Select(we)
        ddelement.select_by_visible_text(opt)

    def isPresent(self, we):
        try:
            element = we
            if element is not None:
                print("Found in the page")
        except NoSuchElementException:
            print("Not in the current DOM")
            return False
        return True

    def switchToIframe(self, iframeXpath):
        # driver.switch_to.frame("ID")
        # driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, "iframe#upload_file_frame"))
        # driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='upload_file_frame']"))
        try:
            WebDriverWait(self.driver, 20).until(
                expected_conditions.frame_to_be_available_and_switch_to_it(self.driver.find_element(By.XPATH, self.inputXPath.get())))
        except:
            print("failed to switch to iframe: ")
            return False
        return True

    def switchBackFromIframe(self):
        self.driver.switchTo().defaultContent();
        pass

    def getCurrentUrl(self):
        return self.driver.current_url
        pass