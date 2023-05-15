from selenium import webdriver
#pip install webdriver-manager
##selenium 3 & 4
from webdriver_manager.chrome import ChromeDriverManager
##selenium 4
from selenium.webdriver.chrome.service import Service as ChromeService

##pip install undetected-chromedriver
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
##pip install psutil
import psutil


class Base:

    def __init__(self):
        pass

    def getDriver(self):
        opts = webdriver.ChromeOptions()
        opts.add_argument("--start-maximized")
        # opts.add_argument(
        #     'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')

        # driver = webdriver.Chrome(executable_path="../browserDrivers/chromedriver_win_113/chromedriver.exe")
        # selenium 3
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=opts)
        # selenium 4
        # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # driver = webdriver.Chrome(options=opts)
        return driver


