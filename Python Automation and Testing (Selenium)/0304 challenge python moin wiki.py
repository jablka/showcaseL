# https://wiki.python.org/moin/FrontPage

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By # pridané 
from selenium.webdriver.support.ui import Select
import time

driver= webdriver.Firefox()
driver.get("https://wiki.python.org/moin/FrontPage");

search = driver.find_element(By.ID,"searchinput") # 
search.send_keys("Beginner");
search.send_keys(Keys.RETURN);
time.sleep(4)

select = Select(driver.find_element(By.XPATH,'//*[@id="sidebar"]/div[3]/ul/li[5]/form/div/select'))
select.select_by_value("raw") # Raw Text
time.sleep(4)

driver.close();
