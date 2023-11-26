
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
location = os.getcwd()

####1--- Create Function for Chrome Broweser:
def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")

    preferences = {"download.default_directory":location}
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs",preferences)

    driver = webdriver.Chrome(service=serv_obj)
    return driver

def firefox_setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("C:\Drivers\geckodriver-v0.32.0-win-aarch64\geckodriver.exe")

    ops = webdriver.FirefoxOptions()
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk","application/msword")
    ops.set_preference("browser.download.manager.showWhenstarting",False)
    ops.set_preference("browser.download.folderList",2)  #0-desktop,1-download,2-directory
    ops.set_preference("browser.download.dir",location)

    driver=webdriver.Firefox(service=serv_obj, options=ops)
    return driver

driver=chrome_setup()

driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
driver.maximize_window()
driver.find_element(By.XPATH,"//tbody/tr[1]/td[5]/a[1]").click()
