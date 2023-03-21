from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import Keys
class Test():
    
        

        
        service=Service("chromedriver.exe")
        driver =webdriver.Chrome(service=service)
        driver.get("https://the-internet.herokuapp.com/login")
        time.sleep(3)

         #kullanıcı adı ve şifre girilmesi 
         #yanlış username adi denemesi
        Username=driver.find_element(By.ID,"username")
        Password=driver.find_element(By.ID,"password")
        LoginButton=driver.find_element(By.CLASS_NAME,"radius")
        Username.send_keys("42")
        Password.send_keys("42")
        LoginButton.click()
        message=driver.find_element(By.ID,"flash").text
        if "Your username is invalid!" in message:
            print(f"yanliş kullanici adi doğru çalişiyor:{message}")
        else:
            print("yanliş kullanici adi çalişmiyor.") 


        #doğru username yanlış password  denemesi    

        driver.get("https://the-internet.herokuapp.com/login")
        Username=driver.find_element(By.ID,"username")
        Password=driver.find_element(By.ID,"password")
        LoginButton=driver.find_element(By.CLASS_NAME,"radius")
        Username.send_keys("tomsmith")
        Password.send_keys("42")
        LoginButton.click()
        message2=driver.find_element(By.ID,"flash").text
        if "Your password is invalid!" in message2:
             print(f"yanliş şifre doğru çalişiyor {message2}")
        else:
             print("yanliş şifre doğru çalişmiyor.")  


        driver.get("https://the-internet.herokuapp.com/login")
        Username=driver.find_element(By.ID,"username")
        Password=driver.find_element(By.ID,"password")
        LoginButton=driver.find_element(By.CLASS_NAME,"radius")
        Username.send_keys("tomsmith")
        Password.send_keys("SuperSecretPassword!")
        LoginButton.click()
        message3=driver.find_element(By.ID,"flash").text
        if "You logged into a secure area!" in message3:
            print(f"username ve password doğru çalişiyor: {message3}")
        else:
            print("doğru bilgiler düzgün çalişmiyor ")  
        link=driver.current_url
        if "secure"in link:
             
            print(f"link secure içeriyor giriş yapildi: {link}")
        else:
            print("hata link secure içermiyor.")  
        TrueMessage=driver.find_element(By.XPATH,"//*[@id='content']/div/h2").text
        time.sleep(2)
           
        if "Secure Area" in TrueMessage:
            print("Doğru giriş sayfa başligi doğru")
        else:
            print(TrueMessage) 
        exitButton=driver.find_element(By.XPATH,"//*[@id='content']/div/a")
        exitButton.click()
        link2=driver.current_url
        if "https://the-internet.herokuapp.com/login"==link2:
             print("çikiş yapildi.") 
                       


        time.sleep(1000)



Test().Login()
