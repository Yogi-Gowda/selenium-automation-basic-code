from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
url = input("http://google.com")
driver.get(url)
links = driver.find_elements(By.TAG_NAME, 'a')
print(f"Number of links: {len(links)}")
driver.quit()
