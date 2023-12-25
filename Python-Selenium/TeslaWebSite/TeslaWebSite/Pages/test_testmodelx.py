#Model-X 
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pathlib import Path
from datetime import date

X="Model X"
class TestTestmodelx:
  def __init__(self,driver):
    self.driver=driver
    self.folderPath = str(date.today())
    Path(self.folderPath).mkdir(exist_ok=True)
  def test_testmodelX(self):
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, "#dx-nav-item--vehicles > .tds-site-nav-item-text").click()
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Model X")))
    time.sleep(1)
    self.driver.find_element(By.LINK_TEXT, X).click()
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".tcl-hero__content-end:nth-child(4)")))
    time.sleep(1)
    self.driver.save_screenshot(f"{self.folderPath}/test-Model-X.png")

  
