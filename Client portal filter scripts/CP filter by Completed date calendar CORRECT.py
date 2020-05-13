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
checkboxes = driver.find_elements(By.CSS_SELECTOR, '._2dWgaQKyo0IbW6qgWYL79d:nth-child(6) > ._3tKwFY9SSNHJkaLR19S-JQ + div input[type=checkbox]')
checkboxes[4].click()
dates_input = driver.find_elements(By.CSS_SELECTOR, '.react-datepicker__input-container input')
# dates_input[0].click()

dates_input[0].send_keys(Keys.BACKSPACE * 10)
dates_input[0].send_keys("05/01/2020")
sleep(3)

dates_input = driver.find_elements(By.CSS_SELECTOR, '.react-datepicker__input-container input')
dates_input[1].click()
dates_input[1].clear()
dates_input[1].send_keys(Keys.BACKSPACE * 10)
dates_input[1].send_keys("05/03/2020")

apply_button = driver.find_element(By.XPATH, '//div[@class="_2YmJUj2HMf2xUn8JxXNUO_"]/button[@name="applyFilter"]').click()
sleep(2)

# Assert
completed_date = driver.find_elements(By. XPATH, './/span[@class = "_2trKg8mIZJBgE5H5qh-UFJ"]')
needed_info = completed_date[1:len(completed_date):2]
index = 0

if len(needed_info) > 0:
    while index < len(needed_info):
        get_date = needed_info[index]
        assert get_date.text == "05/01/2020" or get_date.text == "05/02/2020" or get_date.text == "05/03/2020"
        index += 1
else:
    print("No candidates")

driver.quit()