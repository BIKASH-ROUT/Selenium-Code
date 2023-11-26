# text--- Return inner text value
# get_attribute()-- return any values of any attributes of web element
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
driver.maximize_window()

# for email
emailbox = driver.find_element(By.XPATH,"//input[@id='Email']")
emailbox.clear()
emailbox.send_keys("xyz@gmail.com")
print("result of text:",emailbox.text)
print("result of get_attribute():",emailbox.get_attribute('value'))

# #for log in
button = driver.find_element(By.XPATH,"//button[normalize-space()='Log in']")
print("result of text:",button.text)
print("result of get_attribute():",button.get_attribute('class'))

time.sleep(5)
driver.quit()
