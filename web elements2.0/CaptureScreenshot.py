from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

### Input Chrome driver
serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# ### 1---> Using complete path of a file
# driver.save_screenshot("C:\\Users\\routb\\PycharmProjects\\selenium\\web elements2.0\\homepage.png")
# ### 2---> Using Curent directory file
 driver.save_screenshot(os.getcwd()+"\\homepage.png")
# ### 3--->
# driver.get_screenshot_as_file(os.getcwd()+"\\homepage.png")

##4-->driver.get_screenshot_as_base64() & driver.get_screenshot_as_png()-->saves in binary format

driver.quit()