from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time
import xlrd

print("Starting webscraper...\n")

# Sets xls file (input)
workbook_path = r"src\domains_webscraper\utils\domain_names.xls"
sheet_name = "Planilha1"
workbook = xlrd.open_workbook(workbook_path)  
sheet = workbook.sheet_by_name(sheet_name)
rows = sheet.nrows
columns = sheet.ncols

# Sets txt file (output)
output_file_path = "src\domains_webscraper\output\output.txt"
output_file = open(output_file_path, "w")

# Sets chromedriver
driver_path = "src\chromedriver.exe"
driver_service = Service(driver_path)
driver_options = webdriver.ChromeOptions()
driver_options.add_argument("--disable-logging")
driver_options.add_argument("--log-level=3")
driver = webdriver.Chrome(service=driver_service, options=driver_options)

# Opens website
website_url = "https://registro.br/"
driver.get(website_url)  

# Populates search input and sends it for each domain
for current_row in range(0, rows):
  domain_name = sheet.cell_value(current_row, 0)

  # Finds search input by id and clears it
  search_input_id = "is-avail-field"
  search_input = driver.find_element("id", search_input_id)

  search_input.clear()
  time.sleep(1)

  # Inputs domain in search field 
  search_input.send_keys(domain_name)
  time.sleep(1)

  search_input.send_keys(Keys.RETURN)
  time.sleep(1)

  # Checks if domain is available and translates to english
  is_domain_available = driver.find_element("xpath", "//*[@id=\"app\"]/main/section/div[2]/div/p/span/strong")

  is_available = "not available"
  if (is_domain_available.text == "disponível"):
    is_available = "available"

  # Outputs results 
  output_text = "Domain \"%s\" %s \n" % (domain_name, is_available)
  output_file.write(output_text)

output_file.close()
driver.close()  