from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

serv_obj = Service("C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
####### 1- implicit_wait():----(time specifies)

'''driver.get("https://www.google.com/")
driver.maximize_window()
driver.implicitly_wait(10)

searchbox = driver.find_element(By.NAME,'q')
searchbox.send_keys('selenium')
searchbox.submit()                                 # for press enter key in keyboard we use submit()

driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()'''

######## 2- explicit_wait-----(condition specifies)

from selenium.webdriver.support import expected_conditions as EC

driver.get("https://www.google.com/")
driver.maximize_window()
# #1
'''mywait = WebDriverWait(driver,10)    #explicit wait declaration---its a basic syntax

searchbox = driver.find_element(By.NAME,'q')
searchbox.send_keys('selenium')
searchbox.submit()

searchlink = mywait.until(EC.presence_of_element_located((By.XPATH,"//h3[text()='Selenium']")))
searchlink.click()
'''
# 2
mywait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
                                                                         ElementNotVisibleException,
                                                                         ElementNotSelectableException,
                                                                         Exception])

searchbox = driver.find_element(By.NAME, 'q')
searchbox.send_keys('selenium')
searchbox.submit()

searchlink = mywait.until(EC.presence_of_element_located((By.XPATH, "//h3[text()='Seqdb lenium']")))
searchlink.click()

driver.quit()
