#### Chrome Browser---

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.foundit.in/seeker/registration")
driver.maximize_window()

### click on  chosecv web element
up = driver.find_element(By.XPATH,"//span[@class='browse-text']").click()

### select file location,using send_keys method



