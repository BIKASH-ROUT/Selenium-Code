from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\\Drivers\\chromedriver_win32\\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR,"input[value='radio1']").click()
driver.find_element(By.CSS_SELECTOR,"#name").send_keys("bikash")
driver.find_element(By.CSS_SELECTOR,".inputs").send_keys("P_key")
