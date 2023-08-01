from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By # pridané 
import time

driver= webdriver.Firefox()
driver.get("http://python.org");

# search = driver.find_element_by_name('q');
search = driver.find_element(By.NAME,"q") # ('name',"q")
search.clear(); # clears any existing text there
search.send_keys("pycon");
search.send_keys(Keys.RETURN);
time.sleep(4)

driver.close();
