from selenium import webdriver
import time
from bs4 import BeautifulSoup
driver = webdriver.Chrome("/home/akashrao96/chromedriver_linux64/chromedriver")
driver.get('https://www.google.com')
soup=BeautifulSoup(driver.page_source,'html.parser')
print(soup.prettify())
driver.close()

