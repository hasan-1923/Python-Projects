from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert



from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec






class Test_Alert:
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())   
        self.driver.maximize_window()
        self.driver.get("https://pynishant.github.io/Selenium-python-waits.html")  # pynishant.github.io web sitesine gidip alert kapatma 
        
        

    def teardown_method(self):
        self.driver.quit()
    def waitForElementVisible(self, locator, timeout=5): # locator ile ilgili element belirene kadar kodun beklenmesi fonksiyonu
        WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))
    
    def testAlert(self):
        self.driver.find_element(By.XPATH,"/html/body/button").click() # Try it butonunun bulunması ve butona  tıklanma işlemi 
        self.waitForElementVisible((By.XPATH, "//*[@id='waitCreate']")) # Click Me butonu sayfada belirene kadar beklenme işlemi 
        self.driver.find_element(By.XPATH,"//*[@id='waitCreate']").click() # Click Me butonunun bulunması ve tıklanması işlemi 
        WebDriverWait(self.driver,3).until(ec.alert_is_present()) # alert çıkana kadar kodun bekleme işlemi
        Uyari=Alert(self.driver) # uyarının selenium ile görünür yapılması 
        Uyari.accept()    #alert ile işlem (tıklama)

