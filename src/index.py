from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time

print("Starting webscraper...\n")

# Sets chromedriver
driver_path = 'utils\chromedriver.exe'
driver_service = Service(driver_path)
driver_options = webdriver.ChromeOptions()
driver_options.add_argument("--disable-logging")
driver_options.add_argument("--log-level=3")
driver = webdriver.Chrome(service=driver_service, options=driver_options)

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

# Checks if domain is available and translates to english
is_domain_available = driver.find_element('xpath', '//*[@id="app"]/main/section/div[2]/div/p/span/strong')

is_available = 'not available'

if (is_domain_available.text == 'disponível'):
  is_available = 'available'

print("Domain \"%s\" %s" % (domain_name, is_available))

time.sleep(8)
driver.close()  