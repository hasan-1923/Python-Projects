from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service=Service("chromedriver.exe")
driver =webdriver.Chrome(service=service)
driver.get("http://apple.com") # apple.com açılması
sayfa=driver.current_url

if "apple.com" in  sayfa: 
    print("şuanki sayfa:"+ sayfa)

baslik=driver.title
print("sayfa başligi:" +baslik)
time.sleep(3)
driver.maximize_window()  #program pencereyi büyütür
driver.get("https://www.instagram.com") #instagram.com açılması
driver.save_screenshot("./instagram.png")
sayfa=driver.current_url
baslik=driver.title
if "instagram.com" in sayfa:
    print("şuanki sayfa: "+sayfa)
print("sayfa basligi:"+baslik)
time.sleep(3) # program 3 saniye uyur
driver.back()
baslik=driver.title
driver.save_screenshot("./apple.png") # ekran görüntüsü alır
if "Apple" in baslik:    
    print("Apple.com'a geri dönüldü")
time.sleep(10000)

