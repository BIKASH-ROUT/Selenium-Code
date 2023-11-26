from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://jqueryui.com/slider/#range")
driver.maximize_window()

#### find location of start and end location
min_slider = driver.find_element(By.XPATH,"//span[1]")
max_slider = driver.find_element(By.XPATH,"//span[1]")
print("Location of sliders Before moving:-")
print(min_slider.location)             #{'x': 1347, 'y': 192}
print(max_slider.location)             #{'x': 1347, 'y': 192}

act = ActionChains(driver)
act.drag_and_drop_by_offset(min_slider,100,0).perform()
act.drag_and_drop_by_offset(max_slider,-50,0).perform()

print("Location of sliders After moving:-")
print(min_slider.location)
print(max_slider.location)

#driver.quit()