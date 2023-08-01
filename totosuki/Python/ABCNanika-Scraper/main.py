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
PROB_URL_PATH = "//table[@class='table table-sm table-bordered table-striped']/tbody/tr/td/a[@href]"

def start():
  options = Options()
  driver = webdriver.Chrome(options=options)
  driver.get(URL + PROBLEMS)
  return driver

def get_number(driver: webdriver.Chrome) -> int:
  elem = driver.find_element(By.XPATH, PROB_URL_PATH)
  value = elem.get_attribute("href")
  
  match = re.search(r"abc(\d+)", value)
  if match:
    number = match.group(1)
    try:
      number = int(number)
      return number
    except ValueError:
      return None
  else:
    None

def main():
  driver = start()
  time.sleep(5)
  number = get_number(driver)
  print(number)

if __name__ == "__main__":
  main()