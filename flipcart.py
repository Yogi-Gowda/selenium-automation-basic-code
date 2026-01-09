from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
browser = webdriver.Firefox()
browser.get('https://www.flipkart.com/')
#text = browser.find_element(By.ID,value="login_button")

elem = browser.find_element(By.NAME,"q")
elem.send_keys("laptop")
elem.send_keys(Keys.RETURN)
time.sleep(5)