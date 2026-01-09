from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.by import By
import time
browser=webdriver.Firefox()
browser.maximize_window()
time.sleep(1)
browser.fullscreen_window()
time.sleep(1)
browser.get('https://cu.digiicampus.com/home')
time.sleep(1)
browser.refresh()
time.sleep(1)
browser.get("http://google.com")
titel=browser.title
browser.back()
time.sleep(1)
browser.forward()
time.sleep(1)
browser.minimize_window()
time.sleep(1)
print("Current URL after refresh:", browser.current_url)
browser.close()