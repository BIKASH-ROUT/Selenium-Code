import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()

# # 1--select specific checkbox:
# driver.find_element(By.XPATH,"//input[@id='monday']").click()


## 2-- select all check boxes :
checkboxes = driver.find_elements(By.XPATH,"//*[@type='checkbox' and contains(@id,'day')]")
print(len(checkboxes))         #7

#approach1
# for i in range(len(checkboxes)):
#     checkboxes[i].click()

#approach2
# for i in checkboxes:
#     i.click()

# 3-- select multiple check boxes by choice
# for cbox in checkboxes:
#     dayname = cbox.get_attribute('id')
#     if dayname == 'monday' or dayname == 'sunday':
#         cbox.click()

## 4-- select last 2 checkboxs
# for i in range(len(checkboxes)-2,len(checkboxes)):     #range(5,7)=6,7
#     checkboxes[i].click()

## 5-- select 1st 2 checkboxes
# for i in range(len(checkboxes)):
#     if i<2:
#         checkboxes[i].click()

time.sleep(5)
## 6--clear all the checkboxes:

for i in checkboxes:
    i.click()                         #select all check boxes
time.sleep(5)
for i in checkboxes:
    if i.is_selected():
        i.click()                   #deselect all checkboxes


driver.quit()

