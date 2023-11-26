import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

###########          find_element()-----

## 1- Locator matiching with single web element
'''element = driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
element.send_keys("Apple MacBook Pro 12-inch")
'''
## 2- Locator matching with multiple web elements
'''element = driver.find_element(By.XPATH,"//div[@class='footer']//a")
print(element.text)     # prints 1st link from the footer "sitemap"
'''
### 3- Element not available ,then throw 'NosuchelementException'
'''login_element = driver.find_element(By.LINK_TEXT,"Log")
login_element.click()
'''

##############        Find_eleements()--------

## 1- Locator matiching with single web element
# elements = driver.find_elements(By.XPATH,"//input[@id='small-searchterms']")
# print(len(elements))                  # 1
# elements[0].send_keys("Apple MacBook Pro 12-inch")

### 2- Locator matching with multiple web elements
elements = driver.find_elements(By.XPATH,"//div[@class='footer']//a")
print(len(elements))                    #23
# print(elements[0].text)                #Sitemap
#if we want to print all elements
for elem in elements:
    print(elem.text)

# 3- Elements not available its return zero
'''elements = driver.find_elements(By.LINK_TEXT,"Log")
print("elements returened:-",len(elements))    #0'''


time.sleep(5)
driver.quit()

