from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime, timedelta
#
# # current date and time
# now = datetime.now()
#
# s1 = now.strftime("%m/%d/%Y")
# # mm/dd/YY format
# print(s1)
#
# dt = datetime.now() - timedelta(5)
# print(dt.day)
#
# first_number = int(input("This the first number "))
# second_number = int(input("This ithe second number "4))
#
# if first_number > second_number:
#     print(second_number, first_number)
# else:
#     print(first_number, second_number)
#
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# init driver
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.staging.pymetrics.com/c/p/candidates')

# Log in
login = driver.find_element(By.XPATH, '//input[@id ="username"]')
login.clear()
login.send_keys('alex.lapkouski@pymetrics.com')

password = driver.find_element(By.XPATH, '//input[@id ="password"]')
password.clear()
password.send_keys('6428531_Vbycr')

driver.find_element(By.XPATH, '//button[@name="login"]').click()
sleep(5)

# Click Filters button
filter_button = driver.find_element(By.CSS_SELECTOR, 'i.fa.fa-sliders')
filter_button.click()

checkboxes = driver.find_elements(By.CSS_SELECTOR, '._2dWgaQKyo0IbW6qgWYL79d:first-child > div > div')
checkboxes[-4].click()


