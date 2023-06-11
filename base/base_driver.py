from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
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
        time.sleep(3)
        if self.isBottomAddVisible():
            self.closeBottomAdd()
        pass

    def clickOnStaleElement(self, we, max_attempts=3):
        attempt = 1
        while attempt <= max_attempts:
            try:
                we.click()
                time.sleep(3)
                return  # Successfully completed action
            except StaleElementReferenceException:
                print(f"StaleElementReferenceException occurred. Retrying ({attempt}/{max_attempts})...")
                attempt += 1
                wait = WebDriverWait(self.driver, 10)
                wait.until(expected_conditions.staleness_of(we))
        print("Max attempts reached. Action failed.")

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
        try:
            ddelement = Select(we)
            ddelement.select_by_visible_text(opt)
        except Exception as error:
            print(error)

    def scrollToElement(self, we):
        # first move to the element
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", we)

    def scrollToPixels(self, pixels):
        self.driver.execute_script("window.scrollBy(0, %s);" % pixels)
        # self.driver.execute_script(f"window.scrollBy(0, {pixels});")

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

    def switchToPopup(self):
        self.main_window = self.driver.current_window_handle
        # after opening popup, change window handle
        for handle in self.driver.window_handles:
            if handle != self.main_window:
                popup = handle
                self.driver.switch_to.window(popup)

    def switchBackToMain(self):
        self.driver.switch_to.window(self.main_window)

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

    def actionClickOn(self, we):
        try:
            actions = ActionChains(self.driver)
            actions.move_to_element(we)
            actions.click()
            actions.perform()
            # self.driver.execute_script("return arguments[0].click();", we)
            print("Successfully press action click")
        except:
            print("Unable to press action click")
        pass

    def isBottomAddVisible(self):
        wait = WebDriverWait(self.driver, 10)
        try:
            wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='grippy-host']")))
            return True
        except TimeoutException:
            return False

    def closeBottomAdd(self):
        self.waitForSecond(2)
        self.clickOnWe(self.driver.find_element(By.XPATH, "//div[@class='grippy-host']"))
        pass

    def isAddUrlPresent(self):
        self.waitForSecond(3)
        addUrl = "#google_vignette"
        currenturl = self.getCurrentUrl()
        if addUrl in currenturl:
            return True
        return False

    def isPresentWithScc(self, sccLoc):
        try:
            element = self.driver.find_element(By.CSS_SELECTOR, sccLoc)
            if element is not None:
                print("Element present in the page")
        except NoSuchElementException:
            print("Not in the current DOM")
            return False
        return True

    def closeUrlAdd(self):
        # tips:  can be navigate to url without "#google_vignette"
        visibelAddIframeXPath = "//iframe[contains(@id,'aswift_') and contains(@style,'visibility: visible')]"
        indentedIframeXPath = "//iframe[@id='ad_iframe']"
        addCloseButtonXPath = "//div[@id='dismiss-button']/div/span"
        addCloseIconCss = "#dismiss-button > div > svg > path:nth-child(1)"

        if self.isPresent(visibelAddIframeXPath):
            self.switchToIframe(visibelAddIframeXPath)
            if self.isPresentWithScc(addCloseIconCss):
                self.clickOnWe(self.driver.find_element(By.CSS_SELECTOR, addCloseIconCss))
            elif self.isPresent(indentedIframeXPath):
                self.switchToIframe(indentedIframeXPath)
                self.clickOnWe(self.driver.find_element(By.XPATH, addCloseButtonXPath))
            else:
                if self.isAddUrlPresent():
                    self.driver.get(self.getCurrentUrl().replace("#google_vignette", ""))
            self.switchBackFromIframe()
        pass

    def waitForItemLoad(self, xpath, sec):
        wait = WebDriverWait(self.driver, sec)
        try:
            wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpath)))
            return True
        except TimeoutException:
            return False
        pass

    def addHandeler(self):
        print("google_add: checking")
        if self.isAddUrlPresent():
            print("google_add: in the url")
            self.closeUrlAdd()
            self.waitForSecond(3)
        if self.isBottomAddVisible():
            print("google_add: at the bottom")
            self.closeBottomAdd()
            self.waitForSecond(3)
        print("goolge add resolved")
        pass
