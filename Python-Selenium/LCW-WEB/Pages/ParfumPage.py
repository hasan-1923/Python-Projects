from selenium.webdriver.common.by import By
import time
Parfümvekişiselbakim="//*[@id='content-layout']/div/div[1]/article[2]/div[2]/a/img"
ÜrünTiklama="//*[@id='root']/div/div[2]/div[2]/div[5]/div/div[2]/div[1]/a/div[1]/img"
sepeteEkle="pd_add_to_cart"

class parfumepage:
        def __init__(self,driver):
                self.driver = driver
                
        def parfumeclick(self):

                self.driver.execute_script("window.scrollTo(0,1400)")
                time.sleep(4)
                self.driver.find_element(By.XPATH,Parfümvekişiselbakim).click()#parfümler ve kişisel bakım ürünleri seçimi
                sayfa=self.driver.current_url
                assert "https://www.lcwaikiki.com/tr-TR/TR/etiket/yeni-sezon-kisisel-bakim-ve-parfum" ==sayfa
                self.driver.execute_script("window.scrollTo(0,300)")
                time.sleep(3)
                self.driver.find_element(By.XPATH,ÜrünTiklama).click()#parfüm sayfasında ilk ürüne tıklama
                sayfa=self.driver.current_url
                assert "https://www.lcwaikiki.com/tr-TR/TR/urun/LC-WAIKIKI/erkek/Parfum/6467145/3111843" ==sayfa
                time.sleep(2)
                self.driver.find_element(By.ID,sepeteEkle).click()#ürünün sepete eklenmesi işlemi
                time.sleep(3)
                
                
               