from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webelement_highlighter import WebElementHighlighter
import time
browser=webdriver.Firefox()
browser.get("http://google.com")
w=WebElementHighlighter(browser)
elem=browser.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]")
w.make_it_blink(elem)
time.sleep(10)
browser.close()