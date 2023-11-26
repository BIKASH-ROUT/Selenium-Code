import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import XLUtils
opts = webdriver.ChromeOptions()
opts.add_argument("--disable-notifications")
serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj,options=opts)
driver.implicitly_wait(10)


driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()

file = "C:\\Users\\routb\\OneDrive\\Documents\\FD_Cal.data.xlsx"
rows = XLUtils.getRowCount(file,"Sheet1")

for r in range(2,rows+1):
    #Reading data from excel:
    princ = XLUtils.readData(file,"Sheet1",r,1)
    rateofint = XLUtils.readData(file,"Sheet1",r,2)
    per1 = XLUtils.readData(file,"Sheet1",r,3)
    per2 = XLUtils.readData(file,"Sheet1",r,4)
    freq = XLUtils.readData(file,"Sheet1",r,5)
    exp_matvalue = XLUtils.readData(file,"Sheet1",r,6)

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
        XLUtils.writeData(file,"Sheet1",r,8,"passed")
        XLUtils.fillGreenColor(file,"Sheet1",r,8)
    else:
        print("test fail")
        XLUtils.writeData(file, "Sheet1", r, 8, "faild")
        XLUtils.fillRedColor(file, "Sheet1", r, 8)

    driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[2]/img").click()
    time.sleep(5)

driver.quit()


