import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

## 1-- Open alert window:
#driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']").click()
driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
time.sleep(5)

# #2-- Shift / goto alert window:
alertwindow = driver.switch_to.alert
print(alertwindow.text)

# alertwindow.send_keys('welcome')
# #alertwindow.accept()                  # close alert window by using Ok button
# alertwindow.dismiss()                  # close alert window by using cancle button