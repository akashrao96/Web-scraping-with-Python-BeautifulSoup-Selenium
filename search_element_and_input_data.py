from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
driver = webdriver.Chrome("/home/akashrao96/chromedriver_linux64/chromedriver")
driver.get('https://www.google.com')
# search tag using class
form=driver.find_element(By.NAME,"q")
# input data which you want to search for
form.send_keys("narendra modi")
# submit the form
driver.find_element(By.NAME,"btnK").submit()
sleep(10)
driver.close()


