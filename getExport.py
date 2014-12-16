from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC
from getpass import getpass


user_name = raw_input('Username:')
user_password = getpass('Password:')


fp = webdriver.FirefoxProfile("7oszrqb2.default")

driver = webdriver.Firefox(fp)
driver.get("http://www.lcfcu.org")

name = driver.find_element_by_name("userid")
password = driver.find_element_by_name("password")
login = driver.find_element_by_css_selector('div.loginCol.loginBtn > input[type="image"]')

name.send_keys(user_name)
password.send_keys(user_password)

login.click()


driver.implicitly_wait(10)
driver.switch_to_frame("uspbody")
driver.find_element_by_css_selector('#ext-gen35 > span').click
driver.implicitly_wait(10)
driver.find_element_by_id('ext-gen143').click
driver.find_element_by_id('rangeMonthly').click
driver.find_element_by_id('ext-gen15').click
driver.implicitly_wait(10)
driver.find_element_by_id('ext-gen15').click
driver.find_element_by_id('ext-gen180').click



#driver.close()
















