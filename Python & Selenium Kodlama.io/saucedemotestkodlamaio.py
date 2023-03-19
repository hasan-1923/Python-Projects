from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

class Test_sauce:
    def test_invalid_login(self,username,password,mistaketext):# username , password ve hatatext parametrelerini alıp kodu test eder.
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        
        sleep(5)
        usernameinput = driver.find_element(By.ID,"user-name") #username alanı bulma
        passwordinput = driver.find_element(By.ID,"password")  #password alanı bulma
        sleep(5)
        usernameinput.send_keys(username) #username alanına username parametresini girme
        passwordinput.send_keys(password) #password alanına password parametresini girme
       
        loginbtn=driver.find_element(By.ID,"login-button") #login butonunu  bulma  işlemi 
        sleep(2)
        loginbtn.click() #login butonuna tıklama işlemi
        errormessage = driver.find_element(By.XPATH,"//div[@class='error-message-container error']/h3")
        testResult = errormessage.text==mistaketext #hata mesajının hatatext ile aynı olup olmadıgını karşılaştırma işlemi
        print(f"TEST SONUCU: {testResult}  {errormessage.text}") # ekrana hata mesajını ve  sonucunu yazdırma  
        
        sleep(1000)
    def enter(self,username,password):  # username ve password parametrelerini alıp kodu test eder
             
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        
        sleep(5)
        usernameinput = driver.find_element(By.ID,"user-name") #username alanı bulma
        passwordinput = driver.find_element(By.ID,"password")  #password alanı bulma
        sleep(5)
        usernameinput.send_keys(username) #username alanına username parametresini girme
        passwordinput.send_keys(password) #password alanına password parametresini girme
       
        loginbtn = driver.find_element(By.ID,"login-button")  #login butonunu  bulma  işlemi
          
        sleep(2)
        loginbtn.click()  #login butonuna tıklama işlemi
        sayfa =driver.current_url
        if "https://www.saucedemo.com/inventory.html" in sayfa: # sayfadaki url ile verilen url aynı ise ekrana url yazdırma
            print(f" Şuan bu sayfadasiniz: {sayfa}")
        sleep(3)
        items = driver.find_elements(By.CLASS_NAME,"inventory_item") #login başarılı ise invertory sayfasında kullanıcıya gösterilen ürünlerin bulunması
        print(f"kullaniciya gösterilen ürün sayisi {len(items)} adet ") #kullanıcıya gösterilen ürün sayısını ekrana yazdırma

testClass=Test_sauce()
testClass.test_invalid_login("standard_user","secret_sauce","")
testClass.enter("standard_user","secret_sauce")
while True:
    continue



