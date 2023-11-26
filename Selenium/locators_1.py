#locators:1---(nopcommerce use url)
#ID,NAME,LINK TEXT,PARTIAL LINK TEXT these are used for one element which in html code page
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#
serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()      # maximize/full display the browser window

#  #  ID AND NAME:
# driver.find_element(By.ID,"small-searchterms").send_keys("Lenovo ThinkpadX1 Carbon Laptop")
#
# time.sleep(5)
# driver.close()

#driver.find_element(By.NAME,"q").send_keys("Lenovo ThinkpadX1 Carbon Laptop")

# LINK TEXT,PARTIAL LINK TEXT
# driver.find_element(By.LINK_TEXT,"Register").click()
# driver.find_element(By.PARTIAL_LINK_TEXT,"Regi").click()



