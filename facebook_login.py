from selenium import webdriver
from time import sleep
url='https://www.facebook.com'
driver = webdriver.Chrome("/home/akashrao96/chromedriver_linux64/chromedriver")
driver.get(url)
username = driver.find_element_by_id("email") #username form field
username.send_keys("*****@example.com")
sleep(1)
password = driver.find_element_by_id("pass") #password form field
password.send_keys("*******")
sleep(1)
sign_in_button = driver.find_element_by_xpath('//*[@type="submit"]')
sign_in_button.click()
sleep(2.5)
driver.quit()

