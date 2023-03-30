
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time 
from pathlib import Path
from datetime import date
folderPath = str(date.today())
Path(folderPath).mkdir(exist_ok=True)

service=Service("./chromedriver.exe")
driver=webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://tomspizzeria.b4a.app/")
down = driver.find_element(By.ID,"odeme-tipi") # static dropdown ile saçim yapma
pay =Select(down) # ödeme tiplerini liste haline getirme 
pay_type =pay.options
driver.save_screenshot(f"{folderPath}/test-pizza.png")
time.sleep(2)
for typ in pay_type: # ödeme tiplerinin yazdırılması 
    print(typ.text)
time.sleep(2)    
pay.select_by_visible_text("Kredi Kartı") 
#pay.select_by_index(2) index ile seçim yapılması 
driver.save_screenshot(f"{folderPath}/test-kredi-karti.png")
time.sleep(1000)