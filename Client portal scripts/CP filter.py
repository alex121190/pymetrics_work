from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# init driver
driver = webdriver.Chrome()
driver.maximize_window()
# driver.implicitly_wait(10)

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


# Go to candidates page
# driver.find_element(By.XPATH, '//a[@title="Candidates"]').click()

# Click Filters button
filter_button = driver.find_element(By.XPATH, '//button[@class="QV-QATz9F5xIOwsy25LC0 "]')
filter_button.click()


# Click Invited checkbox
driver.find_element(By.XPATH, '//div[@data-for="Invited"]//input[@type="checkbox"]').click()


# Click Apply filter
driver.find_element(By.XPATH, '//div[@class="_2YmJUj2HMf2xUn8JxXNUO_"]/button[@name="applyFilter"]').click()
sleep(3)


# # Should be 25 Invited
invited = driver.find_elements(By.CSS_SELECTOR, '._1yU0N8HRUChgPbo5OC6WAL ')
assert len(invited) == 25, f'Expected 25, but got {len(invited)}'
# print(len(invited))


# Click Filters button
filter_button = driver.find_element(By.XPATH, '//button[@class="QV-QATz9F5xIOwsy25LC0 "]')
filter_button.click()

# Click Invited checkbox
driver.find_element(By.XPATH, '//div[@data-for="Invited"]//input[@type="checkbox"]').click()

# Click Registered checkbox
driver.find_element(By.XPATH, '//div[@data-for="Registered"]//input[@type="checkbox"]').click()

# Click Apply filter
driver.find_element(By.XPATH, '//div[@class="_2YmJUj2HMf2xUn8JxXNUO_"]/button[@name="applyFilter"]').click()
sleep(3)


# # Should be 25 Invited
registered = driver.find_elements(By.CSS_SELECTOR, '._1yU0N8HRUChgPbo5OC6WAL ')
assert len(registered) == 25, f'Expected 25, but got {len(registered)}'
# print(len(invited))

# Click Filters button
filter_button = driver.find_element(By.XPATH, '//button[@class="QV-QATz9F5xIOwsy25LC0 "]')
filter_button.click()

# Click Registered checkbox
driver.find_element(By.XPATH, '//div[@data-for="Registered"]//input[@type="checkbox"]').click()

# Click In progress checkbox
driver.find_element(By.XPATH, '//div[@data-for="In Progress"]//input[@type="checkbox"]').click()

# Click Apply filter
driver.find_element(By.XPATH, '//div[@class="_2YmJUj2HMf2xUn8JxXNUO_"]/button[@name="applyFilter"]').click()
sleep(3)


# # Should be 25 Invited
in_progress = driver.find_elements(By.CSS_SELECTOR, '._1yU0N8HRUChgPbo5OC6WAL ')
assert len(in_progress) == 25, f'Expected 25, but got {len(in_progress)}'
# print(len(invited))

# Click Filters button
filter_button = driver.find_element(By.XPATH, '//button[@class="QV-QATz9F5xIOwsy25LC0 "]')
filter_button.click()

# Click In progress checkbox
driver.find_element(By.XPATH, '//div[@data-for="In Progress"]//input[@type="checkbox"]').click()

# Click Completed checkbox
driver.find_element(By.XPATH, '//div[@data-for="Completed"]//input[@type="checkbox"]').click()

# Click Apply filter
driver.find_element(By.XPATH, '//div[@class="_2YmJUj2HMf2xUn8JxXNUO_"]/button[@name="applyFilter"]').click()
sleep(3)


# # Should be 25 Invited
completed = driver.find_elements(By.CSS_SELECTOR, '._1yU0N8HRUChgPbo5OC6WAL ')
assert len(completed) == 25, f'Expected 25, but got {len(completed)}'
# print(len(invited))

driver.quit()