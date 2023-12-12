from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path="C:/Users/saura/.cache/selenium/chromedriver"
driver = webdriver.Chrome()

driver.get("https://secure-retreat-92358.herokuapp.com")

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Saurabh")

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("tidgam")

email = driver.find_element(By.NAME, "email")
email.send_keys("saurabhtidgam1991@gmail.com")

submit = driver.find_element(By.CSS_SELECTOR, "form button")
submit.click()

driver.close()