from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://jqueryui.com/slider/")
driver.maximize_window()

start_loc = driver.find_element(By.XPATH,"//span[@class='ui-slider-handle ui-corner-all ui-state-default']")
print(start_loc.location)

act = ActionChains(driver)
act.drag_and_drop_by_offset(start_loc,100,0).perform()
print(start_loc.location)

driver.quit()