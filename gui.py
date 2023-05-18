import tkinter as tk
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException


class Gui:

    def __init__(self, base):
        self.base = base

        root = tk.Tk()
        root.title("Selenium Testing Kit")

        labelURL = tk.Label(root, text="URL/Text")
        labelURL.grid(row=0, column=0)
        self.inputText = tk.Entry(root, width=50)
        self.inputText.insert(0,"https://automationexercise.com/")
        self.inputText.grid(row=0, column=1)
        self.buttonNewBrowser = tk.Button(root, text="New Browser", state="normal", command=self.openNewBrowser)
        self.buttonNewBrowser.grid(row=0, column=3)

        self.buttonDefault = tk.Button(root, text="Open with Default Profile", state="normal", command=self.openProfileBrowser)
        self.buttonDefault.grid(row=1, column=3)

        labelXPath = tk.Label(root, text="XPath")
        labelXPath.grid(row=1, column=0)
        self.inputXPath = tk.Entry(root, width=50)
        self.inputXPath.grid(row=1, column=1)

        buttonClick = tk.Button(root, text="Click", command=self.myClick)
        buttonClick.grid(row=2, column=0)

        buttonInput = tk.Button(root, text="Input", command=self.myInput)
        buttonInput.grid(row=2, column=1)

        buttonIsPresent = tk.Button(root, text="Is E present", command=self.isPreasent)
        buttonIsPresent.grid(row=2, column=2)

        self.buttonClose = tk.Button(root, text="Close browser", state="disabled", command=self.closeBrowser)
        self.buttonClose.grid(row=2, column=3)

        buttonEnter = tk.Button(root, text="Press Enter", command=self.pressEnter)
        buttonEnter.grid(row=3, column=1)

        buttonGoBack = tk.Button(root, text="Go Back", command=self.goBack)
        buttonGoBack.grid(row=3, column=3)

        buttonWaitAndClick = tk.Button(root, text="Wait & Click", command=self.waitAndClick)
        buttonWaitAndClick.grid(row=4, column=0)

        buttonAlertDismiss = tk.Button(root, text="Alert Dismiss", command=self.alertDismiss)
        buttonAlertDismiss.grid(row=4, column=2)

        buttonSelect = tk.Button(root, text="Select", command=self.selectDropdownItem)
        buttonSelect.grid(row=5, column=1)

        buttonScroll = tk.Button(root, text="Scroll UpTo", command=self.scrollIntoElement)
        buttonScroll.grid(row=5, column=3)

        buttonGetText = tk.Button(root, text="Get Text", command=self.getElementText)
        buttonGetText.grid(row=6, column=0)

        buttonSwitchToIframe = tk.Button(root, text="Switch To Iframe", command=self.switchToIframe)
        buttonSwitchToIframe.grid(row=6, column=2)

        buttonBackFromIframe = tk.Button(root, text="Back From Iframe", command=self.backFromIframe)
        buttonBackFromIframe.grid(row=6, column=3)

        buttonTab = tk.Button(root, text="Press TAB", command=self.pressTab)
        buttonTab.grid(row=7, column=1)

        buttonActionClick = tk.Button(root, text="Action Click", command=self.actionClick)
        buttonActionClick.grid(row=7, column=4)

        root.mainloop()

    def myClick(self):
        print("Element: " + self.inputXPath.get())
        try:
            self.driver.find_element(By.XPATH, self.inputXPath.get()).click()
            print("Successfully to clicked")
        except:
            print("Unable to click")
        pass

    def pressEnter(self):
        print("Element: " + self.inputXPath.get())
        try:
            self.driver.find_element(By.XPATH, self.inputXPath.get()).send_keys(Keys.ENTER)
            print("Successfully press Entered")
        except:
            print("Unable to press Enter")
        pass

    def goBack(self):
        try:
            self.driver.back()
            print("Successfully Navigate back")
        except:
            print("Unable to gp back")
        pass

    def myInput(self):
        print(self.inputText.get() + "To: " + self.inputXPath.get())
        try:
            element = self.driver.find_element(By.XPATH, self.inputXPath.get())
            element.send_keys(self.inputText.get())
            print("Text inserted")
        except:
            print("Input Failed")
        pass


    def isPreasent(self):
        print("Element: " + self.inputXPath.get())
        try:
            element = self.driver.find_element(By.XPATH, self.inputXPath.get())
            if element is not None:
                print("Found in the page")
        except NoSuchElementException:
            print("Not in the current DOM")
            return False
        return True
        pass

    def waitAndClick(self):
        print("Element: " + self.inputXPath.get())
        try:
            wait = WebDriverWait(self.driver, 10)
            element = self.driver.find_element(By.XPATH, self.inputXPath.get())
            wait.until(expected_conditions.element_to_be_clickable(element))
            element.click()
            if element is not None: print("Element Clicked")
        except:
            print("Element is not found  in the page")
        pass

    def alertDismiss(self):
        print("Element: " + self.inputXPath.get())
        try:
            WebDriverWait(self.driver, 10).until(expected_conditions.alert_is_present(),
                                            'Timed out waiting for PA creation ' +
                                            'confirmation popup to appear.')
            alert = self.driver.switch_to.alert
            alert.dismiss()
            print("alert accepted")
        except TimeoutException:
            print("No alert present")
        pass

    def openNewBrowser(self):
        self.driver = self.base.getDriver()
        try:
            self.driver.get(self.inputText.get())
            if self.buttonNewBrowser.cget("state") == "normal":
                self.buttonNewBrowser.config(state="disabled")
            else:
                self.buttonNewBrowser.config(state="normal")
            if self.buttonDefault.cget("state") == "normal":
                self.buttonDefault.config(state="disabled")
            else:
                self.buttonDefault.config(state="normal")
            if self.buttonClose.cget("state") == "disabled":
                self.buttonClose.config(state="normal")
            else:
                self.buttonClose.config(state="normal")
        except:
            print("Failed to open new browser")
        print("openNewBrowser: " + self.inputText.get())
        
        pass

    def openProfileBrowser(self):
        self.driver = self.base.getProfieDriver()
        try:
            self.driver.get(self.inputText.get())
            if self.buttonNewBrowser.cget("state") == "normal":
                self.buttonNewBrowser.config(state="disabled")
            else:
                self.buttonNewBrowser.config(state="normal")
            if self.buttonDefault.cget("state") == "normal":
                self.buttonDefault.config(state="disabled")
            else:
                self.buttonDefault.config(state="normal")
            if self.buttonClose.cget("state") == "disabled":
                self.buttonClose.config(state="normal")
            else:
                self.buttonClose.config(state="normal")
        except:
            print("Failed to open new browser")
        print("openNewBrowser: " + self.inputText.get())
        pass

    def closeBrowser(self):
        try:
            self.driver.quit()
            if self.buttonNewBrowser.cget("state") == "disabled":
                self.buttonNewBrowser.config(state="normal")
            else:
                self.buttonNewBrowser.config(state="disabled")
            if self.buttonDefault.cget("state") == "disabled":
                self.buttonDefault.config(state="normal")
            else:
                self.buttonDefault.config(state="disabled")
            if self.buttonClose.cget("state") == "normal":
                self.buttonClose.config(state="disabled")
            else:
                self.buttonClose.config(state="disabled")
            print(" Browser Closed ")
        except:
            print("Unable to Close the Browser ")

    def selectDropdownItem(self):
        ddelement = Select(self.driver.find_element_by_xpath(self.inputXPath.get()))
        #Using the index of dropdown
        #ddelement.select_by_index(1)
        #Using the value of dropdown
        #ddelement.select_by_value('1')
        # Text displayed in the drop down
        ddelement.select_by_visible_text(self.inputText.get())

    def scrollIntoElement(self):
        element = self.driver.find_element_by_xpath(self.inputXPath.get())
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element).perform()
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def getElementText(self):
        etext = self.driver.find_element_by_xpath(self.inputXPath.get()).text
        print(etext)
        pass

    def switchToIframe(self):
        # driver.switch_to.frame("ID")
        # driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, "iframe#upload_file_frame"))
        # driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='upload_file_frame']"))

        WebDriverWait(self.driver, 20).until(
            expected_conditions.frame_to_be_available_and_switch_to_it(self.driver.find_element(By.XPATH, self.inputXPath.get())))
        pass

    def backFromIframe(self):
        self.driver.switch_to.default_content()

    def pressTab(self):
        try:
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.TAB)
            actions.perform()
            print("Successfully press Tab")
        except:
            print("Unable to press Tab")
        pass

    def actionClick(self):
        element = self.driver.find_element(By.XPATH, self.inputXPath.get())
        try:
            actions = ActionChains(self.driver)
            actions.move_to_element(element)
            actions.click()
            actions.perform()
            # self.driver.execute_script("arguments[0].click();", element)
            print("Successfully press action click")
        except:
            print("Unable to press action click")
        pass
