#Model-S
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pathlib import Path
from datetime import date

S="Model S"
class TestTestmodels:
  def __init__(self,driver):
    self.driver = driver
    self.folderPath = str(date.today())
    Path(self.folderPath).mkdir(exist_ok=True)
    
  def test_testmodelS(self):
    
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, "#dx-nav-item--vehicles > .tds-site-nav-item-text").click()
    time.sleep(1)
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Model S")))
    self.driver.find_element(By.LINK_TEXT,S).click()
    time.sleep(1)
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".tcl-hero__subcopy-desktop")))
    Url=self.driver.current_url
    assert "https://www.tesla.com/tr_tr/models"==Url  #Url ile sayfa doğrulama
    time.sleep(2)
    self.driver.save_screenshot(f"{self.folderPath}/test-Model-S.png")
    time.sleep(1)
  
