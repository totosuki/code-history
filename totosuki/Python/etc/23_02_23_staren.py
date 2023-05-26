#LINEスタンプ連打

import pyautogui

count = 1000 #スタンプ連打の個数
speed = 0.05 #スタンプ連打の速さ(秒)

homePos = [1410, 875]
stanpPos = [725, 310]

pyautogui.click(homePos[0], homePos[1], interval = 1, button = "left")
pyautogui.moveTo(725,310)
for i in range(count):
  pyautogui.click(stanpPos[0], stanpPos[1], interval = 0, button = "left")