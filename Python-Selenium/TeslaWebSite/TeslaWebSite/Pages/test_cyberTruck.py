# Model CyberTruck
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from datetime import date
from pathlib import Path
import time


class TestCyberTruck:
  def __init__(self,driver):
    self.driver = driver
    self.folderPath = str(date.today())
    Path(self.folderPath).mkdir(exist_ok=True)
  def test_cyberTruck(self):
    time.sleep(1)
    #WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".tcl-homepage-hero__content:nth-child(1) > .tcl-homepage-hero__content-end")))

    self.driver.find_element(By.CSS_SELECTOR, "#dx-nav-item--vehicles > .tds-site-nav-item-text").click()
    time.sleep(1)

    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".active .dx-mega-menu-product:nth-child(3) .tds-link")))
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".active .dx-mega-menu-product:nth-child(3) .tds-link").click()
    time.sleep(1)
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".dx-hero-content svg")))
    time.sleep(1)
    Url=self.driver.current_url
    assert "https://www.tesla.com/tr_tr/cybertruck"==Url #Url ile sayfa doğrulama
    time.sleep(2)
    self.driver.save_screenshot(f"{self.folderPath}/test-Model-CyberTruck.png")

