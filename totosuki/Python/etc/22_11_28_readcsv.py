#csvデータを読み込んでURLを作るプログラム?

import pandas as pd
import numpy as np
import urllib

def read_csv():
  data = pd.read_csv("path/to.csv",index_col = 0, usecols = [0,2])
  foodList = data.values
  # print(type(data))
  # print(type(foodList))
  # print(foodList)
  foodList = np.squeeze(foodList)
  print(foodList)
  for i,foodname in zip(range(len(foodList)), foodList):
    foodList[i] = urllib.parse.quote(foodname)
  
  print(foodList)

def read_csv_2():
  data = pd.read_csv("path/to.csv", index_col = 0, usecols = [0,2])
  foodList = data.values
  foodList = np.squeeze(foodList)

  food_list_encoded = np.empty(0)

  print(data)
  print(foodList)
  for foodname in foodList:
    food_list_encoded = np.append(food_list_encoded,urllib.parse.quote(foodname))

  print(food_list_encoded)

# read_csv()
read_csv_2()
