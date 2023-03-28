from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path
from datetime import date
import time



class Test_Sauce:
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)

    def teardown_method(self):
        self.driver.quit()

    def test_login(self):
        self.waitForElementVisible((By.ID, 'login-button'))
        loginBtn = self.driver.find_element(By.ID, 'login-button')
        loginBtn.click()

        self.waitForElementVisible((By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3'))

        errorMessage = self.driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')

        self.driver.save_screenshot(f"{self.folderPath}/test-empty-login.png")

        assert errorMessage.text == "Epic sadface: Username is required"

    @pytest.mark.parametrize("username", ["42", "standard_user", "problem_user"])
    def test_password_login(self, username):

        self.waitForElementVisible((By.ID, 'user-name'))
        usernameInput = self.driver.find_element(By.ID, 'user-name')
        usernameInput.send_keys(username)

        self.waitForElementVisible((By.ID, 'login-button'))
        loginBtn = self.driver.find_element(By.ID, 'login-button')
        loginBtn.click()

        errorMessage = self.driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')

        self.driver.save_screenshot(f"{self.folderPath}/test-empty-password-{username}-login.png")

        assert errorMessage.text == 'Epic sadface: Password is required'

    def test_invalid_login(self):
        self.waitForElementVisible((By.ID, 'user-name'))

        usernameInput = self.driver.find_element(By.ID, 'user-name')
        passwordInput = self.driver.find_element(By.ID, 'password')
        loginBtn = self.driver.find_element(By.ID, 'login-button')

        actions = ActionChains(self.driver)
        actions.send_keys_to_element(usernameInput, 'locked_out_user')
        actions.send_keys_to_element(passwordInput, 'secret_sauce')
        actions.send_keys_to_element(loginBtn, Keys.ENTER)
        actions.perform()

        errorMessage = self.driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')

        self.driver.save_screenshot(f"{self.folderPath}/test-invalid-login.png")

        assert errorMessage.text == 'Epic sadface: Sorry, this user has been locked out.'

    

    def test_success_login(self):
        self.waitForElementVisible((By.ID, 'user-name'))

        usernameInput = self.driver.find_element(By.ID, 'user-name')
        passwordInput = self.driver.find_element(By.ID, 'password')
        loginBtn = self.driver.find_element(By.ID, 'login-button')

        actions = ActionChains(self.driver)
        actions.send_keys_to_element(usernameInput, 'standard_user')
        actions.send_keys_to_element(passwordInput, 'secret_sauce')
        actions.send_keys_to_element(loginBtn, Keys.ENTER)
        actions.perform()

        self.waitForElementVisible((By.CLASS_NAME, 'inventory_list'))
        products = self.driver.find_elements(By.CLASS_NAME, 'inventory_item')

        self.driver.save_screenshot(f"{self.folderPath}/test-succes-login.png")

        assert len(products) == 6

    @pytest.mark.parametrize("username, password", [("standard_user", "42"), ("locked_out_user", "42"), ("problem_user", "42"), ("standard_user", "sauce_secret")])
    def test_wrong_password(self, username, password):
        self.waitForElementVisible((By.ID, 'user-name'))

        usernameInput = self.driver.find_element(By.ID, 'user-name')
        passwordInput = self.driver.find_element(By.ID, 'password')
        loginBtn = self.driver.find_element(By.ID, 'login-button')

        actions = ActionChains(self.driver)
        actions.send_keys_to_element(usernameInput, username)
        actions.send_keys_to_element(passwordInput, password)
        actions.send_keys_to_element(loginBtn, Keys.ENTER)
        actions.perform()

        errorMessage = self.driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')

        self.driver.save_screenshot(f"{self.folderPath}/test-wrong-password-{username}-{password}-login.png")

        assert errorMessage.text == 'Epic sadface: Username and password do not match any user in this service'

    def test_add(self):
        self.waitForElementVisible((By.ID, 'user-name'))

        usernameInput = self.driver.find_element(By.ID, 'user-name')
        passwordInput = self.driver.find_element(By.ID, 'password')
        loginButon = self.driver.find_element(By.ID, 'login-button')

        
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(usernameInput, 'standard_user')
        actions.send_keys_to_element(passwordInput, 'secret_sauce')
        actions.send_keys_to_element(loginButon, Keys.ENTER)
        actions.perform()

        self.waitForElementVisible((By.CLASS_NAME, 'inventory_item'))

        liste = self.driver.find_elements(By.CLASS_NAME, 'inventory_item_name')

        liste2 = []
        for x in liste:
            name = x.text.replace(" ", "-").lower()
            liste2.append(name)

        

        items = self.driver.find_elements(By.CLASS_NAME, 'inventory_item')

        i = 0
        for it in items:
            self.waitForElementVisible((By.CLASS_NAME, 'btn_inventory'))
            addToCart = it.find_element(By.ID, f'add-to-cart-{liste2[i]}')
            addToCart.click()
            i += 1

        sshop = self.driver.find_element(By.ID, 'shopping_cart_container')

        self.driver.save_screenshot(f"{self.folderPath}/test-add.png")

        assert sshop.text == "6"

    def waitForElementVisible(self, locator, timeout=5):
        WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))
    def test_testabout(self): # about kısmına giriş yapma testi
        
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "react-burger-menu-btn")))
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "about_sidebar_link")))
        self.driver.find_element(By.ID, "about_sidebar_link").click()
        self.driver.save_screenshot(f"{self.folderPath}/test-About.png")
        
    def test_testLogout(self): # çıkış yapma testi
   
    
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "react-burger-menu-btn")))
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "logout_sidebar_link")))
        self.driver.find_element(By.ID, "logout_sidebar_link").click()
    
        self.driver.save_screenshot(f"{self.folderPath}/test-LogOut.png")
        
    def wait_for_window(self, timeout = 2):    #sayfanın aşagı kaydırılması
        time.sleep(round(timeout / 1000))
        wh_now = self.driver.window_handles
        wh_then = self.vars["window_handles"]
        if len(wh_now) > len(wh_then):
            return set(wh_now).difference(set(wh_then)).pop()
  
    def test_linkedin_page(self): #giriş yapıldıktan sonra sayfanın aşağı kaydırıldınğında çıkan linkedin butonuna tıklanıp açılan sayfanın ekran görüntüsünü almak
    
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
        self.driver.execute_script("window.scrollTo(0,500)")
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#page_wrapper > footer > ul > li.social_linkedin > a")))
        linkedin=self.driver.find_element(By.CSS_SELECTOR, "#page_wrapper > footer > ul > li.social_linkedin > a")
        
        linkedin.click()
        p = self.driver.current_window_handle
        parent = self.driver.window_handles[0]
        chld = self.driver.window_handles[1]
        self.driver.switch_to.window(chld)

        time.sleep(5)
        
        self.driver.save_screenshot(f"{self.folderPath}/test-linkedin-page-open.png")
        time.sleep(2)
        
        

