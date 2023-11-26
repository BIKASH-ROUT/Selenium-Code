import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service = serv_obj)
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
driver.maximize_window()

#is_displayed() & is_enabled--Its return True/False
searchbox = driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
print("display status:-",searchbox.is_displayed())      #True
print("Enable status:-",searchbox.is_enabled())         #True

# is_selected():- Its used for radiobutton/click box and return T/F
rd_male = driver.find_element(By.XPATH,"//input[@id='gender-male']")
rd_female = driver.find_element(By.XPATH,"//input[@id='gender-female']")

print("By deafult radio button status...")
print(rd_male.is_selected())                           #False
print(rd_female.is_selected())                         #False

rd_male.click()                                        #select male radio button
print("After selecting male radio button.....")
print(rd_male.is_selected())                          #True
print(rd_female.is_selected())                        #False

rd_female.click()
print("After selecting female radio button.....")
print(rd_male.is_selected())                          #False
print(rd_female.is_selected())                      #true

time.sleep(5)
driver.close()