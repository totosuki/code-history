# Silly Wisher スライム戦闘用

import sys
import time
import datetime
import pyautogui as pg

pos1 = [1350, 800] #通常の位置
pos2 = [1250, 850] #必殺技の位置

def click_count():
  print("クリック回数を入力して下さい")
  count = int(input())

  pg.moveTo(pos1[0], pos1[1], 1)

  for i in range(count):
    x, _ = pg.position()
    if x != pos1[0] and x != pos2[0]:
      print("============================================")
      print("カーソル移動をしたためプログラムを中止します")
      time.sleep(3)
      sys.exit(1)

    if i % 5 == 0:
      pg.click(pos2[0], pos2[1])
      if i % 100 == 0:
        print(f"あなたがクリックした回数は{i}回です")
      continue

    pg.click(pos1[0], pos1[1])

def click_time():
  print("使う時間を分単位で入力")
  playmin = int(input())

  pg.moveTo(pos1[0], pos1[1], 1)

  startTime = time.time()
  thisTime = time.time()
  endtime = playmin * 60

  nowtime_dt = datetime.datetime.now()
  starttime_dt = nowtime_dt.strftime("%X")
  endtime_dt = nowtime_dt + datetime.timedelta(minutes = playmin)
  endtime_dt = endtime_dt.strftime("%X")

  print("現在の時刻: " + str(starttime_dt))
  print("終わる時刻: " + str(endtime_dt))

  i = 0

  while (thisTime - startTime) < endtime:
    thisTime = time.time()
    i += 1
    x, _ = pg.position()

    if x != pos1[0] and x != pos2[0]:
      print("============================================")
      print("カーソル移動をしたためプログラムを中止します")
      print(f"クリックした回数は{i}回でした")
      time.sleep(3)
      sys.exit(1)

    if i % 5 == 0:
      pg.click(1250, 850)
      continue

    pg.click(1350, 800)
  
  print(f"クリックした回数は{i} 回でした")

def start():
  print("使用したい方式を番号で選んで下さい")
  print("クリック回数指定方式 : 1\nマクロ使用時間方式 : 2")
  def_index = int(input())
  if def_index == 1:
    print("クリック回数指定方式で始めます\n")
    click_count()
  elif def_index == 2:
    print("マクロ使用時間方式で始めます\n")
    click_time()

start()