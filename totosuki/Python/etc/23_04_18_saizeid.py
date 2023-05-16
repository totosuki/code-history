#サイゼリヤの商品番号を取得するプログラム(笑)

import requests
from bs4 import BeautifulSoup
from lxml import html
import numpy as np

URL = "https://cafe-tatsujin.com/saizeriya-menu.html"
res = requests.get(URL)
soup = BeautifulSoup(res.text, "html.parser")
lxml_data = html.fromstring(str(soup))

result = np.empty(0, dtype = object).reshape(0,2)
for figure_num in range(4,32):
  for tr_num in range(1, 100):
    elem = lxml_data.xpath(f'//*[@id="post-6162"]/div/div/figure[{figure_num}]/div/table/tbody/tr[{tr_num}]')
    if len(elem) == 0:
      print("elem is empty")
      break
    id = lxml_data.xpath(f'//*[@id="post-6162"]/div/div/figure[{figure_num}]/div/table/tbody/tr[{tr_num}]/td[1]/text()')
    name = lxml_data.xpath(f'//*[@id="post-6162"]/div/div/figure[{figure_num}]/div/table/tbody/tr[{tr_num}]/td[2]/text()')
    result = np.append(result, [[np.squeeze(id), np.squeeze(name)]], axis = 0)
print(result)