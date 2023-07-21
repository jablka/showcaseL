#
# NOTE: three things were outdated and needed correction:
# - url to demo webpage
# - xpath for value1, value2
# - and using .find_element('xpath','foo') instead of .find_element_by_xpath()
#

from selenium import webdriver

# url = 'https://www.seleniumeasy.com/test/basic-first-form-demo.html'
url = 'https://demo.seleniumeasy.com/basic-first-form-demo.html'

driver = webdriver.Firefox()
# driver = webdriver.Chrome()

driver.get(url)

###
messageField = driver.find_element('xpath','//*[@id="user-message"]')
messageField.send_keys("Hello World")

showMessageButton = driver.find_element('xpath','//*[@id="get-input"]/button') 
showMessageButton.click()

###
additionField1 = driver.find_element('xpath','//*[@id="value1"]')
additionField1.send_keys('10')

additionField2 = driver.find_element('xpath','//*[@id="value2"]')
additionField2.send_keys('12')

getTotalButton = driver.find_element('xpath','//*[@id="gettotal"]/button')
getTotalButton.click()
###

# done!
#
