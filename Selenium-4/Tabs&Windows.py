from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

#1----->In all cases of selenium version:
# driver.get("https://demo.nopcommerce.com/")
# driver.maximize_window()
# ### Default action by automation,the new page also open in same tab
# driver.find_element(By.LINK_TEXT,"Register").click()

# ### The click action perform and open the page in a new tab
# reslnk = Keys.CONTROL+Keys.RETURN
# driver.find_element(By.LINK_TEXT,"Register").send_keys(reslnk)

#2------>in selenium-4:
# ### opens a new tab and switch to a new tab
# driver.get("https://www.opencart.com/")
# driver.switch_to.new_window("tab")
# driver.get("https://www.orangehrm.com/")

### opens a new window and switch to a new window
driver.get("https://www.opencart.com/")
driver.switch_to.new_window("window")
driver.get("https://www.orangehrm.com/")


