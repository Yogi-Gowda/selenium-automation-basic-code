from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
browser = webdriver.Firefox()
browser.get('https://cu.digiicampus.com/home')
time.sleep(2)
browser.get('https://www.google.com/')
time.sleep(1)

browser.back()
time.sleep(2)

browser.forward()
time.sleep(2)
browser.close()
