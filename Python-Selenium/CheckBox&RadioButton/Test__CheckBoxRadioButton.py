
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


from pathlib import Path
from datetime import date



class Test__CheckBoxRadioButton:
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://tomspizzeria.b4a.app/")
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)

    def teardown_method(self):
        self.driver.quit()
    def test_Secim(self):
        self.driver.save_screenshot(f"{self.folderPath}/pizza-login-page.png")
        
        orta_Boy=self.driver.find_element(By.XPATH,"(//input[@name='size'])[2]")
        mantar=self.driver.find_element(By.XPATH,"(//input[@name='topping'])[3]")
        misir=self.driver.find_element(By.XPATH,"(//input[@name='topping'])[4]")

        
        print(orta_Boy.is_selected())
        print(mantar.is_selected())
        print(misir.is_selected())
        orta_Boy.click()
        mantar.click()
        misir.click()
        print(f"{orta_Boy.is_selected()} Orta boy pizza seçildi.")
        print(f"{mantar.is_selected()} Mantar Eklendi.")
        print(f"{misir.is_selected()} Mısır Eklendi.")
        self.driver.save_screenshot(f"{self.folderPath}/test-pizza.png")


  