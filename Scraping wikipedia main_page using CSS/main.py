from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


chrome_driver_path = "C:/Users/saura/.cache/selenium/chromedriver"
driver = webdriver.Chrome()

driver.get("https://en.wikipedia.org/wiki/Main_Page")
article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")

article_count.click()

all_portals = driver.find_element(By.LINK_TEXT, "All portals")

search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(keys.ENTER)

driver.quit()