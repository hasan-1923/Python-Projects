from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service=Service("chromedriver.exe")
driver =webdriver.Chrome(service=service)
driver.get("http://apple.com")
sayfa=driver.current_url
print("şuanki sayfa:"+sayfa)
time.sleep(3)
driver.get("https://www.instagram.com")
sayfa=driver.current_url
print("şuanki sayfa: "+sayfa)
time.sleep(10000)

