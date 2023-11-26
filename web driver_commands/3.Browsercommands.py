import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(5)

driver.find_element(By.LINK_TEXT,'OrangeHRM, Inc').click()
#close()--its close single browser at a time
# time.sleep(5)
# driver.close()
# time.sleep(3)

#quit()-- its close all browser at a time


time.sleep(5)
driver.quit()
