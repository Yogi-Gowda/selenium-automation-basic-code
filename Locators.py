from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webelement_highlighter import WebElementHighlighter
import time
browser=webdriver.Firefox()
browser.get("http://google.com")
w=WebElementHighlighter(browser)
#ID
'''elem=browser.find_element(By.ID,"APjFqb")
w.make_it_blink(elem)
time.sleep(10)
browser.close()
#Name
elem=browser.find_element(By.NAME,"q")
w.make_it_blink(elem)
time.sleep(10)
browser.close()
#Class
elem=browser.find_element(By.CLASS_NAME,"gLFyf")
w.make_it_blink(elem)
time.sleep(10)
browser.close()
#tag
elem=browser.find_element(By.TAG_NAME,"textarea")
w.make_it_blink(elem)
time.sleep(10)
browser.close()
#Xpath
elem=browser.find_element(By.XPATH,"//textarea[@id='APjFqb']")
w.make_it_blink(elem)
time.sleep(10)
browser.close()
#CSS Selectors
elem=browser.find_element(By.CSS_SELECTOR,"#APjFqb")
w.make_it_blink(elem)
time.sleep(10)
browser.close()
#link test
elem=browser.find_element(By.LINK_TEXT,"Gmail")
w.make_it_blink(elem)
time.sleep(10)
browser.close()'''
#partial link
elem=browser.find_element(By.PARTIAL_LINK_TEXT,"Gmail")
w.make_it_blink(elem)
time.sleep(10)
browser.close()