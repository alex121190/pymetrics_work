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


# Go to candidates page
# driver.find_element(By.XPATH, '//a[@title="Candidates"]').click()

# Click Filters button
filter_button = driver.find_element(By.XPATH, '//button[@class="QV-QATz9F5xIOwsy25LC0 "]')
filter_button.click()

checkboxes = driver.find_elements(By.CSS_SELECTOR, '._2dWgaQKyo0IbW6qgWYL79d:first-child > ._3tKwFY9SSNHJkaLR19S-JQ + div '
                                                 '> div[data-for] input[type=checkbox]')
checkboxes_text = driver.find_elements(By.CSS_SELECTOR, '._2dWgaQKyo0IbW6qgWYL79d:first-child > ._3tKwFY9SSNHJkaLR19S-JQ + div > div[data-for]')
index = 0
while index < len(checkboxes):
    checkbox = checkboxes[index]
    # while index < len(checkboxes_text)
    checkbox_text = checkboxes_text[index]
    needed_text = checkbox_text.get_attribute('data-for')
    print(needed_text)
    checkbox.click()
    driver.find_element(By.XPATH, '//div[@class="_2YmJUj2HMf2xUn8JxXNUO_"]/button[@name="applyFilter"]').click()
    sleep(2)
    text1 = driver.find_element(By.XPATH,
                                "//a[@class='_2KIninGfXsD6cdf3q8JMh FkFyqEJe1OWSPqqHhdFNP _3R-oI7bxnSARfvf2PltvFp']/p").text
    print(text1)
    assert needed_text == text1
    # assert len(status) == 25, f'Expected 25, but got {len(status)}'
    # status = driver.find_elements(By.CSS_SELECTOR, '._1yU0N8HRUChgPbo5OC6WAL ')
    filter_button.click()
    sleep(2)
    checkboxes = driver.find_elements(By.CSS_SELECTOR,
                                      '._2dWgaQKyo0IbW6qgWYL79d:first-child > ._3tKwFY9SSNHJkaLR19S-JQ + div '
                                      '> div[data-for] input[type=checkbox]')
    checkboxes_text = driver.find_elements(By.CSS_SELECTOR,
                                          '._2dWgaQKyo0IbW6qgWYL79d:first-child > ._3tKwFY9SSNHJkaLR19S-JQ + div > div[data-for]')
    checkbox_text = checkboxes_text[index]
    needed_text = checkbox_text.get_attribute('data-for')
    checkbox = checkboxes[index]
    checkbox.click()
    index += 1

driver.quit()


# # Click Invited checkbox
# driver.find_element(By.XPATH, '//div[@data-for="Invited"]//input[@type="checkbox"]').click()
#
#
# # Click Apply filter
# driver.find_element(By.XPATH, '//div[@class="_2YmJUj2HMf2xUn8JxXNUO_"]/button[@name="applyFilter"]').click()
# sleep(3)


# # # Should be 25 Invited
# invited = driver.find_elements(By.CSS_SELECTOR, '._1yU0N8HRUChgPbo5OC6WAL ')
# assert len(invited) == 25, f'Expected 25, but got {len(invited)}'
# # print(len(invited))
#
#
# # Click Filters button
# filter_button = driver.find_element(By.XPATH, '//button[@class="QV-QATz9F5xIOwsy25LC0 "]')
# filter_button.click()
#
# # Click Invited checkbox
# driver.find_element(By.XPATH, '//div[@data-for="Invited"]//input[@type="checkbox"]').click()
#
# # Click Registered checkbox
# driver.find_element(By.XPATH, '//div[@data-for="Registered"]//input[@type="checkbox"]').click()
#
# # Click Apply filter
# driver.find_element(By.XPATH, '//div[@class="_2YmJUj2HMf2xUn8JxXNUO_"]/button[@name="applyFilter"]').click()
# sleep(3)
#
#
# # # Should be 25 Invited
# registered = driver.find_elements(By.CSS_SELECTOR, '._1yU0N8HRUChgPbo5OC6WAL ')
# assert len(registered) == 25, f'Expected 25, but got {len(registered)}'
# # print(len(invited))
#
# # Click Filters button
# filter_button = driver.find_element(By.XPATH, '//button[@class="QV-QATz9F5xIOwsy25LC0 "]')
# filter_button.click()
#
# # Click Registered checkbox
# driver.find_element(By.XPATH, '//div[@data-for="Registered"]//input[@type="checkbox"]').click()
#
# # Click In progress checkbox
# driver.find_element(By.XPATH, '//div[@data-for="In Progress"]//input[@type="checkbox"]').click()
#
# # Click Apply filter
# driver.find_element(By.XPATH, '//div[@class="_2YmJUj2HMf2xUn8JxXNUO_"]/button[@name="applyFilter"]').click()
# sleep(3)
#
#
# # # Should be 25 Invited
# in_progress = driver.find_elements(By.CSS_SELECTOR, '._1yU0N8HRUChgPbo5OC6WAL ')
# assert len(in_progress) == 25, f'Expected 25, but got {len(in_progress)}'
# # print(len(invited))
#
# # Click Filters button
# filter_button = driver.find_element(By.XPATH, '//button[@class="QV-QATz9F5xIOwsy25LC0 "]')
# filter_button.click()
#
# # Click In progress checkbox
# driver.find_element(By.XPATH, '//div[@data-for="In Progress"]//input[@type="checkbox"]').click()
#
# # Click Completed checkbox
# driver.find_element(By.XPATH, '//div[@data-for="Completed"]//input[@type="checkbox"]').click()
#
# # Click Apply filter
# driver.find_element(By.XPATH, '//div[@class="_2YmJUj2HMf2xUn8JxXNUO_"]/button[@name="applyFilter"]').click()
# sleep(3)
#
#
# # # Should be 25 Invited
# completed = driver.find_elements(By.CSS_SELECTOR, '._1yU0N8HRUChgPbo5OC6WAL ')
# assert len(completed) == 25, f'Expected 25, but got {len(completed)}'
# # print(len(invited))

# driver.quit()