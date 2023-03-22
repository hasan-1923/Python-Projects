from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import Keys
#IMDB sitesinden top 250 film arasından seçilen döngünün yapılması
service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.imdb.com/")
driver.maximize_window()
driver.find_element(By.ID,"imdbHeader-navDrawerOpen").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"#imdbHeader > div.ipc-page-content-container.ipc-page-content-container--center.navbar__inner > aside > div > div.drawer__panelContent > div > div:nth-child(1) > span > div > div > ul > a:nth-child(2) > span").click()
list_film = driver.find_elements(By.XPATH,"//table/tbody//tr//td[@class='titleColumn']")

for i in range(50): # filmler arasından ilk 50 tanesinin yazılması 
    print(list_film[i].text)

for i in list_film:    #yapım yılı 2010 olan filmleri bulup yazdırma 
    if i.text[-5:-1]=="2010":
        print(i.text)





time.sleep(1000)