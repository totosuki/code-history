import pyautogui as gui
import time as t

### 超危険!!! pyautogui config ###
gui.PAUSE = False
gui.DARWIN_CATCH_UP_TIME = 0

# 連打する位置
POS = (1150, 240)
# 回数
COUNT = 3

t.sleep(5)

for _ in range(COUNT):
    gui.click(POS)