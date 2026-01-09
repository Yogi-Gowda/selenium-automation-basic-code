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

#assert 'Gmail' in browser.title
'''elem = browser.find_element(By.TAG_NAME,"div")
#elem.send_keys("selenium")
#elem.send_keys(Keys.RETURN)
print(len(elem))'''
#time.sleep(5)
browser.close()
