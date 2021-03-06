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

checkboxes = driver.find_elements(By.CSS_SELECTOR, '._2dWgaQKyo0IbW6qgWYL79d:nth-child(3) > div > div input[type=checkbox]')
checkboxes_text = driver.find_elements(By.CSS_SELECTOR, '._2dWgaQKyo0IbW6qgWYL79d:nth-child(3) > div > div[data-for]')
index = 0

while index < len(checkboxes):
    needed_text = checkboxes_text[index].get_attribute('data-for')
    print(needed_text)
    checkboxes[index].click()
    apply_filters = driver.find_element(By.XPATH, '//button[contains(text(), "Apply Filters")]').click()
    sleep(2)
    position_name = driver.find_elements(By.XPATH, '//a[4]/div/div/span[text()]')
    if len(position_name) > 0:
        for name in position_name:
            assert name.text == needed_text, f'Expected {needed_text} but got {name.text}'
    else:
        print("Empty")
    filter_button.click()
    sleep(2)
    checkboxes = driver.find_elements(By.CSS_SELECTOR, '._2dWgaQKyo0IbW6qgWYL79d:nth-child(3) > div > div input[type=checkbox]')
    checkboxes_text = driver.find_elements(By.CSS_SELECTOR, '._2dWgaQKyo0IbW6qgWYL79d:nth-child(3) > div > div[data-for]')
    needed_text = checkboxes_text[index].get_attribute('data-for')
    checkboxes[index].click()
    index += 1

driver.quit()