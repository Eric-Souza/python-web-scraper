from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time
import xlrd

print("Starting webscraper...\n")

# Sets xls file
workbook_path = "utils\domain_names.xls"
sheet_name = "Planilha1"
workbook = xlrd.open_workbook(workbook_path)  
sheet = workbook.sheet_by_name(sheet_name)
rows = sheet.nrows
columns = sheet.ncols

# Sets chromedriver
driver_path = "utils\chromedriver.exe"
driver_service = Service(driver_path)
driver_options = webdriver.ChromeOptions()
driver_options.add_argument("--disable-logging")
driver_options.add_argument("--log-level=3")
driver = webdriver.Chrome(service=driver_service, options=driver_options)

# Opens website
website_url = "https://registro.br/"
driver.get(website_url)  

# Populates search input and sends it
for current_row in range(0, rows):
  domain_name = sheet.cell_value(current_row, 0)

  # Finds search input by id and clears it
  search_input_id = "is-avail-field"
  search_input = driver.find_element("id", search_input_id)

  time.sleep(1)
  search_input.clear()
  time.sleep(1)

  # Inputs domain in search field 
  search_input.send_keys(domain_name)
  search_input.send_keys(Keys.RETURN)

  time.sleep(1)

  # Checks if domain is available and translates to english
  is_domain_available = driver.find_element("xpath", "//*[@id=\"app\"]/main/section/div[2]/div/p/span/strong")

  time.sleep(1)

  is_available = "not available"

  if (is_domain_available.text == "disponível"):
    is_available = "available"

  print("Domain \"%s\" %s" % (domain_name, is_available))

driver.close()  