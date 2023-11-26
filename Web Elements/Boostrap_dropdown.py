
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

### Input Chrome driver
serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

### Put URL of APP Page
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

### Take xpath of Boostrap droupdown
driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']").click()

### Take the list elements
countrieslist = driver.find_elements(By.XPATH,"//ul[@id='select2-billing_country-results']/li")
print(len(countrieslist))

for Country in countrieslist:
    if Country.text=="Iran":
        Country.click()
        break
