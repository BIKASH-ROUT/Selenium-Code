from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()

act = ActionChains(driver)

### for Roam & Itali
source_elem = driver.find_element(By.ID,"box6")
target_elem = driver.find_element(By.ID,"box106")
act.drag_and_drop(source_elem,target_elem).perform()

### for washington & US
source_elem = driver.find_element(By.ID,"box3")
target_elem = driver.find_element(By.ID,"box103")
act.drag_and_drop(source_elem,target_elem).perform()