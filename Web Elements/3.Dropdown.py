from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from  selenium.webdriver.support.select import Select

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()

drpcountry = Select(driver.find_element(By.XPATH,"//select[@id='input-country']"))

## 1--select option from dropdown:
drpcountry.select_by_visible_text('India')
#drpcountry.select_by_value("10")
#drpcountry.select_by_index(13)

## 2-- capture all the options and print them:
# allops = drpcountry.options
# print(len(allops))
# for opt in allops:
#     print(opt.text)

##3 --select option from dropdown without built-in methods
# allops = drpcountry.options
# for opt in allops:
#     if opt.text == 'India':
#         opt.click()
#         break

#4--we can also use without Select(driver.method) ,if div,option,button tagname is child with select tag
alloptions = driver.find_elements(By.XPATH,"//*[@id='input-country']/option")
print(len(alloptions))
for i in alloptions:
    print(i.text)

driver.quit()