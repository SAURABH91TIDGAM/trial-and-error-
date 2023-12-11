from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path="C:/Users/saura/.cache/selenium/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://secure-retreat-92358.herokuapp.com")

first_name = driver.find_element(By.Name, "fName")
first_name.send_keys("Saurabh")
driver.find_element(By.NAME, "lName")
driver.find_element(By.NAME, "email")