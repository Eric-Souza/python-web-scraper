from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

print("Starting webscraper...\n")

# Disables logging to avoid clutter
options = webdriver.ChromeOptions()
options.add_argument("--disable-logging")
options.add_argument("--log-level=3")

# Sets chromedriver
driver_path = 'path'
driver = webdriver.Chrome(driver_path)

# Opens website
website_url = "https://registro.br/"
driver.get(website_url)  

# Finds search input by id
search_input_id = 'is-avail-field'
search_input = driver.find_element('id', search_input_id)
search_input.clear()

# Populates search input and sends it
domain_name = "amazon.com"
search_input.send_keys(domain_name)
search_input.send_keys(Keys.RETURN)

time.sleep(2)

# Checks if domain exists
is_domain_available = driver.find_element('xpath', '//*[@id="app"]/main/section/div[2]/div/p/span/strong')
print("Domain %s %s" % (domain_name, is_domain_available.text))

time.sleep(8)
driver.close()  