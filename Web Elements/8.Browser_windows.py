import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

# ###1. Find single page's windowid
# windowid = driver.current_window_handle
# print(windowid)  #CDwindow-E61660C2C320A3EEFF28034F45643740
#                  #CDwindow-67D9CB10427B78DF35B999AEAE1FC581   its changes in every sec

###2. Find multiple pages windowsid
time.sleep(3)               #give 3 sec bcz its take long time to findelement,
link = driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc")
link.click()
windowids = driver.window_handles

#######  Approach 1
parentwindowid = windowids[0]         ##CDwindow-08FBE8497C39D84A3D128F66C3D0C3A2
childwindowid = windowids[1]          ##CDwindow-A701B1EACA385CAA341CA4C04B19EFC1
print(parentwindowid,childwindowid)

# if driver switch to child window and print its title
driver.switch_to.window(childwindowid)
print(driver.title)
# if driver switch to parent window and print its title
driver.switch_to.window(parentwindowid)
print(driver.title)

######### Approach 2- use looping
# for winid in windowids:
#     driver.switch_to.window(winid)
#     print(driver.title)

####### close to perticular specific browser windows
time.sleep(3)
for winid in windowids:
    driver.switch_to.window(winid)
    if driver.title == "OrangeHRM":
        driver.close()





