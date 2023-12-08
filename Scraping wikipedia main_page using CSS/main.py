from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


chrome_driver_path = "/Users/saurabh/Development/chromedriver"
driver = webdriver.ChromeOptions(chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
print(article_count.text)