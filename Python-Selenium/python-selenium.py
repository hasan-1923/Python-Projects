from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import datetime
import time

service=Service("chromedriver.exe")
driver =webdriver.Chrome(service=service)
driver.get("http://apple.com")

time.sleep(10000)

