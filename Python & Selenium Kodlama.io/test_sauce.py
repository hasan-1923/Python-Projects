from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

class Test_sauce:
    def test_invalid_login(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        
        sleep(5)
        usernameinput=driver.find_element(By.ID,"user-name")
        passwordinput=driver.find_element(By.ID,"password")
        sleep(5)
        usernameinput.send_keys("42")
        passwordinput.send_keys("42")
       
        loginbtn=driver.find_element(By.ID,"login-button")
        sleep(2)
        loginbtn.click()
        errormessage=driver.find_element(By.XPATH,"//div[@class='error-message-container error']/h3")
        testResault=errormessage.text=="Epic sadface: Username and password do not match any user in this service"
        print(f"TEST SONUCU: {testResault}")
        

testClass=Test_sauce()
testClass.test_invalid_login()
while True:
    continue