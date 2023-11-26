from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

## Chrome driver
serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
### Url path of reqired page/applications
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

