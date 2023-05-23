from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def open_first_search_result(link, sku):
    options = Options()
    service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=options)
    full_link = link + sku
    driver.get(full_link)
    time.sleep(3)
    search_results = driver.find_elements('css selector', '[tabindex="0"]')
    if search_results:
        search_results[0].click()
    driver.quit()

link = "https://stockx.com/search?s="
sku_list = []
while True:
    try:
        line = input("Enter your designated SKUs (Press Enter to finish): ")
        if not line:
            break
        sku_list.append(line)
    except EOFError:
        break

if sku_list:
    full_link = link + sku_list[0]
    open_first_search_result(link, sku_list[0])

for sku in sku_list[1:]:
    open_first_search_result(link, sku)