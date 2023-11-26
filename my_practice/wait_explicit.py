'''#####Explicit Wait
An explicit wait is a code you define to wait for a certain condition to occur before proceeding further in the code.
The extreme case of this is time.sleep(), which sets the condition to an exact time period to wait. There are some
convenience methods provided that help you write code that will wait only as long as required. Explicit waits are
achieved by using webdriverWait class in combination with expected_conditions'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C:\\ChromeDriver\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2)


result_prodcuts = driver.find_elements(By.XPATH,"//div[@class='products']/div")

count = len(result_prodcuts)
assert count > 0

#Selenium Changing
for result in result_prodcuts:
    result.find_element(By.XPATH,"div/button").click()

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys('rahulshettyacademy')
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()

#Explict Wait
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located(By.CSS_SELECTOR,"promoInfo"))

msg = driver.find_element(By.CLASS_NAME,"promoInfo").text
print(msg)