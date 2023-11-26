import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import mysql.connector

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()

try:
    con = mysql.connector.connect(host="localhost",port=3306,user="root",password="Bikash1998",database="mydb")
    curs = con.cursor()
    curs.execute("select * from caldata")

    for row in curs:
        #Reading data from excel:
        princ = row[0]
        rateofint = row[1]
        per1 = row[2]
        per2 = row[3]
        freq = row[4]
        exp_matvalue = row[5]

        #passing data to applications
        driver.find_element(By.XPATH,"//input[@id='principal']").send_keys(princ)
        driver.find_element(By.XPATH,"//input[@id='interest']").send_keys(rateofint)
        driver.find_element(By.XPATH,"//input[@id='tenure']").send_keys(per1)
        period_drop=Select(driver.find_element(By.XPATH,"//select[@id='tenurePeriod']"))
        period_drop.select_by_visible_text(per2)
        freqency_drop = Select(driver.find_element(By.XPATH,"//select[@id='frequency']"))
        freqency_drop.select_by_visible_text(freq)
        driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[1]/img").click()
        act_matvalue = driver.find_element(By.XPATH,"//*[@id='resp_matval']/strong").text

        #validation
        if float(exp_matvalue)==float(act_matvalue):
            print("test pass")
        else:
            print("test fail")
        driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[2]/img").click()
        time.sleep(5)
    con.close()
except:
    print("Connection Failed......")
driver.quit()
