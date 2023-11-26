import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

time.sleep(3)
Computers = driver.find_element(By.XPATH,"//ul[@class='top-menu notmobile']//a[normalize-space()='Computers']")
Desktops = driver.find_element(By.XPATH,"//ul[@class='top-menu notmobile']//a[normalize-space()='Desktops']")
Notebooks = driver.find_element(By.XPATH,"//ul[@class='top-menu notmobile']//a[normalize-space()='Notebooks']")
Software = driver.find_element(By.XPATH,"//ul[@class='top-menu notmobile']//a[normalize-space()='Software']")

act = ActionChains(driver)
# ##1---- For click action in Desktops
# act.move_to_element(Computers).move_to_element(Desktops).click().perform()

# ##2----- for click action on Notebooks
# act.move_to_element(Computers).move_to_element(Desktops).move_to_element(Notebooks).click().perform()

##3---- for click action on the Software
act.move_to_element(Computers).move_to_element(Desktops).move_to_element(Notebooks).move_to_element(Software).click().perform()

