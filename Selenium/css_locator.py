import time

from selenium import webdriver
from  selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
d = webdriver.Chrome(service=serv_obj)
d.get("https://www.facebook.com/")
d.maximize_window()

# 1- tag & id---(# symbol use)
# d.find_element(By.CSS_SELECTOR,"input#email").send_keys(8598888278)

'''d.find_element(By.CSS_SELECTOR,"#email").send_keys(8598888278)
d.find_element(By.CSS_SELECTOR,"#pass").send_keys("Bikash1998")'''

# # 2- tag & class----(. symbol use)
# d.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys(8598888278)
'''d.find_element(By.CSS_SELECTOR,".inputtext").send_keys(8598888278)'''

# # 3- tag & attribute
# d.find_element(By.CSS_SELECTOR,"input[data-testid=royal_email]").send_keys(8598888278)
'''d.find_element(By.CSS_SELECTOR,"[type='text']").send_keys(8598888278)
d.find_element(By.CSS_SELECTOR,"[type='password']").send_keys("Bikash1998")'''

# 4- tag,class & attribute
# d.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys(8598888278)
# d.find_element(By.CSS_SELECTOR,"input.inputtext[type='password']").send_keys("Bikash1998")


time.sleep(5)
d.close()