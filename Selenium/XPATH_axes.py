
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
d = webdriver.Chrome(service=serv_obj)

d.get("https://money.rediff.com/gainers/bse/daily/group")
d.maximize_window()

# #self :- we take 'SPIC' element
# text_msg = d.find_element(By.XPATH,"//a[contains(text(),'SPIC')]/self::a").text
# print(text_msg)                   #op--SPIC

# #parent
# text_msg = d.find_element(By.XPATH,"//a[contains(text(),'SPIC')]/parent::td").text
# print(text_msg)                 # op--SPIC  -->bcz in html code the parent node have no attributes/value,so its same as self

# #child
# childs = d.find_elements(By.XPATH,"//a[contains(text(),'SPIC')]/ancestor::tr/child::td")
# print(len(childs))              #op--10

# #Ancestor
# text_msg = d.find_element(By.XPATH,"//a[contains(text(),'SPIC')]/ancestor::tr").text
# print(text_msg)               #op--SPIC B 53.05 60.90 + 14.80

# #Descendant
# des = d.find_elements(By.XPATH,"//a[contains(text(),'SPIC')]/ancestor::tr/descendant::*")
# print("Number of descendant nodes:-",len(des))          #op-- 14

# #Following
# fol = d.find_elements(By.XPATH,"//a[contains(text(),'SPIC')]/ancestor::tr/following::*")
# print("Number of following nodes:-",len(fol))              #op-- 13754

# #following-sibling
# fol_sib = d.find_elements(By.XPATH,"//a[contains(text(),'SPIC')]/ancestor::tr/following-sibling::*")
# print("Number of following nodes:-",len(fol_sib))           #op=1698

# #Preceding
# pre = d.find_elements(By.XPATH,"//a[contains(text(),'SPIC')]/ancestor::tr/preceding::*")
# print("Number of precedings nodes:-",len(pre))             #op--6376

#Preceding-sibling
pre_sib= d.find_elements(By.XPATH,"//a[contains(text(),'SPIC')]/ancestor::tr/preceding-sibling::*")
print("Number of precedings nodes:-",len(pre_sib))           #op-- 775

d.close()