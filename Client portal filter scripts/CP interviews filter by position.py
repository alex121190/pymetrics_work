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

interviews_button = driver.find_elements(By.CSS_SELECTOR, '._1CzUwQfdI5sAtkrdDKRMGu button')
interviews_button[1].click()
sleep(5)

# Click Filters button
filter_button = driver.find_element(By.XPATH, '//button[@class="QV-QATz9F5xIOwsy25LC0 "]')
filter_button.click()
sleep(2)

checkboxes = driver.find_elements(By.CSS_SELECTOR, '._2dWgaQKyo0IbW6qgWYL79d:nth-child(4) > ._3tKwFY9SSNHJkaLR19S-JQ + div '
                                                 '> div[data-for] input[type=checkbox]')

checkboxes_text = driver.find_elements(By.CSS_SELECTOR, '._2dWgaQKyo0IbW6qgWYL79d:nth-child(4) > ._3tKwFY9SSNHJkaLR19S-JQ + div > div[data-for]')
index = 0

while index < len(checkboxes):
    checkbox = checkboxes[index]
    checkbox_text = checkboxes_text[index]
    needed_text = checkbox_text.get_attribute('data-for')
    print(needed_text)
    checkbox.click()
    apply_filters = driver.find_element(By.XPATH, "//div[@class='_2YmJUj2HMf2xUn8JxXNUO_']/button[@class='_3rdl9VsMj4bMvKWMJzb4nx _3VvSq4SKmCoDDK8nzcON1N']").click()
    sleep(5)
    position_name = driver.find_elements(By.XPATH,
        "//a[@class='_2KIninGfXsD6cdf3q8JMh sU5C_SKPfvqMZlRLHWDFp FkFyqEJe1OWSPqqHhdFNP ']/div[@style='align-items: center;']//span")
    if len(position_name) > 0:
        for name in position_name:
            if name.text == "Demo Project test org":
                pass
            else:
                assert name.text == needed_text, f'Expected {needed_text} but got {name.text}'
    else:
        print("Empty")
    filter_button.click()
    sleep(2)
    checkboxes = driver.find_elements(By.CSS_SELECTOR,
                                      '._2dWgaQKyo0IbW6qgWYL79d:nth-child(4) > ._3tKwFY9SSNHJkaLR19S-JQ + div '
                                      '> div[data-for] input[type=checkbox]')
    checkboxes_text = driver.find_elements(By.CSS_SELECTOR,
                                          '._2dWgaQKyo0IbW6qgWYL79d:nth-child(4) > ._3tKwFY9SSNHJkaLR19S-JQ + div > div[data-for]')
    checkbox_text = checkboxes_text[index]
    needed_text = checkbox_text.get_attribute('data-for')
    checkbox = checkboxes[index]
    checkbox.click()
    index += 1

driver.quit()