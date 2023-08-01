from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By # pridané podľa https://www.youtube.com/watch?v=-UB1lR7BDbM
import time

driver = webdriver.Firefox()
driver.get("http://www.python.org")

# elem = driver.find_element_by_name("q")
elem = driver.find_element(By.NAME,"q") # ('name',"q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
time.sleep(8)

driver.close()
