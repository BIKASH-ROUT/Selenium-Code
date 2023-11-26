import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service("C:\\Drivers\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

#Select/Static Dropdown
'''dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Male")
time.sleep(5)
dropdown.select_by_index(1)'''



