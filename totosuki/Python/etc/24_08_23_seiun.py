import pyautogui as pag
import time

class Axis:
  def __init__(self, x: int, y: int):
    self.x = x
    self.y = y

min = Axis(0, 0)
max = Axis(1440, 900)
update = Axis(980, 730)
update_yes = Axis(900, 585)
pack1 = Axis(960, 600)
pack2 = Axis(1040, 660)
pack3 = Axis(1120, 600)
pack4 = Axis(1200, 660)
buydiff = Axis(90, -145)
choose = Axis(1035, 720)
itemlast = Axis(1350, 400)
sell = Axis(1030, 675)

positions = {
  update,
  update_yes,
  pack1,
  pack2,
  pack3,
  pack4,
  buydiff,
  choose,
  itemlast,
  sell
}

def check_stop(x, y):
  pos = Axis(x, y)
  if pos not in positions:
    exit()

def sleep_exec(function, waittime = 1):
  time.sleep(waittime)
  check_stop(*pag.position())
  function()

def main(N):
  pag.click(update.x, update.y)
  for _ in range(N):
    sleep_exec(pag.click(update.x, update.y))
    sleep_exec(pag.click(update_yes.x, update_yes.y), 0.5)
    sleep_exec(pag.click(pack1.x, pack1.y))
    sleep_exec(pag.click(pack1.x + buydiff.x, pack1.y + buydiff.y))
    sleep_exec(pag.click(choose.x, choose.y), 1.5)
    sleep_exec(pag.click(itemlast.x, itemlast.y))
    sleep_exec(pag.click(sell.x, sell.y), 0.5)

main()