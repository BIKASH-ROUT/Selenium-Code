import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

#put the url path of amazon,snapdeel
driver.get("https://www.amazon.in/")
driver.get("https://www.snapdeal.com/")

driver.back()            #amazon

time.sleep(5)
driver.forward()         #snapdeal

driver.refresh()

time.sleep(5)
driver.quit()