## 1) Count number of rows & columns
## 2) Read specific row & column data
## 3) read all the rows 7 columns data
## 4) Read data based on condition (list books name whose other is mukesh)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# ## 1) Count number of rows & columns in the table
# no_of_rows = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
# no_of_columns = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th"))
# print(no_of_rows)        #7
# print(no_of_columns)      #4

# ## 2) Read specific row & column data
# data = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[5]/td[1]").text
# print(data)
#
# data = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[3]/td[3]").text
# print(data)

# ## 3) Read all row & columns data
# no_of_rows = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
# no_of_columns = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th"))
# print("Printing all the rows and columns data................")
# for r in range(2,no_of_rows+1):            #we not need tr1,bcz it is a header row,so we starts 2index
#     for c in range(1,no_of_columns+1):
#         data = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td["+str(c)+"]").text
#         print(data,end="                    ")
#     print()

## 4) Read data based on condition (list books name whose other is mukesh)
no_of_rows = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
no_of_columns = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th"))
for r in range(2,no_of_rows+1):
    authorName = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[2]").text
    if authorName == "Mukesh":
        BookName = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[1]").text
        price = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[4]").text
        print(BookName,"  ",authorName,"     ",price)

driver.close()