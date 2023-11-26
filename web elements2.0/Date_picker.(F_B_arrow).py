from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

driver.switch_to.frame(0)         #1st switch to frame,bcz date box inside a frame element

# 1) using send_keys() directly give input date(1st check manuaaly the design of date format)
driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("06/27/1998")  # mm/dd/yyyy

# # 2)using logic
year = "2023"
month = "March"
Date = "30"

driver.find_element(By.XPATH,"//*[@id='datepicker']").click()            # open datepicker

while True:
    mm = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yy = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text

    if mm == month and yy == year:
        break
    else:
        ####for future dates
        driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-e']").click()
        ##### for past dates
        #driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-w']").click()

dates = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for elem in dates:
    if elem.text == Date:
        elem.click()
        break
