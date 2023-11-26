# open facebook page
'''import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.facebook.com/r.php?locale=en_GB&display=page")
driver.maximize_window()

print(driver.title)
print(driver.current_url)
time.sleep(5)

driver.close()'''

## Locators - ID,NAME,CLASS_NAME,LINK_TEXT
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.facebook.com/r.php?locale=en_GB&display=page")
driver.maximize_window()

driver.find_element(By.NAME,"firstname").send_keys("Bikash")
driver.find_element(By.NAME,"lastname").send_keys("Rout")
driver.find_element(By.NAME,"reg_email__").send_keys("routbikash842@gmail.com")
driver.find_element(By.NAME,"reg_email_confirmation__").send_keys("routbikash842@gmail.com")
driver.find_element(By.ID,"password_step_input").send_keys("Bikash@1998")
driver.find_element(By.ID,"day").send_keys(27)
driver.find_element(By.ID,"month").send_keys("Jun")
driver.find_element(By.ID,"year").send_keys(1998)
gender = driver.find_elements(By.CLASS_NAME,"_8esa")
print(len(gender))
gender[1].click()
driver.find_element(By.NAME,"websubmit").click()

time.sleep(5)
driver.close()
