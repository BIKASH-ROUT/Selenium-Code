from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# chrome driver path
serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

# web browser url path for open
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

# click action which element we needed
driver.find_element(By.XPATH,"//a[normalize-space()='Iframe with in an Iframe']").click()

# inspect outer frame ,and switch on it
outerframe = driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outerframe)

# inspect inner frame, and swith on it which frame is inside the outer frame
innerframe = driver.find_element(By.XPATH,"/html/body/section/div/div/iframe")
driver.switch_to.frame(innerframe)

#inspect on the textbox and enter welcome onit
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("welcome")

# in selenium4 switch_to.parent_frame() can switch from inner to outer frame,which is not possible in selenium3
#driver.switch_to.parent_frame()             #directly switch to parent frame(outer frame