from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

# Disables logging to avoid clutter
options = webdriver.ChromeOptions()
options.add_argument("--disable-logging")
options.add_argument("--log-level=3")

# Sets chromedriver
driver = webdriver.Chrome('path')

# Opens website
driver.get("https://registro.br/")  

# Finds search input, populates it and sends
search_input = driver.find_element("is-avail-field")
search_input.clear()
search_input.send_keys("keys")
search_input.send_keys(Keys.RETURN)

time.sleep(8)
driver.close()