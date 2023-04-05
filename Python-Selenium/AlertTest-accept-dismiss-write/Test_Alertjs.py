import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert



from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


from pathlib import Path
from datetime import date
folderPath = str(date.today())
Path(folderPath).mkdir(exist_ok=True)



class Test_Alert:
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())   
        self.driver.maximize_window()
        self.driver.get("https://the-internet.herokuapp.com/javascript_alerts")  
        
        

    def teardown_method(self):
        self.driver.quit()
    def waitForElementVisible(self, locator, timeout=5): 
        WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))
    
    def testAccept(self):
        self.driver.find_element(By.XPATH,"(//button)[2]").click() #
        
        WebDriverWait(self.driver,3).until(ec.alert_is_present()) # alert çıkana kadar kodun bekleme işlemi
        Uyari=Alert(self.driver) 
        Uyari.accept() #alert üzerinde tamam (ok) basma
        self.driver.save_screenshot(f"{folderPath}/test-accept.png") #ekran görüntüsü tamam
    def testdismiss(self):
        self.driver.find_element(By.XPATH,"(//button)[2]").click() #
        
        WebDriverWait(self.driver,3).until(ec.alert_is_present()) # alert çıkana kadar kodun bekleme işlemi
        Uyari=Alert(self.driver) 
        Uyari.dismiss() # alert üzerinde iptal (cancel) basma
        self.driver.save_screenshot(f"{folderPath}/test-dismiss.png") #ekran görüntüsü iptal
    def testwrite(self):
        self.driver.find_element(By.XPATH,"(//button)[3]").click() # button 3 click
        
        WebDriverWait(self.driver,3).until(ec.alert_is_present()) # alert çıkana kadar kodun bekleme işlemi
        Uyari=Alert(self.driver)
        time.sleep(1) # 1 saniyelik bekleme
        message = Alert.text # alert içeriği 
        Uyari.send_keys("Test-accept-dismiss-write") # alert metin girme
        Uyari.accept() #alert üzerinde tamam (ok) basma
        self.driver.save_screenshot(f"{folderPath}/test-write.png") # metin girildikten sonra tamam (ok) basıp ekran görüntüsü alma

        
        
       
