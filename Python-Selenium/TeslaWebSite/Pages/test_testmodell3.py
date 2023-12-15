#Model3 page open
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

model3="Öğren"

class TestTestmodell3:
  def __init__(self,driver):
                self.driver = driver
  def test_testmodell33(self):
    time.sleep(2)
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".tcl-homepage-hero__content:nth-child(1) > .tcl-homepage-hero__content-end")))
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, "#dx-nav-item--vehicles > .tds-site-nav-item-text").click()
    time.sleep(2)
    self.driver.find_element(By.LINK_TEXT, model3).click()
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".tcl-hero__content-end")))
    Url=self.driver.current_url
    assert "https://www.tesla.com/tr_tr/model3"==Url #Url ile sayfa doğrulama
    time.sleep(2)
  
