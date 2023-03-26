from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
sleep(2)
driver.get("https://www.google.com")
sleep(5)
input =driver.find_element(By.NAME,"q")
sleep(2)
input.send_keys("kodlamaio")
sleep(2)
searchButton=driver.find_element(By.NAME,"btnK")
sleep(3)
searchButton.click()
sleep(3)
firstResault=driver.find_element(By.XPATH,"//div[@class='g']//a/h3[1]")
sleep(2)
firstResault.click()
listofcourses=driver.find_elements(By.CLASS_NAME,"course-listing")
print(f"kodlamaio sitesinde şu anda {len(listofcourses)} tane kurs var.")
while True:
    continue