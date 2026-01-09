from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
browser = webdriver.Firefox()
browser.get('https://www.pesuacademy.com/Academy/')
#text = browser.find_element(By.ID,value="login_button")

elem = browser.find_element(By.ID,"j_scriptusername")
elem.send_keys("yogeshkumar20369@gmail.com")

elem = browser.find_element(By.NAME,"j_password")
elem.send_keys("Yogigowda@4549")
elem.send_keys(Keys.RETURN)
time.sleep(5)
