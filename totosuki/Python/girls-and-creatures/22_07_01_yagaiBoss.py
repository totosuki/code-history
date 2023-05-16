import pyautogui
import time
import numpy as np

bossPos = np.array([[1340,350],[1340,475],[1340,600],[1340,725]])

lv = 0

multi = {
    "weekday" : (1250,300),
    "weekend" : (1370,380)
}

preTreatmentPos = {
    "multi" : (1250,300),
    "zinyou" : (1320,350),
    "myTeam" : (1340,570),
    "party2" : (1100,330),
    "use" : (1180,670),
    "ok" : (1180,530),
    "back1" : (1380,240),
    "back2" : (1380,240),
    "bossIcon" : (1300,750)
}

postTreatmentPos = {
    "back1" : (1380,170),
    "multi" : (1250,300),
    "zinyou" : (1320,350),
    "myTeam" : (1340,570),
    "use" : (1180,670),
    "ok" : (1180,530),
    "back2" : (1380,240),
    "back3" : (1380,240)
}

preValues = np.array(list(preTreatmentPos.values()))
postValues = np.array(list(postTreatmentPos.values()))

pyautogui.moveTo(1370,380,1)

#初期化
pyautogui.click(1180,530)

for i in range(len(preValues)):
    pyautogui.click(preValues[i,0],preValues[i,1], interval = 1, button = "left")

for i in range(4):
    lv += 1
    print(str(lv * 10) + "lv")
    pyautogui.click(bossPos[i,0],bossPos[i,1],button = "left")
    time.sleep(10)
    
for i in range(3):
    pyautogui.mouseDown(bossPos[3,0],bossPos[3,1],button = "left")
    pyautogui.moveTo(bossPos[1,0],bossPos[1,1],0.5)
    pyautogui.mouseUp(bossPos[1,0],bossPos[1,1],button = "left")

    pyautogui.click(bossPos[2,0],bossPos[2,1],button = "left")
    lv += 1
    print(str(lv * 10) + "Lv")
    time.sleep(10)

    pyautogui.click(bossPos[3,0],bossPos[3,1],button = "left")
    lv += 1
    print(str(lv * 10) + "Lv")
    time.sleep(10)

for i in range(len(postValues)):
    pyautogui.click(postValues[i,0],postValues[i,1],interval = 0.5, button = "left")
