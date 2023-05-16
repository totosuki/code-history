#cookpadでスクレイピング練習したやつ

import urllib
import numpy as np
import pandas as pd
import requests
from lxml import html
from bs4 import BeautifulSoup

base_url = "https://cookpad.com/search/"
detail_base_url = "https://cookpad.com"

def read_csv():
  data = pd.read_csv("path/to.csv", index_col = 0, usecols = [0,2])
  food_list = data.values
  food_list = np.squeeze(food_list)
  for i, food_name in zip(range(len(food_list)), food_list):
    food_list[i] = base_url + urllib.parse.quote(food_name)
  print(food_list)
  return food_list

def parse_food_list(food_list):
  responses = np.empty(0)
  detail_id = np.empty(0).reshape(0,2)
  detail_urls = np.empty(0).reshape(0,2)
  id = 0

  print("\n---Use Request---\n")
  for food_url in food_list:
    print("Reqest = " + food_url)
    responses = np.append(responses, requests.get(food_url))
  
  print("\n---Use BeautifulSoup---\n")
  for res, food_url in zip(responses, food_list):
    print("Convert URL = " + food_url)

    #page変数は1ページ目が0です
    for page in range(5):
      #2ページ以降の場合ここで新しいURLのresponseを受け取る
      if page != 0:
        next_url = soup.select("a.next_page")[0].attrs["href"]
        print("next_url : " + next_url)
        res = requests.get(detail_base_url + next_url)

      soup = BeautifulSoup(res.text, "html.parser")
      elems = soup.select("a.recipe-title")
      
      for elem in elems: 
        detail_id = np.append(detail_id, [[id, elem.attrs["href"]]], axis = 0)
    
    id += 1
  
  print(detail_id)
  
  print("\n---Make Detail URL---")
  for id, detail_url in detail_id:
    if "dining" in detail_url:
      continue
    
    detail_urls = np.append(detail_urls, [[id, detail_base_url + detail_url]], axis = 0)

  print("\n---End 'parse_food_list'---\n")
  return detail_urls

def collect_img(detail_urls):
  responses = np.empty(0, dtype = object).reshape(0,2)
  result = np.empty(0, dtype = object).reshape(0,3)

  print("\n---Enter 'collect_img'---\n")

  print("\n---Use Request---\n")
  for id, detail_url in detail_urls:
    print("Request = " + detail_url)
    responses = np.append(responses, [[id,requests.get(detail_url)]], axis = 0)
  
  print("\n---Use BeautifulSoup---\n")
  for res, id, detail_url in zip(responses[:,1], detail_urls[:,0], detail_urls[:,1]):
    print("Collect URL = " + detail_url)
    soup = BeautifulSoup(res.text, "html.parser")
    lxml_data = html.fromstring(str(soup))
    title = lxml_data.xpath('//h1[@class="recipe-title"]/text()')
    image = lxml_data.xpath('//img[@class="photo large_photo_clickable"]/@src')
    title = "".join(title).replace("\n","")
    image = "".join(image)

    result = np.append(result, [[id, title, image]], axis = 0)
  return result

def save_result(result):
  return 

food_list = read_csv()
detail_urls = parse_food_list(food_list)
print(detail_urls)
print(type(detail_urls))
result = collect_img(detail_urls)
print("\n========== Result ==========\n")
print(result)