from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# init driver
driver = webdriver.Chrome(executable_path='/Users/alexlapkouski/Drivers/chromedriver')
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

checkboxes = driver.find_elements(By.CSS_SELECTOR, '._2dWgaQKyo0IbW6qgWYL79d:nth-child(3) > ._3tKwFY9SSNHJkaLR19S-JQ + div '
                                                 '> div[data-for] input[type=checkbox]')

index = 0
while index < len(checkboxes):
    checkbox = checkboxes[index]
    checkbox.click()
    driver.find_element(By.XPATH, '//div[@class="_2YmJUj2HMf2xUn8JxXNUO_"]/button[@name="applyFilter"]').click()
    sleep(3)
    status = driver.find_elements(By.CSS_SELECTOR, '._1yU0N8HRUChgPbo5OC6WAL ')
    # to do a loop for statuses
    assert len(status) == 25, f'Expected 25, but got {len(status)}'
    filter_button.click()
    sleep(3)
    checkboxes = driver.find_elements(By.CSS_SELECTOR,
                                      '._2dWgaQKyo0IbW6qgWYL79d:nth-child(3) > ._3tKwFY9SSNHJkaLR19S-JQ + div '
                                      '> div[data-for] input[type=checkbox]')
    checkbox = checkboxes[index]
    checkbox.click()
    index += 1

driver.quit()