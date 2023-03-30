from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys

from pathlib import Path
from datetime import date



class Test__PizzaOrder:
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://tomspizzeria.b4a.app/")
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)
        

    def teardown_method(self):
        self.driver.quit()
    def test_Secim(self):
        #self.driver.save_screenshot(f"{self.folderPath}/pizza-login-page.png")
        name=self.driver.find_element(By.ID,"musteri-adi")
        name.send_keys("HASAN")
        orta_Boy=self.driver.find_element(By.XPATH,"(//input[@name='size'])[2]")
        mantar=self.driver.find_element(By.XPATH,"(//input[@name='topping'])[3]")
        misir=self.driver.find_element(By.XPATH,"(//input[@name='topping'])[4]")

        
        print(orta_Boy.is_selected())
        print(mantar.is_selected())
        print(misir.is_selected())
        orta_Boy.click()
        mantar.click()
        misir.click()
        print(f"{orta_Boy.is_selected()} Orta boy pizza seçildi.")
        print(f"{mantar.is_selected()} Mantar Eklendi.")
        print(f"{misir.is_selected()} Mısır Eklendi.")
        #self.driver.save_screenshot(f"{self.folderPath}/test-pizza-icerik.png")
    
       

        down = self.driver.find_element(By.ID,"odeme-tipi") # static dropdown ile saçim yapma
        pay =Select(down) # ödeme tiplerini liste haline getirme 
        pay_type =pay.options
        #self.driver.save_screenshot(f"{self.folderPath}/test-pizza.png")
        time.sleep(2)
        #for typ in pay_type: # ödeme tiplerinin yazdırılması 
            #print(typ.text)
        time.sleep(2)    
        pay.select_by_visible_text("Kredi Kartı") 
        #pay.select_by_index(2) index ile seçim yapılması
        sipariş=self.driver.find_element(By.ID,"siparis").click()
        self.driver.execute_script("window.scrollTo(0,500)")
        time.sleep(2)
    

        self.driver.save_screenshot(f"{self.folderPath}/test-sipariş.png")
        
        
        