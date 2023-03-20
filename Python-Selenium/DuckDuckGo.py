from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import Keys

service=Service("chromedriver.exe")
driver =webdriver.Chrome(service=service)
driver.get("https://duckduckgo.com/")
time.sleep(3)
searchForm=driver.find_element(By.ID,"search_form_input_homepage") #searchFrom bulma
searchForm.send_keys("selenium") # searchFrom'a selenium yazdırma 
time.sleep(2)
searchButton=driver.find_element(By.ID,"search_button_homepage")  #searchButton bulma
#searchButton.click()  
searchButton.send_keys(Keys.ENTER)  #tıklama
driver.find_element(By.CLASS_NAME,"Wo6ZAEmESLNUuWBkbMxx").click() #selenium.dev web sitesine giriş yapma








while True:
    continue