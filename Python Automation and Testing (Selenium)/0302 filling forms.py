from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By # pridané 

driver= webdriver.Firefox()
driver.get("") # the address to the 'html_code_03_02.html' in the following format: file:///C:/Exercise%20Files/CH03/html_code_03_02.html

# select= Select(driver.find_element_by_name('numReturnSelect'))
select= Select(driver.find_element(By.NAME,'numReturnSelect'))
select.select_by_index(4) # 15000
time.sleep(2)

select.select_by_visible_text("200") # 200
time.sleep(2)

select.select_by_value("250") # 250
time.sleep(2)

options = select.options
print(options)

# submit_button = driver.find_element_by_name('continue')
submit_button = driver.find_element(By.NAME,'continue')
submit_button.submit();
time.sleep(2)

driver.close()
