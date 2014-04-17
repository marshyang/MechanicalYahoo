'''
Created on Dec 17, 2013

@author: Marshall Yang
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
#from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

import time

lines = [line.rstrip('\n') for line in open("C:\yahooLinks.txt")] 

chrome_options = Options()

chrome_options.add_argument("user-data-dir=C:\Users\AppData\Local\Google\Chrome\User Data")

driver = webdriver.Chrome(chrome_options=chrome_options) #('/path/to/chromedriver')  # Optional argument, if not specified will search path.

for companyLink in lines:
    if companyLink=="":
        print ";;"
    else:
        driver.get("http://finance.yahoo.com/q/ks?s="+companyLink+"+Key+Statistics")
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME,"title")))
        name = driver.find_element_by_class_name("title").text
        evr = driver.find_element_by_xpath("//table[@class='yfnc_datamodoutline1']/TBODY[1]/TR[1]/TD[1]/TABLE[1]/TBODY[1]/TR[8]/TD[2]")
        evebitda = driver.find_element_by_xpath("//table[@class='yfnc_datamodoutline1']/TBODY[1]/TR[1]/TD[1]/TABLE[1]/TBODY[1]/TR[9]/TD[2]")
        print name +";"+ evr.text+";"+ evebitda.text
driver.quit()
