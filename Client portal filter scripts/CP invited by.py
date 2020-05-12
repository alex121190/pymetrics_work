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
filter_button = driver.find_element(By.XPATH, '//button[@class="QV-QATz9F5xIOwsy25LC0 "]')
filter_button.click()

search_line = driver.find_element(By.CSS_SELECTOR, '[placeholder="Search for others"]')
search_line.clear()
search_line.send_keys('lapkouski')
needed_person = driver.find_element(By.CSS_SELECTOR, '[data-for="Alex.Lapkouski@pymetrics.com"] input[type=checkbox]').click()
apply_button = driver.find_element(By.XPATH, '//div[@class="_2YmJUj2HMf2xUn8JxXNUO_"]/button[@name="applyFilter"]').click()
sleep(2)

# Assertion
emails_needed = driver.find_elements(By.XPATH, "//div[@class='_1yU0N8HRUChgPbo5OC6WAL ']/a[@class='_2KIninGfXsD6cdf3q8JMh "
                                               "FkFyqEJe1OWSPqqHhdFNP _1vcpikaMB6B_c_j9hakYb6']//div[@style='text-align: left;']")

if len(emails_needed) > 0:
    for email in emails_needed:
        if "alex" in email.text or "Alex" in email.text:
            continue
        else:
            print("Wrong user")
else:
    print("No results")

driver.quit()