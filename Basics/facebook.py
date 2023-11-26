from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

service_obj = Service("C:\\Drivers\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.facebook.com/")

driver.find_element(By.ID,"email").send_keys("8598888278")
driver.find_element(By.ID,"pass").send_keys("Bikash1998")
driver.find_element(By.NAME,"login").click()

time.sleep(50)
driver.close()

