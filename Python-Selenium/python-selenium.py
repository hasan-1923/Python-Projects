from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service=Service("chromedriver.exe")
driver =webdriver.Chrome(service=service)
driver.get("http://apple.com")
sayfa=driver.current_url

if "apple.com" in  sayfa: 
    print("şuanki sayfa:"+ sayfa)

baslik=driver.title
print("sayfa başligi:" +baslik)
time.sleep(3)
driver.maximize_window()
driver.get("https://www.instagram.com")
sayfa=driver.current_url
baslik=driver.title
if "instagram.com" in sayfa:
    print("şuanki sayfa: "+sayfa)
print("sayfa basligi:"+baslik)
time.sleep(3)
driver.back()
baslik=driver.title
print("şuanki sayfa basligi:"+baslik)
time.sleep(10000)

