import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\\Drivers\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

# Locators- ID,NAME,CLASS NAME,TAG NAME,Link text
'''driver.find_element(By.NAME,"name").send_keys("Bikash Rout")
driver.find_element(By.NAME,"email").send_keys("routbikash842@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("Bikash@1998")
driver.find_element(By.ID,"exampleCheck1").click()'''

#CSS_SELECTORS
'''driver.find_element(By.CSS_SELECTOR,".form-control").send_keys("XYZ")        
driver.find_element(By.CSS_SELECTOR,"[name='email']").send_keys("xyz@gmail.com")
driver.find_element(By.CSS_SELECTOR,"#exampleInputPassword1").send_keys(12345678)'''

# XPATH
#1 Absolute xpath
'''driver.find_element(By.XPATH,"/html/body/app-root/form-comp/div/form/div[1]/input").send_keys("xyz")
driver.find_element(By.XPATH,"/html/body/app-root/form-comp/div/form/div[2]/input").send_keys("xyz@gmail.com")'''
#2 Relative xpath
'''driver.find_element(By.XPATH,"//input[@minlength=2]").send_keys("abc")
driver.find_element(By.XPATH,"//*[@name='email']").send_keys("abc@gmail.com")'''





