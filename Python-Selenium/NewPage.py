import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.apple.com/tr/") #apple.com'un açılması
time.sleep(2)
driver.switch_to.new_window("tab") #yeni sekmenin açılması
time.sleep(2)
driver.get("https://www.tesla.com/tr_tr") #açılan yeni sekmede tesla.com'a gidilmesi
