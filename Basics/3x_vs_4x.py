# using "ORANGE HRM" page
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service = serv_obj)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.CLASS_NAME,"oxd-input oxd-input--active").send_keys("admin123")
driver.find_element(By.CLASS_NAME,"oxd-button oxd-button--medium oxd-button--main orangehrm-login-button").click()
time.sleep(3)

driver.quit()