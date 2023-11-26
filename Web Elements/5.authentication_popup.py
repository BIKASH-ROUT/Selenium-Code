# When some popup windowos having username and password ,this situation we use auth_popups

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://the_internet.herokuapp.com/basic_auth")
driver.maximize_window()

