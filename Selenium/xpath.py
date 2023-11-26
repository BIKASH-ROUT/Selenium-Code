from selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
d = webdriver.Chrome(service=serv_obj)

d.get("http://automationpractice.com/index.php")
d.maximize_window()

## Absolute xpath for search bar and search button
# d.find_element(By.XPATH,"/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/input[4]").send_keys("T-shirts")
# d.find_element(By.XPATH,"/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/button").click()

# # Relative xpath for search bar and search button
# d.find_element(By.XPATH,'//*[@id="search_query_top"]').send_keys("T-Shirts")
# d.find_element(By.XPATH,"//*[@id='searchbox']/button").click()

# #OR-if one attributes bring exact value its run
# d.find_element(By.XPATH,"//input[id='search_query_top' or @name='search_query']").send_keys("T-Shirts")
# d.find_element(By.XPATH,"//button[@type='submit' or name='submit_search'] ").click()

# #AND--It need both attributes and values are exact other wise its error
# d.find_element(By.XPATH,"//input[@id='search_query_top' and @name='search_query']").send_keys("T-Shirts")
# d.find_element(By.XPATH,"//*[@type='submit' and @name='submit_search']").click()

# # contains()--Contains takes one attribute and a substring value of that attribute's,thar value at any position
# d.find_element(By.XPATH,"//input[contains(@class,'_query')]").send_keys("T-shits")
# d.find_element(By.XPATH,"//button[contains(@name,'submit')]").click()

# # starts-with()--its take one attributes and its starting substing value
# d.find_element(By.XPATH,"//input[starts-with(@class,'search_query')]").send_keys("T-Shits")
# d.find_element(By.XPATH,"//button[starts-with(@name,'submit')]").click()

# text()--Its take only value of inner text which not in quote
d.find_element(By.XPATH,"//a[text()='Women']").click()


