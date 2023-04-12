import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.apple.com/tr/") #apple.com'un açılması
time.sleep(3)

print(driver.title)
apple=driver.current_window_handle
time.sleep(2)
driver.switch_to.new_window("tab") #yeni sekmenin açılması
driver.get("https://www.tesla.com/tr_tr") #açılan yeni sekmede tesla.com'a gidilmesi
time.sleep(1)
print(driver.title)
tesla=driver.window_handles[1]
driver.switch_to.window(apple) # apple.com'a geçiş
time.sleep(1)
driver.switch_to.window(tesla) #tesla.com'a geçiiş

