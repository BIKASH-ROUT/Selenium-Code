from selenium import webdriver
from selenium.webdriver.chrome.service import Service


serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

### 1) Capture Cookies from the browser
cookies = driver.get_cookies()
print("Size of Cookies:-",len(cookies))    #3

# ### 2)Print Details of all Cookies
# for c in cookies:
#     #print(c)
#     print(c.get("name"),"::",c.get("value"))

### 3)Add a new Cookie in the browser
driver.add_cookie({"name":"My cookie","value":"1234"})
cookies = driver.get_cookies()
print("Size of Cookies after add one :-",len(cookies))    #4

### 4) Delete a specific cookie from browser
driver.delete_cookie("My cookie")
cookies = driver.get_cookies()
print("Size of Cookies after deleted one :-",len(cookies))   #3

### 5) Delete all cookies
driver.delete_all_cookies()
cookies = driver.get_cookies()
print("Size of Cookies after delete all :-",len(cookies))    #0

driver.quit()