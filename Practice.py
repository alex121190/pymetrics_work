from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime, timedelta

# current date and time
now = datetime.now()

s1 = now.strftime("%m/%d/%Y")
# mm/dd/YY format
print(s1)

dt = datetime.now() - timedelta(5)
print(dt.day)




