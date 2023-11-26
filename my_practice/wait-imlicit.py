#Implicit Wait

#An implicit wait tells WebDriver to poll the DOM for a certain amount of time when trying to find any element (or elements)
# not immediately available. The default setting is 0. Once set, the implicit wait is set for the life of the WebDriver

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

service_obj = Service("C:\\Drivers\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2)
result_prodcuts = driver.find_elements(By.XPATH,"//div[@class='products']/div")

count = len(result_prodcuts)
assert count > 0

#selenium chaining
for result in result_prodcuts:
    result.find_element(By.XPATH,"div/button").click()

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys('rahulshettyacademy')
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()

msg = driver.find_element(By.CLASS_NAME,"promoInfo").text
print(msg)

time.sleep(10)
driver.close()