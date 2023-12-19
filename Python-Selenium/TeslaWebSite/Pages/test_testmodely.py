#Model-Y 
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pathlib import Path
from datetime import date


class TestTestmodely:
  def __init__(self,driver):
    self.driver=driver
    self.folderPath = str(date.today())
    Path(self.folderPath).mkdir(exist_ok=True)
  def test_testmodelY(self):
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, "#dx-nav-item--vehicles > .tds-site-nav-item-text").click()
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#dx-nav-item--vehicles > .tds-site-nav-item-text")))
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".active .dx-mega-menu-product:nth-child(2) .tds-link:nth-child(1)")))
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".active .dx-mega-menu-product:nth-child(2) .tds-link:nth-child(1)").click()
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".tcl-hero__content-end")))
    Url=self.driver.current_url
    assert "https://www.tesla.com/tr_tr/modely"==Url   #Url ile sayfa doğrulama
    time.sleep(1)
    self.driver.save_screenshot(f"{self.folderPath}/test-Model-Y.png")

    
