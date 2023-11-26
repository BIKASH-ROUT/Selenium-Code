from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://text-compare.com/")
driver.maximize_window()

input1 = driver.find_element(By.XPATH,"//textarea[@id='inputText1']")
input2 = driver.find_element(By.XPATH,"//textarea[@id='inputText2']")
input1.send_keys("Welcome to Selenium")

act = ActionChains(driver)
### 1) Ctrl+a ---> select all text
# act.key_down(Keys.CONTROL)
# act.send_keys("a")
# act.key_up(Keys.CONTROL)
# act.perform()

act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

### 2) Ctrl+c ---> copy the select text
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

### 3) Tab ---> press tab key to shift one text box to another
act.send_keys(Keys.TAB).perform()

### 4) ctrl+v ---> paste the copy value in input2 box
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()