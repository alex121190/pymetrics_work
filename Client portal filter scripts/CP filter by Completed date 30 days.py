from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime, date, timedelta

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
checkboxes[2].click()
apply_button = driver.find_element(By.XPATH, '//div[@class="_2YmJUj2HMf2xUn8JxXNUO_"]/button[@name="applyFilter"]').click()
sleep(2)

# Getting selectors we need
completed_date = driver.find_elements(By. XPATH, './/span[@class = "_2trKg8mIZJBgE5H5qh-UFJ"]')
needed_info = completed_date[1:len(completed_date):2]
index = 0

if len(needed_info) > 0:
    while index < len(needed_info):
        get_date = needed_info[index]
        date_parsed = datetime.strptime(get_date.text, "%m/%d/%Y")
        date_difference = datetime.now() - date_parsed
        assert int(date_difference.days) <= 30
        print(date_difference.days)
        index += 1
else:
    print("No candidates")


driver.quit()