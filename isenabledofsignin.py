from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
browser = webdriver.Firefox()
browser.get('https://training.openspan.com/login')
text = browser.find_element(By.ID,value="login_button").is_enabled()

elem = browser.find_element(By.ID,"user_name")
elem.send_keys("username")

elem = browser.find_element(By.NAME,"user_pass")
elem.send_keys("password")
print(text)

time.sleep(5)
