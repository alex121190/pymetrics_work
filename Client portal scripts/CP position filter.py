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

checkboxes_text = driver.find_elements(By.CSS_SELECTOR, '._2dWgaQKyo0IbW6qgWYL79d:nth-child(3) > ._3tKwFY9SSNHJkaLR19S-JQ + div > div[data-for]')
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
                                      '._2dWgaQKyo0IbW6qgWYL79d:nth-child(3) > ._3tKwFY9SSNHJkaLR19S-JQ + div '
                                      '> div[data-for] input[type=checkbox]')
    checkboxes_text = driver.find_elements(By.CSS_SELECTOR,
                                          '._2dWgaQKyo0IbW6qgWYL79d:nth-child(3) > ._3tKwFY9SSNHJkaLR19S-JQ + div > div[data-for]')
    checkbox_text = checkboxes_text[index]
    needed_text = checkbox_text.get_attribute('data-for')
    checkbox = checkboxes[index]
    checkbox.click()
    index += 1

driver.quit()