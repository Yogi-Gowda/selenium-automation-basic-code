from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
browser = webdriver.Firefox()
browser.get('https://www.google.com/')
#title = browser.title
#print(title)
#assert 'Gmail' in browser.title
elem = browser.find_element(By.NAME,"textarea")
elem.send_keys("yogeshk.bca22@chanakyauniversity.edu.in")

elem.send_keys(Keys.RETURN)
time.sleep(50)
browser.close()
