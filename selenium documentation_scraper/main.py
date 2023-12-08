
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Deprecated - no longer needed
chrome_driver_path = "/Users/saurabh/Development/chromedriver"

# keeps chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(executable_path=chrome_driver_path)
# driver = webdriver.Chrome()
driver = webdriver.Chrome(options=chrome_options)

# def test_eight_components():
#     driver.get("https://www.selenium.dev/selenium/web/web-form.html")
#     title = driver.title
#     assert title == "Web form"
#     driver.implicitly_wait(0.5)
#     text_box = driver.find_element(by=By.NAME, value="my-text")
#     submit_button = driver.find_element(By.XPATH, value='//*[@id="selenium-with-python"]/div[2]/ul/li[2]/a')
#     text_box.send_keys("Selenium")
#     submit_button.click()
#     message = driver.find_element(by=By.ID, value="message")
#     value = message.text
#     assert value == "Received!"
#
#
#     # Closes Chrome
#     driver.quit()
#     # driver.close()
#
#
# test_eight_components()

driver.get("https://www.python.org/")

event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n],
        "name": event_names[n],
    }

print(events)
driver.quit()