from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# init driver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

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
needed_person = driver.find_element(By.CSS_SELECTOR, '[data-for="Alex.Lapkouski@pymetrics.com"] [type=checkbox]').click()
apply_button = driver.find_element(By.XPATH, '//button[contains(text(), "Apply Filters")]').click()
# sleep(2)

# Assertion
emails_needed = driver.find_elements(By.XPATH, '//a[3]/div/div/span[text()]')

if len(emails_needed) > 0:
    for email in emails_needed:
        print(email.text)
        if "alex" in email.text or "Alex" in email.text:
            continue
        else:
            print("Wrong user")

driver.quit()