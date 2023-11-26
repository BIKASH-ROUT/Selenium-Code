#1--shaw how we automated use any website,youtube etc
'''from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.youtube.com/watch?v=TlTzth6bYZI&list=RDTlTzth6bYZI&start_radio=1")
driver.maximize_window()
print(driver.title)
print(driver.current_url)'''

#2--my naukri account automated test
'''from selenium import webdriver
driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.naukri.com/mnjuser/homepage")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
'''

#3.1--
from selenium import webdriver
driver = webdriver.Chrome("C:\\Drivers\\chromedriver_win32\\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
print(driver.title)
print(driver.current_url)


#s3 and s4 versions are some upgade so when we run code its run successfully but having some exception/warning.

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="C:\\Users\\routb\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.ID,value="name").send_keys("Bikash rout")
driver.find_element(by=By.ID,value="alertbtn").click()

#driver.find_element(by=By.NAME,value="enter-name").send_keys("Bikash")

#driver.find_element(by=By.CLASS_NAME,value="inputs").send_keys("biki")

#driver.find_element(by=By.LINK_TEXT,value="Free Access to InterviewQues/ResumeAssistance/Material").click()
#
# a=driver.find_element(by=By.ID,value="openwindow").text
# print(a)


