from selenium.webdriver.common.by import By
import time
aksesuar="AKSESUAR"
class Anasayfa:
    def __init__(self,driver):
        self.driver=driver
    def kategoryClick(self):
        self.driver.find_element(By.LINK_TEXT,aksesuar).click() #aksesuar kategorisine tıklama
        self.driver.execute_script("window.scrollTo(0,1400)")
        sayfa=self.driver.current_url # geçerli url alma
        assert "https://www.lcwaikiki.com/tr-TR/TR/lp/kadin-erkek-cocuk-bebek-aksesuar" == sayfa  # geçerli url ile istenen url kontrolü
        time.sleep(1)
        
        