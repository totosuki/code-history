import pyautogui
import time

#英霊クエストの回数
count = 28

#バトル時間
battleTime = 15

normalPos = [1330,460]
hardPos = [1310,720]
battlePos = [1200,675]
disassemblyPos = [1100,530]
okPos = [1200,530]

#ウィンドウ選択用
pyautogui.click(1300,500)

for i in range(count):
    pyautogui.click(normalPos[0],normalPos[1],interval = 0.5,button = "left")
    pyautogui.click(hardPos[0],hardPos[1],interval = 0.5,button = "left")
    pyautogui.click(battlePos[0],battlePos[1],interval=0.5,button="left")
    pyautogui.click(disassemblyPos[0],disassemblyPos[1],interval = 0.5,button="left")
    pyautogui.click(okPos[0],okPos[1],interval=0.5,button="left")
    pyautogui.click(battlePos[0],battlePos[1],interval=0.5,button="left")
    time.sleep(battleTime)
