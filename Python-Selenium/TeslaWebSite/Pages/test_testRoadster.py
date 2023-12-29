# Model Roadster
import time
from datetime import date
from pathlib import Path
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestTestRoadster():
  def __init__(self,driver):
    self.driver = driver
    self.folderPath = str(date.today())
    Path(self.folderPath).mkdir(exist_ok=True)
  def test_testRoadsteR(self):
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, "#dx-nav-item--vehicles > .tds-site-nav-item-text").click()
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Roadster")))
    time.sleep(1)
    self.driver.find_element(By.LINK_TEXT, "Roadster").click()
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".tcl-hero__content-end")))
    time.sleep(1)
    Url=self.driver.current_url
    assert "https://www.tesla.com/tr_tr/roadster"==Url #Url ile sayfa doğrulama
    time.sleep(2)
    self.driver.save_screenshot(f"{self.folderPath}/test-Model-Roadster.png")
    time.sleep(1)

  
