import sys
import re
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

arg = sys.argv
url = arg[1]

PROBLEMS = "?activeTab=Problems"
STANDINGS = "?activeTab=Standings"
URL = url.replace(STANDINGS,"").replace(PROBLEMS, "")
DATE_PATH = "//table[@class='mb-0 table']/tbody/tr/td"
PROB_URL_PATH = "//table[@class='table table-sm table-bordered table-striped']/tbody/tr/td/a[@href]"

def start():
  options = Options()
  driver = webdriver.Chrome(options=options)
  driver.get(URL + PROBLEMS)
  return driver

def get_date(driver: webdriver.Chrome) -> str:
  elem = driver.find_element(By.XPATH, DATE_PATH)
  value = elem.text
  
  match = re.search(r'(\d{4}-\d{2}-\d{2})', value)
  return match.group(1)

def get_number(driver: webdriver.Chrome) -> int:
  elem = driver.find_element(By.XPATH, PROB_URL_PATH)
  value = elem.get_attribute("href")
  
  match = re.search(r"abc(\d+)", value)
  return match.group(1)

def main():
  driver = start()
  time.sleep(5)
  date = get_date(driver)
  number = get_number(driver)
  print(date)
  print(number)

if __name__ == "__main__":
  main()