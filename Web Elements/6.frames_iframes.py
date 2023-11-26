import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
driver.maximize_window()

# ### If we can pass only click action on a perticular frame with its locator,Its not perferm
# driver.find_element(By.LINK_TEXT,"org.openqa.selenium").click()
# driver.find_element(By.LINK_TEXT,"WebDriver").click()
# driver.find_element(By.XPATH,"/html/body/header/nav/div[1]/div[1]/ul/li[8]").click()

### So we can use switch_to.frame() command for go to a perticular page
### And also use switch_to.default_content() for go back to main page
driver.switch_to.frame("packageListFrame")
driver.find_element(By.LINK_TEXT,"org.openqa.selenium").click()
driver.switch_to.default_content()

driver.switch_to.frame("packageFrame")
driver.find_element(By.LINK_TEXT,"WebDriver").click()
driver.switch_to.default_content()

driver.switch_to.frame("classFrame")
driver.find_element(By.XPATH,"/html/body/header/nav/div[1]/div[1]/ul/li[8]").click()












add_str = lambda a,b:a+b
print(add_str('Hii','Mr X'))