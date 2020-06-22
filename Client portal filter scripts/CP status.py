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

checkboxes = driver.find_elements(By.CSS_SELECTOR, '._2dWgaQKyo0IbW6qgWYL79d:first-child > div > div input[type=checkbox')
checkboxes_text = driver.find_elements(By.CSS_SELECTOR, '._2dWgaQKyo0IbW6qgWYL79d:first-child > div > div[data-for]')
index = 0

while index < len(checkboxes):
    checkbox = checkboxes[index]
    checkbox_text = checkboxes_text[index]
    needed_text = checkbox_text.get_attribute('data-for')
    print(needed_text)
    checkbox.click()
    apply_filters = driver.find_element(By.XPATH, '//button[contains(text(), "Apply Filters")]')
    apply_filters.click()
    sleep(5)
    text1 = driver.find_elements(By.XPATH, '//a/p[text()]')
    if len(text1) > 0:
        for element in text1:
            assert needed_text == element.text
            print(element.text)
    filter_button.click()
    sleep(2)
    checkboxes = driver.find_elements(By.CSS_SELECTOR, '._2dWgaQKyo0IbW6qgWYL79d:first-child > div > div input[type=checkbox')
    checkboxes_text = driver.find_elements(By.CSS_SELECTOR, '._2dWgaQKyo0IbW6qgWYL79d:first-child > div > div[data-for]')
    checkbox_text = checkboxes_text[index]
    needed_text = checkbox_text.get_attribute('data-for')
    checkbox = checkboxes[index]
    checkbox.click()
    index += 1

driver.quit()