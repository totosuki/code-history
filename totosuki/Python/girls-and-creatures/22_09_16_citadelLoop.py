import pyautogui
import time
import datetime

bossPos = [1175,725]
citadePos = [1025,850]

#単位は分(min)で
min = 180
endTime = min * 60

pyautogui.click(1175,400,1,1,"left")

startTime = time.time()
thisTime = time.time()

nowTime_dt = datetime.datetime.now()
startTime_dt = nowTime_dt.strftime("%X")
endTime_dt = nowTime_dt + datetime.timedelta(minutes = min)
endTime_dt = endTime_dt.strftime("%X")

print("現在の時刻: " + str(startTime_dt))
print("終わる時刻: " + str(endTime_dt))

while ((thisTime - startTime) < endTime):
    pyautogui.click(citadePos[0],citadePos[1],2,0,"left")
    time.sleep(2)
    pyautogui.click(bossPos[0],bossPos[1],1,0,"left")
    thisTime = time.time()