from selenium import webdriver
browser = webdriver.Firefox()
browser.maximize_window()
browser.get('https://cu.digiicampus.com/home')
title =browser.title
print(title)
assert 'Digiicampus' in browser.title
