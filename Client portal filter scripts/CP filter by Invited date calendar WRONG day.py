from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime, date, timedelta
from selenium.webdriver.common.keys import Keys

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
filter_button = driver.find_element(By.XPATH, '//button[@class="QV-QATz9F5xIOwsy25LC0 "]')
filter_button.click()

# Needed checkbox click
checkboxes = driver.find_elements(By.CSS_SELECTOR, '._2dWgaQKyo0IbW6qgWYL79d:nth-child(5) > ._3tKwFY9SSNHJkaLR19S-JQ + div input[type=checkbox]')
checkboxes[4].click()
dates_input = driver.find_elements(By.CSS_SELECTOR, '.react-datepicker__input-container input')
# dates_input[0].click()
dates_input[0].send_keys(Keys.BACKSPACE * 10)

needed_day = datetime.now() + timedelta(3)
today_format = needed_day.strftime("%m/%d/%Y")
dates_input[0].send_keys(today_format)
sleep(2)


apply_button = driver.find_element(By.XPATH, '//div[@class="_2YmJUj2HMf2xUn8JxXNUO_"]/button[@name="applyFilter"]').click()
sleep(2)

text_locator = driver.find_element(By.CSS_SELECTOR, 'h3').text
assert text_locator == "Sorry it looks like no candidates match that query..."

driver.quit()