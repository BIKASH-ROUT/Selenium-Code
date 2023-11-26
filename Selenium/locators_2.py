#locators:2---
#CLASS NAME,TAG NAME--its use for multiple elements in a html code

from selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("http://automationpractice.com/index.php")
driver.maximize_window()

sliders=driver.find_elements(By.CLASS_NAME,"homeslider-container")
print(len(sliders))

# links=driver.find_elements(By.TAG_NAME,"a")
# print(len(links))
driver.close()
