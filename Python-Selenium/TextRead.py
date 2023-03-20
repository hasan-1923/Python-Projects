from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service=Service("./chromedriver.exe")
driver=webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://tr.wikipedia.org/wiki/Anasayfa")
hatfaninSeckinMaddesi= driver.find_element(By.ID,"mp-tfa") #haftanın seckin maddesi yazı içeriginin  bulunması
haftaninSeckinMaddesitext=hatfaninSeckinMaddesi.text
haftaninSeckinMaddesitext=haftaninSeckinMaddesitext.split(",")[0] #haftanın seckin maddesinin ","e göre ayrılıp [0]'ın print edilmesi
print(f"haftanin seckin maddesi:{haftaninSeckinMaddesitext}")
GününKaliteliMaddesi=driver.find_element(By.ID,"mf-tfp").text #günün kaliteli maddesini yazı içeririginin bulunması
GününKaliteliMaddesi=GününKaliteliMaddesi.split(",")[0] #günün kaliteli maddesinin yazı içeriginin ","e göre ayrılıp [0]'ın print edilmesi
print(f"günün kaliteli maddesi:{GününKaliteliMaddesi}")









while True:
    continue
