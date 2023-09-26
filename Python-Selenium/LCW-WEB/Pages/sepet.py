from selenium.webdriver.common.by import By
import time
sepett="cart-dropdown"
anasayfaya="main-header-logo"
class SepetPage:
    def __init__(self,driver):
        self.driver=driver
    def SepetClick(self):
        self.driver.find_elements(By.CLASS_NAME,sepett)[2].click() #sepet ikonuna tıklama
        sayfa=self.driver.current_url
        assert "sepetim" in sayfa
        
        time.sleep(5)
        self.driver.find_element(By.CLASS_NAME,anasayfaya).click() # anasayfa dönüş için tıklama
        sayfa=self.driver.current_url
        assert "https://www.lcwaikiki.com/tr-TR/TR" == sayfa

        time.sleep(3)
        
        